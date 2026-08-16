#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing patch anchor: {label}")
    return text.replace(old, new, 1)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


# Quality Management: quality authority before stock correction.
qm_path = ROOT / "labs" / "enterprise-context" / "quality-management" / "index.html"
qm = qm_path.read_text(encoding="utf-8")
qm_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>\n    <p><strong>Working rule:</strong> first identify the quality trigger and inspection context. Then separate evidence, business decision, stock consequence, corrective action, and customer proof. Moving stock manually can hide the real quality-control failure.</p>\n    <a href="/labs/enterprise-context/data/quality-management-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
qm_model = qm_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Decision authority model</p><h2>Quality decides disposition. Logistics consumes the decision.</h2><p>This is an authored reasoning frame. It keeps the inspection trigger, recorded evidence, usage decision, and downstream stock or process effect separate.</p></header>\n    <div class="ecg-control-stack">\n      <article><span>TRIGGER</span><h3>Inspection context</h3><p>Why does the inspection exist, and which business event or inspection setup created it?</p><strong>Proof: the inspection lot and context match the intended process.</strong></article>\n      <article><span>EVIDENCE</span><h3>Results and defects</h3><p>What was measured, recorded, accepted, rejected, or left incomplete?</p><strong>Proof: quality evidence supports the next decision.</strong></article>\n      <article><span>DECIDE</span><h3>Usage decision</h3><p>What quality disposition was made, by whom, and with which follow-up action?</p><strong>Proof: decision status and follow-up intent are explicit.</strong></article>\n      <article><span>CONSUME</span><h3>Logistics consequence</h3><p>What should happen to stock, procurement, production, warehouse, delivery, or customer evidence?</p><strong>Proof: downstream logistics state matches the quality decision.</strong></article>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> moving stock is not a substitute for a missing or wrong quality decision. First prove which authority layer is wrong.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms usage-decision behavior and stock posting for stock-relevant inspection lots. The authority model above is an authored diagnostic frame; wider trigger, specification, notification, and integration behavior still requires page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "Quality decides disposition" not in qm:
    qm = replace_once(qm, qm_boundary, qm_model, "QM authority model")
qm_path.write_text(qm, encoding="utf-8")


# EWM: warehouse execution ownership and enterprise reconciliation.
ewm_path = ROOT / "labs" / "enterprise-context" / "ewm" / "index.html"
ewm = ewm_path.read_text(encoding="utf-8")
ewm = ewm.replace("last_modified_at: 2026-08-15", "last_modified_at: 2026-08-16", 1)
ewm_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">warehouse</span>\n    <p><strong>Working thesis:</strong> {{ graph.thesis }}</p>\n    <p><strong>Boundary:</strong> EWM owns detailed warehouse position and execution. ERP Inventory Management remains the enterprise inventory and accounting context. The useful question is not “Which transaction?” but “Which system and object owns the next decision?”</p>\n  </section>\n'''
ewm_model = ewm_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Execution ownership model</p><h2>Do not confuse the warehouse request with the work that executes it.</h2><p>This assessment frame separates business demand, warehouse tasks, work packages, execution confirmation, and the enterprise inventory handoff.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>1. Demand and request</h4><ul><li>Which upstream process created the warehouse demand?</li><li>Which warehouse request represents that demand in EWM?</li><li>Is the demand itself correct before warehouse execution starts?</li></ul></div>\n      <div><h4>2. Task and work package</h4><ul><li>Which warehouse task expresses the stock movement or change?</li><li>How was the task grouped into a warehouse order?</li><li>Which determination rule created the unexpected bin, queue, or work package?</li></ul></div>\n      <div><h4>3. Confirm and reconcile</h4><ul><li>What physical work was confirmed and what stock state changed?</li><li>Did EWM and ERP/Inventory Management reach compatible end states?</li><li>Can the business process prove completion beyond the warehouse monitor?</li></ul></div>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> “no warehouse task”, “wrong bin”, and “ERP stock mismatch” are not one problem. They sit at different ownership layers.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms warehouse-task semantics, warehouse-order grouping, and wave-to-task/order behavior. The ownership model above is an authored diagnostic frame; deployment, production, QM, automation, and cross-system completion still require page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "Do not confuse the warehouse request" not in ewm:
    ewm = replace_once(ewm, ewm_boundary, ewm_model, "EWM ownership model")
ewm_path.write_text(ewm, encoding="utf-8")


