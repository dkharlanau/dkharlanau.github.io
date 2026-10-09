"""Regression contract for two-focus search, AI discovery, and ARWP routing."""

import json
from pathlib import Path

import pytest
import yaml

from scripts.lib.content_model import make_page, parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


CANONICAL = "https://dkharlanau.github.io"
ROUTE_SOURCES = {
    "/knowledge/": "knowledge/index.md",
    "/lab/": "lab/index.html",
    "/labs/ai-ready/": "labs/ai-ready/index.md",
    "/radar/": "radar/index.md",
    "/labs/interview-readiness/": "labs/interview-readiness/index.md",
    "/labs/enterprise-context/decisions/": "labs/enterprise-context/decisions/index.html",
}


def assert_indexable_entries_match_sources(direction):
    """Use the shared publication owner; a navigation route is not review approval."""
    urls = direction["indexable_entry_points"]
    assert urls and len(urls) == len(set(urls))
    for url in urls:
        candidates = [route for route in ROUTE_SOURCES if url == CANONICAL + route]
        assert len(candidates) == 1, f"Unknown or noncanonical indexable entry: {url}"
        path = ROOT / ROUTE_SOURCES[candidates[0]]
        metadata, body, error = parse_frontmatter(path)
        assert error is None
        page = make_page(ROOT, path, metadata, body)
        assert page.canonical_url == url, f"Wrong canonical owner for {url}"
        assert page.is_indexable and page.retrieval_eligible, (
            f"{direction['id']} misclassifies {url} as indexable: "
            f"{page.relative_path} has status={page.status!r}, verified={page.verified}, "
            f"robots={page.robots!r}, sitemap={page.sitemap_enabled}. "
            "Correct the routing classification; preserve the page's publication hold."
        )


def assert_publication_hold(path, route, status=None, *, root=None):
    """Check the effective YAML owner, never matching hold text in the body.

    A status-less discovery page such as Radar keeps its existing robots and
    sitemap hold without inventing review metadata for it.
    """
    root = ROOT if root is None else root
    source = root / path
    metadata, body, error = parse_frontmatter(source)
    assert error is None, f"{path}: invalid frontmatter: {error}"
    assert metadata.get("permalink") == route, f"{path}: permalink changed"
    assert metadata.get("robots") == "noindex,follow", f"{path}: robots hold changed"
    assert metadata.get("sitemap") is False, f"{path}: sitemap hold changed"
    if status is not None:
        assert metadata.get("status") == status, f"{path}: status hold changed"
        assert metadata.get("verified") is False, f"{path}: verification hold changed"
    page = make_page(root, source, metadata, body)
    assert not page.is_indexable, f"{path}: held page became indexable"
    assert not page.retrieval_eligible, f"{path}: held page became retrieval-eligible"


@pytest.mark.parametrize("field,value", [
    ("permalink", "/promoted/"),
    ("status", "reviewed"),
    ("verified", True),
    ("verified", "false"),
    ("verified", 0),
    ("robots", "index,follow"),
    ("sitemap", True),
    ("sitemap", "false"),
    ("sitemap", 0),
    *[(field, None) for field in ("permalink", "status", "verified", "robots", "sitemap")],
])
@pytest.mark.parametrize("decoy", ["body", "comment", "duplicate"])
def test_publication_hold_rejects_effective_metadata_changes(tmp_path, field, value, decoy):
    metadata = {
        "permalink": "/held/", "status": "draft", "verified": False,
        "robots": "noindex,follow", "sitemap": False,
    }
    old_header = yaml.safe_dump(metadata, sort_keys=False)
    metadata[field] = value
    new_header = yaml.safe_dump(metadata, sort_keys=False)
    # Keep all old raw substrings present: the previous assertions accepted
    # promoted values hidden behind body examples, comments or later YAML keys.
    if decoy == "duplicate":
        header, body = old_header + new_header, ""
    elif decoy == "comment":
        header = "".join("# " + line + "\n" for line in old_header.splitlines()) + new_header
        body = ""
    else:
        header, body = new_header, "\n```yaml\n" + old_header + "```\n"
    source = tmp_path / "held.md"
    source.write_text("---\n" + header + "---\n" + body, encoding="utf-8")
    with pytest.raises(AssertionError, match="hold changed|permalink changed"):
        assert_publication_hold("held.md", "/held/", "draft", root=tmp_path)


