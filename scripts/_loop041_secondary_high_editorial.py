#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-041 marker not found: {label}")
    return text.replace(old, new, 1)


def patch_integrations() -> None:
    path = ROOT / "labs" / "enterprise-context" / "integrations" / "index.md"
    text = path.read_text(encoding="utf-8")
    text = text.replace("last_modified_at: 2026-08-14", "last_modified_at: 2026-08-16", 1)
    marker = '''  <section class="research-canvas__inventory" id="architecture-stack" data-reveal>'''
    block = '''  <section class="research-canvas__inventory" id="lead-answer-frame" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead answer frame</p>\n      <h2>Explain the dependency before the platform.</h2>\n      <p>For an assessment answer, move through the design in a fixed order. A technology name is useful only after the business interaction and failure model are clear.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div><h4>01 · Business interaction</h4><p>What business object or event crosses the boundary, who owns it, and does the sender need an immediate answer?</p></div>\n      <div><h4>02 · Contract and semantics</h4><p>Define identity, version, required fields, idempotency expectation, ordering need, and what a successful receiver state means.</p></div>\n      <div><h4>03 · Delivery pattern</h4><p>Choose synchronous request, asynchronous command, event, queue, stream, file, or B2B exchange from the dependency and operating model.</p></div>\n      <div><h4>04 · Platform fit</h4><p>Only now select the SAP or non-SAP runtime, broker, mediation layer, or streaming platform that fits the contract.</p></div>\n      <div><h4>05 · Recovery</h4><p>Explain retries, duplicates, replay, ordering, monitoring, dead-letter or error handling, and the owner of recovery.</p></div>\n      <div><h4>06 · Business proof</h4><p>Close with reconciliation in the receiving business object. A green transport status is not proof of business completion.</p></div>\n    </div>\n    <p class="ecg-caption"><strong>Evidence boundary:</strong> reviewed SAP product claims support selected platform and interface behavior. The architecture stack, selection sequence, and design heuristics are authored reasoning and remain subject to page-level human review.</p>\n    <a href="/labs/enterprise-context/integration-operations/">Continue into runtime recovery and reconciliation <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>\n  </section>\n\n'''
    if 'id="lead-answer-frame"' not in text:
        text = replace_once(text, marker, block + marker, "integrations lead answer frame")
    path.write_text(text, encoding="utf-8")


def patch_sales_processes() -> None:
    path = ROOT / "labs" / "enterprise-context" / "sales-processes" / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("last_modified_at: 2026-08-15", "last_modified_at: 2026-08-16", 1)
    marker = '''  <section class="research-canvas__inventory" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Assessment path</p>'''
    block = '''  <section class="research-canvas__inventory" id="lead-branch-answer" data-reveal>\n    <header>\n      <p class="research-canvas__eyebrow">Lead branch answer</p>\n      <h2>Start from standard sell-from-stock, then name the changed rule.</h2>\n      <p>Special-process questions become much easier when the answer is a controlled delta from the baseline instead of a separate memorized document chain.</p>\n    </header>\n    <div class="ecg-decision-columns">\n      <div><h4>Baseline</h4><p>State the ordinary customer order → delivery → goods issue → billing path and the normal ownership of stock, supply, and billing.</p></div>\n      <div><h4>Changed business rule</h4><p>Name the one or two rules that create the branch: supplier ownership, legal entity, customer-specific supply, consignment ownership, return disposition, transfer of control, or billing trigger.</p></div>\n      <div><h4>Document consequence</h4><p>Explain which document or stock object appears, disappears, or changes role because of that business rule.</p></div>\n      <div><h4>Cross-process owner</h4><p>Show where Procurement, Production, Inventory, Shipping, Billing, FI/CO, EWM, or TM becomes part of the process.</p></div>\n      <div><h4>Failure proof</h4><p>Pick one likely failure and trace the first wrong rule or object. Do not repair the final sales document before proving the branch was correct.</p></div>\n      <div><h4>Trade-off</h4><p>Explain why this variant is useful and which commercial, operational, accounting, or integration cost it adds compared with the baseline.</p></div>\n    </div>\n    <p class="ecg-caption"><strong>Evidence boundary:</strong> source-backed process references support selected SAP behavior and scope. Stable <code>SD.*</code> memory codes, comparisons, and the branch-first method are authored learning tools, not SAP terminology.</p>\n  </section>\n\n'''
    if 'id="lead-branch-answer"' not in text:
        text = replace_once(text, marker, block + marker, "sales process branch answer")
    path.write_text(text, encoding="utf-8")


