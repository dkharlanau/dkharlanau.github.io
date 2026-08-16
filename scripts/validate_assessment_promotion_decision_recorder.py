#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "promotion-review" / "decision" / "index.html"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    schema = load("promotion-decision-schema.json")
    packet = load("promotion-review-packet.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    required = set(schema.get("required", []))
    for field in ("candidate_id", "decided_at", "decision", "review_checks", "reviewer_note", "publication_effect"):
        if field not in required:
            errors.append(f"Promotion decision schema missing required field: {field}")
    effects = schema["properties"]["publication_effect"]["properties"]
    for field in ("case_manifest_changed", "case_published", "calibration_changed"):
        if effects[field].get("const") is not False:
            errors.append(f"Promotion decision schema must force {field}=false")
    checks = schema["properties"]["review_checks"]
    if checks.get("minItems") != 6 or checks.get("maxItems") != 6:
        errors.append("Promotion decision schema must require exactly six review checks")
    decisions = set(schema["properties"]["decision"]["enum"])
    if decisions != {"approve_for_separate_repository_change", "revise_before_promotion", "reject_candidate"}:
        errors.append("Promotion decision outcomes changed unexpectedly")
    if packet["summary"]["approved_candidates"] != 0:
        errors.append("Decision recorder requires a source packet with zero automatic approvals")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/promotion-decision-schema.json",
        "/labs/assessment/data/promotion-review-packet.json",
        "publication_effect:{case_manifest_changed:false,case_published:false,calibration_changed:false}",
        "approve_for_separate_repository_change",
    ):
        if token not in page:
            errors.append(f"Promotion decision page missing token: {token}")
    if "localStorage" in page or ".setItem(" in page:
        errors.append("Promotion decision recorder must not invent a persistent approval store")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Promotion decision recorder valid: {len(packet['items'])} selectable pending candidates, six checks, zero automatic publication effects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
