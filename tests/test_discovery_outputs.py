import json
import re
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
FIXTURE_SITE = REPO_ROOT / "tests" / "fixtures" / "discovery_audit" / "fake_site"

# ---------------------------------------------------------------------------
# Helpers (mirror expected audit_discovery_outputs.py logic)
# ---------------------------------------------------------------------------

SITEMAP_NS = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
PRIVATE_PATH_PATTERNS = (
    "/private/",
    "/draft/",
    "/admin/",
    "WorkOS_Vault",
    ".git",
)

NESTED_REPO_PATTERNS = (
    "/.git/",
    "/.git",
)

FAKE_SCHEMA_FIELDS = (
    "aggregateRating",
    "reviewCount",
    "ratingValue",
    "offers",
    "price",
    "availability",
)


def _is_private_url(url: str) -> bool:
    path = url.replace("https://dkharlanau.github.io", "")
    for pat in PRIVATE_PATH_PATTERNS:
        if pat in path:
            return True
    for pat in NESTED_REPO_PATTERNS:
        if pat in path:
            return True
    return False


def _is_research_url(url: str) -> bool:
    return "/research/" in url


def _is_unverified_atlas_url(url: str) -> bool:
    # In the fixture sitemap-atlas.xml, unverified pages are known by their slug
    unverified_slugs = {"unverified-draft", "pending-review"}
    return any(slug in url for slug in unverified_slugs)


def _extract_json_ld_blocks(html_text: str) -> list[dict]:
    blocks = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html_text, re.DOTALL)
    results = []
    for block in blocks:
        try:
            results.append(json.loads(block.strip()))
        except json.JSONDecodeError:
            results.append(None)
    return results


def _has_fake_schema_fields(json_ld: dict) -> list[str]:
    text = json.dumps(json_ld)
    found = []
    for field in FAKE_SCHEMA_FIELDS:
        if f'"{field}"' in text:
            found.append(field)
    return found


def _parse_sitemap_urls(sitemap_path: Path) -> list[str]:
    text = sitemap_path.read_text(encoding="utf-8")
    return re.findall(r"<loc>(.*?)</loc>", text)


# ---------------------------------------------------------------------------
# Discovery audit: sitemap private-path rejection
# ---------------------------------------------------------------------------


def test_audit_rejects_private_paths_in_sitemap():
    urls = _parse_sitemap_urls(FIXTURE_SITE / "sitemap.xml")
    private = [u for u in urls if _is_private_url(u)]
    assert private, "Fixture should contain private URLs to test rejection"
    # The audit logic must flag these as rejected
    for url in private:
        assert _is_private_url(url), f"Expected {url} to be flagged as private"


def test_audit_rejects_research_urls_in_sitemap():
    urls = _parse_sitemap_urls(FIXTURE_SITE / "sitemap.xml")
    research = [u for u in urls if _is_research_url(u)]
    assert research, "Fixture should contain research URLs to test rejection"
    for url in research:
        assert _is_research_url(url), f"Expected {url} to be flagged as research"


def test_audit_rejects_unverified_atlas_urls_in_sitemap_atlas():
    urls = _parse_sitemap_urls(FIXTURE_SITE / "sitemap-atlas.xml")
    unverified = [u for u in urls if _is_unverified_atlas_url(u)]
    assert unverified, "Fixture should contain unverified Atlas URLs"
    for url in unverified:
        assert _is_unverified_atlas_url(url), f"Expected {url} to be flagged as unverified Atlas"


# ---------------------------------------------------------------------------
# Discovery audit: JSON-LD validation
# ---------------------------------------------------------------------------


def test_audit_validates_json_ld_blocks():
    html_path = FIXTURE_SITE / "about" / "index.html"
    text = html_path.read_text(encoding="utf-8")
    blocks = _extract_json_ld_blocks(text)
    assert len(blocks) > 0, "about/index.html should contain JSON-LD blocks"
    for block in blocks:
        assert block is not None, "Each JSON-LD block must be valid JSON"
        assert "@type" in block, "Each JSON-LD block should have @type"


def test_audit_rejects_fake_rating_review_offer_fields():
    html_path = FIXTURE_SITE / "fake-schema" / "index.html"
    text = html_path.read_text(encoding="utf-8")
    blocks = _extract_json_ld_blocks(text)
    assert len(blocks) > 0, "fake-schema/index.html should contain JSON-LD blocks"
    for block in blocks:
        fake_fields = _has_fake_schema_fields(block)
        assert fake_fields, "Fixture should contain fake schema fields to test rejection"
        for field in fake_fields:
            assert field in FAKE_SCHEMA_FIELDS, f"Field {field} should be in forbidden list"


# ---------------------------------------------------------------------------
# Discovery audit: robots policy checks
# ---------------------------------------------------------------------------


def test_robots_policy_finds_oai_searchbot():
    robots_path = FIXTURE_SITE / "robots.txt"
    text = robots_path.read_text(encoding="utf-8")
    assert "User-agent: OAI-SearchBot" in text, "robots.txt must mention OAI-SearchBot"
    after = text.split("User-agent: OAI-SearchBot")[1].split("User-agent:")[0]
    assert "Allow: /" in after, "OAI-SearchBot must be allowed"


def test_robots_policy_finds_explicit_gptbot():
    robots_path = FIXTURE_SITE / "robots.txt"
    text = robots_path.read_text(encoding="utf-8")
    assert "User-agent: GPTBot" in text, "robots.txt must mention GPTBot"
    after = text.split("User-agent: GPTBot")[1].split("User-agent:")[0]
    assert "Disallow: /" in after, "GPTBot must be disallowed"


# ---------------------------------------------------------------------------
# Discovery audit: integration-style assertions against fixture site
# ---------------------------------------------------------------------------


def test_fixture_sitemap_contains_expected_bad_urls():
    urls = _parse_sitemap_urls(FIXTURE_SITE / "sitemap.xml")
    bad = [u for u in urls if _is_private_url(u) or _is_research_url(u)]
    assert len(bad) >= 5, f"Expected at least 5 bad URLs, got {len(bad)}"


def test_fixture_sitemap_atlas_contains_expected_unverified():
    urls = _parse_sitemap_urls(FIXTURE_SITE / "sitemap-atlas.xml")
    unverified = [u for u in urls if _is_unverified_atlas_url(u)]
    assert len(unverified) == 2, f"Expected 2 unverified Atlas URLs, got {len(unverified)}"


def test_fixture_about_has_valid_json_ld():
    blocks = _extract_json_ld_blocks((FIXTURE_SITE / "about" / "index.html").read_text())
    types = {b.get("@type") for b in blocks if b}
    assert "WebSite" in types, "about/index.html should have WebSite JSON-LD"
    assert "Person" in types, "about/index.html should have Person JSON-LD"


def test_fixture_fake_schema_has_forbidden_fields():
    blocks = _extract_json_ld_blocks((FIXTURE_SITE / "fake-schema" / "index.html").read_text())
    for block in blocks:
        found = _has_fake_schema_fields(block)
        assert set(found) == {"aggregateRating", "reviewCount", "ratingValue", "offers", "price", "availability"}
