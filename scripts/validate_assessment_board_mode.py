#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
CONTRACT = DATA / "board-mode.json"
DRILLS = DATA / "core-boundary-drills.json"
SCORING = DATA / "scoring.json"
REVIEW_MAP = DATA / "review-map.json"
PAGE = ROOT / "labs" / "assessment" / "board" / "index.html"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors: list[str] = []
    contract = load(CONTRACT)
    drills = load(DRILLS)
    scoring = load(SCORING)
    review_map = load(REVIEW_MAP)
    page = PAGE.read_text(encoding="utf-8")

    scoring_dimensions = [item["id"] for item in scoring["dimensions"]]
    if contract.get("scoring", {}).get("dimensions") != scoring_dimensions:
        errors.append("Board Mode scoring dimensions must exactly match scoring.json")
    if contract.get("scoring", {}).get("maximum_score") != scoring.get("maximum_score"):
        errors.append("Board Mode maximum score must come from scoring.json")
    if contract.get("scoring", {}).get("lead_signal_minimum") != scoring.get("lead_signal_minimum"):
        errors.append("Board Mode Lead threshold must match scoring.json")

    default = contract.get("default_session", {})
    rounds = int(default.get("rounds", 0) or 0)
    seconds = int(default.get("seconds_per_round", 0) or 0)
    if rounds < 1 or rounds > len(drills.get("drills", [])):
        errors.append("Board Mode round count must fit the drill set")
    if seconds < 120 or seconds > 900:
        errors.append("Board Mode seconds_per_round must stay between 2 and 15 minutes")
    if len(default.get("answer_sequence", [])) < 5:
        errors.append("Board Mode answer sequence must contain at least five reasoning steps")

    handoff = contract.get("review_handoff", {})
    if contract.get("review_map_contract") != "/labs/assessment/data/review-map.json":
        errors.append("Board Mode must reference the shared review-map contract")
    if handoff.get("history_write") is not False:
        errors.append("Board Mode review handoff must not write persistent history")
    if set(review_map.get("dimension_routes", {})) != set(scoring_dimensions):
        errors.append("Review map must cover every Board Mode scoring dimension")
    if "lowest average" not in str(handoff.get("selection", "")).lower():
        errors.append("Board Mode review handoff must rank weak dimensions from session averages")

    boundary = str(contract.get("session_boundary", "")).lower()
    for token in ("does not publish", "write assessment history automatically"):
        if token not in boundary:
            errors.append(f"Board Mode session boundary is missing: {token}")

    if "verified: false" not in page or "robots: noindex,follow" not in page:
        errors.append("Board Mode page must stay draft/unverified/noindex")
    for endpoint in (
        "/labs/assessment/data/core-boundary-drills.json",
        "/labs/assessment/data/scoring.json",
        "/labs/assessment/data/board-mode.json",
        "/labs/assessment/data/review-map.json",
    ):
        if endpoint not in page:
            errors.append(f"Board Mode page is missing endpoint: {endpoint}")
    for token in ("board-review-handoff", "dimensionScores", "renderReviewHandoff"):
        if token not in page:
            errors.append(f"Board Mode review handoff implementation is missing token: {token}")
    if "localStorage" in page or ".setItem(" in page:
        errors.append("Board Mode must not create a second persistent history implementation")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    contract = load(CONTRACT)
    print(
        "Board Mode valid: "
        f"{contract['default_session']['rounds']} rounds, "
        f"{contract['default_session']['seconds_per_round']} seconds each, "
        f"shared {contract['scoring']['maximum_score']}-point scoring and targeted review handoff."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
