from pathlib import Path
import re

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
CLUSTERS_PATH = REPO_ROOT / "_data" / "site_clusters.yml"
HEADER_PATH = REPO_ROOT / "_includes" / "header.html"
FOOTER_PATH = REPO_ROOT / "_includes" / "footer.html"


def load_registry():
    return yaml.safe_load(CLUSTERS_PATH.read_text(encoding="utf-8"))


def primary_urls(registry):
    return [item["url"] for item in registry["primary_navigation"]]


def header_product_urls():
    html = HEADER_PATH.read_text(encoding="utf-8")
    links = re.findall(r'<a href="([^"]+)" class="([^"]*nav-link[^"]*)"', html)
    return [href for href, classes in links if "nav-link--utility" not in classes]


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
    expected = primary_urls(registry)

    assert header_product_urls() == expected
    assert set(footer_explore_urls()) == set(expected)


def test_primary_navigation_routes_are_owned_by_product_clusters():
    registry = load_registry()
    owned_routes = set()
    for cluster in registry["clusters"].values():
        hub = cluster.get("hub")
        if hub:
            owned_routes.add(hub)
        owned_routes.update(cluster.get("members", []))

    for item in registry["primary_navigation"]:
        assert item["url"] in owned_routes, f"Unowned primary route: {item['url']}"


def test_machine_layer_stays_out_of_primary_navigation():
    registry = load_registry()
    machine = registry["clusters"]["machine"]

    assert machine.get("primary_navigation") is False
    assert machine["hub"] not in primary_urls(registry)
    assert machine["hub"] not in header_product_urls()


def test_primary_navigation_has_unique_labels_and_routes():
    registry = load_registry()
    labels = [item["label"] for item in registry["primary_navigation"]]
    urls = primary_urls(registry)

    assert len(labels) == len(set(labels))
    assert len(urls) == len(set(urls))


def test_secondary_product_hubs_are_reachable_from_knowledge():
    knowledge = (REPO_ROOT / "knowledge/index.md").read_text(encoding="utf-8")
    for route in ("/labs/", "/frameworks/", "/machine/"):
        assert f'href="{route}"' in knowledge
