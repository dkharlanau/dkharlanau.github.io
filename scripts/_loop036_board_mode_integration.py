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


catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.15.0"
practice = catalog.setdefault("practice_modes", [])
if not any(item.get("id") == "board" for item in practice):
    practice.append({
        "id": "board",
        "label": "Board Mode",
        "route": "/labs/assessment/board/",
        "purpose": "Run timed oral ownership-boundary drills with the shared seven-dimension scoring contract and no automatic history write."
    })
strong = catalog.setdefault("coverage", {}).setdefault("strong_now", [])
marker = "Board Mode turns Core 12 boundary drills into timed oral practice using the same 21-point assessment scoring contract"
if marker not in strong:
    strong.append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "use Board Mode to expose weak ownership, evidence, and trade-off dimensions before expanding the question corpus",
    "review the three new Production question candidates and promote only clearly non-duplicate Lead cases",
    "connect Board Mode to persistent history only through the existing attempt schema if durable tracking becomes useful",
    "record true page-level human review separately from automated editorial improvement"
]
endpoints = catalog.setdefault("endpoints", {})
endpoints["board_mode_route"] = "/labs/assessment/board/"
endpoints["board_mode_contract"] = "/labs/assessment/data/board-mode.json"
write_json(catalog_path, catalog)


backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-036" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-036",
        "priority": "P1",
        "title": "Timed Core 12 Board Mode",
        "status": "done",
        "outputs": [
            "/labs/assessment/board/",
            "/labs/assessment/data/board-mode.json",
            "scripts/validate_assessment_board_mode.py"
        ],
        "working_rule": "Use the existing Core boundary drills and shared scoring contract for timed oral practice. Do not create a second history format or publish practice data automatically."
    })
backlog["next_iteration_themes"] = [
    "review the three new Production candidates and promote only a clearly non-duplicate case through an explicit reviewed change",
    "add a Board Mode review handoff that points low scoring dimensions to existing review-map routes without writing history",
    "record true human page-review findings separately from automated editorial improvement",
    "select secondary P1 pages by cross-track assessment value instead of processing all routes mechanically"
]
write_json(backlog_path, backlog)


# Assessment landing page.
index_path = ROOT / "labs" / "assessment" / "index.md"
index = index_path.read_text(encoding="utf-8")
board_link = '      <a href="/labs/assessment/board/"><span>BOARD</span><strong>Board Mode</strong><small>Four timed oral cross-route drills with the shared 21-point Lead scoring model.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>\n'
anchor = '      <a href="/labs/assessment/core-boundaries/"><span>X</span><strong>Core Boundary Drills</strong><small>Cross-route oral practice for ownership changes and end-to-end completion proof.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>\n'
if '/labs/assessment/board/' not in index and anchor in index:
    index = index.replace(anchor, anchor + board_link, 1)
if '/labs/assessment/data/board-mode.json' not in index:
    data_anchor = '      <a href="/labs/assessment/data/core-boundary-drills.json"><span>X</span><strong>Core Boundary Drill Dataset</strong><small>Eight synthetic cross-route drills for ownership and completion reasoning; never auto-published.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>\n'
    if data_anchor in index:
        index = index.replace(
            data_anchor,
            data_anchor + '      <a href="/labs/assessment/data/board-mode.json"><span>BOARD</span><strong>Board Mode Contract</strong><small>Four rounds, six minutes per round, reveal policy, shared scoring, and browser-only session boundary.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a>\n',
            1,
        )
index_path.write_text(index, encoding="utf-8")


# Boundary drill page: make Board Mode the timed continuation.
boundary_page = ROOT / "labs" / "assessment" / "core-boundaries" / "index.html"
text = boundary_page.read_text(encoding="utf-8")
anchor_section = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">policy</span>\n    <p><strong>Publication boundary:</strong> these eight drills are synthetic authored practice. They are not part of <code>case-sets.json</code>, do not change the 59 published cases, and do not make any Core 12 page verified.</p>\n    <a href="/labs/assessment/core/">Back to Core 12 Study Map <span class="material-symbols-outlined" aria-hidden="true">route</span></a>\n  </section>\n'''
board_section = '''  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Timed practice</p><h2>Use the same drills under pressure.</h2><p>Board Mode selects four drills without replacement, gives six minutes per round, hides the reasoning path, and scores the answer on the shared seven dimensions.</p></header>\n    <div class="research-route-list"><a href="/labs/assessment/board/"><span>6:00</span><strong>Open Board Mode</strong><small>Scenario → oral answer → optional boundary hint → reasoning reveal → 21-point self-score.</small><i class="material-symbols-outlined" aria-hidden="true">timer</i></a></div>\n  </section>\n\n'''
if '/labs/assessment/board/' not in text:
    text = text.replace(anchor_section, board_section + anchor_section, 1)
boundary_page.write_text(text, encoding="utf-8")


# Tests.
test_path = ROOT / "tests" / "test_assessment_practice_layer.py"
test = test_path.read_text(encoding="utf-8")
if '"board": ASSESSMENT / "board" / "index.html",' not in test:
    test = test.replace(
        '        "core-boundaries": ASSESSMENT / "core-boundaries" / "index.html",\n',
        '        "core-boundaries": ASSESSMENT / "core-boundaries" / "index.html",\n        "board": ASSESSMENT / "board" / "index.html",\n',
        1,
    )
test = test.replace(
    'assert set(modes) == {"adaptive", "mock", "review", "progress", "feedback", "cross-process"}',
    'assert set(modes) == {"adaptive", "mock", "review", "progress", "feedback", "cross-process", "board"}',
)
if 'assert modes["board"]["route"]' not in test:
    test = test.replace(
        '    assert modes["feedback"]["route"] == "/labs/assessment/feedback/"\n',
        '    assert modes["feedback"]["route"] == "/labs/assessment/feedback/"\n    assert modes["board"]["route"] == "/labs/assessment/board/"\n',
        1,
    )
test = test.replace(
    '"LOOP-033", "LOOP-034", "LOOP-035"):',
    '"LOOP-033", "LOOP-034", "LOOP-035", "LOOP-036"):',
)
board_test = '''\n\ndef test_board_mode_reuses_shared_scoring_without_second_history_store() -> None:\n    board = load_json("board-mode.json")\n    scoring = load_json("scoring.json")\n    drills = load_json("core-boundary-drills.json")\n    page = (ASSESSMENT / "board" / "index.html").read_text(encoding="utf-8")\n\n    assert board["scoring_contract"] == "/labs/assessment/data/scoring.json"\n    assert board["drill_source"] == "/labs/assessment/data/core-boundary-drills.json"\n    assert board["default_session"]["rounds"] <= len(drills["drills"])\n    assert board["scoring"]["dimensions"] == [item["id"] for item in scoring["dimensions"]]\n    assert board["scoring"]["maximum_score"] == scoring["maximum_score"] == 21\n    assert board["scoring"]["lead_signal_minimum"] == scoring["lead_signal_minimum"]\n    assert "localStorage" not in page\n    assert "verified: false" in page\n    assert "robots: noindex,follow" in page\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_board_mode.py"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
if 'def test_board_mode_reuses_shared_scoring_without_second_history_store()' not in test:
    test += board_test
test_path.write_text(test, encoding="utf-8")

print("LOOP-036 Board Mode integration applied")
