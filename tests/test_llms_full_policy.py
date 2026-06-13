"""Verify llms-full.txt only contains verified, indexable Atlas pages.

This test provides defense-in-depth on top of scripts/check_indexing_policy.py
and scripts/generate_atlas_artifacts.py --check.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
PAGE_RE = re.compile(r"^PAGE: (.+)$", re.MULTILINE)
URL_RE = re.compile(r"^URL: (.+)$", re.MULTILINE)


def _parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def _build_permalink_map() -> dict[str, Path]:
    mapping: dict[str, Path] = {}
    for md_path in REPO_ROOT.rglob("*.md"):
        rel = md_path.relative_to(REPO_ROOT).as_posix()
        if any(
            rel.startswith(x)
            for x in (
                "_site/",
                ".git/",
                "vendor/",
                "node_modules/",
            )
        ):
            continue
        fm = _parse_frontmatter(md_path)
        permalink = fm.get("permalink", "")
        if permalink:
            mapping[permalink] = md_path
    return mapping


def test_llms_full_exists():
    path = REPO_ROOT / "llms-full.txt"
    assert path.exists(), "llms-full.txt should exist"
    assert path.stat().st_size > 0, "llms-full.txt should not be empty"


def test_llms_full_only_includes_verified_reviewed_pages():
    llms_path = REPO_ROOT / "llms-full.txt"
    text = llms_path.read_text(encoding="utf-8")

    titles = PAGE_RE.findall(text)
    urls = URL_RE.findall(text)
    assert len(titles) == len(urls), "Every PAGE must have a URL"

    permalink_map = _build_permalink_map()
    failures: list[str] = []

    for title, url in zip(titles, urls):
        source = permalink_map.get(url)
        if not source:
            failures.append(f"{title}: URL {url} has no matching source markdown")
            continue

        fm = _parse_frontmatter(source)
        verified = fm.get("verified", False)
        status = fm.get("status", "")
        robots = fm.get("robots", "")
        sitemap = fm.get("sitemap", True)

        if not verified:
            failures.append(f"{title}: source {source.relative_to(REPO_ROOT)} is not verified")
        if status != "reviewed":
            failures.append(f"{title}: source {source.relative_to(REPO_ROOT)} status is '{status}', expected 'reviewed'")
        if "noindex" in robots.lower():
            failures.append(f"{title}: source {source.relative_to(REPO_ROOT)} has robots:noindex")
        if sitemap is False:
            failures.append(f"{title}: source {source.relative_to(REPO_ROOT)} has sitemap:false")

    if failures:
        pytest.fail("llms-full.txt contains non-indexable/unverified pages:\n" + "\n".join(failures))


def test_llms_full_contains_no_private_path_patterns():
    llms_path = REPO_ROOT / "llms-full.txt"
    text = llms_path.read_text(encoding="utf-8")

    forbidden = ["/Users/", "source_files", "private-source", "kb-drafts", ".env"]
    found: list[str] = []
    for pattern in forbidden:
        if pattern.lower() in text.lower():
            found.append(pattern)

    assert not found, f"llms-full.txt contains private path patterns: {found}"


def test_llms_full_no_linkedin_export_references():
    llms_path = REPO_ROOT / "llms-full.txt"
    text = llms_path.read_text(encoding="utf-8")

    assert "Basic_LinkedInDataExport" not in text
    assert "Basic_LinkInDataExport" not in text
