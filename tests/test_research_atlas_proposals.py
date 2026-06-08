import json
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import generate_research_atlas_proposals as generator


PROPOSALS_PATH = REPO_ROOT / "ai" / "research-atlas-proposals.json"


def load_proposals():
    with open(PROPOSALS_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def test_proposals_file_exists():
    assert PROPOSALS_PATH.exists(), f"{PROPOSALS_PATH} must exist"


def test_top_level_schema():
    data = load_proposals()
    assert data["schema"] == "dkharlanau.research_atlas_proposals"
    assert data["schema_version"] == "1.0"
    assert "generated_at" in data
    assert "count" in data
    assert data["count"] == len(data.get("proposals", []))


def test_each_proposal_has_required_fields():
    data = load_proposals()
    for proposal in data["proposals"]:
        for field in [
            "schema",
            "schema_version",
            "generated_at",
            "source_research_page",
            "proposed_action",
            "rationale",
            "confidence",
            "source_confidence_warnings",
            "safety",
        ]:
            assert field in proposal, f"missing field: {field}"


def test_source_research_page_structure():
    data = load_proposals()
    for proposal in data["proposals"]:
        src = proposal["source_research_page"]
        assert src["path"].startswith("research/")
        assert src["title"]
        assert src["type"] in {"research_brief", "comparison", "watchlist", "source_map"}
        assert src["evidence_level"] in {"low", "medium", "high"}
        assert isinstance(src["source_count"], int)
        assert isinstance(src["topics"], list)


def test_proposed_action_values():
    data = load_proposals()
    for proposal in data["proposals"]:
        assert proposal["proposed_action"] in {"create", "extend", "ignore", "needs_review"}


def test_confidence_values():
    data = load_proposals()
    for proposal in data["proposals"]:
        assert proposal["confidence"] in {"high", "medium", "low"}


def test_safety_flags():
    data = load_proposals()
    for proposal in data["proposals"]:
        safety = proposal["safety"]
        assert safety["direct_page_edits"] is False, "must not edit pages directly"
        assert safety["auto_publish"] is False, "must not auto-publish"
        assert safety["requires_human_review"] is True, "must require human review"
        assert safety["noindex"] is True, "research must stay noindex"
        assert safety["marks_verified"] is False, "must not mark as verified"


def test_no_new_atlas_pages_created():
    """Ensure no proposal creates a public Atlas page."""
    data = load_proposals()
    for proposal in data["proposals"]:
        # Proposals should not contain a proposed_new_page block
        assert "proposed_new_page" not in proposal, "must not create new page blocks"
        # If candidate target exists, it must point to an existing Atlas page
        if "candidate_atlas_target" in proposal:
            target = proposal["candidate_atlas_target"]
            target_path = target.get("path", "")
            if target_path:
                full_path = REPO_ROOT / target_path
                assert full_path.exists(), f"candidate target must exist: {target_path}"


def test_research_pages_remain_noindex():
    """Verify that all source research pages have noindex frontmatter."""
    data = load_proposals()
    for proposal in data["proposals"]:
        src_path = REPO_ROOT / proposal["source_research_page"]["path"]
        fm, _ = generator.parse_frontmatter(src_path)
        robots = fm.get("robots", "")
        assert "noindex" in robots, f"{src_path} must be noindex"
        assert fm.get("sitemap") is False, f"{src_path} must have sitemap:false"
        assert fm.get("status") == "draft", f"{src_path} must be draft"


def test_homepage_not_touched():
    """Ensure no proposal references the homepage."""
    data = load_proposals()
    for proposal in data["proposals"]:
        src = proposal.get("source_research_page", {})
        assert src.get("url") != "/", "must not touch homepage"
        assert src.get("path") != "index.md", "must not touch homepage"
        if "candidate_atlas_target" in proposal:
            target = proposal["candidate_atlas_target"]
            assert target.get("url") != "/", "must not touch homepage"
            assert target.get("path") != "index.md", "must not touch homepage"


def test_rationale_is_non_empty():
    data = load_proposals()
    for proposal in data["proposals"]:
        assert proposal["rationale"].strip(), "rationale must not be empty"
        assert len(proposal["rationale"]) > 20, "rationale must be substantive"


def test_source_confidence_warnings_is_list():
    data = load_proposals()
    for proposal in data["proposals"]:
        assert isinstance(proposal["source_confidence_warnings"], list)


def test_matcher_result_structure():
    data = load_proposals()
    for proposal in data["proposals"]:
        matcher = proposal["matcher_result"]
        assert "decision" in matcher
        assert "candidates" in matcher
        assert matcher["decision"]["target_decision"] in {
            "update_existing_page",
            "create_new_page_candidate",
            "needs_research",
            "reject",
        }
        for candidate in matcher["candidates"]:
            assert "path" in candidate
            assert "url" in candidate
            assert "title" in candidate
            assert "score" in candidate
            assert isinstance(candidate["score"], (int, float))


def test_check_mode_passes():
    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "generate_research_atlas_proposals.py"),
            "--check",
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert "CHECK PASSED" in result.stdout


