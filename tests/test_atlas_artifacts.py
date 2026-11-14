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
    for name in ["manifest.json", "llms-full.txt", "related.json", "atlas-compact-index.json", "verified-pages.json", "markdown-clusters.json"]:
        if name == "manifest.json":
            path = REPO_ROOT / "atlas" / name
        elif name == "related.json":
            path = REPO_ROOT / "ai" / "rag" / name
        elif name in ("atlas-compact-index.json", "verified-pages.json", "markdown-clusters.json"):
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


def test_citable_section_is_extracted_from_the_reviewed_article():
    from scripts.generate_atlas_artifacts import parse_frontmatter
    from scripts.lib.atlas_citation_sections import read_atlas_citation_sections

    path = REPO_ROOT / "atlas/concepts/sap-stock-exists-not-promisable.md"
    frontmatter, body = parse_frontmatter(path)
    url = "https://dkharlanau.github.io" + frontmatter["permalink"]
    args = {"task_anchors": frontmatter["task_pack_sections"]}
    [section] = read_atlas_citation_sections(body, frontmatter["citation_sections"], url, **args)
    index = json.loads((REPO_ROOT / "ai/verified-pages.json").read_text())
    [entry] = [row for row in index["entries"] if row["url"] == url]
    assert entry["citation_sections"] == [section]
    assert section["section_url"] == url + "#diagnostic-sequence"
    assert "inventory report alone cannot establish the reason" in section["paragraphs"][-1]
    assert all(row.get("citation_sections") is None for row in index["entries"] if "openui5-odata-" in row["url"])
    changed = body.replace("The relevant checks depend", "The appropriate checks depend", 1)
    [changed_section] = read_atlas_citation_sections(changed, frontmatter["citation_sections"], url, **args)
    assert changed_section["sha256"] != section["sha256"]
    pack = section["task_pack"]
    assert pack["schema"] == "atlas.read_only_task.v1"
    assert pack["canonical"] == section["section_url"]
    assert changed_section["task_pack"]["version"] != pack["version"]
    assert len(pack["method"]) == 5
    assert pack["sources"] == section["sources"]
    assert "https://userapps.support.sap.com/sap/support/knowledge/en/3701626" in pack["sources"]
    for value in [pack["task"], *pack["conditions"], *pack["method"], *pack["example"], *pack["check"], *pack["limits"]]:
        assert value in section["paragraphs"]
    assert not any("openui5-odata-" in row["url"] for row in index["entries"])


def test_citable_section_requires_the_declared_fragment_and_a_source():
    import pytest

    from scripts.generate_atlas_artifacts import parse_frontmatter
    from scripts.lib.atlas_citation_sections import read_atlas_citation_sections

    path = REPO_ROOT / "atlas/concepts/sap-stock-exists-not-promisable.md"
    frontmatter, body = parse_frontmatter(path)
    url = "https://dkharlanau.github.io" + frontmatter["permalink"]
    args = {"task_anchors": frontmatter["task_pack_sections"]}
    with pytest.raises(ValueError, match="heading, visible text and an HTTPS source"):
        read_atlas_citation_sections(body.replace('id="diagnostic-sequence"', ""), frontmatter["citation_sections"], url)
    hidden = body.replace('id="diagnostic-sequence"', 'id="diagnostic-sequence" hidden')
    with pytest.raises(ValueError, match="Expected one visible section"):
        read_atlas_citation_sections(hidden, frontmatter["citation_sections"], url)
    [section] = read_atlas_citation_sections(body, frontmatter["citation_sections"], url, **args)
    for source_url in section["sources"]:
        body = body.replace(source_url, "/")
    with pytest.raises(ValueError, match="heading, visible text and an HTTPS source"):
        read_atlas_citation_sections(body, frontmatter["citation_sections"], url, **args)


