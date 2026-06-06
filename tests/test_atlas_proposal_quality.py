import copy
import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))
TESTS_DIR = REPO_ROOT / "tests"
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

import match_atlas_signal as matcher
import propose_atlas_update as proposer
import validate_atlas_proposal as quality
import test_atlas_update_proposals as fixtures


EXISTING_SAMPLE = REPO_ROOT / "ai" / "atlas-proposals" / "examples" / "existing-page-update.json"
NEW_SAMPLE = REPO_ROOT / "ai" / "atlas-proposals" / "examples" / "new-page-candidate.json"


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def test_good_existing_page_update_passes_quality_gates():
    proposal = load_json(EXISTING_SAMPLE)
    result = quality.validate_proposal(proposal)
    assert result["passed"] is True
    assert result["status"] == "passed"
    assert result["issues"] == []
    assert result["checks"]["target_page_exists"] is True


def test_good_new_page_candidate_passes_quality_gates():
    proposal = load_json(NEW_SAMPLE)
    result = quality.validate_proposal(proposal)
    assert result["passed"] is True
    assert result["status"] == "passed"
    assert result["checks"]["new_page_noindex_until_reviewed"] is True
    assert result["checks"]["no_existing_page_above_update_threshold"] is True


def test_weak_signal_proposal_is_rejected_or_downgraded():
    signal = fixtures.weak_signal()
    match = matcher.match_signal(signal, fixtures.load_index())
    proposal = proposer.build_proposal(signal, match)
    result = quality.validate_proposal(proposal)

    assert result["passed"] is False
    assert result["status"] == "reject"
    assert result["checks"]["no_public_content_for_rejected_signal"] is True


def test_duplicate_new_page_candidate_is_rejected():
    proposal = load_json(NEW_SAMPLE)
    duplicate = copy.deepcopy(proposal)
    duplicate["proposed_new_page"]["proposed_path"] = "atlas/ai-operations/ai-agent-for-sap-support.md"

    result = quality.validate_proposal(duplicate)
    assert result["passed"] is False
    assert result["status"] == "rejected"
    assert any("already exists" in issue for issue in result["issues"])


def test_new_page_candidate_with_strong_existing_match_is_rejected():
    proposal = load_json(NEW_SAMPLE)
    duplicate = copy.deepcopy(proposal)
    duplicate["atlas_candidates"][0]["score"] = 0.9

    result = quality.validate_proposal(duplicate)
    assert result["passed"] is False
    assert any("existing Atlas candidate is strong enough" in issue for issue in result["issues"])


def test_generic_commentary_is_rejected():
    proposal = load_json(EXISTING_SAMPLE)
    generic = copy.deepcopy(proposal)
    generic["proposed_content_block"] = (
        "AI is transforming SAP operations. SAP teams need to prepare.\n\n"
        f"Source: {generic['signal']['source_url']}"
    )

    result = quality.validate_proposal(generic)
    assert result["passed"] is False
    assert any("generic commentary" in issue for issue in result["issues"])


def test_private_path_pattern_is_rejected():
    proposal = load_json(EXISTING_SAMPLE)
    private = copy.deepcopy(proposal)
    private["risks"].append("Review local file " + "/" + "Users/example/private-note.md")

    result = quality.validate_proposal(private)
    assert result["passed"] is False
    assert any("private/local path" in issue for issue in result["issues"])


def test_cli_returns_zero_for_passing_proposal():
    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "validate_atlas_proposal.py"),
            "--proposal",
            str(EXISTING_SAMPLE),
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["passed"] is True


def test_docs_reference_quality_gate_command():
    workflow = (REPO_ROOT / "docs" / "atlas" / "SIGNAL_DRIVEN_ATLAS_UPDATES.md").read_text(encoding="utf-8")
    proposal_doc = (REPO_ROOT / "docs" / "atlas" / "ATLAS_SIGNAL_PROPOSAL_FORMAT.md").read_text(encoding="utf-8")
    quality_doc = (REPO_ROOT / "docs" / "atlas" / "ATLAS_SIGNAL_QUALITY_GATES.md").read_text(encoding="utf-8")

    assert "scripts/validate_atlas_proposal.py" in workflow
    assert "scripts/validate_atlas_proposal.py" in proposal_doc
    assert "existing_page_update" in quality_doc
    assert "new_page_candidate" in quality_doc
