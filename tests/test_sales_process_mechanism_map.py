import json
from pathlib import Path


ROOT = Path("_data/labs/enterprise_context")
PROCESS_INDEX_PATH = ROOT / "processes" / "sales_process_atlas" / "index.json"
MECHANISM_INDEX_PATH = ROOT / "mechanisms" / "sales_mechanisms" / "index.json"
PROCESS_MAP_PATH = ROOT / "mechanisms" / "sales_mechanisms" / "process_map.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_process_mechanism_map_uses_known_ids():
    process_index = load_json(PROCESS_INDEX_PATH)
    mechanism_index = load_json(MECHANISM_INDEX_PATH)
    process_map = load_json(PROCESS_MAP_PATH)

    process_codes = {
        code
        for group in process_index["groups"]
        for code in group.get("codes", [])
    }
    mechanism_codes = set(mechanism_index["mechanism_codes"])

    mapped_processes = [link["process"] for link in process_map["links"]]
    assert len(mapped_processes) == len(set(mapped_processes))

    for link in process_map["links"]:
        assert link["process"] in process_codes
        assert link["mechanisms"], f"{link['process']} has an empty mechanism composition"
        unknown = set(link["mechanisms"]) - mechanism_codes
        assert not unknown, f"{link['process']} has unknown mechanisms: {sorted(unknown)}"


def test_process_mechanism_map_declares_partial_coverage_honestly():
    process_index = load_json(PROCESS_INDEX_PATH)
    process_map = load_json(PROCESS_MAP_PATH)
    coverage = process_map["coverage"]

    assert coverage["atlas_process_count"] == process_index["process_count"]
    assert coverage["mapped_process_count"] == len(process_map["links"])
    assert coverage["is_exhaustive"] is (coverage["mapped_process_count"] == coverage["atlas_process_count"])
    assert coverage["absence_semantics"]
    assert coverage["addition_rule"]

    if not coverage["is_exhaustive"]:
        assert "not proven to use no mechanisms" in coverage["absence_semantics"]
        assert coverage["next_review_processes"]


def test_next_review_processes_are_real_and_not_already_mapped():
    process_index = load_json(PROCESS_INDEX_PATH)
    process_map = load_json(PROCESS_MAP_PATH)

    process_codes = {
        code
        for group in process_index["groups"]
        for code in group.get("codes", [])
    }
    mapped = {link["process"] for link in process_map["links"]}

    for code in process_map["coverage"]["next_review_processes"]:
        assert code in process_codes
        assert code not in mapped