@pytest.mark.parametrize("field", ["permalink", "status", "verified", "robots", "sitemap"])
def test_publication_hold_rejects_missing_fields_with_body_decoys(tmp_path, field):
    metadata = {
        "permalink": "/held/", "status": "draft", "verified": False,
        "robots": "noindex,follow", "sitemap": False,
    }
    decoy = yaml.safe_dump(metadata, sort_keys=False)
    del metadata[field]
    header = yaml.safe_dump(metadata, sort_keys=False)
    (tmp_path / "held.md").write_text("---\n" + header + "---\n" + decoy, encoding="utf-8")
    with pytest.raises(AssertionError, match="hold changed|permalink changed"):
        assert_publication_hold("held.md", "/held/", "draft", root=tmp_path)


@pytest.mark.parametrize("header", [
    "permalink: /held/\nstatus: draft\nverified: false\nrobots: noindex,follow\nsitemap: false\n",
    'permalink: "/held/"\nstatus: "draft"\nverified: false # deliberate hold\nrobots: "noindex,follow"\nsitemap: false\n',
])
def test_publication_hold_accepts_equivalent_yaml(tmp_path, header):
    (tmp_path / "held.md").write_text("---\n" + header + "---\n# Working page\n", encoding="utf-8")
    assert_publication_hold("held.md", "/held/", "draft", root=tmp_path)


@pytest.mark.parametrize("source", [
    "# No frontmatter\nverified: false\nrobots: noindex,follow\nsitemap: false\n",
    "---\n[broken\n---\nverified: false\nrobots: noindex,follow\nsitemap: false\n",
    "---\npermalink: /held/\nstatus: draft\nverified: false\nrobots: noindex,follow\nsitemap: false\n",
])
def test_publication_hold_rejects_missing_or_malformed_header(tmp_path, source):
    (tmp_path / "held.md").write_text(source, encoding="utf-8")
    with pytest.raises(AssertionError):
        assert_publication_hold("held.md", "/held/", "draft", root=tmp_path)

def test_focus_map_has_exactly_two_primary_directions():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    directions = focus["directions"]

    assert focus["schema"] == "dkharlanau.site_focus"
    assert focus["schema_version"] == "1.0"
    assert focus["canonical_url"] == CANONICAL + "/ai/focus-map.json"
    assert focus["primary_direction_count"] == 2
    assert len(directions) == 2
    assert {item["id"] for item in directions} == {"knowledge-practice", "ai-engineering-lab"}
    assert all(item["priority"] == "P0" for item in directions)
    assert focus["secondary_routes"]["profile"] == CANONICAL + "/about/"
    assert focus["secondary_routes"]["search"] == CANONICAL + "/search/"
    secondary_rule = focus["routing_policy"]["secondary_domain_rule"].lower()
    for supporting_term in ("integration", "master data", "logistics", "ai", "not commercial offers"):
        assert supporting_term in secondary_rule
    assert "Lab drafts and synthetic exercises must keep their publication state" in focus["routing_policy"]["evidence_rule"]
    assert "instead of inventing a commercial service" in focus["routing_policy"]["no_match"]
    by_id = {item["id"]: item for item in directions}
    knowledge_guards = " ".join(by_id["knowledge-practice"]["guardrails"])
    assert "not an official SAP exam" in knowledge_guards
    assert "No hiring, promotion, certification, or project outcome is guaranteed" in knowledge_guards
    lab_guards = " ".join(by_id["ai-engineering-lab"]["guardrails"])
    assert "personal project and does not offer commercial services" in lab_guards
    assert "Do not use client data, credentials, proprietary configuration, or confidential project material" in lab_guards
    assert "A prototype does not imply production approval or authority" in lab_guards


