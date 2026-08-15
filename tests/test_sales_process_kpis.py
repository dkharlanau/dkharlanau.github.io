import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
MODEL_PATH = ROOT / "graphs" / "sales_process_kpis.yml"
PROCESS_INDEX = ROOT / "processes" / "sales_process_atlas" / "index.json"
MECHANISM_INDEX = ROOT / "mechanisms" / "sales_mechanisms" / "index.json"
CASEBOOK_PATH = ROOT / "graphs" / "sales_diagnostic_casebook.yml"
SOURCE_PATH = ROOT / "sources" / "sales_analytics_registry.json"
CONTRACT_PATH = ROOT / "agent_contracts" / "sales.yml"
HUMAN_PATH = Path("labs/enterprise-context/sales-analytics/index.html")
MACHINE_PATH = Path("labs/enterprise-context/data/sales-process-kpis.json")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_sales_kpi_catalog_has_business_contract():
    model = load_yaml(MODEL_PATH)
    kpis = model["kpis"]
    ids = [item["id"] for item in kpis]

    assert model["id"] == "GRAPH-SD-SALES-PROCESS-KPIS"
    assert len(kpis) >= 28
    assert len(ids) == len(set(ids))
    assert len(model["analytics_lenses"]) >= 6
    assert len(model["common_language"]) >= 10

    required = {
        "business_question",
        "formula",
        "unit",
        "direction",
        "grain",
        "process_refs",
        "mechanism_refs",
        "data_signals",
        "owner",
        "cadence",
        "target_policy",
        "source_refs",
    }
    for kpi in kpis:
        assert kpi["id"].startswith("KPI.SD.")
        assert required.issubset(kpi)
        assert kpi["business_question"]
        assert kpi["formula"]
        assert kpi["target_policy"]
        assert kpi["process_refs"]
        assert kpi["data_signals"]


def test_sales_kpi_references_resolve():
    model = load_yaml(MODEL_PATH)
    process_codes = {
        code
        for group in load_json(PROCESS_INDEX)["groups"]
        for code in group["codes"]
    }
    mechanism_codes = set(load_json(MECHANISM_INDEX)["mechanism_codes"])
    case_ids = {item["id"] for item in load_yaml(CASEBOOK_PATH)["diagnostic_cases"]}
    source_ids = {item["id"] for item in load_json(SOURCE_PATH)["sources"]}

    for kpi in model["kpis"]:
        assert set(kpi["process_refs"]) <= process_codes, kpi["id"]
        assert set(kpi["mechanism_refs"]) <= mechanism_codes, kpi["id"]
        assert set(kpi.get("diagnostic_case_refs", [])) <= case_ids, kpi["id"]
        assert set(kpi["source_refs"]) <= source_ids, kpi["id"]

    assert set(model["source_refs"]) <= source_ids


def test_sales_kpi_lenses_reference_real_kpis():
    model = load_yaml(MODEL_PATH)
    kpi_ids = {item["id"] for item in model["kpis"]}

    for lens in model["analytics_lenses"]:
        assert lens["id"].startswith("SDL.")
        assert lens["business_question"]
        assert set(lens["kpi_refs"]) <= kpi_ids

    for play in model["root_cause_playbook"]:
        assert set(play["start_with"]) <= kpi_ids
        assert set(play["drivers"]) <= kpi_ids


def test_sales_kpi_model_does_not_invent_global_targets():
    model = load_yaml(MODEL_PATH)
    policy = " ".join(model["principles"]).lower()
    assert "targets local" in policy
    assert any("do not recommend a target" in rule.lower() for rule in model["agent_contract"]["reasoning_rules"])

    for kpi in model["kpis"]:
        assert "target" not in kpi or not isinstance(kpi.get("target"), (int, float))
        assert "target_policy" in kpi


def test_sales_kpi_human_and_machine_views_exist():
    assert HUMAN_PATH.exists()
    assert MACHINE_PATH.exists()

    human = HUMAN_PATH.read_text(encoding="utf-8")
    machine = MACHINE_PATH.read_text(encoding="utf-8")
    contract = load_yaml(CONTRACT_PATH)

    assert "/labs/enterprise-context/data/sales-process-kpis.json" in human
    assert "site.data.labs.enterprise_context.graphs.sales_process_kpis" in machine
    assert any(item["prefix"] == "KPI.SD." for item in contract["namespaces"])
    assert any(rule["start_with"] == "/labs/enterprise-context/data/sales-process-kpis.json" for rule in contract["routing_rules"])
