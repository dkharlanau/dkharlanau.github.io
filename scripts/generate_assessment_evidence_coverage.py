#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
CATALOG_PATH = DATA / "catalog.json"
READINESS_PATH = DATA / "promotion-readiness.json"
FACTUAL_REVIEW_PATH = DATA / "factual-review.json"
OUTPUT_PATH = DATA / "evidence-coverage.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def evidence_applicable(route: str) -> bool:
    return route.startswith("/labs/enterprise-context/") or route in {"/labs/ai-ready/", "/labs/business-ai/"}


def track_entry_routes(track: dict[str, Any]) -> list[str]:
    return sorted({route for route in track.get("entry_points", []) if isinstance(route, str) and evidence_applicable(route)})


def build() -> dict[str, Any]:
    catalog = load_json(CATALOG_PATH)
    readiness = load_json(READINESS_PATH)
    factual = load_json(FACTUAL_REVIEW_PATH)
    readiness_by_route = {item["route"]: item for item in readiness["items"]}
    factual_claims_by_route = Counter(item["route"] for item in factual["claims"] if item.get("status") == "source_supported")

    route_track_count: Counter[str] = Counter()
    tracks: list[dict[str, Any]] = []
    unique_routes: set[str] = set()
    reviewed_unique: set[str] = set()
    p0_unique: set[str] = set()
    p1_unique: set[str] = set()

    for track in catalog["tracks"]:
        routes = track_entry_routes(track)
        for route in routes:
            route_track_count[route] += 1
            unique_routes.add(route)

        route_rows: list[dict[str, Any]] = []
        for route in routes:
            item = readiness_by_route.get(route)
            if item is None:
                route_rows.append({
                    "route": route,
                    "state": "missing_readiness_record",
                    "priority": "P0",
                    "evidence_status": "not_reviewed",
                    "reviewed_claims": 0,
                    "review_reason": "Route is in the assessment track but missing from promotion-readiness inventory.",
                })
                p0_unique.add(route)
                continue
            factual_state = item.get("factual_review", {})
            evidence_status = factual_state.get("status", "not_reviewed")
            reviewed_claims = factual_claims_by_route.get(route, 0)
            if evidence_status == "source_supported":
                reviewed_unique.add(route)
            if item["priority"] == "P0":
                p0_unique.add(route)
            if item["priority"] == "P1" and evidence_status == "source_supported":
                p1_unique.add(route)
            route_rows.append({
                "route": route,
                "state": item["state"],
                "priority": item["priority"],
                "evidence_status": evidence_status,
                "reviewed_claims": reviewed_claims,
                "structural_score": item["structural_score"],
                "review_reason": item.get("review_reason", ""),
            })

        source_reviewed = [row for row in route_rows if row["evidence_status"] == "source_supported"]
        evidence_debt = [row for row in route_rows if row["priority"] == "P0"]
        page_review_ready = [row for row in route_rows if row["priority"] == "P1" and row["evidence_status"] == "source_supported"]
        route_rows.sort(key=lambda row: ({"P0": 0, "P1": 1, "P2": 2}.get(row["priority"], 9), row["route"]))
        tracks.append({
            "id": track["id"],
            "label": track["label"],
            "evidence_applicable_routes": len(routes),
            "source_reviewed_routes": len(source_reviewed),
            "evidence_debt_routes": len(evidence_debt),
            "page_review_ready_routes": len(page_review_ready),
            "reviewed_claims": sum(row["reviewed_claims"] for row in route_rows),
            "coverage_percent": round((len(source_reviewed) / len(routes) * 100), 1) if routes else 100.0,
            "routes": route_rows,
        })

    focus: list[dict[str, Any]] = []
    for route in sorted(p0_unique):
        item = readiness_by_route.get(route, {})
        factual_state = item.get("factual_review", {})
        focus.append({
            "route": route,
            "assessment_track_count": route_track_count[route],
            "priority": item.get("priority", "P0"),
            "evidence_status": factual_state.get("status", "not_reviewed"),
            "structural_score": item.get("structural_score"),
            "review_reason": item.get("review_reason", "Missing readiness record."),
        })
    focus.sort(key=lambda row: (-row["assessment_track_count"], -(row["structural_score"] or 0), row["route"]))

    return {
        "id": "sap-lead-assessment-evidence-coverage",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "purpose": "Show primary-source review coverage and evidence debt across SAP Lead assessment tracks so the next review batch is selected from data rather than intuition.",
        "source_contracts": {
            "catalog": "/labs/assessment/data/catalog.json",
            "promotion_readiness": "/labs/assessment/data/promotion-readiness.json",
            "factual_review": "/labs/assessment/data/factual-review.json",
        },
        "boundary": "Evidence coverage measures claim-level source review, not page-level verification, learner knowledge, or publication readiness by itself.",
        "summary": {
            "unique_evidence_applicable_routes": len(unique_routes),
            "unique_source_reviewed_routes": len(reviewed_unique),
            "unique_p0_evidence_debt_routes": len(p0_unique),
            "unique_p1_page_review_ready_routes": len(p1_unique),
            "source_supported_claims": sum(1 for item in factual["claims"] if item.get("status") == "source_supported"),
            "coverage_percent": round((len(reviewed_unique) / len(unique_routes) * 100), 1) if unique_routes else 100.0,
        },
        "tracks": tracks,
        "next_focus": focus,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate evidence coverage across SAP Lead assessment tracks.")
    parser.add_argument("--check", action="store_true", help="Verify committed evidence coverage is current.")
    args = parser.parse_args()
    payload = build()
    rendered = serialize(payload)
    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"Missing evidence coverage: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        if OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(f"Stale evidence coverage: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        summary = payload["summary"]
        print(
            "Evidence coverage is current: "
            f"{summary['unique_source_reviewed_routes']}/{summary['unique_evidence_applicable_routes']} unique assessment routes source-reviewed; "
            f"{summary['unique_p0_evidence_debt_routes']} P0 evidence-debt route(s)."
        )
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    summary = payload["summary"]
    print(
        f"Generated {OUTPUT_PATH.relative_to(ROOT)}: "
        f"{summary['unique_source_reviewed_routes']}/{summary['unique_evidence_applicable_routes']} source-reviewed, "
        f"{summary['unique_p0_evidence_debt_routes']} P0 evidence-debt route(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
