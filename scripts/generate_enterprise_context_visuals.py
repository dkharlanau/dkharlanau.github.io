#!/usr/bin/env python3
"""Generate Visual Workbench-compatible Enterprise Context visual projections."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROCUREMENT_SOURCE = ROOT / "_data" / "labs" / "enterprise_context" / "graphs" / "procurement.yml"
PROCUREMENT_OUTPUT = ROOT / "_data" / "labs" / "enterprise_context" / "visuals" / "procurement_runtime.json"

GROUPS = [
    {
        "id": "demand",
        "label": "Business demand",
        "order": 1,
        "description": "Planning or requester context that creates the need to procure.",
    },
    {
        "id": "purchasing",
        "label": "Purchasing",
        "order": 2,
        "description": "Item behavior, source, commercial terms, approval and supplier communication.",
    },
    {
        "id": "execution",
        "label": "Logistics execution",
        "order": 3,
        "description": "Goods receipt or accepted service execution.",
    },
    {
        "id": "finance",
        "label": "Finance",
        "order": 4,
        "description": "Account assignment, invoice verification and settlement.",
    },
]

PRESENTATION: dict[str, dict[str, str]] = {
    "PUR-RUNTIME-DEMAND": {
        "id": "demand",
        "group": "demand",
        "type": "step",
        "owner": "Planning · Requester",
        "subtitle": "Business need",
    },
    "PUR-RUNTIME-ITEM-CONTROL": {
        "id": "item-type",
        "group": "purchasing",
        "type": "decision",
        "owner": "Purchasing",
        "subtitle": "Stock · consumption · service",
    },
    "PUR-RUNTIME-SOURCE": {
        "id": "source",
        "group": "purchasing",
        "type": "decision",
        "owner": "Purchasing",
        "subtitle": "Valid source of supply",
    },
    "PUR-RUNTIME-COMMERCIAL": {
        "id": "price",
        "group": "purchasing",
        "type": "decision",
        "owner": "Purchasing",
        "subtitle": "Price + conditions",
    },
    "PUR-RUNTIME-ACCOUNT": {
        "id": "account",
        "group": "finance",
        "type": "decision",
        "owner": "MM · FI/CO",
        "subtitle": "Stock or consumption value",
    },
    "PUR-RUNTIME-APPROVE": {
        "id": "approve",
        "group": "purchasing",
        "type": "checkpoint",
        "owner": "Workflow · Approver",
        "subtitle": "Release control",
    },
    "PUR-RUNTIME-ORDER": {
        "id": "order",
        "group": "purchasing",
        "type": "checkpoint",
        "owner": "Purchasing",
        "subtitle": "Purchase order",
    },
    "PUR-RUNTIME-OUTPUT": {
        "id": "output",
        "group": "purchasing",
        "type": "data",
        "owner": "Purchasing · Integration",
        "subtitle": "Supplier communication",
    },
    "PUR-RUNTIME-RECEIVE": {
        "id": "receive",
        "group": "execution",
        "type": "checkpoint",
        "owner": "Inventory · Service",
        "subtitle": "Goods or service receipt",
    },
    "PUR-RUNTIME-INVOICE": {
        "id": "invoice",
        "group": "finance",
        "type": "checkpoint",
        "owner": "Invoice Verification",
        "subtitle": "Supplier invoice",
    },
    "PUR-RUNTIME-SETTLE": {
        "id": "settle",
        "group": "finance",
        "type": "outcome",
        "owner": "FI / AP",
        "subtitle": "GR/IR + liability",
        "status": "success",
    },
}

EDGE_LABELS = [
    "Requirement",
    "Item behavior",
    "Source decision",
    "Commercial terms",
    "Accounting context",
    "Approved",
    "Released PO",
    "Supplier execution",
    "Receipt history",
    "Financial close",
]

NODE_TYPES = {"step", "system", "data", "role", "decision", "checkpoint", "milestone", "outcome", "risk", "note"}
EDGE_TYPES = {"flow", "data", "dependency", "relation", "control", "exception"}
KINDS = {"process", "plan", "data-flow", "relationship", "system-flow", "checkpoint-flow", "roadmap", "timeline", "handoff", "dependency-map"}
STATUSES = {"neutral", "success", "warning", "danger", "muted"}


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"{path}: expected a YAML object")
    return payload


def build_procurement_runtime_visual(source: dict[str, Any]) -> dict[str, Any]:
    pipeline = source.get("runtime_pipeline")
    if not isinstance(pipeline, list) or not pipeline:
        raise RuntimeError("procurement.yml: runtime_pipeline is missing")

    source_ids = [str(item.get("id") or "") for item in pipeline if isinstance(item, dict)]
    expected_ids = list(PRESENTATION)
    if source_ids != expected_ids:
        raise RuntimeError(
            "procurement.yml: runtime_pipeline IDs/order changed; update the visual adapter intentionally. "
            f"Expected {expected_ids}, got {source_ids}"
        )

    nodes: list[dict[str, Any]] = []
    for item in pipeline:
        source_id = str(item["id"])
        meta = PRESENTATION[source_id]
        node = {
            "id": meta["id"],
            "label": str(item["title"]),
            "type": meta["type"],
            "subtitle": meta["subtitle"],
            "description": str(item["question"]),
            "owner": meta["owner"],
            "group": meta["group"],
            "status": meta.get("status", "neutral"),
            "tags": ["procurement-runtime", f"source:{source_id}"],
        }
        nodes.append(node)

    edges = [
        {
            "from": nodes[index]["id"],
            "to": nodes[index + 1]["id"],
            "label": EDGE_LABELS[index],
            "type": "data" if nodes[index]["id"] == "output" else "flow",
        }
        for index in range(len(nodes) - 1)
    ]

    result = {
        "visual": {
            "version": 1,
            "title": "Procure-to-Pay runtime decisions",
            "description": (
                "A semantic handoff view derived from the canonical procurement runtime pipeline. "
                "It shows where demand, purchasing, logistics execution and finance own the next decision."
            ),
            "kind": "handoff",
            "direction": "right",
            "theme": "paper",
            "density": "balanced",
            "groups": GROUPS,
            "nodes": nodes,
            "edges": edges,
            "views": [
                {
                    "id": "executive",
                    "title": "Procurement business milestones",
                    "focus": "executive",
                    "kind": "process",
                },
                {
                    "id": "controls",
                    "title": "Procurement decisions and checkpoints",
                    "focus": "controls",
                    "kind": "checkpoint-flow",
                },
                {
                    "id": "purchasing-execution",
                    "title": "Purchasing to execution handoff",
                    "focus": "flow",
                    "kind": "handoff",
                    "includeGroups": ["purchasing", "execution"],
                },
                {
                    "id": "finance",
                    "title": "Procurement financial boundary",
                    "focus": "flow",
                    "kind": "handoff",
                    "includeGroups": ["finance"],
                },
            ],
        }
    }
    validate_visual(result)
    return result


def validate_visual(payload: dict[str, Any]) -> None:
    visual = payload.get("visual")
    if not isinstance(visual, dict):
        raise RuntimeError("visual projection: missing visual object")
    if visual.get("kind") not in KINDS:
        raise RuntimeError(f"visual projection: unsupported kind {visual.get('kind')!r}")

    groups = visual.get("groups") or []
    group_ids = [item.get("id") for item in groups if isinstance(item, dict)]
    if len(group_ids) != len(set(group_ids)):
        raise RuntimeError("visual projection: duplicate group IDs")

    nodes = visual.get("nodes") or []
    node_ids = [item.get("id") for item in nodes if isinstance(item, dict)]
    if not node_ids or len(node_ids) != len(set(node_ids)):
        raise RuntimeError("visual projection: node IDs must be present and unique")

    for node in nodes:
        if node.get("type") not in NODE_TYPES:
            raise RuntimeError(f"visual projection: unsupported node type {node.get('type')!r}")
        if node.get("status", "neutral") not in STATUSES:
            raise RuntimeError(f"visual projection: unsupported node status {node.get('status')!r}")
        if node.get("group") not in group_ids:
            raise RuntimeError(f"visual projection: unresolved group {node.get('group')!r}")

    node_id_set = set(node_ids)
    for edge in visual.get("edges") or []:
        if edge.get("type", "flow") not in EDGE_TYPES:
            raise RuntimeError(f"visual projection: unsupported edge type {edge.get('type')!r}")
        if edge.get("from") not in node_id_set or edge.get("to") not in node_id_set:
            raise RuntimeError(f"visual projection: unresolved edge {edge!r}")

    for view in visual.get("views") or []:
        if view.get("kind", visual.get("kind")) not in KINDS:
            raise RuntimeError(f"visual projection: unsupported view kind {view.get('kind')!r}")
        for group_id in view.get("includeGroups") or []:
            if group_id not in group_ids:
                raise RuntimeError(f"visual projection: unresolved view group {group_id!r}")


def render(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if committed output is stale")
    args = parser.parse_args()

    payload = build_procurement_runtime_visual(load_yaml(PROCUREMENT_SOURCE))
    expected = render(payload)

    if args.check:
        actual = PROCUREMENT_OUTPUT.read_text(encoding="utf-8") if PROCUREMENT_OUTPUT.exists() else ""
        if actual != expected:
            raise SystemExit(f"{PROCUREMENT_OUTPUT.relative_to(ROOT)} is stale; run {Path(__file__).name}")
        print(f"OK: {PROCUREMENT_OUTPUT.relative_to(ROOT)}")
        return 0

    PROCUREMENT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PROCUREMENT_OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Wrote {PROCUREMENT_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
