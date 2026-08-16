#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
GENERATED = DATA / "question-candidates.json"
GENERATED_SEMANTIC = DATA / "candidate-semantic-review.json"
REASONING_GAPS = DATA / "reasoning-gap-candidates.json"
REASONING_SEMANTIC = DATA / "reasoning-gap-semantic-review.json"
CASE_SETS = DATA / "case-sets.json"
OUTPUT = DATA / "promotion-review-packet.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def published_ids() -> set[str]:
    manifest = load_json(CASE_SETS)
    ids: set[str] = set()
    for case_set in manifest["sets"]:
        ids.update(str(item["id"]) for item in load_jsonl(ROOT / case_set["url"].lstrip("/")))
    return ids


def build() -> dict[str, Any]:
    generated = load_json(GENERATED)
    generated_semantic = load_json(GENERATED_SEMANTIC)
    gap_data = load_json(REASONING_GAPS)
    gap_semantic = load_json(REASONING_SEMANTIC)
    manifest = load_json(CASE_SETS)
    published = published_ids()

    generated_by_id = {item["id"]: item for item in generated["items"] if item["status"] == "candidate"}
    gap_by_id = {item["id"]: item for item in gap_data["candidates"]}
    generated_decisions = {item["candidate_id"]: item for item in generated_semantic["decisions"]}
    gap_decisions = {item["candidate_id"]: item for item in gap_semantic["decisions"]}

    packet: list[dict[str, Any]] = []
    for candidate_id, decision in generated_decisions.items():
        if decision["recommendation"] != "retain_for_human_promotion_review":
            continue
        candidate = generated_by_id[candidate_id]
        packet.append({
            "candidate_id": candidate_id,
            "candidate_source": "generated_failure_candidate",
            "track": candidate["track"],
            "level": candidate["level"],
            "title": candidate["title"],
            "prompt": candidate["prompt"],
            "expected_points": candidate["expected_points"],
            "follow_up_questions": candidate.get("follow_up_questions", []),
            "red_flags": candidate.get("red_flags", []),
            "graph_refs": candidate.get("graph_refs", []),
            "human_refs": candidate.get("human_refs", []),
            "source_refs": candidate.get("source_refs", []),
            "evidence_gate": candidate.get("evidence_gate", {}),
            "semantic_review": {
                "recommendation": decision["recommendation"],
                "reason": decision["reason"],
                "novel_signal": decision.get("novel_signal"),
                "closest_published_cases": decision.get("closest_published_cases", []),
                "review_checks": decision.get("review_checks", []),
            },
            "human_decision": {
                "status": "pending_human_review",
                "decision": None,
                "reviewed_at": None,
                "reviewer_note": "",
            },
        })

    for candidate_id, decision in gap_decisions.items():
        if decision["recommendation"] != "retain_for_human_promotion_review":
            continue
        candidate = gap_by_id[candidate_id]
        packet.append({
            "candidate_id": candidate_id,
            "candidate_source": "reasoning_gap_candidate",
            "track": candidate["track"],
            "level": candidate["level"],
            "title": candidate["title"],
            "prompt": candidate["prompt"],
            "expected_points": candidate["expected_points"],
            "follow_up_questions": candidate.get("follow_up_questions", []),
            "red_flags": candidate.get("red_flags", []),
            "graph_refs": [],
            "human_refs": candidate.get("evidence_routes", []),
            "source_refs": [],
            "evidence_gate": {
                "eligible": True,
                "route_model": "multiple_source_supported_routes",
                "evidence_routes": candidate.get("evidence_routes", []),
                "evidence_class": candidate.get("evidence_class"),
            },
            "semantic_review": {
                "recommendation": decision["recommendation"],
                "reason": decision["reason"],
                "novel_signal": decision.get("novel_signal"),
                "closest_published_cases": decision.get("closest_published_cases", []),
                "review_checks": decision.get("review_checks", []),
            },
            "human_decision": {
                "status": "pending_human_review",
                "decision": None,
                "reviewed_at": None,
                "reviewer_note": "",
            },
        })

    packet.sort(key=lambda item: (item["track"], item["level"], item["candidate_id"]))
    overlap = sorted({item["candidate_id"] for item in packet} & published)
    if overlap:
        raise SystemExit(f"Promotion packet candidate IDs overlap published cases: {overlap}")

    tracks = Counter(item["track"] for item in packet)
    levels = Counter(item["level"] for item in packet)
    return {
        "id": "sap-lead-candidate-promotion-review-packet",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "purpose": "Present every semantic-surviving assessment candidate in one human review packet before any published-case change.",
        "inputs": {
            "generated_candidates": "/labs/assessment/data/question-candidates.json",
            "generated_semantic_review": "/labs/assessment/data/candidate-semantic-review.json",
            "reasoning_gap_candidates": "/labs/assessment/data/reasoning-gap-candidates.json",
            "reasoning_gap_semantic_review": "/labs/assessment/data/reasoning-gap-semantic-review.json",
            "published_case_manifest": "/labs/assessment/data/case-sets.json"
        },
        "promotion_boundary": "Packet generation is read-only with respect to the published case manifest. Every item starts pending_human_review. A separate explicit human decision and a reviewed repository change are required to publish a case.",
        "review_rule": [
            "Confirm the candidate adds a materially new Lead reasoning signal.",
            "Confirm expected points match the requested reasoning level rather than only topic knowledge.",
            "Confirm evidence and human references support the load-bearing SAP facts or clearly mark author heuristics.",
            "Confirm closest published cases do not make the candidate redundant.",
            "Confirm red flags, follow-ups, and proof requirements are useful for an actual oral assessment.",
            "Decide approve, revise, or reject explicitly; no missing decision is treated as approval."
        ],
        "summary": {
            "published_case_count": manifest["total_cases"],
            "pending_candidates": len(packet),
            "generated_candidates": sum(item["candidate_source"] == "generated_failure_candidate" for item in packet),
            "reasoning_gap_candidates": sum(item["candidate_source"] == "reasoning_gap_candidate" for item in packet),
            "track_counts": dict(sorted(tracks.items())),
            "level_counts": dict(sorted(levels.items())),
            "semantic_duplicates_excluded": generated_semantic["summary"]["reject_semantic_duplicate"] + gap_semantic["summary"]["reject_semantic_duplicate"],
            "approved_candidates": 0,
        },
        "items": packet,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print("Stale or missing promotion review packet")
            return 2
        print(f"Promotion packet current: {data['summary']['pending_candidates']} pending candidates, {data['summary']['published_case_count']} published cases unchanged.")
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Generated promotion packet: {data['summary']['pending_candidates']} pending candidates, {data['summary']['published_case_count']} published cases unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
