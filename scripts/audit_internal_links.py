#!/usr/bin/env python3
"""Audit internal link graph of the built site.

Produces:
  - reports/seo/internal-link-graph-YYYY-MM-DD.csv
  - reports/seo/internal-link-graph-YYYY-MM-DD.md

Usage:
    python3 scripts/audit_internal_links.py [--site-dir _site] [--repo-dir .]
"""

from __future__ import annotations

import argparse
import csv
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


def is_external(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme in {"http", "https", "mailto", "tel", "data", "javascript"}


def normalize_local_path(link: str, site_dir: Path, current_dir: Path) -> Path | None:
    if not link or link.startswith("#") or is_external(url=link):
        return None
    local = link.lstrip("/")
    if not local:
        return site_dir / "index.html"
    target = site_dir / local
    if target.is_dir():
        target = target / "index.html"
    elif not str(target).endswith(".html"):
        target = target.with_suffix(".html")
    return target


def extract_page_info(html_path: Path) -> dict:
    content = html_path.read_text(encoding="utf-8", errors="ignore")
    robots_match = META_ROBOTS_RE.search(content)
    robots = robots_match.group(1).lower() if robots_match else ""
    title_match = TITLE_RE.search(content)
    title = title_match.group(1).strip() if title_match else ""
    return {
        "title": title,
        "is_noindex": "noindex" in robots,
        "links": LINK_HREF_RE.findall(content),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    repo_dir = Path(args.repo_dir).resolve()
    if not site_dir.is_dir():
        print(f"Missing site directory: {site_dir}", file=sys.stderr)
        return 1

    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    csv_path = repo_dir / "reports" / "seo" / f"internal-link-graph-{today}.csv"
    md_path = repo_dir / "reports" / "seo" / f"internal-link-graph-{today}.md"
    csv_path.parent.mkdir(parents=True, exist_ok=True)

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
                target_rel = target.relative_to(site_dir).as_posix()
                outbound[rel].append(link)
                inbound[target_rel].add(rel)

    # Build CSV rows
    rows: list[dict] = []
    for rel in sorted(page_info.keys()):
        info = page_info[rel]
        rows.append({
            "page": rel,
            "title": info["title"],
            "noindex": "yes" if info["is_noindex"] else "no",
            "inbound_count": len(inbound[rel]),
            "outbound_count": len(outbound[rel]),
            "broken_count": len(broken[rel]),
            "inbound_from": " | ".join(sorted(inbound[rel]))[:200],
            "broken_links": " | ".join(broken[rel])[:200],
        })

    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "page", "title", "noindex", "inbound_count", "outbound_count",
            "broken_count", "inbound_from", "broken_links",
        ])
        writer.writeheader()
        writer.writerows(rows)

    # Orphan pages (no inbound from other content pages)
    orphans = [r for r in rows if r["inbound_count"] == 0 and r["page"] != "index.html"]
    # Hub pages (high inbound)
    hubs = sorted(rows, key=lambda x: x["inbound_count"], reverse=True)[:15]
    # Indexable pages linking to noindex pages
    indexable_to_noindex: list[tuple[str, str]] = []
    for rel in sorted(page_info.keys()):
        if page_info[rel]["is_noindex"]:
            continue
        for link in outbound[rel]:
            target = normalize_local_path(link, site_dir, site_dir)
            if target and target.exists():
                target_rel = target.relative_to(site_dir).as_posix()
                if target_rel in page_info and page_info[target_rel]["is_noindex"]:
                    indexable_to_noindex.append((rel, link))

    md_lines = [
        f"# Internal Link Graph Report",
        f"",
        f"**Date:** {today}",
        f"**Pages scanned:** {len(rows)}",
        f"",
        f"## Summary",
        f"- **Orphan pages:** {len(orphans)}",
        f"- **Pages with broken links:** {sum(1 for r in rows if r['broken_count'] > 0)}",
        f"- **Indexable pages linking to noindex:** {len(indexable_to_noindex)}",
        f"",
        f"## Orphan Pages (no inbound links)",
        f"",
    ]
    if orphans:
        for o in orphans:
            md_lines.append(f"- `{o['page']}` — {o['title']}")
    else:
        md_lines.append("No orphan pages detected.")

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
    if broken_found:
        for b in broken_found:
            md_lines.append(f"- `{b['page']}`: {b['broken_links']}")
    else:
        md_lines.append("No broken local links detected.")

    md_lines.extend([
        "",
        "## Indexable Pages Linking to Noindex Pages",
        "",
    ])
    if indexable_to_noindex:
        for src, link in indexable_to_noindex[:30]:
            md_lines.append(f"- `{src}` → `{link}`")
        if len(indexable_to_noindex) > 30:
            md_lines.append(f"- ... and {len(indexable_to_noindex) - 30} more")
    else:
        md_lines.append("No indexable pages link to noindex pages.")

    md_lines.extend([
        "",
        "## Recommendations",
        "",
        "1. Add internal links to orphan pages from related index pages or hub pages.",
        "2. Fix broken links before indexing new pages.",
        "3. Review indexable→noindex links — ensure they are intentional (e.g., 'review candidate' disclaimers).",
        "4. Strengthen hub pages (index pages, atlas index, skill-hub index) with more outbound links to verified content.",
    ])

    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    print(f"Link graph audit complete: {len(rows)} pages")
    print(f"  CSV: {csv_path}")
    print(f"  MD:  {md_path}")
    print(f"  Orphans: {len(orphans)}")
    print(f"  Broken: {len(broken_found)}")
    print(f"  Indexable→noindex: {len(indexable_to_noindex)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
