"""Regression tests for the synthetic Living Documentation Contract pilot."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/living_docs_demo.py"

spec = importlib.util.spec_from_file_location("living_docs_demo", MODULE_PATH)
assert spec is not None and spec.loader is not None
demo = importlib.util.module_from_spec(spec)
spec.loader.exec_module(demo)


def test_manifest_describes_real_sample_behavior():
    contract = demo.load_contract()
    payload = json.loads(
        (ROOT / "frameworks/living-documentation/example-order.json").read_text(
            encoding="utf-8"
        )
    )
    result = demo.inspect_input(contract, payload)
    assert result["missing_required_fields"] == ["departure_zone"]
    assert result["status"] == "input_incomplete"
    assert "no SAP route" in result["warning"]


def test_generated_human_card_and_diagram_are_current():
    contract = demo.load_contract()
    assert demo.CARD.read_text(encoding="utf-8") == demo.card_text(contract)
    assert demo.DIAGRAM.read_text(encoding="utf-8") == demo.diagram_text(contract)
    assert demo.DIAGRAM_SVG.read_text(encoding="utf-8") == demo.svg_text(contract)
    assert "<title" in demo.svg_text(contract)


def test_contract_change_requires_updated_projection():
    contract = demo.load_contract()
    changed = copy.deepcopy(contract)
    changed["tool"]["fields"].append(
        {
            "name": "test_new_input",
            "required": True,
            "meaning": "Synthetic schema change.",
        }
    )
    assert demo.card_text(contract) != demo.card_text(changed)
    assert "test_new_input" in demo.card_text(changed)
    assert demo.CARD.read_text(encoding="utf-8") != demo.card_text(changed)


def test_complete_payload_does_not_claim_route_determination():
    contract = demo.load_contract()
    data = {field["name"]: "TEST" for field in contract["tool"]["fields"]}
    result = demo.inspect_input(contract, data)
    assert result["missing_required_fields"] == []
    assert result["status"] == "fields_present_not_route_proven"
