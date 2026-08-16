#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "reasoning-coverage" / "index.html"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    coverage = load("reasoning-pressure-coverage.json")
    manifest = load("case-sets.json")
    catalog = load("catalog.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    expected_tracks = {track["id"] for track in catalog["tracks"]}
    actual_tracks = {track["track"] for track in coverage["tracks"]}
    if actual_tracks != expected_tracks:
        errors.append("Reasoning coverage must include every assessment track exactly once")
    if coverage["summary"]["published_cases"] != manifest["total_cases"]:
        errors.append("Reasoning coverage published count must match the case manifest")
    if coverage["policy"]["lead_pressure_levels"] != ["diagnose", "design", "challenge"]:
        errors.append("Lead-pressure levels must remain Diagnose, Design, and Challenge")
    if coverage["policy"]["minimum_published_cases_per_lead_pressure_level"] != 2:
        errors.append("Reasoning coverage minimum pressure threshold must remain explicit and stable")
    for track in coverage["tracks"]:
        if [item["level"] for item in track["levels"]] != ["explain", "trace", "diagnose", "design", "challenge"]:
            errors.append(f"Unexpected level order for track {track['track']}")
        if sum(item["count"] for item in track["levels"]) != track["total_cases"]:
            errors.append(f"Track total mismatch for {track['track']}")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/reasoning-pressure-coverage.json",
        "Diagnose, Design, and Challenge",
    ):
        if token not in page:
            errors.append(f"Reasoning coverage page is missing token: {token}")

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_reasoning_coverage.py", "--check"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 0:
        errors.append(result.stdout + result.stderr)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Reasoning pressure coverage valid: {coverage['summary']['published_cases']} cases and {len(coverage['authoring_gaps'])} authoring gaps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
