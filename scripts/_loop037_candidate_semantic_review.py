#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump_patch(value: str) -> str:
    parts = value.split(".")
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        parts[2] = str(int(parts[2]) + 1)
        return ".".join(parts)
    return value


def main() -> None:
    catalog_path = DATA / "catalog.json"
    catalog = load(catalog_path)
    if not any(item.get("id") == "candidate-semantic-review" for item in catalog.get("authoring_tools", [])):
        catalog.setdefault("authoring_tools", []).append({
            "id": "candidate-semantic-review",
            "label": "Candidate Semantic Review",
            "route": "/labs/assessment/candidate-semantic-review/",
            "purpose": "Review evidence-gated question candidates for semantic novelty after deterministic duplicate checks and before any human promotion decision."
        })
        catalog["version"] = bump_patch(str(catalog.get("version", "1.0.0")))
        catalog["updated_at"] = "2026-08-16"
        dump(catalog_path, catalog)

    backlog_path = DATA / "backlog.json"
    backlog = load(backlog_path)
    if not any(item.get("id") == "LOOP-037" for item in backlog.get("items", [])):
        backlog.setdefault("items", []).append({
            "id": "LOOP-037",
            "priority": "P1",
            "title": "Production candidate semantic review",
            "status": "done",
            "outputs": [
                "/labs/assessment/candidate-semantic-review/",
                "/labs/assessment/data/candidate-semantic-review.json",
                "scripts/validate_assessment_candidate_semantic_review.py"
            ],
            "working_rule": "Use semantic review after deterministic dedup. Retain only candidates that add a materially new Lead reasoning signal, and never publish them without a separate human promotion decision."
        })
        backlog["updated_at"] = "2026-08-16"
        themes = backlog.get("next_iteration_themes", [])
        themes = [theme for theme in themes if "Production candidates" not in theme and "Production candidate" not in theme]
        themes.insert(0, "add a Board Mode review handoff that points low scoring dimensions to existing review-map routes without writing history")
        backlog["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(backlog_path, backlog)

    tests_path = ROOT / "tests" / "test_assessment_practice_layer.py"
    tests = tests_path.read_text(encoding="utf-8")
    if '"candidate-semantic-review": ASSESSMENT / "candidate-semantic-review" / "index.html",' not in tests:
        tests = tests.replace(
            '        "question-review": ASSESSMENT / "question-review" / "index.html",\n',
            '        "question-review": ASSESSMENT / "question-review" / "index.html",\n        "candidate-semantic-review": ASSESSMENT / "candidate-semantic-review" / "index.html",\n'
        )
    if 'assert authoring["candidate-semantic-review"]["route"]' not in tests:
        tests = tests.replace(
            '    assert authoring["question-review"]["route"] == "/labs/assessment/question-review/"\n',
            '    assert authoring["question-review"]["route"] == "/labs/assessment/question-review/"\n    assert authoring["candidate-semantic-review"]["route"] == "/labs/assessment/candidate-semantic-review/"\n'
        )
    if '"LOOP-037"' not in tests:
        tests = tests.replace('"LOOP-035", "LOOP-036"):', '"LOOP-035", "LOOP-036", "LOOP-037"):')
    marker = "\ndef test_candidate_semantic_review_keeps_publication_separate_from_novelty_review() -> None:\n"
    if marker not in tests:
        tests += '''\n\ndef test_candidate_semantic_review_keeps_publication_separate_from_novelty_review() -> None:\n    review = load_json("candidate-semantic-review.json")\n    inventory = load_json("question-candidates.json")\n    manifest = load_json("case-sets.json")\n    decisions = {item["candidate_id"]: item for item in review["decisions"]}\n\n    assert review["summary"]["published_case_change"] == 0\n    assert manifest["total_cases"] == inventory["published_case_count"]\n    assert decisions["CAND-PP-WRONG-QUANTITY"]["recommendation"] == "retain_for_human_promotion_review"\n    assert decisions["CAND-PP-GR"]["recommendation"] == "retain_for_human_promotion_review"\n    assert decisions["CAND-PP-COST"]["recommendation"] == "reject_semantic_duplicate"\n    assert "ASSESS-FIN-005" in decisions["CAND-PP-COST"]["closest_published_cases"]\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_candidate_semantic_review.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    tests_path.write_text(tests, encoding="utf-8")


if __name__ == "__main__":
    main()
