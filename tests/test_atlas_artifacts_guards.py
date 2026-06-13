"""Regression guards for Atlas verification/indexing consistency.

These tests enforce the contract between Atlas frontmatter and the generated
indexable artifacts (manifest, compact-index, verified-pages, llms-full,
sitemap). They fail loudly when a verified page is missing from an indexable
artifact or when an unverified page leaks into one.

Requires:
- PyYAML
- A built site at _site/ for sitemap checks (sitemap checks are skipped if
  _site/ is absent).
"""

from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
BASE_URL = "https://dkharlanau.github.io"

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import generate_atlas_artifacts as gen  # noqa: E402


def _atlas_pages():
    """Yield (rel_path, frontmatter) for every discovered Atlas article."""
    for rel_path in gen.discover_atlas_articles():
        abs_path = REPO_ROOT / rel_path
        fm, _ = gen.parse_frontmatter(abs_path)
        yield rel_path, fm


def _is_verified(fm: dict) -> bool:
    return fm.get("verified") is True and fm.get("status") == "reviewed"


def _load_sitemap_urls() -> set[str] | None:
    """Load all canonical URLs from built sitemap*.xml files."""
    site_dir = REPO_ROOT / "_site"
    if not site_dir.is_dir():
        return None

    urls: set[str] = set()
    for sitemap_path in sorted(site_dir.glob("sitemap*.xml")):
        try:
            tree = ET.parse(sitemap_path)
            root = tree.getroot()
        except ET.ParseError:
            text = sitemap_path.read_text(encoding="utf-8", errors="ignore").lstrip()
            if text.startswith("<?xml"):
                try:
                    root = ET.fromstring(text)
                except ET.ParseError:
                    continue
            else:
                continue

        tag = root.tag.split("}")[-1] if "}" in root.tag else root.tag
        if tag == "sitemapindex":
            for sitemap in root.findall(f"{{{SITEMAP_NS}}}sitemap"):
                loc = sitemap.find(f"{{{SITEMAP_NS}}}loc")
                if loc is None or not loc.text:
                    continue
                loc_path = site_dir / Path(urlparse(loc.text.strip()).path).name
                if not loc_path.exists():
                    continue
                try:
                    sub_root = ET.parse(loc_path).getroot()
                except ET.ParseError:
                    continue
                for url in sub_root.findall(f"{{{SITEMAP_NS}}}url"):
                    url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                    if url_loc is not None and url_loc.text:
                        urls.add(url_loc.text.strip())
        elif tag == "urlset":
            for url in root.findall(f"{{{SITEMAP_NS}}}url"):
                url_loc = url.find(f"{{{SITEMAP_NS}}}loc")
                if url_loc is not None and url_loc.text:
                    urls.add(url_loc.text.strip())
    return urls


def _artifact_url_sets() -> dict[str, set[str] | None]:
    """Load URL sets from generated indexable artifacts."""
    manifest_path = REPO_ROOT / "atlas" / "manifest.json"
    compact_path = REPO_ROOT / "ai" / "atlas-compact-index.json"
    verified_path = REPO_ROOT / "ai" / "verified-pages.json"
    llms_path = REPO_ROOT / "llms-full.txt"

    with manifest_path.open(encoding="utf-8") as f:
        manifest = json.load(f)
    manifest_urls = {e["url"] for e in manifest["entries"]}

    with compact_path.open(encoding="utf-8") as f:
        compact = json.load(f)
    compact_urls = {e["url"] for e in compact["entries"]}

    with verified_path.open(encoding="utf-8") as f:
        verified = json.load(f)
    verified_urls = {e["url"] for e in verified["entries"]}

    llms_text = llms_path.read_text(encoding="utf-8")
    llms_urls = set(re.findall(r"^URL: (.+)$", llms_text, re.MULTILINE))

    return {
        "manifest": manifest_urls,
        "compact_index": compact_urls,
        "verified_pages": verified_urls,
        "llms_full": llms_urls,
        "sitemap": _load_sitemap_urls(),
    }


def test_verified_atlas_pages_meet_indexing_invariants():
    """Every verified+reviewed Atlas article must be indexable."""
    failures: list[str] = []
    for rel_path, fm in _atlas_pages():
        if not _is_verified(fm):
            continue
        url = fm.get("permalink", "")
        prefix = f"{rel_path} ({url})"

        if fm.get("status") != "reviewed":
            failures.append(f"{prefix}: status is not 'reviewed'")
        if fm.get("level", 0) < 2:
            failures.append(f"{prefix}: level < 2")
        robots = fm.get("robots", "")
        if not robots.startswith("index,follow"):
            failures.append(f"{prefix}: robots does not start with 'index,follow': {robots!r}")
        if fm.get("sitemap", True) is not True:
            failures.append(f"{prefix}: sitemap is not true")
        if not fm.get("title"):
            failures.append(f"{prefix}: missing title")
        if not fm.get("description"):
            failures.append(f"{prefix}: missing description")
        last_reviewed = fm.get("last_reviewed")
        if not last_reviewed:
            failures.append(f"{prefix}: missing last_reviewed")
        elif not isinstance(last_reviewed, (date, str)):
            failures.append(f"{prefix}: last_reviewed is not a date or string")

    assert not failures, "Verified Atlas pages fail indexing invariants:\n" + "\n".join(failures)


