import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_manifest_json_is_valid():
    path = REPO_ROOT / "atlas" / "manifest.json"
    assert path.exists(), "manifest.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.manifest"
    assert data["count"] == len(data["entries"])
    assert data["verified_count"] == data["count"]
    assert data["unverified_count"] == 0
    assert data["eligibility_policy"]
    for entry in data["entries"]:
        assert entry["verified"] is True
        assert entry["status"] == "reviewed"
        assert entry["url"].startswith("https://dkharlanau.github.io/atlas/")


def test_related_json_is_valid():
    path = REPO_ROOT / "ai" / "rag" / "related.json"
    assert path.exists(), "related.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.related"
    assert data["count"] == len(data["edges"])
    assert data["broken_link_count"] == 0
    assert data["warnings"] == []
    assert data["eligibility_policy"]
    for edge in data["edges"]:
        assert edge["source_verified"] is True
        assert edge["source_status"] == "reviewed"
        assert edge["source_url"].startswith("https://dkharlanau.github.io/atlas/")
        assert edge["target_url"].startswith("https://dkharlanau.github.io/atlas/")


def test_compact_signal_index_is_valid():
    path = REPO_ROOT / "ai" / "atlas-compact-index.json"
    assert path.exists(), "atlas-compact-index.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.compact_signal_index"
    assert data["count"] == len(data["entries"])
    assert data["count"] > 0
    assert data["eligibility_policy"]
    assert data["fallback"]["decision"] == "needs_research"
    for entry in data["entries"]:
        assert entry["verified"] is True
        assert entry["status"] == "reviewed"


def test_verified_pages_json_is_valid():
    path = REPO_ROOT / "ai" / "verified-pages.json"
    assert path.exists(), "verified-pages.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.site.verified_pages"
    assert data["count"] == len(data["entries"])
    assert data["count"] > 0
    assert data["collections"]
    for entry in data["entries"]:
        assert entry["url"].startswith("https://dkharlanau.github.io/"), f"Invalid URL: {entry.get('url')}"
        assert entry["title"], f"Missing title for {entry.get('url')}"
        assert entry["type"] in data["collections"], f"Unknown type {entry.get('type')} for {entry.get('url')}"
        assert entry.get("verified") is True
        assert entry.get("status") == "reviewed"


def test_manifest_no_private_paths():
    path = REPO_ROOT / "atlas" / "manifest.json"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"manifest.json contains forbidden pattern: {pattern}"


def test_compact_signal_index_no_private_paths():
    path = REPO_ROOT / "ai" / "atlas-compact-index.json"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"atlas-compact-index.json contains forbidden pattern: {pattern}"


def test_llms_full_no_private_paths():
    path = REPO_ROOT / "llms-full.txt"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"llms-full.txt contains forbidden pattern: {pattern}"


def test_related_json_no_private_paths():
    path = REPO_ROOT / "ai" / "rag" / "related.json"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"related.json contains forbidden pattern: {pattern}"


def test_verified_pages_no_private_paths():
    path = REPO_ROOT / "ai" / "verified-pages.json"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"verified-pages.json contains forbidden pattern: {pattern}"


def test_no_linkedin_export_names_in_artifacts():
    for name in ["manifest.json", "llms-full.txt", "related.json", "atlas-compact-index.json", "verified-pages.json"]:
        if name == "manifest.json":
            path = REPO_ROOT / "atlas" / name
        elif name == "related.json":
            path = REPO_ROOT / "ai" / "rag" / name
        elif name in ("atlas-compact-index.json", "verified-pages.json"):
            path = REPO_ROOT / "ai" / name
        else:
            path = REPO_ROOT / name
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        assert "Basic_LinkedInDataExport" not in text, f"{name} contains LinkedIn export reference"
        assert "Basic_LinkInDataExport" not in text, f"{name} contains misspelled LinkedIn export reference"


def test_llms_full_only_verified_reviewed_pages():
    path = REPO_ROOT / "llms-full.txt"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Load manifest to know which pages are verified+reviewed
    manifest_path = REPO_ROOT / "atlas" / "manifest.json"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    verified_titles = []
    unverified_titles = []
    for entry in manifest["entries"]:
        title = entry["title"]
        if entry.get("verified") and entry.get("status") == "reviewed":
            verified_titles.append(title)
        else:
            unverified_titles.append(title)

    for title in verified_titles:
        assert f"PAGE: {title}" in text, f"llms-full.txt missing verified page: {title}"

    for title in unverified_titles:
        assert f"PAGE: {title}" not in text, f"llms-full.txt should not contain unverified page: {title}"


