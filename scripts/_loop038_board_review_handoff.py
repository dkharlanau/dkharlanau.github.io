#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "board" / "index.html"
TESTS = ROOT / "tests" / "test_assessment_practice_layer.py"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def dump(path: Path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"LOOP-038 patch marker not found: {label}")
    return text.replace(old, new, 1)


def patch_page() -> None:
    text = PAGE.read_text(encoding="utf-8")
    if 'id="board-review-handoff"' not in text:
        old = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">policy</span>'''
        new = '''  <section class="research-canvas__inventory" id="board-review-handoff" data-reveal>\n    <header><p class="research-canvas__eyebrow">Targeted review handoff</p><h2>Use the weakest dimensions, not the loudest mistake.</h2><p>After a scored round, Board Mode averages each scoring dimension in the current session and points the two weakest dimensions to focused routes from the shared Review Map.</p></header>\n    <p id="board-review-status">Complete and score at least one round to build a review handoff.</p>\n    <div class="research-route-list" id="board-review-list"></div>\n    <p class="ecg-caption">This recommendation exists only in the current page session. It does not write assessment history or change calibration.</p>\n    <a href="/labs/assessment/data/review-map.json">Open shared Review Map <span class="material-symbols-outlined" aria-hidden="true">data_object</span></a>\n  </section>\n\n  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">policy</span>'''
        text = replace_once(text, old, new, "review handoff section")

    if "reviewMap: null" not in text:
        text = replace_once(
            text,
            "    contract: null,\n    session: [],\n    roundIndex: -1,\n    scores: [],",
            "    contract: null,\n    reviewMap: null,\n    session: [],\n    roundIndex: -1,\n    scores: [],\n    dimensionScores: [],",
            "state review fields",
        )

    if "function renderReviewHandoff()" not in text:
        marker = '''  function commitRoundScore() {\n    const selects = Array.from(document.querySelectorAll('#board-score-grid select'));'''
        function = '''  function renderReviewHandoff() {\n    const container = $('board-review-list');\n    const status = $('board-review-status');\n    if (!container || !status || !state.scoring || !state.reviewMap) return;\n    const completed = state.dimensionScores.filter(Boolean);\n    container.replaceChildren();\n    if (!completed.length) {\n      status.textContent = 'Complete and score at least one round to build a review handoff.';\n      return;\n    }\n\n    const ranked = state.scoring.dimensions.map(dimension => {\n      const values = completed.map(item => item[dimension.id]).filter(value => Number.isFinite(value));\n      const average = values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : 0;\n      return {id: dimension.id, label: dimension.label, average};\n    }).sort((left, right) => left.average - right.average || left.label.localeCompare(right.label)).slice(0, 2);\n\n    status.textContent = `Current-session review focus after ${completed.length} scored round${completed.length === 1 ? '' : 's'}.`;\n    ranked.forEach(item => {\n      const mapping = state.reviewMap.dimension_routes[item.id];\n      if (!mapping || !mapping.routes || !mapping.routes.length) return;\n      const route = mapping.routes[0];\n      const link = document.createElement('a');\n      link.href = route.url;\n      const score = document.createElement('span');\n      score.textContent = item.average.toFixed(1);\n      const title = document.createElement('strong');\n      title.textContent = `${item.label}: ${mapping.review_question}`;\n      const detail = document.createElement('small');\n      detail.textContent = `${route.label} · ${route.why}`;\n      const icon = document.createElement('i');\n      icon.className = 'material-symbols-outlined';\n      icon.setAttribute('aria-hidden', 'true');\n      icon.textContent = 'target';\n      link.append(score, title, detail, icon);\n      container.appendChild(link);\n    });\n  }\n\n  function commitRoundScore() {\n    const selects = Array.from(document.querySelectorAll('#board-score-grid select'));'''
        text = replace_once(text, marker, function, "renderReviewHandoff function")

    if "state.dimensionScores[state.roundIndex]" not in text:
        old = '''    const total = selects.reduce((sum, select) => sum + Number(select.value), 0);\n    state.scores[state.roundIndex] = total;\n    const completed = state.scores.filter(value => Number.isFinite(value));'''
        new = '''    const total = selects.reduce((sum, select) => sum + Number(select.value), 0);\n    state.scores[state.roundIndex] = total;\n    const dimensionScore = {};\n    selects.forEach(select => { dimensionScore[select.dataset.dimension] = Number(select.value); });\n    state.dimensionScores[state.roundIndex] = dimensionScore;\n    const completed = state.scores.filter(value => Number.isFinite(value));'''
        text = replace_once(text, old, new, "capture dimension scores")
        text = replace_once(
            text,
            "    $('board-lead-rounds').textContent = String(completed.filter(value => value >= state.scoring.lead_signal_minimum).length);\n  }",
            "    $('board-lead-rounds').textContent = String(completed.filter(value => value >= state.scoring.lead_signal_minimum).length);\n    renderReviewHandoff();\n  }",
            "render handoff after score",
        )

    if "state.dimensionScores = [];" not in text:
        text = replace_once(
            text,
            "    state.roundIndex = 0;\n    state.scores = [];\n    $('board-average').textContent = '—';",
            "    state.roundIndex = 0;\n    state.scores = [];\n    state.dimensionScores = [];\n    $('board-average').textContent = '—';",
            "reset dimension scores",
        )
        text = replace_once(
            text,
            "    $('board-lead-rounds').textContent = '0';\n    renderRound();",
            "    $('board-lead-rounds').textContent = '0';\n    renderReviewHandoff();\n    renderRound();",
            "reset handoff display",
        )

    if "fetch('/labs/assessment/data/review-map.json'" not in text:
        old = '''    fetch('/labs/assessment/data/scoring.json', {cache: 'no-store'}).then(response => response.json()),\n    fetch('/labs/assessment/data/board-mode.json', {cache: 'no-store'}).then(response => response.json())\n  ]).then(([drills, scoring, contract]) => {'''
        new = '''    fetch('/labs/assessment/data/scoring.json', {cache: 'no-store'}).then(response => response.json()),\n    fetch('/labs/assessment/data/board-mode.json', {cache: 'no-store'}).then(response => response.json()),\n    fetch('/labs/assessment/data/review-map.json', {cache: 'no-store'}).then(response => response.json())\n  ]).then(([drills, scoring, contract, reviewMap]) => {'''
        text = replace_once(text, old, new, "review map fetch")
        text = replace_once(
            text,
            "    state.contract = contract;\n    state.remaining = contract.default_session.seconds_per_round;",
            "    state.contract = contract;\n    state.reviewMap = reviewMap;\n    state.remaining = contract.default_session.seconds_per_round;",
            "store review map",
        )
        text = replace_once(
            text,
            "    renderScoreGrid();\n  }).catch(() => {",
            "    renderScoreGrid();\n    renderReviewHandoff();\n  }).catch(() => {",
            "initial handoff render",
        )

    PAGE.write_text(text, encoding="utf-8")


