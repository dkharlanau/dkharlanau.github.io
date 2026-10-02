import json
from pathlib import Path

import yaml

from scripts.generate_enterprise_context_process_contracts import (
    PROCUREMENT_ATLAS,
    PROCUREMENT_P2P_OUTPUT,
    build_p2p_contract,
    load_yaml as load_process_atlas,
    validate_contract,
)
from scripts.generate_enterprise_context_visuals import (
    PROCUREMENT_OUTPUT,
    PROCUREMENT_SOURCE,
    build_procurement_runtime_visual,
    load_yaml,
    validate_visual,
)

ROOT = Path(__file__).resolve().parents[1]


def test_procurement_runtime_visual_is_current():
    expected = build_procurement_runtime_visual(load_yaml(PROCUREMENT_SOURCE))
    actual = json.loads(PROCUREMENT_OUTPUT.read_text(encoding="utf-8"))
    assert actual == expected


def test_procurement_visual_preserves_runtime_source_identity():
    source = yaml.safe_load(PROCUREMENT_SOURCE.read_text(encoding="utf-8"))
    visual = json.loads(PROCUREMENT_OUTPUT.read_text(encoding="utf-8"))["visual"]

    source_ids = [item["id"] for item in source["runtime_pipeline"]]
    projected_ids = [
        next(tag.removeprefix("source:") for tag in node["tags"] if tag.startswith("source:"))
        for node in visual["nodes"]
    ]

    assert projected_ids == source_ids
    assert [node["label"] for node in visual["nodes"]] == [
        item["title"] for item in source["runtime_pipeline"]
    ]


def test_procurement_visual_has_resolved_semantic_contract():
    payload = json.loads(PROCUREMENT_OUTPUT.read_text(encoding="utf-8"))
    validate_visual(payload)

    visual = payload["visual"]
    node_ids = [node["id"] for node in visual["nodes"]]
    assert len(node_ids) == len(set(node_ids)) == 11
    assert visual["kind"] == "handoff"
    assert {group["id"] for group in visual["groups"]} == {
        "demand",
        "purchasing",
        "execution",
        "finance",
    }
    assert [(edge["from"], edge["to"]) for edge in visual["edges"]] == list(
        zip(node_ids, node_ids[1:])
    )
    assert not any(key in node for node in visual["nodes"] for key in ("x", "y", "color"))


def test_procurement_page_renders_shared_semantic_visual_and_practice_handoffs():
    page = (ROOT / "labs/enterprise-context/procurement/index.html").read_text(encoding="utf-8")
    assert "site.data.labs.enterprise_context.visuals.procurement_runtime.visual" in page
    assert "{% include labs/semantic-lane-flow.html model=procurement_visual %}" in page
    assert "/labs/enterprise-context/data/procurement-runtime-visual.json" in page
    assert "/labs/interview-readiness/diagnostic-lab/?case=po-ack" in page
    assert "/labs/assessment/practice-engine/" in page


def test_procurement_visual_machine_endpoint_reuses_same_data_source():
    endpoint = (
        ROOT / "labs/enterprise-context/data/procurement-runtime-visual.json"
    ).read_text(encoding="utf-8")
    assert "site.data.labs.enterprise_context.visuals.procurement_runtime | jsonify" in endpoint


def test_diagnostic_lab_supports_stable_case_deep_links():
    page = (ROOT / "labs/interview-readiness/diagnostic-lab/index.md").read_text(
        encoding="utf-8"
    )
    assert "new URLSearchParams(window.location.search).get('case')" in page
    assert "cases.findIndex(item => item.id === requestedCase)" in page
    assert "url.searchParams.set('case', cases[index].id)" in page
    assert "window.history.replaceState" in page


def test_procurement_p2p_process_contract_is_current():
    expected = build_p2p_contract(load_process_atlas(PROCUREMENT_ATLAS))
    actual = json.loads(PROCUREMENT_P2P_OUTPUT.read_text(encoding="utf-8"))
    assert actual == expected


def test_procurement_p2p_contract_has_resolved_process_references():
    contract = json.loads(PROCUREMENT_P2P_OUTPUT.read_text(encoding="utf-8"))
    validate_contract(contract)

    assert contract["version"] == "0.2"
    assert contract["process"]["id"] == "sap_procure_to_pay"
    assert contract["extensions"]["dkharlanau"]["source_process_code"] == "MM.P2P"

    step_ids = [step["id"] for step in contract["steps"]]
    assert step_ids == [
        "demand",
        "purchase_requisition",
        "source_determination",
        "purchase_order",
        "goods_receipt",
        "supplier_invoice",
        "payment",
    ]
    assert contract["process"]["start"] == step_ids[0]
    assert [
        transition["to"]
        for step in contract["steps"]
        for transition in step.get("transitions", [])
    ] == step_ids[1:]


def test_procurement_page_links_process_as_code_projection():
    page = (ROOT / "labs/enterprise-context/procurement/index.html").read_text(encoding="utf-8")
    assert "/labs/enterprise-context/data/procurement-p2p.process.json" in page
    assert "Process as Code v0.2 projection" in page
