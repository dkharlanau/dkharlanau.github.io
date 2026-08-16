#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "human-review" / "secondary" / "index.html"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    priority = load("secondary-review-priority.json")
    queue = load("human-review-queue.json")
    core = load("core-study-map.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    secondary_routes = {item["route"] for item in queue["items"] if item.get("wave") == "secondary"}
    core_routes = {item["route"] for item in core["items"]}
    ranked_routes = {item["route"] for item in priority["items"]}

    if ranked_routes != secondary_routes:
        errors.append("Secondary priority must rank exactly the secondary human-review routes")
    if ranked_routes & core_routes:
        errors.append("Secondary priority must not contain Core 12 routes")
    if priority["summary"]["secondary_routes"] != len(priority["items"]):
        errors.append("Secondary priority summary count mismatch")
    if not priority["summary"]["all_source_supported"]:
        errors.append("Every ranked secondary route must be source-supported")
    if not priority["summary"]["all_unverified"]:
        errors.append("Secondary priority must not treat any page as verified")
    if [item["priority_position"] for item in priority["items"]] != list(range(1, len(priority["items"]) + 1)):
        errors.append("Secondary priority positions must be contiguous")
    if any(priority["items"][i]["priority_score"] < priority["items"][i + 1]["priority_score"] for i in range(len(priority["items"]) - 1)):
        errors.append("Secondary priority must be sorted by descending score")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/secondary-review-priority.json",
        "/labs/assessment/human-review/findings/",
    ):
        if token not in page:
            errors.append(f"Secondary review page is missing token: {token}")

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_secondary_review_priority.py", "--check"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 0:
        errors.append(result.stdout + result.stderr)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Secondary human-review priority valid: {len(priority['items'])} routes ranked, no verification changes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
