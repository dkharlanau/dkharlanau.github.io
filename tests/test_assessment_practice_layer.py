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

    assert len(rows) == manifest["total_cases"]
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

    assert manifest["total_cases"] == inventory["published_case_count"]
    assert generation["published_case_manifest"] == "/labs/assessment/data/case-sets.json"
    assert generation["generated_inventory"] == "/labs/assessment/data/question-candidates.json"
    assert seeds["dedup_threshold"] == 0.55
    assert inventory["candidate_count"] == sum(item["status"] == "candidate" for item in inventory["items"])
    assert inventory["rejected_duplicate_count"] == sum(item["status"] == "rejected_duplicate" for item in inventory["items"])

    candidates = {item["id"]: item for item in inventory["items"] if item["status"] == "candidate"}
    assert candidates
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
    manifest = load_json("case-sets.json")
    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert f"{manifest['total_cases']} published cases unchanged" in result.stdout


def test_human_practice_routes_and_catalog_are_registered() -> None:
    expected_pages = {
        "practice-engine": ASSESSMENT / "practice-engine" / "index.html",
        "mock": ASSESSMENT / "mock" / "index.html",
        "review": ASSESSMENT / "review" / "index.html",
        "progress": ASSESSMENT / "progress" / "index.html",
        "feedback": ASSESSMENT / "feedback" / "index.html",
        "question-review": ASSESSMENT / "question-review" / "index.html",
        "candidate-semantic-review": ASSESSMENT / "candidate-semantic-review" / "index.html",
        "factual-review": ASSESSMENT / "factual-review" / "index.html",
        "evidence-coverage": ASSESSMENT / "evidence-coverage" / "index.html",
        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",
        "reasoning-coverage": ASSESSMENT / "reasoning-coverage" / "index.html",
        "reasoning-gaps": ASSESSMENT / "reasoning-gaps" / "index.html",
        "promotion-review": ASSESSMENT / "promotion-review" / "index.html",
        "human-review": ASSESSMENT / "human-review" / "index.html",
        "human-review-findings": ASSESSMENT / "human-review" / "findings" / "index.html",
        "human-review-secondary": ASSESSMENT / "human-review" / "secondary" / "index.html",
        "core-study": ASSESSMENT / "core" / "index.html",
        "core-boundaries": ASSESSMENT / "core-boundaries" / "index.html",
        "board": ASSESSMENT / "board" / "index.html",
        "cross-process": ASSESSMENT / "cross-process" / "index.html",
    }
    for name, path in expected_pages.items():
        assert path.exists(), name

    catalog = load_json("catalog.json")
    modes = {item["id"]: item for item in catalog["practice_modes"]}
    assert set(modes) == {"adaptive", "mock", "review", "progress", "feedback", "cross-process", "board"}
    assert modes["adaptive"]["route"] == "/labs/assessment/practice-engine/"
    assert modes["mock"]["route"] == "/labs/assessment/mock/"
    assert modes["review"]["route"] == "/labs/assessment/review/"
    assert modes["progress"]["route"] == "/labs/assessment/progress/"
    assert modes["feedback"]["route"] == "/labs/assessment/feedback/"
    assert modes["board"]["route"] == "/labs/assessment/board/"
    authoring = {item["id"]: item for item in catalog["authoring_tools"]}
    assert authoring["question-review"]["route"] == "/labs/assessment/question-review/"
    assert authoring["candidate-semantic-review"]["route"] == "/labs/assessment/candidate-semantic-review/"
    assert authoring["factual-review"]["route"] == "/labs/assessment/factual-review/"
    assert authoring["evidence-coverage"]["route"] == "/labs/assessment/evidence-coverage/"
    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"
    assert authoring["reasoning-coverage"]["route"] == "/labs/assessment/reasoning-coverage/"
    assert authoring["reasoning-gap-review"]["route"] == "/labs/assessment/reasoning-gaps/"
    assert authoring["promotion-review"]["route"] == "/labs/assessment/promotion-review/"
    assert authoring["human-review"]["route"] == "/labs/assessment/human-review/"
    assert authoring["core-study"]["route"] == "/labs/assessment/core/"


