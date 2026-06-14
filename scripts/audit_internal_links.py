#!/usr/bin/env python3
"""Audit internal link graph of the built site.

Produces by default:
  - reports/seo/internal-link-graph-YYYY-MM-DD.csv
  - reports/seo/internal-link-graph-YYYY-MM-DD.md

Usage:
    python3 scripts/audit_internal_links.py [--site-dir _site] [--repo-dir .]
    python3 scripts/audit_internal_links.py --stdout > /tmp/links.md
    python3 scripts/audit_internal_links.py --output-dir /tmp/reports
"""

from __future__ import annotations

import argparse
import csv
import posixpath
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

LINK_HREF_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
META_ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)

EXPECTED_SOURCE_PREFIXES = (
    ".well-known/",
    "agent-skills/",
    "docs/",
    "reports/",
    "research/skill-hub/",
)
EXPECTED_SOURCE_DOCS = {
    "AGENTS/index.html",
    "ARCHITECTURE/index.html",
    "CITATION/index.html",
    "DESIGN-SYSTEM/index.html",
    "PROJECT_MAP/index.html",
}
EXPECTED_NOINDEX_PREFIXES = (
    "agent-skills/",
    "atlas/",
    "atlas/research-notes/",
    "docs/",
    "legal/",
    "news/",
    "notes/",
    "radar/",
    "reports/",
    "research/skill-hub/",
    "scenarios/",
    "search/",
)


def is_external(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}


def normalize_local_path(link: str, site_dir: Path, current_dir: Path) -> Path | None:
    if not link or link.startswith("#") or is_external(url=link):
        return None

    parsed = urlparse(link)
    local = parsed.path
    if not local:
        return None
    if local == "/":
        return site_dir / "index.html"

    if local.startswith("/"):
        target = site_dir / local.lstrip("/")
    else:
        normalized = posixpath.normpath(local)
        target = current_dir / normalized

    if target.is_dir():
        target = target / "index.html"
    elif not target.suffix:
        pretty_target = target / "index.html"
        if pretty_target.exists():
            target = pretty_target
        else:
            target = target.with_suffix(".html")
    return target


def safe_rel(path: Path, site_dir: Path) -> str | None:
    try:
        return path.relative_to(site_dir).as_posix()
    except ValueError:
        return None


def classify_orphan(rel: str, info: dict) -> str:
    if rel == "404.html":
        return "expected_utility_page"
    if info["is_noindex"]:
        return "expected_noindex_page"
    if rel in EXPECTED_SOURCE_DOCS or rel.startswith(EXPECTED_SOURCE_PREFIXES):
        return "expected_generated_or_source_page"
    return "actionable_review"


def classify_broken_link(src: str, link: str) -> str:
    parsed = urlparse(link)
    suffix = Path(parsed.path).suffix.lower()
    if suffix and suffix != ".html":
        return "actionable_missing_static_artifact"
    if src in EXPECTED_SOURCE_DOCS or src.startswith(EXPECTED_SOURCE_PREFIXES):
        return "expected_source_surface_noise"
    return "actionable_review"


def classify_indexable_to_noindex(src: str, target_rel: str) -> str:
    if target_rel.startswith(EXPECTED_NOINDEX_PREFIXES):
        return "expected_noindex_reference"
    if target_rel in EXPECTED_SOURCE_DOCS or target_rel.startswith(EXPECTED_SOURCE_PREFIXES):
        return "expected_generated_or_source_page"
    if src.startswith(EXPECTED_SOURCE_PREFIXES):
        return "expected_source_surface_noise"
    return "actionable_review"


def strip_non_link_markup(content: str) -> str:
    no_scripts = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r"<style[^>]*>.*?</style>", "", no_scripts, flags=re.IGNORECASE | re.DOTALL)


