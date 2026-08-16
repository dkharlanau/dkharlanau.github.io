#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs/assessment/data"

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.0.0"
authoring = {item["id"]: item for item in catalog.get("authoring_tools", [])}
authoring["evidence-coverage"] = {
    "id": "evidence-coverage",
    "label": "Evidence Coverage",
    "route": "/labs/assessment/evidence-coverage/",
    "purpose": "Measure primary-source review coverage and evidence debt across the four SAP Lead assessment tracks so factual-review work is selected from data.",
}
catalog["authoring_tools"] = [authoring[key] for key in sorted(authoring)]
marker = "Assessment-track evidence coverage and P0 evidence-debt ranking derived from catalog, factual review, and promotion readiness"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "use evidence-coverage ranking to review the highest cross-track P0 routes",
    "continue factual review for Pricing, Shipping, Procurement, MDG, Development, Tax, and other evidence-debt routes",
    "connect real assessment feedback to review priority without converting feedback into factual truth",
    "use evidence coverage as a gate for future graph-backed question generation",
]
catalog["endpoints"]["evidence_coverage_route"] = "/labs/assessment/evidence-coverage/"
catalog["endpoints"]["evidence_coverage"] = "/labs/assessment/data/evidence-coverage.json"
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-021"] = {
    "id": "LOOP-021",
    "priority": "P1",
    "title": "Assessment-track evidence coverage matrix",
    "status": "done",
    "outputs": [
        "/labs/assessment/evidence-coverage/",
        "/labs/assessment/data/evidence-coverage.json",
        "scripts/generate_assessment_evidence_coverage.py",
    ],
    "working_rule": "Select the next factual-review batch from cross-track P0 evidence debt, not from page count or editing convenience.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "review the highest-ranked cross-track P0 evidence-debt routes from evidence-coverage.json",
    "expand factual review until every assessment track has balanced primary-source coverage",
    "connect assessment feedback to practice priority while keeping factual truth source-based",
    "use evidence coverage as a publication and question-generation quality gate",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

index_path = ROOT / "labs/assessment/index.md"
text = index_path.read_text(encoding="utf-8")
old = '      <a href="/labs/assessment/factual-review/"><span>FACT</span><strong>Factual Review</strong><small>Check release-sensitive SAP claims against primary sources and record product and release scope.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>\n      <a href="/labs/assessment/promotion-readiness/"><span>CONTENT</span><strong>Promotion Readiness</strong>'
new = '      <a href="/labs/assessment/factual-review/"><span>FACT</span><strong>Factual Review</strong><small>Check release-sensitive SAP claims against primary sources and record product and release scope.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>\n      <a href="/labs/assessment/evidence-coverage/"><span>COVER</span><strong>Evidence Coverage</strong><small>Compare source-review coverage and P0 evidence debt across all four assessment tracks.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>\n      <a href="/labs/assessment/promotion-readiness/"><span>CONTENT</span><strong>Promotion Readiness</strong>'
if old not in text:
    raise SystemExit("Authoring-control evidence anchor not found")
text = text.replace(old, new, 1)
text = text.replace(
    '<a href="/labs/assessment/data/promotion-readiness.json"><span>39</span><strong>Promotion Readiness Inventory</strong>',
    '<a href="/labs/assessment/data/promotion-readiness.json"><span>AUDIT</span><strong>Promotion Readiness Inventory</strong>',
    1,
)
old_machine = '      <a href="/labs/assessment/data/factual-review.json"><span>35</span><strong>Factual Review Registry</strong><small>Thirty-five source-supported claims across twelve release-sensitive SAP routes; page verification remains unchanged.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>\n      <a href="/labs/assessment/data/backlog.json"><span>LOOP</span><strong>Development State</strong><small>LOOP-001 through LOOP-020 are complete; twelve core SAP routes now have claim-level primary-source review.</small>'
new_machine = '      <a href="/labs/assessment/data/factual-review.json"><span>35</span><strong>Factual Review Registry</strong><small>Thirty-five source-supported claims across twelve release-sensitive SAP routes; page verification remains unchanged.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>\n      <a href="/labs/assessment/data/evidence-coverage.json"><span>COVER</span><strong>Evidence Coverage Dataset</strong><small>Track-level source-review coverage, cross-track P0 debt, and data-driven next-focus ranking.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>\n      <a href="/labs/assessment/data/backlog.json"><span>LOOP</span><strong>Development State</strong><small>LOOP-001 through LOOP-021 are complete; next factual review is selected from cross-track evidence debt.</small>'
if old_machine not in text:
    raise SystemExit("Machine evidence coverage anchor not found")
text = text.replace(old_machine, new_machine, 1)
index_path.write_text(text, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '        "factual-review": ASSESSMENT / "factual-review" / "index.html",\n        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",',
    '        "factual-review": ASSESSMENT / "factual-review" / "index.html",\n        "evidence-coverage": ASSESSMENT / "evidence-coverage" / "index.html",\n        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",',
    1,
)
tests = tests.replace(
    '    assert authoring["factual-review"]["route"] == "/labs/assessment/factual-review/"\n    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"',
    '    assert authoring["factual-review"]["route"] == "/labs/assessment/factual-review/"\n    assert authoring["evidence-coverage"]["route"] == "/labs/assessment/evidence-coverage/"\n    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"',
    1,
)
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021")',
    1,
)
coverage_test = '''

def test_evidence_coverage_is_reproducible_and_tracks_review_debt() -> None:
    coverage = load_json("evidence-coverage.json")
    factual = load_json("factual-review.json")

    assert coverage["source_contracts"]["factual_review"] == "/labs/assessment/data/factual-review.json"
    assert len(coverage["tracks"]) == 4
    assert coverage["summary"]["unique_source_reviewed_routes"] >= 12
    assert coverage["summary"]["source_supported_claims"] >= 35
    assert coverage["summary"]["unique_source_reviewed_routes"] <= coverage["summary"]["unique_evidence_applicable_routes"]
    assert all(track["source_reviewed_routes"] <= track["evidence_applicable_routes"] for track in coverage["tracks"])
    assert all(item["priority"] == "P0" for item in coverage["next_focus"])
    assert coverage["summary"]["source_supported_claims"] == sum(1 for claim in factual["claims"] if claim["status"] == "source_supported")

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_evidence_coverage.py", "--check"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Evidence coverage is current" in result.stdout
'''
if "test_evidence_coverage_is_reproducible_and_tracks_review_debt" not in tests:
    tests = tests.rstrip() + coverage_test + "\n"
tests_path.write_text(tests, encoding="utf-8")

print("Evidence coverage layer registered.")