def test_atp_passages_keep_their_own_sources_and_identity():
    import pytest

    from scripts.generate_atlas_artifacts import parse_frontmatter
    from scripts.lib.atlas_citation_sections import content_digest, read_atlas_citation_sections

    frontmatter, body = parse_frontmatter(REPO_ROOT / "atlas/concepts/sap-stock-exists-not-promisable.md")
    url = "https://dkharlanau.github.io" + frontmatter["permalink"]
    anchors = frontmatter["citation_sections"]
    args = {"task_anchors": frontmatter["task_pack_sections"]}
    [section] = read_atlas_citation_sections(body, anchors, url, **args)
    scope, allocation, verification, case, limits = section["passages"]
    assert [(row["part"], row["url"].split("#")[-1]) for row in section["passages"]] == [
        ("method", "check-atp-scope"),
        ("method", "check-allocation-when-active"),
        ("check", "verify-schedule-line"),
        ("example", "public-edition-atp-case"),
        ("limits", "atp-case-limits"),
    ]
    pack = section["task_pack"]
    assert scope["sources"] == [pack["sources"][0]]
    assert case["sources"] == ["https://userapps.support.sap.com/sap/support/knowledge/en/3701626"]
    assert allocation["sources"] == verification["sources"] == limits["sources"] == []
    assert [row["text"] for row in section["passages"]] == [
        pack["method"][2], pack["method"][4], pack["check"][0], pack["example"][0], pack["limits"][0],
    ]
    for row in (scope, allocation, verification, case):
        assert row["context"] == {
            "section_url": section["section_url"],
            "conditions": pack["conditions"],
            "limits": pack["limits"],
        }
        assert row["sha256"] == content_digest({key: value for key, value in row.items() if key != "sha256"})
    assert "context" not in limits

    changed = body.replace("A different simulation context", "Another simulation context", 1)
    [updated] = read_atlas_citation_sections(changed, anchors, url, **args)
    assert updated["passages"][2]["sha256"] != verification["sha256"]
    assert updated["passages"][:2] == [scope, allocation]
    assert updated["passages"][3:] == [case, limits]

    changed = body.replace("The relevant checks depend", "The appropriate checks depend", 1)
    [updated] = read_atlas_citation_sections(changed, anchors, url, **args)
    assert all(before["sha256"] != after["sha256"]
               for before, after in zip(section["passages"], updated["passages"]))
    duplicate = body.replace('id="atp-case-limits"', 'id="verify-schedule-line"', 1)
    with pytest.raises(ValueError, match="duplicate citation passage ID"):
        read_atlas_citation_sections(duplicate, anchors, url, **args)


def test_task_pack_requires_complete_visible_sections():
    import pytest

    from scripts.generate_atlas_artifacts import parse_frontmatter
    from scripts.lib.atlas_citation_sections import read_atlas_citation_sections

    frontmatter, body = parse_frontmatter(REPO_ROOT / "atlas/concepts/sap-stock-exists-not-promisable.md")
    url = "https://dkharlanau.github.io" + frontmatter["permalink"]
    anchors = frontmatter["citation_sections"]
    with pytest.raises(ValueError, match="declared citation"):
        read_atlas_citation_sections(body, anchors, url, task_anchors=["unknown"])
    with pytest.raises(ValueError, match="all six parts"):
        read_atlas_citation_sections(body.replace(' data-atlas-task-part="check"', ""), anchors, url, task_anchors=anchors)


def test_atp_claim_review_checks_visible_context_without_claiming_a_source_observation():
    from scripts.generate_atlas_artifacts import parse_frontmatter
    from scripts.lib.atlas_claim_review import review_atlas_claims

    initial = review_atlas_claims(REPO_ROOT, parse_frontmatter)
    assert [claim["id"] for claim in initial] == [
        "atp-public-edition",
        "atp-create-open-quantity",
        "atp-change-confirmed-quantity",
    ]
    assert all(claim["state"] == "source_unknown" for claim in initial)
    assert all(claim["source"]["observed"] is None for claim in initial)

    def without_edition(path):
        frontmatter, body = parse_frontmatter(path)
        return frontmatter, body.replace(" in SAP S/4HANA Cloud Public Edition.", ".", 1)

    changed = review_atlas_claims(REPO_ROOT, without_edition)
    assert all(claim["state"] == "needs_review" for claim in changed)
