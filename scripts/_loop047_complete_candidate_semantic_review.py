#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "candidate-semantic-review" / "index.html"
VALIDATOR = ROOT / "scripts" / "validate_assessment_candidate_semantic_review.py"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def patch_registry() -> None:
    path = DATA / "candidate-semantic-review.json"
    value = load(path)
    decisions = value.setdefault("decisions", [])
    ids = {item["candidate_id"] for item in decisions}
    additions = [
        {
            "candidate_id": "CAND-BIL-WRONG-REFERENCE",
            "recommendation": "retain_for_human_promotion_review",
            "reason": "The published Billing cases cover due-state, split, repricing, FI transfer/account determination, external invoice delivery, and correction lifecycle. This candidate instead asks why billing quantity or value follows an unexpected predecessor relationship. The Lead signal is to reconstruct the reference document, copy-control path, source quantity/value, and billing relationship before changing pricing or the invoice manually.",
            "novel_signal": "Prove the billing reference and copy-control relationship before repairing a downstream quantity or value symptom.",
            "closest_published_cases": ["ASSESS-BIL-001", "ASSESS-BIL-003"],
            "review_checks": [
                "Keep the first diagnostic branch on source document relationship and copied quantity/value, not generic billing troubleshooting.",
                "Require document flow and copy-control evidence before any pricing or manual billing correction.",
                "Reject a rewrite that collapses into not-billing-due or repricing behavior already covered by published cases."
            ]
        },
        {
            "candidate_id": "CAND-INTOPS-OWNERSHIP",
            "recommendation": "retain_for_human_promotion_review",
            "reason": "Published Integration Operations cases test commit state, retry/idempotency, ordering, master-data failure, duplicate consumers, and an operational scorecard. This candidate is a Diagnose case about a different failure: the error is visible, but ownership of correction and business confirmation is undefined. It requires separating technical recipient ownership, business-state ownership, master-data/configuration ownership, SLA/runbook responsibility, and final reconciliation.",
            "novel_signal": "An observable integration error is not operationally controlled until correction ownership and business-confirmation ownership are explicit.",
            "closest_published_cases": ["ASSESS-INTOPS-001", "ASSESS-INTOPS-006"],
            "review_checks": [
                "Keep the case diagnostic: find the first missing ownership contract, not design a generic monitoring dashboard.",
                "Require separate owners for technical correction and business confirmation when they differ.",
                "Reject a rewrite that becomes only a KPI/scorecard design case already covered by ASSESS-INTOPS-006."
            ]
        }
    ]
    for item in additions:
        if item["candidate_id"] not in ids:
            decisions.append(item)
    value["version"] = "1.2.0"
    value["updated_at"] = "2026-08-16"
    value["review_scope"] = {
        "candidate_inventory": "/labs/assessment/data/question-candidates.json",
        "published_case_manifest": "/labs/assessment/data/case-sets.json",
        "reviewed_candidates": len(decisions),
        "routes": [
            "/labs/enterprise-context/billing/",
            "/labs/enterprise-context/integration-operations/",
            "/labs/enterprise-context/production/",
            "/labs/enterprise-context/business-ai/agents/"
        ]
    }
    value["summary"] = {
        "retain_for_human_promotion_review": sum(item["recommendation"] == "retain_for_human_promotion_review" for item in decisions),
        "reject_semantic_duplicate": sum(item["recommendation"] == "reject_semantic_duplicate" for item in decisions),
        "published_case_change": 0
    }
    dump(path, value)


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    text = text.replace('<div class="research-canvas__signal-line"><span>01</span><strong>5</strong><small>Candidates reviewed</small></div>', '<div class="research-canvas__signal-line"><span>01</span><strong>7</strong><small>Candidates reviewed</small></div>')
    text = text.replace('<div class="research-canvas__signal-line"><span>02</span><strong>3</strong><small>Retain for human review</small></div>', '<div class="research-canvas__signal-line"><span>02</span><strong>5</strong><small>Retain for human review</small></div>')
    if 'id="legacy-generated-review"' not in text:
        marker = '  <section class="research-canvas__inventory" id="ai-semantic-review" data-reveal>'
        block = '''  <section class="research-canvas__inventory" id="legacy-generated-review" data-reveal>\n    <header><p class="research-canvas__eyebrow">Generated backlog close</p><h2>The semantic registry now covers every active generated candidate.</h2><p>Two older candidates predated the semantic-review layer. Both add distinct diagnostic pressure and stay in human promotion review.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>Billing reference</h4><p><strong>CAND-BIL-WRONG-REFERENCE</strong> tests source-document relationship, copy-control path, copied quantity/value, and document-flow proof before downstream repair.</p></div>\n      <div><h4>Integration ownership</h4><p><strong>CAND-INTOPS-OWNERSHIP</strong> tests the missing operating contract between technical correction ownership and business confirmation ownership.</p></div>\n      <div><h4>Invariant</h4><p>Every active generated candidate now has exactly one semantic decision. A future generator expansion cannot silently bypass semantic review.</p></div>\n    </div>\n  </section>\n\n'''
        if marker not in text:
            raise SystemExit("candidate semantic page marker missing")
        text = text.replace(marker, block + marker, 1)
    PAGE.write_text(text, encoding="utf-8")


