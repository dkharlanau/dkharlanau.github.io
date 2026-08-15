#!/usr/bin/env python3
"""Run all AI Ready practice self-tests."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
PROJECTS = [
    BASE_DIR / "model-benchmark" / "benchmark.py",
    BASE_DIR / "context-experiment" / "context_experiment.py",
    BASE_DIR / "retrieval-benchmark" / "retrieval_benchmark.py",
    BASE_DIR / "local-assistant" / "app.py",
]


def main() -> int:
    for script in PROJECTS:
        completed = subprocess.run(
            [sys.executable, str(script), "--self-test"],
            cwd=BASE_DIR.parent.parent.parent,
            check=False,
            text=True,
            capture_output=True,
        )
        if completed.stdout:
            print(completed.stdout.strip())
        if completed.returncode != 0:
            if completed.stderr:
                print(completed.stderr, file=sys.stderr)
            return completed.returncode
    print("AI Ready practice: all self-tests passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
