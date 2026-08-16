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


# Pricing: turn the existing diagnostic engine into a compact assessment answer frame.
pricing_path = ROOT / "labs" / "enterprise-context" / "pricing" / "index.html"
pricing = pricing_path.read_text(encoding="utf-8")
pricing = pricing.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)
pricing_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">troubleshoot</span>\n    <p><strong>My working rule:</strong> when pricing is wrong, I do not start with the condition record. I find the first place where the actual path differs from the expected path.</p>\n    <a href="/labs/enterprise-context/data/pricing-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
pricing_frame = pricing_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Do not explain pricing from the final net value.</h2>\n      <p>A short Lead answer should show where the pricing path first diverged. That gives the interviewer a diagnosis, not a list of configuration objects.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div>\n        <h4>1. Context and procedure</h4>\n        <ul><li>State the expected commercial result and document context.</li><li>Confirm the pricing procedure before checking one condition.</li><li>If the procedure is wrong, trace its determination inputs upstream.</li></ul>\n      </div>\n      <div>\n        <h4>2. Search and calculation</h4>\n        <ul><li>Check condition eligibility, access sequence, and runtime key.</li><li>Prove whether a valid record was found and whether it stayed active.</li><li>Separate rate, base, scale, formula, and final condition value.</li></ul>\n      </div>\n      <div>\n        <h4>3. Boundary and proof</h4>\n        <ul><li>Compare order and billing as separate pricing contexts when required.</li><li>Check custom-field or routine inputs before changing shared configuration.</li><li>Explain blast radius, proof of cause, and proof of corrected value.</li></ul>\n      </div>\n    </div>\n    <p class="ecg-caption"><strong>Good diagnostic sentence:</strong> “The record exists, but first I need to prove that the expected procedure, condition, access, and runtime key were actually used.”</p>\n  </section>\n'''
if "Good diagnostic sentence:" not in pricing:
    pricing = replace_once(pricing, pricing_boundary, pricing_frame, "pricing Lead frame")

pricing_memory = '''  <section class="research-canvas__inventory" id="pricing-memory" data-reveal>\n'''
pricing_evidence = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms the condition-technique search model and pricing-procedure determination inputs. The wider page includes extensions, billing parity, and practitioner heuristics from its source registry, but it still needs page-level human review before any verification or publication decision.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n\n'''
if "claim-level review currently confirms the condition-technique" not in pricing:
    pricing = replace_once(pricing, pricing_memory, pricing_evidence + pricing_memory, "pricing evidence boundary")
pricing_path.write_text(pricing, encoding="utf-8")


# Procurement: make the end-to-end answer shape explicit without flattening the process into a PO-only story.
proc_path = ROOT / "labs" / "enterprise-context" / "procurement" / "index.html"
proc = proc_path.read_text(encoding="utf-8")
proc = proc.replace("last_modified_at: 2026-08-15", "last_modified_at: 2026-08-16", 1)
proc_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">shopping_cart</span>\n    <p><strong>My working rule:</strong> I start with the original requirement and find the first wrong procurement decision. I do not repair a PO field until I know why that field has the value.</p>\n    <a href="/labs/enterprise-context/data/procurement-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
proc_frame = proc_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Start before the PO and finish after the receipt.</h2>\n      <p>A procurement answer becomes Lead-level when it connects demand, sourcing, document control, execution, and financial completion instead of treating the purchase order as the whole process.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div>\n        <h4>1. Requirement and source</h4>\n        <ul><li>State what demand started the process and what should be procured.</li><li>Trace source-of-supply logic before blaming the supplier field.</li><li>Separate supplier choice from purchasing price determination.</li></ul>\n      </div>\n      <div>\n        <h4>2. Item and control</h4>\n        <ul><li>Separate item category from account-assignment category.</li><li>Identify approval, output, and organizational ownership.</li><li>Check the first wrong rule or master-data input before changing the PO.</li></ul>\n      </div>\n      <div>\n        <h4>3. Execute and reconcile</h4>\n        <ul><li>Trace goods or service receipt, invoice verification, and PO history.</li><li>Separate physical completion from GR/IR and financial completion.</li><li>Close with proof of cause, corrected process state, and reconciliation.</li></ul>\n      </div>\n    </div>\n    <p class="ecg-caption"><strong>Lead signal:</strong> a wrong supplier, wrong account assignment, blocked PO, missing receipt, and open GR/IR may appear in one document flow, but they belong to different decision owners.</p>\n  </section>\n'''
if "Lead signal:" not in proc:
    proc = replace_once(proc, proc_boundary, proc_frame, "procurement Lead frame")

proc_memory = '''  <section class="research-canvas__inventory" id="procurement-memory" data-reveal>\n'''
proc_evidence = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms source-of-supply behavior and the distinction between item category and account-assignment category. The end-to-end map covers more decisions and integrations, so page-level human review is still required before any verification or publication decision.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n\n'''
if "claim-level review currently confirms source-of-supply" not in proc:
    proc = replace_once(proc, proc_memory, proc_evidence + proc_memory, "procurement evidence boundary")
proc_path.write_text(proc, encoding="utf-8")


backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-030" for item in backlog["items"]):
    backlog["items"].append(
        {
            "id": "LOOP-030",
            "priority": "P1",
            "title": "Pricing and Procurement Lead-answer consistency pass",
            "status": "done",
            "outputs": [
                "/labs/enterprise-context/pricing/",
                "/labs/enterprise-context/procurement/"
            ],
            "working_rule": "Expose domain-specific Lead answer frames and factual-review boundaries without replacing the deeper graph model or changing verification/publication state."
        }
    )
backlog["next_iteration_themes"] = [
    "continue the core human-review content pass with ATP and Shipping, then Production",
    "review new Production question candidates without auto-publishing them",
    "inspect Procurement, ATP, EWM, and MDG graphs for additional evidence-complete candidate gaps",
    "use real assessment feedback to influence practice selection without changing factual truth"
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.9.0"
for marker in [
    "Pricing now exposes a concise Lead diagnosis from procedure determination through access, runtime key, calculation, billing parity, and proof",
    "Procurement now exposes a concise Lead answer from requirement and sourcing through document control, execution, GR/IR, and reconciliation"
]:
    if marker not in catalog["coverage"]["strong_now"]:
        catalog["coverage"]["strong_now"].append(marker)
write_json(catalog_path, catalog)

print("LOOP-030 Pricing and Procurement assessment pass applied")
