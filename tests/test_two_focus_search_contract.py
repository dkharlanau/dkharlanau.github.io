"""Regression contract for personal-lab search, AI discovery, and ARWP routing."""

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://dkharlanau.github.io"


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def frontmatter(path: str) -> dict:
    content = read(path)
    assert content.startswith("---\n"), path
    return yaml.safe_load(content.split("---", 2)[1])


def focus_directions() -> dict:
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    assert focus["primary_direction_count"] == 2
    assert len(focus["directions"]) == 2
    return {item["id"]: item for item in focus["directions"]}


def test_focus_map_has_exactly_two_personal_lab_routes():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    directions = focus_directions()

    assert set(directions) == {"knowledge-practice", "ai-engineering-lab"}
    assert all(item["priority"] == "P0" for item in directions.values())
    assert "personal" in focus["site_promise"].lower()
    assert "not commercial offers" in focus["routing_policy"]["secondary_domain_rule"].lower()
    assert "instead of inventing a commercial service" in focus["routing_policy"]["no_match"].lower()
    for supporting_term in ("logistics", "integration", "master data", "ai"):
        assert supporting_term in focus["routing_policy"]["secondary_domain_rule"].lower()


def test_knowledge_route_preserves_review_and_indexing_gates():
    knowledge = focus_directions()["knowledge-practice"]
    assert knowledge["human_entry"] == ORIGIN + "/knowledge/"
    assert knowledge["search_state"] == "active"
    assert knowledge["search_owner"] == knowledge["human_entry"]
    assert knowledge["indexable_entry_points"] == [
        ORIGIN + "/knowledge/",
        ORIGIN + "/labs/interview-readiness/",
        ORIGIN + "/labs/enterprise-context/decisions/",
    ]
    assert any(url.endswith("/labs/assessment/") for url in knowledge["non_indexable_practice_routes"])
    assert any(url.endswith("/labs/enterprise-context/") for url in knowledge["non_indexable_practice_routes"])

    for path in ("learning/index.md", "labs/assessment/index.md", "labs/enterprise-context/index.md"):
        metadata = frontmatter(path)
        assert metadata["verified"] is False
        assert "noindex" in metadata["robots"]
        assert metadata["sitemap"] is False

    for path in ("labs/interview-readiness/index.md", "labs/enterprise-context/decisions/index.html"):
        metadata = frontmatter(path)
        assert metadata["status"] == "reviewed"
        assert metadata["verified"] is True
        assert "noindex" not in metadata["robots"]
        assert metadata["sitemap"] is True


def test_engineering_route_points_to_reviewed_toolkit_not_services():
    lab = focus_directions()["ai-engineering-lab"]
    assert lab["human_entry"] == ORIGIN + "/lab/"
    assert lab["search_owner"] == lab["human_entry"]
    assert lab["search_state"] == "active"
    assert ORIGIN + "/lab/" in lab["indexable_entry_points"]
    assert all("/services/" not in url for url in lab["indexable_entry_points"])
    assert any("does not offer commercial services" in guardrail for guardrail in lab["guardrails"])
    assert any("client data" in guardrail.lower() for guardrail in lab["guardrails"])

    metadata = frontmatter("lab/index.html")
    assert metadata["status"] == "reviewed"
    assert metadata["verified"] is True
    assert metadata["sitemap"] is True
    assert "noindex" not in metadata["robots"]
    assert "not commercial services" in read("lab/index.html")


def test_arwp_profile_exposes_canonical_personal_lab_routes():
    profile = json.loads(read("ai/site-profile.json"))
    assert profile["profileVersion"] == "0.1"
    assert profile["name"] == "Dzmitryi Kharlanau — Personal SAP & AI Lab"
    assert "does not offer commercial consulting services" in profile["description"]
    extension = profile["extensions"]["io.github.dkharlanau/two-focus-routing"]
    assert extension["status"] == "active-site-routing"
    assert extension["profile"] == ORIGIN + "/ai/focus-map.json"
    assert extension["primaryDirections"] == ["knowledge-practice", "ai-engineering-lab"]
    assert extension["knowledgeEntry"] == ORIGIN + "/knowledge/"
    assert extension["labEntry"] == ORIGIN + "/lab/"
    assert "not commercial service routes" in extension["note"]
    assert profile["retrieval"]["indexes"][0]["url"] == ORIGIN + "/ai/focus-map.json"


def test_ai_search_profile_describes_knowledge_and_experiments():
    profile = json.loads(read("ai/ai-search-profile.json"))
    assert profile["site"]["name"] == "Dzmitryi Kharlanau — Personal SAP & AI Lab"
    objective = profile["objective"]["primary"].lower()
    assert "knowledge and practice" in objective
    assert "engineering experiments" in objective
    assert "without presenting the site as a commercial consulting offer" in objective

    vocabulary = {item["term"]: item for item in profile["vocabulary"]}
    assert vocabulary["Knowledge & Practice"]["url"] == ORIGIN + "/knowledge/"
    assert vocabulary["AI & Engineering Lab"]["url"] == ORIGIN + "/lab/"
    assert profile["modules"]["answerPages"]["priority"] == "P0"
    assert profile["modules"]["aiVisibility"]["priority"] == "P1"
    assert "reviewed knowledge" in profile["modules"]["answerPages"]["description"].lower()
    assert "commercial offer" in profile["modules"]["answerPages"]["description"].lower()


def test_html_head_advertises_profile_and_real_site_routes():
    head = read("_includes/head.html")
    for path in ("/ai/site-profile.json", "/ai/focus-map.json", "/ai/ai-search-profile.json"):
        assert 'href="{{ \'' + path + '\' | absolute_url }}"' in head
    assert 'title="Agent-Ready Web Profile"' in head
    assert 'title="Two-Focus Routing Map"' in head
    assert '"name": "Dzmitryi Kharlanau"' in head
    assert '"alternateName": ["dkharlanau.github.io"]' in head
    assert '"name": "Knowledge & Practice"' in head
    assert '"name": "AI & Engineering Lab"' in head
    assert ORIGIN + "/knowledge/" in head
    assert ORIGIN + "/lab/" in head
    assert ORIGIN + "/services/sap-ams-consulting/" not in head


def test_llms_manifest_routes_to_knowledge_and_lab_before_machine_endpoints():
    manifest = read("_includes/llms-manifest.txt")
    supplement = read("_includes/llms-arwp-supplement.txt")
    assert manifest.startswith("# LLM Access Manifest (v1.21)")
    assert "## Two Primary Routes" in manifest
    assert "### 1. Knowledge & Practice" in manifest
    assert "### 2. AI & Engineering Lab" in manifest
    assert ORIGIN + "/ai/focus-map.json" in manifest
    assert manifest.index("## Two Primary Routes") < manifest.index("## Machine Endpoints")
    assert "Route → Domain → Decision → Scenario → Evidence" in manifest
    assert "does not offer commercial consulting" in manifest
    assert "personal and independent technical project" in supplement
    assert "Do not present old " in supplement
    assert "Preserve page-level review, verification, and indexing state" in supplement


def test_focus_map_is_part_of_machine_data_sitemap():
    endpoint = read("ai/focus-map.json")
    sitemap = read("sitemap-data.xml")
    assert "permalink: /ai/focus-map.json" in endpoint
    assert "sitemap: true" in endpoint
    assert ORIGIN + "/ai/focus-map.json" in sitemap
    assert 'where: "url", "/ai/focus-map.json"' in sitemap
