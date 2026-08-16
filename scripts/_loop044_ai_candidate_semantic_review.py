#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "candidate-semantic-review" / "index.html"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-044 marker not found: {label}")
    return text.replace(old, new, 1)


def patch_registry() -> None:
    path = DATA / "candidate-semantic-review.json"
    value = load(path)
    decisions = value.setdefault("decisions", [])
    by_id = {item["candidate_id"]: item for item in decisions}
    additions = [
        {
            "candidate_id": "CAND-AIAG-RAW-MCP",
            "recommendation": "retain_for_human_promotion_review",
            "reason": "The candidate tests a distinct AI/Data diagnostic path. The published AI diagnosis case focuses on trajectory, permissions, and approval bypass after a risky agent path. RAW-MCP instead asks whether the selected SAP capability and write payload are semantically correct: tool contract, semantic context, input schema, business-key resolution, and backend write validation.",
            "novel_signal": "Tool access can be technically valid while the selected business capability, key, or field semantics are wrong.",
            "closest_published_cases": ["ASSESS-AI-003", "ASSESS-INT-001"],
            "review_checks": [
                "Keep the case focused on tool semantics and business-key resolution rather than generic prompt quality.",
                "Require the learner to separate MCP/tool discovery from the business contract of the SAP capability.",
                "Require proof in the authoritative SAP object after correction, not only a successful tool response."
            ]
        },
        {
            "candidate_id": "CAND-AIAG-OVERPRIVILEGED",
            "recommendation": "reject_semantic_duplicate",
            "reason": "Published case ASSESS-AI-003 already tests an agent that reaches the expected result through an unnecessary write and bypasses the intended approval path. Its required reasoning includes trajectory evaluation, reduced tool permissions, explicit approval state, deterministic policy checks, and negative tests. An over-privileged-agent diagnosis would exercise materially the same Lead signal.",
            "novel_signal": None,
            "closest_published_cases": ["ASSESS-AI-003", "ASSESS-AI-001"],
            "review_checks": [
                "Keep the generated record for provenance but do not promote it as a new published case.",
                "A future identity case must change the problem materially, for example cross-tenant delegated identity or conflicting user-agent authorization, rather than restating broad permissions."
            ]
        }
    ]
    for item in additions:
        if item["candidate_id"] not in by_id:
            decisions.append(item)
    value["version"] = "1.1.0"
    value["updated_at"] = "2026-08-16"
    value["review_scope"] = {
        "candidate_inventory": "/labs/assessment/data/question-candidates.json",
        "published_case_manifest": "/labs/assessment/data/case-sets.json",
        "reviewed_candidates": len(decisions),
        "routes": [
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
    text = text.replace('<div class="research-canvas__signal-line"><span>01</span><strong>3</strong><small>Candidates reviewed</small></div>', '<div class="research-canvas__signal-line"><span>01</span><strong>5</strong><small>Candidates reviewed</small></div>', 1)
    text = text.replace('<div class="research-canvas__signal-line"><span>02</span><strong>2</strong><small>Retain for human review</small></div>', '<div class="research-canvas__signal-line"><span>02</span><strong>3</strong><small>Retain for human review</small></div>', 1)
    text = text.replace('<div class="research-canvas__signal-line"><span>03</span><strong>1</strong><small>Semantic duplicate</small></div>', '<div class="research-canvas__signal-line"><span>03</span><strong>2</strong><small>Semantic duplicates</small></div>', 1)
    if 'id="ai-semantic-review"' not in text:
        marker = '''  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Working rule</p>'''
        block = '''  <section class="research-canvas__inventory" id="ai-semantic-review" data-reveal>\n    <header><p class="research-canvas__eyebrow">AI/Data batch</p><h2>One new signal survives semantic review.</h2><p>The evidence gate produced two Agent Architecture Diagnose candidates. Semantic comparison against the published AI cases keeps only the tool-semantics failure.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>Keep · RAW MCP</h4><p><strong>CAND-AIAG-RAW-MCP</strong> asks whether a technically valid tool call selected the wrong SAP capability, business key, or field semantics. The diagnostic path is tool contract → semantic context → schema → key resolution → authoritative write validation.</p></div>\n      <div><h4>Reject · Over-privileged</h4><p><strong>CAND-AIAG-OVERPRIVILEGED</strong> materially repeats <strong>ASSESS-AI-003</strong>: risky trajectory, unnecessary write scope, approval bypass, reduced permissions, deterministic policy, and negative tests.</p></div>\n      <div><h4>Publication boundary</h4><p>The surviving candidate is still review-stage only. Semantic novelty is necessary for promotion, but it is not a human promotion decision.</p></div>\n    </div>\n  </section>\n\n'''
        text = replace_once(text, marker, block + marker, "AI semantic review section")
    PAGE.write_text(text, encoding="utf-8")


def patch_validator() -> None:
    path = ROOT / "scripts" / "validate_assessment_candidate_semantic_review.py"
    text = path.read_text(encoding="utf-8")
    text = text.replace('    assert review["summary"]["retain_for_human_promotion_review"] == 2\n    assert review["summary"]["reject_semantic_duplicate"] == 1\n', '    assert review["summary"]["retain_for_human_promotion_review"] == 3\n    assert review["summary"]["reject_semantic_duplicate"] == 2\n    raw_mcp = next(item for item in review["decisions"] if item["candidate_id"] == "CAND-AIAG-RAW-MCP")\n    overprivileged = next(item for item in review["decisions"] if item["candidate_id"] == "CAND-AIAG-OVERPRIVILEGED")\n    assert raw_mcp["recommendation"] == "retain_for_human_promotion_review"\n    assert overprivileged["recommendation"] == "reject_semantic_duplicate"\n    assert "ASSESS-AI-003" in overprivileged["closest_published_cases"]\n')
    text = text.replace('print("Candidate semantic review valid: 2 retained for human promotion review, 1 semantic duplicate, published cases unchanged.")', 'print("Candidate semantic review valid: 3 retained for human promotion review, 2 semantic duplicates, published cases unchanged.")')
    path.write_text(text, encoding="utf-8")


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if 'CAND-AIAG-RAW-MCP' not in text[text.find('def test_candidate_semantic_review'):]:
        text = text.replace(
            '    assert decisions["CAND-PP-COST"]["recommendation"] == "reject_semantic_duplicate"\n    assert "ASSESS-FIN-005" in decisions["CAND-PP-COST"]["closest_published_cases"]\n',
            '    assert decisions["CAND-PP-COST"]["recommendation"] == "reject_semantic_duplicate"\n    assert "ASSESS-FIN-005" in decisions["CAND-PP-COST"]["closest_published_cases"]\n    assert decisions["CAND-AIAG-RAW-MCP"]["recommendation"] == "retain_for_human_promotion_review"\n    assert decisions["CAND-AIAG-OVERPRIVILEGED"]["recommendation"] == "reject_semantic_duplicate"\n    assert "ASSESS-AI-003" in decisions["CAND-AIAG-OVERPRIVILEGED"]["closest_published_cases"]\n'
        )
    if '"LOOP-044"' not in text:
        text = text.replace('"LOOP-042", "LOOP-043"):', '"LOOP-042", "LOOP-043", "LOOP-044"):')
    TESTS.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-044" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-044",
            "priority": "P1",
            "title": "AI/Data Diagnose candidate semantic review",
            "status": "done",
            "outputs": [
                "/labs/assessment/candidate-semantic-review/",
                "/labs/assessment/data/candidate-semantic-review.json"
            ],
            "working_rule": "Reject evidence-backed candidates that repeat an existing Lead reasoning signal. Retain RAW-MCP for human promotion review and reject over-privileged-agent diagnosis as a semantic duplicate of ASSESS-AI-003."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "semantic novelty review on the new AI/Data" not in theme]
        themes.insert(0, "design explicit non-diagnostic authoring contracts for the thin Sales Design and AI/Data Challenge cells")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def main() -> None:
    patch_registry()
    patch_page()
    patch_validator()
    patch_tests()
    patch_backlog()


if __name__ == "__main__":
    main()