def patch_tm() -> None:
    path = ROOT / "labs" / "enterprise-context" / "transportation-management" / "index.html"
    text = path.read_text(encoding="utf-8")
    text = text.replace("last_modified_at: 2026-08-15", "last_modified_at: 2026-08-16", 1)
    marker = '''  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">TM deep dives</p>'''
    block = '''  <section class="research-canvas__inventory" id="lead-answer-frame" data-reveal>\n    <header><p class="research-canvas__eyebrow">Lead answer frame</p><h2>Demand is not the plan, and the plan is not settlement.</h2><p>A short TM answer should preserve the ownership changes from ERP demand through planning and execution to freight cost completion.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>01 · Demand</h4><p>Start with the ERP business document and prove the transportation demand object is complete and relevant.</p></div>\n      <div><h4>02 · Planning unit</h4><p>Explain Freight Unit Building and the attributes that define what can be planned together or separately.</p></div>\n      <div><h4>03 · Feasible plan</h4><p>Trace locations, times, resources, capacities, constraints, incompatibilities, and planning profile before blaming the optimizer.</p></div>\n      <div><h4>04 · Execution</h4><p>Separate Freight Order or Booking ownership from warehouse execution and carrier communication. Confirmations must reconcile across the boundary.</p></div>\n      <div><h4>05 · Charges and settlement</h4><p>Keep transport execution, charge calculation, settlement document, and downstream MM/FI completion as separate states.</p></div>\n      <div><h4>06 · Proof</h4><p>Find the first wrong object, show downstream impact, and prove the corrected demand, plan, execution state, and financial handoff.</p></div>\n    </div>\n    <p class="ecg-caption"><strong>Evidence boundary:</strong> reviewed SAP product facts support selected TM object and process behavior. The six-step diagnostic frame is an authored assessment model and does not change page verification state.</p>\n  </section>\n\n'''
    if 'id="lead-answer-frame"' not in text:
        text = replace_once(text, marker, block + marker, "TM lead answer frame")
    path.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not any(item.get("id") == "LOOP-041" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-041",
            "priority": "P1",
            "title": "High-reuse secondary editorial consistency pass",
            "status": "done",
            "outputs": [
                "/labs/enterprise-context/integrations/",
                "/labs/enterprise-context/sales-processes/",
                "/labs/enterprise-context/transportation-management/"
            ],
            "selection": {
                "input": "/labs/assessment/data/secondary-review-priority.json",
                "top_five": [
                    "/labs/enterprise-context/billing/",
                    "/labs/enterprise-context/automotive-jit/",
                    "/labs/enterprise-context/integrations/",
                    "/labs/enterprise-context/sales-processes/",
                    "/labs/enterprise-context/transportation-management/"
                ],
                "edited": [
                    "/labs/enterprise-context/integrations/",
                    "/labs/enterprise-context/sales-processes/",
                    "/labs/enterprise-context/transportation-management/"
                ],
                "already_strong_no_change": [
                    "/labs/enterprise-context/billing/",
                    "/labs/enterprise-context/automotive-jit/"
                ]
            },
            "working_rule": "Use the secondary review ranking to inspect high-reuse pages, but edit only real assessment gaps. Add domain-specific answer frames and evidence boundaries without changing verification or publication state."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "secondary review ranking" not in theme]
        themes.insert(0, "measure published-case reasoning coverage by scoring dimension so new cases target weak signals instead of raw topic count")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"LOOP-041"' not in text:
        text = text.replace('"LOOP-039", "LOOP-040"):', '"LOOP-039", "LOOP-040", "LOOP-041"):')
    marker = "\ndef test_secondary_high_reuse_editorial_pass_preserves_verification_boundary() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_secondary_high_reuse_editorial_pass_preserves_verification_boundary() -> None:\n    pages = {\n        "integrations": ROOT / "labs" / "enterprise-context" / "integrations" / "index.md",\n        "sales-processes": ROOT / "labs" / "enterprise-context" / "sales-processes" / "index.html",\n        "transportation-management": ROOT / "labs" / "enterprise-context" / "transportation-management" / "index.html",\n    }\n    required_tokens = {\n        "integrations": ["id=\\\"lead-answer-frame\\\"", "Explain the dependency before the platform.", "Evidence boundary:"],\n        "sales-processes": ["id=\\\"lead-branch-answer\\\"", "Start from standard sell-from-stock", "Evidence boundary:"],\n        "transportation-management": ["id=\\\"lead-answer-frame\\\"", "Demand is not the plan", "Evidence boundary:"],\n    }\n    for key, path in pages.items():\n        page = path.read_text(encoding="utf-8")\n        assert "verified: false" in page\n        assert "robots: noindex,follow" in page\n        for token in required_tokens[key]:\n            assert token in page, (key, token)\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_integrations()
    patch_sales_processes()
    patch_tm()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
