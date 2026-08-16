#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"

def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))

def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]

def main() -> int:
    review = load("reasoning-gap-semantic-review.json")
    candidates = load("reasoning-gap-candidates.json")
    manifest = load("case-sets.json")
    errors: list[str] = []

    candidate_by_id = {item["id"]: item for item in candidates["candidates"]}
    published = {}
    for case_set in manifest["sets"]:
        for row in load_jsonl(ROOT / case_set["url"].lstrip("/")):
            published[row["id"]] = row

    decisions = review["decisions"]
    if review["summary"]["reviewed_candidates"] != len(decisions):
        errors.append("Reasoning-gap semantic review count mismatch")
    if review["summary"]["published_case_change"] != 0:
        errors.append("Semantic review must not change the published case set")
    if {item["candidate_id"] for item in decisions} != set(candidate_by_id):
        errors.append("Semantic review must cover every current reasoning-gap candidate exactly once")

    retained = 0
    rejected = 0
    for item in decisions:
        cid = item["candidate_id"]
        candidate = candidate_by_id.get(cid)
        if not candidate:
            continue
        if item["recommendation"] == "retain_for_human_promotion_review":
            retained += 1
        elif item["recommendation"] == "reject_semantic_duplicate":
            rejected += 1
        else:
            errors.append(f"Unsupported semantic recommendation: {cid}")
        if not item.get("reason") or not item.get("novel_signal"):
            errors.append(f"Semantic review requires reason and novel signal: {cid}")
        if len(item.get("review_checks", [])) < 3:
            errors.append(f"Semantic review requires at least three review checks: {cid}")
        for published_id in item.get("closest_published_cases", []):
            if published_id not in published:
                errors.append(f"Closest published case does not exist: {published_id}")
        if cid in published:
            errors.append(f"Review-stage candidate unexpectedly published: {cid}")

    if review["summary"]["retain_for_human_promotion_review"] != retained:
        errors.append("Retained-candidate summary count mismatch")
    if review["summary"]["reject_semantic_duplicate"] != rejected:
        errors.append("Rejected-candidate summary count mismatch")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Reasoning-gap semantic review valid: {retained} retained, {rejected} rejected, published cases unchanged.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
