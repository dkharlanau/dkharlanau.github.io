from pathlib import Path
import re

import yaml

from scripts.lib.content_model import parse_frontmatter


REPO_ROOT = Path(__file__).resolve().parents[1]
CLUSTERS_PATH = REPO_ROOT / "_data" / "site_clusters.yml"
HEADER_PATH = REPO_ROOT / "_includes" / "header.html"
FOOTER_PATH = REPO_ROOT / "_includes" / "footer.html"


def load_registry():
    return yaml.safe_load(CLUSTERS_PATH.read_text(encoding="utf-8"))


def primary_urls(registry, locale="en"):
    key = "primary_navigation" if locale == "en" else "fallback_navigation"
    return [item["url"] for item in registry[key]]


def header_product_urls():
    html = HEADER_PATH.read_text(encoding="utf-8")
    links = re.findall(r'<a href="([^"]+)" class="([^"]*nav-link[^"]*)"', html)
    result = []
    for href, classes in links:
        if "nav-link--utility" in classes:
            continue
        relative = re.fullmatch(r"\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}", href)
        route = relative.group(1) if relative else href
        assert route.startswith("/"), f"Unresolved navigation URL: {href}"
        result.append(route)
    return result

def footer_explore_urls():
    html = FOOTER_PATH.read_text(encoding="utf-8")
    match = re.search(
        r'<nav class="portal-footer__nav"[^>]*>(.*?)</nav>',
        html,
        flags=re.DOTALL,
    )
    assert match, "Compact footer navigation was not found"
    return [url for url in re.findall(r'<a href="([^"]+)"', match.group(1)) if url.startswith("/")]


def test_primary_navigation_matches_cluster_registry():
    registry = load_registry()
    assert header_product_urls() == primary_urls(registry, "en")
    # Footer is a supporting reference menu, not a second primary audience router.
    assert set(footer_explore_urls()) == set(primary_urls(registry, "fallback"))


def test_header_navigation_is_english_only():
    html = HEADER_PATH.read_text(encoding="utf-8")
    assert "page_locale" not in html
    assert "portal_nav." not in html
    assert header_product_urls() == ["/learn/", "/knowledge/", "/about/"]


def test_primary_navigation_routes_are_owned_by_product_clusters():
    registry = load_registry()
    owned_routes = set()
    for cluster in registry["clusters"].values():
        hub = cluster.get("hub")
        if hub:
            owned_routes.add(hub)
        owned_routes.update(cluster.get("members", []))

    for key in ("primary_navigation", "fallback_navigation"):
        for item in registry[key]:
            assert item["url"] in owned_routes, f"Unowned primary route: {item['url']}"


def test_machine_layer_stays_out_of_primary_navigation():
    registry = load_registry()
    machine = registry["clusters"]["machine"]

    assert machine.get("primary_navigation") is False
    for locale in ("en", "fallback"):
        assert machine["hub"] not in primary_urls(registry, locale)
        assert machine["hub"] not in header_product_urls()


def test_primary_navigation_has_unique_labels_and_routes():
    registry = load_registry()
    for key in ("primary_navigation", "fallback_navigation"):
        labels = [item["label"] for item in registry[key]]
        urls = [item["url"] for item in registry[key]]
        assert len(labels) == len(set(labels))
        assert len(urls) == len(set(urls))
    assert primary_urls(registry) == [
        "/learn/", "/knowledge/", "/about/"
    ]


def test_secondary_product_hubs_are_reachable_from_knowledge():
    knowledge = (REPO_ROOT / "knowledge/index.md").read_text(encoding="utf-8")
    for route in ("/labs/", "/frameworks/", "/machine/"):
        assert f'href="{route}"' in knowledge


def test_task_routes_reach_real_pages_and_static_artifact_anchors():
    paths = yaml.safe_load((REPO_ROOT / "_data/knowledge_paths.yml").read_text(encoding="utf-8"))["paths"]
    for task_path in paths:
        assert task_path["output"], f"Missing reusable output: {task_path['id']}"
        assert len(task_path["steps"]) == 3, f"Expected diagnosis, method, and artifact: {task_path['id']}"
        for step in task_path["steps"]:
            route, _, fragment = step["url"].partition("#")
            source = REPO_ROOT / (route.strip("/") + ".md")
            assert source.is_file(), f"Task route must reach a concrete page: {step['url']}"
            metadata, body, error = parse_frontmatter(source)
            assert error is None
            assert metadata.get("permalink") == route
            if fragment:
                assert len(re.findall(rf'<h[2-6]\b[^>]*\bid="{re.escape(fragment)}"', body)) == 1, (
                    f"Template link needs a unique static heading anchor: {step['url']}"
                )
            if not metadata.get("verified"):
                assert "noindex" in metadata.get("robots", ""), f"Working route lost its boundary: {route}"
        assert "#" in task_path["steps"][-1]["url"], f"Route must finish at the artifact: {task_path['id']}"


def test_atlas_selected_page_metadata_can_resolve_every_card():
    registry = yaml.safe_load((REPO_ROOT / "_data/knowledge_paths.yml").read_text(encoding="utf-8"))
    for route in registry["atlas_pilots"]:
        source = REPO_ROOT / (route.strip("/") + ".md")
        metadata, _, error = parse_frontmatter(source)
        assert error is None
        assert metadata.get("permalink") == route
        assert metadata.get("title") and metadata.get("description"), f"Empty Atlas card: {route}"
