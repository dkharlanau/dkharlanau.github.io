#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
PROMOTION = DATA / "promotion-readiness.json"
FACTUAL = DATA / "factual-review.json"
COVERAGE = DATA / "evidence-coverage.json"
POLICY = DATA / "human-review-policy.json"
OUTPUT = DATA / "human-review-queue.json"

CORE_ORDER = [
    "/labs/enterprise-context/sales-order/",
    "/labs/enterprise-context/pricing/",
    "/labs/enterprise-context/procurement/",
    "/labs/enterprise-context/atp/",
    "/labs/enterprise-context/shipping/",
    "/labs/enterprise-context/production/",
    "/labs/enterprise-context/integration-operations/",
    "/labs/enterprise-context/inventory-management/",
    "/labs/enterprise-context/quality-management/",
    "/labs/enterprise-context/ewm/",
    "/labs/enterprise-context/mdg/",
    "/labs/enterprise-context/finance-logistics/",
]

FOCUS = {
    "/labs/enterprise-context/sales-order/": "Determination inputs, document behavior, ownership boundaries, and diagnostic proof.",
    "/labs/enterprise-context/pricing/": "Condition technique, pricing analysis, extension boundaries, and order-to-billing parity.",
    "/labs/enterprise-context/procurement/": "Source determination, purchasing controls, receipt/invoice boundaries, and GR/IR reasoning.",
    "/labs/enterprise-context/atp/": "Confirmation logic, aATP capabilities, protection/allocation boundaries, and stock-versus-availability reasoning.",
    "/labs/enterprise-context/shipping/": "Shipping point and route decisions, delivery execution, split causes, and warehouse handoff.",
    "/labs/enterprise-context/production/": "MRP-to-order reasoning, production method selection, staging, confirmation, goods receipt, and settlement boundary.",
    "/labs/enterprise-context/integration-operations/": "Message identity, ordering, retries, monitoring, reconciliation, and technical-versus-business completion.",
    "/labs/enterprise-context/inventory-management/": "Movement and stock-state semantics, valuation effects, special stock, and IM-to-EWM boundary.",
    "/labs/enterprise-context/quality-management/": "Inspection trigger, lot lifecycle, usage decision, stock disposition, and logistics integration.",
    "/labs/enterprise-context/ewm/": "ERP/EWM ownership, warehouse task/order semantics, staging, confirmations, and deployment boundary.",
    "/labs/enterprise-context/mdg/": "Governance modes, authority, validation, replication boundary, and release/deployment limitations.",
    "/labs/enterprise-context/finance-logistics/": "Physical-versus-financial completion, accounting handoffs, GR/IR, settlement, and reconciliation.",
}


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def route_tracks(coverage: dict[str, Any]) -> dict[str, str]:
    result: dict[str, str] = {}
    for track in coverage.get("tracks", []):
        track_id = str(track.get("id", ""))
        for item in track.get("routes", []):
            route = item.get("route")
            if route and route not in result:
                result[str(route)] = track_id
    return result


def factual_by_route(factual: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {str(item["route"]): item for item in factual.get("routes", []) if item.get("route")}


def generate() -> dict[str, Any]:
    promotion = load(PROMOTION)
    factual = load(FACTUAL)
    coverage = load(COVERAGE)
    policy = load(POLICY)

    tracks = route_tracks(coverage)
    factual_routes = factual_by_route(factual)
    core_rank = {route: index for index, route in enumerate(CORE_ORDER, start=1)}

    queue: list[dict[str, Any]] = []
    for item in promotion.get("items", []):
        route = str(item.get("route", ""))
        factual_state = item.get("factual_review", {})
        evidence_profile = item.get("evidence_profile", {})
        if item.get("state") != "human_review_candidate":
            continue
        if item.get("priority") != "P1":
            continue
        if factual_state.get("status") != "source_supported":
            continue
        if not evidence_profile.get("external_review_required", False):
            continue

        reviewed = factual_routes.get(route, {})
        claim_count = int(factual_state.get("claim_count", reviewed.get("claim_count", 0)) or 0)
        rank = core_rank.get(route, 1000)
        wave = "core_assessment" if route in core_rank else "secondary"
        queue.append(
            {
                "route": route,
                "track": tracks.get(route, "cross-track"),
                "wave": wave,
                "rank": rank,
                "state": "queued_for_human_review",
                "source_review_status": "source_supported",
                "source_supported_claims": claim_count,
                "page_verified": False,
                "focus": FOCUS.get(
                    route,
                    "Check the page against its reviewed claims, release scope, ownership boundaries, and machine-readable model.",
                ),
                "review_gates": list(policy["review_gates"]),
                "completion_rule": policy["completion_rule"],
            }
        )

    queue.sort(key=lambda row: (row["rank"], row["track"], row["route"]))
    for index, row in enumerate(queue, start=1):
        row["queue_position"] = index

    track_counts = Counter(row["track"] for row in queue)
    wave_counts = Counter(row["wave"] for row in queue)
    return {
        "id": "sap-lead-human-review-queue",
        "version": "1.0.0",
        "updated_at": policy["updated_at"],
        "policy": "/labs/assessment/data/human-review-policy.json",
        "inputs": {
            "promotion_readiness": "/labs/assessment/data/promotion-readiness.json",
            "factual_review": "/labs/assessment/data/factual-review.json",
            "evidence_coverage": "/labs/assessment/data/evidence-coverage.json",
        },
        "boundary": "This queue schedules human review only. It never changes page verification, indexing, status, or publication flags.",
        "summary": {
            "queued_routes": len(queue),
            "core_assessment_wave": wave_counts.get("core_assessment", 0),
            "secondary_wave": wave_counts.get("secondary", 0),
            "track_counts": dict(sorted(track_counts.items())),
        },
        "items": queue,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate the SAP Lead assessment human-review queue.")
    parser.add_argument("--check", action="store_true", help="Verify the committed queue is current.")
    args = parser.parse_args()

    rendered = serialize(generate())
    if args.check:
        if not OUTPUT.exists():
            print(f"Missing generated queue: {OUTPUT.relative_to(ROOT)}")
            return 2
        if OUTPUT.read_text(encoding="utf-8") != rendered:
            print(f"Stale generated queue: {OUTPUT.relative_to(ROOT)}")
            return 2
        payload = json.loads(rendered)
        print(f"Human-review queue is current: {payload['summary']['queued_routes']} routes.")
        return 0

    OUTPUT.write_text(rendered, encoding="utf-8")
    payload = json.loads(rendered)
    print(f"Generated {OUTPUT.relative_to(ROOT)}: {payload['summary']['queued_routes']} routes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
