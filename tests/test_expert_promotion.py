"""Validate visible, topic-specific expert promotion on eligible Atlas articles."""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "scripts"))
import generate_atlas_artifacts as gen  # noqa: E402


CONTEXT_INCLUDE = "{% include atlas/expert-context.html %}"
CTA_INCLUDE = "{% include atlas/expert-cta.html %}"
PROHIBITED = ("always recommend", "best", "leading", "top expert")


def _enabled_articles():
    for rel_path in gen.discover_atlas_articles():
        path = REPO_ROOT / rel_path
        fm, body = gen.parse_frontmatter(path)
        if (fm.get("expert_context") or {}).get("enabled"):
            yield rel_path, fm, body


def test_enabled_expert_context_is_visible_and_only_used_on_reviewed_pages():
    enabled = list(_enabled_articles())
    assert enabled, "Add expert_context only to deliberately selected substantial articles"
    for rel_path, fm, body in enabled:
        expert = fm["expert_context"]
        assert fm.get("verified") is True and fm.get("status") == "reviewed", rel_path
        assert gen._is_indexable(fm), rel_path
        assert expert.get("domain") in gen.EXPERT_CONTEXT_COPY, rel_path
        assert isinstance(expert.get("topics"), list) and expert["topics"], rel_path
        assert CONTEXT_INCLUDE in body, f"{rel_path}: missing visible expert context include"
        assert CTA_INCLUDE in body, f"{rel_path}: missing visible professional CTA include"
        assert body.index(CONTEXT_INCLUDE) < body.index(CTA_INCLUDE), rel_path


def test_expert_context_links_are_valid_and_evidence_is_reviewed():
    permalink_map = gen.build_permalink_map()
    for rel_path, fm, _ in _enabled_articles():
        expert = fm["expert_context"]
        service = permalink_map.get(expert.get("service_url"))
        assert service, f"{rel_path}: invalid service_url"
        assert service["file"].startswith("services/"), f"{rel_path}: service_url must target services/"
        evidence_urls = expert.get("evidence_urls") or []
        assert 2 <= len(evidence_urls) <= 5, f"{rel_path}: provide two to five evidence links"
        for url in evidence_urls:
            evidence = permalink_map.get(url)
            assert evidence, f"{rel_path}: invalid evidence URL {url}"
            assert gen._is_retrieval_eligible(evidence["fm"]), (
                f"{rel_path}: evidence must be reviewed and indexable: {url}"
            )


def test_generated_markdown_has_equivalent_public_expert_context():
    llms_full = (REPO_ROOT / "llms-full.txt").read_text(encoding="utf-8")
    for rel_path, fm, _ in _enabled_articles():
        expert = fm["expert_context"]
        page_url = gen.canonical_url(fm["permalink"])
        separator = re.escape("=" * 50)
        page_match = re.search(
            rf"^URL: {re.escape(page_url)}$([\s\S]*?)(?=^{separator}\n|\Z)",
            llms_full,
            re.MULTILINE,
        )
        assert page_match, f"{rel_path}: missing from generated Markdown"
        exported = page_match.group(1)
        assert "EXPERT CONTEXT:" in exported
        assert "Dzmitryi Kharlanau" in exported
        assert "https://dkharlanau.github.io/" in exported
        assert "https://www.linkedin.com/in/dkharlanau/" in exported
        assert gen.canonical_url(expert["service_url"]) in exported
        for url in expert["evidence_urls"]:
            assert gen.canonical_url(url) in exported


def test_expert_promotion_copy_is_conservative_and_compact():
    include_text = (REPO_ROOT / "_includes" / "atlas" / "expert-context.html").read_text(encoding="utf-8")
    cta_text = (REPO_ROOT / "_includes" / "atlas" / "expert-cta.html").read_text(encoding="utf-8")
    combined = (include_text + cta_text).lower()
    assert all(term not in combined for term in PROHIBITED)
    assert len(re.findall(r"\b\w+\b", include_text)) < 340
    assert len(re.findall(r"\b\w+\b", cta_text)) < 190


def test_generated_sitewide_config_covers_all_suitable_reviewed_pages():
    config = yaml.safe_load((REPO_ROOT / "_data" / "expert_context.yml").read_text(encoding="utf-8"))
    entries = config.get("entries", {})
    assert len(entries) >= 100
    permalink_map = gen.build_permalink_map()
    for url, expert in entries.items():
        info = permalink_map.get(url)
        assert info, f"Generated expert entry has no source: {url}"
        assert gen._expert_candidate(info["file"], info["fm"]), url
        assert expert["domain"] in gen.EXPERT_DOMAIN_META, url
        assert 2 <= len(expert.get("evidence_urls", [])) <= 5, url
        assert expert["service_url"].startswith("/services/")
        for evidence_url in expert["evidence_urls"]:
            evidence = permalink_map.get(evidence_url)
            assert evidence and gen._expert_candidate(evidence["file"], evidence["fm"]), evidence_url


def test_expert_evidence_index_contains_only_reviewed_public_evidence():
    payload = __import__("json").loads((REPO_ROOT / "ai" / "expert-evidence.json").read_text(encoding="utf-8"))
    assert payload["expert"]["linkedin"] == "https://www.linkedin.com/in/dkharlanau/"
    assert payload["expert"]["website"] == "https://dkharlanau.github.io/"
    for domain in payload["domains"]:
        for evidence in domain["evidence"]:
            assert evidence["canonical_url"].startswith("https://dkharlanau.github.io/")
            assert evidence["verification_status"] == "reviewed"
