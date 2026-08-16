#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs/assessment/data"


def replace_once(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"Missing patch anchor: {label}")
    return text.replace(old, new, 1)


# Candidate generator: validate seed eligibility before constructing any candidate.
generator_path = ROOT / "scripts/generate_assessment_candidates.py"
text = generator_path.read_text(encoding="utf-8")
text = replace_once(
    text,
    "import yaml\n",
    "import yaml\n\nfrom assessment_candidate_evidence import validate_seed_evidence_contract\n",
    "generator evidence import",
)
text = replace_once(
    text,
    "    source_refs: list[str],\n    cases: list[dict[str, Any]],\n    threshold: float,\n) -> dict[str, Any]:",
    "    source_refs: list[str],\n    cases: list[dict[str, Any]],\n    evidence_gate: dict[str, Any],\n    threshold: float,\n) -> dict[str, Any]:",
    "candidate signature",
)
text = replace_once(
    text,
    '        "evidence_map": build_evidence_map(failure_id, source_refs, len(expected)),\n',
    '        "evidence_map": build_evidence_map(failure_id, source_refs, len(expected)),\n        "evidence_gate": evidence_gate,\n',
    "candidate evidence field",
)
text = replace_once(
    text,
    '    threshold = float(seeds["dedup_threshold"])\n    candidates: list[dict[str, Any]] = []\n',
    '    threshold = float(seeds["dedup_threshold"])\n    evidence_gates = validate_seed_evidence_contract(ROOT, seeds)\n    candidates: list[dict[str, Any]] = []\n',
    "generate gate initialization",
)
text = replace_once(
    text,
    '    for seed in seeds["graphs"]:\n        graph_path = ROOT / seed["path"]\n',
    '    for seed in seeds["graphs"]:\n        seed_gate = evidence_gates[seed["path"]]\n        graph_path = ROOT / seed["path"]\n',
    "seed gate lookup",
)
text = replace_once(
    text,
    '            candidate = build_candidate(graph, seed, failure_id, list(source_refs), cases, threshold)\n',
    '            candidate = build_candidate(graph, seed, failure_id, list(source_refs), cases, seed_gate, threshold)\n',
    "candidate gate argument",
)
text = replace_once(text, '        "version": "1.0.0",\n', '        "version": "1.1.0",\n', "inventory version")
text = replace_once(
    text,
    '        "publication_boundary": "Candidate inventory is review-stage only and is not referenced by case-sets.json.",\n',
    '        "publication_boundary": "Candidate inventory is review-stage only and is not referenced by case-sets.json.",\n        "evidence_gate": {\n            "policy": "/labs/assessment/data/evidence-profile.json",\n            "factual_review": "/labs/assessment/data/factual-review.json",\n            "eligible_seed_graphs": len(evidence_gates),\n            "blocked_seed_graphs": 0,\n            "all_emitted_candidates_evidence_eligible": True,\n        },\n',
    "inventory evidence summary",
)
generator_path.write_text(text, encoding="utf-8")

# Seed contract: each graph declares what evidence class it is using.
seeds_path = DATA / "candidate-generation-seeds.json"
seeds = json.loads(seeds_path.read_text(encoding="utf-8"))
seeds["version"] = "1.1.0"
seeds["purpose"] = "Whitelist graph failure modes, their evidence class, and primary-source references for deterministic assessment-question candidate generation."
for graph in seeds["graphs"]:
    graph["evidence_class"] = "sap_product_primary"