def patch_backlog() -> None:
    path = DATA / "backlog.json"
    value = load(path)
    if not any(item.get("id") == "LOOP-038" for item in value.get("items", [])):
        value.setdefault("items", []).append({
            "id": "LOOP-038",
            "priority": "P1",
            "title": "Board Mode targeted review handoff",
            "status": "done",
            "outputs": [
                "/labs/assessment/board/",
                "/labs/assessment/data/board-mode.json",
                "/labs/assessment/data/review-map.json",
                "scripts/validate_assessment_board_mode.py"
            ],
            "working_rule": "Aggregate Board self-scores only in the current browser-memory session, then route the two weakest dimensions to the existing Review Map. Do not write history, recalibrate scoring, or create a second profile model."
        })
        value["updated_at"] = "2026-08-16"
        themes = [theme for theme in value.get("next_iteration_themes", []) if "Board Mode review handoff" not in theme]
        themes.insert(0, "define a true human page-review findings contract without fabricating human verification")
        value["next_iteration_themes"] = list(dict.fromkeys(themes))
        dump(path, value)


def patch_tests() -> None:
    text = TESTS.read_text(encoding="utf-8")
    if '"LOOP-038"' not in text:
        text = text.replace('"LOOP-036", "LOOP-037"):', '"LOOP-036", "LOOP-037", "LOOP-038"):')
    if 'assert board["review_map_contract"]' not in text:
        text = text.replace(
            '    assert board["drill_source"] == "/labs/assessment/data/core-boundary-drills.json"\n',
            '    assert board["drill_source"] == "/labs/assessment/data/core-boundary-drills.json"\n    assert board["review_map_contract"] == "/labs/assessment/data/review-map.json"\n    assert board["review_handoff"]["history_write"] is False\n'
        )
    if 'assert "renderReviewHandoff" in page' not in text:
        text = text.replace(
            '    assert "localStorage" not in page\n',
            '    assert "localStorage" not in page\n    assert "renderReviewHandoff" in page\n    assert "dimensionScores" in page\n    assert "/labs/assessment/data/review-map.json" in page\n'
        )
    TESTS.write_text(text, encoding="utf-8")


def main() -> None:
    patch_page()
    patch_backlog()
    patch_tests()


if __name__ == "__main__":
    main()
