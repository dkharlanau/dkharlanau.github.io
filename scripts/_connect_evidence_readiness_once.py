#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing patch anchor: {label}")
    return text.replace(old, new, 1)


policy_path = ROOT / "labs/assessment/data/promotion-readiness-policy.json"
policy = json.loads(policy_path.read_text(encoding="utf-8"))
policy["version"] = "1.1.0"
policy["purpose"] = (
    "Prioritize mature draft/noindex Lab pages for human review using both structural readiness "
    "and claim-level factual-review coverage without automatically publishing or verifying a page."
)
policy["evidence_checks"] = [
    "claim-level factual review is read from /labs/assessment/data/factual-review.json",
    "source conflicts and unclear release scope are higher priority than normal unreviewed content",
    "mature enterprise knowledge without factual review is prioritized before already source-supported routes",
    "source-supported routes still require page-level human verification",
    "verified:false never becomes verified through this audit",
]
policy["priority_rule"] = (
    "For human-review candidates, enterprise knowledge with source conflicts, unclear release scope, "
    "or no factual review is P0. Source-supported enterprise knowledge is P1. Assessment and authoring "
    "routes are P2 unless another policy explicitly raises them."
)
if "Do not treat source-supported claims as page-level verification." not in policy["anti_shortcut_rules"]:
    policy["anti_shortcut_rules"].append("Do not treat source-supported claims as page-level verification.")