def test_backlog_records_completed_practice_loops() -> None:
    backlog = load_json("backlog.json")
    items = {item["id"]: item for item in backlog["items"]}

    for loop_id in ("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024", "LOOP-025", "LOOP-026", "LOOP-027", "LOOP-028", "LOOP-029", "LOOP-030", "LOOP-031", "LOOP-032", "LOOP-033", "LOOP-034", "LOOP-035", "LOOP-036", "LOOP-037", "LOOP-038", "LOOP-039", "LOOP-040", "LOOP-041", "LOOP-042", "LOOP-043", "LOOP-044", "LOOP-045", "LOOP-046", "LOOP-047", "LOOP-048"):
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
    assert sum(inventory["counts"].values()) == len(inventory["items"])
    assert set(inventory["counts"]).issubset({"human_review_candidate", "needs_structure", "public_or_indexable", "missing_source"})
    candidates = [item for item in inventory["items"] if item["state"] == "human_review_candidate"]
    assert all(item["structural_score"] >= 4 for item in candidates)
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
    assert all(item["page_verified"] is False for item in review["routes"])
    assert all(claim["status"] == "source_supported" for claim in review["claims"])
    assert all(claim["human_verification_required"] is True for claim in review["claims"])
    assert all(claim["source_refs"] for claim in review["claims"])
    assert all(claim["evidence_class"] == "sap_product_primary" for claim in review["claims"])
    assert "author_heuristic" in policy["evidence_classes"]
    allowed_primary_hosts = ("https://help.sap.com/", "https://architecture.learning.sap.com/")
    assert all(all(url.startswith(allowed_primary_hosts) for url in claim["official_evidence"]) for claim in review["claims"])
    promotion_by_route = {item["route"]: item for item in promotion["items"]}
    for route in review["routes"]:
        current = promotion_by_route[route["route"]]
        assert current["factual_review"]["status"] == "source_supported"
        assert current["factual_review"]["claim_count"] == len(route["claim_ids"])
    assert "cannot declare the complete page verified" in policy["promotion_boundary"].lower()

def test_promotion_readiness_uses_factual_review_coverage_for_priority() -> None:
    inventory = load_json("promotion-readiness.json")
    review = load_json("factual-review.json")
    reviewed_routes = {item["route"] for item in review["routes"]}
    by_route = {item["route"]: item for item in inventory["items"]}

    assert inventory["factual_review_registry"] == "/labs/assessment/data/factual-review.json"
    assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == review["summary"]["routes_reviewed"]
    assert sum(inventory["priority_counts"].values()) == inventory["scope_route_count"]
    for route in reviewed_routes:
        current = by_route[route]
        assert current["factual_review"]["status"] == "source_supported"
        assert current["factual_review"]["claim_count"] > 0
        if current["state"] == "human_review_candidate" and current["evidence_profile"].get("counts_as_source_review_debt"):
            assert current["priority"] == "P1"
            assert "human page-level verification" in current["review_reason"]
        else:
            assert current["priority"] == "P2"

    required_unreviewed = [
        item for item in inventory["items"]
        if item.get("evidence_profile", {}).get("counts_as_source_review_debt")
        and item.get("factual_review", {}).get("status") in {"not_reviewed", "needs_source_review"}
    ]
    for item in required_unreviewed:
        assert item["priority"] == "P0"
        assert "primary-source review" in item["review_reason"]

def test_evidence_coverage_is_reproducible_and_tracks_review_debt() -> None:
    coverage = load_json("evidence-coverage.json")
    factual = load_json("factual-review.json")

    assert coverage["source_contracts"]["factual_review"] == "/labs/assessment/data/factual-review.json"
    assert coverage["source_contracts"]["evidence_profile"] == "/labs/assessment/data/evidence-profile.json"
    assert len(coverage["tracks"]) == 4
    assert coverage["summary"]["unique_source_reviewed_routes"] == coverage["summary"]["unique_externally_review_required_routes"]
    assert coverage["summary"]["source_supported_claims"] == factual["summary"]["source_supported"]
    assert coverage["summary"]["unique_source_reviewed_routes"] <= coverage["summary"]["unique_externally_review_required_routes"]
    assert coverage["summary"]["unique_selective_or_heuristic_routes"] >= 3
    assert all(track["source_reviewed_routes"] <= track["externally_review_required_routes"] for track in coverage["tracks"])
    assert all(item["priority"] == "P0" for item in coverage["next_focus"])
    assert coverage["summary"]["source_supported_claims"] == sum(1 for claim in factual["claims"] if claim["status"] == "source_supported")

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_evidence_coverage.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Evidence coverage is current" in result.stdout

