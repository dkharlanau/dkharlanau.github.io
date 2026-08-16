#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def bump_patch(version: str) -> str:
    parts = version.split(".")
    if len(parts) == 3 and all(part.isdigit() for part in parts):
        parts[2] = str(int(parts[2]) + 1)
        return ".".join(parts)
    return version


def patch_catalog() -> None:
    path = DATA / "catalog.json"
    value = load(path)
    tools = value.setdefault("authoring_tools", [])
    if not any(item.get("id") == "reasoning-gap-review" for item in tools):
        tools.append({
            "id": "reasoning-gap-review",
            "label": "Reasoning Gap Review",
            "route": "/labs/assessment/reasoning-gaps/",
            "purpose": "Create review-stage Design and Challenge candidates only for thin published reasoning cells, using alternatives, trade-offs, decision-changing conditions, and source-supported evidence routes."
        })
        value["version"] = bump_patch(str(value.get("version", "1.0.0")))
        value["updated_at"] = "2026-08-16"
        dump(path, value)


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-045" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-045",
            "priority": "P1",
            "title": "Non-diagnostic reasoning-gap authoring contract",
            "status": "done",
            "outputs": [
                "/labs/assessment/reasoning-gaps/",
                "/labs/assessment/data/reasoning-gap-candidates.json",
                "scripts/validate_assessment_reasoning_gap_candidates.py"
            ],
            "working_rule": "Do not force Design and Challenge gaps through a symptom-to-root-cause generator. Require explicit alternatives, ownership, trade-offs, decision-changing conditions, and source-supported evidence routes while keeping all candidates outside the published manifest."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "non-diagnostic authoring" not in theme and "Sales Design and AI/Data Challenge" not in theme]
        themes.insert(0, "run semantic novelty review on the two new Design and Challenge reasoning-gap candidates before any promotion decision")
        themes.insert(1, "prepare one human promotion review packet for the surviving reasoning-gap signals without publishing them automatically")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"reasoning-gaps": ASSESSMENT / "reasoning-gaps" / "index.html",' not in text:
        text = text.replace(
            '        "reasoning-coverage": ASSESSMENT / "reasoning-coverage" / "index.html",\n',
            '        "reasoning-coverage": ASSESSMENT / "reasoning-coverage" / "index.html",\n        "reasoning-gaps": ASSESSMENT / "reasoning-gaps" / "index.html",\n'
        )
    if 'assert authoring["reasoning-gap-review"]["route"]' not in text:
        text = text.replace(
            '    assert authoring["reasoning-coverage"]["route"] == "/labs/assessment/reasoning-coverage/"\n',
            '    assert authoring["reasoning-coverage"]["route"] == "/labs/assessment/reasoning-coverage/"\n    assert authoring["reasoning-gap-review"]["route"] == "/labs/assessment/reasoning-gaps/"\n'
        )
    if '"LOOP-045"' not in text:
        candidates = [
            ('"LOOP-043", "LOOP-044"):', '"LOOP-043", "LOOP-044", "LOOP-045"):'),
            ('"LOOP-042", "LOOP-043", "LOOP-044"):', '"LOOP-042", "LOOP-043", "LOOP-044", "LOOP-045"):')
        ]
        for old, new in candidates:
            if old in text:
                text = text.replace(old, new, 1)
                break
    marker = "\ndef test_non_diagnostic_reasoning_gap_candidates_match_thin_cells_and_stay_unpublished() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_non_diagnostic_reasoning_gap_candidates_match_thin_cells_and_stay_unpublished() -> None:\n    gaps = load_json("reasoning-gap-candidates.json")\n    coverage = load_json("reasoning-pressure-coverage.json")\n    manifest = load_json("case-sets.json")\n\n    expected = {(item["track"], item["level"]) for item in coverage["authoring_gaps"]}\n    actual = {(item["track"], item["level"]) for item in gaps["gap_plan"]}\n    assert actual == expected\n    assert gaps["summary"]["published_cases_changed"] == 0\n    assert gaps["summary"]["new_review_candidates"] == 2\n    assert {item["level"] for item in gaps["candidates"]} == {"design", "challenge"}\n    published_ids = set()\n    for case_set in manifest["sets"]:\n        published_ids.update(item["id"] for item in load_jsonl(ROOT / case_set["url"].lstrip("/")))\n    assert not published_ids & {item["id"] for item in gaps["candidates"]}\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_reasoning_gap_candidates.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_catalog()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
