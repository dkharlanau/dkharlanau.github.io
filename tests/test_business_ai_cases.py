import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.check_business_ai_cases import (
    CaseContractError,
    build_report,
    infer_legacy_review_state,
    validate_case,
    validate_transition,
)

CONTRACT = yaml.safe_load(
    (ROOT / "_data" / "labs" / "business_ai" / "contract.yml").read_text(
        encoding="utf-8"
    )
)


def review_ready_case(state="review_ready"):
    return {
        "id": "test-case",
        "title": "Test case",
        "case_kind": "ai_implementation",
        "review_state": state,
        "business_problem": "Reduce manual invoice exception work.",
        "process_id": "source-to-pay",
        "process_stage_ids": ["source-to-pay-invoice"],
        "ai_job": "Extract and compare invoice data.",
        "pattern_ids": ["document-to-workflow"],
        "implementation_maturity": "production",
        "autonomy_level": "L2",
        "systems_of_record": ["ERP"],
        "data_dependencies": ["Supplier invoice", "Purchase order"],
        "integration_boundaries": ["Document intake to ERP validation"],
        "authority_boundary": "AI prepares; ERP validates and posts.",
        "controls": ["Tolerance checks", "Duplicate checks"],
        "human_review": {"kind": "human", "reviewed_by": "Reviewer", "reviewed_at": "2026-08-18"},
        "metrics": [{"name": "touchless rate", "value": "reported"}],
        "measurement_state": "reported_metric",
        "evidence_grade": "B",
        "evidence_claims": [
            {"statement": "A public source reports production use.", "level": "source_fact"},
            {"statement": "The pattern may transfer to similar invoice flows.", "level": "supported_inference"},
        ],
        "source_ids": ["source-1"],
        "source_types": ["customer_first_party"],
        "limitations": ["Public source does not provide a full baseline."],
        "proof_gaps": ["No approved runtime test was performed by this project."],
        "transferability": "medium",
        "consultant_interpretation": "Use only behind ERP controls.",
    }


def test_repository_case_lifecycle_contract_passes_and_reports_migration_gaps():
    report = build_report()
    assert report["contract_version"] == "1.3.0"
    assert report["case_schema_version"] == "2.0"
    assert report["case_count"] > 0
    assert report["agent_maximum_state"] == "review_ready"
    assert report["human_approval_state"] == "approved"
    assert report["migration_gap_count"] > 0


def test_legacy_review_state_is_inferred_conservatively():
    assert infer_legacy_review_state({}) == "candidate"
    assert infer_legacy_review_state({"source_ids": ["s1"]}) == "sourced"
    assert (
        infer_legacy_review_state(
            {"source_ids": ["s1"], "pattern": "p1", "evidence_grade": "B"}
        )
        == "structured"
    )


def test_lifecycle_allows_forward_challenge_and_blocks_invalid_back_jump():
    validate_transition("structured", "challenged", CONTRACT)
    with pytest.raises(CaseContractError, match="Invalid review transition"):
        validate_transition("review_ready", "structured", CONTRACT)


def test_runtime_proof_requires_authorized_and_observed_runtime_activity():
    case = review_ready_case()
    case["evidence_claims"] = [
        {
            "statement": "Runtime behavior was observed.",
            "level": "runtime_proof",
            "runtime_authorized": False,
            "runtime_observed": True,
        }
    ]
    with pytest.raises(CaseContractError, match="runtime_proof requires authorized"):
        validate_case(case, CONTRACT, {"source-1"})


def test_review_ready_blocks_unsupported_claims():
    case = review_ready_case()
    case["evidence_claims"].append(
        {"statement": "This always eliminates invoice errors.", "level": "unsupported_claim"}
    )
    with pytest.raises(CaseContractError, match="blocked evidence levels"):
        validate_case(case, CONTRACT, {"source-1"})


def test_review_ready_cannot_hide_unknown_maturity():
    case = review_ready_case()
    case["implementation_maturity"] = "unknown"
    with pytest.raises(CaseContractError, match="implementation_maturity is still unknown"):
        validate_case(case, CONTRACT, {"source-1"})


def test_approved_requires_identified_human_reviewer():
    case = review_ready_case(state="approved")
    case["human_review"] = {"kind": "agent", "reviewed_by": "curator", "reviewed_at": "2026-08-18"}
    with pytest.raises(CaseContractError, match="without a human review"):
        validate_case(case, CONTRACT, {"source-1"})


def test_valid_approved_case_passes_when_human_review_is_present():
    case = review_ready_case(state="approved")
    validated = validate_case(case, CONTRACT, {"source-1"})
    assert validated["review_state"] == "approved"
