import json
from pathlib import Path

import yaml


ROOT = Path("_data/labs/enterprise_context")
CASEBOOK_PATH = ROOT / "graphs" / "sales_diagnostic_casebook.yml"
PROCESS_INDEX_PATH = ROOT / "processes" / "sales_process_atlas" / "index.json"
MECHANISM_INDEX_PATH = ROOT / "mechanisms" / "sales_mechanisms" / "index.json"
SOURCE_ROOT = ROOT / "sources"
PAGE_PATH = Path("labs/enterprise-context/sales-diagnostics/index.html")
ENDPOINT_PATH = Path("labs/enterprise-context/data/sales-diagnostic-casebook.json")


def load_yaml(path: Path):
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def known_source_ids() -> set[str]:
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


def test_sales_diagnostic_casebook_contract():
    graph = load_yaml(CASEBOOK_PATH)
    cases = graph["diagnostic_cases"]

    assert graph["id"] == "GRAPH-SD-SALES-DIAGNOSTIC-CASEBOOK"
    assert graph["type"] == "diagnostic_casebook"
    assert graph["status"] == "draft"
    assert graph["verified"] is False
    assert len(cases) >= 6
    assert len(graph["assessment_drills"]) >= 6

    case_ids = [case["id"] for case in cases]
    drill_ids = [drill["id"] for drill in graph["assessment_drills"]]
    assert len(case_ids) == len(set(case_ids))
    assert len(drill_ids) == len(set(drill_ids))


def test_cases_reference_known_processes_and_mechanisms():
    graph = load_yaml(CASEBOOK_PATH)
    process_index = load_json(PROCESS_INDEX_PATH)
    mechanism_index = load_json(MECHANISM_INDEX_PATH)

    process_codes = {
        code
        for group in process_index["groups"]
        for code in group.get("codes", [])
    }
    mechanism_codes = set(mechanism_index["mechanism_codes"])

    for case in graph["diagnostic_cases"]:
        missing_processes = set(case.get("process_refs", [])) - process_codes
        missing_mechanisms = set(case.get("mechanism_refs", [])) - mechanism_codes
        assert not missing_processes, f"{case['id']} has unknown processes: {sorted(missing_processes)}"
        assert not missing_mechanisms, f"{case['id']} has unknown mechanisms: {sorted(missing_mechanisms)}"


def test_cases_have_ordered_evidence_paths_and_handoffs():
    graph = load_yaml(CASEBOOK_PATH)

    for case in graph["diagnostic_cases"]:
        path = case["diagnostic_path"]
        assert [step["order"] for step in path] == list(range(1, len(path) + 1))
        assert len(path) >= 4
        assert len(case["symptoms"]) >= 2
        assert len(case["failure_modes"]) >= 3
        assert case["business_impact"]
        assert case["boundary"]
        assert case["lead_answer"]

        for step in path:
            assert step["check"]
            assert step["evidence"]
            assert step["decision"]

        handoff = case["handoff"]
        assert handoff["primary_owner"]
        assert len(handoff["evidence_package"]) >= 4
        assert handoff["proof_of_fix"]


def test_agent_contract_is_present_per_case():
    graph = load_yaml(CASEBOOK_PATH)
    top_contract = graph["agent_contract"]

    assert len(top_contract["retrieval_keys"]) >= 5
    assert len(top_contract["reasoning_rules"]) >= 4
    assert len(top_contract["answer_shape"]) >= 5

    for case in graph["diagnostic_cases"]:
        contract = case["agent_case_contract"]
        assert contract["retrieve_when"]
        assert len(contract["do_not_conflate"]) >= 2
        assert len(contract["minimum_output"]) >= 5
        assert len(case["intent_aliases"]) >= 3


def test_down_payment_case_routes_classic_and_advanced_models():
    graph = load_yaml(CASEBOOK_PATH)
    cases = {case["id"]: case for case in graph["diagnostic_cases"]}
    down_payment = cases["SDC.DP.01"]

    assert {"SD.DP.CLASSIC", "SD.DP.ADV"}.issubset(down_payment["process_refs"])
    assert {"SRC-SAP-DP-CLASSIC-BKJ", "SRC-SAP-DP-ADVANCED"}.issubset(down_payment["source_refs"])


def test_related_views_use_registered_sales_routes():
    graph = load_yaml(CASEBOOK_PATH)
    related = {item["title"]: item["url"] for item in graph["related_views"]}

    assert related["Sales Process Atlas"] == "/labs/enterprise-context/sales-processes/"
    assert related["Sales Mechanisms"] == "/labs/enterprise-context/sales-processes/mechanisms/"


def test_all_case_source_refs_resolve():
    graph = load_yaml(CASEBOOK_PATH)
    sources = known_source_ids()

    referenced = {
        source_ref
        for case in graph["diagnostic_cases"]
        for source_ref in case.get("source_refs", [])
    }
    missing = referenced - sources
    assert not missing, f"Unknown Sales diagnostic source refs: {sorted(missing)}"


def test_human_and_machine_views_exist():
    assert PAGE_PATH.exists()
    assert ENDPOINT_PATH.exists()

    page = PAGE_PATH.read_text(encoding="utf-8")
    endpoint = ENDPOINT_PATH.read_text(encoding="utf-8")

    assert "status: draft" in page
    assert "robots: noindex,follow" in page
    assert "Sales Diagnostic Casebook" in page
    assert "/labs/enterprise-context/data/sales-diagnostic-casebook.json" in page
    assert "site.data.labs.enterprise_context.graphs.sales_diagnostic_casebook" in endpoint
    assert "site.data.labs.enterprise_context.processes.sales_process_atlas.index" in endpoint
    assert "site.data.labs.enterprise_context.mechanisms.sales_mechanisms.index" in endpoint
