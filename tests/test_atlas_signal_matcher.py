import json
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import match_atlas_signal as matcher


def load_index():
    with open(REPO_ROOT / "ai" / "atlas-compact-index.json", "r", encoding="utf-8") as f:
        return json.load(f)


def strong_existing_signal():
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


def strong_new_page_signal():
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


def test_strong_signal_matches_existing_atlas_page():
    result = matcher.match_signal(strong_existing_signal(), load_index())
    assert result["decision"]["target_decision"] == "update_existing_page"
    assert result["candidates"][0]["path"] == "atlas/ai-operations/ai-agent-for-sap-support.md"
    assert result["candidates"][0]["score"] >= 0.55
    assert result["candidates"][0]["match_reasons"]
    assert result["safety"]["full_site_content_loaded"] is False
    assert result["safety"]["page_edits_performed"] is False


def test_strong_uncovered_signal_suggests_new_page_candidate():
    result = matcher.match_signal(strong_new_page_signal(), load_index())
    assert result["decision"]["target_decision"] == "create_new_page_candidate"
    assert result["decision"]["review_status"] == "draft"
    assert result["evidence_summary"]["concrete_fact_count"] == 2


def test_weak_title_only_signal_is_rejected_even_when_title_matches():
    result = matcher.match_signal(weak_signal(), load_index())
    assert result["decision"]["target_decision"] == "reject"
    assert "source body was not opened" in result["decision"]["reason"]
    assert "fewer than two concrete facts" in result["decision"]["reason"]


def test_cli_writes_reviewable_matcher_output(tmp_path):
    signal_path = tmp_path / "signal.json"
    output_path = tmp_path / "matcher-result.json"
    signal_path.write_text(json.dumps(strong_existing_signal()), encoding="utf-8")

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "match_atlas_signal.py"),
            "--signal",
            str(signal_path),
            "--output",
            str(output_path),
        ],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
    )

    assert result.returncode == 0, result.stderr
    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data["schema"] == "dkharlanau.atlas_matcher_result"
    assert data["decision"]["target_decision"] == "update_existing_page"
    assert data["safety"]["index_path"] == "ai/atlas-compact-index.json"
