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
        raise SystemExit(f"LOOP-039 patch marker not found: {label}")
    return text.replace(old, new, 1)


def patch_human_review_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    if '/labs/assessment/human-review/findings/' not in text:
        old = '''      <a href="/labs/assessment/data/human-review-policy.json"><span>POLICY</span><strong>Human Review Policy</strong><small>Eligibility, review gates, priority rule, completion rule, and publication boundary.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>\n      <a href="/labs/assessment/promotion-readiness/"><span>INPUT</span>'''
        new = '''      <a href="/labs/assessment/data/human-review-policy.json"><span>POLICY</span><strong>Human Review Policy</strong><small>Eligibility, review gates, priority rule, completion rule, and publication boundary.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>\n      <a href="/labs/assessment/human-review/findings/"><span>FIND</span><strong>Review Finding Recorder</strong><small>Record a real page review against all seven gates and export a portable finding without changing verification or indexing.</small><i class="material-symbols-outlined" aria-hidden="true">rate_review</i></a>\n      <a href="/labs/assessment/data/human-review-finding-schema.json"><span>SCHEMA</span><strong>Finding Schema</strong><small>Structured gate results, findings, disposition, claim scope, and zero automatic publication effects.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>\n      <a href="/labs/assessment/promotion-readiness/"><span>INPUT</span>'''
        text = replace_once(text, old, new, "findings links")
    PAGE.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-039" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-039",
            "priority": "P1",
            "title": "Human page-review finding contract",
            "status": "done",
            "outputs": [
                "/labs/assessment/human-review/findings/",
                "/labs/assessment/data/human-review-finding-schema.json",
                "/labs/assessment/data/human-review-policy.json",
                "scripts/validate_assessment_human_review_findings.py"
            ],
            "working_rule": "Record true reviewer evidence through all seven page-review gates. Never infer human verification from automation, and never alter verified, indexing, status, or publication state from the finding recorder."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "human page-review findings contract" not in theme]
        themes.insert(0, "rank secondary P1 human-review routes by cross-track assessment value and direct published-case reuse")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"human-review-findings": ASSESSMENT / "human-review" / "findings" / "index.html",' not in text:
        text = text.replace(
            '        "human-review": ASSESSMENT / "human-review" / "index.html",\n',
            '        "human-review": ASSESSMENT / "human-review" / "index.html",\n        "human-review-findings": ASSESSMENT / "human-review" / "findings" / "index.html",\n'
        )
    if '"LOOP-039"' not in text:
        text = text.replace('"LOOP-037", "LOOP-038"):', '"LOOP-037", "LOOP-038", "LOOP-039"):')
    marker = "\ndef test_human_review_finding_contract_never_changes_publication_state() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_human_review_finding_contract_never_changes_publication_state() -> None:\n    policy = load_json("human-review-policy.json")\n    schema = load_json("human-review-finding-schema.json")\n    publication = schema["properties"]["publication_effect"]["properties"]\n\n    assert policy["finding_contract"] == "/labs/assessment/data/human-review-finding-schema.json"\n    assert policy["findings_route"] == "/labs/assessment/human-review/findings/"\n    assert len(policy["review_gates"]) == 7\n    assert schema["properties"]["gate_results"]["minItems"] == 7\n    assert schema["properties"]["gate_results"]["maxItems"] == 7\n    assert publication["verified_changed"]["const"] is False\n    assert publication["indexing_changed"]["const"] is False\n    assert publication["status_changed"]["const"] is False\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_human_review_findings.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_human_review_page()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
