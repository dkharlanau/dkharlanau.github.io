"""Source-only ownership guards for the two thin JSON endpoint projections.

These checks deliberately accept only one direct jsonify expression. They do
not evaluate Liquid or replace the required Ruby/Jekyll rendered-site checks.
A more complex template needs an explicit contract review, not a partial parser.
"""
from pathlib import Path
import re

import pytest
import yaml

from scripts.lib.content_model import parse_frontmatter


ROOT = Path(__file__).resolve().parents[1]
ENDPOINTS = [
    ("ai/focus-map.json", "site_focus", True),
    ("ai/public-portfolio.json", "public_portfolio", False),
]


def assert_endpoint_owner(path, owner, sitemap, *, root=ROOT):
    metadata, body, error = parse_frontmatter(root / path)
    assert error is None, f"{path}: invalid frontmatter: {error}"
    assert metadata.get("permalink") == "/" + path, f"{path}: endpoint route changed"
    assert "layout" in metadata and metadata["layout"] is None, f"{path}: layout must remain null"
    assert metadata.get("sitemap") is sitemap, f"{path}: sitemap policy changed"
    # Full-body matching rejects comments/raw blocks containing a decoy owner,
    # extra output, assignments, branches and filters that alter the projection.
    expression = r"\s*\{\{-?\s*site\.data\." + re.escape(owner) + r"\s*\|\s*jsonify\s*-?\}\}\s*"
    assert re.fullmatch(expression, body), f"{path}: expected only direct {owner} JSON projection"


@pytest.mark.parametrize("path,owner,sitemap", ENDPOINTS)
def test_machine_endpoint_keeps_its_single_data_owner(path, owner, sitemap):
    assert_endpoint_owner(path, owner, sitemap)


def write_endpoint(root, path, owner, sitemap, *, body=None, overrides=None):
    metadata = {"layout": None, "permalink": "/" + path, "sitemap": sitemap}
    metadata.update(overrides or {})
    target = root / path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("---\n" + yaml.safe_dump(metadata) + "---\n" + (
        body if body is not None else "{{ site.data." + owner + " | jsonify }}\n"
    ), encoding="utf-8")


@pytest.mark.parametrize("path,owner,sitemap", ENDPOINTS)
@pytest.mark.parametrize("variant", [
    "swap", "comment-decoy", "raw-decoy", "header-decoy", "html-comment-decoy",
    "conditional", "assignment", "extra-output", "duplicate", "missing-jsonify",
    "extra-filter", "string-literal", "empty", "trailing-text",
])
def test_endpoint_owner_rejects_swaps_and_inactive_decoys(tmp_path, path, owner, sitemap, variant):
    expected = "{{ site.data." + owner + " | jsonify }}"
    other = "public_portfolio" if owner == "site_focus" else "site_focus"
    wrong = "{{ site.data." + other + " | jsonify }}"
    bodies = {
        "swap": wrong,
        "comment-decoy": "{% comment %}" + expected + "{% endcomment %}" + wrong,
        "raw-decoy": "{% raw %}" + expected + "{% endraw %}" + wrong,
        "header-decoy": wrong,
        "html-comment-decoy": "<!-- " + expected + " -->" + wrong,
        "conditional": "{% if false %}" + expected + "{% else %}" + wrong + "{% endif %}",
        "assignment": "{% assign site = other %}" + expected,
        "extra-output": expected + wrong,
        "duplicate": expected + expected,
        "missing-jsonify": "{{ site.data." + owner + " }}",
        "extra-filter": expected.replace("jsonify", "jsonify | escape"),
        "string-literal": "{{ 'site.data." + owner + "' | jsonify }}",
        "empty": "",
        "trailing-text": expected + "not JSON",
    }
    overrides = {"description": expected} if variant == "header-decoy" else None
    write_endpoint(tmp_path, path, owner, sitemap, body=bodies[variant], overrides=overrides)
    with pytest.raises(AssertionError, match="direct .* JSON projection"):
        assert_endpoint_owner(path, owner, sitemap, root=tmp_path)


@pytest.mark.parametrize("path,owner,sitemap", ENDPOINTS)
@pytest.mark.parametrize("field,value", [
    ("layout", "default"), ("layout", "null"),
    ("permalink", "/wrong.json"), ("sitemap", "false"), ("sitemap", 0),
])
def test_endpoint_owner_rejects_effective_metadata_changes(tmp_path, path, owner, sitemap, field, value):
    write_endpoint(tmp_path, path, owner, sitemap, overrides={field: value})
    with pytest.raises(AssertionError, match="route changed|layout must|sitemap policy"):
        assert_endpoint_owner(path, owner, sitemap, root=tmp_path)


@pytest.mark.parametrize("path,owner,sitemap", ENDPOINTS)
@pytest.mark.parametrize("expression", [
    "{{ site.data.OWNER | jsonify }}",
    "\n\t{{site.data.OWNER|jsonify}}\n",
    "{{- site.data.OWNER | jsonify -}}\n",
])
def test_endpoint_owner_accepts_direct_projection_whitespace(tmp_path, path, owner, sitemap, expression):
    write_endpoint(tmp_path, path, owner, sitemap, body=expression.replace("OWNER", owner))
    assert_endpoint_owner(path, owner, sitemap, root=tmp_path)
