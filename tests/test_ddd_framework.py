from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DDD = ROOT / "ddd"


def load_json(name: str) -> dict:
    return json.loads((DDD / name).read_text(encoding="utf-8"))


def test_ddd_machine_files_are_valid_json() -> None:
    for name in ["framework.json", "decision.schema.json", "examples.json"]:
        data = load_json(name)
        assert isinstance(data, dict), name


def test_ddd_versions_are_aligned() -> None:
    framework = load_json("framework.json")
    schema = load_json("decision.schema.json")
    examples = load_json("examples.json")
    version_file = (DDD / "VERSION").read_text(encoding="utf-8")

    version = framework["framework"]["version"]
    assert version == "0.3.0"
    assert schema["properties"]["schema_version"]["const"] == version
    assert examples["catalog"]["version"] == version
    assert f"ddd-for-acting-systems {version}" in version_file


def test_framework_links_practical_contracts() -> None:
    framework = load_json("framework.json")
    metadata = framework["framework"]
    practical = framework["practical_layer"]

    assert metadata["decision_schema"].endswith("/ddd/decision.schema.json")
    assert metadata["decision_canvas"].endswith("/ddd/decision-canvas/")
    assert metadata["reference_cases"].endswith("/ddd/examples.json")
    assert practical["decision_schema"]["schema_draft"] == "2020-12"
    assert practical["reference_cases"]["domains"]


def test_reference_decision_cards_match_core_contract_shape() -> None:
    schema = load_json("decision.schema.json")
    examples = load_json("examples.json")

    required_top = set(schema["required"])
    decision_types = set(schema["properties"]["decision_type"]["enum"])
    autonomy_levels = set(schema["$defs"]["authority"]["properties"]["autonomy_level"]["enum"])
    postures = set(schema["$defs"]["judgment"]["properties"]["design_posture"]["enum"])

    rows = examples["examples"]
    assert len(rows) >= 5

    ids: set[str] = set()
    for example in rows:
        assert example["id"] not in ids
        ids.add(example["id"])

        card = example["decision_card"]
        assert required_top.issubset(card)
        assert card["schema_version"] == "0.3.0"
        assert card["decision_type"] in decision_types
        assert card["authority"]["autonomy_level"] in autonomy_levels
        assert card["judgment"]["design_posture"] in postures
        assert card["truth"]["authoritative_inputs"]
        assert card["truth"]["invariants"]
        assert card["authority"]["scope"]
        assert card["evidence"]["retain"]
        assert card["evaluation"]["cases"]

        if card["commitment"]["creates_business_effect"]:
            assert card["commitment"]["owner"]
            assert card["commitment"]["domain_command"]
            assert card["commitment"]["transactional_system"]
            assert card["commitment"]["resulting_event"]


def test_framework_reference_catalog_matches_examples() -> None:
    framework = load_json("framework.json")
    examples = load_json("examples.json")

    framework_ids = {row["id"] for row in framework["reference_case_catalog"]}
    example_ids = {row["id"] for row in examples["examples"]}
    assert framework_ids == example_ids
