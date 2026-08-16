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

    if review["summary"]["reviewed_candidates"] != len(review["decisions"]):
        errors.append("Reasoning-gap semantic review count mismatch")
    if review["summary"]["published_case_change"] != 0:
        errors.append("Semantic review must not change the published case set")
    if set(item["candidate_id"] for item in review["decisions"]) != set(candidate_by_id):
        errors.append("Semantic review must cover every non-diagnostic reasoning-gap candidate exactly once")

    for item in review["decisions"]:
        cid = item["candidate_id"]
        candidate = candidate_by_id.get(cid)
        if not candidate:
            continue
        if item["recommendation"] not in {"retain_for_human_promotion_review", "reject_semantic_duplicate"}:
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

    if review["summary"]["retain_for_human_promotion_review"] != 2:
        errors.append("Both current Design/Challenge gap candidates should remain in human promotion review")
    if review["summary"]["reject_semantic_duplicate"] != 0:
        errors.append("Current Design/Challenge gap review should have zero semantic duplicates")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print("Reasoning-gap semantic review valid: 2 retained for human promotion review, published cases unchanged.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
