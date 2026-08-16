#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"


def load_json(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> None:
    review = load_json("candidate-semantic-review.json")
    inventory = load_json("question-candidates.json")
    manifest = load_json("case-sets.json")

    published = []
    for case_set in manifest["sets"]:
        published.extend(load_jsonl(ROOT / case_set["url"].lstrip("/")))
    published_by_id = {item["id"]: item for item in published}
    candidates = {item["id"]: item for item in inventory["items"]}

    assert review["summary"]["published_case_change"] == 0
    assert manifest["total_cases"] == inventory["published_case_count"]
    assert review["review_scope"]["reviewed_candidates"] == len(review["decisions"])

    allowed = {"retain_for_human_promotion_review", "reject_semantic_duplicate"}
    for decision in review["decisions"]:
        cid = decision["candidate_id"]
        assert cid in candidates, cid
        assert candidates[cid]["status"] == "candidate", cid
        assert decision["recommendation"] in allowed
        assert decision["reason"]
        assert decision["review_checks"]
        for case_id in decision["closest_published_cases"]:
            assert case_id in published_by_id, case_id

    cost = next(item for item in review["decisions"] if item["candidate_id"] == "CAND-PP-COST")
    assert cost["recommendation"] == "reject_semantic_duplicate"
    assert "ASSESS-FIN-005" in cost["closest_published_cases"]
    active_candidate_ids = {item["id"] for item in inventory["items"] if item["status"] == "candidate"}
    decision_ids = {item["candidate_id"] for item in review["decisions"]}
    assert decision_ids == active_candidate_ids, (sorted(decision_ids), sorted(active_candidate_ids))
    assert review["summary"]["retain_for_human_promotion_review"] == 5
    assert review["summary"]["reject_semantic_duplicate"] == 2
    raw_mcp = next(item for item in review["decisions"] if item["candidate_id"] == "CAND-AIAG-RAW-MCP")
    overprivileged = next(item for item in review["decisions"] if item["candidate_id"] == "CAND-AIAG-OVERPRIVILEGED")
    assert raw_mcp["recommendation"] == "retain_for_human_promotion_review"
    assert overprivileged["recommendation"] == "reject_semantic_duplicate"
    assert "ASSESS-AI-003" in overprivileged["closest_published_cases"]

    print("Candidate semantic review valid: all active generated candidates reviewed; 5 retained, 2 semantic duplicates, published cases unchanged.")


if __name__ == "__main__":
    main()
