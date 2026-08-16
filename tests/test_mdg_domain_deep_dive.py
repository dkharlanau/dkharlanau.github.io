import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "_data" / "labs" / "enterprise_context" / "topics"
SOURCES = ROOT / "_data" / "labs" / "enterprise_context" / "sources" / "mdg_domain_deep_dive_registry.yml"
ASSESSMENT_DATA = ROOT / "labs" / "assessment" / "data"

TOPIC_FILES = [
    "mdg_material_domain.yml",
    "mdg_business_partner_domain.yml",
    "mdg_governance_process_engine.yml",
    "mdg_replication_distribution.yml",
    "mdg_consolidation_golden_record.yml",
    "mdg_migration_load_strategy.yml",
    "mdg_logistics_end_to_end_cases.yml",
    "mdg_material_entity_reference.yml",
    "mdg_bp_entity_reference.yml",
    "mdg_change_request_design_matrix.yml",
    "mdg_brfplus_rule_catalog.yml",
    "mdg_drf_operations_control.yml",
    "mdg_survivorship_matching_policy.yml",
]

ALLOWED_RELATION_PREDICATES = {"requires", "provides_context_to"}


def load(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_mdg_domain_topics_have_agent_contract():
    for filename in TOPIC_FILES:
        data = load(TOPICS / filename)
        assert data["id"].startswith("TOPIC-MDG-")
        assert data["status"] == "researching"
        assert data["verified_at"] is None
        assert data["human_view"].startswith("/labs/enterprise-context/mdg/")
        assert data["source_refs"]


def test_mdg_domain_sources_are_official_sap_help():
    data = load(SOURCES)
    sources = {item["id"]: item for item in data["sources"]}
    required = set()
    for filename in TOPIC_FILES:
        required.update(load(TOPICS / filename)["source_refs"])
    assert required <= set(sources)
    for source_id in required:
        source = sources[source_id]
        assert source["publisher"] == "SAP"
        assert source["source_type"] == "official_help"
        assert source["status"] == "source_verified"
        assert source["accessed_at"] == "2026-08-16"
        assert source["url"].startswith("https://help.sap.com/")


def test_mdg_domain_relations_use_enterprise_graph_contract():
    for filename in TOPIC_FILES:
        data = load(TOPICS / filename)
        for relation in data.get("relations", []):
            assert relation["predicate"] in ALLOWED_RELATION_PREDICATES
            assert relation["subject"].startswith("TOPIC-MDG-")
            assert relation["object"].startswith("TOPIC-MDG-")


def test_domain_pages_exist_and_are_noindex_drafts():
    pages = [
        "labs/enterprise-context/mdg/domains/index.md",
        "labs/enterprise-context/mdg/domains/material/index.md",
        "labs/enterprise-context/mdg/domains/material/entity-map/index.md",
        "labs/enterprise-context/mdg/domains/business-partner/index.md",
        "labs/enterprise-context/mdg/domains/business-partner/entity-map/index.md",
        "labs/enterprise-context/mdg/governance-engine/index.md",
        "labs/enterprise-context/mdg/governance-engine/change-request-matrix/index.md",
        "labs/enterprise-context/mdg/governance-engine/brfplus-rules/index.md",
        "labs/enterprise-context/mdg/replication/index.md",
        "labs/enterprise-context/mdg/replication/operations/index.md",
        "labs/enterprise-context/mdg/consolidation/index.md",
        "labs/enterprise-context/mdg/consolidation/survivorship/index.md",
        "labs/enterprise-context/mdg/migration/index.md",
        "labs/enterprise-context/mdg/logistics/cases/index.md",
        "labs/enterprise-context/mdg/assessment/index.md",
    ]
    for rel in pages:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "verified: false" in text
        assert "robots: noindex,follow" in text
        assert "sitemap: false" in text


def test_technical_entity_maps_keep_key_delivered_entities_visible():
    material = load(TOPICS / "mdg_material_entity_reference.yml")
    material_text = json.dumps(material)
    for entity in ("MATERIAL", "MARCBASIC", "MARCATP", "MARCPURCH", "MVKESALES", "MARDSTOR", "MBEWVALUA", "MLGNSTOR"):
        assert entity in material_text

    bp = load(TOPICS / "mdg_bp_entity_reference.yml")
    bp_text = json.dumps(bp)
    for entity in ("BP_HEADER", "BP_CENTRL", "BP_ADDR", "BP_ROLE", "BP_CMPNY", "BP_PORG", "BP_SALES"):
        assert entity in bp_text


def test_governance_and_operations_models_preserve_separation_of_concerns():
    cr = load(TOPICS / "mdg_change_request_design_matrix.yml")
    assert {item["pattern"] for item in cr["pattern_matrix"]} >= {
        "Create new identity",
        "Organizational extension",
        "Sensitive attribute change",
        "Mass change",
    }

    rules = load(TOPICS / "mdg_brfplus_rule_catalog.yml")
    assert set(rules["rule_classes"]) == {
        "workflow_routing",
        "validation",
        "derivation",
        "authorization_or_scope",
        "duplicate_or_identity",
    }

    drf = load(TOPICS / "mdg_drf_operations_control.yml")
    assert set(drf["replay_decision"]["outcomes"]) == {
        "safe_replay",
        "rebuild_from_current_truth",
        "manual_resolution",
        "stop_and_reconcile",
    }

    survivorship = load(TOPICS / "mdg_survivorship_matching_policy.yml")
    assert set(survivorship["matching_policy"]["thresholds"]) == {
        "automatic_match",
        "review_band",
        "non_match",
    }


def test_mdg_assessment_case_set_is_registered_and_valid():
    manifest = json.loads((ASSESSMENT_DATA / "case-sets.json").read_text(encoding="utf-8"))
    mdg_set = next(item for item in manifest["sets"] if item["id"] == "mdg-lead")
    assert mdg_set["count"] == 4
    assert manifest["total_cases"] == 63

    candidates = json.loads((ASSESSMENT_DATA / "question-candidates.json").read_text(encoding="utf-8"))
    assert candidates["published_case_count"] == manifest["total_cases"]

    rows = [
        json.loads(line)
        for line in (ASSESSMENT_DATA / "mdg-cases.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    assert len(rows) == 4
    assert {row["id"] for row in rows} == {
        "ASSESS-MDG-001",
        "ASSESS-MDG-002",
        "ASSESS-MDG-003",
        "ASSESS-MDG-004",
    }
    for row in rows:
        assert row["expected_points"]
        assert row["follow_up_questions"]
        assert row["red_flags"]
        assert row["graph_refs"]
        assert row["human_refs"]


def test_sap_mdg_profile_includes_domain_design_skill():
    profile = load(ROOT / "agent-skills" / "profiles" / "sap-mdg.yml")
    assert "sap-mdg-domain-solution-design" in profile["skills"]
    assert "sap-mdg-lineage-analysis" in profile["skills"]
