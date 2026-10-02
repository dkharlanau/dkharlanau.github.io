#!/usr/bin/env python3
"""Generate Process as Code contracts from canonical Enterprise Context process atlases."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
PROCUREMENT_ATLAS = ROOT / "_data" / "labs" / "enterprise_context" / "processes" / "procurement_process_atlas.yml"
PROCUREMENT_P2P_OUTPUT = ROOT / "labs" / "enterprise-context" / "data" / "procurement-p2p.process.json"

EXPECTED_FLOW = [
    "Demand / MRP",
    "Purchase Requisition",
    "Source",
    "Purchase Order",
    "Goods Receipt",
    "Supplier Invoice",
    "FI Payment",
]

STEP_META = {
    "Demand / MRP": {
        "id": "demand",
        "type": "event",
        "actor": "requester",
        "name": "Demand requires external procurement",
    },
    "Purchase Requisition": {
        "id": "purchase_requisition",
        "type": "user_task",
        "actor": "requester",
        "name": "Create purchase requisition",
        "objects": ["purchase_requisition"],
    },
    "Source": {
        "id": "source_determination",
        "type": "decision",
        "actor": "buyer",
        "name": "Determine source of supply",
        "controls": ["source_determination"],
    },
    "Purchase Order": {
        "id": "purchase_order",
        "type": "user_task",
        "actor": "buyer",
        "name": "Create and approve purchase order",
        "objects": ["purchase_order"],
        "controls": [
            "document_type",
            "item_category",
            "account_assignment",
            "purchasing_conditions",
            "approval",
        ],
    },
    "Goods Receipt": {
        "id": "goods_receipt",
        "type": "user_task",
        "actor": "goods_receiver",
        "name": "Post goods receipt",
        "objects": ["material_document"],
    },
    "Supplier Invoice": {
        "id": "supplier_invoice",
        "type": "user_task",
        "actor": "accounts_payable",
        "name": "Verify supplier invoice",
        "objects": ["supplier_invoice", "accounting_document"],
        "controls": ["gr_ir_settings"],
    },
    "FI Payment": {
        "id": "payment",
        "type": "end",
        "actor": "accounts_payable",
        "name": "Settle supplier liability",
        "objects": ["accounting_document"],
    },
}


def snake(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def load_yaml(path: Path) -> dict[str, Any]:
    payload = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"{path}: expected a YAML object")
    return payload


def find_process(atlas: dict[str, Any], code: str) -> dict[str, Any]:
    for group in atlas.get("groups") or []:
        if not isinstance(group, dict):
            continue
        for process in group.get("processes") or []:
            if isinstance(process, dict) and process.get("code") == code:
                return process
    raise RuntimeError(f"procurement process atlas: process {code!r} not found")


def build_p2p_contract(atlas: dict[str, Any]) -> dict[str, Any]:
    process = find_process(atlas, "MM.P2P")
    flow = process.get("flow")
    if flow != EXPECTED_FLOW:
        raise RuntimeError(
            "MM.P2P flow changed; update the Process as Code adapter intentionally. "
            f"Expected {EXPECTED_FLOW}, got {flow}"
        )

    controls = [
        {"id": snake(name), "name": name}
        for name in process.get("key_controls") or []
    ]
    control_ids = {item["id"] for item in controls}
    required_controls = {
        control_id
        for meta in STEP_META.values()
        for control_id in meta.get("controls", [])
    }
    if not required_controls.issubset(control_ids):
        missing = sorted(required_controls - control_ids)
        raise RuntimeError(f"MM.P2P key controls no longer cover adapter controls: {missing}")

    canonical_objects = {
        snake(name): name for name in process.get("main_documents") or []
    }
    object_aliases = {
        "purchase_requisition": "Purchase Requisition",
        "purchase_order": "Purchase Order",
        "material_document": "Material Document",
        "supplier_invoice": "Supplier Invoice",
        "accounting_document": "Accounting Document",
    }
    missing_objects = [
        name for object_id, name in object_aliases.items()
        if canonical_objects.get(object_id) != name
    ]
    if missing_objects:
        raise RuntimeError(f"MM.P2P main documents changed; missing expected objects: {missing_objects}")

    steps: list[dict[str, Any]] = []
    for index, flow_name in enumerate(flow):
        meta = STEP_META[flow_name]
        step = {
            "id": meta["id"],
            "name": meta["name"],
            "type": meta["type"],
            "actor": meta["actor"],
            "system": "sap_s4hana",
        }
        if meta.get("objects"):
            step["objects"] = meta["objects"]
        if meta.get("controls"):
            step["controls"] = meta["controls"]
        if index < len(flow) - 1:
            next_id = STEP_META[flow[index + 1]]["id"]
            step["transitions"] = [{"to": next_id}]
        steps.append(step)

    contract = {
        "version": "0.2",
        "process": {
            "id": "sap_procure_to_pay",
            "name": process["title"],
            "description": process["business_intent"],
            "owner": "p2p_process_owner",
            "start": "demand",
            "trigger": "A material or service requirement needs external procurement.",
            "outcome": "Supplier liability is settled after controlled purchasing, receipt, and invoice processing.",
            "tags": ["sap", "s4hana", "mm", "fi", "p2p", "enterprise-context"],
        },
        "roles": [
            {"id": "requester", "name": "Requester / Planner"},
            {"id": "buyer", "name": "Buyer"},
            {"id": "goods_receiver", "name": "Goods Receiver"},
            {"id": "accounts_payable", "name": "Accounts Payable"},
            {"id": "p2p_process_owner", "name": "P2P Process Owner"},
        ],
        "systems": [{"id": "sap_s4hana", "name": "SAP S/4HANA"}],
        "objects": [
            {"id": object_id, "name": name}
            for object_id, name in object_aliases.items()
        ],
        "controls": controls,
        "steps": steps,
        "extensions": {
            "sap": {
                "process_area": "MM-FI",
                "applications": ["SAP S/4HANA"],
            },
            "dkharlanau": {
                "source_process_code": process["code"],
                "source_atlas": "_data/labs/enterprise_context/processes/procurement_process_atlas.yml",
                "memory_hook": process["memory_hook"],
                "lead_questions": process["lead_questions"],
                "source_refs": process["source_refs"],
            },
        },
    }
    validate_contract(contract)
    return contract


def validate_contract(contract: dict[str, Any]) -> None:
    if contract.get("version") != "0.2":
        raise RuntimeError("Process as Code projection must use contract v0.2")

    process = contract.get("process")
    steps = contract.get("steps")
    if not isinstance(process, dict) or not process.get("id"):
        raise RuntimeError("Process as Code projection: missing process identity")
    if not isinstance(steps, list) or not steps:
        raise RuntimeError("Process as Code projection: missing steps")

    role_ids = {item["id"] for item in contract.get("roles") or []}
    system_ids = {item["id"] for item in contract.get("systems") or []}
    object_ids = {item["id"] for item in contract.get("objects") or []}
    control_ids = {item["id"] for item in contract.get("controls") or []}
    step_ids = [item["id"] for item in steps]

    if len(step_ids) != len(set(step_ids)):
        raise RuntimeError("Process as Code projection: duplicate step IDs")
    if process.get("start") not in set(step_ids):
        raise RuntimeError("Process as Code projection: start step does not resolve")

    step_id_set = set(step_ids)
    for step in steps:
        if step.get("actor") not in role_ids:
            raise RuntimeError(f"Process as Code projection: unresolved actor {step.get('actor')!r}")
        if step.get("system") not in system_ids:
            raise RuntimeError(f"Process as Code projection: unresolved system {step.get('system')!r}")
        for object_id in step.get("objects") or []:
            if object_id not in object_ids:
                raise RuntimeError(f"Process as Code projection: unresolved object {object_id!r}")
        for control_id in step.get("controls") or []:
            if control_id not in control_ids:
                raise RuntimeError(f"Process as Code projection: unresolved control {control_id!r}")
        for transition in step.get("transitions") or []:
            if transition.get("to") not in step_id_set:
                raise RuntimeError(f"Process as Code projection: unresolved transition {transition!r}")


def render(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if committed output is stale")
    args = parser.parse_args()

    contract = build_p2p_contract(load_yaml(PROCUREMENT_ATLAS))
    expected = render(contract)

    if args.check:
        actual = PROCUREMENT_P2P_OUTPUT.read_text(encoding="utf-8") if PROCUREMENT_P2P_OUTPUT.exists() else ""
        if actual != expected:
            raise SystemExit(
                f"{PROCUREMENT_P2P_OUTPUT.relative_to(ROOT)} is stale; run {Path(__file__).name}"
            )
        print(f"OK: {PROCUREMENT_P2P_OUTPUT.relative_to(ROOT)}")
        return 0

    PROCUREMENT_P2P_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PROCUREMENT_P2P_OUTPUT.write_text(expected, encoding="utf-8")
    print(f"Wrote {PROCUREMENT_P2P_OUTPUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
