#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs/assessment/data"

review_path = DATA / "factual-review.json"
review = json.loads(review_path.read_text(encoding="utf-8"))
for claim in review["claims"]:
    claim.setdefault("evidence_class", "sap_product_primary")
review["version"] = "1.3.0"
review_path.write_text(json.dumps(review, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.1.0"
catalog["endpoints"]["evidence_profile"] = "/labs/assessment/data/evidence-profile.json"
marker = "Evidence classes separate SAP product facts, standards or research, and explicit author heuristics"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review SAP Business AI, MDG, Integration Suite, and Development with product-primary evidence",
    "profile generic AI architecture claims with standards, primary research, or explicit author-heuristic labels",
    "continue the highest P0 evidence-debt routes after profile-aware coverage is regenerated",
    "use evidence class and coverage as gates for future question generation and promotion",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-022"] = {
    "id": "LOOP-022",
    "priority": "P1",
    "title": "Evidence classes and route evidence profiles",
    "status": "done",
    "outputs": [
        "/labs/assessment/data/evidence-profile.json",
        "/labs/assessment/data/factual-review-policy.json",
        "scripts/audit_assessment_promotion_readiness.py",
        "scripts/generate_assessment_evidence_coverage.py",
    ],
    "working_rule": "Validate product facts with product primary sources, standards with their owning specifications, research claims with original research, and keep author heuristics explicitly non-factual.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "review SAP Business AI, MDG, Integration Suite, and Development product facts",
    "add standard/research evidence only where generic AI architecture pages make externally checkable claims",
    "continue profile-aware P0 evidence debt after the AI/Data and Integration batch",
    "use evidence class as a gate for question generation and publication review",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

index_path = ROOT / "labs/assessment/index.md"
text = index_path.read_text(encoding="utf-8")
anchor = '      <a href="/labs/assessment/data/evidence-coverage.json"><span>COVER</span><strong>Evidence Coverage Dataset</strong><small>Track-level source-review coverage, cross-track P0 debt, and data-driven next-focus ranking.</small><i class="material-symbols-outlined" aria-hidden="true">analytics</i></a>'
addition = anchor + '\n      <a href="/labs/assessment/data/evidence-profile.json"><span>CLASS</span><strong>Evidence Profile</strong><small>Route-level expectations for SAP product sources, standards, research, and explicit author heuristics.</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>'
if '/labs/assessment/data/evidence-profile.json' not in text:
    if anchor not in text:
        raise SystemExit("Evidence coverage machine link anchor not found")
    text = text.replace(anchor, addition, 1)
text = text.replace(
    "LOOP-001 through LOOP-021 are complete; next factual review is selected from cross-track evidence debt.",
    "LOOP-001 through LOOP-022 are complete; evidence debt now respects the evidence class expected by each route.",
    1,
)
index_path.write_text(text, encoding="utf-8")

coverage_page_path = ROOT / "labs/assessment/evidence-coverage/index.html"
page = coverage_page_path.read_text(encoding="utf-8")
page = page.replace(
    "This view connects the four assessment tracks with factual-review coverage. It shows which routes already have primary-source support and which mature routes still carry evidence debt.",
    "This view connects the four assessment tracks with factual-review coverage and route evidence profiles. Product-heavy routes carry source-review debt; selective architecture routes can instead use standards, primary research, and explicit author heuristics.",
    1,
)
page = page.replace(
    "Coverage is a planning signal. It is not a verified-page count.",
    "Coverage counts routes where external source review is a required gate. Selective or heuristic routes are shown separately.",
    1,
)
page = page.replace(
    "`${track.coverage_percent}% source-reviewed across ${track.evidence_applicable_routes} evidence-applicable route(s).`",
    "`${track.coverage_percent}% source-reviewed across ${track.externally_review_required_routes} required route(s); ${track.selective_or_heuristic_routes} selective/heuristic route(s).`",
    1,
)
page = page.replace(
    "$('ec-reviewed').textContent=s.unique_source_reviewed_routes;$('ec-total').textContent=s.unique_evidence_applicable_routes;",
    "$('ec-reviewed').textContent=s.unique_source_reviewed_routes;$('ec-total').textContent=s.unique_externally_review_required_routes;",
    1,
)
page = page.replace(
    "`${s.coverage_percent}% of unique evidence-applicable assessment routes have claim-level primary-source review.`",
    "`${s.coverage_percent}% of routes that require external review have claim-level primary-source support; ${s.unique_selective_or_heuristic_routes} route(s) use selective or heuristic evidence profiles.`",
    1,
)
coverage_page_path.write_text(page, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022")',
    1,
)
tests = tests.replace(
    '    assert all(claim["source_refs"] for claim in review["claims"])',
    '    assert all(claim["source_refs"] for claim in review["claims"])\n    assert all(claim["evidence_class"] == "sap_product_primary" for claim in review["claims"])\n    assert "author_heuristic" in policy["evidence_classes"]',
    1,
)
old = '''    assert coverage["source_contracts"]["factual_review"] == "/labs/assessment/data/factual-review.json"
    assert len(coverage["tracks"]) == 4
    assert coverage["summary"]["unique_source_reviewed_routes"] >= 12
    assert coverage["summary"]["source_supported_claims"] >= 35
    assert coverage["summary"]["unique_source_reviewed_routes"] <= coverage["summary"]["unique_evidence_applicable_routes"]
    assert all(track["source_reviewed_routes"] <= track["evidence_applicable_routes"] for track in coverage["tracks"])
    assert all(item["priority"] == "P0" for item in coverage["next_focus"])'''
new = '''    assert coverage["source_contracts"]["factual_review"] == "/labs/assessment/data/factual-review.json"
    assert coverage["source_contracts"]["evidence_profile"] == "/labs/assessment/data/evidence-profile.json"
    assert len(coverage["tracks"]) == 4
    assert coverage["summary"]["unique_source_reviewed_routes"] >= 12
    assert coverage["summary"]["source_supported_claims"] >= 35
    assert coverage["summary"]["unique_source_reviewed_routes"] <= coverage["summary"]["unique_externally_review_required_routes"]
    assert coverage["summary"]["unique_selective_or_heuristic_routes"] >= 2
    assert all(track["source_reviewed_routes"] <= track["externally_review_required_routes"] for track in coverage["tracks"])
    assert all(item["priority"] == "P0" for item in coverage["next_focus"])'''
if old not in tests:
    raise SystemExit("Coverage test anchor not found")
tests = tests.replace(old, new, 1)
profile_test = '''

def test_evidence_profiles_do_not_force_sap_product_proof_for_author_heuristics() -> None:
    profile = load_json("evidence-profile.json")
    readiness = load_json("promotion-readiness.json")
    by_route = {item["route"]: item for item in readiness["items"]}

    assert profile["route_overrides"]["/labs/ai-ready/"]["counts_as_source_review_debt"] is False
    assert profile["route_overrides"]["/labs/business-ai/"]["counts_as_source_review_debt"] is False
    assert "author_heuristic" in profile["route_overrides"]["/labs/ai-ready/"]["expected_evidence_classes"]
    assert by_route["/labs/ai-ready/"]["priority"] == "P2"
    assert by_route["/labs/business-ai/"]["priority"] == "P2"
    assert by_route["/labs/enterprise-context/business-ai/"]["priority"] == "P0"
'''
if "test_evidence_profiles_do_not_force_sap_product_proof_for_author_heuristics" not in tests:
    tests = tests.rstrip() + profile_test + "\n"
tests_path.write_text(tests, encoding="utf-8")

print("Evidence classes registered and existing factual claims migrated.")
