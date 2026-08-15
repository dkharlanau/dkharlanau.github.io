import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
ATLAS_ROOT = ROOT / "processes" / "sales_process_atlas"
MECHANISM_ROOT = ROOT / "mechanisms" / "sales_mechanisms"
CASEBOOK_PATH = ROOT / "graphs" / "sales_diagnostic_casebook.yml"
ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-process-coverage.json")


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
    assert summary["atlas_records"] == atlas_index["process_count"]
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
