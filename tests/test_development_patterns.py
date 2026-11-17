"""Structural tests for the public SAP programming pattern catalog."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = ROOT / "atlas" / "sap" / "development-patterns"


def _catalog() -> dict:
    return json.loads((ROOT / "_data" / "development_patterns.json").read_text(encoding="utf-8"))


def _page_for_permalink(route: str) -> Path:
    assert route.startswith("/atlas/sap/development-patterns/"), route
    slug = route.rstrip("/").rsplit("/", 1)[-1]
    if slug == "development-patterns":
        return CATALOG_ROOT / "index.md"
    return CATALOG_ROOT / f"{slug}.md"


def test_catalog_is_large_unique_and_useful() -> None:
    data = _catalog()
    patterns = data["patterns"]
    groups = {group["id"] for group in data["groups"]}
    assert len(patterns) >= 150
    assert len(groups) >= 8
    assert len({item["slug"] for item in patterns}) == len(patterns)
    assert all(item["category"] in groups for item in patterns)
    for item in patterns:
        for key in ("name", "problem", "solution", "sap_example", "pitfall"):
            assert str(item[key]).strip(), f"{item['slug']} missing {key}"


def test_all_pattern_profile_links_have_pages() -> None:
    for item in _catalog()["patterns"]:
        if item.get("profile"):
            assert _page_for_permalink(item["profile"]).is_file(), item["profile"]


def test_hub_pattern_links_and_noindex_policy() -> None:
    hub = (CATALOG_ROOT / "index.md").read_text(encoding="utf-8")
    for path in set(re.findall(r'href="(/atlas/sap/development-patterns/[^"#]+/)"', hub)):
        assert _page_for_permalink(path).is_file(), path
    for expected in ("status: needs_verification", "verified: false", "robots: noindex,follow", "sitemap: false"):
        assert expected in hub
    assert 'id="pattern-search"' in hub
    assert 'id="pattern-group"' in hub


def test_pattern_pages_keep_provisional_review_state() -> None:
    for page in CATALOG_ROOT.glob("*.md"):
        source = page.read_text(encoding="utf-8")
        assert "status: needs_verification" in source, page
        assert "verified: false" in source, page
        assert "robots: noindex,follow" in source, page
        assert "sitemap: false" in source, page
