#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGE = ROOT / "labs" / "enterprise-context" / "sales-order" / "index.html"
DATA = ROOT / "labs" / "assessment" / "data"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing patch anchor: {label}")
    return text.replace(old, new, 1)


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


page = PAGE.read_text(encoding="utf-8")
page = page.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)

boundary = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">hub</span>\n    <p><strong>Working rule:</strong> when a value is wrong, do not begin with the table. Begin with the question: <em>what decided this value, which inputs were used, and who uses the result next?</em></p>\n    <a href="/labs/enterprise-context/data/sales-order-graph.json">Open graph JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n'''
lead_section = boundary + '''\n  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Explain the first wrong decision in sixty seconds.</h2>\n      <p>A Lead answer should not become a tour of configuration. Start with the business symptom, identify the control level, trace the decision, and finish with evidence that proves both the cause and the corrected business result.</p>\n    </header>\n\n    <div class="ecg-decision-columns">\n      <div>\n        <h4>1. Frame</h4>\n        <ul>\n          <li>State the expected business behavior.</li>\n          <li>Name the first wrong value, status, quantity, or date.</li>\n          <li>Place it at header, item, or schedule-line level.</li>\n        </ul>\n      </div>\n      <div>\n        <h4>2. Trace</h4>\n        <ul>\n          <li>Read the runtime inputs before opening configuration.</li>\n          <li>Follow input → determination → output → downstream consumer.</li>\n          <li>Stop at the first layer where expected and actual behavior diverge.</li>\n        </ul>\n      </div>\n      <div>\n        <h4>3. Prove</h4>\n        <ul>\n          <li>Separate root cause from downstream symptoms.</li>\n          <li>Explain the blast radius before changing shared configuration.</li>\n          <li>Define proof of cause and proof of business completion.</li>\n        </ul>\n      </div>\n    </div>\n\n    <p class="ecg-caption"><strong>Example:</strong> if a schedule line behaves incorrectly, do not start by forcing the final schedule-line category. Check the item category and material-planning input first, because they are part of the determination context.</p>\n  </section>\n'''
if "Lead answer frame" not in page:
    page = replace_once(page, boundary, lead_section, "Lead answer frame insertion")

assessment_header = '''  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Assessment drills</p>\n'''
pre_drill = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>\n    <p><strong>Evidence boundary:</strong> the assessment factual-review layer currently confirms two load-bearing controls on this route: item-category determination and schedule-line-category behavior. The wider decision map keeps its own source registry, but the page still requires end-to-end human review before any verification or publication decision.</p>\n    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>\n  </section>\n\n'''
if "Evidence boundary:" not in page:
    page = replace_once(page, assessment_header, pre_drill + assessment_header, "evidence boundary insertion")

PAGE.write_text(page, encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-029" for item in backlog["items"]):
    backlog["items"].append(
        {
            "id": "LOOP-029",
            "priority": "P1",
            "title": "Sales Order Lead-answer editorial and consistency pass",
            "status": "done",
            "outputs": ["/labs/enterprise-context/sales-order/"],
            "working_rule": "Improve assessment usefulness and evidence transparency without changing page verification or publication state. Keep runtime diagnosis before configuration changes.",
        }
    )
backlog["next_iteration_themes"] = [
    "apply the same assessment-focused consistency pass to Pricing and Procurement, the next two core human-review routes",
    "review new Production question candidates without auto-publishing them",
    "inspect Procurement, ATP, EWM, and MDG graphs for the next evidence-complete candidate gaps",
    "use real assessment feedback to influence practice selection without changing factual truth",
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.8.0"
marker = "Sales Order now exposes a compact Lead-answer frame that connects runtime inputs, determination ownership, root-cause proof, blast radius, and business-completion evidence"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
write_json(catalog_path, catalog)

print("LOOP-029 Sales Order assessment pass applied")
