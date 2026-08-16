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
EVIDENCE_PROFILE_PATH = DATA / "evidence-profile.json"
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
    profile = load_json(EVIDENCE_PROFILE_PATH)
    readiness_by_route = {item["route"]: item for item in readiness["items"]}
    factual_claims_by_route = Counter(item["route"] for item in factual["claims"] if item.get("status") == "source_supported")

    route_track_count: Counter[str] = Counter()
    tracks: list[dict[str, Any]] = []
    unique_routes: set[str] = set()
    required_unique: set[str] = set()
    reviewed_unique: set[str] = set()
    p0_unique: set[str] = set()
    p1_unique: set[str] = set()
    selective_unique: set[str] = set()

    for track in catalog["tracks"]:
        routes = track_entry_routes(track)
        for route in routes:
            route_track_count[route] += 1
            unique_routes.add(route)

        rows: list[dict[str, Any]] = []
        for route in routes:
            item = readiness_by_route.get(route)
            if item is None:
                rows.append({"route": route, "state": "missing_readiness_record", "priority": "P0", "evidence_status": "not_reviewed", "reviewed_claims": 0, "external_review_required": True, "expected_evidence_classes": [], "review_reason": "Route is in the assessment track but missing from promotion-readiness inventory."})
                required_unique.add(route)
                p0_unique.add(route)
                continue
            evidence_profile = item.get("evidence_profile", {})
            external_required = bool(evidence_profile.get("counts_as_source_review_debt", False))
            if external_required:
                required_unique.add(route)
            else:
                selective_unique.add(route)
            factual_state = item.get("factual_review", {})
            evidence_status = factual_state.get("status", "not_reviewed")
            reviewed_claims = factual_claims_by_route.get(route, 0)
            if evidence_status == "source_supported":
                reviewed_unique.add(route)
            if external_required and item["priority"] == "P0":
                p0_unique.add(route)
            if item["priority"] == "P1" and evidence_status == "source_supported":
                p1_unique.add(route)
            rows.append({
                "route": route,
                "state": item["state"],
                "priority": item["priority"],
                "evidence_status": evidence_status,
                "reviewed_claims": reviewed_claims,
                "external_review_required": external_required,
                "external_review_mode": evidence_profile.get("external_review_mode"),
                "expected_evidence_classes": evidence_profile.get("expected_evidence_classes", []),
                "structural_score": item["structural_score"],
                "review_reason": item.get("review_reason", ""),
            })

        required_rows = [row for row in rows if row["external_review_required"]]
        source_reviewed = [row for row in required_rows if row["evidence_status"] == "source_supported"]
        evidence_debt = [row for row in required_rows if row["priority"] == "P0"]
        selective_rows = [row for row in rows if not row["external_review_required"]]
        page_review_ready = [row for row in rows if row["priority"] == "P1" and row["evidence_status"] == "source_supported"]
        rows.sort(key=lambda row: ({"P0": 0, "P1": 1, "P2": 2}.get(row["priority"], 9), row["route"]))
        tracks.append({
            "id": track["id"],
            "label": track["label"],
            "evidence_profile_routes": len(rows),
            "externally_review_required_routes": len(required_rows),
            "selective_or_heuristic_routes": len(selective_rows),
            "source_reviewed_routes": len(source_reviewed),
            "evidence_debt_routes": len(evidence_debt),
            "page_review_ready_routes": len(page_review_ready),
            "reviewed_claims": sum(row["reviewed_claims"] for row in rows),
            "coverage_percent": round((len(source_reviewed) / len(required_rows) * 100), 1) if required_rows else 100.0,
            "routes": rows,
        })

    focus: list[dict[str, Any]] = []
    for route in sorted(p0_unique):
        item = readiness_by_route.get(route, {})
        factual_state = item.get("factual_review", {})
        evidence_profile = item.get("evidence_profile", {})
        focus.append({
            "route": route,
            "assessment_track_count": route_track_count[route],
            "priority": item.get("priority", "P0"),
            "evidence_status": factual_state.get("status", "not_reviewed"),
            "expected_evidence_classes": evidence_profile.get("expected_evidence_classes", []),
            "structural_score": item.get("structural_score"),
            "review_reason": item.get("review_reason", "Missing readiness record."),
        })
    focus.sort(key=lambda row: (-row["assessment_track_count"], -(row["structural_score"] or 0), row["route"]))

    return {
        "id": "sap-lead-assessment-evidence-coverage",
        "version": "1.1.0",
        "updated_at": "2026-08-16",
        "purpose": "Show primary-source review coverage and evidence debt across SAP Lead assessment tracks while distinguishing routes that mainly use standards, research, or explicit author heuristics.",
        "source_contracts": {
            "catalog": "/labs/assessment/data/catalog.json",
            "promotion_readiness": "/labs/assessment/data/promotion-readiness.json",
            "factual_review": "/labs/assessment/data/factual-review.json",
            "evidence_profile": "/labs/assessment/data/evidence-profile.json"
        },
        "boundary": "Coverage counts only routes whose evidence profile requires external source review. Selective or heuristic routes are shown separately and are not treated as missing SAP product evidence.",
        "summary": {
            "unique_profiled_routes": len(unique_routes),
            "unique_externally_review_required_routes": len(required_unique),
            "unique_selective_or_heuristic_routes": len(selective_unique),
            "unique_source_reviewed_routes": len(reviewed_unique & required_unique),
            "unique_p0_evidence_debt_routes": len(p0_unique),
            "unique_p1_page_review_ready_routes": len(p1_unique),
            "source_supported_claims": sum(1 for item in factual["claims"] if item.get("status") == "source_supported"),
            "coverage_percent": round((len(reviewed_unique & required_unique) / len(required_unique) * 100), 1) if required_unique else 100.0
        },
        "tracks": tracks,
        "next_focus": focus,
        "evidence_classes": profile.get("evidence_classes", [])
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate profile-aware evidence coverage across SAP Lead assessment tracks.")
    parser.add_argument("--check", action="store_true", help="Verify committed evidence coverage is current.")
    args = parser.parse_args()
    payload = build()
    rendered = serialize(payload)
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print(f"Stale or missing evidence coverage: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        summary = payload["summary"]
        print(f"Evidence coverage is current: {summary['unique_source_reviewed_routes']}/{summary['unique_externally_review_required_routes']} required routes source-reviewed; {summary['unique_p0_evidence_debt_routes']} P0 evidence-debt route(s).")
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    summary = payload["summary"]
    print(f"Generated {OUTPUT_PATH.relative_to(ROOT)}: {summary['unique_source_reviewed_routes']}/{summary['unique_externally_review_required_routes']} required routes source-reviewed, {summary['unique_selective_or_heuristic_routes']} selective/heuristic route(s), {summary['unique_p0_evidence_debt_routes']} P0 debt route(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
