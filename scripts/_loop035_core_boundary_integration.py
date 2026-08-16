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


# Catalog: add endpoints and current next-practice direction without inventing a publication mode.
catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.14.0"
strong = catalog.setdefault("coverage", {}).setdefault("strong_now", [])
marker = "Core 12 boundary drills now force ownership changes across adjacent SAP domains without entering the published case manifest"
if marker not in strong:
    strong.append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "use Core 12 boundary drills in timed oral practice and score the ownership transition, not only the module facts",
    "review the three new Production question candidates and promote only clearly non-duplicate Lead cases",
    "record true page-level human review separately from automated editorial improvement",
    "select secondary P1 pages by cross-track assessment value rather than page count"
]
endpoints = catalog.setdefault("endpoints", {})
endpoints["core_boundary_route"] = "/labs/assessment/core-boundaries/"
endpoints["core_boundary_drills"] = "/labs/assessment/data/core-boundary-drills.json"
write_json(catalog_path, catalog)


# Backlog: record LOOP-035 and move the next loop toward oral/board practice.
backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-035" for item in backlog["items"]):
    backlog["items"].append({
        "id": "LOOP-035",
        "priority": "P1",
        "title": "Core 12 cross-route ownership drills",
        "status": "done",
        "outputs": [
            "/labs/assessment/core-boundaries/",
            "/labs/assessment/data/core-boundary-drills.json",
            "scripts/validate_assessment_core_boundary_drills.py"
        ],
        "working_rule": "Practice the first ownership change between evidence-supported Core 12 routes. Keep drills synthetic, review-safe, and outside the published assessment case manifest."
    })
backlog["next_iteration_themes"] = [
    "build a timed oral Board Mode from Core 12 routes and boundary drills using the existing seven-dimension scoring contract",
    "review the three new Production question candidates and promote only non-duplicate Lead cases through an explicit reviewed change",
    "record true human page-review findings separately from automated editorial improvement",
    "select secondary P1 pages by cross-track assessment value instead of processing all routes mechanically"
]
write_json(backlog_path, backlog)


# Core Study page: make the boundary layer the next step after the three waves.
core_path = ROOT / "labs" / "assessment" / "core" / "index.html"
core = core_path.read_text(encoding="utf-8")
anchor = '''  <section class="research-canvas__boundary" data-reveal>\n    <span class="material-symbols-outlined" aria-hidden="true">rule</span>\n    <p><strong>Verification boundary:</strong> this study map only organizes existing evidence and practice. It does not mark any source page verified, approve review-stage candidates, or change indexing/publication state.</p>\n    <a href="/labs/assessment/human-review/">Open Human Review Queue <span class="material-symbols-outlined" aria-hidden="true">checklist</span></a>\n  </section>\n'''
insert = '''  <section class="research-canvas__inventory" data-reveal>\n    <header><p class="research-canvas__eyebrow">Next step / Boundaries</p><h2>Now make two correct modules disagree.</h2><p>Core 12 teaches each route. Boundary Drills train the harder part: finding the first wrong owner when the final symptom appears in another domain.</p></header>\n    <div class="research-route-list">\n      <a href="/labs/assessment/core-boundaries/"><span>X</span><strong>Core Boundary Drills</strong><small>Eight synthetic oral drills across Sales Order, Pricing, ATP, Shipping, Procurement, Production, Inventory, QM, EWM, Integration, MDG, and FI/CO.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>\n      <a href="/labs/assessment/data/core-boundary-drills.json"><span>DATA</span><strong>Boundary Drill Dataset</strong><small>Route pairs, boundary questions, expected reasoning, and red flags. Not part of the published case manifest.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>\n    </div>\n  </section>\n\n'''
if '/labs/assessment/core-boundaries/' not in core:
    core = replace_once(core, anchor, insert + anchor, "Core boundary drill route")
core_path.write_text(core, encoding="utf-8")


