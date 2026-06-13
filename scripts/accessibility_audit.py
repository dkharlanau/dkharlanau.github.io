#!/usr/bin/env python3
"""Accessibility and semantic HTML audit for AI/browser agents.

Checks built HTML for:
- Semantic landmarks (<main>, <header>, <footer>, <nav>, <article>)
- Heading hierarchy (no skipped levels, one H1 per page)
- Descriptive link anchor text (no generic "click here" / "read more")
- Image alt text on meaningful images
- Skip link presence

Outputs a report; CI can fail on critical issues.

Usage:
    python3 scripts/accessibility_audit.py [--site-dir _site] [--fail-on-critical]
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

GENERIC_ANCHORS = {
    "click here", "read more", "more", "here", "link", "click", "details",
    "continue reading", "learn more", "see more", "download", "view",
}

CRITICAL_MISSING_LANDMARKS = {"main", "header", "footer"}

HEADING_RE = re.compile(r"<h([1-6])[^>]*>(.*?)</h\1>", re.IGNORECASE | re.DOTALL)
LINK_RE = re.compile(r'<a[^>]+href=["\'](.*?)["\'][^>]*>(.*?)</a>', re.IGNORECASE | re.DOTALL)
IMG_RE = re.compile(r"<img[^>]*>", re.IGNORECASE | re.DOTALL)
ALT_RE = re.compile(r'alt=["\'](.*?)["\']', re.IGNORECASE | re.DOTALL)
SRC_RE = re.compile(r'src=["\'](.*?)["\']', re.IGNORECASE | re.DOTALL)
SKIP_LINK_RE = re.compile(r'<a[^>]+href=["\']#([^"\']+)["\'][^>]*>.*?(skip|jump).*?</a>', re.IGNORECASE | re.DOTALL)
TARGET_RE = re.compile(r'id=["\']([^"\']+)["\']', re.IGNORECASE | re.DOTALL)


def strip_html(text: str) -> str:
    return re.sub(r"<[^>]+>", "", text).strip()


def check_page(html_path: Path, site_dir: Path, text: str) -> tuple[list[str], list[str]]:
    """Return (critical_issues, warnings) for a single HTML file."""
    critical: list[str] = []
    warnings: list[str] = []
    rel = html_path.relative_to(site_dir).as_posix()

    lower = text.lower()

    # Landmarks
    landmarks = {
        "main": "<main" in lower,
        "header": "<header" in lower,
        "footer": "<footer" in lower,
        "nav": "<nav" in lower,
        "article": "<article" in lower,
    }
    for name in CRITICAL_MISSING_LANDMARKS:
        if not landmarks[name]:
            critical.append(f"missing <{name}> landmark")
    if not landmarks["nav"]:
        warnings.append("missing <nav> landmark")

    # Skip link
    if not SKIP_LINK_RE.search(text):
        warnings.append("missing skip navigation link")

    # Headings
    headings = HEADING_RE.findall(text)
    h1_count = sum(1 for level, _ in headings if level == "1")
    if h1_count == 0:
        critical.append("missing <h1>")
    elif h1_count > 1:
        warnings.append(f"multiple <h1> elements ({h1_count})")

    prev_level = 0
    for level_str, _ in headings:
        level = int(level_str)
        if prev_level > 0 and level > prev_level + 1:
            warnings.append(f"skipped heading level (h{prev_level} to h{level})")
        prev_level = max(prev_level, level)

    # Links
    for href, anchor in LINK_RE.findall(text):
        clean = strip_html(anchor)
        if not clean:
            continue
        lower_anchor = clean.lower()
        if lower_anchor in GENERIC_ANCHORS and not href.startswith("#"):
            warnings.append(f"generic anchor text: '{clean}' -> {href}")

    # Images
    for img_tag in IMG_RE.findall(text):
        src_match = SRC_RE.search(img_tag)
        src = src_match.group(1) if src_match else ""
        alt_match = ALT_RE.search(img_tag)
        alt = alt_match.group(1) if alt_match else None
        if alt is None and src and not src.endswith((".svg", ".webp")):
            # Decorative SVGs/webp often do not need alt; flag others.
            warnings.append(f"image missing alt text: {src}")

    # Prefix each issue with file path.
    critical = [f"{rel}: {issue}" for issue in critical]
    warnings = [f"{rel}: {issue}" for issue in warnings]
    return critical, warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", default="_site", help="Built site directory")
    parser.add_argument("--fail-on-critical", action="store_true", help="Exit non-zero on critical issues")
    parser.add_argument("--max-issues", type=int, default=100, help="Max issues to print per category")
    parser.add_argument(
        "--exclude-prefix",
        action="append",
        default=["docs/", "_site/docs/"],
        help="Path prefixes to exclude from audit (default: docs/)"
    )
    args = parser.parse_args()

    site_dir = Path(args.site_dir).resolve()
    if not site_dir.is_dir():
        print(f"ERROR: site directory not found: {site_dir}", file=sys.stderr)
        return 1

    all_critical: list[str] = []
    all_warnings: list[str] = []

    exclude_prefixes = tuple(p.strip("/") for p in args.exclude_prefix)
    for html_path in sorted(site_dir.rglob("*.html")):
        rel = html_path.relative_to(site_dir).as_posix()
        if rel.startswith(exclude_prefixes):
            continue
        try:
            text = html_path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        critical, warnings = check_page(html_path, site_dir, text)
        all_critical.extend(critical)
        all_warnings.extend(warnings)

    total_issues = len(all_critical) + len(all_warnings)

    if all_critical:
        print(f"Accessibility audit: {len(all_critical)} critical issue(s)")
        for issue in all_critical[: args.max_issues]:
            print(f"  CRITICAL - {issue}")
        if len(all_critical) > args.max_issues:
            print(f"  ... and {len(all_critical) - args.max_issues} more critical issues")
    else:
        print("Accessibility audit: no critical issues")

    if all_warnings:
        print(f"Accessibility audit: {len(all_warnings)} warning(s)")
        for issue in all_warnings[: args.max_issues]:
            print(f"  WARNING - {issue}")
        if len(all_warnings) > args.max_issues:
            print(f"  ... and {len(all_warnings) - args.max_issues} more warnings")
    else:
        print("Accessibility audit: no warnings")

    if all_critical and args.fail_on_critical:
        return 2

    print(f"Accessibility audit complete: {total_issues} total issue(s) across built site.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