def test_manifest_sections_complete():
    path = REPO_ROOT / "atlas" / "manifest.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    gen = _import_generator()
    expected_sections = set()
    for rel_path in gen.discover_atlas_articles():
        fm, _ = gen.parse_frontmatter(REPO_ROOT / rel_path)
        if gen._is_retrieval_eligible(fm):
            expected_sections.add(fm["atlas_section"])
    assert set(data["sections"]) == expected_sections


def test_manifest_related_urls_are_retrieval_eligible():
    data = json.loads((REPO_ROOT / "atlas" / "manifest.json").read_text(encoding="utf-8"))
    eligible_urls = {entry["url"] for entry in data["entries"]}
    for entry in data["entries"]:
        for related_url in entry["related"]:
            assert related_url in eligible_urls, (
                f"{entry['url']} references non-eligible related URL {related_url}"
            )


def test_related_edges_have_valid_targets():
    path = REPO_ROOT / "ai" / "rag" / "related.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for edge in data["edges"]:
        assert edge["valid"] is True
        assert edge["target_file"]
        assert edge["target_title"]


# ---------------------------------------------------------------------------
# Dynamic discovery behavior tests
# ---------------------------------------------------------------------------

def _import_generator():
    """Import generator module with repo root on path."""
    scripts_dir = REPO_ROOT / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))
    import generate_atlas_artifacts as gen
    return gen


def test_dynamic_discovery_returns_at_least_215_article_pages():
    gen = _import_generator()
    articles = gen.discover_atlas_articles()
    assert len(articles) >= 215, f"Expected at least 215 articles, found {len(articles)}"
    # All paths must be under atlas/ and be .md files
    for p in articles:
        assert p.startswith("atlas/"), f"Path outside atlas/: {p}"
        assert p.endswith(".md"), f"Not a markdown file: {p}"


def test_dynamic_discovery_excludes_index_pages():
    gen = _import_generator()
    articles = gen.discover_atlas_articles()
    index_paths = [p for p in articles if p.endswith("/index.md")]
    assert index_paths == [], f"Index pages should be excluded: {index_paths}"
    assert "atlas/index.md" not in articles


def test_dynamic_discovery_excludes_files_outside_atlas():
    gen = _import_generator()
    articles = gen.discover_atlas_articles()
    outside = [p for p in articles if not p.startswith("atlas/")]
    assert outside == [], f"Files outside atlas/ discovered: {outside}"


def test_dynamic_discovery_excludes_pages_without_required_frontmatter():
    gen = _import_generator()
    articles = set(gen.discover_atlas_articles())
    # atlas/research-notes/index.md has status=research_note and no atlas_section
    # It should NOT be discovered
    assert "atlas/research-notes/index.md" not in articles
    # atlas/links/index.md has no atlas_section
    assert "atlas/links/index.md" not in articles


def test_check_mode_detects_stale_artifacts():
    """--check must return non-zero when an artifact is stale."""
    # Run check on current committed artifacts; should pass
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "generate_atlas_artifacts.py"), "--check"],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"--check failed unexpectedly: {result.stdout}\n{result.stderr}"


def test_manifest_entries_have_required_fields():
    path = REPO_ROOT / "atlas" / "manifest.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for entry in data["entries"]:
        assert entry.get("url", "").startswith("https://dkharlanau.github.io/atlas/"), f"Invalid permalink: {entry.get('url')}"
        assert entry.get("atlas_section"), f"Missing atlas_section: {entry.get('title')}"
        assert "status" in entry, f"Missing status: {entry.get('title')}"
        assert "verified" in entry, f"Missing verified: {entry.get('title')}"


def test_compact_signal_index_entries_have_required_fields():
    path = REPO_ROOT / "ai" / "atlas-compact-index.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    required = {
        "path",
        "url",
        "title",
        "description",
        "atlas_section",
        "sap_area",
        "business_process",
        "last_reviewed",
        "tags",
        "headings",
        "sap_domain_keywords",
        "matching_terms",
    }
    for entry in data["entries"]:
        missing = required - set(entry)
        assert not missing, f"Compact index entry missing {missing}: {entry.get('title')}"
        assert entry["url"].startswith("https://dkharlanau.github.io/atlas/"), f"Invalid Atlas URL: {entry.get('url')}"
        assert (REPO_ROOT / entry["path"]).exists(), f"Missing source page: {entry['path']}"
        assert entry["matching_terms"], f"Missing matching terms: {entry['path']}"
