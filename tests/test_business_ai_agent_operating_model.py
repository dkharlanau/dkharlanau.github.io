from pathlib import Path
import subprocess
import sys

import yaml

ROOT = Path(__file__).resolve().parents[1]
EXPORTERS = ROOT / "agent-skills" / "exporters"
sys.path.insert(0, str(EXPORTERS))

from index_loader import load_skill_index

MODEL_PATH = ROOT / "_data" / "labs" / "business_ai" / "agent_operating_model.yml"
CONTEXT_PATH = ROOT / "ai" / "business-ai-agent-context.json"

EXPECTED_ROLES = {
    "research_scout",
    "case_curator",
    "evidence_challenger",
    "graph_steward",
    "lead_decision_analyst",
    "assessment_builder",
}
NEW_SKILLS = {
    "business-ai-case-curator",
    "business-ai-lead-decision-analyst",
    "business-ai-graph-steward",
    "business-ai-assessment-builder",
}


def load_model():
    return yaml.safe_load(MODEL_PATH.read_text(encoding="utf-8"))


def test_operating_model_has_six_specialised_roles():
    model = load_model()
    assert set(model["roles"]) == EXPECTED_ROLES
    assert model["orchestration"]["default_flow"] == [
        "research_scout",
        "case_curator",
        "evidence_challenger",
        "graph_steward",
        "lead_decision_analyst",
        "assessment_builder",
    ]


def test_roles_have_review_and_stop_boundaries():
    model = load_model()
    for role_id, role in model["roles"].items():
        assert role["mission"], role_id
        assert role["source_refs"], role_id
        assert role["skills"], role_id
        assert role["allowed_outputs"], role_id
        assert role["review_boundary"], role_id
        assert role["stop_conditions"], role_id
        assert "approved" not in role["allowed_outputs"], role_id


def test_handoffs_reference_known_roles():
    model = load_model()
    for role_id, role in model["roles"].items():
        unknown = set(role.get("handoff_to", [])) - EXPECTED_ROLES
        assert unknown == set(), f"{role_id} has unknown handoff roles: {unknown}"


def test_all_role_skills_are_indexed_and_new_skills_exist():
    model = load_model()
    index = load_skill_index(ROOT / "agent-skills")
    indexed = {entry["name"] for entry in index["skills"]}
    referenced = {skill for role in model["roles"].values() for skill in role["skills"]}
    assert referenced <= indexed
    assert NEW_SKILLS <= indexed
    for skill in NEW_SKILLS:
        assert (ROOT / "agent-skills" / "skills" / skill / "SKILL.md").exists()


def test_portable_skill_validator_accepts_new_skill_set():
    completed = subprocess.run(
        [sys.executable, str(EXPORTERS / "validate_agent_skills.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert completed.returncode == 0, completed.stdout + completed.stderr


def test_approval_is_human_only():
    model = load_model()
    boundary = model["publication_boundary"]
    assert boundary["agent_maximum_review_state"] == "review_ready"
    assert boundary["human_approval_state"] == "approved"
    assert boundary["runtime_rule"].startswith("Runtime proof is valid only")


def test_context_endpoint_is_generated_from_canonical_model():
    source = CONTEXT_PATH.read_text(encoding="utf-8")
    assert "site.data.labs.business_ai.agent_operating_model" in source
    assert "site.data.labs.business_ai.contract" in source
    assert "role_pair in model.roles" in source
    assert 'permalink: /ai/business-ai-agent-context.json' in source
    assert '"contract_version"' in source
    assert '"freshness"' in source


def test_context_schema_requires_review_boundary_and_stop_conditions():
    required = set(load_model()["context_schema"]["required_fields"])
    assert {"review_boundary", "stop_conditions", "source_refs", "skills"} <= required
