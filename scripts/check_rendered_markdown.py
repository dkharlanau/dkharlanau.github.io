#!/usr/bin/env python3
"""Detect Markdown syntax that leaked into rendered GitHub Pages HTML.

The site intentionally mixes Markdown, Liquid, and hand-written HTML. A common
failure mode is placing a Markdown table or fenced block inside an HTML wrapper
that Jekyll/Kramdown does not convert as expected. The page still builds, but
visitors see raw pipes/backticks as one unreadable paragraph.

This check runs against the built `_site` output, so it validates what a browser
will actually receive rather than assuming a source construct is safe.
"""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path


PROTECTED_BLOCK_RE = re.compile(
    r"<(pre|code|script|style|textarea)\b[^>]*>.*?</\1>",
    flags=re.IGNORECASE | re.DOTALL,
)
HTML_COMMENT_RE = re.compile(r"<!--.*?-->", flags=re.DOTALL)

# A Markdown/GFM table delimiter row such as:
# | --- | ---: | :---: |
TABLE_DELIMITER_RE = re.compile(
    r"(?m)^[ \t]*\|?[ \t]*:?-{3,}:?[ \t]*(?:\|[ \t]*:?-{3,}:?[ \t]*)+\|?[ \t]*$"
)

# Fences outside <pre>/<code> normally mean Markdown was left unconverted.
FENCE_RE = re.compile(r"(?m)^[ \t]*(?:```+|~~~+)[^\n]*$")

# Source-only signal. This does not fail CI by itself because some Kramdown
# constructs can be valid, but it points reviewers to fragile mixed markup.
MARKDOWN_HTML_ATTR_RE = re.compile(r"\bmarkdown\s*=\s*['\"](?:1|block|span)['\"]", re.IGNORECASE)

SOURCE_EXTENSIONS = {".md", ".markdown", ".html"}
SOURCE_EXCLUDED_DIRS = {
    ".git",
    ".github",
    ".playwright-cli",
    "_site",
    "docs",
    "node_modules",
    "reports",
    "scripts",
    "tests",
    "vendor",
}


def visible_html_source(text: str) -> str:
    """Remove blocks where literal Markdown syntax is expected and legitimate."""
    text = HTML_COMMENT_RE.sub("\n", text)
    text = PROTECTED_BLOCK_RE.sub("\n", text)
    return html.unescape(text)


def compact_excerpt(text: str, start: int, width: int = 180) -> str:
    left = max(0, start - 60)
    right = min(len(text), start + width)
    excerpt = text[left:right]
    return " ".join(excerpt.split())


def scan_rendered(site_dir: Path) -> list[tuple[str, str, str]]:
    findings: list[tuple[str, str, str]] = []
    for path in sorted(site_dir.rglob("*.html")):
        raw = path.read_text(encoding="utf-8", errors="ignore")
        visible = visible_html_source(raw)
        rel = path.relative_to(site_dir).as_posix()

        table_match = TABLE_DELIMITER_RE.search(visible)
        if table_match:
            findings.append(
                (
                    rel,
                    "raw Markdown table delimiter",
                    compact_excerpt(visible, table_match.start()),
                )
            )

        fence_match = FENCE_RE.search(visible)
        if fence_match:
            findings.append(
                (
                    rel,
                    "raw Markdown code fence",
                    compact_excerpt(visible, fence_match.start()),
                )
            )
    return findings


def is_source_candidate(path: Path, source_dir: Path) -> bool:
    if path.suffix.lower() not in SOURCE_EXTENSIONS:
        return False
    rel_parts = path.relative_to(source_dir).parts
    return not any(part in SOURCE_EXCLUDED_DIRS for part in rel_parts[:-1])


def scan_fragile_sources(source_dir: Path) -> list[str]:
    """Report source pages that combine markdown=1 with table syntax.

    These are review hints, not automatic failures. The rendered check above is
    the authority because it catches the actual browser-facing failure.
    """
    risky: list[str] = []
    for path in sorted(source_dir.rglob("*")):
        if not path.is_file() or not is_source_candidate(path, source_dir):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        if MARKDOWN_HTML_ATTR_RE.search(text) and TABLE_DELIMITER_RE.search(text):
            risky.append(path.relative_to(source_dir).as_posix())
    return risky


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("_site"))
    parser.add_argument("--source-dir", type=Path, default=Path("."))
    args = parser.parse_args()

    if not args.site_dir.is_dir():
        print(f"ERROR: built site directory does not exist: {args.site_dir}", file=sys.stderr)
        return 2

    rendered_findings = scan_rendered(args.site_dir)
    fragile_sources = scan_fragile_sources(args.source_dir)

    if fragile_sources:
        print("Fragile mixed Markdown/HTML sources to review:")
        for rel in fragile_sources:
            print(f"  WARN  {rel}: markdown=1 used together with Markdown table syntax")

    if rendered_findings:
        print("\nBrowser-facing Markdown rendering failures:", file=sys.stderr)
        for rel, kind, excerpt in rendered_findings:
            print(f"  ERROR {rel}: {kind}", file=sys.stderr)
            print(f"        {excerpt}", file=sys.stderr)
        print(
            f"\nFAILED: {len(rendered_findings)} rendered Markdown artifact(s) found. "
            "Convert the block to explicit HTML or render captured Markdown with markdownify.",
            file=sys.stderr,
        )
        return 1

    html_count = sum(1 for _ in args.site_dir.rglob("*.html"))
    print(
        f"Rendered Markdown check passed: {html_count} HTML files scanned; "
        f"{len(fragile_sources)} fragile source pattern(s) reported for review."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
