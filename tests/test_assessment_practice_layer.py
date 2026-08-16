from __future__ import annotations

import json
import subprocess
import sys
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


def test_feedback_schema_and_calibration_policy_preserve_provenance() -> None:
    schema = load_json("feedback-schema.json")
    policy = load_json("calibration-policy.json")

    source_values = set(schema["properties"]["source_type"]["enum"])
    assert source_values == {
        "self_reflection",
        "peer_review",
        "manager_feedback",
        "interviewer_feedback",
        "formal_assessment_result",
    }

    observation = schema["properties"]["observations"]["items"]["properties"]
    assert set(observation["dimension_id"]["enum"]) == DIMENSIONS | {None}
    assert set(observation["track"]["enum"]) == TRACKS | {None}
    assert policy["feedback_contract"] == "/labs/assessment/data/feedback-schema.json"
    assert policy["scoring_contract"] == "/labs/assessment/data/scoring.json"
    assert "explicit human-reviewed accepted decision" in policy["calibration_decision"]["acceptance_rule"]
    assert any("Do not create external feedback records" in rule for rule in policy["principles"])


def test_graph_backed_candidate_inventory_is_review_stage_only() -> None:
    manifest = load_json("case-sets.json")
    inventory = load_json("question-candidates.json")
    seeds = load_json("candidate-generation-seeds.json")
    generation = load_json("question-generation.json")

    assert manifest["total_cases"] == inventory["published_case_count"] == 59
    assert generation["published_case_manifest"] == "/labs/assessment/data/case-sets.json"
    assert generation["generated_inventory"] == "/labs/assessment/data/question-candidates.json"
    assert seeds["dedup_threshold"] == 0.55
    assert inventory["candidate_count"] == 2
    assert inventory["rejected_duplicate_count"] == 12

    candidates = {item["id"]: item for item in inventory["items"] if item["status"] == "candidate"}
    assert set(candidates) == {"CAND-BIL-WRONG-REFERENCE", "CAND-INTOPS-OWNERSHIP"}
    for item in inventory["items"]:
        assert item["source_refs"]
        assert item["evidence_map"]
        assert len(item["evidence_map"]) == len(item["expected_points"])
        assert item["dedup_signature"]
        if item["status"] == "candidate":
            assert not item["dedup"]["matching_case_ids"]
        if item["status"] == "rejected_duplicate":
            assert item["dedup"]["matching_case_ids"]


def test_graph_backed_candidate_generator_is_reproducible() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "59 published cases unchanged" in result.stdout


def test_human_practice_routes_and_catalog_are_registered() -> None:
    expected_pages = {
        "practice-engine": ASSESSMENT / "practice-engine" / "index.html",
        "mock": ASSESSMENT / "mock" / "index.html",
        "review": ASSESSMENT / "review" / "index.html",
        "progress": ASSESSMENT / "progress" / "index.html",
        "feedback": ASSESSMENT / "feedback" / "index.html",
        "question-review": ASSESSMENT / "question-review" / "index.html",
        "factual-review": ASSESSMENT / "factual-review" / "index.html",
        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",
        "cross-process": ASSESSMENT / "cross-process" / "index.html",
    }
    for name, path in expected_pages.items():
        assert path.exists(), name

    catalog = load_json("catalog.json")
    modes = {item["id"]: item for item in catalog["practice_modes"]}
    assert set(modes) == {"adaptive", "mock", "review", "progress", "feedback", "cross-process"}
    assert modes["adaptive"]["route"] == "/labs/assessment/practice-engine/"
    assert modes["mock"]["route"] == "/labs/assessment/mock/"
    assert modes["review"]["route"] == "/labs/assessment/review/"
    assert modes["progress"]["route"] == "/labs/assessment/progress/"
    assert modes["feedback"]["route"] == "/labs/assessment/feedback/"
    authoring = {item["id"]: item for item in catalog["authoring_tools"]}
    assert authoring["question-review"]["route"] == "/labs/assessment/question-review/"
    assert authoring["factual-review"]["route"] == "/labs/assessment/factual-review/"
    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"