def test_evidence_profiles_do_not_force_sap_product_proof_for_author_heuristics() -> None:
    profile = load_json("evidence-profile.json")
    readiness = load_json("promotion-readiness.json")
    by_route = {item["route"]: item for item in readiness["items"]}

    assert profile["route_overrides"]["/labs/ai-ready/"]["counts_as_source_review_debt"] is False
    assert profile["route_overrides"]["/labs/business-ai/"]["counts_as_source_review_debt"] is False
    assert "author_heuristic" in profile["route_overrides"]["/labs/ai-ready/"]["expected_evidence_classes"]
    assert by_route["/labs/ai-ready/"]["priority"] == "P2"
    assert by_route["/labs/business-ai/"]["priority"] == "P2"
    assert by_route["/labs/enterprise-context/business-ai/"]["priority"] == "P1"

def test_broad_required_evidence_debt_is_closed_without_forcing_authored_diagnostics() -> None:
    coverage = load_json("evidence-coverage.json")
    profile = load_json("evidence-profile.json")
    readiness = load_json("promotion-readiness.json")
    by_route = {item["route"]: item for item in readiness["items"]}

    assert coverage["summary"]["coverage_percent"] == 100.0
    assert coverage["summary"]["unique_p0_evidence_debt_routes"] == 0
    assert coverage["next_focus"] == []
    assert profile["route_overrides"]["/labs/enterprise-context/sales-diagnostics/"]["counts_as_source_review_debt"] is False
    assert by_route["/labs/enterprise-context/sales-diagnostics/"]["priority"] == "P2"
    assert by_route["/labs/enterprise-context/data-governance/"]["factual_review"]["status"] == "source_supported"

def test_candidate_generation_fails_closed_behind_evidence_gate() -> None:
    inventory = load_json("question-candidates.json")
    seeds = load_json("candidate-generation-seeds.json")
    profile = load_json("evidence-profile.json")
    factual = load_json("factual-review.json")

    assert inventory["evidence_gate"]["all_emitted_candidates_evidence_eligible"] is True
    assert inventory["evidence_gate"]["blocked_seed_graphs"] == 0
    assert inventory["evidence_gate"]["eligible_seed_graphs"] == len(seeds["graphs"])
    assert all(item["evidence_gate"]["eligible"] is True for item in inventory["items"])
    assert all(item["evidence_gate"]["source_status"] == "source_verified" for item in inventory["items"])
    assert all(item["evidence_gate"]["verified_source_count"] > 0 for item in inventory["items"])

    factual_routes = {item["route"]: item for item in factual["routes"]}
    for seed in seeds["graphs"]:
        evidence_class = seed["evidence_class"]
        override = profile["route_overrides"].get(seed["human_ref"])
        route_profile = override or profile["defaults"]["enterprise_context"]
        assert evidence_class in route_profile["expected_evidence_classes"]
        if route_profile["counts_as_source_review_debt"]:
            assert seed["human_ref"] in factual_routes



