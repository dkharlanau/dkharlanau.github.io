"""Source-level contracts for the two-audience entry points; not browser validation."""
from pathlib import Path
from html import unescape
import json
import re

import yaml

from scripts.lib.content_model import infer_content_model

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def frontmatter(path):
    text = read(path)
    assert text.startswith("---\n"), path
    return yaml.safe_load(text.split("---", 2)[1])


def test_home_routes_to_two_jobs_without_replacing_the_brand():
    home = read("_includes/sections/home-focus.html")
    assert frontmatter("index.md")["sections"] == ["home-focus"]
    cards = re.findall(r'<article class="focus-card(?:\s|")[^>]*>(.*?)</article>', home, re.S)
    assert len(cards) == 2
    for card, route in zip(cards, ("/knowledge/", "/lab/")):
        assert f"'{route}' | relative_url" in card
        assert "portal-primary-link" in card
        assert "/services/" not in card and "'/learn/'" not in card
    assert home.count("<h1 ") == 1
    assert '<h1 id="home-title">Personal SAP &amp; AI lab.' in home
    assert "This website is a personal and independent project." in home
    assert "It is not an official EPAM Systems, SAP, OpenAI, or other company publication." in home
    assert 'role="search"' in home and "'/search/' | relative_url" in home and 'name="q"' in home
    header = read("_includes/header.html")
    assert "/assets/img/logo-d.svg" in header
    assert "page_locale" not in header
    assert "portal_nav." not in header
    assert "'/learn/' | relative_url" in header
    assert "'/knowledge/' | relative_url" in header
    assert 'href="/about/"' in header
    assert "data-site-header" in header and 'aria-controls="site-navigation"' in header


def test_pack_catalogue_matches_implemented_pilot_scope():
    data = yaml.safe_load(read("_data/learning_packs.yml"))
    assert data["schema_version"] == "1.0"
    packs = data["packs"]
    assert len(packs) == 1, "Do not advertise unimplemented inventory."
    pack = packs[0]
    page = frontmatter("learning/packs/bp-mdg-replication.md")
    assert pack["id"] == page["pack_id"]
    assert pack["href"] == page["permalink"]
    assert pack["case_count"] == 5
    assert pack["status"] == "draft"
    assert pack["access"] == "free_pilot"
    assert pack["version"] == "0.2.0"
    assert pack["duration_minutes"] > 0
    assert len(pack["learning_outcomes"]) >= 5
    assert len(pack["curriculum"]) == pack["case_count"]
    assert len({item["id"] for item in pack["curriculum"]}) == pack["case_count"]
    for path in ("learning/index.md", "learning/packs/bp-mdg-replication.md"):
        metadata = frontmatter(path)
        assert metadata["verified"] is False
        assert metadata["sitemap"] is False
        assert metadata["robots"] == "noindex,follow"
        assert metadata["status"] == "needs_verification"


def test_learning_is_integrated_with_the_content_quality_model():
    config = yaml.safe_load(read("config/content-quality.yml"))
    assert "learning" in config["public_roots"]
    assert "learning_pack" in config["content_models"]
    assert "learning/packs/" in config["content_models"]["learning_pack"]["paths"]
    assert infer_content_model("learning/index.md", {})[0] == "landing_page"
    assert infer_content_model("learning/packs/example.md", {})[0] == "learning_pack"
    assert frontmatter("learning/index.md")["content_model"] == "landing_page"
    assert frontmatter("learning/packs/bp-mdg-replication.md")["content_model"] == "learning_pack"


def test_pilot_has_five_attempt_review_cycles_and_no_new_data_collection():
    page = read("learning/packs/bp-mdg-replication.md")
    assert page.count('<details class="focus-answer">') == 5
    for number in range(1, 6):
        assert f'id="case-{number}"' in page
    assert "synthetic cases" in page
    assert "not an employment or certification score" in page
    assert "source checks do not constitute human approval" in page
    assert "There is no validated pass threshold" in page
    assert "customer case" in page.lower()
    assert "Blank, omitted and clear" in page
    assert "One exception list is not one recovery action" in page
    for prohibited in ("<form", "<input", "localStorage", "fetch(", "<script"):
        assert prohibited not in page
    css = read("assets/site-focus.css")
    assert "@media print" in css and ".focus-answer" in css
    assert "@media (max-width: 720px)" in css
    assert ":focus-visible" in css
    assert ".focus-diagnostic-sheet" in css


