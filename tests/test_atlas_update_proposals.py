import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import match_atlas_signal as matcher
import propose_atlas_update as proposer


def load_index():
    with open(REPO_ROOT / "ai" / "atlas-compact-index.json", "r", encoding="utf-8") as f:
        return json.load(f)


def existing_signal():
    return {
        "record_id": "sig-ai-agent-support",
        "signal": {
            "title": "AI Agent for SAP Support",
            "source_name": "SAP Newsroom",
            "source_url": "https://news.sap.com/example-ai-agent-support",
            "source_date": "2026-06-06",
            "date_checked": "2026-06-06",
            "source_type": "official_vendor",
        },
        "evidence": {
            "source_body_opened": True,
            "concrete_facts": [
                "The source describes AI-assisted SAP support workflows.",
                "The source names human review and traceability as operating requirements.",
            ],
            "product_names": ["SAP support"],
            "named_components": ["AI agent", "runbook retrieval"],
            "numbers": [],
            "examples": ["ticket enrichment"],
        },
        "classification": {
            "sap_domain": "AI-assisted operations",
            "business_process": "Support operations",
            "technology_area": "AI agents",
            "operational_implication": "Reduce repeated triage while preserving human review.",
            "tags": ["ai-operations", "sap-ams", "operational-memory"],
        },
    }


def new_page_signal():
    return {
        "record_id": "sig-green-ledger",
        "signal": {
            "title": "SAP Green Ledger Carbon Allocation Controls",
            "source_name": "SAP Help Portal",
            "source_url": "https://help.sap.com/example-green-ledger",
            "source_date": "2026-06-06",
            "date_checked": "2026-06-06",
            "source_type": "official_docs",
        },
        "evidence": {
            "source_body_opened": True,
            "concrete_facts": [
                "The source describes carbon allocation controls for sustainability accounting.",
                "The source links reporting controls to audit and finance ownership.",
            ],
            "product_names": ["SAP Green Ledger"],
            "named_components": ["carbon allocation", "sustainability accounting"],
            "numbers": [],
            "examples": ["audit-ready sustainability postings"],
        },
        "classification": {
            "sap_domain": "Sustainability accounting",
            "business_process": "Carbon accounting",
            "technology_area": "Finance controls",
            "operational_implication": "Clarify ownership before sustainability data becomes audit evidence.",
            "tags": ["sustainability-accounting", "carbon-ledger"],
        },
    }


def weak_signal():
    return {
        "record_id": "sig-weak-title-only",
        "signal": {
            "title": "AI Agent for SAP Support",
            "source_name": "",
            "source_url": "",
            "source_date": "2026-06-06",
            "date_checked": "2026-06-06",
            "source_type": "manual_research",
        },
        "evidence": {
            "source_body_opened": False,
            "concrete_facts": [],
            "product_names": [],
            "named_components": [],
            "numbers": [],
            "examples": [],
        },
        "classification": {
            "sap_domain": "AI-assisted operations",
            "business_process": "Support operations",
            "technology_area": "AI agents",
            "operational_implication": "Title-only signal should be rejected.",
            "tags": ["ai-operations"],
        },
    }


def test_existing_page_match_generates_update_proposal():
    signal = existing_signal()
    match = matcher.match_signal(signal, load_index())
    proposal = proposer.build_proposal(signal, match)

    assert proposal["schema"] == "dkharlanau.atlas_update_proposal"
    assert proposal["proposal_type"] == "existing_page_update"
    assert proposal["target"]["path"] == "atlas/ai-operations/ai-agent-for-sap-support.md"
    assert "proposed_content_block" in proposal
    assert "SAP Newsroom" in proposal["source_attribution_block"]
    assert proposal["safety"]["direct_page_edits"] is False
    assert proposal["safety"]["requires_human_review"] is True


def test_new_page_match_generates_noindex_candidate_proposal():
    signal = new_page_signal()
    match = matcher.match_signal(signal, load_index())
    proposal = proposer.build_proposal(signal, match)

    assert proposal["proposal_type"] == "new_page_candidate"
    new_page = proposal["proposed_new_page"]
    assert new_page["proposed_path"].startswith("atlas/research-notes/")
    assert new_page["noindex_until_reviewed"] is True
    assert "why_existing_pages_are_insufficient" in new_page
    assert "proposed_content_block" in proposal


def test_weak_signal_proposal_has_no_public_content_block():
    signal = weak_signal()
    match = matcher.match_signal(signal, load_index())
    proposal = proposer.build_proposal(signal, match)

    assert proposal["proposal_type"] == "reject"
    assert "proposed_content_block" not in proposal
    assert proposal["safety"]["auto_publish"] is False


def test_cli_writes_proposal_json(tmp_path):
    signal = existing_signal()
    match = matcher.match_signal(signal, load_index())
    signal_path = tmp_path / "signal.json"
    match_path = tmp_path / "match.json"
    output_path = tmp_path / "proposal.json"
    signal_path.write_text(json.dumps(signal), encoding="utf-8")
    match_path.write_text(json.dumps(match), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "propose_atlas_update.py"),
            "--signal",
            str(signal_path),
            "--match",
            str(match_path),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data["proposal_type"] == "existing_page_update"
    assert data["validation_checklist"]


def test_committed_sample_proposals_exist():
    existing_path = REPO_ROOT / "ai" / "atlas-proposals" / "examples" / "existing-page-update.json"
    new_path = REPO_ROOT / "ai" / "atlas-proposals" / "examples" / "new-page-candidate.json"
    existing = json.loads(existing_path.read_text(encoding="utf-8"))
    new = json.loads(new_path.read_text(encoding="utf-8"))

    assert existing["proposal_type"] == "existing_page_update"
    assert existing["target"]["path"].startswith("atlas/")
    assert existing["safety"]["direct_page_edits"] is False
    assert new["proposal_type"] == "new_page_candidate"
    assert new["proposed_new_page"]["noindex_until_reviewed"] is True
    assert new["safety"]["auto_publish"] is False
