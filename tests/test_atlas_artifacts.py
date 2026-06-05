import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_manifest_json_is_valid():
    path = REPO_ROOT / "atlas" / "manifest.json"
    assert path.exists(), "manifest.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.manifest"
    assert data["count"] == 22
    assert data["verified_count"] == 14
    assert data["unverified_count"] == 8
    assert len(data["entries"]) == 22


def test_related_json_is_valid():
    path = REPO_ROOT / "ai" / "rag" / "related.json"
    assert path.exists(), "related.json missing"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    assert data["schema"] == "dkharlanau.atlas.related"
    assert data["count"] == 50
    assert data["broken_link_count"] == 0
    assert data["warnings"] == []
    assert len(data["edges"]) == 50


def test_manifest_no_private_paths():
    path = REPO_ROOT / "atlas" / "manifest.json"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    forbidden = ["source_files", "private-source", "kb-drafts", "/Users/", ".env"]
    for pattern in forbidden:
        assert pattern not in text, f"manifest.json contains forbidden pattern: {pattern}"


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


def test_no_linkedin_export_names_in_artifacts():
    for name in ["manifest.json", "llms-full.txt", "related.json"]:
        if name == "manifest.json":
            path = REPO_ROOT / "atlas" / name
        elif name == "related.json":
            path = REPO_ROOT / "ai" / "rag" / name
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
    expected_sections = {
        "ai-operations",
        "automation",
        "concepts",
        "data-quality",
        "diagnostics",
        "maps",
        "sap",
    }
    assert set(data["sections"]) == expected_sections


def test_related_edges_have_valid_targets():
    path = REPO_ROOT / "ai" / "rag" / "related.json"
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    for edge in data["edges"]:
        assert edge["valid"] is True
        assert edge["target_file"]
        assert edge["target_title"]
