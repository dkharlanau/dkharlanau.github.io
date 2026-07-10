import json
from pathlib import Path

import pytest


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "ai" / "signal-to-atlas.schema.json"
DOC_PATH = REPO_ROOT / "docs" / "atlas" / "SIGNAL_TO_ATLAS_SCHEMA.md"
WORKFLOW_PATH = REPO_ROOT / "docs" / "atlas" / "SIGNAL_DRIVEN_ATLAS_UPDATES.md"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def conditional_for_decision(schema, decision):
    for branch in schema["allOf"]:
        target = (
            branch.get("if", {})
            .get("properties", {})
            .get("decision", {})
            .get("properties", {})
            .get("target_decision", {})
        )
        if target.get("const") == decision:
            return branch
        if decision in target.get("enum", []):
            return branch
    raise AssertionError(f"Missing conditional branch for {decision}")


def test_schema_file_is_valid_json_and_named():
    schema = load_schema()
    assert schema["$id"] == "https://dkharlanau.github.io/ai/signal-to-atlas.schema.json"
    assert schema["properties"]["schema"]["const"] == "dkharlanau.signal_to_atlas"
    assert schema["properties"]["schema_version"]["const"] == "1.0"


def test_schema_defines_required_states():
    schema = load_schema()
    states = schema["properties"]["state"]["enum"]
    assert states == [
        "RAW_SIGNAL",
        "ENRICHED_SIGNAL",
        "MATCHED_TO_ATLAS",
        "UPDATE_PROPOSED",
        "REVIEW_READY",
        "APPROVED",
        "REJECTED",
        "NEEDS_RESEARCH",
    ]


def test_schema_defines_target_decisions():
    schema = load_schema()
    decisions = schema["properties"]["decision"]["properties"]["target_decision"]["enum"]
    assert decisions == [
        "update_existing_page",
        "create_new_page_candidate",
        "reject",
        "needs_research",
    ]


def test_page_update_requires_existing_target_and_source_body_evidence():
    schema = load_schema()
    branch = conditional_for_decision(schema, "update_existing_page")["then"]
    assert branch["required"] == ["atlas_candidates", "proposed_update"]
    assert branch["properties"]["atlas_candidates"]["minItems"] == 1
    evidence = branch["properties"]["evidence"]["properties"]
    assert evidence["source_body_opened"]["const"] is True
    assert evidence["concrete_facts"]["minItems"] == 2


def test_new_page_candidate_requires_distinct_new_page_block():
    schema = load_schema()
    branch = conditional_for_decision(schema, "create_new_page_candidate")["then"]
    assert branch["required"] == [
        "atlas_candidates",
        "proposed_new_page",
        "proposed_update",
    ]
    proposed_new_page = schema["properties"]["proposed_new_page"]
    assert "why_existing_pages_are_insufficient" in proposed_new_page["required"]
    assert proposed_new_page["properties"]["noindex_until_reviewed"]["const"] is True


def test_reject_and_needs_research_require_reason():
    schema = load_schema()
    branch = conditional_for_decision(schema, "reject")["then"]
    assert branch["properties"]["decision"]["required"] == ["rejection_reason"]


def test_core_blocks_require_source_and_classification_fields():
    schema = load_schema()
    assert schema["properties"]["signal"]["required"] == [
        "title",
        "source_name",
        "source_url",
        "source_date",
        "date_checked",
        "source_type",
    ]
    assert schema["properties"]["classification"]["required"] == [
        "sap_domain",
        "business_process",
        "technology_area",
        "operational_implication",
        "tags",
    ]


@pytest.mark.skipif(
    not DOC_PATH.exists() or not WORKFLOW_PATH.exists(),
    reason="Local-only internal docs",
)
def test_docs_reference_schema_states_and_validation():
    doc = DOC_PATH.read_text(encoding="utf-8")
    workflow = WORKFLOW_PATH.read_text(encoding="utf-8")
    for token in [
        "ai/signal-to-atlas.schema.json",
        "RAW_SIGNAL",
        "ENRICHED_SIGNAL",
        "MATCHED_TO_ATLAS",
        "UPDATE_PROPOSED",
        "REVIEW_READY",
        "APPROVED",
        "REJECTED",
        "NEEDS_RESEARCH",
        "update_existing_page",
        "create_new_page_candidate",
        "Title-Only Prevention",
    ]:
        assert token in doc
    assert "ai/signal-to-atlas.schema.json" in workflow
