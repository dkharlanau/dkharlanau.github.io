import json
from pathlib import Path


ROOT = Path("_data/labs/enterprise_context")
MASTER = ROOT / "master_data" / "sales_master_data"
VISUAL = ROOT / "visuals" / "sales_o2c_runtime.json"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_sales_master_data_index_matches_entity_files():
    index = load(MASTER / "index.json")
    groups = [
        load(MASTER / "01_core.json"),
        load(MASTER / "02_hierarchies_and_content.json"),
        load(MASTER / "03_condition_and_relationship_records.json"),
        load(MASTER / "04_adjacent_sales_consumed_master.json"),
    ]
    entities = [entity for group in groups for entity in group.get("entities", [])]
    codes = {entity["code"] for entity in entities}

    assert index["summary"]["entity_count"] == len(entities)
    assert len(codes) == len(entities)

    required = {
        "MD.SD.BP",
        "MD.SD.ADDRESS",
        "MD.SD.PRODUCT",
        "MD.SD.CMIR",
        "MD.SD.PARTNERREL",
        "MD.SD.CUSTHIER",
        "MD.SD.PRODHIER",
        "MD.SD.ITEMPROPOSAL",
        "MD.SD.TEXT",
        "MD.SD.PRICE",
        "MD.SD.MATDET",
        "MD.SD.LISTEXCL",
        "MD.SD.FREEGOODS",
        "MD.SD.CROSS",
        "MD.SD.CREDIT",
    }
    assert required <= codes


def test_o2c_visual_has_resolved_groups_and_edges():
    visual = load(VISUAL)["visual"]
    group_ids = {group["id"] for group in visual["groups"]}
    node_ids = {node["id"] for node in visual["nodes"]}

    assert len(node_ids) == len(visual["nodes"])
    assert all(node["group"] in group_ids for node in visual["nodes"])
    assert all(edge["from"] in node_ids and edge["to"] in node_ids for edge in visual["edges"])


def test_o2c_visual_and_event_ledger_use_same_runtime_stages():
    visual_ids = [node["id"] for node in load(VISUAL)["visual"]["nodes"]]
    ledger = load(MASTER / "05_document_consumption.json")["event_ledger"]
    ledger_ids = [event["id"] for event in sorted(ledger, key=lambda item: item["order"])]

    assert ledger_ids == visual_ids
    assert ledger_ids == ["order", "supply", "delivery", "pgi", "billing", "payment"]


def test_o2c_event_ledger_keeps_read_write_proof_contract():
    ledger = load(MASTER / "05_document_consumption.json")["event_ledger"]

    for event in ledger:
        assert event["owner"]
        assert event["main_object"]
        assert event["reads"]
        assert event["writes"]
        assert event["cross_process"]
        assert event["proof"]
