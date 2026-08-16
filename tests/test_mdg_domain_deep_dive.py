from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TOPICS = ROOT / "_data" / "labs" / "enterprise_context" / "topics"
SOURCES = ROOT / "_data" / "labs" / "enterprise_context" / "sources" / "mdg_domain_deep_dive_registry.yml"

TOPIC_FILES = [
    "mdg_material_domain.yml",
    "mdg_business_partner_domain.yml",
    "mdg_governance_process_engine.yml",
    "mdg_replication_distribution.yml",
    "mdg_consolidation_golden_record.yml",
    "mdg_migration_load_strategy.yml",
    "mdg_logistics_end_to_end_cases.yml",
]


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
        assert sources[source_id]["publisher"] == "SAP"
        assert sources[source_id]["url"].startswith("https://help.sap.com/")


def test_domain_pages_exist_and_are_noindex_drafts():
    pages = [
        "labs/enterprise-context/mdg/domains/index.md",
        "labs/enterprise-context/mdg/domains/material/index.md",
        "labs/enterprise-context/mdg/domains/business-partner/index.md",
        "labs/enterprise-context/mdg/governance-engine/index.md",
        "labs/enterprise-context/mdg/replication/index.md",
        "labs/enterprise-context/mdg/consolidation/index.md",
        "labs/enterprise-context/mdg/migration/index.md",
        "labs/enterprise-context/mdg/logistics/cases/index.md",
    ]
    for rel in pages:
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "verified: false" in text
        assert "robots: noindex,follow" in text
        assert "sitemap: false" in text


def test_sap_mdg_profile_includes_domain_design_skill():
    profile = load(ROOT / "agent-skills" / "profiles" / "sap-mdg.yml")
    assert "sap-mdg-domain-solution-design" in profile["skills"]
    assert "sap-mdg-lineage-analysis" in profile["skills"]
