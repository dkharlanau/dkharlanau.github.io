from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "_data/labs/enterprise_context/graphs/pricing_scenarios.yml"
SOURCES_PATH = ROOT / "_data/labs/enterprise_context/sources/pricing_scenarios.yml"
PAGE_PATH = ROOT / "labs/enterprise-context/pricing/scenarios/index.html"
GRAPH_ENDPOINT = ROOT / "labs/enterprise-context/data/pricing-scenarios.json"
SOURCE_ENDPOINT = ROOT / "labs/enterprise-context/data/pricing-scenario-sources.json"


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def collect_source_refs(value):
    refs = set()
    if isinstance(value, dict):
        for key, item in value.items():
            if key == "source_refs" and isinstance(item, list):
                refs.update(item)
            else:
                refs.update(collect_source_refs(item))
    elif isinstance(value, list):
        for item in value:
            refs.update(collect_source_refs(item))
    return refs


def test_graph_and_source_registry_exist():
    assert GRAPH_PATH.exists()
    assert SOURCES_PATH.exists()
    assert PAGE_PATH.exists()
    assert GRAPH_ENDPOINT.exists()
    assert SOURCE_ENDPOINT.exists()


def test_all_source_refs_resolve():
    graph = load_yaml(GRAPH_PATH)
    sources = load_yaml(SOURCES_PATH)
    known = {item["id"] for item in sources["sources"]}
    refs = collect_source_refs(graph)
    assert refs
    assert refs <= known


def test_scenario_ids_are_unique_and_ordered():
    graph = load_yaml(GRAPH_PATH)
    scenarios = graph["scenario_families"]
    ids = [item["id"] for item in scenarios]
    orders = [item["order"] for item in scenarios]
    assert len(ids) == len(set(ids))
    assert orders == list(range(1, len(scenarios) + 1))
    assert len(scenarios) >= 9


def test_core_advanced_pricing_scenarios_are_present():
    graph = load_yaml(GRAPH_PATH)
    ids = {item["id"] for item in graph["scenario_families"]}
    required = {
        "PRC-SCN-PROMOTION",
        "PRC-SCN-HIERARCHY",
        "PRC-SCN-VARIANT",
        "PRC-SCN-INTERCOMPANY",
        "PRC-SCN-BILLING-REPRICE",
        "PRC-SCN-RETRO",
        "PRC-SCN-CCM",
        "PRC-SCN-TAX",
        "PRC-SCN-EXTERNAL",
    }
    assert required <= ids


def test_commercial_clocks_do_not_collapse_lifecycle():
    graph = load_yaml(GRAPH_PATH)
    stages = {item["stage"] for item in graph["commercial_clock"]}
    assert "Before / at sales order" in stages
    assert "At billing" in stages
    assert "After billing" in stages
    assert "Period / accumulated volume" in stages
    assert "External channel" in stages


def test_billing_repricing_and_retroactive_billing_are_distinct():
    graph = load_yaml(GRAPH_PATH)
    scenarios = {item["id"]: item for item in graph["scenario_families"]}
    billing = scenarios["PRC-SCN-BILLING-REPRICE"]
    retro = scenarios["PRC-SCN-RETRO"]
    assert "copying control" in billing["boundary"].lower()
    assert "existing billing documents" in retro["boundary"].lower()
    boundary_text = " ".join(item["rule"] for item in graph["boundary_rules"])
    assert "retroactive billing" in boundary_text.lower()
    assert "invoice creation" in boundary_text.lower()


def test_intercompany_keeps_customer_and_affiliate_values_separate():
    graph = load_yaml(GRAPH_PATH)
    intercompany = next(item for item in graph["scenario_families"] if item["id"] == "PRC-SCN-INTERCOMPANY")
    text = " ".join(intercompany["classic_shape"] + intercompany["design_questions"])
    assert "external customer" in text.lower()
    assert "intercompany" in text.lower()
    assert "internal" in text.lower()


def test_ccm_is_volume_and_settlement_not_order_discount():
    graph = load_yaml(GRAPH_PATH)
    ccm = next(item for item in graph["scenario_families"] if item["id"] == "PRC-SCN-CCM")
    text = " ".join(ccm["runtime_path"] + ccm["design_questions"] + ccm["failure_modes"])
    assert "business volume" in text.lower()
    assert "settlement" in text.lower()
    assert ccm["cross_link"] == "/labs/enterprise-context/condition-contract-management/sales/"


def test_variant_scenario_connects_configuration_to_pricing_key():
    graph = load_yaml(GRAPH_PATH)
    variant = next(item for item in graph["scenario_families"] if item["id"] == "PRC-SCN-VARIANT")
    text = " ".join(variant["runtime_path"] + variant["configuration_shape"])
    assert "variant-condition key" in text.lower()
    assert "pricing" in text.lower()


def test_synthetic_cases_cover_cross_mechanism_reasoning():
    graph = load_yaml(GRAPH_PATH)
    ids = {item["id"] for item in graph["synthetic_cases"]}
    required = {
        "PRC-CASE-RETAIL-CAMPAIGN",
        "PRC-CASE-CONFIG-INTCO",
        "PRC-CASE-RETRO-METAL",
        "PRC-CASE-ANNUAL-REBATE",
        "PRC-CASE-CHANNEL-PARITY",
    }
    assert required <= ids


def test_assessment_drills_cover_lead_boundaries():
    graph = load_yaml(GRAPH_PATH)
    drills = graph["assessment_drills"]
    assert len(drills) >= 7
    all_text = " ".join(
        item["prompt"] + " " + " ".join(item["expected_reasoning"])
        for item in drills
    ).lower()
    for term in ["hierarchy", "variant", "retroactive", "condition contract", "intercompany", "copying control", "portal"]:
        assert term in all_text


def test_page_exposes_machine_endpoints_and_related_pricing_views():
    page = PAGE_PATH.read_text(encoding="utf-8")
    assert "/labs/enterprise-context/data/pricing-scenarios.json" in page
    assert "/labs/enterprise-context/data/pricing-scenario-sources.json" in page
    assert "/labs/enterprise-context/pricing/anatomy/" in page
    assert "/labs/enterprise-context/pricing/configuration/" in page
    assert "/labs/enterprise-context/condition-contract-management/sales/" not in page or "scenario.cross_link" in page