def test_legacy_practice_keeps_noncommercial_schema_and_bounded_example():
    path = "services/sap-ams-consulting.md"
    text = read(path)
    metadata = frontmatter(path)
    assert metadata["permalink"] == "/services/sap-ams-consulting/"
    assert metadata.get("content_model") != "service"
    assert metadata["hide_global_cta"] is True
    assert "public practice playbook from my independent technical lab" in text
    assert "It is not a commercial service, proposal, or client engagement offer." in text
    assert "Use public or synthetic data only." in text
    documents = [json.loads(block) for block in re.findall(
        r"""<script\b[^>]*\btype\s*=\s*["']application/ld\+json["'][^>]*>\s*(.*?)\s*</script\s*>""", text, re.S | re.I
    )]
    assert documents, "Keep canonical breadcrumb ownership on the stable practice URL."

    def inspect_schema(value):
        if isinstance(value, dict):
            types = value.get("@type", [])
            types = [types] if isinstance(types, str) else types
            types = {value.rsplit("/", 1)[-1].rsplit("#", 1)[-1].rsplit(":", 1)[-1].lower() for value in types}
            assert not types & {"service", "offer", "aggregateoffer", "aggregaterating", "professionalservice", "localbusiness"}
            assert not {"offers", "aggregateRating", "price", "priceCurrency"} & value.keys()
            for child in value.values():
                inspect_schema(child)
        elif isinstance(value, list):
            for child in value:
                inspect_schema(child)

    for document in documents:
        inspect_schema(document)
    breadcrumb = next(item for item in documents if item["@type"] == "BreadcrumbList")
    assert breadcrumb["@context"] == "https://schema.org"
    assert breadcrumb["itemListElement"] == [
        {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://dkharlanau.github.io/"},
        {"@type": "ListItem", "position": 2, "name": "Practice playbooks", "item": "https://dkharlanau.github.io/services/"},
        {"@type": "ListItem", "position": 3, "name": "SAP AMS optimization", "item": "https://dkharlanau.github.io/services/sap-ams-consulting/"},
    ]
    # Inspect actionable copy, allowing factual or negative mentions in the prose.
    for _, label in re.findall(r'<(a|button)\b[^>]*>(.*?)</\1>', text, re.S | re.I):
        label = unescape(re.sub(r"<[^>]+>", " ", label))
        assert not re.search(r"\b(?:hire me|(?:book|schedule)\s+(?:(?:a|an|free|discovery|introductory|consulting|paid)\s+)*(?:call|consultation)|request (?:a )?proposal|get (?:a )?quote|pricing)\b", label, re.I)
    assert not re.search(r'<(?:form|input)\b', text, re.I)
    assert 'href="/atlas/diagnostics/"' in text
    assert 'href="/lab/"' in text
    assert "not a replacement" in text
    assert "Released team capacity and cash savings are different outcomes" in text
    assert 'id="diagnostic-example"' in text
    assert "Illustrative diagnostic output" in text
    assert "synthetic example" in text
    assert "not customer evidence" in text
    assert "Do not make mass replay the default action" in text


def test_strategy_retains_source_product_and_production_boundaries():
    strategy = read("docs/two-focus-product-strategy.md")
    assert "English entry points only" in strategy
    assert "not a seventh independent knowledge base" in strategy
    assert "five synthetic cases" in strategy
    assert "No checkout" in strategy
    assert "Do not dispatch Repository State Sync" in strategy
    assert "#329" in strategy and "#331" in strategy and "#380" in strategy
    assert "never manufacture review status" in strategy
    assert "training case is never customer evidence" in strategy