def patch_validator() -> None:
    text = VALIDATOR.read_text(encoding="utf-8")
    old = '''    assert review["summary"]["retain_for_human_promotion_review"] == 3\n    assert review["summary"]["reject_semantic_duplicate"] == 2\n'''
    new = '''    active_candidate_ids = {item["id"] for item in inventory["items"] if item["status"] == "candidate"}\n    decision_ids = {item["candidate_id"] for item in review["decisions"]}\n    assert decision_ids == active_candidate_ids, (sorted(decision_ids), sorted(active_candidate_ids))\n    assert review["summary"]["retain_for_human_promotion_review"] == 5\n    assert review["summary"]["reject_semantic_duplicate"] == 2\n'''
    if old in text:
        text = text.replace(old, new, 1)
    elif "active_candidate_ids" not in text:
        raise SystemExit("semantic validator count marker missing")
    text = text.replace('print("Candidate semantic review valid: 3 retained for human promotion review, 2 semantic duplicates, published cases unchanged.")', 'print("Candidate semantic review valid: all active generated candidates reviewed; 5 retained, 2 semantic duplicates, published cases unchanged.")')
    VALIDATOR.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-047" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-047",
            "priority": "P1",
            "title": "Complete generated-candidate semantic coverage",
            "status": "done",
            "outputs": [
                "/labs/assessment/candidate-semantic-review/",
                "/labs/assessment/data/candidate-semantic-review.json",
                "scripts/validate_assessment_candidate_semantic_review.py"
            ],
            "working_rule": "Require exactly one semantic decision for every active generated candidate. Retain the billing-reference and integration-ownership signals, and prevent future generator output from bypassing semantic review."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "remaining generated candidates" not in theme]
        themes.insert(0, "build one human promotion review packet from every semantic-surviving generated and non-diagnostic candidate without publishing any case")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"LOOP-047"' not in text:
        for old, new in [
            ('"LOOP-045", "LOOP-046"):', '"LOOP-045", "LOOP-046", "LOOP-047"):'),
            ('"LOOP-044", "LOOP-045", "LOOP-046"):', '"LOOP-044", "LOOP-045", "LOOP-046", "LOOP-047"):')
        ]:
            if old in text:
                text = text.replace(old, new, 1)
                break
    marker = "\ndef test_every_active_generated_candidate_has_one_semantic_decision() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_every_active_generated_candidate_has_one_semantic_decision() -> None:\n    inventory = load_json("question-candidates.json")\n    review = load_json("candidate-semantic-review.json")\n    active = {item["id"] for item in inventory["items"] if item["status"] == "candidate"}\n    decisions = {item["candidate_id"] for item in review["decisions"]}\n    assert decisions == active\n    assert review["summary"]["retain_for_human_promotion_review"] == 5\n    assert review["summary"]["reject_semantic_duplicate"] == 2\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_registry()
    patch_page()
    patch_validator()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
