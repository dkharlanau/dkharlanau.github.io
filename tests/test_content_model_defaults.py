"""Source inventories must respect the same publication defaults as Jekyll."""
from pathlib import Path
import json
import re

import pytest
import yaml

from scripts.lib.content_model import make_page, parse_frontmatter
from scripts import generate_atlas_artifacts as artifacts


ROOT = Path(__file__).resolve().parents[1]


def model(root, relative, frontmatter=None):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('---\n' + yaml.safe_dump(frontmatter or {"title": "Example"}) + '---\nExample body.\n')
    fm, body, error = parse_frontmatter(path)
    assert error is None
    return make_page(root, path, fm, body)


def config(root, defaults):
    (root / '_config.yml').write_text(yaml.safe_dump({
        'collections': {'radar': {'output': True}, 'notes': {'output': True}},
        'defaults': defaults,
    }))


def test_collection_defaults_prevent_false_publication(tmp_path):
    config(tmp_path, [{'scope': {'path': '', 'type': 'radar'}, 'values': {
        'robots': 'noindex,follow', 'sitemap': False, 'status': 'needs_verification', 'verified': False,
    }}])
    page = model(tmp_path, '_radar/2026-10-06-example.md')
    assert not page.is_indexable and not page.retrieval_eligible
    assert page.status == 'needs_verification'
    assert page.permalink == '/radar/example/'
    ordinary = model(tmp_path, 'radar-guide.md', {'title': 'Guide', 'permalink': '/guide/'})
    assert ordinary.is_indexable


def test_frontmatter_and_nested_defaults_keep_jekyll_precedence(tmp_path):
    config(tmp_path, [
        {'scope': {'path': 'docs/reviewed'}, 'values': {'robots': 'index,follow', 'sitemap': True, 'search': {'source': 'reviewed'}}},
        {'scope': {'path': 'docs'}, 'values': {'robots': 'noindex,follow', 'sitemap': False, 'search': {'format': 'guide'}}},
    ])
    page = model(tmp_path, 'docs/reviewed/page.md', {'title': 'Example', 'permalink': '/example/', 'sitemap': False})
    assert page.robots == 'index,follow'
    assert not page.sitemap_enabled
    assert page.frontmatter['search'] == {'source': 'reviewed', 'format': 'guide'}
    assert not page.retrieval_eligible


def test_type_precedence_and_page_overrides_are_independent(tmp_path):
    config(tmp_path, [
        {'scope': {'path': '', 'type': 'notes'}, 'values': {'robots': 'noindex,follow', 'sitemap': False}},
        {'scope': {'path': ''}, 'values': {'robots': 'index,follow', 'sitemap': True}},
    ])
    draft = model(tmp_path, '_notes/2026-10-06-working.md', {'title': 'Working', 'verified': True, 'status': 'reviewed'})
    assert not draft.retrieval_eligible
    approved = model(tmp_path, '_notes/2026-10-06-approved.md', {
        'title': 'Approved', 'status': 'reviewed', 'verified': True,
        'robots': 'index,follow', 'sitemap': True, 'slug': 'stable-example',
    })
    assert approved.permalink == '/notes/stable-example/' and approved.retrieval_eligible


def test_scope_paths_do_not_match_lexical_prefixes(tmp_path):
    config(tmp_path, [{'scope': {'path': 'docs'}, 'values': {'sitemap': False}}])
    assert model(tmp_path, 'docs-other/page.md', {'title': 'Example'}).sitemap_enabled


def test_config_changes_are_not_hidden_by_a_cache(tmp_path):
    config(tmp_path, [{'scope': {'path': ''}, 'values': {'sitemap': False}}])
    assert not model(tmp_path, 'page.md').sitemap_enabled
    config(tmp_path, [{'scope': {'path': ''}, 'values': {'sitemap': True}}])
    assert model(tmp_path, 'page.md').sitemap_enabled


def test_generator_uses_effective_defaults_and_collection_routes(tmp_path, monkeypatch):
    config(tmp_path, [{'scope': {'path': '', 'type': 'radar'}, 'values': {'robots': 'noindex,follow', 'sitemap': False}}])
    model(tmp_path, '_radar/2026-10-06-example.md', {'title': 'Example', 'status': 'reviewed', 'verified': True})
    monkeypatch.setattr(artifacts, 'REPO_DIR', tmp_path)
    fm, _ = artifacts.parse_frontmatter(tmp_path / '_radar/2026-10-06-example.md')
    assert fm['permalink'] == '/radar/example/'
    assert not artifacts._is_retrieval_eligible(fm)


def test_real_source_model_matches_rendered_radar_state_and_route():
    source = ROOT / '_radar/2026-10-06-harness-engineering-software-factory-dru-knox.md'
    fm, body, error = parse_frontmatter(source)
    assert error is None
    page = make_page(ROOT, source, fm, body)
    built = ROOT / '_site' / page.permalink.strip('/') / 'index.html'
    if not built.exists():
        pytest.skip('Build the site to compare rendered publication state')
    html = built.read_text()
    robots = re.findall(r'<meta[^>]+name="robots"[^>]+content="([^"]*)"', html)
    assert page.robots in robots and 'noindex' in page.robots
    assert not page.is_indexable
