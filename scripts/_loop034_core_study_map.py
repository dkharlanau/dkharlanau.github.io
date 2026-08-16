#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload) -> None:
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing patch anchor: {label}")
    return text.replace(old, new, 1)


catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.13.0"
catalog["purpose"] = (
    "Turn the Lab into a structured SAP Lead assessment route across process knowledge, diagnostics, architecture, integration, data, AI, "
    "adaptive practice, feedback, evidence-backed question authoring, promotion readiness, claim-level primary-source review, human page review, and a Core 12 study sequence."
)
authoring = catalog.setdefault("authoring_tools", [])
if not any(item.get("id") == "core-study" for item in authoring):
    authoring.append({
        "id": "core-study",
        "label": "Core 12 Study Map",
        "route": "/labs/assessment/core/",
        "purpose": "Organize the twelve highest-value Lead routes into decision, execution/state, and governance/value waves with one reasoning contract."
    })
strong = catalog.setdefault("coverage", {}).setdefault("strong_now", [])
marker = "Core 12 study map connects the first assessment wave to ownership boundaries, answer paths, source-review state, and direct published practice cases"
if marker not in strong:
    strong.append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review the three new Production question candidates and promote only clearly non-duplicate Lead cases",
    "capture true page-level human review separately from automated editorial improvement",
    "add cross-route Core 12 drills that force ownership changes between adjacent domains",
    "select secondary P1 pages by cross-track assessment value rather than page count"
]
endpoints = catalog.setdefault("endpoints", {})
endpoints["core_study_route"] = "/labs/assessment/core/"
endpoints["core_study_contract"] = "/labs/assessment/data/core-study-contract.json"
endpoints["core_study_map"] = "/labs/assessment/data/core-study-map.json"
write_json(catalog_path, catalog)

backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-034" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-034",
        "priority": "P1",
        "title": "Core 12 assessment study map",
        "status": "done",
        "outputs": [
            "/labs/assessment/core/",
            "/labs/assessment/data/core-study-contract.json",
            "/labs/assessment/data/core-study-map.json",
            "scripts/generate_assessment_core_study_map.py"
        ],
        "working_rule": "Study the core routes as ownership and diagnostic chains. Enrich the qualitative contract from factual-review and published-case data without changing verification or publication state."
    })
backlog["next_iteration_themes"] = [
    "review the three new Production question candidates and promote only non-duplicate Lead cases through an explicit reviewed change",
    "add cross-route Core 12 drills that force the learner to cross an ownership boundary",
    "record true human page-review findings separately from automated editorial improvement",
    "select secondary P1 pages by cross-track assessment value instead of processing all routes mechanically"
]
write_json(backlog_path, backlog)

index_path = ROOT / "labs" / "assessment" / "index.md"
index = index_path.read_text(encoding="utf-8")
anchor = '      <a href="/labs/assessment/human-review/"><span>HUMAN</span><strong>Human Review Queue</strong><small>Read source-supported P1 pages end to end before any verification or publication decision.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>\n'
if '/labs/assessment/core/' not in index:
    index = replace_once(
        index,
        anchor,
        anchor + '      <a href="/labs/assessment/core/"><span>CORE</span><strong>Core 12 Study Map</strong><small>Study decisions, execution/state, governance and value as one Lead reasoning route.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>\n',
        "assessment core route link"
    )
index_path.write_text(index, encoding="utf-8")

test_path = ROOT / "tests" / "test_assessment_practice_layer.py"
test = test_path.read_text(encoding="utf-8")
if '"core-study": ASSESSMENT / "core" / "index.html",' not in test:
    test = test.replace(
        '        "human-review": ASSESSMENT / "human-review" / "index.html",\n',
        '        "human-review": ASSESSMENT / "human-review" / "index.html",\n        "core-study": ASSESSMENT / "core" / "index.html",\n',
    )
if 'assert authoring["core-study"]["route"]' not in test:
    test = test.replace(
        '    assert authoring["human-review"]["route"] == "/labs/assessment/human-review/"\n',
        '    assert authoring["human-review"]["route"] == "/labs/assessment/human-review/"\n    assert authoring["core-study"]["route"] == "/labs/assessment/core/"\n',
    )
test = test.replace(
    '"LOOP-031", "LOOP-032", "LOOP-033"):',
    '"LOOP-031", "LOOP-032", "LOOP-033", "LOOP-034"):',
)
core_test = '''\n\ndef test_core_study_map_is_reproducible_and_non_publishing() -> None:\n    contract = load_json("core-study-contract.json")\n    study = load_json("core-study-map.json")\n    assert study["summary"]["core_routes"] == len(contract["routes"]) == 12\n    assert study["summary"]["waves"] == len(contract["waves"]) == 3\n    assert study["summary"]["source_supported_routes"] == 12\n    assert study["summary"]["page_verified_routes"] == 0\n    assert [item["order"] for item in study["items"]] == list(range(1, 13))\n    assert all(item["evidence"]["human_verification_required"] for item in study["items"])\n    assert all(item["assessment_question"] and item["ownership_boundary"] for item in study["items"])\n    assert all(len(item["answer_path"]) >= 7 for item in study["items"])\n\n    result = subprocess.run(\n        [sys.executable, "scripts/generate_assessment_core_study_map.py", "--check"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
if 'def test_core_study_map_is_reproducible_and_non_publishing()' not in test:
    test += core_test
test_path.write_text(test, encoding="utf-8")

print("LOOP-034 Core 12 integration applied")
