import json
from pathlib import Path


ROOT = Path("_data/labs/enterprise_context")
BILLING_PATH = ROOT / "processes" / "sales_process_atlas" / "10_billing_lifecycle.json"
SOURCE_PATH = ROOT / "sources" / "sales_complex_variants_registry.json"
PROCESS_MAP_PATH = ROOT / "mechanisms" / "sales_mechanisms" / "process_map.json"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_advanced_down_payment_is_a_distinct_sales_process():
    billing = load_json(BILLING_PATH)
    processes = {item["code"]: item for item in billing["processes"]}

    assert "SD.DP.CLASSIC" in processes
    assert "SD.DP.ADV" in processes

    advanced = processes["SD.DP.ADV"]
    scopes = {item["id"] for item in advanced["sap_scope_items"]}
    assert scopes == {"7S7", "7Z1"}
    assert "delivery-related" in " ".join(advanced["impact_summary"]).lower()
    assert "order-related" in " ".join(advanced["impact_summary"]).lower()
    assert any("classic" in item.lower() and "one business transaction" in item.lower() for item in advanced["constraints"])
    assert any("retroactive billing" in item.lower() for item in advanced["constraints"])


def test_advanced_down_payment_sources_resolve_in_verified_registry():
    billing = load_json(BILLING_PATH)
    registry = load_json(SOURCE_PATH)
    sources = {item["id"]: item for item in registry["sources"]}
    advanced = next(item for item in billing["processes"] if item["code"] == "SD.DP.ADV")

    for source_ref in advanced["source_refs"]:
        assert source_ref in sources
        assert sources[source_ref]["status"] == "source_verified"
        assert sources[source_ref]["publisher"] == "SAP"


def test_advanced_down_payment_has_reviewed_reusable_mechanisms():
    process_map = load_json(PROCESS_MAP_PATH)
    links = {item["process"]: item for item in process_map["links"]}

    advanced = links["SD.DP.ADV"]
    assert {"MEC.SD.BILLPLAN", "MEC.SD.BILLREL", "MEC.SD.BILLTYPE", "MEC.SD.BILL", "MEC.SD.ACCOUNT"}.issubset(advanced["mechanisms"])
    assert advanced["unmodeled_controls"]
