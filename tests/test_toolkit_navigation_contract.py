"""Guard the Toolkit footer contract without changing the primary header."""
from collections import Counter
from html import unescape
from pathlib import Path
import re

import pytest
import yaml

from scripts.lib.content_model import parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_FOOTER = [
    {"label": "Lab", "url": "/lab/"},
    {"label": "Learn & prepare", "url": "/labs/"},
    {"label": "Library", "url": "/knowledge/"},
    {"label": "About", "url": "/about/"},
]
ROUTE_SOURCES = {
    "/lab/": "lab/index.html",
    "/labs/": "labs/index.md",
    "/knowledge/": "knowledge/index.md",
    "/about/": "about.md",
    "/services/": "services/index.md",
    "/services/sap-ams-consulting/": "services/sap-ams-consulting.md",
}


def registry():
    return yaml.safe_load((ROOT / "_data/site_clusters.yml").read_text())


def test_relationship_quick_run_emits_the_supported_consumer_contract():
    toolkit = yaml.safe_load((ROOT / "_data/enterprise_engineering_toolkit.yml").read_text())
    tool = next(item for item in toolkit["tools"] if item["id"] == "data-relationship-map")
    commands = tool["quickstart"]
    assert "python3 -m venv .venv" in commands
    assert ".venv/bin/data-relationship-map handoff build" in commands
    assert "build/customer-handoff --policy examples/identity-policy.json" in commands
    assert "--focus AFS:4711 --max-depth 2" in commands
    assert "--observed-at 2026-08-25T10:00:00Z" in commands
    assert commands.index("handoff build") < commands.index("handoff verify build/customer-handoff")
    assert "artifact-index.json" in tool["output"]
    assert "synthetic example" in tool["output"]
    assert "Project Evidence Graph" in tool["next"]
    assert "import-relationship" in tool["next"]
    assert "separate environment" in tool["next"]
    assert "requirement bridge" in tool["next"]
    assert "not business acceptance" in tool["next"]
    assert "Transformation Graph" not in tool["next"]
    assert tool["docs_url"].endswith("#hand-the-bounded-evidence-to-project-evidence-graph")


def assert_valid_entries(entries):
    for field in ("label", "url"):
        values = [entry[field] for entry in entries]
        assert all(isinstance(value, str) and value.strip() for value in values)
        assert all(count == 1 for count in Counter(values).values()), f"Duplicate {field}"
    for entry in entries:
        route = entry["url"]
        assert re.fullmatch(r"/(?:[a-z0-9-]+/)+", route), f"Invalid route: {route}"
        assert route in ROUTE_SOURCES, f"Unknown route: {route}"
        metadata, _, error = parse_frontmatter(ROOT / ROUTE_SOURCES[route])
        assert error is None
        assert metadata.get("permalink") == route, f"No concrete route: {route}"


def test_footer_registry_matches_visible_labels_order_and_real_routes():
    entries = registry()["fallback_navigation"]
    assert_valid_entries(entries)
    text = (ROOT / "_includes/footer.html").read_text()
    nav = re.search(r'<nav class="portal-footer__nav"[^>]*>(.*?)</nav>', text, re.S)
    assert nav, "Footer navigation is missing"
    visible = [
        {"label": unescape(label).strip(), "url": route}
        for route, label in re.findall(r'<a href="([^"]+)">(.*?)</a>', nav.group(1), re.S)
    ]
    assert_valid_entries(visible)
    assert entries == visible == EXPECTED_FOOTER


def test_toolkit_launcher_and_learning_hub_keep_distinct_roles():
    clusters = registry()["clusters"]
    labs = clusters["labs"]
    assert labs["hub"] == "/labs/"
    owners = [key for key, value in clusters.items() if "/lab/" in value.get("members", []) or value.get("hub") == "/lab/"]
    assert owners == ["labs"]
    assert "/lab/ is the executable Toolkit launcher" in labs["role"]
    assert "/labs/ is the learning and preparation hub" in labs["role"]
    assert EXPECTED_FOOTER[0]["label"] != EXPECTED_FOOTER[1]["label"]


def test_legacy_practice_routes_keep_their_noncommercial_owner_and_sources():
    practice = registry()["clusters"]["services"]
    assert practice["label"] == "Practice"
    assert "Non-commercial practice playbooks" in practice["role"]
    assert practice["hub"] == "/services/"
    assert practice["members"] == ["/services/", "/services/sap-ams-consulting/"]
    assert_valid_entries([{"label": route, "url": route} for route in practice["members"]])
    assert 'href="/lab/"' in (ROOT / "services/index.md").read_text()


@pytest.mark.parametrize("route", ["", "lab/", "//other.example/lab/", "https://other.example/lab/", "/lab/?q=1", "/lab/#tools", "/../lab/", "/lab//", "/missing/"])
def test_navigation_guard_rejects_invalid_or_unknown_routes(route):
    with pytest.raises(AssertionError):
        assert_valid_entries([{"label": "Lab", "url": route}])


@pytest.mark.parametrize("field", ["label", "url"])
def test_navigation_guard_rejects_duplicate_labels_or_routes(field):
    entries = [dict(entry) for entry in EXPECTED_FOOTER]
    entries[1][field] = entries[0][field]
    with pytest.raises(AssertionError, match=f"Duplicate {field}"):
        assert_valid_entries(entries)