# Assessment landing page: add route and repair stale generated-candidate wording from pre-LOOP-028 state.
index_path = ROOT / "labs" / "assessment" / "index.md"
index = index_path.read_text(encoding="utf-8")
core_link = '      <a href="/labs/assessment/core/"><span>CORE</span><strong>Core 12 Study Map</strong><small>Study decisions, execution/state, governance and value as one Lead reasoning route.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>\n'
if '/labs/assessment/core-boundaries/' not in index and core_link in index:
    index = index.replace(
        core_link,
        core_link + '      <a href="/labs/assessment/core-boundaries/"><span>X</span><strong>Core Boundary Drills</strong><small>Cross-route oral practice for ownership changes and end-to-end completion proof.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>\n',
        1,
    )
index = index.replace(
    '<a href="/labs/assessment/data/question-candidates.json"><span>2</span><strong>Question Candidate Inventory</strong><small>Two review candidates and twelve duplicate rejections; not part of the 59 published cases.</small>',
    '<a href="/labs/assessment/data/question-candidates.json"><span>GEN</span><strong>Question Candidate Inventory</strong><small>Review-stage candidates and duplicate rejections are generated from evidence-gated graphs and stay outside the published case manifest.</small>',
)
index = index.replace(
    '<a href="/labs/assessment/data/backlog.json"><span>LOOP</span><strong>Development State</strong><small>LOOP-001 through LOOP-026 are complete; broad evidence debt is closed and candidate generation now fails closed on incomplete evidence.</small>',
    '<a href="/labs/assessment/data/backlog.json"><span>LOOP</span><strong>Development State</strong><small>Machine-readable agent-loop state, completed capabilities, and the next assessment-development themes.</small>',
)
if '/labs/assessment/data/core-boundary-drills.json' not in index:
    dataset_anchor = '      <a href="/labs/assessment/data/evidence-profile.json"><span>CLASS</span><strong>Evidence Profile</strong><small>Route-level expectations for SAP product sources, standards, research, and explicit author heuristics.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>\n'
    if dataset_anchor in index:
        index = index.replace(
            dataset_anchor,
            dataset_anchor + '      <a href="/labs/assessment/data/core-boundary-drills.json"><span>X</span><strong>Core Boundary Drill Dataset</strong><small>Eight synthetic cross-route drills for ownership and completion reasoning; never auto-published.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>\n',
            1,
        )
index_path.write_text(index, encoding="utf-8")


# Assessment tests: register route, loop, and publication-safe drill validation.
test_path = ROOT / "tests" / "test_assessment_practice_layer.py"
test = test_path.read_text(encoding="utf-8")
if '"core-boundaries": ASSESSMENT / "core-boundaries" / "index.html",' not in test:
    test = test.replace(
        '        "core-study": ASSESSMENT / "core" / "index.html",\n',
        '        "core-study": ASSESSMENT / "core" / "index.html",\n        "core-boundaries": ASSESSMENT / "core-boundaries" / "index.html",\n',
        1,
    )
test = test.replace(
    '"LOOP-032", "LOOP-033", "LOOP-034"):',
    '"LOOP-032", "LOOP-033", "LOOP-034", "LOOP-035"):',
)
drill_test = '''\n\ndef test_core_boundary_drills_cross_supported_routes_without_publishing() -> None:\n    drills = load_json("core-boundary-drills.json")\n    core = load_json("core-study-map.json")\n    manifest = load_json("case-sets.json")\n    core_by_route = {item["route"]: item for item in core["items"]}\n\n    assert len(drills["drills"]) >= 8\n    assert len({item["id"] for item in drills["drills"]}) == len(drills["drills"])\n    for drill in drills["drills"]:\n        assert len(drill["routes"]) >= 2\n        assert len(drill["expected_reasoning"]) >= 5\n        assert len(drill["red_flags"]) >= 2\n        for route in drill["routes"]:\n            assert route in core_by_route\n            assert core_by_route[route]["evidence"]["review_status"] == "primary_source_review_complete"\n            assert core_by_route[route]["evidence"]["page_verified"] is False\n\n    serialized_manifest = json.dumps(manifest)\n    assert "CORE-X-" not in serialized_manifest\n    assert "core-boundary-drills" not in serialized_manifest\n\n    result = subprocess.run(\n        [sys.executable, "scripts/validate_assessment_core_boundary_drills.py", "--check"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
if 'def test_core_boundary_drills_cross_supported_routes_without_publishing()' not in test:
    test += drill_test
test_path.write_text(test, encoding="utf-8")

print("LOOP-035 Core boundary integration applied")
