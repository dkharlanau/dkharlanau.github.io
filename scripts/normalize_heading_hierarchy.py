#!/usr/bin/env python3
"""Normalize known Lab heading patterns before the expensive site build.

The normalizer keeps visual card layouts aligned with semantic heading levels:
- peer ``ecg-decision-columns`` cards directly under H2 use H3 titles;
- nested decision columns after H3 keep H4 titles;
- the Sales derivation card grid uses H3 card titles and H4 detail titles;
- the dynamic promotion-review rule cards use H3 under their H2 section.

Both HTML and Markdown Lab sources are scanned. Use ``--check`` in CI to report
source files that still need normalization without writing them.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOTS = (Path("labs/assessment"), Path("labs/enterprise-context"))
SOURCE_SUFFIXES = {".html", ".md"}
HEADING_RE = re.compile(r"<h([1-6])\b[^>]*>.*?</h\1>", re.IGNORECASE | re.DOTALL)
OPEN_DECISION_RE = re.compile(
    r'<div\b[^>]*class=["\'][^"\']*\becg-decision-columns\b[^"\']*["\'][^>]*>',
    re.IGNORECASE,
)
DIV_TOKEN_RE = re.compile(r"</?div\b[^>]*>", re.IGNORECASE)
H4_OPEN_RE = re.compile(r"<h4(\b[^>]*)>", re.IGNORECASE)
H4_CLOSE_RE = re.compile(r"</h4>", re.IGNORECASE)
H5_OPEN_RE = re.compile(r"<h5(\b[^>]*)>", re.IGNORECASE)
H5_CLOSE_RE = re.compile(r"</h5>", re.IGNORECASE)

DERIVATION_PATH = Path("labs/enterprise-context/sales-processes/mechanisms/derivation/index.html")
PROMOTION_REVIEW_PATH = Path("labs/assessment/promotion-review/index.html")


def matching_div_end(text: str, start: int) -> int | None:
    depth = 0
    for match in DIV_TOKEN_RE.finditer(text, start):
        token = match.group(0).lower()
        if token.startswith("</div"):
            depth -= 1
            if depth == 0:
                return match.end()
        else:
            depth += 1
    return None


def last_heading_in(text: str) -> int | None:
    headings = list(HEADING_RE.finditer(text))
    return int(headings[-1].group(1)) if headings else None


def normalize_text(text: str) -> tuple[str, int]:
    """Normalize generic decision-column groups in one source string."""
    changes = 0
    cursor = 0
    last_heading_level = 0
    parts: list[str] = []

    while True:
        heading = HEADING_RE.search(text, cursor)
        decision = OPEN_DECISION_RE.search(text, cursor)
        if not heading and not decision:
            parts.append(text[cursor:])
            break

        if heading and (not decision or heading.start() < decision.start()):
            parts.append(text[cursor:heading.start()])
            parts.append(heading.group(0))
            last_heading_level = int(heading.group(1))
            cursor = heading.end()
            continue

        assert decision is not None
        parts.append(text[cursor:decision.start()])
        block_end = matching_div_end(text, decision.start())
        if block_end is None:
            parts.append(decision.group(0))
            cursor = decision.end()
            continue

        block = text[decision.start():block_end]
        if last_heading_level == 2 and H4_OPEN_RE.search(block):
            block, open_count = H4_OPEN_RE.subn(r"<h3\1>", block)
            block, close_count = H4_CLOSE_RE.subn("</h3>", block)
            if open_count != close_count:
                raise RuntimeError("Unbalanced H4 tags while normalizing decision columns")
            changes += open_count

        block_last_heading = last_heading_in(block)
        if block_last_heading is not None:
            last_heading_level = block_last_heading

        parts.append(block)
        cursor = block_end

    return "".join(parts), changes


def normalize_path_text(path: Path, text: str) -> tuple[str, int]:
    """Apply generic and route-specific heading rules for one Lab source file."""
    normalized, changes = normalize_text(text)
    rel = path.as_posix()

    if rel.endswith(DERIVATION_PATH.as_posix()):
        replacements = (
            ("<h4>{{ item.field }}</h4>", "<h3>{{ item.field }}</h3>"),
            ("<h4>{{ row.procedure }}</h4>", "<h3>{{ row.procedure }}</h3>"),
            ("<h4>{{ mechanism.title }}</h4>", "<h3>{{ mechanism.title }}</h3>"),
        )
        for old, new in replacements:
            count = normalized.count(old)
            if count:
                normalized = normalized.replace(old, new)
                changes += count

        # Detail headings live inside the H3 card titles above.
        normalized, open_count = H5_OPEN_RE.subn(r"<h4\1>", normalized)
        normalized, close_count = H5_CLOSE_RE.subn("</h4>", normalized)
        if open_count != close_count:
            raise RuntimeError("Unbalanced H5 tags in Sales derivation page")
        changes += open_count

    if rel.endswith(PROMOTION_REVIEW_PATH.as_posix()):
        old = "const title=document.createElement('h4');"
        new = "const title=document.createElement('h3');"
        count = normalized.count(old)
        if count:
            normalized = normalized.replace(old, new)
            changes += count

    return normalized, changes


def iter_files() -> list[Path]:
    files: set[Path] = set()
    for root in ROOTS:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.is_file() and path.suffix.lower() in SOURCE_SUFFIXES:
                files.add(path)
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report required changes without writing files")
    args = parser.parse_args()

    changed_files: list[tuple[Path, int]] = []
    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        normalized, count = normalize_path_text(path, original)
        if count and normalized != original:
            changed_files.append((path, count))
            if not args.check:
                path.write_text(normalized, encoding="utf-8")

    if changed_files:
        state = "needs normalization" if args.check else "normalized"
        print(f"Heading hierarchy {state}: {len(changed_files)} file(s)")
        for path, count in changed_files:
            print(f"  {path}: {count} heading change(s)")
        return 1 if args.check else 0

    print("Heading hierarchy normalization: no changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
