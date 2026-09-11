#!/usr/bin/env python3
import argparse
import html
import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse


TITLE_RE = re.compile(r"<title>(.*?)</title>", re.IGNORECASE | re.DOTALL)
DESC_RE = re.compile(
    r'<meta[^>]+name=["\']description["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
ROBOTS_RE = re.compile(
    r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
CANONICAL_RE = re.compile(
    r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_URL_RE = re.compile(
    r'<meta[^>]+property=["\']og:url["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
OG_SITE_NAME_RE = re.compile(
    r'<meta[^>]+property=["\']og:site_name["\'][^>]+content=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)
JSON_LD_RE = re.compile(
    r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',
    re.IGNORECASE | re.DOTALL,
)
ICON_RE = re.compile(
    r'<link[^>]+rel=["\'](?:shortcut\s+)?icon["\'][^>]+href=["\'](.*?)["\']',
    re.IGNORECASE | re.DOTALL,
)


def pick(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    return html.unescape(match.group(1)).strip()


def is_absolute_https(url: str) -> bool:
    return url.startswith("https://")


def collect_type(value, type_name: str, found: list[dict]) -> None:
    if isinstance(value, list):
        for item in value:
            collect_type(item, type_name, found)
        return
    if not isinstance(value, dict):
        return
    node_type = value.get("@type")
    types = node_type if isinstance(node_type, list) else [node_type]
    if type_name in types:
        found.append(value)
    for child in value.values():
        collect_type(child, type_name, found)


def png_dimensions(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} is not a valid PNG")
    return int.from_bytes(data[16:20], "big"), int.from_bytes(data[20:24], "big")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check built HTML and final Search Release invariants.")
    parser.add_argument("root", nargs="?", default="_site", help="Built site root (default: _site)")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"Missing directory: {root}. Build the site before running.")
        return 1

    identity_path = Path("_data/site_identity.json")
    if not identity_path.is_file():
        print("Missing _data/site_identity.json search identity contract.")
        return 1
    identity = json.loads(identity_path.read_text(encoding="utf-8"))
    site_url = identity["siteUrl"]
    site_origin = urlparse(site_url).netloc

    html_files = sorted(root.rglob("*.html"))
    errors = []

    for file_path in html_files:
        rel = file_path.relative_to(root)
        content = file_path.read_text(encoding="utf-8", errors="ignore")

        title = pick(TITLE_RE, content)
        description = pick(DESC_RE, content)
        robots = pick(ROBOTS_RE, content).lower()
        canonical = pick(CANONICAL_RE, content)
        og_url = pick(OG_URL_RE, content)
        is_noindex = "noindex" in robots
        is_404 = rel.as_posix() == "404.html"

        if not title:
            errors.append(f"{rel}: missing <title>")
        if not description:
            errors.append(f"{rel}: missing meta description")

        if is_404:
            if not is_noindex:
                errors.append("404.html: must be noindex")
            if canonical:
                errors.append(f"404.html: must not advertise canonical content ({canonical})")
            if og_url:
                errors.append(f"404.html: must not advertise og:url content ({og_url})")
            if 'href="/"' not in content:
                errors.append("404.html: missing recovery link to homepage")
            continue

        if not canonical:
            errors.append(f"{rel}: missing canonical link")
        else:
            if not is_absolute_https(canonical):
                errors.append(f"{rel}: canonical is not absolute https URL ({canonical})")
            if "localhost" in canonical:
                errors.append(f"{rel}: canonical points to localhost ({canonical})")

        if not og_url:
            errors.append(f"{rel}: missing og:url")
        else:
            if not is_absolute_https(og_url):
                errors.append(f"{rel}: og:url is not absolute https URL ({og_url})")
            if "localhost" in og_url:
                errors.append(f"{rel}: og:url points to localhost ({og_url})")

        if canonical and og_url and canonical != og_url and not is_noindex:
            errors.append(f"{rel}: canonical and og:url mismatch ({canonical} != {og_url})")

    home_path = root / "index.html"
    if not home_path.is_file():
        errors.append("index.html: missing built homepage")
    else:
        home = home_path.read_text(encoding="utf-8", errors="ignore")
        if pick(TITLE_RE, home) != identity["homepageTitle"]:
            errors.append(f"index.html: homepage title drifted from site_identity.json ({pick(TITLE_RE, home)!r})")
        if pick(DESC_RE, home) != identity["homepageDescription"]:
            errors.append("index.html: homepage description drifted from site_identity.json")
        if pick(CANONICAL_RE, home) != site_url:
            errors.append(f"index.html: canonical must be {site_url}")
        if pick(OG_URL_RE, home) != site_url:
            errors.append(f"index.html: og:url must be {site_url}")
        if pick(OG_SITE_NAME_RE, home) != identity["siteName"]:
            errors.append("index.html: og:site_name drifted from site_identity.json")
        icons = [html.unescape(match.group(1)).strip() for match in ICON_RE.finditer(home)]
        if identity["faviconPath"] not in icons:
            errors.append(f"index.html: stable PNG favicon {identity['faviconPath']} is not declared")

        parsed_json_ld = []
        for raw in JSON_LD_RE.findall(home):
            try:
                parsed_json_ld.append(json.loads(html.unescape(raw.strip())))
            except json.JSONDecodeError as exc:
                errors.append(f"index.html: invalid JSON-LD ({exc})")
        website_nodes: list[dict] = []
        for value in parsed_json_ld:
            collect_type(value, "WebSite", website_nodes)
        full_websites = [node for node in website_nodes if node.get("name") and node.get("url")]
        if len(full_websites) != 1:
            errors.append(f"index.html: expected one full WebSite identity, found {len(full_websites)}")
        elif full_websites[0].get("name") != identity["siteName"] or full_websites[0].get("url") != site_url:
            errors.append("index.html: WebSite identity disagrees with site_identity.json")

    favicon_path = root / identity["faviconPath"].lstrip("/")
    if not favicon_path.is_file():
        errors.append(f"favicon: missing {identity['faviconPath']}")
    else:
        try:
            width, height = png_dimensions(favicon_path)
            if width != height:
                errors.append(f"favicon: expected square PNG, got {width}x{height}")
            if width < 48:
                errors.append(f"favicon: expected at least 48px source, got {width}x{height}")
        except ValueError as exc:
            errors.append(f"favicon: {exc}")

    sitemap_path = root / "sitemap.xml"
    if not sitemap_path.is_file():
        errors.append("sitemap.xml: missing")
    else:
        try:
            sitemap_root = ET.fromstring(sitemap_path.read_text(encoding="utf-8"))
            locs = [node.text.strip() for node in sitemap_root.iter() if node.tag.endswith("loc") and node.text]
            if len(locs) != len(set(locs)):
                errors.append("sitemap.xml: duplicate URL entries")
            if site_url not in locs:
                errors.append("sitemap.xml: canonical homepage is missing")
            for loc in locs:
                if urlparse(loc).netloc != site_origin:
                    errors.append(f"sitemap.xml: non-canonical host {loc}")
                if loc.endswith("/404.html") or loc.endswith("/404/"):
                    errors.append("sitemap.xml: 404 route must not be listed")
        except ET.ParseError as exc:
            errors.append(f"sitemap.xml: invalid XML ({exc})")

    robots_path = root / "robots.txt"
    if not robots_path.is_file():
        errors.append("robots.txt: missing")
    else:
        robots_txt = robots_path.read_text(encoding="utf-8", errors="ignore")
        if f"Sitemap: {site_url}sitemap.xml" not in robots_txt:
            errors.append("robots.txt: canonical sitemap declaration is missing")

    profile_path = root / "ai/site-profile.json"
    if not profile_path.is_file():
        errors.append("ai/site-profile.json: missing")
    else:
        profile_text = profile_path.read_text(encoding="utf-8", errors="ignore")
        if identity["siteName"] not in profile_text or site_url not in profile_text:
            errors.append("ai/site-profile.json: machine-readable identity disagrees with canonical site identity")
        if "localhost" in profile_text:
            errors.append("ai/site-profile.json: leaks localhost identity")

    if errors:
        print(f"SEO/Search Release checks failed for {len(errors)} issue(s):")
        for item in errors[:300]:
            print(f"- {item}")
        if len(errors) > 300:
            print(f"... and {len(errors) - 300} more")
        return 2

    print(
        f"SEO/Search Release checks passed for {len(html_files)} HTML files; "
        f"homepage identity={identity['siteName']!r}, canonical={site_url}, favicon and 404 verified."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
