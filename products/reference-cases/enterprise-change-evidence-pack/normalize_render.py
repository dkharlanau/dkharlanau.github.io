#!/usr/bin/env python3
"""Remove renderer-only trailing horizontal whitespace from one retained SVG."""

from __future__ import annotations

import argparse
from pathlib import Path


def normalize(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    normalized = "\n".join(line.rstrip(" \t") for line in text.splitlines()) + "\n"
    path.write_text(normalized, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("svg", type=Path)
    args = parser.parse_args()
    normalize(args.svg)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