def test_human_review_queue_is_reproducible_and_non_publishing() -> None:
    policy = load_json("human-review-policy.json")
    queue = load_json("human-review-queue.json")
    promotion = load_json("promotion-readiness.json")

    eligible = [
        item for item in promotion["items"]
        if item.get("state") == "human_review_candidate"
        and item.get("priority") == "P1"
        and item.get("factual_review", {}).get("status") == "source_supported"
        and item.get("evidence_profile", {}).get("counts_as_source_review_debt", False)
    ]
    assert queue["summary"]["queued_routes"] == len(queue["items"]) == len(eligible)
    core_eligible = {item["route"] for item in eligible} & set(policy["core_assessment_wave"])
    assert queue["summary"]["core_assessment_wave"] == len(core_eligible)
    assert {item["route"] for item in queue["items"] if item["wave"] == "core_assessment"} == core_eligible
    assert all(item["page_verified"] is False for item in queue["items"])
    assert all(item["state"] == "queued_for_human_review" for item in queue["items"])
    assert "never changes" in queue["boundary"].lower()

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_human_review_queue.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_core_study_map_is_reproducible_and_non_publishing() -> None:
    contract = load_json("core-study-contract.json")
    study = load_json("core-study-map.json")
    assert study["summary"]["core_routes"] == len(contract["routes"]) == 12
    assert study["summary"]["waves"] == len(contract["waves"]) == 3
    assert study["summary"]["source_supported_routes"] == 12
    promotion = load_json("promotion-readiness.json")
    by_route = {item["route"]: item for item in promotion["items"]}
    expected_verified = sum(bool(by_route[item["route"]]["verified"]) for item in study["items"])
    assert study["summary"]["page_verified_routes"] == expected_verified
    assert study["summary"]["public_or_indexable_routes"] == sum(by_route[item["route"]]["state"] == "public_or_indexable" for item in study["items"])
    assert [item["order"] for item in study["items"]] == list(range(1, 13))
    assert all(item["publication"]["verified"] == bool(by_route[item["route"]]["verified"]) for item in study["items"])
    assert all(item["assessment_question"] and item["ownership_boundary"] for item in study["items"])
    assert all(len(item["answer_path"]) >= 7 for item in study["items"])

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_core_study_map.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_core_boundary_drills_cross_supported_routes_without_publishing() -> None:
    drills = load_json("core-boundary-drills.json")
    core = load_json("core-study-map.json")
    manifest = load_json("case-sets.json")
    core_by_route = {item["route"]: item for item in core["items"]}

    assert len(drills["drills"]) >= 8
    assert len({item["id"] for item in drills["drills"]}) == len(drills["drills"])
    for drill in drills["drills"]:
        assert len(drill["routes"]) >= 2
        assert len(drill["expected_reasoning"]) >= 5
        assert len(drill["red_flags"]) >= 2
        for route in drill["routes"]:
            assert route in core_by_route
            assert core_by_route[route]["evidence"]["review_status"] == "primary_source_review_complete"
            assert core_by_route[route]["publication"]["state"] in {"human_review_candidate", "public_or_indexable", "needs_structure", "missing_source", "unknown"}

    serialized_manifest = json.dumps(manifest)
    assert "CORE-X-" not in serialized_manifest
    assert "core-boundary-drills" not in serialized_manifest

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_core_boundary_drills.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_board_mode_reuses_shared_scoring_without_second_history_store() -> None:
    board = load_json("board-mode.json")
    scoring = load_json("scoring.json")
    drills = load_json("core-boundary-drills.json")
    page = (ASSESSMENT / "board" / "index.html").read_text(encoding="utf-8")

    assert board["scoring_contract"] == "/labs/assessment/data/scoring.json"
    assert board["drill_source"] == "/labs/assessment/data/core-boundary-drills.json"
    assert board["review_map_contract"] == "/labs/assessment/data/review-map.json"
    assert board["review_handoff"]["history_write"] is False
    assert board["default_session"]["rounds"] <= len(drills["drills"])
    assert board["scoring"]["dimensions"] == [item["id"] for item in scoring["dimensions"]]
    assert board["scoring"]["maximum_score"] == scoring["maximum_score"] == 21
    assert board["scoring"]["lead_signal_minimum"] == scoring["lead_signal_minimum"]
    assert "localStorage" not in page
    assert "renderReviewHandoff" in page
    assert "dimensionScores" in page
    assert "/labs/assessment/data/review-map.json" in page
    assert "verified: false" in page
    assert "robots: noindex,follow" in page

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_board_mode.py"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_candidate_semantic_review_keeps_publication_separate_from_novelty_review() -> None:
    review = load_json("candidate-semantic-review.json")
    inventory = load_json("question-candidates.json")
    manifest = load_json("case-sets.json")
    decisions = {item["candidate_id"]: item for item in review["decisions"]}

    assert review["summary"]["published_case_change"] == 0
    assert manifest["total_cases"] == inventory["published_case_count"]
    assert decisions["CAND-PP-WRONG-QUANTITY"]["recommendation"] == "retain_for_human_promotion_review"
    assert decisions["CAND-PP-GR"]["recommendation"] == "retain_for_human_promotion_review"
    assert decisions["CAND-PP-COST"]["recommendation"] == "reject_semantic_duplicate"
    assert "ASSESS-FIN-005" in decisions["CAND-PP-COST"]["closest_published_cases"]
    assert decisions["CAND-AIAG-RAW-MCP"]["recommendation"] == "retain_for_human_promotion_review"
    assert decisions["CAND-AIAG-OVERPRIVILEGED"]["recommendation"] == "reject_semantic_duplicate"
    assert "ASSESS-AI-003" in decisions["CAND-AIAG-OVERPRIVILEGED"]["closest_published_cases"]

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_candidate_semantic_review.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_human_review_finding_contract_never_changes_publication_state() -> None:
    policy = load_json("human-review-policy.json")
    schema = load_json("human-review-finding-schema.json")
    publication = schema["properties"]["publication_effect"]["properties"]

    assert policy["finding_contract"] == "/labs/assessment/data/human-review-finding-schema.json"
    assert policy["findings_route"] == "/labs/assessment/human-review/findings/"
    assert len(policy["review_gates"]) == 7
    assert schema["properties"]["gate_results"]["minItems"] == 7
    assert schema["properties"]["gate_results"]["maxItems"] == 7
    assert publication["verified_changed"]["const"] is False
    assert publication["indexing_changed"]["const"] is False
    assert publication["status_changed"]["const"] is False

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_human_review_findings.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_secondary_human_review_priority_ranks_only_source_supported_non_core_routes() -> None:
    priority = load_json("secondary-review-priority.json")
    queue = load_json("human-review-queue.json")
    core = load_json("core-study-map.json")
    secondary = {item["route"] for item in queue["items"] if item["wave"] == "secondary"}
    core_routes = {item["route"] for item in core["items"]}
    ranked = {item["route"] for item in priority["items"]}

    assert ranked == secondary
    assert not ranked & core_routes
    assert priority["summary"]["all_source_supported"] is True
    assert priority["summary"]["all_unverified"] is True
    assert priority["summary"]["secondary_routes"] == len(priority["items"])
    assert all(item["page_verified"] is False for item in priority["items"])

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_secondary_review_priority.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_secondary_high_reuse_editorial_pass_preserves_verification_boundary() -> None:
    pages = {
        "integrations": ROOT / "labs" / "enterprise-context" / "integrations" / "index.md",
        "sales-processes": ROOT / "labs" / "enterprise-context" / "sales-processes" / "index.html",
        "transportation-management": ROOT / "labs" / "enterprise-context" / "transportation-management" / "index.html",
    }
    required_tokens = {
        "integrations": ["id=\"lead-answer-frame\"", "Explain the dependency before the platform.", "Evidence boundary:"],
        "sales-processes": ["id=\"lead-branch-answer\"", "Start from standard sell-from-stock", "Evidence boundary:"],
        "transportation-management": ["id=\"lead-answer-frame\"", "Demand is not the plan", "Evidence boundary:"],
    }
    for key, path in pages.items():
        page = path.read_text(encoding="utf-8")
        for token in required_tokens[key]:
            assert token in page, (key, token)