def extract_page_info(html_path: Path) -> dict:
    content = html_path.read_text(encoding="utf-8", errors="ignore")
    link_content = strip_non_link_markup(content)
    robots_match = META_ROBOTS_RE.search(content)
    robots = robots_match.group(1).lower() if robots_match else ""
    title_match = TITLE_RE.search(content)
    title = title_match.group(1).strip() if title_match else ""
    return {
        "title": title,
        "is_noindex": "noindex" in robots,
        "links": LINK_HREF_RE.findall(link_content),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--output-dir", default=None, help="Directory for report files (default: reports/seo)")
    parser.add_argument("--stdout", action="store_true", help="Print Markdown report to stdout and skip file writes")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    repo_dir = Path(args.repo_dir).resolve()
    if not site_dir.is_dir():
        print(f"Missing site directory: {site_dir}", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if args.stdout:
        csv_path = None
        md_path = None
    else:
        out_dir = Path(args.output_dir).resolve() if args.output_dir else repo_dir / "reports" / "seo"
        out_dir.mkdir(parents=True, exist_ok=True)
        csv_path = out_dir / f"internal-link-graph-{today}.csv"
        md_path = out_dir / f"internal-link-graph-{today}.md"

    html_files = sorted(site_dir.rglob("*.html"))

    inbound: dict[str, set[str]] = defaultdict(set)
    outbound: dict[str, list[str]] = defaultdict(list)
    broken: dict[str, list[str]] = defaultdict(list)
    page_info: dict[str, dict] = {}

    for html_path in html_files:
        rel = html_path.relative_to(site_dir).as_posix()
        info = extract_page_info(html_path)
        page_info[rel] = info

        for link in info["links"]:
            target = normalize_local_path(link, site_dir, html_path.parent)
            if target is None:
                continue
            if not target.exists():
                broken[rel].append(link)
            else:
                target_rel = safe_rel(target, site_dir)
                if target_rel is None:
                    broken[rel].append(link)
                    continue
                outbound[rel].append(link)
                inbound[target_rel].add(rel)

    # Build CSV rows
    rows: list[dict] = []
    for rel in sorted(page_info.keys()):
        info = page_info[rel]
        orphan_classification = ""
        if len(inbound[rel]) == 0 and rel != "index.html":
            orphan_classification = classify_orphan(rel, info)
        rows.append({
            "page": rel,
            "title": info["title"],
            "noindex": "yes" if info["is_noindex"] else "no",
            "inbound_count": len(inbound[rel]),
            "outbound_count": len(outbound[rel]),
            "broken_count": len(broken[rel]),
            "orphan_classification": orphan_classification,
            "inbound_from": " | ".join(sorted(inbound[rel]))[:200],
            "broken_links": " | ".join(broken[rel])[:200],
        })

    if csv_path is not None:
        with open(csv_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=[
                "page", "title", "noindex", "inbound_count", "outbound_count",
                "broken_count", "orphan_classification", "inbound_from", "broken_links",
            ], lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    # Orphan pages (no inbound from other content pages)
    orphans = [r for r in rows if r["inbound_count"] == 0 and r["page"] != "index.html"]
    actionable_orphans = [r for r in orphans if r["orphan_classification"] == "actionable_review"]
    expected_orphans = [r for r in orphans if r["orphan_classification"] != "actionable_review"]
    # Hub pages (high inbound)
    hubs = sorted(rows, key=lambda x: x["inbound_count"], reverse=True)[:15]
    # Indexable pages linking to noindex pages
    indexable_to_noindex: list[tuple[str, str, str, str]] = []
    for rel in sorted(page_info.keys()):
        if page_info[rel]["is_noindex"]:
            continue
        for link in outbound[rel]:
            target = normalize_local_path(link, site_dir, site_dir / Path(rel).parent)
            if target and target.exists():
                target_rel = safe_rel(target, site_dir)
                if target_rel in page_info and page_info[target_rel]["is_noindex"]:
                    classification = classify_indexable_to_noindex(rel, target_rel)
                    indexable_to_noindex.append((rel, link, target_rel, classification))

    actionable_noindex_links = [
        item for item in indexable_to_noindex if item[3] == "actionable_review"
    ]
    expected_noindex_links = [
        item for item in indexable_to_noindex if item[3] != "actionable_review"
    ]

    broken_items: list[tuple[str, str, str]] = []
    for src, links in broken.items():
        for link in links:
            broken_items.append((src, link, classify_broken_link(src, link)))
    actionable_broken = [item for item in broken_items if item[2].startswith("actionable")]
    expected_broken = [item for item in broken_items if not item[2].startswith("actionable")]

    md_lines = [
        f"# Internal Link Graph Report",
        f"",
        f"**Date:** {today}",
        f"**Pages scanned:** {len(rows)}",
        f"",
        f"## Summary",
        f"- **Orphan pages:** {len(orphans)}",
        f"  - Actionable review: {len(actionable_orphans)}",
        f"  - Expected noindex/generated/source pages: {len(expected_orphans)}",
        f"- **Pages with broken links:** {sum(1 for r in rows if r['broken_count'] > 0)}",
        f"  - Actionable broken link records: {len(actionable_broken)}",
        f"  - Expected source-surface noise records: {len(expected_broken)}",
        f"- **Indexable pages linking to noindex:** {len(indexable_to_noindex)}",
        f"  - Actionable review: {len(actionable_noindex_links)}",
        f"  - Expected noindex references: {len(expected_noindex_links)}",
        f"",
        f"## Actionable Orphan Pages",
        f"",
    ]
    if actionable_orphans:
        for o in actionable_orphans:
            md_lines.append(f"- `{o['page']}` — {o['title']}")
    else:
        md_lines.append("No actionable orphan pages detected.")

    md_lines.extend([
        "",
        "## Expected Orphan Noise",
        "",
        "Generated, noindex, source-document, or utility pages can be intentionally outside the normal human navigation graph.",
        "",
    ])
    if expected_orphans:
        for o in expected_orphans[:50]:
            md_lines.append(f"- `{o['page']}` — {o['orphan_classification']} — {o['title']}")
        if len(expected_orphans) > 50:
            md_lines.append(f"- ... and {len(expected_orphans) - 50} more")
    else:
        md_lines.append("No expected orphan-noise pages detected.")

    md_lines.extend([
        "",
        "## Top Hub Pages (most inbound links)",
        "",
        "| Page | Title | Inbound | Outbound |",
        "|------|-------|---------|----------|",
    ])
    for h in hubs:
        md_lines.append(f"| `{h['page']}` | {h['title'][:50]} | {h['inbound_count']} | {h['outbound_count']} |")

    md_lines.extend([
        "",
        "## Broken Local Links",
        "",
    ])
    broken_found = [r for r in rows if r["broken_count"] > 0]
    if actionable_broken:
        for src, link, classification in actionable_broken[:50]:
            md_lines.append(f"- `{src}` → `{link}` — {classification}")
        if len(actionable_broken) > 50:
            md_lines.append(f"- ... and {len(actionable_broken) - 50} more")
    else:
        md_lines.append("No actionable broken local links detected.")

    if expected_broken:
        md_lines.extend([
            "",
            "Expected source-surface broken-link noise:",
            "",
        ])
        for src, link, classification in expected_broken[:30]:
            md_lines.append(f"- `{src}` → `{link}` — {classification}")
        if len(expected_broken) > 30:
            md_lines.append(f"- ... and {len(expected_broken) - 30} more")

    md_lines.extend([
        "",
        "## Indexable Pages Linking to Noindex Pages",
        "",
    ])
    if actionable_noindex_links:
        for src, link, target, classification in actionable_noindex_links[:30]:
            md_lines.append(f"- `{src}` → `{link}` (`{target}`) — {classification}")
        if len(actionable_noindex_links) > 30:
            md_lines.append(f"- ... and {len(actionable_noindex_links) - 30} more")
    else:
        md_lines.append("No actionable indexable→noindex links detected.")

    if expected_noindex_links:
        md_lines.extend([
            "",
            "Expected indexable→noindex references:",
            "",
        ])
        for src, link, target, classification in expected_noindex_links[:30]:
            md_lines.append(f"- `{src}` → `{link}` (`{target}`) — {classification}")
        if len(expected_noindex_links) > 30:
            md_lines.append(f"- ... and {len(expected_noindex_links) - 30} more")

    md_lines.extend([
        "",
        "## Recommendations",
        "",
        "1. Review actionable orphan pages and add links from related hubs or mark the surface as intentionally generated/noindex.",
        "2. Fix actionable broken local links. Non-HTML artifacts are valid local links when the target file exists.",
        "3. Review actionable indexable→noindex links and keep expected review-candidate, legal, report, and generated references classified.",
        "4. Strengthen hub pages (index pages, atlas index, skill-hub index) with more outbound links to verified content.",
    ])

    if args.stdout:
        print("\n".join(md_lines))
    elif md_path is not None:
        md_path.write_text("\n".join(md_lines), encoding="utf-8")

    summary_stream = sys.stderr if args.stdout else sys.stdout
    print(f"Link graph audit complete: {len(rows)} pages", file=summary_stream)
    print(f"  CSV: {csv_path}", file=summary_stream)
    print(f"  MD:  {md_path}", file=summary_stream)
    print(f"  Orphans: {len(orphans)}", file=summary_stream)
    print(f"    Actionable: {len(actionable_orphans)}", file=summary_stream)
    print(f"    Expected/noise: {len(expected_orphans)}", file=summary_stream)
    print(f"  Broken pages: {len(broken_found)}", file=summary_stream)
    print(f"    Actionable records: {len(actionable_broken)}", file=summary_stream)
    print(f"    Expected/noise records: {len(expected_broken)}", file=summary_stream)
    print(f"  Indexable→noindex: {len(indexable_to_noindex)}", file=summary_stream)
    print(f"    Actionable: {len(actionable_noindex_links)}", file=summary_stream)
    print(f"    Expected/noise: {len(expected_noindex_links)}", file=summary_stream)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
