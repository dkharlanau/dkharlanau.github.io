import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
ATLAS_ROOT = ROOT / "processes" / "sales_process_atlas"
MECHANISM_ROOT = ROOT / "mechanisms" / "sales_mechanisms"
CASEBOOK_PATH = ROOT / "graphs" / "sales_diagnostic_casebook.yml"
ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-process-coverage.json")
INTEGRATION_ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-order-integration-map.json")
INTEGRATION_PAGE_PATH = Path("labs/enterprise-context/sales-processes/integrations/index.html")


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_sales_coverage_summary_matches_canonical_data():
    audit = load_json(ATLAS_ROOT / "coverage_audit.json")
    atlas_index = load_json(ATLAS_ROOT / "index.json")
    mechanism_index = load_json(MECHANISM_ROOT / "index.json")
    process_map = load_json(MECHANISM_ROOT / "process_map.json")
    casebook = load_yaml(CASEBOOK_PATH)

    summary = audit["summary"]
    assert summary["atlas_records"] == atlas_index["coverage_model"]["process_count"]
    assert summary["groups"] == len(atlas_index["groups"])
    assert summary["mechanisms"] == len(mechanism_index["mechanism_codes"])
    assert summary["reviewed_process_mechanism_compositions"] == len(process_map["links"])
    assert summary["diagnostic_cases"] == len(casebook["diagnostic_cases"])
    assert summary["assessment_drills"] == len(casebook["assessment_drills"])


def test_coverage_layers_state_partial_mapping_semantics():
    audit = load_json(ATLAS_ROOT / "coverage_audit.json")
    layers = {layer["layer"]: layer for layer in audit["coverage_layers"]}
    process_map = load_json(MECHANISM_ROOT / "process_map.json")

    mechanisms = layers["mechanism_library"]
    assert mechanisms["records"] == len(load_json(MECHANISM_ROOT / "index.json")["mechanism_codes"])
    assert mechanisms["reviewed_process_compositions"] == len(process_map["links"])
    assert mechanisms["is_process_mapping_exhaustive"] == process_map["coverage"]["is_exhaustive"]
    assert "not proof" in mechanisms["coverage_semantics"]


def test_sales_coverage_endpoint_exposes_reasoning_layers():
    endpoint = ENDPOINT_PATH.read_text(encoding="utf-8")

    assert '"mechanism_index"' in endpoint
    assert '"process_mechanism_map"' in endpoint
    assert '"diagnostic_casebook"' in endpoint
    assert "sales_complex_variants_registry" in endpoint


def test_numeric_sales_atlas_keys_use_liquid_bracket_access():
    coverage_endpoint = ENDPOINT_PATH.read_text(encoding="utf-8")
    integration_endpoint = INTEGRATION_ENDPOINT_PATH.read_text(encoding="utf-8")
    integration_page = INTEGRATION_PAGE_PATH.read_text(encoding="utf-8")

    for numeric_key in (
        "07_after_sales",
        "08_commercial_extensions",
        "09_industry_variants",
        "10_billing_lifecycle",
        "11_cross_application_execution",
    ):
        assert f"sales_process_atlas.{numeric_key}" not in coverage_endpoint
        assert f'sales_atlas["{numeric_key}"]' in coverage_endpoint

    assert "sales_process_atlas.11_cross_application_execution" not in integration_endpoint
    assert 'sales_atlas["11_cross_application_execution"]' in integration_endpoint
    assert "sales_process_atlas.11_cross_application_execution" not in integration_page
