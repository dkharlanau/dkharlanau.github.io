import json
from pathlib import Path

import yaml

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
