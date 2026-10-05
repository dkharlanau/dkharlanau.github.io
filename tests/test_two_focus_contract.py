"""Source-level contracts for the two-audience entry points; not browser validation."""
from pathlib import Path
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


def test_home_routes_to_four_public_jobs_with_private_boundary():
    home = read("_includes/sections/home-focus.html")
    assert frontmatter("index.md")["sections"] == ["home-focus"]
    assert len(re.findall(r'class="focus-card(?:\s|\")', home)) == 4
    assert "'/legal/professional-disclosure/' | relative_url" in home
    assert "'/knowledge/' | relative_url" in home
    assert "'/lab/' | relative_url" in home
    assert "'/research/' | relative_url" in home
    assert "EPAM Systems" in home
    assert "no independent commercial services" in home
    assert home.count("<h1 ") == 1
    assert 'role="search"' in home and "'/search/' | relative_url" in home and 'name="q"' in home
    header = read("_includes/header.html")
    assert "/assets/img/logo-d.svg" in header
    assert "page_locale" not in header
    assert "portal_nav." not in header
    assert "'/knowledge/' | relative_url" in header
    assert "'/lab/' | relative_url" in header
    assert "'/research/' | relative_url" in header
    assert 'href="/about/"' in header
    assert "/services/" not in header
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


def test_legacy_service_route_is_noindex_and_reference_only():
    path = "services/sap-ams-consulting.md"
    text = read(path)
    fm = frontmatter(path)
    assert fm["permalink"] == "/services/sap-ams-consulting/"
    assert fm["robots"] == "noindex,follow"
    assert fm["sitemap"] is False
    assert "Reference-only page." in text
    assert "does not offer independent commercial services" in text
    assert "Senior SAP Consultant at [EPAM Systems]" in text


def test_strategy_defines_noncommercial_four_route_model():
    strategy = read("docs/two-focus-product-strategy.md")
    assert "English entry points only" in strategy
    assert "Private boundary" in strategy
    assert "Knowledge Base" in strategy
    assert "Practical Setup" in strategy
    assert "Technology Watch" in strategy
    assert "Senior SAP Consultant at EPAM Systems" in strategy
    assert "No checkout" in strategy
    assert "no independent commercial services" in strategy.lower()
    assert "legacy service pages are noindex" in strategy.lower()

