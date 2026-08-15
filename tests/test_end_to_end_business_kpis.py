from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "_data/labs/enterprise_context/graphs/end_to_end_business_kpis.yml"
SOURCE_PATH = ROOT / "_data/labs/enterprise_context/sources/end_to_end_analytics_registry.json"
PAGE_PATH = ROOT / "labs/enterprise-context/end-to-end-analytics/index.html"
ENDPOINT_PATH = ROOT / "labs/enterprise-context/data/end-to-end-business-kpis.json"


def load_graph():
    return yaml.safe_load(GRAPH_PATH.read_text(encoding="utf-8"))


def load_sources():
    return json.loads(SOURCE_PATH.read_text(encoding="utf-8"))


def test_e2e_kpi_contract_is_business_first_and_complete():
    graph = load_graph()
    kpis = graph["kpis"]
    assert graph["id"] == "GRAPH-E2E-BUSINESS-KPIS"
    assert len(kpis) >= 18
    assert len(graph["analytics_lenses"]) >= 6

    ids = [kpi["id"] for kpi in kpis]
    assert len(ids) == len(set(ids))

    required = set(graph["metric_contract"]["required_fields"])
    for kpi in kpis:
        missing = required - set(kpi)
        assert not missing, f"{kpi['id']} missing {sorted(missing)}"
        assert kpi["target_policy"].strip()
        assert kpi["start_event"].strip()
        assert kpi["end_event"].strip()
        assert kpi["population"].strip()
        assert isinstance(kpi["exclusions"], list)
        assert isinstance(kpi["contributing_areas"], list) and kpi["contributing_areas"]


def test_driver_lens_area_and_source_references_resolve():
    graph = load_graph()
    sources = load_sources()
    kpi_ids = {kpi["id"] for kpi in graph["kpis"]}
    area_ids = {area["id"] for area in graph["business_areas"]}
    source_ids = {source["id"] for source in sources["sources"]}

    allowed_domains = {
        "DOM-PROCUREMENT",
        "DOM-MATERIALS-INVENTORY",
        "DOM-SUPPLY-PLANNING",
        "DOM-MANUFACTURING",
        "DOM-WAREHOUSING",
        "DOM-TRANSPORTATION",
    }

    for lens in graph["analytics_lenses"]:
        assert set(lens["kpi_refs"]) <= kpi_ids

    for kpi in graph["kpis"]:
        assert set(kpi["contributing_areas"]) <= area_ids
        assert set(kpi.get("driver_refs", [])) <= kpi_ids
        assert set(kpi.get("domain_refs", [])) <= allowed_domains
        assert set(kpi["source_refs"]) <= source_ids


def test_metric_governance_avoids_fake_standard_targets():
    graph = load_graph()
    text = GRAPH_PATH.read_text(encoding="utf-8").lower()
    assert "industry standard target" not in text
    assert "sap standard target" not in text
    for kpi in graph["kpis"]:
        assert not isinstance(kpi.get("target"), (int, float))


def test_human_and_machine_views_discover_model():
    page = PAGE_PATH.read_text(encoding="utf-8")
    endpoint = ENDPOINT_PATH.read_text(encoding="utf-8")
    assert "site.data.labs.enterprise_context.graphs.end_to_end_business_kpis" in page
    assert "/labs/enterprise-context/data/end-to-end-business-kpis.json" in page
    assert "site.data.labs.enterprise_context.graphs.end_to_end_business_kpis" in endpoint
    assert "site.data.labs.enterprise_context.sources.end_to_end_analytics_registry" in endpoint


def test_core_lead_metrics_and_cross_functional_driver_paths_exist():
    graph = load_graph()
    by_id = {kpi["id"]: kpi for kpi in graph["kpis"]}
    for metric_id in [
        "KPI.E2E.OTIF",
        "KPI.E2E.ORDER_TO_CASH",
        "KPI.E2E.SUPPLIER_OTD",
        "KPI.E2E.MFG_SCHEDULE_ADHERENCE",
        "KPI.E2E.WH_OUTBOUND_CYCLE",
        "KPI.E2E.TRANSPORT_OTD",
        "KPI.E2E.INVENTORY_DAYS",
        "KPI.E2E.PO_TO_AP_CLEAR",
    ]:
        assert metric_id in by_id

    otif = by_id["KPI.E2E.OTIF"]
    assert len(otif["contributing_areas"]) >= 5
    assert len(otif["driver_refs"]) >= 5

    otc = by_id["KPI.E2E.ORDER_TO_CASH"]
    assert "AREA-FI-AR" in otc["contributing_areas"]
    assert "KPI.E2E.BILL_TO_CLEAR" in otc["driver_refs"]