# MDG: governance completion is more than approval.
mdg_path = ROOT / "labs" / "enterprise-context" / "mdg" / "index.md"
mdg = mdg_path.read_text(encoding="utf-8")
mdg = mdg.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)
mdg_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>\n    <p><strong>Data Book:</strong> {{ topic.memory_model.data_book }}</p>\n    <p><strong>Memory line:</strong> {{ topic.memory_model.phrase }}.</p>\n    <a href="/labs/enterprise-context/mdg/scenario/">Run one object from request to business proof <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>\n  </section>\n'''
mdg_model = mdg_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Governance completion model</p><h2>Approved data is not yet business proof.</h2><p>I separate governance completion into four checkpoints. The model is intentionally broader than one MDG workflow because the business value appears only when consumers use the governed object correctly.</p></header>\n    <div class="ecg-control-stack">\n      <article><span>REQUEST</span><h3>Change is governed</h3><p>The reason, object, ownership, required attributes, validations, and approvals are explicit.</p><strong>Proof: the request follows the intended governance process.</strong></article>\n      <article><span>ACTIVE</span><h3>Record is activated</h3><p>The approved master data becomes the authoritative active record for the chosen governance model.</p><strong>Proof: active data matches the approved decision.</strong></article>\n      <article><span>REPLICATE</span><h3>Consumers receive it</h3><p>Replication, mapping, filtering, interface ownership, and error handling deliver the expected object version.</p><strong>Proof: target systems reconcile to the governed source.</strong></article>\n      <article><span>USE</span><h3>Business process proves it</h3><p>Sales, procurement, planning, warehouse, transport, or finance can use the object without local repair.</p><strong>Proof: the target process consumes the intended data and outcome.</strong></article>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> “workflow approved” proves a governance step. It does not prove replication or business usability.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms the 2025 FPS01 classic/cloud-ready mode boundary and the effects of switching cloud-ready mode. The four-checkpoint governance model is an authored reasoning frame; domain, replication, extension, and consumer-process details still require page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "Approved data is not yet business proof" not in mdg:
    mdg = replace_once(mdg, mdg_boundary, mdg_model, "MDG completion model")
mdg_path.write_text(mdg, encoding="utf-8")


# FI/CO bridge: posting, clearing/settlement, reconciliation are distinct checkpoints.
fin_path = ROOT / "labs" / "enterprise-context" / "finance-logistics" / "index.html"
fin = fin_path.read_text(encoding="utf-8")
fin_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>\n    <p><strong>Working rule:</strong> do not start with debit and credit memorization. Start with the business event, expected value change, account logic, cost or revenue object, and the evidence that connects Finance back to Logistics.</p>\n    <a href="/labs/enterprise-context/data/finance-logistics-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
fin_model = fin_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Financial completion model</p><h2>A posting can be correct and the process can still be open.</h2><p>This diagnostic frame separates event posting, matching or settlement, and end-to-end reconciliation. It prevents Finance from becoming a repair screen for an upstream logistics defect.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>1. Event and posting</h4><ul><li>Which logistics event changed quantity, value, revenue, cost, or liability?</li><li>Did the expected value, account, and cost/revenue object result?</li><li>If not, find whether the wrong input came from Logistics or account/control logic.</li></ul></div>\n      <div><h4>2. Match or settle</h4><ul><li>Which later event should clear, settle, or match the open state?</li><li>For procurement, compare GR and invoice receipt before calling GR/IR wrong.</li><li>For production, separate order completion from CO settlement.</li></ul></div>\n      <div><h4>3. Reconcile</h4><ul><li>Does the financial state match the operational process state?</li><li>Is an open balance genuinely wrong, or is a later event still expected?</li><li>Close the issue with source-document and journal evidence, not a manual journal alone.</li></ul></div>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> “posted” answers whether an accounting event exists. It does not answer whether the process has cleared, settled, or reconciled.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms GR/IR separation between goods receipt and invoice receipt, and production-order settlement through settlement rules. The financial completion model above is an authored diagnostic frame; the wider O2C, P2P, production, TM, account, valuation, and exception map still requires page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "A posting can be correct and the process can still be open" not in fin:
    fin = replace_once(fin, fin_boundary, fin_model, "FI completion model")
fin_path.write_text(fin, encoding="utf-8")


backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-033" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-033",
        "priority": "P1",
        "title": "Close the twelve-route core human-review wave",
        "status": "done",
        "outputs": [
            "/labs/enterprise-context/quality-management/",
            "/labs/enterprise-context/ewm/",
            "/labs/enterprise-context/mdg/",
            "/labs/enterprise-context/finance-logistics/"
        ],
        "working_rule": "Close the first core assessment content wave with domain-specific ownership/completion models and explicit evidence boundaries. Do not mark any page verified or public automatically."
    })
backlog["next_iteration_themes"] = [
    "review the three new Production question candidates and promote only non-duplicate Lead cases through an explicit reviewed change",
    "record page-level human-review findings separately from automated assessment-oriented editorial passes",
    "inspect secondary P1 routes for the highest cross-track assessment value instead of processing all fourteen in order",
    "use real assessment feedback to influence practice selection without changing factual truth"
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.12.0"
marker = "All twelve core human-review routes now expose assessment-oriented ownership or completion boundaries while remaining draft, noindex, and unverified"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review the new Production question candidates and promote only clearly non-duplicate Lead cases",
    "capture true page-level human review separately from automated editorial improvement",
    "select secondary P1 pages by cross-track assessment value rather than page count",
    "connect real assessment feedback to practice priority while factual truth remains source-based"
]
write_json(catalog_path, catalog)

print("LOOP-033 core human-review wave closed")
