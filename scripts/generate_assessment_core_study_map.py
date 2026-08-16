#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
CONTRACT = DATA / "core-study-contract.json"
FACTUAL = DATA / "factual-review.json"
PROMOTION = DATA / "promotion-readiness.json"
HUMAN_QUEUE = DATA / "human-review-queue.json"
CASE_SETS = DATA / "case-sets.json"
OUTPUT = DATA / "core-study-map.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def published_cases() -> list[dict[str, Any]]:
    manifest = load_json(CASE_SETS)
    rows: list[dict[str, Any]] = []
    for case_set in manifest["sets"]:
        rows.extend(load_jsonl(ROOT / case_set["url"].lstrip("/")))
    return rows


def factual_by_route() -> dict[str, dict[str, Any]]:
    payload = load_json(FACTUAL)
    return {str(row["route"]): row for row in payload.get("routes", []) if row.get("route")}


def promotion_by_route() -> dict[str, dict[str, Any]]:
    payload = load_json(PROMOTION)
    return {str(row["route"]): row for row in payload.get("items", []) if row.get("route")}


def queue_by_route() -> dict[str, dict[str, Any]]:
    payload = load_json(HUMAN_QUEUE)
    return {str(row["route"]): row for row in payload.get("items", []) if row.get("route")}


def generate() -> dict[str, Any]:
    contract = load_json(CONTRACT)
    factual = factual_by_route()
    promotion = promotion_by_route()
    queue = queue_by_route()
    cases = published_cases()
    wave_defs = {wave["id"]: wave for wave in contract["waves"]}

    items: list[dict[str, Any]] = []
    linked_case_ids: set[str] = set()
    for route in sorted(contract["routes"], key=lambda row: int(row["order"])):
        route_path = str(route["route"])
        evidence = factual.get(route_path, {})
        publication = promotion.get(route_path, {})
        review = queue.get(route_path, {})
        direct_cases = [
            case for case in cases
            if route_path in set(case.get("human_refs", []))
        ]
        direct_case_ids = [str(case["id"]) for case in direct_cases]
        linked_case_ids.update(direct_case_ids)
        items.append(
            {
                **route,
                "wave_label": wave_defs[route["wave"]]["label"],
                "wave_goal": wave_defs[route["wave"]]["goal"],
                "evidence": {
                    "status": evidence.get("status", evidence.get("review_status", "unknown")),
                    "review_status": evidence.get("review_status", "unknown"),
                    "reviewed_at": evidence.get("reviewed_at"),
                    "reviewed_claims": len(evidence.get("claim_ids", [])),
                    "human_verification_required": bool(evidence.get("human_verification_required", True)),
                },
                "publication": {
                    "state": publication.get("state", "unknown"),
                    "verified": bool(publication.get("verified", False)),
                    "status": publication.get("status"),
                    "robots": publication.get("robots"),
                    "sitemap": publication.get("sitemap"),
                    "priority": publication.get("priority"),
                },
                "review_queue": {
                    "queue_position": review.get("queue_position"),
                    "wave": review.get("wave"),
                    "focus": review.get("focus"),
                },
                "published_practice": {
                    "case_count": len(direct_case_ids),
                    "case_ids": direct_case_ids,
                },
            }
        )

    wave_counts = Counter(item["wave"] for item in items)
    track_counts = Counter(item["track"] for item in items)
    return {
        "id": "sap-lead-core-study-map",
        "version": "1.1.0",
        "updated_at": contract["updated_at"],
        "purpose": contract["purpose"],
        "study_rule": contract["study_rule"],
        "boundary": "This map organizes assessment study. Claim evidence comes from factual review, while current publication state comes from Promotion Readiness. The generator changes neither source.",
        "source_contracts": {
            "factual_review": "/labs/assessment/data/factual-review.json",
            "promotion_readiness": "/labs/assessment/data/promotion-readiness.json",
            "human_review_queue": "/labs/assessment/data/human-review-queue.json"
        },
        "summary": {
            "core_routes": len(items),
            "waves": len(contract["waves"]),
            "source_supported_routes": sum(item["evidence"]["review_status"] == "primary_source_review_complete" for item in items),
            "page_verified_routes": sum(item["publication"]["verified"] for item in items),
            "public_or_indexable_routes": sum(item["publication"]["state"] == "public_or_indexable" for item in items),
            "queued_for_human_review_routes": sum(item["review_queue"]["queue_position"] is not None for item in items),
            "direct_published_cases": len(linked_case_ids),
            "wave_counts": dict(sorted(wave_counts.items())),
            "track_counts": dict(sorted(track_counts.items())),
        },
        "waves": contract["waves"],
        "items": items,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the SAP Lead Core 12 study map.")
    parser.add_argument("--check", action="store_true", help="Verify the committed study map is current.")
    args = parser.parse_args()
    payload = generate()
    rendered = serialize(payload)
    if args.check:
        if not OUTPUT.exists():
            print(f"Missing generated study map: {OUTPUT.relative_to(ROOT)}")
            return 2
        if OUTPUT.read_text(encoding="utf-8") != rendered:
            print(f"Stale generated study map: {OUTPUT.relative_to(ROOT)}")
            return 2
        print(
            f"Core study map is current: {payload['summary']['core_routes']} routes, "
            f"{payload['summary']['direct_published_cases']} directly linked published cases, "
            f"{payload['summary']['page_verified_routes']} verified route(s)."
        )
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(
        f"Generated {OUTPUT.relative_to(ROOT)}: {payload['summary']['core_routes']} routes, "
        f"{payload['summary']['direct_published_cases']} directly linked published cases, "
        f"{payload['summary']['page_verified_routes']} verified route(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
