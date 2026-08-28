import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "products" / "validation.json"


def load_protocol():
    return json.loads(PROTOCOL.read_text(encoding="utf-8"))


def test_validated_status_requires_independent_task_evidence_not_self_proof():
    protocol = load_protocol()
    assert protocol["schema_version"] == "0.1"
    assert protocol["status_claim"] == "validated"

    independence = protocol["independence"]
    assert independence["participant_implemented_tested_feature"] is False
    assert independence["participant_authored_exact_validation_fixture"] is False
    assert independence["setup_help_allowed_if_recorded"] is True

    assert protocol["author_fixture_only_qualifies"] is False
    non_qualifying = set(protocol["non_qualifying_alone"])
    assert "author_run_demo" in non_qualifying
    assert "ci_or_regression_tests" in non_qualifying
    assert "self_or_agent_review" in non_qualifying
    assert "successful_release_pipeline" in non_qualifying
    assert "documentation_or_pages_site" in non_qualifying


def test_validation_records_keep_negative_results_scope_and_limit_claims():
    protocol = load_protocol()
    assert protocol["negative_attempts_retained"] is True
    assert protocol["report_all_qualifying_attempt_outcomes"] is True
    assert set(protocol["outcomes"]) == {"success", "partial", "failed", "blocked"}

    required = set(protocol["required_record_fields"])
    assert {
        "product",
        "product_version_or_commit",
        "participant_independence",
        "task",
        "success_criteria",
        "input_class",
        "outcome",
        "defects_or_ambiguities",
        "limitations",
    } <= required

    promotion = protocol["promotion_requirements"]
    assert promotion["qualifying_external_record_exists"] is True
    assert promotion["representative_non_scripted_input"] is True
    assert promotion["negative_findings_retained"] is True
    assert promotion["status_scope_explicit"] is True
    assert promotion["limitations_explicit"] is True
    assert promotion["product_specific_stricter_threshold_wins"] is True


def test_validation_protocol_keeps_private_inputs_out_of_public_repo_by_default():
    privacy = load_protocol()["privacy"]
    assert privacy["commit_private_or_proprietary_input_by_default"] is False
    assert privacy["privacy_safe_hashes_metadata_redactions_allowed"] is True
    assert privacy["participant_identity_publication_requires_permission"] is True