def test_reasoning_pressure_coverage_matches_published_case_metadata() -> None:
    coverage = load_json("reasoning-pressure-coverage.json")
    manifest = load_json("case-sets.json")
    catalog = load_json("catalog.json")

    assert coverage["summary"]["published_cases"] == manifest["total_cases"]
    assert {item["track"] for item in coverage["tracks"]} == {item["id"] for item in catalog["tracks"]}
    assert coverage["policy"]["lead_pressure_levels"] == ["diagnose", "design", "challenge"]
    assert coverage["policy"]["minimum_published_cases_per_lead_pressure_level"] == 2

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_reasoning_coverage.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_ai_agent_diagnose_seed_has_claim_level_primary_evidence() -> None:
    factual = load_json("factual-review.json")
    seeds = load_json("candidate-generation-seeds.json")
    route = next(item for item in factual["routes"] if item["route"] == "/labs/enterprise-context/business-ai/agents/")
    claims = {item["id"]: item for item in factual["claims"]}
    seed = next(item for item in seeds["graphs"] if item["path"].endswith("agent_architecture.yml"))

    assert route["review_status"] == "primary_source_review_complete"
    assert set(route["claim_ids"]) == {"FACT-AIAG-001", "FACT-AIAG-002"}
    assert all(claims[claim_id]["status"] == "source_supported" for claim_id in route["claim_ids"])
    assert seed["track"] == "ai-data"
    assert seed["level"] == "diagnose"
    assert set(seed["failure_sources"]) == {"FAIL-AI-AGENT-RAW-MCP", "FAIL-AI-AGENT-OVERPRIVILEGED"}
    assert seed["human_ref"] == "/labs/enterprise-context/business-ai/agents/"

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_non_diagnostic_reasoning_gap_candidates_match_thin_cells_and_stay_unpublished() -> None:
    gaps = load_json("reasoning-gap-candidates.json")
    coverage = load_json("reasoning-pressure-coverage.json")
    manifest = load_json("case-sets.json")

    expected = {(item["track"], item["level"]) for item in coverage["authoring_gaps"]}
    actual = {(item["track"], item["level"]) for item in gaps["gap_plan"]}
    assert actual == expected
    assert gaps["summary"]["published_cases_changed"] == 0
    assert gaps["summary"]["new_review_candidates"] == 2
    assert {item["level"] for item in gaps["candidates"]} == {"design", "challenge"}
    published_ids = set()
    for case_set in manifest["sets"]:
        published_ids.update(item["id"] for item in load_jsonl(ROOT / case_set["url"].lstrip("/")))
    assert not published_ids & {item["id"] for item in gaps["candidates"]}

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_reasoning_gap_candidates.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_reasoning_gap_semantic_review_keeps_novel_signals_in_human_queue_only() -> None:
    review = load_json("reasoning-gap-semantic-review.json")
    candidates = load_json("reasoning-gap-candidates.json")
    decisions = {item["candidate_id"]: item for item in review["decisions"]}

    assert set(decisions) == {item["id"] for item in candidates["candidates"]}
    assert decisions["RCAND-SALES-DESIGN-SUPPLY-MODEL"]["recommendation"] == "retain_for_human_promotion_review"
    assert decisions["RCAND-AI-CHALLENGE-AUTONOMY"]["recommendation"] == "retain_for_human_promotion_review"
    assert review["summary"]["published_case_change"] == 0

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_reasoning_gap_semantic_review.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_every_active_generated_candidate_has_one_semantic_decision() -> None:
    inventory = load_json("question-candidates.json")
    review = load_json("candidate-semantic-review.json")
    active = {item["id"] for item in inventory["items"] if item["status"] == "candidate"}
    decisions = {item["candidate_id"] for item in review["decisions"]}
    assert decisions == active
    assert review["summary"]["retain_for_human_promotion_review"] == 5
    assert review["summary"]["reject_semantic_duplicate"] == 2


def test_promotion_review_packet_contains_only_semantic_survivors_and_zero_approvals() -> None:
    packet = load_json("promotion-review-packet.json")
    generated_review = load_json("candidate-semantic-review.json")
    gap_review = load_json("reasoning-gap-semantic-review.json")
    expected = {item["candidate_id"] for item in generated_review["decisions"] if item["recommendation"] == "retain_for_human_promotion_review"}
    expected |= {item["candidate_id"] for item in gap_review["decisions"] if item["recommendation"] == "retain_for_human_promotion_review"}
    assert {item["candidate_id"] for item in packet["items"]} == expected
    assert packet["summary"]["pending_candidates"] == len(expected)
    assert packet["summary"]["approved_candidates"] == 0
    assert all(item["human_decision"]["status"] == "pending_human_review" for item in packet["items"])
    assert all(item["human_decision"]["decision"] is None for item in packet["items"])

    result = subprocess.run(
        [sys.executable, "scripts/validate_assessment_promotion_review_packet.py"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
