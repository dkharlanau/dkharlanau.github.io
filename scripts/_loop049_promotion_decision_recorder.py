#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "promotion-review" / "index.html"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-049 marker not found: {label}")
    return text.replace(old, new, 1)


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    if '/labs/assessment/promotion-review/decision/' not in text:
        old = '''    <a href="/labs/assessment/data/promotion-review-packet.json">Open promotion packet JSON <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>'''
        new = '''    <div class="research-route-list">\n      <a href="/labs/assessment/data/promotion-review-packet.json"><span>DATA</span><strong>Promotion Packet JSON</strong><small>Every semantic-surviving candidate, evidence boundary, closest published cases, and pending human state.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>\n      <a href="/labs/assessment/promotion-review/decision/"><span>HUMAN</span><strong>Record Promotion Decision</strong><small>Export an explicit approve-for-separate-change, revise, or reject decision. The recorder cannot publish a case.</small><i class="material-symbols-outlined" aria-hidden="true">rate_review</i></a>\n    </div>'''
        text = replace_once(text, old, new, "decision recorder link")
    PAGE.write_text(text, encoding="utf-8")


def patch_catalog() -> None:
    path = DATA / "catalog.json"
    value = load(path)
    tools = value.setdefault("authoring_tools", [])
    if not any(item.get("id") == "promotion-decision" for item in tools):
        tools.append({
            "id": "promotion-decision",
            "label": "Promotion Decision Record",
            "route": "/labs/assessment/promotion-review/decision/",
            "purpose": "Export an explicit human approve-for-separate-change, revise, or reject decision for one promotion candidate without editing the published case manifest."
        })
        parts = str(value.get("version", "1.0.0")).split(".")
        if len(parts) == 3 and all(part.isdigit() for part in parts):
            parts[2] = str(int(parts[2]) + 1)
            value["version"] = ".".join(parts)
        value["updated_at"] = "2026-08-16"
        dump(path, value)


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-049" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-049",
            "priority": "P1",
            "title": "Export-only human promotion decision record",
            "status": "done",
            "outputs": [
                "/labs/assessment/promotion-review/decision/",
                "/labs/assessment/data/promotion-decision-schema.json",
                "scripts/validate_assessment_promotion_decision_recorder.py"
            ],
            "working_rule": "A human may explicitly approve a candidate only for a separate reviewed repository change. The decision recorder exports evidence and structurally forbids case-manifest, publication, or calibration changes."
        })
        value["updated_at"] = "2026-08-16"
        value["next_iteration_themes"] = [
            "use real exported human promotion decisions as evidence for future reviewed repository changes; never infer approval from the packet itself",
            "use real Board Mode and assessment attempt history to decide whether reasoning-pressure thresholds need calibration",
            "continue page-level human review only where the current queue still contains unverified source-supported routes"
        ]
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"promotion-decision": ASSESSMENT / "promotion-review" / "decision" / "index.html",' not in text:
        text = text.replace(
            '        "promotion-review": ASSESSMENT / "promotion-review" / "index.html",\n',
            '        "promotion-review": ASSESSMENT / "promotion-review" / "index.html",\n        "promotion-decision": ASSESSMENT / "promotion-review" / "decision" / "index.html",\n'
        )
    if 'assert authoring["promotion-decision"]["route"]' not in text:
        text = text.replace(
            '    assert authoring["promotion-review"]["route"] == "/labs/assessment/promotion-review/"\n',
            '    assert authoring["promotion-review"]["route"] == "/labs/assessment/promotion-review/"\n    assert authoring["promotion-decision"]["route"] == "/labs/assessment/promotion-review/decision/"\n'
        )
    if '"LOOP-049"' not in text:
        for old, new in [
            ('"LOOP-047", "LOOP-048"):', '"LOOP-047", "LOOP-048", "LOOP-049"):'),
            ('"LOOP-046", "LOOP-047", "LOOP-048"):', '"LOOP-046", "LOOP-047", "LOOP-048", "LOOP-049"):')
        ]:
            if old in text:
                text = text.replace(old, new, 1)
                break
    marker = "\ndef test_promotion_decision_record_is_human_explicit_and_non_publishing() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_promotion_decision_record_is_human_explicit_and_non_publishing() -> None:\n    schema = load_json("promotion-decision-schema.json")\n    effects = schema["properties"]["publication_effect"]["properties"]\n    assert effects["case_manifest_changed"]["const"] is False\n    assert effects["case_published"]["const"] is False\n    assert effects["calibration_changed"]["const"] is False\n    assert schema["properties"]["review_checks"]["minItems"] == 6\n    assert schema["properties"]["review_checks"]["maxItems"] == 6\n    assert set(schema["properties"]["decision"]["enum"]) == {\n        "approve_for_separate_repository_change", "revise_before_promotion", "reject_candidate"\n    }\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_promotion_decision_recorder.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_page()
    patch_catalog()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
