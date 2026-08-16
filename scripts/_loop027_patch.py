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


# Catalog registration.
catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.6.0"
catalog["purpose"] = (
    "Turn the Lab into a structured SAP Lead assessment route across process knowledge, diagnostics, architecture, "
    "integration, data, AI, adaptive practice, feedback, evidence-backed question authoring, promotion readiness, "
    "claim-level primary-source review, and explicit human page review."
)
authoring = catalog.setdefault("authoring_tools", [])
if not any(item.get("id") == "human-review" for item in authoring):
    authoring.append(
        {
            "id": "human-review",
            "label": "Human Review Queue",
            "route": "/labs/assessment/human-review/",
            "purpose": "Order source-supported SAP pages for page-level human review without changing verification, indexing, or publication state automatically.",
        }
    )
strong = catalog.setdefault("coverage", {}).setdefault("strong_now", [])
marker = "Source-supported P1 routes are now ordered through an explicit human page-review queue with a non-publishing boundary"
if marker not in strong:
    strong.append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "complete the core human-review wave and record page-level findings without auto-publishing",
    "extend candidate seeds only into evidence-complete graphs where the new reasoning signal is not already covered",
    "connect real assessment feedback to practice priority while factual truth remains source-based",
    "add standards or original research to selective routes only when an external claim actually needs it",
]
endpoints = catalog.setdefault("endpoints", {})
endpoints["human_review_route"] = "/labs/assessment/human-review/"
endpoints["human_review_policy"] = "/labs/assessment/data/human-review-policy.json"
endpoints["human_review_queue"] = "/labs/assessment/data/human-review-queue.json"
write_json(catalog_path, catalog)


# Backlog state.
backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
items = backlog.setdefault("items", [])
if not any(item.get("id") == "LOOP-027" for item in items):
    items.append(
        {
            "id": "LOOP-027",
            "priority": "P1",
            "title": "Source-supported human page-review queue",
            "status": "done",
            "outputs": [
                "/labs/assessment/human-review/",
                "/labs/assessment/data/human-review-policy.json",
                "/labs/assessment/data/human-review-queue.json",
                "scripts/generate_assessment_human_review_queue.py",
            ],
            "working_rule": "Use source-supported Promotion Readiness routes to order page-level human review. Never change verified, status, robots, sitemap, or publication state automatically.",
        }
    )
backlog["next_iteration_themes"] = [
    "complete the first core human-review wave and capture page-level findings separately from factual-review claims",
    "remove brittle practice-count assertions before expanding the graph-backed candidate corpus",
    "extend candidate generation into evidence-complete gaps with aggressive duplicate rejection",
    "use real feedback to influence practice selection without changing factual truth",
]
write_json(backlog_path, backlog)


# Assessment route registration and stale count wording cleanup.
index_path = ROOT / "labs" / "assessment" / "index.md"
index = index_path.read_text(encoding="utf-8")
needle = '      <a href="/labs/assessment/promotion-readiness/"><span>CONTENT</span><strong>Promotion Readiness</strong><small>Review structurally mature draft pages while factual verification and publication policy remain separate decisions.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>\n'
addition = needle + '      <a href="/labs/assessment/human-review/"><span>HUMAN</span><strong>Human Review Queue</strong><small>Read source-supported P1 pages end to end before any verification or publication decision.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>\n'
if '/labs/assessment/human-review/' not in index:
    index = replace_once(index, needle, addition, "assessment human review link")
index = index.replace(
    '<a href="/labs/assessment/data/question-candidates.json"><span>2</span><strong>Generated Candidate Inventory</strong><small>Two review candidates, twelve duplicate rejections, and a hard publication boundary.</small>',
    '<a href="/labs/assessment/data/question-candidates.json"><span>GEN</span><strong>Generated Candidate Inventory</strong><small>Review-stage candidates and duplicate rejections stay outside the published case manifest.</small>',
)
index_path.write_text(index, encoding="utf-8")


