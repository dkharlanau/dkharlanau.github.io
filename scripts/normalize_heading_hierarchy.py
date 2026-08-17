#!/usr/bin/env python3
"""Normalize card heading groups that sit directly under an H2 section.

Some Lab pages use ``ecg-decision-columns`` for peer cards. When the group is
introduced directly by an H2, those card titles are H3 headings. Nested groups
that follow an H3 keep H4 titles.

Use ``--check`` to report files that still need normalization without writing.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

ROOTS = (Path("labs/assessment"), Path("labs/enterprise-context"))
HEADING_RE = re.compile(r"<h([1-6])\b[^>]*>.*?</h\1>", re.IGNORECASE | re.DOTALL)
OPEN_DECISION_RE = re.compile(
    r'<div\b[^>]*class=["\'][^"\']*\becg-decision-columns\b[^"\']*["\'][^>]*>',
    re.IGNORECASE,
)
DIV_TOKEN_RE = re.compile(r"</?div\b[^>]*>", re.IGNORECASE)
H4_OPEN_RE = re.compile(r"<h4(\b[^>]*)>", re.IGNORECASE)
H4_CLOSE_RE = re.compile(r"</h4>", re.IGNORECASE)


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


def iter_files() -> list[Path]:
    files: list[Path] = []
    for root in ROOTS:
        if root.exists():
            files.extend(path for path in root.rglob("*.html") if path.is_file())
    return sorted(files)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report required changes without writing files")
    args = parser.parse_args()

    changed_files: list[tuple[Path, int]] = []
    for path in iter_files():
        original = path.read_text(encoding="utf-8")
        normalized, count = normalize_text(original)
        if count and normalized != original:
            changed_files.append((path, count))
            if not args.check:
                path.write_text(normalized, encoding="utf-8")

    if changed_files:
        state = "needs normalization" if args.check else "normalized"
        print(f"Heading hierarchy {state}: {len(changed_files)} file(s)")
        for path, count in changed_files:
            print(f"  {path}: {count} H4 -> H3")
        return 1 if args.check else 0

    print("Heading hierarchy normalization: no changes needed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
