import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "products" / "compatibility.json"


def load_policy():
    return json.loads(POLICY.read_text(encoding="utf-8"))


def test_contract_versions_and_consumer_support_are_explicit():
    policy = load_policy()
    assert policy["schema_version"] == "0.1"
    assert policy["scope"] == "portfolio-cross-repository-contract-evolution"
    producer = policy["producer_rules"]
    assert producer["public_contract_version_explicit_where_compatibility_matters"] is True
    assert producer["reuse_same_contract_version_for_changed_semantics"] is False
    assert producer["breaking_contract_change_requires_new_contract_version"] is True
    consumer = policy["consumer_rules"]
    assert consumer["supported_versions_explicit"] is True
    assert consumer["assume_unknown_version_is_latest_compatible"] is False
    assert consumer["fail_required_unsupported_version_explicitly"] is True
    assert consumer["guess_or_coerce_unknown_semantics"] is False


def test_semantic_authority_and_identity_changes_are_breaking():
    policy = load_policy()
    breaking = set(policy["breaking_change_examples"])
    assert "change_identity_or_canonicalization_semantics" in breaking
    assert "change_evidence_meaning_toward_false_positive_assurance" in breaking
    assert "widen_execution_or_agent_authority" in breaking
    assert "change_semantic_ownership_boundary" in breaking
    adapter = policy["adapter_rules"]
    assert adapter == {
        "explicit": True,
        "deterministic": True,
        "tested_against_source_and_target_versions": True,
        "silent_guessing": False,
    }


def test_cross_repo_consumers_must_test_future_version_failure():
    required = set(load_policy()["cross_repo_test_minimum"])
    assert "supported_current_fixture" in required
    assert "unsupported_future_version_fixture" in required
    assert "integrity_or_provenance_mismatch_when_pinned" in required
