import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.check_business_ai_graph import (
    GraphIntegrityError,
    build_report,
    records_by_id,
    require_refs,
    source_route_exists,
)


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
    assert report["contract_version"] == "1.3.0"
    assert report["structural_errors"] == 0
    assert report["counts"]["processes"] > 0
    assert report["counts"]["process_stages"] >= 12
    assert report["counts"]["enterprise_capabilities"] >= 10
    assert report["counts"]["sap_stage_links"] >= 12
    assert report["counts"]["sap_domain_links"] >= 2
    assert isinstance(report["coverage_gaps"], list)
    assert any(gap["kind"] == "stable-stage-id" for gap in report["coverage_gaps"])


def test_business_ai_graph_rejects_duplicate_ids():
    with pytest.raises(GraphIntegrityError, match="Duplicate test id"):
        records_by_id([{"id": "same"}, {"id": "same"}], "test")


def test_business_ai_graph_rejects_orphan_reference():
    with pytest.raises(GraphIntegrityError, match="missing target"):
        require_refs("owner", "refs", ["missing"], {"known": {}}, "target")


def test_sap_cross_links_cover_priority_families_and_real_routes():
    data = yaml.safe_load(
        (ROOT / "_data" / "labs" / "business_ai" / "sap_process_links.yml").read_text(
            encoding="utf-8"
        )
    )
    families = {item["family"] for item in data["capabilities"]}
    assert {
        "lead-to-cash",
        "source-to-pay",
        "forecast-to-fulfill",
        "master-data",
        "integration-operations",
    } <= families
    for capability in data["capabilities"]:
        assert source_route_exists(capability["canonical_url"])
        for route in capability.get("operational_context_urls", []):
            assert source_route_exists(route)


def test_sap_cross_links_keep_neutral_and_platform_specific_ids_separate():
    data = yaml.safe_load(
        (ROOT / "_data" / "labs" / "business_ai" / "sap_process_links.yml").read_text(
            encoding="utf-8"
        )
    )
    stage_ids = {item["id"] for item in data["process_stages"]}
    capability_ids = {item["id"] for item in data["capabilities"]}
    assert all(not item.startswith("sap-") for item in stage_ids)
    assert all(item.startswith("sap-") for item in capability_ids)
    assert "Other ERP platforms should add their own capability-link dataset" in data["non_sap_usage"]["rule"]


def test_machine_graph_endpoint_is_contract_driven_and_exposes_proof_gaps():
    endpoint = (ROOT / "ai" / "business-ai-graph.json").read_text(encoding="utf-8")
    contract = (ROOT / "_data" / "labs" / "business_ai" / "contract.yml").read_text(encoding="utf-8")
    assert "site.data.labs.business_ai.contract" in endpoint
    assert "site.data.labs.business_ai.sap_process_links" in endpoint
    assert '"schema": "dkharlanau.business-ai.graph"' in endpoint
    assert '"process-crosses-domain"' in endpoint
    assert '"process-has-stage"' in endpoint
    assert '"stage-maps-to-capability"' in endpoint
    assert '"domain-maps-to-capability"' in endpoint
    assert '"process-uses-pattern"' in endpoint
    assert '"domain-supports-case"' in endpoint
    assert '"case-uses-pattern"' in endpoint
    assert '"proof_gaps"' in endpoint
    assert '"legacy_case_kind": "unknown"' in endpoint
    assert '"legacy_source_confidence": "unknown"' in endpoint
    assert '"case_contract"' in endpoint
    assert "ai/business-ai-graph.json" in contract