# Make assessment tests growth-safe and register LOOP-027.
test_path = ROOT / "tests" / "test_assessment_practice_layer.py"
test = test_path.read_text(encoding="utf-8")
test = test.replace(
    '    assert len(rows) == manifest["total_cases"] == 59\n',
    '    assert len(rows) == manifest["total_cases"]\n',
)
test = test.replace(
    '    assert manifest["total_cases"] == inventory["published_case_count"] == 59\n',
    '    assert manifest["total_cases"] == inventory["published_case_count"]\n',
)
test = test.replace(
    '    assert inventory["candidate_count"] == 2\n    assert inventory["rejected_duplicate_count"] == 12\n\n    candidates = {item["id"]: item for item in inventory["items"] if item["status"] == "candidate"}\n    assert set(candidates) == {"CAND-BIL-WRONG-REFERENCE", "CAND-INTOPS-OWNERSHIP"}\n',
    '    assert inventory["candidate_count"] == sum(item["status"] == "candidate" for item in inventory["items"])\n    assert inventory["rejected_duplicate_count"] == sum(item["status"] == "rejected_duplicate" for item in inventory["items"])\n\n    candidates = {item["id"]: item for item in inventory["items"] if item["status"] == "candidate"}\n    assert candidates\n',
)
old_generator_test = '''def test_graph_backed_candidate_generator_is_reproducible() -> None:\n    result = subprocess.run(\n        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n    assert "59 published cases unchanged" in result.stdout\n'''
new_generator_test = '''def test_graph_backed_candidate_generator_is_reproducible() -> None:\n    manifest = load_json("case-sets.json")\n    result = subprocess.run(\n        [sys.executable, "scripts/generate_assessment_candidates.py", "--check"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n    assert f"{manifest['total_cases']} published cases unchanged" in result.stdout\n'''
test = replace_once(test, old_generator_test, new_generator_test, "candidate generator growth-safe assertion")
if '"human-review": ASSESSMENT / "human-review" / "index.html",' not in test:
    test = test.replace(
        '        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",\n',
        '        "promotion-readiness": ASSESSMENT / "promotion-readiness" / "index.html",\n        "human-review": ASSESSMENT / "human-review" / "index.html",\n',
    )
if 'assert authoring["human-review"]["route"]' not in test:
    test = test.replace(
        '    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"\n',
        '    assert authoring["promotion-readiness"]["route"] == "/labs/assessment/promotion-readiness/"\n    assert authoring["human-review"]["route"] == "/labs/assessment/human-review/"\n',
    )
test = test.replace(
    '"LOOP-024", "LOOP-025", "LOOP-026"):',
    '"LOOP-024", "LOOP-025", "LOOP-026", "LOOP-027"):',
)

human_test = '''\n\ndef test_human_review_queue_is_reproducible_and_non_publishing() -> None:\n    policy = load_json("human-review-policy.json")\n    queue = load_json("human-review-queue.json")\n    promotion = load_json("promotion-readiness.json")\n\n    eligible = [\n        item for item in promotion["items"]\n        if item.get("state") == "human_review_candidate"\n        and item.get("priority") == "P1"\n        and item.get("factual_review", {}).get("status") == "source_supported"\n        and item.get("evidence_profile", {}).get("external_review_required", False)\n    ]\n    assert queue["summary"]["queued_routes"] == len(queue["items"]) == len(eligible)\n    assert queue["summary"]["core_assessment_wave"] == len(policy["core_assessment_wave"])\n    assert all(item["page_verified"] is False for item in queue["items"])\n    assert all(item["state"] == "queued_for_human_review" for item in queue["items"])\n    assert "never edits" in queue["boundary"].lower()\n\n    result = subprocess.run(\n        [sys.executable, "scripts/generate_assessment_human_review_queue.py", "--check"],\n        cwd=ROOT,\n        text=True,\n        capture_output=True,\n        check=False,\n    )\n    assert result.returncode == 0, result.stdout + result.stderr\n'''
if 'def test_human_review_queue_is_reproducible_and_non_publishing()' not in test:
    test += human_test

test_path.write_text(test, encoding="utf-8")

print("LOOP-027 integration patch applied")
