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


# Production: explicit completion checkpoints.
prod_path = ROOT / "labs" / "enterprise-context" / "production" / "index.html"
prod = prod_path.read_text(encoding="utf-8")
prod_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">precision_manufacturing</span>\n    <p><strong>Working rule:</strong> when a production result is wrong, move upstream until the first wrong decision is visible. A manual order correction can hide bad demand, MRP parameters, production method, master data, staging, or settlement design.</p>\n    <a href="/labs/enterprise-context/data/production-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
prod_completion = prod_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Completion model</p>\n      <h2>One order can be complete in one layer and open in another.</h2>\n      <p>This is a diagnostic model, not a new SAP status model. I use four checkpoints to avoid calling production complete too early.</p>\n    </header>\n    <div class="ecg-control-stack">\n      <article><span>PLAN</span><h3>Planned correctly</h3><p>Demand, MRP result, dates, quantity, and production method represent the business need.</p><strong>Proof: the order starts from the intended requirement and master data.</strong></article>\n      <article><span>EXECUTE</span><h3>Executed correctly</h3><p>Components, operations, staging, confirmations, and exceptions represent what happened on the shop floor.</p><strong>Proof: execution evidence explains quantity, time, and consumption.</strong></article>\n      <article><span>STOCK</span><h3>Received correctly</h3><p>The finished quantity reaches the expected stock and warehouse state through the intended goods-receipt path.</p><strong>Proof: order, material document, stock state, and warehouse state agree.</strong></article>\n      <article><span>COST</span><h3>Financially closed</h3><p>Actual costs, WIP or variance, settlement rule, receiver, and settlement state agree with the process design.</p><strong>Proof: physical completion and financial completion reconcile.</strong></article>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> a technically confirmed order is not enough evidence for stock receipt or financial close. Name which completion layer is still open.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms production-version selection and the goods-receipt / settlement relationship. The four-checkpoint completion model above is an authored diagnostic frame; the wider MRP, execution, capacity, staging, and integration content still requires page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "One order can be complete in one layer" not in prod:
    prod = replace_once(prod, prod_boundary, prod_completion, "production completion model")
prod_path.write_text(prod, encoding="utf-8")


# Integration Operations: transport/application/business completion.
int_path = ROOT / "labs" / "enterprise-context" / "integration-operations" / "index.html"
integ = int_path.read_text(encoding="utf-8")
int_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">sync_problem</span>\n    <p><strong>Working rule:</strong> before any retry, prove message identity, first failed hop, receiver commit state, ordering dependency, and duplicate protection. Close the incident only when the business result is reconciled.</p>\n    <a href="/labs/enterprise-context/data/integration-operations-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
int_completion = int_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Completion model</p>\n      <h2>Three green lights mean three different things.</h2>\n      <p>I separate technical delivery, application processing, and business reconciliation. A monitor can prove one layer while the next layer is still wrong.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div><h4>1. Transport complete</h4><ul><li>The expected message identity reached the intended receiver path.</li><li>Delivery semantics and ordering behaved as designed.</li><li>Retries did not create an uncontrolled duplicate.</li></ul></div>\n      <div><h4>2. Application complete</h4><ul><li>The receiver processing state and commit outcome are known.</li><li>The expected business object or update exists once.</li><li>Application errors are corrected or deliberately rejected with ownership.</li></ul></div>\n      <div><h4>3. Business complete</h4><ul><li>The downstream process state matches the sender's business intent.</li><li>Reconciliation proves quantity, value, status, or object consistency.</li><li>The incident closes on business evidence, not only a green middleware status.</li></ul></div>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> before replay, answer “did the receiver commit?” Before closure, answer “did the business process reconcile?”</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> six claim-level checks already cover duplicate handling, ordering, queue behavior, monitoring, handled exceptions, and AIF correction/restart behavior. The three-layer completion model is an authored operating frame and does not turn the whole page into a verified product statement.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "Three green lights mean three different things" not in integ:
    integ = replace_once(integ, int_boundary, int_completion, "integration completion model")
int_path.write_text(integ, encoding="utf-8")


# Inventory Management: physical/book/warehouse/financial consistency.
im_path = ROOT / "labs" / "enterprise-context" / "inventory-management" / "index.html"
im = im_path.read_text(encoding="utf-8")
im_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">inventory_2</span>\n    <p><strong>Working rule:</strong> a material document is evidence of a stock event. Explain what changed in quantity, location, stock type, ownership, valuation, consumption, or transit state before discussing a movement-type number.</p>\n    <a href="/labs/enterprise-context/data/inventory-management-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
im_completion = im_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Completion model</p>\n      <h2>Prove the same event in four state views.</h2>\n      <p>A posting can be valid in Inventory Management and still leave a warehouse, accounting, or physical-count inconsistency. I compare the state views before creating a compensating movement.</p>\n    </header>\n    <div class="ecg-control-stack">\n      <article><span>EVENT</span><h3>Business event</h3><p>What happened: receipt, issue, transfer, stock-type change, consumption, or inventory difference?</p><strong>Proof: the reference and movement semantics match the business event.</strong></article>\n      <article><span>STOCK</span><h3>Book stock</h3><p>Which quantity, plant, storage location, stock type, ownership, batch, or special-stock dimension changed?</p><strong>Proof: before/after stock state matches the intended event.</strong></article>\n      <article><span>WAREHOUSE</span><h3>Physical execution</h3><p>If EWM or another warehouse layer is involved, does its execution state represent the same physical movement?</p><strong>Proof: IM and warehouse states reconcile across the handoff.</strong></article>\n      <article><span>VALUE</span><h3>Financial effect</h3><p>Did valuation, consumption, account assignment, or accounting follow the intended movement semantics?</p><strong>Proof: material and accounting consequences tell the same business story.</strong></article>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> do not use a compensating posting until you know which state view is wrong. Otherwise the stock number may improve while the evidence chain gets worse.</p>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms movement-type control behavior and the difference between counting stock and posting physical-inventory differences. The four-view completion model is an authored diagnostic frame; warehouse and finance handoffs still require page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n'''
if "Prove the same event in four state views" not in im:
    im = replace_once(im, im_boundary, im_completion, "inventory completion model")
im_path.write_text(im, encoding="utf-8")


backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-032" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-032",
        "priority": "P1",
        "title": "Execution and completion boundary pass",
        "status": "done",
        "outputs": [
            "/labs/enterprise-context/production/",
            "/labs/enterprise-context/integration-operations/",
            "/labs/enterprise-context/inventory-management/"
        ],
        "working_rule": "Separate local technical completion from stock, warehouse, business, and financial completion. Keep completion models explicitly authored and factual claims source-bound."
    })
backlog["next_iteration_themes"] = [
    "continue the core human-review content pass with Quality Management, EWM, MDG, and FI/CO Logistics",
    "review the three new Production question candidates without auto-publishing them",
    "inspect ATP, EWM, and MDG graphs for additional evidence-complete candidate gaps",
    "use real assessment feedback to influence practice selection without changing factual truth"
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.11.0"
for marker in [
    "Production now separates planned, executed, stock-received, and financially closed states in one Lead completion model",
    "Integration Operations now separates transport completion, receiver application completion, and business reconciliation",
    "Inventory Management now compares business-event, book-stock, warehouse-execution, and financial state before compensating postings"
]:
    if marker not in catalog["coverage"]["strong_now"]:
        catalog["coverage"]["strong_now"].append(marker)
write_json(catalog_path, catalog)

print("LOOP-032 completion boundaries applied")
