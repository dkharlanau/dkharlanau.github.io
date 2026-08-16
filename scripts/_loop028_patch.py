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


# Make candidate IDs graph-agnostic: each seed may declare its own failure prefix.
generator_path = ROOT / "scripts" / "generate_assessment_candidates.py"
generator = generator_path.read_text(encoding="utf-8")
old_id = '''def candidate_id(prefix: str, failure_id: str) -> str:\n    suffix = failure_id\n    for marker in ("FAIL-SD-BILLING-", "INTOPS-FAIL-"):\n        if suffix.startswith(marker):\n            suffix = suffix[len(marker):]\n            break\n    suffix = re.sub(r"[^A-Z0-9]+", "-", suffix.upper()).strip("-")\n    return f"{prefix}-{suffix}"\n'''
new_id = '''def candidate_id(prefix: str, failure_id: str, failure_prefix: str | None = None) -> str:\n    suffix = failure_id\n    if failure_prefix and suffix.startswith(failure_prefix):\n        suffix = suffix[len(failure_prefix):]\n    suffix = re.sub(r"[^A-Z0-9]+", "-", suffix.upper()).strip("-")\n    return f"{prefix}-{suffix}"\n'''
generator = replace_once(generator, old_id, new_id, "generic candidate id")
generator = replace_once(
    generator,
    '    cid = candidate_id(seed["candidate_prefix"], failure_id)\n',
    '    cid = candidate_id(seed["candidate_prefix"], failure_id, seed.get("failure_prefix"))\n',
    "seed failure prefix call",
)
generator = generator.replace('        "version": "1.1.0",\n', '        "version": "1.2.0",\n', 1)
generator_path.write_text(generator, encoding="utf-8")


# Expand deterministic seeds into Production where source support is already explicit.
seeds_path = DATA / "candidate-generation-seeds.json"
seeds = load_json(seeds_path)
seeds["version"] = "1.2.0"
for graph in seeds["graphs"]:
    if graph["path"].endswith("billing.yml"):
        graph["failure_prefix"] = "FAIL-SD-BILLING-"
    elif graph["path"].endswith("integration_operations.yml"):
        graph["failure_prefix"] = "INTOPS-FAIL-"

production_path = "_data/labs/enterprise_context/graphs/production.yml"
if not any(graph.get("path") == production_path for graph in seeds["graphs"]):
    seeds["graphs"].append(
        {
            "path": production_path,
            "human_ref": "/labs/enterprise-context/production/",
            "track": "procurement-logistics",
            "level": "diagnose",
            "candidate_prefix": "CAND-PP",
            "failure_prefix": "PP-FAIL-",
            "failure_sources": {
                "PP-FAIL-WRONG-QUANTITY": ["SRC-SAP-PP-PLANNING"],
                "PP-FAIL-WRONG-DATES": ["SRC-SAP-PP-PLANNING"],
                "PP-FAIL-GR": ["SRC-SAP-PP-GR"],
                "PP-FAIL-COST": ["SRC-SAP-PP-SETTLEMENT", "SRC-SAP-PP-SETTLEMENT-RULE"],
            },
            "evidence_class": "sap_product_primary",
            "selection_reason": "These failure paths add planning, receipt, and financial-close reasoning not already represented by the existing Production structure and staging cases.",
        }
    )
seeds["seed_selection_rule"] = (
    "Add a graph only when its route passes the evidence gate and at least one selected failure path adds a new diagnostic signal. "
    "Prefer explicit failure-level source references or a primary source whose scope directly supports the selected failure path."
)
write_json(seeds_path, seeds)


# Update generation contract without changing the publication boundary.
generation_path = DATA / "question-generation.json"
generation = load_json(generation_path)
generation["version"] = "1.3.0"
generation["current_scope"] = (
    "Deterministic candidate generation now covers Billing, Integration Operations, and selected Production failure modes. "
    "Production expansion is limited to MRP quantity/date reasoning, manufacturing-order goods receipt, and financial settlement where source support is explicit."
)
rule = "Seed expansion must add a new reasoning signal, not only another wording of an already published symptom."
if rule not in generation["quality_rules"]:
    generation["quality_rules"].append(rule)
write_json(generation_path, generation)


# Backlog and catalog record the completed loop and the next useful expansion boundary.
backlog_path = DATA / "backlog.json"
backlog = load_json(backlog_path)
if not any(item.get("id") == "LOOP-028" for item in backlog["items"]):
    backlog["items"].append(
        {
            "id": "LOOP-028",
            "priority": "P1",
            "title": "Evidence-gated Production candidate expansion",
            "status": "done",
            "outputs": [
                "/labs/assessment/data/candidate-generation-seeds.json",
                "/labs/assessment/data/question-candidates.json",
                "scripts/generate_assessment_candidates.py",
            ],
            "working_rule": "Expand question generation only where a source-supported graph adds a new diagnostic signal. Duplicate rejection and human promotion remain mandatory.",
        }
    )
backlog["next_iteration_themes"] = [
    "review new Production candidates and promote only clearly non-duplicate Lead cases through an explicit human-reviewed repository change",
    "complete the first core human-review wave and record page-level findings separately from factual-review claims",
    "inspect Procurement, ATP, EWM, and MDG graphs for the next evidence-complete candidate gaps",
    "use real assessment feedback to influence practice selection without changing factual truth",
]
write_json(backlog_path, backlog)

catalog_path = DATA / "catalog.json"
catalog = load_json(catalog_path)
catalog["version"] = "2.7.0"
strong = catalog["coverage"]["strong_now"]
marker = "Evidence-gated question generation now includes selected Production planning, goods-receipt, and settlement failure paths"
if marker not in strong:
    strong.append(marker)
catalog["coverage"]["next_practice_layers"] = [
    "review new Production question candidates and promote only clearly non-duplicate Lead cases",
    "complete the core human-review wave without changing publication flags automatically",
    "inspect Procurement, ATP, EWM, and MDG for the next evidence-complete diagnostic gaps",
    "connect real assessment feedback to practice priority while factual truth remains source-based",
]
write_json(catalog_path, catalog)

print("LOOP-028 candidate expansion patch applied")
