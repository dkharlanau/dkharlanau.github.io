import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCTS = ROOT / "products"


def _load(name: str):
    return json.loads((PRODUCTS / name).read_text(encoding="utf-8"))


def test_external_validation_policy_retains_negative_evidence_and_scope():
    policy = _load("validation-policy.json")

    assert policy["schema_version"] == "0.1"
    assert set(policy["validation_dimensions"]) == {
        "usability",
        "correctness",
        "production_suitability",
    }
    assert set(policy["outcome_statuses"]) == {
        "passed",
        "partial",
        "failed",
        "inconclusive",
    }

    qualifying = policy["qualifying_attempt_requires"]
    assert qualifying["participant_independent_from_implementation"] is True
    assert qualifying["participant_did_not_author_test_fixture"] is True
    assert qualifying["pinned_product_commit"] is True
    assert qualifying["limitations_retained"] is True

    promotion = policy["promotion_rules"]
    assert promotion["validated_is_scoped_not_universal"] is True
    assert promotion["all_known_qualifying_attempts_in_stated_cohort_retained"] is True
    assert promotion["failed_partial_and_inconclusive_attempts_remain_in_denominator"] is True
    assert promotion["public_status_must_name_dimension_and_sample_or_scope"] is True
    assert promotion["usability_or_correctness_does_not_imply_production_suitability"] is True
    assert promotion["universal_minimum_sample_size"] is None

    human = (PRODUCTS / "VALIDATION.md").read_text(encoding="utf-8").lower()
    assert "failed qualifying attempt is still validation evidence" in human
    assert "scoped evidence statement" in human


def test_validation_record_contract_and_example_are_privacy_safe():
    schema = _load("validation-record.schema.json")
    example = _load("validation-record.example.json")

    required = set(schema["required"])
    assert required.issubset(example)
    assert schema["properties"]["participant"]["properties"]["independent"]["const"] is True
    assert schema["properties"]["participant"]["properties"]["authored_test_fixture"]["const"] is False
    assert example["participant"]["independent"] is True
    assert example["participant"]["authored_test_fixture"] is False
    assert example["validation_dimension"] in schema["properties"]["validation_dimension"]["enum"]
    assert example["outcome"]["status"] in schema["properties"]["outcome"]["properties"]["status"]["enum"]
    assert example["evidence_retention"]["class"] in schema["properties"]["evidence_retention"]["properties"]["class"]["enum"]
    assert example["limitations"]

    serialized = json.dumps(example).lower()
    for forbidden_key in ["participant_name", "participant_email", "client_name", "employer_name"]:
        assert forbidden_key not in serialized


def test_portfolio_manifest_links_governance_contracts_without_breaking_manifest_version():
    manifest = _load("manifest.json")

    assert manifest["schema_version"] == "1.2"
    assert manifest["compatibility_source"].endswith("/products/COMPATIBILITY.md")
    assert manifest["compatibility_contract"].endswith("/products/compatibility.json")
    assert manifest["external_validation_source"].endswith("/products/VALIDATION.md")
    assert manifest["external_validation_policy"].endswith("/products/validation-policy.json")
    assert manifest["external_validation_record_schema"].endswith("/products/validation-record.schema.json")
