from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
GRAPH_PATH = ROOT / "_data/labs/enterprise_context/graphs/pricing_operations.yml"
SOURCE_PATH = ROOT / "_data/labs/enterprise_context/sources/pricing_operations.yml"
PAGE_PATH = ROOT / "labs/enterprise-context/pricing/operations/index.html"
GRAPH_ENDPOINT = ROOT / "labs/enterprise-context/data/pricing-operations.json"
SOURCE_ENDPOINT = ROOT / "labs/enterprise-context/data/pricing-operations-sources.json"


def load_yaml(path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def walk_source_refs(value):
    refs = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key == "source_refs" and isinstance(child, list):
                refs.extend(child)
            else:
                refs.extend(walk_source_refs(child))
    elif isinstance(value, list):
        for child in value:
            refs.extend(walk_source_refs(child))
    return refs


def collect_ids(value):
    ids = []
    if isinstance(value, dict):
        if isinstance(value.get("id"), str):
            ids.append(value["id"])
        for child in value.values():
            ids.extend(collect_ids(child))
    elif isinstance(value, list):
        for child in value:
            ids.extend(collect_ids(child))
    return ids


def test_pricing_operations_graph_has_stable_lifecycle():
    graph = load_yaml(GRAPH_PATH)

    assert graph["id"] == "GRAPH-SD-PRICING-OPERATIONS"
    assert graph["memory_path"] == "RULE → OWNER → DATA → LOAD → PROVE → CUTOVER → TRACE → IMPROVE"

    lifecycle = graph["delivery_lifecycle"]
    assert [item["order"] for item in lifecycle] == list(range(1, 8))
    assert [item["key"] for item in lifecycle] == [
        "DISCOVER",
        "DESIGN",
        "BUILD",
        "LOAD",
        "CUTOVER",
        "OPERATE",
        "IMPROVE",
    ]

    ids = collect_ids(graph)
    assert len(ids) == len(set(ids)), "Pricing operations IDs must be unique"


def test_pricing_operations_source_references_resolve():
    graph = load_yaml(GRAPH_PATH)
    source_registry = load_yaml(SOURCE_PATH)
    source_ids = {source["id"] for source in source_registry["sources"]}

    refs = walk_source_refs(graph)
    assert refs, "Pricing operations graph should stay source-tracked"
    assert set(refs) <= source_ids

    required_fields = {
        "id",
        "publisher",
        "source_type",
        "title",
        "url",
        "accessed_at",
        "status",
    }
    for source in source_registry["sources"]:
        assert required_fields <= source.keys()
        assert source["publisher"] == "SAP"
        assert source["source_type"] == "official_help"
        assert source["status"] == "source_verified"


def test_pricing_operations_separates_data_movement_modes():
    graph = load_yaml(GRAPH_PATH)
    modes = {item["mode"]: item for item in graph["data_movement_modes"]}

    assert set(modes) == {"MIGRATION", "MASS_MAINTENANCE", "ONGOING_INTEGRATION"}
    assert "Migration Cockpit" in " ".join(modes["MIGRATION"]["tools_or_patterns"])
    assert "spreadsheet" in " ".join(modes["MASS_MAINTENANCE"]["tools_or_patterns"]).lower()
    assert "API" in " ".join(modes["ONGOING_INTEGRATION"]["tools_or_patterns"])


def test_pricing_operations_cutover_is_reconciled_not_only_loaded():
    graph = load_yaml(GRAPH_PATH)
    steps = graph["migration_cutover"]["steps"]

    assert [item["order"] for item in steps] == list(range(1, 11))
    assert any(item["title"] == "Reconcile population and calculations" for item in steps)
    assert any(item["title"] == "Load approved deltas" for item in steps)
    assert any(item["title"] == "Prove order and billing" for item in steps)


def test_release_specific_volume_guardrails_stay_explicit():
    graph = load_yaml(GRAPH_PATH)
    guardrails = {item["id"]: item for item in graph["performance_guardrails"]}

    cloud_import = guardrails["PRCO-PERF-01"]
    reference_create = guardrails["PRCO-PERF-02"]

    assert cloud_import["release_specific"] is True
    assert cloud_import["documented_limit"] == 100000
    assert "import/export" in cloud_import["unit"]

    assert reference_create["release_specific"] is True
    assert reference_create["documented_limit"] == 10000
    assert "mass creation" in reference_create["unit"]


def test_incident_runbook_starts_with_scope_and_uses_pricing_analysis():
    graph = load_yaml(GRAPH_PATH)
    steps = graph["production_runbook"]["steps"]

    assert steps[0]["id"] == "PRCO-INC-01"
    assert steps[0]["title"] == "Scope the incident before changing data"

    analysis_step = next(item for item in steps if item["id"] == "PRCO-INC-03")
    assert analysis_step["title"] == "Run pricing analysis"
    assert "SRC-SAP-PRC-OPS-PRICING-ANALYSIS" in analysis_step["source_refs"]

    population_step = next(item for item in steps if item["id"] == "PRCO-INC-06")
    assert population_step["title"] == "Find the affected population"


def test_go_live_model_covers_business_data_security_and_support():
    graph = load_yaml(GRAPH_PATH)
    gates = {item["gate"] for item in graph["go_live_checklist"]}

    assert gates == {
        "Commercial sign-off",
        "Configuration sign-off",
        "Data sign-off",
        "Security and approval sign-off",
        "Performance sign-off",
        "Business regression sign-off",
        "Support sign-off",
    }


def test_pricing_operations_human_and_machine_views_exist():
    page = PAGE_PATH.read_text(encoding="utf-8")
    graph_endpoint = GRAPH_ENDPOINT.read_text(encoding="utf-8")
    source_endpoint = SOURCE_ENDPOINT.read_text(encoding="utf-8")

    assert "site.data.labs.enterprise_context.graphs.pricing_operations" in page
    assert "site.data.labs.enterprise_context.sources.pricing_operations" in page
    assert "robots: noindex,follow" in page
    assert "DISCOVER → DESIGN → BUILD → LOAD → CUTOVER → OPERATE → IMPROVE" in page
    assert "/labs/enterprise-context/data/pricing-operations.json" in page
    assert "/labs/enterprise-context/data/pricing-operations-sources.json" in page

    assert "graphs.pricing_operations" in graph_endpoint
    assert "sources.pricing_operations" in source_endpoint