def test_cli_generates_output(tmp_path):
    output_path = tmp_path / "test-proposals.json"
    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "generate_research_atlas_proposals.py"),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    assert output_path.exists()
    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data["schema"] == "dkharlanau.research_atlas_proposals"
    assert data["count"] > 0


def test_validate_proposals_catches_bad_safety():
    good = load_proposals()
    bad = good.copy()
    bad["proposals"] = []
    # Inject a proposal with wrong safety flag
    bad_proposal = {
        "schema": "dkharlanau.research_atlas_proposal",
        "schema_version": "1.0",
        "generated_at": "2026-01-01T00:00:00Z",
        "source_research_page": {
            "path": "research/briefs/fake.md",
            "url": "",
            "title": "Fake",
            "type": "research_brief",
            "evidence_level": "low",
            "source_count": 1,
            "topics": [],
        },
        "proposed_action": "extend",
        "rationale": "test",
        "confidence": "low",
        "source_confidence_warnings": [],
        "safety": {
            "direct_page_edits": True,  # BAD
            "auto_publish": False,
            "requires_human_review": True,
            "noindex": True,
            "marks_verified": False,
        },
    }
    bad["proposals"].append(bad_proposal)
    issues = generator.validate_proposals(bad)
    assert any("direct_page_edits must be False" in i for i in issues)


def test_validate_proposals_catches_invalid_action():
    good = load_proposals()
    bad = good.copy()
    bad["proposals"] = []
    bad_proposal = {
        "schema": "dkharlanau.research_atlas_proposal",
        "schema_version": "1.0",
        "generated_at": "2026-01-01T00:00:00Z",
        "source_research_page": {
            "path": "research/briefs/fake.md",
            "url": "",
            "title": "Fake",
            "type": "research_brief",
            "evidence_level": "low",
            "source_count": 1,
            "topics": [],
        },
        "proposed_action": "publish_now",  # BAD
        "rationale": "test",
        "confidence": "low",
        "source_confidence_warnings": [],
        "safety": {
            "direct_page_edits": False,
            "auto_publish": False,
            "requires_human_review": True,
            "noindex": True,
            "marks_verified": False,
        },
    }
    bad["proposals"].append(bad_proposal)
    issues = generator.validate_proposals(bad)
    assert any("invalid action" in i for i in issues)


def test_validate_proposals_catches_non_research_source():
    good = load_proposals()
    bad = good.copy()
    bad["proposals"] = []
    bad_proposal = {
        "schema": "dkharlanau.research_atlas_proposal",
        "schema_version": "1.0",
        "generated_at": "2026-01-01T00:00:00Z",
        "source_research_page": {
            "path": "atlas/sap/fake.md",  # BAD: not under research/
            "url": "",
            "title": "Fake",
            "type": "research_brief",
            "evidence_level": "low",
            "source_count": 1,
            "topics": [],
        },
        "proposed_action": "extend",
        "rationale": "test",
        "confidence": "low",
        "source_confidence_warnings": [],
        "safety": {
            "direct_page_edits": False,
            "auto_publish": False,
            "requires_human_review": True,
            "noindex": True,
            "marks_verified": False,
        },
    }
    bad["proposals"].append(bad_proposal)
    issues = generator.validate_proposals(bad)
    assert any("source path must be under research/" in i for i in issues)
