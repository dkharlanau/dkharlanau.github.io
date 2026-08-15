import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
MECHANISM_ROOT = ROOT / "mechanisms" / "sales_mechanisms"
SOURCE_ROOT = ROOT / "sources"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def source_ids() -> set[str]:
    ids: set[str] = set()
    for pattern in ("*.yml", "*.yaml", "*.json"):
        for path in SOURCE_ROOT.glob(pattern):
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                continue
            for source in data.get("sources", []):
                if isinstance(source, dict) and isinstance(source.get("id"), str):
                    ids.add(source["id"])
    return ids


def mechanism_model():
    index = load_json(MECHANISM_ROOT / "index.json")
    contract = load_json(ROOT / "mechanisms" / "sales_mechanism_contract.json")
    mechanisms = []
    for group_name in index["groups"]:
        group = load_json(MECHANISM_ROOT / f"{group_name}.json")
        mechanisms.extend(group["mechanisms"])
    return index, contract, mechanisms


def test_sales_mechanism_contract_and_index_are_complete():
    index, contract, mechanisms = mechanism_model()
    required = set(contract["required_fields"])
    discovered_codes = [item["code"] for item in mechanisms]

    assert len(discovered_codes) == len(set(discovered_codes)), "Mechanism codes must be unique across groups"
    assert len(index["mechanism_codes"]) == len(set(index["mechanism_codes"])), "Index contains duplicate mechanism codes"
    assert set(index["mechanism_codes"]) == set(discovered_codes), "Index and mechanism groups disagree"

    for mechanism in mechanisms:
        missing = required - set(mechanism)
        assert not missing, f"{mechanism.get('code', '<unknown>')} missing fields: {sorted(missing)}"
        assert mechanism["code"].startswith("MEC.SD.")
        assert mechanism["id"].startswith("MEC-SD-")


def test_sales_mechanism_references_resolve():
    index, _contract, mechanisms = mechanism_model()
    codes = set(index["mechanism_codes"])
    sources = source_ids()

    for mechanism in mechanisms:
        for target in mechanism.get("downstream", []):
            if isinstance(target, str) and target.startswith("MEC."):
                assert target in codes, f"{mechanism['code']} has unknown downstream mechanism {target}"
        for source_ref in mechanism.get("source_refs", []):
            assert source_ref in sources, f"{mechanism['code']} has unknown source ref {source_ref}"

    for lane in index["lanes"]:
        for code in lane["codes"]:
            assert code in codes, f"Lane {lane['id']} references unknown mechanism {code}"

    relations = load_json(MECHANISM_ROOT / "relations.json")
    for edge in relations["edges"]:
        assert edge["from"] in codes, f"Relation has unknown from mechanism {edge['from']}"
        assert edge["to"] in codes, f"Relation has unknown to mechanism {edge['to']}"

    process_map = load_json(MECHANISM_ROOT / "process_map.json")
    for link in process_map["links"]:
        for code in link["mechanisms"]:
            assert code in codes, f"Process {link['process']} references unknown mechanism {code}"


def test_sales_derivation_layers_have_stable_unique_ids_and_sources():
    index, _contract, _mechanisms = mechanism_model()
    codes = set(index["mechanism_codes"])
    sources = source_ids()

    provenance = load_json(MECHANISM_ROOT / "field_provenance.json")
    field_ids = [item["id"] for item in provenance["fields"]]
    assert len(field_ids) == len(set(field_ids)), "Field provenance IDs must be unique"
    for item in provenance["fields"]:
        for source_ref in item.get("source_refs", []):
            assert source_ref in sources, f"{item['id']} has unknown source ref {source_ref}"
        for target in item.get("downstream", []):
            if isinstance(target, str) and target.startswith("MEC."):
                assert target in codes, f"{item['id']} has unknown downstream mechanism {target}"

    events = load_json(MECHANISM_ROOT / "redetermination_events.json")
    event_ids = [item["id"] for item in events["events"]]
    assert len(event_ids) == len(set(event_ids)), "Redetermination event IDs must be unique"
    for event in events["events"]:
        assert event["evidence_class"] in {"documented_fact", "reasoned_interpretation"}
        for source_ref in event.get("source_refs", []):
            assert source_ref in sources, f"{event['id']} has unknown source ref {source_ref}"

    matrix = load_json(MECHANISM_ROOT / "procedure_matrix.json")
    matrix_codes = [row["mechanism"] for row in matrix["rows"]]
    assert len(matrix_codes) == len(set(matrix_codes)), "Procedure matrix must contain one row per mechanism"
    for row in matrix["rows"]:
        assert row["mechanism"] in codes, f"Procedure matrix references unknown mechanism {row['mechanism']}"
        for source_ref in row.get("source_refs", []):
            assert source_ref in sources, f"{row['mechanism']} has unknown matrix source ref {source_ref}"
