import subprocess
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from scripts.check_business_ai_contract import ContractError, validate_graph_payload

CONTRACT_PATH = ROOT / "_data" / "labs" / "business_ai" / "contract.yml"
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "business_ai_graph_valid.yml"


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_business_ai_contract_validator_passes_repository_model():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "check_business_ai_contract.py")],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Business AI contract passed" in result.stdout


def test_business_ai_graph_fixture_rejects_invalid_id():
    contract = load_yaml(CONTRACT_PATH)
    graph = load_yaml(FIXTURE_PATH)
    graph["nodes"][0]["id"] = "Bad ID"
    with pytest.raises(ContractError, match="Invalid node id"):
        validate_graph_payload(graph, contract)


def test_business_ai_graph_fixture_rejects_invalid_edge_type_pair():
    contract = load_yaml(CONTRACT_PATH)
    graph = load_yaml(FIXTURE_PATH)
    graph["edges"][0]["from"] = "example-case"
    with pytest.raises(ContractError, match="source type does not match"):
        validate_graph_payload(graph, contract)


def test_business_ai_graph_fixture_rejects_invalid_evidence_grade():
    contract = load_yaml(CONTRACT_PATH)
    graph = load_yaml(FIXTURE_PATH)
    graph["nodes"][4]["evidence_grade"] = "Z"
    with pytest.raises(ContractError, match="invalid evidence_grade"):
        validate_graph_payload(graph, contract)


def test_generated_outputs_are_not_canonical_sources():
    contract = load_yaml(CONTRACT_PATH)
    source_paths = {
        entry["path"] for entry in contract["source_of_truth"]["datasets"].values()
    }
    assert source_paths.isdisjoint(contract["generated_outputs"])
