"""Validate the complete Markdown cluster index used for AI search routing."""

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def _artifact():
    with (REPO_ROOT / "ai" / "markdown-clusters.json").open(encoding="utf-8") as handle:
        return json.load(handle)


def test_markdown_cluster_index_has_expected_shape_and_coverage():
    artifact = _artifact()
    assert artifact["schema"] == "dkharlanau.markdown_clusters"
    assert artifact["canonical_url"] == "https://dkharlanau.github.io/ai/markdown-clusters.json"
    assert artifact["summary"]["markdown_pages"] == len(artifact["entries"])
    assert artifact["summary"]["markdown_pages"] >= 690
    cluster_ids = {cluster["id"] for cluster in artifact["clusters"]}
    assert {"ai", "sap-architecture-course", "sap-ams", "datasets", "agent-tools"} <= cluster_ids


def test_cluster_entries_are_canonical_and_private_safe():
    artifact = _artifact()
    forbidden = ("/Users/", ".env", "Basic_LinkedInDataExport", "private-source")
    for entry in artifact["entries"]:
        if entry["canonical_url"]:
            assert entry["canonical_url"].startswith("https://dkharlanau.github.io/")
        else:
            assert entry["readiness"]["permalink_present"] is False
            assert entry["readiness"]["reviewed_retrieval_eligible"] is False
        assert entry["source_file"].endswith(".md")
        assert entry["clusters"]
        assert not any(pattern in json.dumps(entry) for pattern in forbidden)


def test_noindex_course_pages_are_not_retrieval_eligible():
    artifact = _artifact()
    course_entries = [
        entry for entry in artifact["entries"]
        if "sap-architecture-course" in entry["clusters"]
    ]
    assert len(course_entries) == 7
    assert all(entry["readiness"]["indexable"] is False for entry in course_entries)
    assert all(entry["readiness"]["reviewed_retrieval_eligible"] is False for entry in course_entries)


def test_ai_intent_pages_are_routing_candidates_without_bypassing_review_policy():
    artifact = _artifact()
    intent_entries = [
        entry for entry in artifact["entries"]
        if entry["source_file"].startswith("ai/") and entry["source_file"].endswith(".md")
        and "intent_id" in (REPO_ROOT / entry["source_file"]).read_text(encoding="utf-8")
    ]
    assert len(intent_entries) == 7
    assert all(entry["readiness"]["routing_eligible"] for entry in intent_entries)
    assert all(not entry["readiness"]["reviewed_retrieval_eligible"] for entry in intent_entries)
