#!/usr/bin/env python3
"""Generate a report-only content inventory for future site audits.

The inventory uses built HTML as the audit surface and merges source
front matter when a source Markdown page can be resolved.

Usage:
    python3 scripts/content_inventory_report.py --site-dir _site --summary
    python3 scripts/content_inventory_report.py --site-dir _site --output /tmp/content-inventory.json
    python3 scripts/content_inventory_report.py --site-dir _site --output /tmp/content-inventory.csv --format csv
"""

from __future__ import annotations

import argparse
import csv
import html
import json
import posixpath
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)


REPO_URL = "https://dkharlanau.github.io"
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
SCRIPT_LD_RE = re.compile(
    r'<script\s+type=["\']application/ld\+json["\']\s*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
LINK_HREF_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>', re.IGNORECASE | re.DOTALL)
VISIBLE_TEXT_RE = re.compile(r">([^<]{2,})<", re.DOTALL)

EXCLUDED_SOURCE_PREFIXES = (
    ".git/",
    ".pytest_cache/",
    ".ruby-lsp/",
    "_site/",
    "vendor/",
    "node_modules/",
    "docs/templates/",
    "scripts/",
    "tests/",
)
COLLECTION_URL_PREFIXES = {
    "_notes": "notes",
    "_blog": "blog",
    "_radar": "radar",
    "_news": "news",
}


def pick(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    return html.unescape(re.sub(r"<[^>]+>", "", match.group(1))).strip()


def extract_visible_text(content: str) -> str:
    no_scripts = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.IGNORECASE | re.DOTALL)
    no_styles = re.sub(r"<style[^>]*>.*?</style>", "", no_scripts, flags=re.IGNORECASE | re.DOTALL)
    parts = VISIBLE_TEXT_RE.findall(no_styles)
    return " ".join(part.strip() for part in parts if part.strip())


def strip_non_link_markup(content: str) -> str:
    no_scripts = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.IGNORECASE | re.DOTALL)
    return re.sub(r"<style[^>]*>.*?</style>", "", no_scripts, flags=re.IGNORECASE | re.DOTALL)


def parse_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}, text
    try:
        frontmatter = yaml.safe_load(match.group(1)) or {}
    except yaml.YAMLError:
        frontmatter = {}
    return frontmatter, match.group(2)


def should_skip_source(path: Path, repo_dir: Path) -> bool:
    rel = path.relative_to(repo_dir).as_posix()
    if rel.startswith(EXCLUDED_SOURCE_PREFIXES):
        return True
    if rel.startswith("Basic_LinkedInDataExport_"):
        return True
    return False


def normalize_url_path(path: str) -> str:
    if not path:
        return "/"
    if not path.startswith("/"):
        path = f"/{path}"
    return path if path.endswith("/") or Path(path).suffix else f"{path}/"


def source_url_path(rel: str, frontmatter: dict) -> str:
    permalink = frontmatter.get("permalink")
    if permalink:
        return normalize_url_path(str(permalink))

    path = Path(rel)
    parts = path.parts
    if parts and parts[0] in COLLECTION_URL_PREFIXES:
        prefix = COLLECTION_URL_PREFIXES[parts[0]]
        return f"/{prefix}/{path.stem}/"

    if path.name == "index.md":
        parent = path.parent.as_posix()
        return "/" if parent == "." else f"/{parent}/"

    if path.name == "README.md":
        parent = path.parent.as_posix()
        if parent == ".":
            return "/README/"
        return f"/{parent}/"

    return f"/{path.with_suffix('').as_posix()}/"


def built_url_path(rel: str) -> str:
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return f"/{rel[:-len('/index.html')]}/"
    return f"/{rel}"


def is_external(url: str) -> bool:
    return urlparse(url).scheme in {"http", "https", "mailto", "tel", "data", "javascript"}


def normalize_local_path(link: str, site_dir: Path, current_dir: Path) -> Path | None:
    if not link or link.startswith("#") or is_external(link):
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
        target = current_dir / posixpath.normpath(local)
    if target.is_dir():
        return target / "index.html"
    if target.suffix:
        return target
    pretty_target = target / "index.html"
    return pretty_target if pretty_target.exists() else target.with_suffix(".html")


def schema_types(content: str) -> list[str]:
    found: list[str] = []
    for block in SCRIPT_LD_RE.findall(content):
        try:
            data = json.loads(html.unescape(block))
        except json.JSONDecodeError:
            continue
        items = data if isinstance(data, list) else [data]
        for item in items:
            if not isinstance(item, dict):
                continue
            value = item.get("@type")
            if isinstance(value, str):
                found.append(value)
            elif isinstance(value, list):
                found.extend(str(v) for v in value)
    return sorted(set(found))


def build_source_map(repo_dir: Path) -> dict[str, dict]:
    source_map: dict[str, dict] = {}
    for md_path in sorted(repo_dir.rglob("*.md")):
        if should_skip_source(md_path, repo_dir):
            continue
        rel = md_path.relative_to(repo_dir).as_posix()
        frontmatter, body = parse_frontmatter(md_path)
        url_path = source_url_path(rel, frontmatter)
        source_map[url_path] = {
            "source_path": rel,
            "frontmatter_title": str(frontmatter.get("title", "") or ""),
            "frontmatter_description": str(frontmatter.get("description", "") or ""),
            "status": str(frontmatter.get("status", "") or ""),
            "verified": frontmatter.get("verified", ""),
            "sitemap": frontmatter.get("sitemap", ""),
            "source_word_count": len(re.findall(r"\b\w+\b", body)),
        }
    return source_map


