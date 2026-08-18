from datetime import date
from pathlib import Path

import yaml

from scripts.check_business_ai_graph_quality import (
    collect_graph_findings,
    collect_source_findings,
    duplicate_findings,
    route_exists,
)

ROOT = Path(__file__).resolve().parents[1]


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_enterprise_context_source_has_no_structural_errors():
    findings = collect_source_findings(today=date(2026, 8, 18))
    errors = [item for item in findings if item["severity"] == "error"]
    assert errors == []


def test_source_quality_keeps_review_gaps_advisory():
    findings = collect_source_findings(today=date(2026, 8, 18))
    review_gaps = [item for item in findings if item["rule_id"] == "BAI-GAP-001"]
    assert review_gaps
    assert all(item["severity"] == "gap" for item in review_gaps)


def test_duplicate_ids_are_structural_errors():
    findings = duplicate_findings([{"id": "same"}, {"id": "same"}], "case")
    assert findings[0]["rule_id"] == "BAI-GRAPH-001"
    assert findings[0]["severity"] == "error"


def test_sap_enterprise_directory_routes_are_valid():
    assert route_exists("/labs/enterprise-context/procurement/")
    assert route_exists("/labs/enterprise-context/sales-order/")
    assert route_exists("/labs/enterprise-context/integration-operations/")


def test_contract_fixture_still_passes_graph_quality_contract_validation():
    contract = load_yaml(ROOT / "_data" / "labs" / "business_ai" / "contract.yml")
    graph = load_yaml(ROOT / "tests" / "fixtures" / "business_ai_graph_valid.yml")
    findings = collect_graph_findings(graph, contract)
    structural = [item for item in findings if item["severity"] == "error"]
    assert structural == []
