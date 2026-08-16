#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "human-review" / "index.html"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-040 patch marker not found: {label}")
    return text.replace(old, new, 1)


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    if '/labs/assessment/human-review/secondary/' not in text:
        old = '''      <a href="/labs/assessment/human-review/findings/"><span>FIND</span><strong>Review Finding Recorder</strong><small>Record a real page review against all seven gates and export a portable finding without changing verification or indexing.</small><i class="material-symbols-outlined" aria-hidden="true">rate_review</i></a>\n      <a href="/labs/assessment/data/human-review-finding-schema.json"><span>SCHEMA</span>'''
        new = '''      <a href="/labs/assessment/human-review/findings/"><span>FIND</span><strong>Review Finding Recorder</strong><small>Record a real page review against all seven gates and export a portable finding without changing verification or indexing.</small><i class="material-symbols-outlined" aria-hidden="true">rate_review</i></a>\n      <a href="/labs/assessment/human-review/secondary/"><span>NEXT</span><strong>Secondary Review Priority</strong><small>Rank the 14 routes after Core 12 by direct case reuse, cross-track value, and source-supported claim depth.</small><i class="material-symbols-outlined" aria-hidden="true">sort</i></a>\n      <a href="/labs/assessment/data/human-review-finding-schema.json"><span>SCHEMA</span>'''
        text = replace_once(text, old, new, "secondary review link")
    PAGE.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-040" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-040",
            "priority": "P1",
            "title": "Secondary human-review priority map",
            "status": "done",
            "outputs": [
                "/labs/assessment/human-review/secondary/",
                "/labs/assessment/data/secondary-review-priority.json",
                "scripts/generate_assessment_secondary_review_priority.py",
                "scripts/validate_assessment_secondary_review_priority.py"
            ],
            "working_rule": "After the Core 12 wave, rank source-supported secondary pages by direct published-case reuse and cross-track assessment value. Priority orders review work only and never changes verification or publication state."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "rank secondary P1 human-review routes" not in theme]
        themes.insert(0, "use the secondary review ranking to select the next high-reuse editorial consistency pass without pretending it is human verification")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"human-review-secondary": ASSESSMENT / "human-review" / "secondary" / "index.html",' not in text:
        text = text.replace(
            '        "human-review-findings": ASSESSMENT / "human-review" / "findings" / "index.html",\n',
            '        "human-review-findings": ASSESSMENT / "human-review" / "findings" / "index.html",\n        "human-review-secondary": ASSESSMENT / "human-review" / "secondary" / "index.html",\n'
        )
    if '"LOOP-040"' not in text:
        text = text.replace('"LOOP-038", "LOOP-039"):', '"LOOP-038", "LOOP-039", "LOOP-040"):')
    marker = "\ndef test_secondary_human_review_priority_ranks_only_source_supported_non_core_routes() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_secondary_human_review_priority_ranks_only_source_supported_non_core_routes() -> None:\n    priority = load_json("secondary-review-priority.json")\n    queue = load_json("human-review-queue.json")\n    core = load_json("core-study-map.json")\n    secondary = {item["route"] for item in queue["items"] if item["wave"] == "secondary"}\n    core_routes = {item["route"] for item in core["items"]}\n    ranked = {item["route"] for item in priority["items"]}\n\n    assert ranked == secondary\n    assert not ranked & core_routes\n    assert priority["summary"]["all_source_supported"] is True\n    assert priority["summary"]["all_unverified"] is True\n    assert priority["summary"]["secondary_routes"] == len(priority["items"])\n    assert all(item["page_verified"] is False for item in priority["items"])\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_secondary_review_priority.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_page()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
