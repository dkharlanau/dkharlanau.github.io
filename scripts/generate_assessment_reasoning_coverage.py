#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "labs" / "assessment" / "data"
MANIFEST = DATA / "case-sets.json"
CATALOG = DATA / "catalog.json"
OUTPUT = DATA / "reasoning-pressure-coverage.json"
LEVELS = ["explain", "trace", "diagnose", "design", "challenge"]
LEAD_PRESSURE = ["diagnose", "design", "challenge"]
MIN_PER_LEAD_LEVEL = 2


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def all_cases() -> list[dict[str, Any]]:
    manifest = load_json(MANIFEST)
    rows: list[dict[str, Any]] = []
    for case_set in manifest["sets"]:
        rows.extend(load_jsonl(ROOT / case_set["url"].lstrip("/")))
    return rows


def build() -> dict[str, Any]:
    cases = all_cases()
    catalog = load_json(CATALOG)
    tracks = [track["id"] for track in catalog["tracks"]]
    counts: dict[str, Counter[str]] = defaultdict(Counter)
    ids: dict[tuple[str, str], list[str]] = defaultdict(list)
    for case in cases:
        track = case["track"]
        level = case["level"]
        counts[track][level] += 1
        ids[(track, level)].append(case["id"])

    track_items = []
    gaps = []
    for track in tracks:
        level_items = []
        total = sum(counts[track].values())
        lead_total = sum(counts[track][level] for level in LEAD_PRESSURE)
        for level in LEVELS:
            count = counts[track][level]
            state = "covered"
            if level in LEAD_PRESSURE and count == 0:
                state = "missing"
            elif level in LEAD_PRESSURE and count < MIN_PER_LEAD_LEVEL:
                state = "thin"
            level_items.append({
                "level": level,
                "count": count,
                "case_ids": sorted(ids[(track, level)]),
                "pressure_state": state,
            })
            if state in {"missing", "thin"}:
                gaps.append({
                    "track": track,
                    "level": level,
                    "count": count,
                    "state": state,
                    "authoring_need": f"Add or promote a materially distinct {level} case for {track}; current published count is {count}."
                })
        track_items.append({
            "track": track,
            "total_cases": total,
            "lead_pressure_cases": lead_total,
            "lead_pressure_share": round(lead_total / total, 3) if total else 0,
            "levels": level_items,
        })

    overall = Counter(case["level"] for case in cases)
    gaps.sort(key=lambda item: (0 if item["state"] == "missing" else 1, item["count"], item["track"], item["level"]))
    return {
        "id": "sap-lead-reasoning-pressure-coverage",
        "version": "1.0.0",
        "updated_at": "2026-08-16",
        "purpose": "Measure exact published-case coverage by assessment track and reasoning level so authoring work targets missing Lead-pressure cells instead of raw topic volume.",
        "inputs": {
            "case_manifest": "/labs/assessment/data/case-sets.json",
            "catalog": "/labs/assessment/data/catalog.json"
        },
        "policy": {
            "levels": LEVELS,
            "lead_pressure_levels": LEAD_PRESSURE,
            "minimum_published_cases_per_lead_pressure_level": MIN_PER_LEAD_LEVEL,
            "state_rule": {
                "missing": "zero published cases in a Lead-pressure cell",
                "thin": f"one published case or otherwise fewer than {MIN_PER_LEAD_LEVEL} cases in a Lead-pressure cell",
                "covered": f"at least {MIN_PER_LEAD_LEVEL} published cases, or a non-Lead-pressure level"
            },
            "boundary": "The threshold is an authored practice-design heuristic. It does not change scoring, candidate approval, factual review, or publication state."
        },
        "summary": {
            "published_cases": len(cases),
            "tracks": len(tracks),
            "levels": len(LEVELS),
            "lead_pressure_cases": sum(overall[level] for level in LEAD_PRESSURE),
            "lead_pressure_share": round(sum(overall[level] for level in LEAD_PRESSURE) / len(cases), 3) if cases else 0,
            "missing_lead_pressure_cells": sum(gap["state"] == "missing" for gap in gaps),
            "thin_lead_pressure_cells": sum(gap["state"] == "thin" for gap in gaps),
            "level_counts": {level: overall[level] for level in LEVELS},
        },
        "tracks": track_items,
        "authoring_gaps": gaps,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = build()
    rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print("Stale or missing reasoning pressure coverage dataset")
            return 2
        print(f"Reasoning coverage current: {data['summary']['published_cases']} cases, {len(data['authoring_gaps'])} Lead-pressure gaps.")
        return 0
    OUTPUT.write_text(rendered, encoding="utf-8")
    print(f"Generated reasoning coverage: {data['summary']['published_cases']} cases, {len(data['authoring_gaps'])} Lead-pressure gaps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
