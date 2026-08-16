#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "reasoning-gaps" / "index.html"

def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main() -> int:
    gaps = load("reasoning-gap-candidates.json")
    coverage = load("reasoning-pressure-coverage.json")
    factual = load("factual-review.json")
    manifest = load("case-sets.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    coverage_gaps = {(item["track"], item["level"]): item for item in coverage["authoring_gaps"]}
    plan = {(item["track"], item["level"]): item for item in gaps["gap_plan"]}
    if set(plan) != set(coverage_gaps):
        errors.append("Reasoning-gap plan must match the current published authoring gaps exactly")
    for key, item in plan.items():
        if item["published_count"] != coverage_gaps[key]["count"]:
            errors.append(f"Published count mismatch for reasoning gap {key}")

    candidate_ids = {item["id"] for item in gaps["candidates"]}
    planned_signals = {item.get("review_stage_signal") for item in gaps["gap_plan"]}
    if not candidate_ids <= planned_signals:
        errors.append("Every authored reasoning-gap candidate must correspond to a current gap-plan signal")
    if gaps["summary"]["new_review_candidates"] != len(gaps["candidates"]):
        errors.append("Reasoning-gap candidate summary count mismatch")
    if gaps["summary"]["thin_cells_with_review_stage_signal"] != len(gaps["gap_plan"]):
        errors.append("Reasoning-gap thin-cell summary count mismatch")

    factual_routes = {item["route"]: item for item in factual["routes"]}
    for candidate in gaps["candidates"]:
        if candidate["level"] not in {"design", "challenge"}:
            errors.append(f"Reasoning-gap candidate must be Design or Challenge: {candidate['id']}")
        if len(candidate.get("expected_points", [])) < 6:
            errors.append(f"Candidate needs at least six expected points: {candidate['id']}")
        if len(candidate.get("red_flags", [])) < 2:
            errors.append(f"Candidate needs at least two red flags: {candidate['id']}")
        if not candidate.get("novelty_note"):
            errors.append(f"Candidate needs an explicit novelty note: {candidate['id']}")
        for route in candidate.get("evidence_routes", []):
            review = factual_routes.get(route)
            if not review:
                errors.append(f"Evidence route is not in factual review: {route}")
                continue
            if review.get("review_status") != "primary_source_review_complete":
                errors.append(f"Evidence route is not source-review complete: {route}")
            if not review.get("claim_ids"):
                errors.append(f"Evidence route has no reviewed claim ids: {route}")
            if review.get("page_verified") is not False:
                errors.append(f"Reasoning-gap authoring must not require verified pages: {route}")

    published_ids = set()
    for case_set in manifest["sets"]:
        published_ids.update(item["id"] for item in load_jsonl(ROOT / case_set["url"].lstrip("/")))
    if published_ids & candidate_ids:
        errors.append("Review-stage reasoning candidate entered published manifest")
    if gaps["summary"]["published_cases_changed"] != 0:
        errors.append("Reasoning-gap candidates must not change published cases")

    for pattern in ("design", "challenge"):
        if len(gaps.get("pattern_contract", {}).get(pattern, [])) < 6:
            errors.append(f"{pattern.title()} pattern contract must define at least six reasoning moves")

    for token in ("verified: false", "robots: noindex,follow", "/labs/assessment/data/reasoning-gap-candidates.json"):
        if token not in page:
            errors.append(f"Reasoning-gap page missing token: {token}")
    for candidate_id in candidate_ids:
        if candidate_id not in page:
            errors.append(f"Reasoning-gap page missing active candidate: {candidate_id}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Reasoning-gap candidates valid: {len(gaps['gap_plan'])} current thin cells, {len(gaps['candidates'])} authored review candidates, published cases unchanged.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
