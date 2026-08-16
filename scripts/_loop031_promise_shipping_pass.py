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


# ATP / aATP
atp_path = ROOT / "labs" / "enterprise-context" / "atp" / "index.html"
atp = atp_path.read_text(encoding="utf-8")
atp = atp.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)
atp_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">inventory_2</span>\n    <p><strong>My working rule:</strong> if ATP looks wrong, I first reconstruct the promise: requirement, plant, material availability date, scope, supply/demand, and policy restrictions.</p>\n    <a href="/labs/enterprise-context/data/atp-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
atp_frame = atp_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Separate promise logic from the stock number.</h2>\n      <p>A good ATP answer explains why a requirement could or could not be confirmed on a date. It does not stop at “stock exists” or “ATP is zero”.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div>\n        <h4>1. Build the requirement</h4>\n        <ul><li>Confirm ATP relevance and the actual requirement quantity.</li><li>Check plant and material availability date before reading supply.</li><li>Separate a scheduling-date problem from an availability problem.</li></ul>\n      </div>\n      <div>\n        <h4>2. Build the promise</h4>\n        <ul><li>Check scope and the supply-demand picture used by the availability check.</li><li>Explain the PAC result before adding advanced policy controls.</li><li>Then inspect PAL, Supply Protection, alternatives, or BOP when they are active.</li></ul>\n      </div>\n      <div>\n        <h4>3. Prove the owner</h4>\n        <ul><li>Show whether the first divergence is date, supply, scope, or business policy.</li><li>Trace alternative plant/product decisions into Shipping, EWM, TM, tax, or margin impact.</li><li>Close with proof of confirmation and downstream business feasibility.</li></ul>\n      </div>\n    </div>\n    <p class="ecg-caption"><strong>Boundary with Shipping:</strong> ATP answers what can be promised. Shipping and scheduling explain how the logistics dates and execution context are built. A wrong upstream date can make a correct availability check look wrong.</p>\n  </section>\n'''
if "Boundary with Shipping:" not in atp:
    atp = replace_once(atp, atp_boundary, atp_frame, "ATP Lead frame")

atp_memory = '''  <section class="research-canvas__inventory" id="atp-memory" data-reveal>\n'''
atp_evidence = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms the advanced ATP simulation API scope, Supply Protection behavior, and the complementary PAL/Supply Protection model. The wider page also covers classic ATP controls, BOP, alternatives, and integrations, so page-level human review is still required.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n\n'''
if "advanced ATP simulation API scope" not in atp:
    atp = replace_once(atp, atp_memory, atp_evidence + atp_memory, "ATP evidence boundary")
atp_path.write_text(atp, encoding="utf-8")


# Shipping & scheduling
shipping_path = ROOT / "labs" / "enterprise-context" / "shipping" / "index.html"
shipping = shipping_path.read_text(encoding="utf-8")
shipping = shipping.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)
shipping_boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">local_shipping</span>\n    <p><strong>My working rule:</strong> I find the first wrong shipping input or calculated date. I do not change transit time until the final delivery date looks acceptable.</p>\n    <a href="/labs/enterprise-context/data/shipping-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
shipping_frame = shipping_boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Trace the date back to the first logistics decision.</h2>\n      <p>A final delivery date is a downstream result. The Lead-level task is to identify which plant, shipping, route, calendar, or scheduling decision first moved away from the expected business path.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div>\n        <h4>1. Execution context</h4>\n        <ul><li>Confirm the delivering plant before debugging Shipping.</li><li>Trace plant + shipping condition + loading group into shipping point.</li><li>Trace origin, destination, shipping policy, and transportation group into route.</li></ul>\n      </div>\n      <div>\n        <h4>2. Date construction</h4>\n        <ul><li>Separate route/transit data from pick-pack, loading, and calendar effects.</li><li>Trace requested delivery date backward to material availability, loading, GI, and transportation dates.</li><li>Check whether ATP is consuming the date you actually intended.</li></ul>\n      </div>\n      <div>\n        <h4>3. Execute and prove</h4>\n        <ul><li>Distinguish delivery-due state from warehouse or transport execution.</li><li>Identify the handoff to EWM or TM instead of changing SD to repair their downstream state.</li><li>Prove the corrected dates and the executable delivery path end to end.</li></ul>\n      </div>\n    </div>\n    <p class="ecg-caption"><strong>Boundary with ATP:</strong> Shipping builds important logistics dates and execution context. ATP evaluates the promise against its requirement date, supply-demand scope, and policy controls. Diagnose the first wrong owner before changing lead times or confirmations.</p>\n  </section>\n'''
if "Diagnose the first wrong owner" not in shipping:
    shipping = replace_once(shipping, shipping_boundary, shipping_frame, "Shipping Lead frame")

shipping_memory = '''  <section class="research-canvas__inventory" id="shipping-memory" data-reveal>\n'''
shipping_evidence = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> claim-level review currently confirms the shipping-point input model and the classic route-determination context, including the role of route data in scheduling. The wider execution and EWM/TM boundary still requires page-level human review.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n\n'''
if "shipping-point input model" not in shipping:
    shipping = replace_once(shipping, shipping_memory, shipping_evidence + shipping_memory, "Shipping evidence boundary")
shipping_path.write_text(shipping, encoding="utf-8")


backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-031" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-031",
        "priority": "P1",
        "title": "ATP and Shipping Lead-boundary consistency pass",
        "status": "done",
        "outputs": ["/labs/enterprise-context/atp/", "/labs/enterprise-context/shipping/"],
        "working_rule": "Separate promise ownership from shipping/scheduling ownership, expose first-wrong-decision diagnostics, and keep factual review distinct from page verification."
    })
backlog["next_iteration_themes"] = [
    "continue the core human-review content pass with Production, Integration Operations, and Inventory Management",
    "review new Production question candidates without auto-publishing them",
    "inspect ATP, EWM, and MDG graphs for additional evidence-complete candidate gaps",
    "use real assessment feedback to influence practice selection without changing factual truth"
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.10.0"
for marker in [
    "ATP now exposes a Lead answer that separates requirement/date context, availability scope, policy controls, alternatives, and proof of promise",
    "Shipping now exposes a Lead answer that separates upstream plant, shipping point, route, scheduling, execution ownership, and the ATP boundary"
]:
    if marker not in catalog["coverage"]["strong_now"]:
        catalog["coverage"]["strong_now"].append(marker)
write_json(catalog_path, catalog)

print("LOOP-031 ATP and Shipping assessment pass applied")
