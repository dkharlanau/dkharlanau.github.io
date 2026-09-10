"""Regression contract for two-focus search, AI discovery, and ARWP routing."""

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_focus_map_has_exactly_two_primary_directions():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    directions = focus["directions"]

    assert focus["primary_direction_count"] == 2
    assert len(directions) == 2
    assert {item["id"] for item in directions} == {
        "sap-learning-practice",
        "sap-ams-optimization",
    }
    assert all(item["priority"] == "P0" for item in directions)

    secondary_rule = focus["routing_policy"]["secondary_domain_rule"].lower()
    for supporting_term in ("integration", "mdg", "logistics", "practical ai"):
        assert supporting_term in secondary_rule


def test_learning_search_route_preserves_human_review_gate():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    learning = next(item for item in focus["directions"] if item["id"] == "sap-learning-practice")

    assert learning["human_entry"].endswith("/learn/")
    assert learning["human_entry_status"] == "review-gated"
    assert learning["search_state"] == "staged"
    assert learning["indexable_entry_points"]
    assert all("/learn/" not in url for url in learning["indexable_entry_points"])
    assert any(url.endswith("/labs/interview-readiness/") for url in learning["indexable_entry_points"])
    assert any(url.endswith("/labs/assessment/") for url in learning["indexable_entry_points"])

    learning_page = read("learning/index.md")
    assert "verified: false" in learning_page
    assert "robots: noindex,follow" in learning_page
    assert "sitemap: false" in learning_page


def test_ams_route_is_the_single_commercial_pillar():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    ams = next(item for item in focus["directions"] if item["id"] == "sap-ams-optimization")

    assert ams["human_entry"].endswith("/services/sap-ams-consulting/")
    assert ams["human_entry_status"] == "active"
    assert ams["search_state"] == "active"
    assert "SAP AMS optimization" in ams["target_queries"]
    assert any("integration-reliability-assessment" in url for url in ams["indexable_entry_points"])
    assert any("master-data-stability-assessment" in url for url in ams["indexable_entry_points"])


def test_arwp_site_profile_exposes_two_focus_extension():
    profile = json.loads(read("ai/site-profile.json"))

    assert profile["profileVersion"] == "0.1"
    assert profile["name"] == "Dzmitryi Kharlanau — SAP Learning & AMS Optimization"
    assert "two primary routes" in profile["description"].lower()

    extension = profile["extensions"]["io.github.dkharlanau/two-focus-routing"]
    assert extension["status"] == "active-site-routing"
    assert extension["profile"] == "https://dkharlanau.github.io/ai/focus-map.json"
    assert extension["primaryDirections"] == [
        "sap-learning-practice",
        "sap-ams-optimization",
    ]

    indexes = profile["retrieval"]["indexes"]
    assert indexes[0]["url"] == "https://dkharlanau.github.io/ai/focus-map.json"


def test_ai_search_profile_names_both_intents_without_old_site_identity():
    profile = json.loads(read("ai/ai-search-profile.json"))

    assert profile["site"]["name"] == "Dzmitryi Kharlanau — SAP Learning & AMS Optimization"
    objective = profile["objective"]["primary"].lower()
    assert "sap learning" in objective
    assert "sap ams optimization" in objective
    assert "enterprise operations & agentic ai" not in profile["site"]["name"].lower()

    vocabulary = {item["term"]: item for item in profile["vocabulary"]}
    assert vocabulary["Two-focus routing"]["url"] == "https://dkharlanau.github.io/ai/focus-map.json"
    assert profile["modules"]["aiVisibility"]["priority"] == "P0"


def test_html_head_advertises_arwp_and_focus_map():
    head = read("_includes/head.html")

    for path in (
        "/ai/site-profile.json",
        "/ai/focus-map.json",
        "/ai/ai-search-profile.json",
    ):
        assert f"href=\"{{{{ '{path}' | absolute_url }}}}\"" in head

    assert 'title="Agent-Ready Web Profile"' in head
    assert 'title="Two-Focus Routing Map"' in head
    assert '"name": "SAP Learning & AMS Optimization — Dzmitryi Kharlanau"' in head
    assert '"name": "SAP Learning & Assessment Practice"' in head
    assert '"name": "SAP AMS Optimization"' in head


def test_llms_manifest_routes_before_deeper_knowledge_model():
    manifest = read("_includes/llms-manifest.txt")
    supplement = read("_includes/llms-arwp-supplement.txt")

    assert manifest.startswith("# LLM Access Manifest (v1.20)")
    assert "## Two Primary Routes" in manifest
    assert "SAP Learning & Assessment Practice" in manifest
    assert "SAP AMS Optimization" in manifest
    assert "https://dkharlanau.github.io/ai/focus-map.json" in manifest
    assert manifest.index("## Two Primary Routes") < manifest.index("## Canonical Knowledge Model")
    assert "Learn or Improve AMS → Domain → Decision → Scenario → Evidence" in manifest

    assert "Read this first: two primary routes" in supplement
    assert "The `/learn/` hub and current BP/MDG pilot pack remain review-gated and `noindex`." in supplement


def test_focus_map_is_part_of_machine_data_sitemap():
    endpoint = read("ai/focus-map.json")
    sitemap = read("sitemap-data.xml")

    assert "permalink: /ai/focus-map.json" in endpoint
    assert "sitemap: true" in endpoint
    assert "https://dkharlanau.github.io/ai/focus-map.json" in sitemap
    assert 'where: "url", "/ai/focus-map.json"' in sitemap
