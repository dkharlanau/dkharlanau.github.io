import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.check_business_ai_graph import GraphIntegrityError, build_report, records_by_id, require_refs


def test_business_ai_graph_integrity_validator_passes_repository_model():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_business_ai_graph.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Business AI graph integrity passed" in result.stdout


def test_business_ai_graph_report_separates_structural_errors_from_coverage_gaps():
    report = build_report()
    assert report["schema"] == "dkharlanau.business-ai.graph-integrity"
    assert report["contract_version"] == "1.1.0"
    assert report["structural_errors"] == 0
    assert report["counts"]["processes"] > 0
    assert isinstance(report["coverage_gaps"], list)
    assert any(gap["kind"] == "stable-stage-id" for gap in report["coverage_gaps"])


def test_business_ai_graph_rejects_duplicate_ids():
    with pytest.raises(GraphIntegrityError, match="Duplicate test id"):
        records_by_id([{"id": "same"}, {"id": "same"}], "test")


def test_business_ai_graph_rejects_orphan_reference():
    with pytest.raises(GraphIntegrityError, match="missing target"):
        require_refs("owner", "refs", ["missing"], {"known": {}}, "target")


def test_machine_graph_endpoint_is_contract_driven_and_exposes_proof_gaps():
    endpoint = (ROOT / "ai" / "business-ai-graph.json").read_text(encoding="utf-8")
    contract = (ROOT / "_data" / "labs" / "business_ai" / "contract.yml").read_text(encoding="utf-8")
    assert "site.data.labs.business_ai.contract" in endpoint
    assert '"schema": "dkharlanau.business-ai.graph"' in endpoint
    assert '"process-crosses-domain"' in endpoint
    assert '"process-uses-pattern"' in endpoint
    assert '"domain-supports-case"' in endpoint
    assert '"case-uses-pattern"' in endpoint
    assert '"proof_gaps"' in endpoint
    assert '"legacy_source_confidence": "unknown"' in endpoint
    assert "ai/business-ai-graph.json" in contract