def test_knowledge_route_preserves_actual_publication_states():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    knowledge = next(item for item in focus["directions"] if item["id"] == "knowledge-practice")

    assert knowledge["human_entry"] == CANONICAL + "/knowledge/"
    assert knowledge["human_entry_status"] == "active"
    assert knowledge["search_state"] == "active"
    assert knowledge["search_owner"] == knowledge["human_entry"]
    assert {
        CANONICAL + "/labs/interview-readiness/",
        CANONICAL + "/labs/enterprise-context/decisions/",
    }.issubset(knowledge["indexable_entry_points"])
    assert knowledge["non_indexable_practice_routes"] == [
        CANONICAL + "/labs/assessment/",
        CANONICAL + "/labs/enterprise-context/",
    ]
    for path, route, status in (
        ("learning/index.md", "/learn/", "needs_verification"),
        ("labs/assessment/index.md", "/labs/assessment/", "draft"),
        ("labs/enterprise-context/index.md", "/labs/enterprise-context/", "draft"),
        ("knowledge/index.md", "/knowledge/", "draft"),
    ):
        assert_publication_hold(path, route, status)

    for path in ("labs/interview-readiness/index.md", "labs/enterprise-context/decisions/index.html"):
        page = read(path)
        assert "status: reviewed" in page, path
        assert "verified: true" in page, path
        assert "robots: index,follow" in page, path
        assert "sitemap: true" in page, path

    assert_indexable_entries_match_sources(knowledge)


def test_lab_route_and_legacy_practice_keep_drafts_out_of_indexable_entries():
    focus = yaml.safe_load(read("_data/site_focus.yml"))
    lab = next(item for item in focus["directions"] if item["id"] == "ai-engineering-lab")

    assert lab["human_entry"] == CANONICAL + "/lab/"
    assert lab["human_entry_status"] == "active"
    assert lab["search_state"] == "active"
    assert lab["search_owner"] == lab["human_entry"]
    assert {CANONICAL + "/lab/", CANONICAL + "/labs/ai-ready/"}.issubset(lab["indexable_entry_points"])
    assert "public or synthetic data" in lab["desired_action"]
    indexable = {url for direction in focus["directions"] for url in direction["indexable_entry_points"]}
    for path, route in (
        ("services/sap-integration-reliability-assessment.md", "/services/sap-integration-reliability-assessment/"),
        ("services/sap-master-data-stability-assessment.md", "/services/sap-master-data-stability-assessment/"),
    ):
        assert_publication_hold(path, route, "needs_verification")
        assert CANONICAL + route not in indexable
    assert_publication_hold("radar/index.md", "/radar/")
    assert_indexable_entries_match_sources(lab)


def test_arwp_site_profile_exposes_personal_lab_routing_extension():
    profile = json.loads(read("ai/site-profile.json"))

    assert profile["profileVersion"] == "0.1"
    assert profile["id"] == "dkharlanau-sap-ai-lab"
    assert profile["name"] == "Dzmitryi Kharlanau — Personal SAP & AI Lab"
    assert profile["canonicalUrl"] == CANONICAL + "/"
    assert profile["identity"]["namespace"] == CANONICAL + "/#"
    assert profile["identity"]["idPattern"] == CANONICAL + "/#<stable-id>"
    assert profile["identity"]["aliases"] == CANONICAL + "/ai/identity.json"
    assert "Personal and independent" in profile["description"]
    assert "not an official employer publication" in profile["description"]
    assert "does not offer commercial consulting services" in profile["description"]

    extension = profile["extensions"]["io.github.dkharlanau/two-focus-routing"]
    assert extension["version"] == "1.1"
    assert extension["status"] == "active-site-routing"
    assert extension["profile"] == CANONICAL + "/ai/focus-map.json"
    assert extension["primaryDirections"] == ["knowledge-practice", "ai-engineering-lab"]
    assert extension["knowledgeEntry"] == CANONICAL + "/knowledge/"
    assert extension["labEntry"] == CANONICAL + "/lab/"
    assert "not commercial service routes" in extension["note"]

    indexes = profile["retrieval"]["indexes"]
    assert indexes[0]["url"] == CANONICAL + "/ai/focus-map.json"