def build_inbound_map(site_dir: Path) -> dict[str, set[str]]:
    inbound: dict[str, set[str]] = defaultdict(set)
    html_files = sorted(site_dir.rglob("*.html"))
    for html_path in html_files:
        rel = html_path.relative_to(site_dir).as_posix()
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        for link in LINK_HREF_RE.findall(strip_non_link_markup(content)):
            target = normalize_local_path(link, site_dir, html_path.parent)
            if target is None or not target.exists():
                continue
            try:
                target_rel = target.relative_to(site_dir).as_posix()
            except ValueError:
                continue
            if target_rel.endswith(".html"):
                inbound[target_rel].add(rel)
    return inbound


def section_for(rel: str, url_path: str) -> str:
    if url_path.startswith("/.well-known/agent-skills/"):
        return "agent-skill-discovery"
    clean = rel.strip("/")
    if not clean or clean == "index.html":
        return "home"
    return clean.split("/", 1)[0].replace("_", "-")


def recommended_action(row: dict) -> str:
    robots = str(row.get("robots", "")).lower()
    is_noindex = "noindex" in robots
    if not row.get("title"):
        return "add_title"
    if row.get("status") in {"draft", "needs_verification", "skeleton"} or row.get("verified") is False:
        if not is_noindex and row.get("sitemap") is not False:
            return "review_indexing_policy"
        return "keep_out_of_index_until_reviewed"
    if not is_noindex and row.get("word_count", 0) < 150:
        return "review_thin_indexable_page"
    if not is_noindex and row.get("inlink_count", 0) == 0 and row.get("url_path") != "/":
        return "review_orphan_indexable_page"
    return "maintain"


def build_inventory(repo_dir: Path, site_dir: Path) -> dict:
    source_map = build_source_map(repo_dir)
    inbound = build_inbound_map(site_dir)
    rows: list[dict] = []

    for html_path in sorted(site_dir.rglob("*.html")):
        rel = html_path.relative_to(site_dir).as_posix()
        url_path = built_url_path(rel)
        content = html_path.read_text(encoding="utf-8", errors="ignore")
        visible_text = extract_visible_text(content)
        source = source_map.get(url_path, {})

        row = {
            "page": rel,
            "url_path": url_path,
            "url": f"{REPO_URL}{url_path}",
            "section": section_for(rel, url_path),
            "source_path": source.get("source_path", ""),
            "title": source.get("frontmatter_title") or pick(TITLE_RE, content),
            "description": source.get("frontmatter_description") or pick(DESC_RE, content),
            "status": source.get("status", ""),
            "verified": source.get("verified", ""),
            "robots": pick(ROBOTS_RE, content),
            "sitemap": source.get("sitemap", ""),
            "word_count": len(re.findall(r"\b\w+\b", visible_text)),
            "schema_types": schema_types(content),
            "inlink_count": len(inbound.get(rel, set())),
            "inlinks": sorted(inbound.get(rel, set()))[:20],
        }
        row["recommended_action"] = recommended_action(row)
        rows.append(row)

    action_counts = Counter(row["recommended_action"] for row in rows)
    noindex_count = sum(1 for row in rows if "noindex" in str(row["robots"]).lower())
    thin_indexable = sum(
        1
        for row in rows
        if "noindex" not in str(row["robots"]).lower() and row["word_count"] < 150
    )
    orphan_indexable = sum(
        1
        for row in rows
        if row["url_path"] != "/"
        and "noindex" not in str(row["robots"]).lower()
        and row["inlink_count"] == 0
    )

    return {
        "schema": "dkharlanau.content_inventory_report",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "summary": {
            "pages": len(rows),
            "indexable_pages": len(rows) - noindex_count,
            "noindex_pages": noindex_count,
            "source_matched_pages": sum(1 for row in rows if row["source_path"]),
            "thin_indexable_pages": thin_indexable,
            "orphan_indexable_pages": orphan_indexable,
            "recommended_actions": dict(sorted(action_counts.items())),
        },
        "pages": rows,
    }


def write_csv(report: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "page",
        "url_path",
        "url",
        "section",
        "source_path",
        "title",
        "description",
        "status",
        "verified",
        "robots",
        "sitemap",
        "word_count",
        "schema_types",
        "inlink_count",
        "recommended_action",
    ]
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for row in report["pages"]:
            csv_row = dict(row)
            csv_row["schema_types"] = "|".join(row["schema_types"])
            writer.writerow({key: csv_row.get(key, "") for key in fieldnames})


def write_json(report: dict, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-dir", default=".", help="Repository root (default: current directory)")
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--output", help="Explicit output path for JSON or CSV report")
    parser.add_argument("--format", choices=("json", "csv"), default="json", help="Report format")
    parser.add_argument("--summary", action="store_true", help="Print summary only and do not write files")
    args = parser.parse_args()

    repo_dir = Path(args.repo_dir).resolve()
    site_dir = Path(args.site_dir).resolve()
    if not repo_dir.is_dir():
        print(f"Missing repository directory: {repo_dir}", file=sys.stderr)
        return 1
    if not site_dir.is_dir():
        print(f"Missing site directory: {site_dir}. Build the site before running.", file=sys.stderr)
        return 1
    if not args.summary and not args.output:
        print("ERROR: --output is required unless --summary is used.", file=sys.stderr)
        return 1

    report = build_inventory(repo_dir, site_dir)

    if args.summary:
        print(json.dumps(report["summary"], indent=2, ensure_ascii=False))
        return 0

    output = Path(args.output).resolve()
    if args.format == "csv":
        write_csv(report, output)
    else:
        write_json(report, output)

    print(f"Content inventory report written: {output}")
    print(json.dumps(report["summary"], indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
