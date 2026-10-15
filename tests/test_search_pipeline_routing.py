"""Search routing must respect review gates and remain independent of legacy offers."""

import json
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
ORIGIN = "https://dkharlanau.github.io"


def page_metadata(url: str) -> dict:
    assert url.startswith(ORIGIN + "/"), url
    relative = url.removeprefix(ORIGIN).strip("/")
    candidates = (
        [ROOT / "index.md", ROOT / "index.html"]
        if not relative
        else [ROOT / relative / "index.md", ROOT / relative / "index.html"]
    )
    source = next((path for path in candidates if path.is_file()), None)
    assert source is not None, f"No concrete page source found for {url}"
    content = source.read_text(encoding="utf-8")
    assert content.startswith("---\n"), source
    return yaml.safe_load(content.split("---", 2)[1])


def test_personal_lab_search_entries_are_reviewed_and_indexable():
    focus = yaml.safe_load((ROOT / "_data/site_focus.yml").read_text(encoding="utf-8"))
    assert len(focus["directions"]) == 2
    for direction in focus["directions"]:
        search_owner = direction["search_owner"]
        assert search_owner in direction["indexable_entry_points"]
        for url in direction["indexable_entry_points"]:
            metadata = page_metadata(url)
            assert metadata.get("verified") is True, url
            assert metadata.get("status") == "reviewed", url
            assert "noindex" not in metadata.get("robots", "").lower(), url
            assert metadata.get("sitemap") is True, url


def test_noindex_personal_lab_hubs_are_not_search_targets():
    focus = yaml.safe_load((ROOT / "_data/site_focus.yml").read_text(encoding="utf-8"))
    directions = {d["id"]: d for d in focus["directions"]}
    knowledge = directions["knowledge-practice"]
    lab = directions["ai-engineering-lab"]
    assert knowledge["human_entry"] == ORIGIN + "/knowledge/"
    assert knowledge["human_entry_status"] == "review-gated"
    assert ORIGIN + "/knowledge/" in knowledge["non_indexable_practice_routes"]
    assert ORIGIN + "/radar/" in lab["non_indexable_observation_routes"]
    for url in (ORIGIN + "/knowledge/", ORIGIN + "/radar/"):
        assert "noindex" in page_metadata(url).get("robots", "").lower()
        assert all(url not in d["indexable_entry_points"] for d in directions.values())


def test_recovery_priorities_are_real_lab_pages_not_commercial_routes():
    cfg = json.loads((ROOT / "config/indexation-recovery.json").read_text(encoding="utf-8"))
    priority_paths = {item["path"] for item in cfg["priority_routes"]}
    for required in ("/", "/about/", "/lab/", "/labs/", "/labs/ai-ready/"):
        assert required in priority_paths
    assert not any(path.startswith("/services/") for path in priority_paths)
    assert "/knowledge/" not in priority_paths
    assert "/radar/" not in priority_paths
    assert not any(rule["prefix"].startswith("/services/") for rule in cfg["prefix_rules"])


def test_post_deploy_search_audit_and_safe_indexnow_gate():
    google = (ROOT / ".github/workflows/google-search.yml").read_text(encoding="utf-8")
    indexnow = (ROOT / ".github/workflows/indexnow.yml").read_text(encoding="utf-8")
    assert "- pages build and deployment" in google
    assert "github.event.workflow_run.conclusion == 'success'" in google
    assert "github.event.workflow_run.head_branch == 'main'" in google
    assert "post-deploy priority refresh" in google
    assert "GOOGLE_SEARCH_CONSOLE_SERVICE_ACCOUNT" in google

    # Real IndexNow submissions still require a successful CI built-site artifact.
    assert "      - CI" in indexnow
    assert "github.event.workflow_run.conclusion == 'success'" in indexnow
    assert "ci-built-site" in indexnow
    assert "--require-key-file" in indexnow