def test_backlog_records_completed_practice_loops() -> None:
    backlog = load_json("backlog.json")
    items = {item["id"]: item for item in backlog["items"]}

    for loop_id in ("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019"):
        assert items[loop_id]["status"] == "done"
        assert items[loop_id]["outputs"]


def test_browser_modes_use_shared_portability_and_lead_threshold() -> None:
    practice = (ASSESSMENT / "practice-engine" / "index.html").read_text(encoding="utf-8")
    mock = (ASSESSMENT / "mock" / "index.html").read_text(encoding="utf-8")

    assert "format:'sap-lead-assessment-history'" in practice
    assert "sap-lead-assessment-history.json" in practice
    assert "lead_signal:total >= 18" not in mock
    assert "thresholds.case_total_lead_minimum" in mock
    assert "fetch('/labs/assessment/data/scoring.json'" in mock

def test_promotion_readiness_audit_is_reproducible_and_non_publishing() -> None:
    policy = load_json("promotion-readiness-policy.json")
    inventory = load_json("promotion-readiness.json")

    assert inventory["policy"] == "/labs/assessment/data/promotion-readiness-policy.json"
    assert inventory["scope_route_count"] == len(inventory["items"])
    assert inventory["counts"].get("human_review_candidate") == len(inventory["items"])
    assert all(item["structural_score"] >= 4 for item in inventory["items"])
    assert all(item["verified"] is False for item in inventory["items"])
    assert "never changes status" in policy["promotion_rule"].lower()

    result = subprocess.run(
        [sys.executable, "scripts/audit_assessment_promotion_readiness.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert f'{inventory["scope_route_count"]} routes' in result.stdout

def test_factual_review_keeps_source_support_separate_from_page_verification() -> None:
    policy = load_json("factual-review-policy.json")
    review = load_json("factual-review.json")
    promotion = load_json("promotion-readiness.json")

    assert review["policy"] == "/labs/assessment/data/factual-review-policy.json"
    assert review["summary"]["routes_reviewed"] == len(review["routes"])
    assert review["summary"]["claims_reviewed"] == len(review["claims"])
    assert review["summary"]["source_supported"] == sum(1 for claim in review["claims"] if claim["status"] == "source_supported")
    assert review["summary"]["source_conflict"] == sum(1 for claim in review["claims"] if claim["status"] == "source_conflict")
    assert review["summary"]["human_verification_required"] == sum(1 for claim in review["claims"] if claim["human_verification_required"])
    assert review["summary"]["routes_reviewed"] == 6
    assert review["summary"]["claims_reviewed"] == 23
    assert all(item["page_verified"] is False for item in review["routes"])
    assert all(claim["status"] == "source_supported" for claim in review["claims"])
    assert all(claim["human_verification_required"] is True for claim in review["claims"])
    assert all(claim["source_refs"] for claim in review["claims"])
    assert all(all(url.startswith("https://help.sap.com/") for url in claim["official_evidence"]) for claim in review["claims"])
    promotion_by_route = {item["route"]: item for item in promotion["items"]}
    for route in review["routes"]:
        assert promotion_by_route[route["route"]]["verified"] is False
    assert "cannot declare the complete page verified" in policy["promotion_boundary"].lower()

def test_promotion_readiness_uses_factual_review_coverage_for_priority() -> None:
    inventory = load_json("promotion-readiness.json")
    review = load_json("factual-review.json")
    reviewed_routes = {item["route"] for item in review["routes"]}
    by_route = {item["route"]: item for item in inventory["items"]}

    assert inventory["factual_review_registry"] == "/labs/assessment/data/factual-review.json"
    assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 6
    assert sum(inventory["priority_counts"].values()) == inventory["scope_route_count"]
    for route in reviewed_routes:
        assert by_route[route]["factual_review"]["status"] == "source_supported"
        assert by_route[route]["factual_review"]["claim_count"] > 0
        assert by_route[route]["priority"] == "P1"
        assert "human page-level verification" in by_route[route]["review_reason"]

    assert by_route["/labs/enterprise-context/pricing/"]["factual_review"]["status"] == "not_reviewed"
    assert by_route["/labs/enterprise-context/pricing/"]["priority"] == "P0"
    assert "primary-source review" in by_route["/labs/enterprise-context/pricing/"]["review_reason"]

