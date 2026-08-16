#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PAGE = ROOT / "labs" / "assessment" / "human-review" / "findings" / "index.html"


def load(name: str):
    return json.loads((DATA / name).read_text(encoding="utf-8"))


def main() -> int:
    policy = load("human-review-policy.json")
    schema = load("human-review-finding-schema.json")
    queue = load("human-review-queue.json")
    page = PAGE.read_text(encoding="utf-8")
    errors: list[str] = []

    if policy.get("finding_contract") != "/labs/assessment/data/human-review-finding-schema.json":
        errors.append("Human review policy must reference the finding schema")
    if policy.get("findings_route") != "/labs/assessment/human-review/findings/":
        errors.append("Human review policy must reference the findings route")
    if len(policy.get("review_gates", [])) != 7:
        errors.append("Human review policy must keep seven explicit page-review gates")

    required = set(schema.get("required", []))
    for field in ("route", "reviewed_at", "gate_results", "findings", "disposition", "publication_effect"):
        if field not in required:
            errors.append(f"Finding schema is missing required field: {field}")
    publication = schema.get("properties", {}).get("publication_effect", {}).get("properties", {})
    for field in ("verified_changed", "indexing_changed", "status_changed"):
        if publication.get(field, {}).get("const") is not False:
            errors.append(f"Finding schema must force {field}=false")
    gate_results = schema.get("properties", {}).get("gate_results", {})
    if gate_results.get("minItems") != 7 or gate_results.get("maxItems") != 7:
        errors.append("Finding schema must require exactly seven gate results")

    if any(not str(item.get("route", "")).startswith("/labs/enterprise-context/") for item in queue.get("items", [])):
        errors.append("Human review queue contains a route outside Enterprise Context")

    for token in (
        "verified: false",
        "robots: noindex,follow",
        "/labs/assessment/data/human-review-policy.json",
        "/labs/assessment/data/human-review-queue.json",
        "/labs/assessment/data/factual-review.json",
        "publication_effect:{verified_changed:false,indexing_changed:false,status_changed:false}",
    ):
        if token not in page:
            errors.append(f"Human review findings page is missing token: {token}")
    if "localStorage" in page or ".setItem(" in page:
        errors.append("Human review finding recorder must not fabricate a persistent review store")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    print(f"Human review finding contract valid: {len(queue['items'])} queued routes, 7 gates, zero automatic publication effects.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
