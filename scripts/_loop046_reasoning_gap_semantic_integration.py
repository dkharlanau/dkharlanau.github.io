#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "reasoning-gaps" / "index.html"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-046 marker not found: {label}")
    return text.replace(old, new, 1)


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    if 'id="semantic-result"' not in text:
        marker = '''  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Pattern contract</p>'''
        block = '''  <section class="research-canvas__inventory" id="semantic-result" data-reveal>\n    <header><p class="research-canvas__eyebrow">Semantic review</p><h2>Both non-diagnostic signals survive.</h2><p>Published-case comparison keeps the Sales Design and AI/Data Challenge candidates in the human promotion queue. Retention means “new reasoning signal”, not “approved for publication”.</p></header>\n    <div class="ecg-decision-columns">\n      <div><h4>Sales Design</h4><p>The existing third-party case starts after the model is chosen. The new candidate asks which supply model should exist at all, what becomes the default, and what condition changes that choice.</p></div>\n      <div><h4>AI/Data Challenge</h4><p>The existing Challenge case compares RAG and fine-tuning. The new candidate challenges autonomy itself and keeps deterministic workflow as a serious alternative.</p></div>\n      <div><h4>Next gate</h4><p>Both candidates still require explicit human promotion review before entering the 59-case published manifest.</p></div>\n    </div>\n    <a href="/labs/assessment/data/reasoning-gap-semantic-review.json">Open semantic review dataset <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n\n'''
        text = replace_once(text, marker, block + marker, "semantic result section")
    PAGE.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-046" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-046",
            "priority": "P1",
            "title": "Design and Challenge reasoning-gap semantic review",
            "status": "done",
            "outputs": [
                "/labs/assessment/reasoning-gaps/",
                "/labs/assessment/data/reasoning-gap-semantic-review.json",
                "scripts/validate_assessment_reasoning_gap_semantic_review.py"
            ],
            "working_rule": "Compare non-diagnostic candidates against published reasoning, not only wording. Retain both current Design/Challenge signals for human promotion review while keeping the published case manifest unchanged."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "semantic novelty review on the two new Design" not in theme]
        themes.insert(0, "prepare one human promotion review packet for all surviving reasoning-gap candidates without publishing them automatically")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"LOOP-046"' not in text:
        candidates = [
            ('"LOOP-044", "LOOP-045"):', '"LOOP-044", "LOOP-045", "LOOP-046"):'),
            ('"LOOP-043", "LOOP-044", "LOOP-045"):', '"LOOP-043", "LOOP-044", "LOOP-045", "LOOP-046"):')
        ]
        for old, new in candidates:
            if old in text:
                text = text.replace(old, new, 1)
                break
    marker = "\ndef test_reasoning_gap_semantic_review_keeps_novel_signals_in_human_queue_only() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_reasoning_gap_semantic_review_keeps_novel_signals_in_human_queue_only() -> None:\n    review = load_json("reasoning-gap-semantic-review.json")\n    candidates = load_json("reasoning-gap-candidates.json")\n    decisions = {item["candidate_id"]: item for item in review["decisions"]}\n\n    assert set(decisions) == {item["id"] for item in candidates["candidates"]}\n    assert decisions["RCAND-SALES-DESIGN-SUPPLY-MODEL"]["recommendation"] == "retain_for_human_promotion_review"\n    assert decisions["RCAND-AI-CHALLENGE-AUTONOMY"]["recommendation"] == "retain_for_human_promotion_review"\n    assert review["summary"]["published_case_change"] == 0\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_reasoning_gap_semantic_review.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_page()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