seeds["evidence_gate_rule"] = "A seed graph is eligible only when its evidence class is allowed by the route profile, required factual review is source-supported, and every referenced source is source_verified."
seeds_path.write_text(json.dumps(seeds, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Candidate schema: evidence eligibility is part of every emitted record.
schema_path = DATA / "candidate-question-schema.json"
schema = json.loads(schema_path.read_text(encoding="utf-8"))
required = schema["required"]
if "evidence_gate" not in required:
    required.append("evidence_gate")
schema["properties"]["evidence_gate"] = {
    "type": "object",
    "required": [
        "eligible",
        "route",
        "evidence_class",
        "expected_evidence_classes",
        "external_review_required",
        "route_review_status",
        "route_reviewed_claims",
        "verified_source_count",
        "source_status"
    ],
    "properties": {
        "eligible": {"const": True},
        "route": {"type": "string", "pattern": "^/labs/"},
        "evidence_class": {"enum": ["sap_product_primary", "standard_or_spec_primary", "research_primary", "author_heuristic"]},
        "expected_evidence_classes": {"type": "array", "minItems": 1, "items": {"type": "string"}},
        "external_review_required": {"type": "boolean"},
        "route_review_status": {"type": "string"},
        "route_reviewed_claims": {"type": "integer", "minimum": 0},
        "route_reviewed_at": {"type": ["string", "null"]},
        "verified_source_count": {"type": "integer", "minimum": 1},
        "source_status": {"const": "source_verified"}
    },
    "additionalProperties": False
}
schema_path.write_text(json.dumps(schema, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Generation policy: make the gate an explicit publication-independent contract.
generation_path = DATA / "question-generation.json"
generation = json.loads(generation_path.read_text(encoding="utf-8"))
generation["version"] = "1.2.0"
generation["evidence_gate"] = {
    "profile_contract": "/labs/assessment/data/evidence-profile.json",
    "factual_review_contract": "/labs/assessment/data/factual-review.json",
    "source_registry": "_data/labs/enterprise_context/sources/*.yml",
    "rule": "Validate route evidence profile, factual-review state, and source_verified status before a whitelisted graph can emit any candidate.",
    "failure_behavior": "Generation fails closed. An ineligible seed does not emit a weaker or provisional candidate.",
    "author_heuristic_rule": "Author-heuristic generation requires explicit seed approval and is never inferred from the absence of product evidence."
}
quality_rule = "Do not generate from a graph whose route fails its evidence profile or whose referenced sources are not source_verified."
if quality_rule not in generation["quality_rules"]:
    generation["quality_rules"].append(quality_rule)
generation_path.write_text(json.dumps(generation, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Catalog and backlog.
catalog_path = DATA / "catalog.json"
catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
catalog["version"] = "2.5.0"
marker = "Assessment candidate generation fails closed when route evidence profiles or source verification are incomplete"
if marker not in catalog["coverage"]["strong_now"]:
    catalog["coverage"]["strong_now"].append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "extend candidate seeds only into evidence-complete graphs where the new reasoning signal is not already covered",
    "start page-level human review on source-supported P1 routes without auto-publishing",
    "connect real assessment feedback to practice priority while factual truth remains source-based",
    "add standards or original research to selective routes only when an external claim actually needs it"
]
catalog_path.write_text(json.dumps(catalog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

backlog_path = DATA / "backlog.json"
backlog = json.loads(backlog_path.read_text(encoding="utf-8"))
items = {item["id"]: item for item in backlog["items"]}
items["LOOP-026"] = {
    "id": "LOOP-026",
    "priority": "P1",
    "title": "Evidence-gated assessment candidate generation",
    "status": "done",
    "outputs": [
        "scripts/assessment_candidate_evidence.py",
        "scripts/generate_assessment_candidates.py",
        "/labs/assessment/data/candidate-generation-seeds.json",
        "/labs/assessment/data/candidate-question-schema.json",
        "/labs/assessment/data/question-generation.json",
        "/labs/assessment/data/question-candidates.json"
    ],
    "working_rule": "Fail candidate generation before question construction when the route evidence profile, factual-review state, or source verification is incomplete. Evidence eligibility never publishes a case automatically."
}
backlog["items"] = [items[key] for key in sorted(items)]
backlog["next_iteration_themes"] = [
    "extend graph-backed candidate generation into evidence-complete gaps and keep aggressive duplicate rejection",
    "start page-level human review of source-supported P1 routes",
    "use real feedback to influence practice selection without changing factual truth",
    "add standards or primary research to selective routes only for externally checkable claims"
]
backlog_path.write_text(json.dumps(backlog, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

# Root assessment copy.
index_path = ROOT / "labs/assessment/index.md"
index = index_path.read_text(encoding="utf-8")
index = index.replace(
    "Question candidates are generated from whitelisted graph evidence. Release-sensitive SAP claims now have a separate primary-source review layer before any page-level verification or publication decision.",
    "Question candidates are generated only from whitelisted graph evidence that passes the route evidence profile, factual-review state, and source-verification gate. Release-sensitive SAP claims remain separate from page-level verification or publication decisions.",
    1,
)
index = index.replace(
    "LOOP-001 through LOOP-025 are complete; broad required evidence debt is closed and the next gate is page-level human review.",
    "LOOP-001 through LOOP-026 are complete; broad evidence debt is closed and candidate generation now fails closed on incomplete evidence.",
    1,
)
index_path.write_text(index, encoding="utf-8")

# Tests: validate emitted candidates and seed contracts, without hardcoding one future seed set.
tests_path = ROOT / "tests/test_assessment_practice_layer.py"
tests = tests_path.read_text(encoding="utf-8")
tests = tests.replace(
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024", "LOOP-025")',
    '("LOOP-010", "LOOP-011", "LOOP-012", "LOOP-013", "LOOP-014", "LOOP-015", "LOOP-016", "LOOP-017", "LOOP-018", "LOOP-019", "LOOP-020", "LOOP-021", "LOOP-022", "LOOP-023", "LOOP-024", "LOOP-025", "LOOP-026")',
    1,
)
gate_test = '''

def test_candidate_generation_fails_closed_behind_evidence_gate() -> None:
    inventory = load_json("question-candidates.json")
    seeds = load_json("candidate-generation-seeds.json")
    profile = load_json("evidence-profile.json")
    factual = load_json("factual-review.json")

    assert inventory["evidence_gate"]["all_emitted_candidates_evidence_eligible"] is True
    assert inventory["evidence_gate"]["blocked_seed_graphs"] == 0
    assert inventory["evidence_gate"]["eligible_seed_graphs"] == len(seeds["graphs"])
    assert all(item["evidence_gate"]["eligible"] is True for item in inventory["items"])
    assert all(item["evidence_gate"]["source_status"] == "source_verified" for item in inventory["items"])
    assert all(item["evidence_gate"]["verified_source_count"] > 0 for item in inventory["items"])

    factual_routes = {item["route"]: item for item in factual["routes"]}
    for seed in seeds["graphs"]:
        evidence_class = seed["evidence_class"]
        override = profile["route_overrides"].get(seed["human_ref"])
        route_profile = override or profile["defaults"]["enterprise_context"]
        assert evidence_class in route_profile["expected_evidence_classes"]
        if route_profile["counts_as_source_review_debt"]:
            assert seed["human_ref"] in factual_routes
'''
if "test_candidate_generation_fails_closed_behind_evidence_gate" not in tests:
    tests = tests.rstrip() + gate_test + "\n"
tests_path.write_text(tests, encoding="utf-8")

print("Candidate evidence gate registered.")
