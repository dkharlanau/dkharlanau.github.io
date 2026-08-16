#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "promotion-review" / "index.html"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def load_jsonl(path: Path):
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    packet = load("promotion-review-packet.json")
    generated_semantic = load("candidate-semantic-review.json")
    gap_semantic = load("reasoning-gap-semantic-review.json")
    manifest = load("case-sets.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    expected_generated = {
        item["candidate_id"] for item in generated_semantic["decisions"]
        if item["recommendation"] == "retain_for_human_promotion_review"
    }
    expected_gap = {
        item["candidate_id"] for item in gap_semantic["decisions"]
        if item["recommendation"] == "retain_for_human_promotion_review"
    }
    expected = expected_generated | expected_gap
    actual = {item["candidate_id"] for item in packet["items"]}
    if actual != expected:
        errors.append(f"Promotion packet mismatch: expected {sorted(expected)}, got {sorted(actual)}")

    published_ids = set()
    for case_set in manifest["sets"]:
        published_ids.update(item["id"] for item in load_jsonl(ROOT / case_set["url"].lstrip("/")))
    if actual & published_ids:
        errors.append(f"Promotion packet overlaps published cases: {sorted(actual & published_ids)}")
    if packet["summary"]["published_case_count"] != manifest["total_cases"]:
        errors.append("Promotion packet published count does not match manifest")
    if packet["summary"]["pending_candidates"] != len(packet["items"]):
        errors.append("Promotion packet pending count mismatch")
    if packet["summary"]["approved_candidates"] != 0:
        errors.append("Generated promotion packet must contain zero approvals")

    for item in packet["items"]:
        decision = item.get("human_decision", {})
        if decision.get("status") != "pending_human_review":
            errors.append(f"Candidate is not pending human review: {item['candidate_id']}")
        if decision.get("decision") is not None or decision.get("reviewed_at") is not None:
            errors.append(f"Candidate contains an automatic human decision: {item['candidate_id']}")
        if item.get("semantic_review", {}).get("recommendation") != "retain_for_human_promotion_review":
            errors.append(f"Packet includes a non-retained semantic decision: {item['candidate_id']}")
        if not item.get("semantic_review", {}).get("novel_signal"):
            errors.append(f"Candidate is missing a semantic novelty signal: {item['candidate_id']}")
        if item.get("evidence_gate", {}).get("eligible") is not True:
            errors.append(f"Candidate is not evidence eligible: {item['candidate_id']}")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/promotion-review-packet.json",
        "Zero automatic approvals",
    ):
        if token not in page:
            errors.append(f"Promotion review page missing token: {token}")

    result = subprocess.run(
        [sys.executable, "scripts/generate_assessment_promotion_review_packet.py", "--check"],
        cwd=ROOT, text=True, capture_output=True, check=False,
    )
    if result.returncode != 0:
        errors.append(result.stdout + result.stderr)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Promotion review packet valid: {len(packet['items'])} pending candidates, {manifest['total_cases']} published cases unchanged, zero approvals.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
