"""Regression guards for production canonical and Person identity URLs."""

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_production_url_is_explicit_and_local_preview_hook_preserves_it():
    config = yaml.safe_load((REPO_ROOT / "_config.yml").read_text(encoding="utf-8"))
    assert config["url"] == "https://dkharlanau.github.io"
    assert config["production_url"] == "https://dkharlanau.github.io"
    plugin = (REPO_ROOT / "_plugins" / "production_url.rb").read_text(encoding="utf-8")
    assert 'site.config["url"] = production_url' in plugin


def test_structured_data_uses_one_person_identity():
    structured = (REPO_ROOT / "_includes" / "seo" / "structured-data.html").read_text(encoding="utf-8")
    assert 'author_profile_url = \'https://dkharlanau.github.io/about/\'' in structured
    assert 'author_linkedin_url = \'https://www.linkedin.com/in/dkharlanau/\'' in structured
    assert 'author_github_url = \'https://github.com/dkharlanau\'' in structured
    assert '"@id": "{{ author_id }}"' in structured
    assert structured.count('"sameAs": ["{{ author_website_url }}", "{{ author_linkedin_url }}", "{{ author_github_url }}"]') >= 3


def test_expert_endpoints_use_canonical_identity_urls():
    for filename in ("expert-evidence.json", "expert-promotion-inventory.json"):
        text = (REPO_ROOT / "ai" / filename).read_text(encoding="utf-8")
        assert "https://dkharlanau.github.io/" in text
        if filename == "expert-evidence.json":
            assert "https://www.linkedin.com/in/dkharlanau/" in text
        assert "localhost" not in text
