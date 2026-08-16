#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
QUEUE_PATH = DATA / "human-review-queue.json"
CATALOG_PATH = DATA / "catalog.json"
CASE_SETS_PATH = DATA / "case-sets.json"
OUTPUT_PATH = DATA / "secondary-review-priority.json"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def published_cases() -> list[dict[str, Any]]:
    manifest = load_json(CASE_SETS_PATH)
    rows: list[dict[str, Any]] = []
    for case_set in manifest["sets"]:
        rows.extend(load_jsonl(ROOT / case_set["url"].lstrip("/")))
    return rows


def catalog_route_tracks(catalog: dict[str, Any]) -> dict[str, set[str]]:
    result: dict[str, set[str]] = {}
    for track in catalog.get("tracks", []):
        track_id = str(track.get("id", ""))
        for route in track.get("entry_points", []):
            result.setdefault(str(route), set()).add(track_id)
    return result


def build() -> dict[str, Any]:
    queue = load_json(QUEUE_PATH)
    catalog = load_json(CATALOG_PATH)
    cases = published_cases()
    catalog_tracks = catalog_route_tracks(catalog)
    secondary = [item for item in queue["items"] if item.get("wave") == "secondary"]

    items: list[dict[str, Any]] = []
    for item in secondary:
        route = item["route"]
        direct_cases = [case for case in cases if route in case.get("human_refs", [])]
        direct_case_ids = sorted(case["id"] for case in direct_cases)
        case_tracks = sorted({str(case.get("track", "")) for case in direct_cases if case.get("track")})
        route_catalog_tracks = sorted(catalog_tracks.get(route, set()))
        all_tracks = sorted(set(case_tracks) | set(route_catalog_tracks) | {item["track"]})
        claims = int(item.get("source_supported_claims", 0) or 0)

        score_components = {
            "direct_case_reuse": len(direct_case_ids) * 4,
            "case_track_breadth": len(case_tracks) * 3,
            "catalog_track_reuse": len(route_catalog_tracks) * 2,
            "source_supported_claims": min(claims, 4),
        }
        score = sum(score_components.values())
        items.append({
            "route": route,
            "track": item["track"],
            "source_review_status": item["source_review_status"],
            "page_verified": item["page_verified"],
            "source_supported_claims": claims,
            "direct_published_case_count": len(direct_case_ids),
            "direct_published_case_ids": direct_case_ids,
            "case_tracks": case_tracks,
            "catalog_tracks": route_catalog_tracks,
            "assessment_tracks": all_tracks,
            "cross_track_reuse": len(all_tracks),
            "score_components": score_components,
            "priority_score": score,
        })

    items.sort(key=lambda row: (-row["priority_score"], -row["direct_published_case_count"], row["route"]))
    for index, item in enumerate(items, start=1):
        item["priority_position"] = index
        if index <= 5:
            item["review_wave"] = "secondary_high"
        elif index <= 10:
            item["review_wave"] = "secondary_medium"
        else:
            item["review_wave"] = "secondary_later"
        signals = []
        if item["direct_published_case_count"]:
            signals.append(f"{item['direct_published_case_count']} published case(s) directly reuse this route")
        if item["cross_track_reuse"] > 1:
            signals.append(f"reused across {item['cross_track_reuse']} assessment track(s)")
        if item["source_supported_claims"]:
            signals.append(f"{item['source_supported_claims']} source-supported claim(s) already reviewed")
        if not signals:
            signals.append("source-supported secondary route with limited direct practice reuse")
        item["review_reason"] = "; ".join(signals) + "."

    return {
        "id": "sap-lead-secondary-human-review-priority",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "purpose": "Rank source-supported secondary human-review routes by direct assessment reuse and cross-track value after the Core 12 wave.",
        "inputs": {
            "human_review_queue": "/labs/assessment/data/human-review-queue.json",
            "case_manifest": "/labs/assessment/data/case-sets.json",
            "catalog": "/labs/assessment/data/catalog.json"
        },
        "boundary": "Priority changes review order only. It never changes page verification, indexing, status, factual-review state, or publication policy.",
        "scoring_rule": {
            "direct_case_reuse": "4 points per published case whose human_refs include the route",
            "case_track_breadth": "3 points per distinct assessment track among those direct published cases",
            "catalog_track_reuse": "2 points per catalog track that lists the route as an entry point",
            "source_supported_claims": "1 point per source-supported reviewed claim, capped at 4",
            "tie_break": "higher direct case count, then route name"
        },
        "summary": {
            "secondary_routes": len(items),
            "high_priority": sum(item["review_wave"] == "secondary_high" for item in items),
            "medium_priority": sum(item["review_wave"] == "secondary_medium" for item in items),
            "later_priority": sum(item["review_wave"] == "secondary_later" for item in items),
            "routes_with_direct_cases": sum(item["direct_published_case_count"] > 0 for item in items),
            "all_source_supported": all(item["source_review_status"] == "source_supported" for item in items),
            "all_unverified": all(item["page_verified"] is False for item in items),
        },
        "items": items,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = build()
    rendered = json.dumps(generated, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT_PATH.exists() or OUTPUT_PATH.read_text(encoding="utf-8") != rendered:
            print("Stale or missing secondary human-review priority dataset")
            return 2
        print(f"Secondary review priority is current: {generated['summary']['secondary_routes']} routes ranked.")
        return 0
    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(f"Generated secondary human-review priority: {generated['summary']['secondary_routes']} routes ranked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
