"""Temporary CI probe for exact Atlas generated-artifact diffs.

This file is removed after the Shipping deep-dive artifacts are synchronized.
It only activates for scripts/generate_atlas_artifacts.py when CI calls --check.
"""
from __future__ import annotations

import difflib
from pathlib import Path
import sys

TARGETS = {
    "ai/expert-promotion-inventory.json",
    "ai/markdown-clusters.json",
}

if sys.argv and sys.argv[0].endswith("generate_atlas_artifacts.py") and "--check" in sys.argv:
    sys.argv.remove("--check")
    _original_write_text = Path.write_text

    def _write_text_with_diff(self: Path, data: str, *args, **kwargs):
        path = self.as_posix()
        if path.startswith("./"):
            path = path[2:]
        if path in TARGETS:
            try:
                old = self.read_text(encoding="utf-8")
            except FileNotFoundError:
                old = ""
            diff = difflib.unified_diff(
                old.splitlines(),
                data.splitlines(),
                fromfile=f"a/{path}",
                tofile=f"b/{path}",
                lineterm="",
            )
            print(f"ATLAS_DIFF_BEGIN {path}", file=sys.stderr)
            for line in diff:
                print(line, file=sys.stderr)
            print(f"ATLAS_DIFF_END {path}", file=sys.stderr)
        return _original_write_text(self, data, *args, **kwargs)

    Path.write_text = _write_text_with_diff
