#!/usr/bin/env python3
import argparse
import html
import re
import sys
from pathlib import Path


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


def pick(pattern: re.Pattern, text: str) -> str:
    match = pattern.search(text)
    if not match:
        return ""
    return html.unescape(match.group(1)).strip()


def is_absolute_https(url: str) -> bool:
    return url.startswith("https://")


def main() -> int:
    parser = argparse.ArgumentParser(description="Check built HTML for SEO metadata quality.")
    parser.add_argument("root", nargs="?", default="_site", help="Built site root (default: _site)")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.is_dir():
        print(f"Missing directory: {root}. Build the site before running.")
        return 1

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

        if not title:
            errors.append(f"{rel}: missing <title>")
        if not description:
            errors.append(f"{rel}: missing meta description")

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

    if errors:
        print(f"SEO checks failed for {len(errors)} issue(s):")
        for item in errors[:300]:
            print(f"- {item}")
        if len(errors) > 300:
            print(f"... and {len(errors) - 300} more")
        return 2

    print(f"SEO checks passed for {len(html_files)} HTML files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