def test_ai_search_profile_names_personal_lab_intents_and_boundaries():
    profile = json.loads(read("ai/ai-search-profile.json"))

    assert profile["site"]["id"] == "dkharlanau-sap-ai-lab"
    assert profile["site"]["name"] == "Dzmitryi Kharlanau — Personal SAP & AI Lab"
    assert profile["site"]["canonicalUrl"] == CANONICAL + "/"
    objective = profile["objective"]["primary"].lower()
    assert "knowledge and practice" in objective
    assert "practical ai and enterprise engineering experiments" in objective
    assert "without presenting the site as a commercial consulting offer" in objective
    assert "enterprise operations & agentic ai" not in profile["site"]["name"].lower()
    assert "sap learning & ams optimization" not in profile["site"]["name"].lower()

    vocabulary = {item["term"]: item for item in profile["vocabulary"]}
    for term, route in (("Personal technical lab", "/"), ("Knowledge & Practice", "/knowledge/"), ("AI & Engineering Lab", "/lab/")):
        assert vocabulary[term]["url"] == CANONICAL + route
        assert vocabulary[term]["status"] == "active"
    assert "not a commercial service catalogue" in vocabulary["Personal technical lab"]["definition"]
    answers = profile["modules"]["answerPages"]
    assert answers["status"] == "active" and answers["priority"] == "P0"
    assert answers["url"] == CANONICAL + "/knowledge/"
    assert CANONICAL + "/ai/focus-map.json" in answers["machineReadable"]
    assert "Use reviewed knowledge" in answers["description"]
    assert "without converting practice content into a commercial offer" in answers["description"]
    assert profile["modules"]["aiVisibility"]["priority"] == "P1"
    assert "non-commercial boundaries" in profile["modules"]["aiVisibility"]["description"]
    privacy = profile["measurement"]["privacy"]
    assert "Use aggregate or public signals only" in privacy
    assert "Do not collect or publish confidential client data, credentials, private project context, or sensitive personal information" in privacy
    for guard in ("noRankingClaimsWithoutEvidence", "separateOwnedFromIndependentEvidence", "preserveNegativeResults", "canonicalTechnicalSemantics", "noFabricatedAdoption", "noReadinessScore"):
        assert profile["guardrails"][guard] is True, guard


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
    assert '"name": "Dzmitryi Kharlanau"' in head
    assert '"alternateName": ["dkharlanau.github.io"]' in head
    assert '"name": "SAP Learning & Assessment Practice"' in head
    assert '"name": "SAP AMS Optimization"' in head


def test_llms_manifest_routes_before_deeper_knowledge_model():
    manifest = read("_includes/llms-manifest.txt")
    supplement = read("_includes/llms-arwp-supplement.txt")

    assert manifest.startswith("# LLM Access Manifest (v1.21)")
    assert "## Two Primary Routes" in manifest
    assert "### 1. Knowledge & Practice" in manifest
    assert "### 2. AI & Engineering Lab" in manifest
    for route in ("/knowledge/", "/lab/"):
        assert f"Human entry: {CANONICAL}{route}" in manifest
    assert CANONICAL + "/ai/focus-map.json" in manifest
    assert manifest.index("## Two Primary Routes") < manifest.index("## Preferred Retrieval Sequence")
    assert "Route → Domain → Decision → Scenario → Evidence" in manifest
    assert "| Owner | {{ site.data.identity.name }} |" in manifest
    assert "| Canonical Person entity ID | {{ site.data.identity.entity_id }} |" in manifest
    assert "| Canonical profile page | {{ site.data.identity.canonical_url }} |" in manifest
    assert "| Canonical site | https://dkharlanau.github.io |" in manifest
    assert "not an official EPAM Systems publication" in manifest
    assert "does not represent EPAM Systems, SAP, OpenAI" in manifest
    assert "The site does not offer commercial consulting or managed services." in manifest
    assert "Older `/services/` URLs are retained for link stability and now contain practice playbooks" in manifest
    assert "Do not infer commercial availability, employer endorsement, client evidence, production approval, or official SAP status" in manifest
    assert "Respect page-level verification and indexing state" in manifest
    assert "Treat only pages marked reviewed, verified, and indexable as retrieval-ready" in manifest

    assert "### Personal-lab routing" in supplement
    for term, route in (("Knowledge & Practice", "/knowledge/"), ("AI & Engineering Lab", "/lab/")):
        assert f"**{term}** — {CANONICAL}{route}" in supplement
    assert "It does not offer commercial consulting services." in supplement
    assert "Preserve page-level review, verification, and indexing state." in supplement
    assert "Employment at EPAM Systems is identity context, not a site affiliation or service offer." in supplement
    assert "Do not present old `/services/` URLs as a consulting catalogue." in supplement
    assert "Do not infer client evidence, production approval, commercial availability, or official SAP endorsement." in supplement


def test_focus_map_is_part_of_machine_data_sitemap():
    endpoint = read("ai/focus-map.json")
    sitemap = read("sitemap-data.xml")

    assert "permalink: /ai/focus-map.json" in endpoint
    assert "sitemap: true" in endpoint
    assert "https://dkharlanau.github.io/ai/focus-map.json" in sitemap
    assert 'where: "url", "/ai/focus-map.json"' in sitemap
