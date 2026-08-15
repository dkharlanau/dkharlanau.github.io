import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
ARCH_PATH = ROOT / "graphs" / "sales_analytics_architecture.yml"
KPI_PATH = ROOT / "graphs" / "sales_process_kpis.yml"
KPI_SOURCE_PATH = ROOT / "sources" / "sales_analytics_registry.json"
PLATFORM_SOURCE_PATH = ROOT / "sources" / "sales_analytics_platform_registry.json"
ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-process-kpis.json")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_sales_analytics_has_five_distinct_layers():
    model = load_yaml(ARCH_PATH)
    layer_ids = {item["id"] for item in model["layers"]}

    assert model["id"] == "GRAPH-SD-SALES-ANALYTICS-ARCHITECTURE"
    assert layer_ids == {
        "ANA.SD.OPERATIONAL",
        "ANA.SD.SEMANTIC",
        "ANA.SD.MANAGEMENT",
        "ANA.SD.PROCESS_INTELLIGENCE",
        "ANA.SD.AGENT",
    }


def test_sales_analytics_kpi_and_source_refs_resolve():
    architecture = load_yaml(ARCH_PATH)
    kpi_ids = {item["id"] for item in load_yaml(KPI_PATH)["kpis"]}
    source_ids = {
        item["id"]
        for path in (KPI_SOURCE_PATH, PLATFORM_SOURCE_PATH)
        for item in load_json(path)["sources"]
    }

    for layer in architecture["layers"]:
        assert set(layer["kpi_examples"]) <= kpi_ids, layer["id"]
        assert set(layer["source_refs"]) <= source_ids, layer["id"]

    assert set(architecture["source_refs"]) <= source_ids


def test_sales_analytics_selection_rules_choose_real_layers():
    architecture = load_yaml(ARCH_PATH)
    layer_ids = {item["id"] for item in architecture["layers"]}

    for rule in architecture["selection_rules"]:
        assert rule["choose"] in layer_ids
        assert rule["question"]
        assert rule["reason"]


def test_sales_kpi_endpoint_exposes_architecture_and_sources():
    endpoint = ENDPOINT_PATH.read_text(encoding="utf-8")

    assert "site.data.labs.enterprise_context.graphs.sales_analytics_architecture" in endpoint
    assert "site.data.labs.enterprise_context.sources.sales_analytics_platform_registry" in endpoint