policy_path.write_text(json.dumps(policy, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

page_path = ROOT / "labs/assessment/promotion-readiness/index.html"
text = page_path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "The audit checks page structure, navigation, machine-readable links, and placeholder markers. It reports factual verification separately. A mature draft becomes a human-review candidate, not an automatically public page.",
    "The audit checks page structure and claim-level evidence coverage. Mature enterprise pages without primary-source review move ahead of already source-supported routes, but no page becomes verified or public automatically.",
    "promotion hero",
)
text = replace_once(
    text,
    '      <div class="research-canvas__signal-line"><span>03</span><strong id="pr-verified">—</strong><small>verified:true</small></div>',
    '      <div class="research-canvas__signal-line"><span>03</span><strong id="pr-evidence">—</strong><small>Source-reviewed routes</small></div>\n      <div class="research-canvas__signal-line"><span>04</span><strong id="pr-verified">—</strong><small>verified:true</small></div>',
    "promotion evidence signal",
)
old_controls = '''      <label>Local review state
        <select id="pr-local-filter"><option value="all">All local states</option><option value="unreviewed">Unreviewed</option><option value="needs_factual_review">Needs factual review</option><option value="keep_draft">Keep draft</option><option value="recommend_promotion">Recommend promotion</option></select>
      </label>'''
new_controls = old_controls + '''
      <label>Evidence state
        <select id="pr-evidence-filter"><option value="all">All evidence states</option><option value="not_reviewed">Not source-reviewed</option><option value="source_supported">Source-supported</option><option value="source_conflict">Source conflict</option><option value="release_scope_unclear">Release scope unclear</option></select>
      </label>'''
text = replace_once(text, old_controls, new_controls, "promotion evidence filter")
text = replace_once(
    text,
    "The current assessment-linked routes already pass the structural bar. The next useful action is to review factual claims and decide whether a page should remain research-only or become indexable.",
    "The queue now separates structural maturity from factual-review coverage. For enterprise knowledge, missing or conflicting evidence comes first; source-supported pages move to page-level human review.",
    "promotion queue copy",
)
text = replace_once(
    text,
    '<a href="/labs/assessment/data/promotion-readiness.json"><span>AUDIT</span><strong>Promotion Readiness Inventory</strong><small>Current routes, structural checks, verification state, and review priority.</small>',
    '<a href="/labs/assessment/data/promotion-readiness.json"><span>AUDIT</span><strong>Promotion Readiness Inventory</strong><small>Current routes, structural checks, factual-review coverage, review reason, and priority.</small>',
    "promotion machine copy",
)
factual_link = '      <a href="/labs/assessment/factual-review/"><span>FACT</span><strong>Factual Review</strong><small>Inspect the claim-level evidence registry that now feeds promotion priority.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>\n'
question_link = '      <a href="/labs/assessment/question-review/"><span>AUTHOR</span><strong>Question Candidate Review</strong>'
if factual_link not in text:
    text = replace_once(text, question_link, factual_link + question_link, "promotion factual link")
text = replace_once(
    text,
    "const root=document.createElement('article');root.className='pr-card';root.dataset.group=group(item.route);root.dataset.local=(reviews()[item.route]?.decision)||'unreviewed';",
    "const root=document.createElement('article');root.className='pr-card';root.dataset.group=group(item.route);root.dataset.local=(reviews()[item.route]?.decision)||'unreviewed';root.dataset.evidence=item.factual_review?.status||'not_reviewed';",
    "promotion card evidence data",
)
text = replace_once(
    text,
    "[item.route,item.state,item.priority,`structure ${item.structural_score}/5`,item.verified?'verified:true':'verified:false'].forEach(value=>{const chip=document.createElement('span');chip.textContent=value;meta.appendChild(chip)});",
    "[item.route,item.state,item.priority,`structure ${item.structural_score}/5`,`evidence ${item.factual_review?.status||'not_reviewed'}`,`${item.factual_review?.claim_count||0} reviewed claim(s)`,item.verified?'verified:true':'verified:false'].forEach(value=>{const chip=document.createElement('span');chip.textContent=value;meta.appendChild(chip)});",
    "promotion evidence chips",
)
text = replace_once(
    text,
    "const path=document.createElement('p');path.textContent=item.source_path||'No source file resolved.';",
    "const path=document.createElement('p');path.textContent=item.source_path||'No source file resolved.';const reason=document.createElement('p');reason.textContent=item.review_reason||'';",
    "promotion review reason",
)
text = replace_once(text, "root.append(meta,path,checks);", "root.append(meta,path,reason,checks);", "promotion card append")
old_filter = "function applyFilters(){const wantedGroup=$('pr-group').value;const wantedLocal=$('pr-local-filter').value;let visible=0;document.querySelectorAll('.pr-card').forEach(card=>{const show=(wantedGroup==='all'||card.dataset.group===wantedGroup)&&(wantedLocal==='all'||card.dataset.local===wantedLocal);card.hidden=!show;if(show)visible+=1});if(inventory)$('pr-status').textContent=`${visible} route(s) shown. ${inventory.counts.human_review_candidate||0} total human-review candidates; ${inventory.items.filter(item=>item.verified).length} verified:true.`;}"
new_filter = "function applyFilters(){const wantedGroup=$('pr-group').value;const wantedLocal=$('pr-local-filter').value;const wantedEvidence=$('pr-evidence-filter').value;let visible=0;document.querySelectorAll('.pr-card').forEach(card=>{const show=(wantedGroup==='all'||card.dataset.group===wantedGroup)&&(wantedLocal==='all'||card.dataset.local===wantedLocal)&&(wantedEvidence==='all'||card.dataset.evidence===wantedEvidence);card.hidden=!show;if(show)visible+=1});if(inventory)$('pr-status').textContent=`${visible} route(s) shown. ${inventory.counts.human_review_candidate||0} human-review candidates; ${inventory.factual_review_counts?.source_supported||0} source-reviewed; ${inventory.priority_counts?.P0||0} P0 evidence-review routes.`;}"
text = replace_once(text, old_filter, new_filter, "promotion filters JS")
text = replace_once(
    text,
    "function render(data){inventory=data;$('pr-routes').textContent=data.scope_route_count;$('pr-review').textContent=data.counts.human_review_candidate||0;$('pr-verified').textContent=data.items.filter(item=>item.verified).length;",
    "function render(data){inventory=data;$('pr-routes').textContent=data.scope_route_count;$('pr-review').textContent=data.counts.human_review_candidate||0;$('pr-evidence').textContent=data.factual_review_counts?.source_supported||0;$('pr-verified').textContent=data.items.filter(item=>item.verified).length;",
    "promotion render JS",
)
text = replace_once(
    text,
    "$('pr-group').addEventListener('change',applyFilters);$('pr-local-filter').addEventListener('change',applyFilters);",
    "$('pr-group').addEventListener('change',applyFilters);$('pr-local-filter').addEventListener('change',applyFilters);$('pr-evidence-filter').addEventListener('change',applyFilters);",
    "promotion filter listener",
)
page_path.write_text(text, encoding="utf-8")

catalog_path = ROOT / "labs/assessment/data/catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "1.8.0"
marker = "Evidence-aware promotion prioritization using factual-review coverage and explicit review reasons"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "continue factual review across remaining logistics verticals, starting with Production, Quality, Inventory, Finance Logistics, Automotive, and TM",
    "add evidence-coverage summaries by assessment track and domain",
    "connect real assessment feedback to review priority without converting feedback into factual truth",
    "extend graph-backed question generation only where factual evidence coverage is sufficient",
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = ROOT / "labs/assessment/data/backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-019"] = {
    "id": "LOOP-019",
    "priority": "P1",
    "title": "Evidence-aware promotion prioritization",
    "status": "done",
    "outputs": [
        "/labs/assessment/promotion-readiness/",
        "/labs/assessment/data/promotion-readiness.json",
        "scripts/audit_assessment_promotion_readiness.py",
    ],
    "working_rule": "Prioritize mature enterprise pages with missing, conflicting, or release-unclear evidence before routes that already have source-supported claims. Never promote automatically.",
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "continue factual review across remaining high-value SAP logistics routes",
    "create track-level evidence coverage and review debt views",
    "connect real assessment feedback to review priority without changing factual truth",
    "extend question generation only for sufficiently sourced graphs",
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

assessment_path = ROOT / "labs/assessment/index.md"
assessment = assessment_path.read_text(encoding="utf-8")
assessment = assessment.replace("<li>Integrate factual-review coverage into promotion prioritization</li>", "<li>Continue factual review across remaining logistics verticals</li>", 1)
assessment = assessment.replace("LOOP-001 through LOOP-018 are complete; next work connects factual coverage to promotion priority.", "LOOP-001 through LOOP-019 are complete; promotion priority now uses factual-review coverage.", 1)
assessment_path.write_text(assessment, encoding="utf-8")

tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019")',
    1,
)
evidence_test = '''

def test_promotion_readiness_uses_factual_review_coverage_for_priority() -> None:
    inventory = load_json("promotion-readiness.json")
    review = load_json("factual-review.json")
    reviewed_routes = {item["route"] for item in review["routes"]}
    by_route = {item["route"]: item for item in inventory["items"]}

    assert inventory["factual_review_registry"] == "/labs/assessment/data/factual-review.json"
    assert inventory["factual_review_counts"]["source_supported"] == len(reviewed_routes) == 6
    assert sum(inventory["priority_counts"].values()) == inventory["scope_route_count"]
    for route in reviewed_routes:
        assert by_route[route]["factual_review"]["status"] == "source_supported"
        assert by_route[route]["factual_review"]["claim_count"] > 0
        assert by_route[route]["priority"] == "P1"
        assert "human page-level verification" in by_route[route]["review_reason"]

    assert by_route["/labs/enterprise-context/pricing/"]["factual_review"]["status"] == "not_reviewed"
    assert by_route["/labs/enterprise-context/pricing/"]["priority"] == "P0"
    assert "primary-source review" in by_route["/labs/enterprise-context/pricing/"]["review_reason"]
'''
if "test_promotion_readiness_uses_factual_review_coverage_for_priority" not in tests:
    tests = tests.rstrip() + evidence_test + "\n"
tests_path.write_text(tests, encoding="utf-8")

print("Evidence-aware readiness patch applied.")
