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
    if not any(item.get("id") == "reasoning-coverage" for item in tools):
        tools.append({
            "id": "reasoning-coverage",
            "label": "Reasoning Coverage",
            "route": "/labs/assessment/reasoning-coverage/",
            "purpose": "Measure exact published-case pressure by track and reasoning level, with explicit Diagnose, Design, and Challenge authoring gaps."
        })
        value["version"] = bump_patch(str(value.get("version", "1.0.0")))
        value["updated_at"] = "2026-08-16"
        dump(path, value)


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-042" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-042",
            "priority": "P1",
            "title": "Published-case reasoning pressure coverage",
            "status": "done",
            "outputs": [
                "/labs/assessment/reasoning-coverage/",
                "/labs/assessment/data/reasoning-pressure-coverage.json",
                "scripts/generate_assessment_reasoning_coverage.py",
                "scripts/validate_assessment_reasoning_coverage.py"
            ],
            "working_rule": "Use exact case track and reasoning-level metadata to identify thin Diagnose, Design, and Challenge cells. Treat the two-case threshold as an explicit authoring heuristic, not a scoring or factual claim."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "measure published-case reasoning coverage" not in theme]
        themes.insert(0, "use reasoning-pressure gaps to select evidence-backed candidate seeds only where the corpus is thin and the case adds semantic novelty")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"reasoning-coverage": ASSESSMENT / "reasoning-coverage" / "index.html",' not in text:
        text = text.replace(
            '        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",\n',
            '        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",\n        "reasoning-coverage": ASSESSMENT / "reasoning-coverage" / "index.html",\n'
        )
    if 'assert authoring["reasoning-coverage"]["route"]' not in text:
        text = text.replace(
            '    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"\n',
            '    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"\n    assert authoring["reasoning-coverage"]["route"] == "/labs/assessment/reasoning-coverage/"\n'
        )
    if '"LOOP-042"' not in text:
        text = text.replace('"LOOP-040", "LOOP-041"):', '"LOOP-040", "LOOP-041", "LOOP-042"):')
    marker = "\ndef test_reasoning_pressure_coverage_matches_published_case_metadata() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_reasoning_pressure_coverage_matches_published_case_metadata() -> None:\n    coverage = load_json("reasoning-pressure-coverage.json")\n    manifest = load_json("case-sets.json")\n    catalog = load_json("catalog.json")\n\n    assert coverage["summary"]["published_cases"] == manifest["total_cases"]\n    assert {item["track"] for item in coverage["tracks"]} == {item["id"] for item in catalog["tracks"]}\n    assert coverage["policy"]["lead_pressure_levels"] == ["diagnose", "design", "challenge"]\n    assert coverage["policy"]["minimum_published_cases_per_lead_pressure_level"] == 2\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_reasoning_coverage.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_catalog()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
