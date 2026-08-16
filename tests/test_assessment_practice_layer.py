from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT = ROOT / "labs" / "assessment"
DATA = ASSESSMENT / "data"

DIMENSIONS = {
    "business_goal",
    "owner",
    "process_flow",
    "decision_logic",
    "boundary",
    "failure_and_evidence",
    "trade_off",
}
TRACKS = {"sales", "procurement-logistics", "integration-architecture", "ai-data"}


def load_json(name: str) -> dict:
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def test_assessment_case_manifest_matches_real_case_files() -> None:
    manifest = load_json("case-sets.json")
    rows: list[dict] = []

    for case_set in manifest["sets"]:
        path = ROOT / case_set["url"].lstrip("/")
        assert path.exists(), case_set["url"]
        current = load_jsonl(path)
        assert len(current) == case_set["count"], case_set["id"]
        rows.extend(current)

    assert len(rows) == manifest["total_cases"] == 59
    ids = [row["id"] for row in rows]
    assert len(ids) == len(set(ids)), "assessment case ids must be unique"


def test_practice_contracts_share_one_scoring_model() -> None:
    scoring = load_json("scoring.json")
    attempt = load_json("attempt-schema.json")
    profile = load_json("profile-schema.json")
    adaptive = load_json("adaptive-selection.json")
    mock = load_json("mock-session.json")
    portability = load_json("history-portability.json")

    scoring_dimensions = {item["id"] for item in scoring["dimensions"]}
    assert scoring_dimensions == DIMENSIONS
    assert scoring["maximum_score"] == 21

    score_properties = attempt["properties"]["scores"]["properties"]
    assert set(score_properties) == DIMENSIONS
    assert mock["scoring_contract"] == "/labs/assessment/data/scoring.json"
    assert mock["attempt_contract"] == "/labs/assessment/data/attempt-schema.json"
    assert adaptive["attempt_contract"] == "/labs/assessment/data/attempt-schema.json"
    assert portability["attempt_contract"] == "/labs/assessment/data/attempt-schema.json"
    assert "dimension_signals" in profile["properties"]


def test_mock_session_is_balanced_by_contract() -> None:
    mock = load_json("mock-session.json")
    default = mock["default_session"]

    assert default["case_count"] == 8
    assert set(default["track_targets"]) == TRACKS
    assert sum(default["track_targets"].values()) == default["case_count"]
    assert sum(default["level_targets"].values()) == default["case_count"]
    assert default["cross_process_minimum"] >= 2


def test_review_map_covers_every_scoring_dimension_and_track() -> None:
    review = load_json("review-map.json")

    assert set(review["dimension_routes"]) == DIMENSIONS
    assert set(review["track_routes"]) == TRACKS
    for dimension, item in review["dimension_routes"].items():
        assert item["routes"], dimension
        assert item["review_question"], dimension
        for route in item["routes"]:
            assert route["url"].startswith("/labs/")


def test_history_portability_keeps_attempts_as_source_of_truth() -> None:
    portability = load_json("history-portability.json")

    assert portability["storage_key"] == "sapLeadAssessmentAttemptsV1"
    assert portability["export_format"]["root"]["format"] == "sap-lead-assessment-history"
    assert set(portability["merge_modes"]) == {"merge", "replace"}
    assert "derived" in portability["profile_rule"].lower()
    assert "server" in portability["privacy"].lower()


def test_human_practice_routes_and_catalog_are_registered() -> None:
    expected_pages = {
        "practice-engine": ASSESSMENT / "practice-engine" / "index.html",
        "mock": ASSESSMENT / "mock" / "index.html",
        "review": ASSESSMENT / "review" / "index.html",
        "progress": ASSESSMENT / "progress" / "index.html",
        "cross-process": ASSESSMENT / "cross-process" / "index.html",
    }
    for name, path in expected_pages.items():
        assert path.exists(), name

    catalog = load_json("catalog.json")
    modes = {item["id"]: item for item in catalog["practice_modes"]}
    assert set(modes) == {"adaptive", "mock", "review", "progress", "cross-process"}
    assert modes["adaptive"]["route"] == "/labs/assessment/practice-engine/"
    assert modes["mock"]["route"] == "/labs/assessment/mock/"
    assert modes["review"]["route"] == "/labs/assessment/review/"
    assert modes["progress"]["route"] == "/labs/assessment/progress/"


def test_backlog_records_completed_practice_loops() -> None:
    backlog = load_json("backlog.json")
    items = {item["id"]: item for item in backlog["items"]}

    for loop_id in ("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013"):
        assert items[loop_id]["status"] == "done"
        assert items[loop_id]["outputs"]
