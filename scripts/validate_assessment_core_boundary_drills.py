#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
DRILLS = DATA / "core-boundary-drills.json"
CORE = DATA / "core-study-map.json"
CASE_SETS = DATA / "case-sets.json"

ALLOWED_LEVELS = {"trace", "diagnose", "design", "challenge"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def published_case_ids() -> set[str]:
    manifest = load_json(CASE_SETS)
    ids: set[str] = set()
    for case_set in manifest["sets"]:
        path = ROOT / case_set["url"].lstrip("/")
        ids.update(str(row["id"]) for row in load_jsonl(path))
    return ids


def validate() -> list[str]:
    errors: list[str] = []
    payload = load_json(DRILLS)
    core = load_json(CORE)
    manifest = load_json(CASE_SETS)

    drills = payload.get("drills", [])
    if len(drills) < 8:
        errors.append(f"Expected at least 8 boundary drills, found {len(drills)}")

    core_routes = {
        str(item["route"]): item
        for item in core.get("items", [])
        if item.get("route")
    }
    if len(core_routes) != 12:
        errors.append(f"Core study map must expose 12 routes, found {len(core_routes)}")

    ids = [str(item.get("id", "")) for item in drills]
    if len(ids) != len(set(ids)):
        errors.append("Boundary drill IDs must be unique")

    published_ids = published_case_ids()
    overlap = sorted(set(ids) & published_ids)
    if overlap:
        errors.append(f"Boundary drill IDs overlap published cases: {overlap}")

    serialized_manifest = json.dumps(manifest, ensure_ascii=False)
    if "core-boundary-drills" in serialized_manifest or "CORE-X-" in serialized_manifest:
        errors.append("Published case manifest must not reference Core boundary drills")

    for index, drill in enumerate(drills, start=1):
        did = str(drill.get("id", ""))
        prefix = f"Drill {index} ({did or 'missing id'})"
        if not re.fullmatch(r"CORE-X-\d{3}", did):
            errors.append(f"{prefix}: id must match CORE-X-NNN")
        if drill.get("level") not in ALLOWED_LEVELS:
            errors.append(f"{prefix}: unsupported level {drill.get('level')!r}")

        routes = drill.get("routes", [])
        if not isinstance(routes, list) or len(routes) < 2:
            errors.append(f"{prefix}: must cross at least two routes")
            routes = []
        if len(routes) != len(set(routes)):
            errors.append(f"{prefix}: route references must be unique")
        for route in routes:
            core_item = core_routes.get(str(route))
            if not core_item:
                errors.append(f"{prefix}: route is outside Core 12: {route}")
                continue
            evidence = core_item.get("evidence", {})
            if evidence.get("review_status") != "primary_source_review_complete":
                errors.append(f"{prefix}: route is not source-supported: {route}")
            if evidence.get("page_verified") is not False:
                errors.append(f"{prefix}: route page_verified must remain false: {route}")

        for field in ("title", "scenario", "prompt", "boundary_question"):
            value = drill.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"{prefix}: {field} must be non-empty")

        reasoning = drill.get("expected_reasoning", [])
        if not isinstance(reasoning, list) or len(reasoning) < 5:
            errors.append(f"{prefix}: expected_reasoning must contain at least 5 steps")
        elif any(not isinstance(value, str) or not value.strip() for value in reasoning):
            errors.append(f"{prefix}: expected_reasoning contains an empty step")

        red_flags = drill.get("red_flags", [])
        if not isinstance(red_flags, list) or len(red_flags) < 2:
            errors.append(f"{prefix}: at least two red flags are required")

    boundary = str(payload.get("boundary", "")).lower()
    if "not published assessment cases" not in boundary:
        errors.append("Dataset boundary must state that drills are not published assessment cases")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Core 12 cross-route assessment drills.")
    parser.add_argument("--check", action="store_true", help="Compatibility flag; validation is always read-only.")
    parser.parse_args()

    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 2
    payload = load_json(DRILLS)
    route_pairs = sum(len(item["routes"]) for item in payload["drills"])
    print(f"Core boundary drills valid: {len(payload['drills'])} drills, {route_pairs} route references, publication boundary intact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
