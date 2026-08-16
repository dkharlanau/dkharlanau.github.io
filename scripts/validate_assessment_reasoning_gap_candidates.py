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
    semantic = load("candidate-semantic-review.json")
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
    for candidate in gaps["candidates"]:
        if candidate["id"] in published_ids:
            errors.append(f"Review-stage reasoning candidate entered published manifest: {candidate['id']}")
    if gaps["summary"]["published_cases_changed"] != 0:
        errors.append("Reasoning-gap candidates must not change published cases")

    semantic_decisions = {item["candidate_id"]: item for item in semantic["decisions"]}
    raw = semantic_decisions.get("CAND-AIAG-RAW-MCP")
    if not raw or raw.get("recommendation") != "retain_for_human_promotion_review":
        errors.append("AI/Data Diagnose thin cell must reuse the retained RAW-MCP semantic signal")

    design_contract = gaps.get("pattern_contract", {}).get("design", [])
    challenge_contract = gaps.get("pattern_contract", {}).get("challenge", [])
    if len(design_contract) < 6 or len(challenge_contract) < 6:
        errors.append("Design and Challenge pattern contracts must each define at least six reasoning moves")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/reasoning-gap-candidates.json",
        "RCAND-SALES-DESIGN-SUPPLY-MODEL",
        "RCAND-AI-CHALLENGE-AUTONOMY",
    ):
        if token not in page:
            errors.append(f"Reasoning-gap page missing token: {token}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print("Reasoning-gap candidates valid: 3 thin cells covered by review-stage signals, 2 new non-diagnostic candidates, published cases unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
