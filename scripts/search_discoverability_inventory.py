#!/usr/bin/env python3
"""Build a source-level search discoverability inventory for the whole site.

The inventory answers four practical questions for every public Markdown route:
1. Is the page allowed to be indexed?
2. Is it mature enough to be indexed?
3. Is its metadata complete enough to publish?
4. Does it collide with another route or title?

Default outputs:
  reports/seo/search-discoverability.csv
  reports/seo/search-discoverability.md

The report itself is excluded from the public site by _config.yml.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


INTERNAL_PREFIXES = (
    ".git/",
    ".github/",
    "_includes/",
    "_layouts/",
    "_plugins/",
    "agent-skills/",
    "docs/templates/",
    "scripts/",
    "tests/",
    "vendor/",
    "reports/",
)

GOVERNED_ROUTE_PREFIXES = (
    "/atlas/",
    "/labs/",
    "/skill-hub/",
    "/scenarios/",
    "/research/",
)

DRAFT_STATUSES = {"draft", "needs_verification", "working", "experimental"}


@dataclass
class PageRecord:
    source_path: str
    route: str
    title: str
    description: str
    status: str
    verified: Any
    robots: str
    sitemap: Any
    section: str
    search_intent: str
    governed: bool
    indexable: bool
    classification: str
    reasons: list[str]
    critical: bool = False


def load_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    return data if isinstance(data, dict) else {}


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    raw = text[4:end]
    data = yaml.safe_load(raw)
    return data if isinstance(data, dict) else {}


def collection_type(rel: str, config: dict) -> str:
    if not rel.startswith("_"):
        return "pages"
    first = rel.split("/", 1)[0]
    label = first[1:]
    if label in (config.get("collections") or {}):
        return label
    if label == "posts":
        return "posts"
    return "pages"


def apply_defaults(rel: str, fm: dict, config: dict) -> dict:
    merged: dict = {}
    ctype = collection_type(rel, config)
    for item in config.get("defaults") or []:
        if not isinstance(item, dict):
            continue
        scope = item.get("scope") or {}
        values = item.get("values") or {}
        scope_path = str(scope.get("path") or "").strip("/")
        scope_type = scope.get("type")
        rel_norm = rel.strip("/")
        path_match = not scope_path or rel_norm == scope_path or rel_norm.startswith(scope_path + "/")
        type_match = not scope_type or scope_type == ctype
        if path_match and type_match and isinstance(values, dict):
            merged.update(values)
    merged.update(fm)
    return merged


def slug_from_path(rel: str) -> str:
    stem = Path(rel).stem
    return stem.lower().replace("_", "-")


def derive_route(rel: str, fm: dict, config: dict) -> str:
    permalink = fm.get("permalink")
    if permalink:
        route = str(permalink)
        if not route.startswith("/"):
            route = "/" + route
        return route

    ctype = collection_type(rel, config)
    collection_cfg = (config.get("collections") or {}).get(ctype) if ctype != "pages" else None
    if isinstance(collection_cfg, dict) and collection_cfg.get("permalink"):
        pattern = str(collection_cfg["permalink"])
        slug = slug_from_path(rel)
        path_inside = rel.split("/", 1)[1] if "/" in rel else Path(rel).name
        path_no_ext = str(Path(path_inside).with_suffix("")).replace("\\", "/")
        route = pattern.replace(":slug", slug).replace(":path", path_no_ext)
        if not route.startswith("/"):
            route = "/" + route
        return route

    path = Path(rel)
    if path.name == "index.md":
        parent = path.parent.as_posix()
        return "/" if parent == "." else f"/{parent.strip('/')}/"
    if path.name == "404.md":
        return "/404.html"
    return f"/{path.with_suffix('').as_posix().strip('/')}/"


def section_from_route(route: str) -> str:
    parts = [p for p in route.split("/") if p]
    return parts[0] if parts else "home"


def is_truthy_false(value: Any) -> bool:
    return value is False or (isinstance(value, str) and value.strip().lower() in {"false", "no"})


def classify(rel: str, route: str, fm: dict) -> tuple[str, list[str], bool, bool, bool]:
    title = str(fm.get("title") or "").strip()
    description = str(fm.get("description") or "").strip()
    status = str(fm.get("status") or "").strip().lower()
    verified = fm.get("verified")
    robots = str(fm.get("robots") or "index,follow").lower()
    sitemap = fm.get("sitemap", True)

    noindex = "noindex" in robots
    sitemap_enabled = not is_truthy_false(sitemap)
    indexable = not noindex and sitemap_enabled
    governed = route.startswith(GOVERNED_ROUTE_PREFIXES) or "verified" in fm or "status" in fm
    mature = verified is True and status == "reviewed"
    explicitly_draft = verified is False or status in DRAFT_STATUSES

    reasons: list[str] = []
    critical = False

    if noindex and sitemap_enabled:
        reasons.append("noindex page is still sitemap-enabled")
        critical = True

    if governed:
        if mature and indexable:
            classification = "INDEX"
        elif mature and not indexable:
            classification = "REVIEW_TO_INDEX"
            reasons.append("reviewed+verified page is still hidden from search")
        elif not mature and indexable:
            classification = "BLOCK_INDEX"
            reasons.append("governed page is indexable before reviewed+verified gate")
            critical = True
        else:
            classification = "KEEP_NOINDEX"
            if not explicitly_draft and not mature:
                reasons.append("publication state is incomplete")
    else:
        classification = "KEEP_NOINDEX" if not indexable else "INDEX"

    if indexable and not title:
        reasons.append("missing title")
        classification = "REVIEW_METADATA" if classification == "INDEX" else classification
        critical = True
    if indexable and not description:
        reasons.append("missing description")
        classification = "REVIEW_METADATA" if classification == "INDEX" else classification

    explicit_action = str(fm.get("search_action") or "").strip().lower()
    if explicit_action in {"remove", "merge", "index", "keep_noindex"}:
        classification = explicit_action.upper()
        reasons.append("explicit search_action override")

    return classification, reasons, critical, governed, indexable


def iter_markdown(repo: Path, config: dict):
    excluded = [str(x).rstrip("/") for x in config.get("exclude") or []]
    for path in sorted(repo.rglob("*.md")):
        rel = path.relative_to(repo).as_posix()
        if rel.startswith(INTERNAL_PREFIXES):
            continue
        if any(rel == item or rel.startswith(item + "/") for item in excluded):
            continue
        fm = parse_frontmatter(path)
        if fm is None:
            continue
        yield path, rel, apply_defaults(rel, fm, config)


def build_records(repo: Path) -> list[PageRecord]:
    config = load_yaml(repo / "_config.yml")
    records: list[PageRecord] = []

    for _path, rel, fm in iter_markdown(repo, config):
        route = derive_route(rel, fm, config)
        classification, reasons, critical, governed, indexable = classify(rel, route, fm)
        title = str(fm.get("title") or "").strip()
        records.append(
            PageRecord(
                source_path=rel,
                route=route,
                title=title,
                description=str(fm.get("description") or "").strip(),
                status=str(fm.get("status") or "").strip(),
                verified=fm.get("verified", ""),
                robots=str(fm.get("robots") or "index,follow"),
                sitemap=fm.get("sitemap", True),
                section=section_from_route(route),
                search_intent=str(fm.get("search_intent") or title).strip(),
                governed=governed,
                indexable=indexable,
                classification=classification,
                reasons=reasons,
                critical=critical,
            )
        )

    route_map: dict[str, list[PageRecord]] = defaultdict(list)
    title_map: dict[str, list[PageRecord]] = defaultdict(list)
    for record in records:
        route_map[record.route].append(record)
        if record.title and record.indexable:
            title_map[re.sub(r"\s+", " ", record.title.lower()).strip()].append(record)

    for route, items in route_map.items():
        if len(items) > 1:
            for item in items:
                item.classification = "MERGE_OR_FIX_ROUTE"
                item.reasons.append(f"duplicate route used by {len(items)} source files")
                item.critical = True

    for _title, items in title_map.items():
        routes = {item.route for item in items}
        if len(routes) > 1:
            for item in items:
                if item.classification == "INDEX":
                    item.classification = "REVIEW_DUPLICATE_TITLE"
                item.reasons.append("same title used by another indexable route")

    return records


def write_csv(path: Path, records: list[PageRecord]) -> None:
    fields = [
        "source_path", "route", "section", "classification", "indexable", "governed",
        "status", "verified", "robots", "sitemap", "title", "description",
        "search_intent", "critical", "reasons",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for record in records:
            row = record.__dict__.copy()
            row["reasons"] = "; ".join(record.reasons)
            writer.writerow({field: row.get(field, "") for field in fields})


def write_markdown(path: Path, records: list[PageRecord]) -> None:
    counts = Counter(r.classification for r in records)
    sections = Counter(r.section for r in records)
    critical = [r for r in records if r.critical]
    review = [r for r in records if r.classification.startswith("REVIEW") or r.classification.startswith("MERGE") or r.classification == "BLOCK_INDEX"]

    lines = [
        "# Search Discoverability Inventory",
        "",
        "Generated from source front matter and `_config.yml` defaults. This report is operational metadata, not public content.",
        "",
        "## Summary",
        "",
        f"- Routes scanned: **{len(records)}**",
        f"- Critical policy conflicts: **{len(critical)}**",
        f"- Review queue: **{len(review)}**",
        "",
        "### Classification",
        "",
    ]
    for name, count in sorted(counts.items()):
        lines.append(f"- **{name}:** {count}")

    lines.extend(["", "### Sections", ""])
    for name, count in sorted(sections.items(), key=lambda item: (-item[1], item[0])):
        lines.append(f"- **/{name}/:** {count}")

    lines.extend([
        "",
        "## Critical conflicts",
        "",
        "| Route | Source | Classification | Reason |",
        "|---|---|---|---|",
    ])
    if critical:
        for record in critical:
            lines.append(f"| `{record.route}` | `{record.source_path}` | {record.classification} | {'; '.join(record.reasons)} |")
    else:
        lines.append("| — | — | — | No critical conflicts |")

    lines.extend([
        "",
        "## Publication review queue",
        "",
        "| Route | Classification | Status | Verified | Search intent |",
        "|---|---|---|---|---|",
    ])
    if review:
        for record in review:
            lines.append(
                f"| `{record.route}` | {record.classification} | {record.status or '—'} | "
                f"{record.verified if record.verified != '' else '—'} | {record.search_intent or record.title or '—'} |"
            )
    else:
        lines.append("| — | — | — | — | No pages currently require publication review |")

    lines.extend([
        "",
        "## Policy",
        "",
        "- `INDEX`: route is allowed to be discovered.",
        "- `KEEP_NOINDEX`: intentional working/private/search-noise surface.",
        "- `REVIEW_TO_INDEX`: reviewed+verified content is still hidden and should be consciously promoted or downgraded.",
        "- `BLOCK_INDEX`: immature governed content escaped the publication gate. CI must fail.",
        "- `REVIEW_METADATA`: indexable route lacks required search metadata.",
        "- `REVIEW_DUPLICATE_TITLE`: two indexable routes compete under the same title.",
        "- `MERGE_OR_FIX_ROUTE`: more than one source resolves to the same route. CI must fail.",
        "",
    ])
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".")
    parser.add_argument("--output-dir", default="reports/seo")
    parser.add_argument("--fail-on-critical", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo_dir).resolve()
    records = build_records(repo)
    output = repo / args.output_dir
    csv_path = output / "search-discoverability.csv"
    md_path = output / "search-discoverability.md"
    write_csv(csv_path, records)
    write_markdown(md_path, records)

    critical = [r for r in records if r.critical]
    counts = Counter(r.classification for r in records)
    print(f"Search discoverability inventory: {len(records)} routes")
    for name, count in sorted(counts.items()):
        print(f"  {name}: {count}")
    print(f"  Critical: {len(critical)}")
    print(f"  CSV: {csv_path}")
    print(f"  MD:  {md_path}")

    if critical and args.fail_on_critical:
        for record in critical[:30]:
            print(f"  - {record.route}: {record.classification}: {'; '.join(record.reasons)}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
