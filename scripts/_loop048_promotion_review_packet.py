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
    if not any(item.get("id") == "promotion-review" for item in tools):
        tools.append({
            "id": "promotion-review",
            "label": "Candidate Promotion Review",
            "route": "/labs/assessment/promotion-review/",
            "purpose": "Present every semantic-surviving generated and reasoning-gap candidate in one human review packet before any published-case change."
        })
        value["version"] = bump_patch(str(value.get("version", "1.0.0")))
        value["updated_at"] = "2026-08-16"
        dump(path, value)


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-048" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-048",
            "priority": "P1",
            "title": "Unified candidate promotion review packet",
            "status": "done",
            "outputs": [
                "/labs/assessment/promotion-review/",
                "/labs/assessment/data/promotion-review-packet.json",
                "scripts/generate_assessment_promotion_review_packet.py",
                "scripts/validate_assessment_promotion_review_packet.py"
            ],
            "working_rule": "Combine every semantic-surviving candidate in one read-only human review packet. Keep every human decision pending and require a separate explicit reviewed change before any candidate enters the published case manifest."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "human promotion review packet" not in theme and "promotion packet" not in theme]
        themes.insert(0, "add an export-only human promotion decision record for approve, revise, or reject without writing the published manifest automatically")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"promotion-review": ASSESSMENT / "promotion-review" / "index.html",' not in text:
        text = text.replace(
            '        "reasoning-gaps": ASSESSMENT / "reasoning-gaps" / "index.html",\n',
            '        "reasoning-gaps": ASSESSMENT / "reasoning-gaps" / "index.html",\n        "promotion-review": ASSESSMENT / "promotion-review" / "index.html",\n'
        )
    if 'assert authoring["promotion-review"]["route"]' not in text:
        text = text.replace(
            '    assert authoring["reasoning-gap-review"]["route"] == "/labs/assessment/reasoning-gaps/"\n',
            '    assert authoring["reasoning-gap-review"]["route"] == "/labs/assessment/reasoning-gaps/"\n    assert authoring["promotion-review"]["route"] == "/labs/assessment/promotion-review/"\n'
        )
    if '"LOOP-048"' not in text:
        for old, new in [
            ('"LOOP-046", "LOOP-047"):', '"LOOP-046", "LOOP-047", "LOOP-048"):'),
            ('"LOOP-045", "LOOP-046", "LOOP-047"):', '"LOOP-045", "LOOP-046", "LOOP-047", "LOOP-048"):')
        ]:
            if old in text:
                text = text.replace(old, new, 1)
                break
    marker = "\ndef test_promotion_review_packet_contains_only_semantic_survivors_and_zero_approvals() -> None:\n"
    if marker not in text:
        text += '''\n\ndef test_promotion_review_packet_contains_only_semantic_survivors_and_zero_approvals() -> None:\n    packet = load_json("promotion-review-packet.json")\n    generated_review = load_json("candidate-semantic-review.json")\n    gap_review = load_json("reasoning-gap-semantic-review.json")\n    expected = {item["candidate_id"] for item in generated_review["decisions"] if item["recommendation"] == "retain_for_human_promotion_review"}\n    expected |= {item["candidate_id"] for item in gap_review["decisions"] if item["recommendation"] == "retain_for_human_promotion_review"}\n    assert {item["candidate_id"] for item in packet["items"]} == expected\n    assert packet["summary"]["pending_candidates"] == len(expected)\n    assert packet["summary"]["approved_candidates"] == 0\n    assert all(item["human_decision"]["status"] == "pending_human_review" for item in packet["items"])\n    assert all(item["human_decision"]["decision"] is None for item in packet["items"])\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_promotion_review_packet.py"],\n        cwd=ROOT, text=True, capture_output=True, check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_catalog()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
