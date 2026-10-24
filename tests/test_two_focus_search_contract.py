"""Keep the personal-lab routes consistent across human and machine surfaces."""
import json
import os
import html
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from lib.content_model import make_page, parse_frontmatter


def read(path):
    return (ROOT / path).read_text(encoding="utf-8")


def focus():
    return yaml.safe_load(read("_data/site_focus.yml"))


def source_page(url):
    route = urlparse(url).path
    candidates = [ROOT / route.strip("/") / name for name in ("index.md", "index.html")]
    candidates += [ROOT / (route.strip("/") + ".md")]
    path = next(path for path in candidates if path.is_file())
    fm, body, error = parse_frontmatter(path)
    assert not error
    assert fm["permalink"] == route
    return make_page(ROOT, path, fm, body)


def test_focus_map_has_exactly_two_current_personal_lab_directions():
    data = focus()
    assert data["primary_direction_count"] == len(data["directions"]) == 2
    assert {item["id"] for item in data["directions"]} == {"knowledge-practice", "ai-engineering-lab"}
    assert all(item["priority"] == "P0" for item in data["directions"])
    assert "not commercial offers" in data["routing_policy"]["secondary_domain_rule"]


def test_search_owners_and_indexable_entry_points_are_actually_eligible():
    for direction in focus()["directions"]:
        for url in [direction["search_owner"], *direction["indexable_entry_points"]]:
            page = source_page(url)
            assert page.retrieval_eligible, (url, page.status, page.robots)
        entry = source_page(direction["human_entry"])
        if not entry.retrieval_eligible:
            assert direction["human_entry_status"] == "review-gated"
            assert direction["search_state"] == "staged"
            assert direction["search_owner"] != direction["human_entry"]


def test_working_routes_remain_excluded_without_promotion():
    directions = {item["id"]: item for item in focus()["directions"]}
    knowledge = directions["knowledge-practice"]
    assert knowledge["human_entry"].endswith("/knowledge/")
    assert knowledge["search_owner"].endswith("/labs/interview-readiness/")
    routes = [knowledge["human_entry"], *knowledge["non_indexable_practice_routes"],
              *directions["ai-engineering-lab"]["non_indexable_supporting_routes"]]
    assert any(url.endswith("/radar/") for url in routes)
    for url in routes:
        page = source_page(url)
        assert not page.is_indexable, url
        assert "noindex" in page.robots and not page.sitemap_enabled, url


def test_arwp_profile_agrees_with_the_focus_source():
    profile = json.loads(read("ai/site-profile.json"))
    extension = profile["extensions"]["io.github.dkharlanau/two-focus-routing"]
    assert extension["primaryDirections"] == [item["id"] for item in focus()["directions"]]
    assert extension["profile"] == focus()["canonical_url"]
    assert profile["retrieval"]["indexes"][0]["url"] == focus()["canonical_url"]
    assert "Personal SAP & AI Lab" in profile["name"]
    ai_profile = json.loads(read("ai/ai-search-profile.json"))
    assert "Personal SAP & AI Lab" in ai_profile["site"]["name"]
    assert "commercial consulting offer" in ai_profile["objective"]["primary"]


def test_human_hub_and_homepage_graph_use_the_same_direction_source():
    hub = read("ai/index.md")
    head = read("_includes/head.html")
    for template in (hub, head):
        assert "for direction in site.data.site_focus.directions" in template
        assert "direction.label" in template and "direction.human_entry" in template
    assert "direction.job_to_be_done" in hub
    assert "SAP AMS Optimization" not in head
    assert "SAP learning/practice or SAP AMS optimization" not in hub


def test_head_and_manifest_expose_existing_toolkit_data():
    hub, _, error = parse_frontmatter(ROOT / "ai/index.md")
    toolkit, _, toolkit_error = parse_frontmatter(ROOT / "lab/index.html")
    assert not error and not toolkit_error
    assert "/ai/focus-map.json" in hub["machine_readable"]
    assert toolkit["ai_sidecar"] == "/lab/toolkit.json"
    assert "https://dkharlanau.github.io/lab/toolkit.json" in read("_includes/llms-manifest.txt")
    assert '/lab/toolkit.json' in read("ai/index.md")
    assert "page.ai_sidecar | absolute_url" in read("_includes/seo/page-machine-links.html")


def test_focus_map_keeps_its_existing_machine_sitemap_contract():
    endpoint = read("ai/focus-map.json")
    sitemap = read("sitemap-data.xml")
    assert "permalink: /ai/focus-map.json" in endpoint
    assert "sitemap: true" in endpoint
    assert 'where: "url", "/ai/focus-map.json"' in sitemap


def test_rendered_routes_and_graph_match_the_machine_contract():
    site = Path(os.environ.get("ROUTING_SITE_DIR", ROOT / "_site"))
    if not (site / "ai/index.html").is_file():
        pytest.skip("Build the site to check rendered route parity")
    data = json.loads((site / "ai/focus-map.json").read_text())
    assert data == json.loads(json.dumps(focus(), default=str))
    hub = (site / "ai/index.html").read_text()
    routes = re.search(r'<div class="ai-route-list ai-primary-routes">(.*?)</div>', hub, re.S).group(1)
    for direction in data["directions"]:
        link = re.search(r'<a href="' + re.escape(direction["human_entry"]) + r'">(.*?)</a>', routes, re.S)
        assert link and direction["label"] in html.unescape(link.group(1))
        for url in direction["indexable_entry_points"]:
            rendered = (site / urlparse(url).path.strip("/") / "index.html").read_text()
            robots = re.findall(r'<meta[^>]+name="robots"[^>]+content="([^"]*)"', rendered)
            assert all("noindex" not in item.lower() for item in robots)
    home = (site / "index.html").read_text()
    graphs = [json.loads(block) for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', home, re.S)]
    website = next(graph for graph in graphs if graph.get("@type") == "WebSite")
    assert [(part["name"], part["url"]) for part in website["hasPart"]] == [(d["label"], d["human_entry"]) for d in data["directions"]]
    toolkit_head = (site / "lab/index.html").read_text().split("</head>")[0]
    assert '<link rel="describedby" type="application/json" href="https://dkharlanau.github.io/lab/toolkit.json"' in toolkit_head