def test_unverified_atlas_pages_are_excluded_from_indexing():
    """Every unverified Atlas article must explicitly opt out of indexing."""
    failures: list[str] = []
    for rel_path, fm in _atlas_pages():
        if _is_verified(fm):
            continue
        url = fm.get("permalink", "")
        robots = fm.get("robots", "")
        sitemap = fm.get("sitemap", True)
        if "noindex" not in robots.lower() and sitemap is not False:
            failures.append(
                f"{rel_path} ({url}): unverified page must have robots:noindex or sitemap:false"
            )

    assert not failures, "Unverified Atlas pages are not excluded from indexing:\n" + "\n".join(failures)


def test_verified_atlas_pages_appear_in_indexable_artifacts():
    """Every verified+reviewed Atlas article must appear in all indexable artifacts."""
    artifacts = _artifact_url_sets()
    sitemap_urls = artifacts["sitemap"]
    if sitemap_urls is None:
        pytest.skip("_site not built; sitemap checks skipped")

    missing: dict[str, list[str]] = {
        "manifest": [],
        "compact_index": [],
        "verified_pages": [],
        "llms_full": [],
        "sitemap": [],
    }

    for rel_path, fm in _atlas_pages():
        if not _is_verified(fm):
            continue
        url = fm.get("permalink", "")
        full_url = f"{BASE_URL}{url}"
        if url not in artifacts["manifest"]:
            missing["manifest"].append(f"{rel_path}: {url}")
        if url not in artifacts["compact_index"]:
            missing["compact_index"].append(f"{rel_path}: {url}")
        if url not in artifacts["verified_pages"]:
            missing["verified_pages"].append(f"{rel_path}: {url}")
        if url not in artifacts["llms_full"]:
            missing["llms_full"].append(f"{rel_path}: {url}")
        if full_url not in sitemap_urls:
            missing["sitemap"].append(f"{rel_path}: {full_url}")

    messages: list[str] = []
    for name, items in missing.items():
        if items:
            messages.append(f"{name} missing {len(items)} verified page(s):\n" + "\n".join(items))

    assert not messages, "Verified Atlas pages missing from indexable artifacts:\n\n" + "\n\n".join(messages)


def test_unverified_atlas_pages_do_not_appear_in_indexable_artifacts():
    """Unverified Atlas articles must not appear in restricted indexable artifacts."""
    artifacts = _artifact_url_sets()
    sitemap_urls = artifacts["sitemap"]
    if sitemap_urls is None:
        pytest.skip("_site not built; sitemap checks skipped")

    # manifest and compact_index intentionally include all Atlas articles; only
    # enforce exclusion from the strictly indexable artifacts.
    extra: dict[str, list[str]] = {
        "verified_pages": [],
        "llms_full": [],
        "sitemap": [],
    }

    for rel_path, fm in _atlas_pages():
        if _is_verified(fm):
            continue
        url = fm.get("permalink", "")
        full_url = f"{BASE_URL}{url}"
        if url in artifacts["verified_pages"]:
            extra["verified_pages"].append(f"{rel_path}: {url}")
        if url in artifacts["llms_full"]:
            extra["llms_full"].append(f"{rel_path}: {url}")
        if full_url in sitemap_urls:
            extra["sitemap"].append(f"{rel_path}: {full_url}")

    messages: list[str] = []
    for name, items in extra.items():
        if items:
            messages.append(f"{name} contains {len(items)} unverified page(s):\n" + "\n".join(items))

    assert not messages, "Unverified Atlas pages found in indexable artifacts:\n\n" + "\n\n".join(messages)


def test_atlas_verification_consistency_across_artifacts():
    """Frontmatter verification state must match inclusion in indexable artifacts."""
    artifacts = _artifact_url_sets()
    sitemap_urls = artifacts["sitemap"]

    manifest_path = REPO_ROOT / "atlas" / "manifest.json"
    manifest_entries = json.loads(manifest_path.read_text(encoding="utf-8"))["entries"]
    manifest_by_url = {e["url"]: e for e in manifest_entries}

    mismatches: list[str] = []
    for rel_path, fm in _atlas_pages():
        url = fm.get("permalink", "")
        is_verified = _is_verified(fm)

        in_manifest = url in artifacts["manifest"]
        in_compact = url in artifacts["compact_index"]
        in_verified_pages = url in artifacts["verified_pages"]
        in_llms = url in artifacts["llms_full"]
        in_sitemap = sitemap_urls is not None and f"{BASE_URL}{url}" in sitemap_urls

        # manifest/compact_index include all Atlas articles, so only verify
        # presence/absence for the strictly indexable artifacts.
        if is_verified != in_verified_pages:
            mismatches.append(
                f"{rel_path}: verified={is_verified} but verified_pages inclusion={in_verified_pages}"
            )
        if is_verified != in_llms:
            mismatches.append(
                f"{rel_path}: verified={is_verified} but llms_full inclusion={in_llms}"
            )
        if sitemap_urls is not None and is_verified != in_sitemap:
            mismatches.append(
                f"{rel_path}: verified={is_verified} but sitemap inclusion={in_sitemap}"
            )

        if url in manifest_by_url:
            entry = manifest_by_url[url]
            if entry.get("verified") != fm.get("verified"):
                mismatches.append(
                    f"{rel_path}: manifest verified={entry.get('verified')} != "
                    f"frontmatter verified={fm.get('verified')}"
                )
            if entry.get("status") != fm.get("status"):
                mismatches.append(
                    f"{rel_path}: manifest status={entry.get('status')} != "
                    f"frontmatter status={fm.get('status')}"
                )

    assert not mismatches, "Atlas verification inconsistent across artifacts:\n" + "\n".join(mismatches)
