#!/usr/bin/env python3
"""Detect date drift between source frontmatter, built HTML, JSON-LD, and sitemap.

Checks:
- Source frontmatter date (last_modified_at, updated, date, last_reviewed)
- HTML <meta property="article:modified_time">
- JSON-LD dateModified / datePublished
- Sitemap <lastmod>

Drift is reported; no files are modified.

Usage:
    python3 scripts/check_date_consistency.py [--site-dir _site] [--repo-dir .]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import yaml

BASE_URL = "https://dkharlanau.github.io"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
META_ARTICLE_MOD_RE = re.compile(
    r'<meta[^>]+property=["\']article:modified_time["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
JSON_LD_RE = re.compile(
    r'<script type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def load_sitemap_lastmods(site_dir: Path) -> dict[str, str]:
    """Return map of canonical URL -> lastmod string from all sitemap files."""
    lastmods: dict[str, str] = {}
    for sitemap_path in sorted(site_dir.glob("sitemap*.xml")):
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
        except ET.ParseError:
            continue

        tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        if tag == "sitemapindex":
            for sitemap in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
                loc = sitemap.find(f"{{{SITEMAP_NS}}}loc")
                if loc is None or not loc.text:
                    continue
                loc_path = site_dir / Path(urlparse(loc.text.strip()).path).name
                if not loc_path.exists():
                    continue
                try:
                    sub_tree = ET.parse(loc_path)
                    sub_root = sub_tree.getroot()
                    for url in sub_root.findall(f"{{{SITEMAP_NS}}}url"):
                        url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                        url_lastmod = url.find(f"{{{SITEMAP_NS}}}lastmod")
                        if url_loc is not None and url_loc.text and url_lastmod is not None and url_lastmod.text:
                            lastmods[url_loc.text.strip()] = url_lastmod.text.strip()
                except ET.ParseError:
                    continue
        elif tag == "urlset":
            for url in root.findall(f"{{{SITEMAP_NS}}}url"):
                url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                url_lastmod = url.find(f"{{{SITEMAP_NS}}}lastmod")
                if url_loc is not None and url_loc.text and url_lastmod is not None and url_lastmod.text:
                    lastmods[url_loc.text.strip()] = url_lastmod.text.strip()
    return lastmods


def normalize_date(value: str | None) -> str:
    """Reduce an ISO-like date string to YYYY-MM-DD for comparison."""
    if not value:
        return ""
    value = value.strip()
    # Strip time and timezone, keep date portion.
    if "T" in value:
        value = value.split("T")[0]
    elif " " in value:
        value = value.split(" ")[0]
    return value


def extract_html_dates(html_path: Path) -> dict[str, str]:
    """Extract article:modified_time and JSON-LD dates from built HTML."""
    result: dict[str, str] = {}
    try:
        text = html_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return result

    match = META_ARTICLE_MOD_RE.search(text)
    if match:
        result["article:modified_time"] = match.group(1).strip()

    for block in JSON_LD_RE.findall(text):
        try:
            data = json.loads(block)
            if isinstance(data, dict):
                for key in ("dateModified", "datePublished"):
                    if key in data and data[key]:
                        result[key] = str(data[key]).strip()
                        break
        except Exception:
            continue

    return result


def source_date(fm: dict) -> str:
    """Pick the most appropriate source date from frontmatter."""
    for key in ("last_modified_at", "updated", "last_reviewed", "date"):
        value = fm.get(key)
        if value:
            return str(value).strip()
    return ""


def source_for_url(url: str, repo_dir: Path) -> tuple[Path | None, dict]:
    if not url.startswith(BASE_URL):
        return None, {}
    path = urlparse(url).path.strip("/")
    candidates = []
    if not path:
        candidates = ["index.md"]
    else:
        candidates = [f"{path}.md", f"{path}/index.md"]
    for candidate in candidates:
        source = repo_dir / candidate
        if source.exists():
            return source, parse_frontmatter(source)
    return None, {}


def check_url(url: str, lastmod: str, repo_dir: Path, site_dir: Path) -> list[str]:
    issues: list[str] = []
    source, fm = source_for_url(url, repo_dir)
    if source is None:
        # Static files are not checked for date consistency.
        return issues

    rel = source.relative_to(repo_dir).as_posix()
    src_date = normalize_date(source_date(fm))
    sitemap_date = normalize_date(lastmod)

    # Map URL to built HTML path.
    path = urlparse(url).path.strip("/")
    if not path:
        html_path = site_dir / "index.html"
    else:
        html_path = site_dir / path
        if html_path.is_dir():
            html_path = html_path / "index.html"
        elif html_path.suffix.lower() not in {".html"}:
            html_path = html_path.with_suffix(html_path.suffix + ".html")

    html_dates = extract_html_dates(html_path) if html_path.exists() else {}

    # Compare sitemap lastmod with source date.
    if src_date and sitemap_date and src_date != sitemap_date:
        issues.append(
            f"{url}: sitemap lastmod ({sitemap_date}) differs from source date ({src_date}) in {rel}"
        )

    # Compare HTML article:modified_time with source date.
    html_mod = normalize_date(html_dates.get("article:modified_time"))
    if src_date and html_mod and src_date != html_mod:
        issues.append(
            f"{url}: HTML article:modified_time ({html_mod}) differs from source date ({src_date}) in {rel}"
        )

    # Compare JSON-LD dateModified with source date.
    jsonld_mod = normalize_date(html_dates.get("dateModified"))
    if src_date and jsonld_mod and src_date != jsonld_mod:
        issues.append(
            f"{url}: JSON-LD dateModified ({jsonld_mod}) differs from source date ({src_date}) in {rel}"
        )

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on drift")
    args = parser.parse_args()

    repo_dir = Path(args.repo_dir).resolve()
    site_dir = Path(args.site_dir).resolve()

    if not site_dir.is_dir():
        print(f"ERROR: site directory not found: {site_dir}", file=sys.stderr)
        return 1

    lastmods = load_sitemap_lastmods(site_dir)
    if not lastmods:
        print("WARNING: no lastmod values found in sitemaps", file=sys.stderr)

    all_issues: list[str] = []
    for url in sorted(lastmods):
        all_issues.extend(check_url(url, lastmods[url], repo_dir, site_dir))

    if all_issues:
        print(f"Date consistency check failed: {len(all_issues)} drift issue(s)")
        for issue in all_issues[:50]:
            print(f"  - {issue}")
        if len(all_issues) > 50:
            print(f"  ... and {len(all_issues) - 50} more")
        if args.fail_on_critical:
            return 2
    else:
        print(f"Date consistency check passed for {len(lastmods)} URL(s) with lastmod.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
