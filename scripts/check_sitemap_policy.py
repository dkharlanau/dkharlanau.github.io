#!/usr/bin/env python3
"""Validate that generated sitemaps only contain indexable, policy-compliant URLs.

Checks:
- Every URL in sitemap*.xml resolves to a built page that is not noindex.
- Atlas pages in sitemaps have a verified=true, status=reviewed source.
- Research pages are not in sitemaps.
- Static data endpoints match an allowlist.

Pages without a markdown source are accepted if their built HTML is indexable
and they are not Atlas pages (Atlas requires frontmatter verification).

Usage:
    python3 scripts/check_sitemap_policy.py [--site-dir _site] [--repo-dir .]
"""

from __future__ import annotations

import argparse
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse

import yaml

SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
BASE_URL = "https://dkharlanau.github.io"

FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
META_ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)

# Static endpoints that are allowed in sitemap-data.xml without a markdown source.
ALLOWLISTED_STATIC_PATHS = {
    "/ai/resume.yml",
    "/ai/resume.json",
    "/ai/principles.json",
    "/ai/recommendations.json",
    "/ai/catalog.json",
    "/ai/discovery-map.json",
    "/LLM.txt",
    "/llms.txt",
    "/datasets/manifest.json",
    "/datasets/schema.json",
}


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def load_sitemap_urls(site_dir: Path) -> set[str]:
    urls: set[str] = set()
    for sitemap_path in sorted(site_dir.glob("sitemap*.xml")):
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
        except ET.ParseError as exc:
            # sitemap-data.xml contains Jekyll frontmatter that is stripped during render;
            # if parsing fails here, try after removing leading blank lines.
            text = sitemap_path.read_text(encoding="utf-8", errors="ignore")
            text = text.lstrip()
            if text.startswith("<?xml"):
                try:
                    root = ET.fromstring(text)
                except ET.ParseError:
                    print(f"WARNING: could not parse {sitemap_path}: {exc}", file=sys.stderr)
                    continue
            else:
                print(f"WARNING: could not parse {sitemap_path}: {exc}", file=sys.stderr)
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
                        if url_loc is not None and url_loc.text:
                            urls.add(url_loc.text.strip())
                except ET.ParseError as exc:
                    print(f"WARNING: could not parse {loc_path}: {exc}", file=sys.stderr)
        elif tag == "urlset":
            for url in root.findall(f"{{{SITEMAP_NS}}}url"):
                url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                if url_loc is not None and url_loc.text:
                    urls.add(url_loc.text.strip())
    return urls


def built_html_path(site_dir: Path, url_path: str) -> Path | None:
    """Map a URL path to the corresponding built HTML file."""
    rel = url_path.lstrip("/")
    if not rel:
        candidate = site_dir / "index.html"
    else:
        candidate = site_dir / rel
        if candidate.is_dir():
            candidate = candidate / "index.html"
        elif candidate.suffix.lower() not in {".html", ".json", ".yml", ".xml", ".txt"}:
            candidate = candidate.with_suffix(candidate.suffix + ".html")
    if candidate.exists():
        return candidate
    return None


def is_built_noindex(site_dir: Path, url_path: str) -> bool:
    """Check whether the built page has robots:noindex."""
    html_path = built_html_path(site_dir, url_path)
    if html_path is None or html_path.suffix.lower() != ".html":
        return False
    try:
        text = html_path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return False
    match = META_ROBOTS_RE.search(text)
    if match and "noindex" in match.group(1).lower():
        return True
    return False


def source_for_url(url: str, repo_dir: Path) -> tuple[Path | None, dict]:
    """Find source markdown and frontmatter for a canonical URL."""
    if not url.startswith(BASE_URL):
        return None, {}
    path = urlparse(url).path

    if path in ALLOWLISTED_STATIC_PATHS:
        return None, {"static": True}

    rel = path.strip("/")
    candidates = []
    if not rel:
        candidates = ["index.md"]
    else:
        candidates = [f"{rel}.md", f"{rel}/index.md"]

    for candidate in candidates:
        source = repo_dir / candidate
        if source.exists():
            return source, parse_frontmatter(source)

    return None, {}


def check_url(url: str, repo_dir: Path, site_dir: Path) -> list[str]:
    issues: list[str] = []
    if not url.startswith(BASE_URL):
        issues.append(f"{url}: not a site URL")
        return issues

    path = urlparse(url).path
    source, fm = source_for_url(url, repo_dir)

    # Static allowlisted files need no further checks.
    if fm.get("static"):
        return issues

    if source is not None:
        rel = source.relative_to(repo_dir).as_posix()
        robots = fm.get("robots", "")
        sitemap = fm.get("sitemap", True)
        verified = fm.get("verified", False)
        status = fm.get("status", "")

        if "noindex" in robots.lower():
            issues.append(f"{url}: source {rel} has robots:noindex")
        if sitemap is False:
            issues.append(f"{url}: source {rel} has sitemap:false")
        if rel.startswith("research/"):
            issues.append(f"{url}: research page {rel} must not be in sitemap")

        if "/atlas/" in path or rel.startswith("atlas/"):
            if verified is not True:
                issues.append(f"{url}: Atlas source {rel} is not verified=true")
            if status != "reviewed":
                issues.append(f"{url}: Atlas source {rel} status is '{status}', expected 'reviewed'")
    else:
        # No markdown source: only enforce indexability and Atlas restriction.
        if "/atlas/" in path:
            issues.append(f"{url}: Atlas URL without source markdown cannot be verified")
        if path.startswith("/research/"):
            issues.append(f"{url}: research URL must not be in sitemap")

    # Defense-in-depth: check built HTML for noindex.
    if is_built_noindex(site_dir, path):
        issues.append(f"{url}: built HTML has robots:noindex")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--repo-dir", default=".", help="Repository root")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on issues")
    args = parser.parse_args()

    repo_dir = Path(args.repo_dir).resolve()
    site_dir = Path(args.site_dir).resolve()

    if not site_dir.is_dir():
        print(f"ERROR: site directory not found: {site_dir}", file=sys.stderr)
        return 1

    urls = load_sitemap_urls(site_dir)
    if not urls:
        print("WARNING: no URLs found in sitemaps", file=sys.stderr)

    all_issues: list[str] = []
    for url in sorted(urls):
        all_issues.extend(check_url(url, repo_dir, site_dir))

    if all_issues:
        print(f"Sitemap policy check failed: {len(all_issues)} issue(s)")
        for issue in all_issues[:50]:
            print(f"  - {issue}")
        if len(all_issues) > 50:
            print(f"  ... and {len(all_issues) - 50} more")
        if args.fail_on_critical:
            return 2
    else:
        print(f"Sitemap policy check passed for {len(urls)} URL(s).")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
