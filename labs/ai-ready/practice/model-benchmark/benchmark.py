#!/usr/bin/env python3
"""Provider-neutral model selection benchmark using recorded fixture outputs.

The fixtures are not claims about real models. Replace recorded_outputs.jsonl
with results from models you are evaluating, keeping the same case IDs.
"""
from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def evaluate(cases: list[dict], outputs: list[dict]) -> dict[str, dict]:
    expected = {case["id"]: case["expected"] for case in cases}
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in outputs:
        grouped[row["profile"]].append(row)

    result: dict[str, dict] = {}
    for profile, rows in grouped.items():
        passed = 0
        invalid = 0
        latency = 0.0
        cost = 0.0
        details = []
        seen = set()

        for row in rows:
            case_id = row["case_id"]
            seen.add(case_id)
            raw = row.get("output")
            try:
                parsed = json.loads(raw) if isinstance(raw, str) else raw
                valid_json = isinstance(parsed, dict)
            except json.JSONDecodeError:
                parsed = None
                valid_json = False

            ok = valid_json and parsed == expected.get(case_id)
            passed += int(ok)
            invalid += int(not valid_json)
            latency += float(row.get("relative_latency_units", 0))
            cost += float(row.get("relative_cost_units", 0))
            details.append({"case_id": case_id, "passed": ok, "valid_json": valid_json})

        missing = sorted(set(expected) - seen)
        total = len(expected)
        result[profile] = {
            "pass_rate": passed / total if total else 0.0,
            "passed": passed,
            "total": total,
            "invalid_json": invalid,
            "missing_cases": missing,
            "relative_latency_units": latency,
            "relative_cost_units": cost,
            "details": details,
        }
    return result


def choose_profile(results: dict[str, dict], quality_floor: float = 0.9) -> str:
    eligible = [
        (name, metrics)
        for name, metrics in results.items()
        if metrics["pass_rate"] >= quality_floor and not metrics["missing_cases"]
    ]
    if eligible:
        eligible.sort(key=lambda item: (
            item[1]["relative_cost_units"],
            item[1]["relative_latency_units"],
            item[0],
        ))
        return eligible[0][0]

    return max(
        results,
        key=lambda name: (
            results[name]["pass_rate"],
            -results[name]["relative_cost_units"],
            name,
        ),
    )


def self_test() -> None:
    cases = read_jsonl(BASE_DIR / "cases.jsonl")
    outputs = read_jsonl(BASE_DIR / "recorded_outputs.jsonl")
    results = evaluate(cases, outputs)
    assert results["quality_fixture"]["pass_rate"] == 1.0
    assert results["fast_fixture"]["pass_rate"] < 1.0
    assert choose_profile(results, 0.9) == "quality_fixture"
    assert choose_profile(results, 0.5) == "fast_fixture"
    print("model-benchmark self-test: ok")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--quality-floor", type=float, default=0.9)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        self_test()
        return 0

    cases = read_jsonl(BASE_DIR / "cases.jsonl")
    outputs = read_jsonl(BASE_DIR / "recorded_outputs.jsonl")
    results = evaluate(cases, outputs)
    selected = choose_profile(results, args.quality_floor)

    print(json.dumps({
        "quality_floor": args.quality_floor,
        "selected_profile": selected,
        "profiles": results,
        "note": "Latency and cost values are relative training fixtures, not vendor benchmarks."
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
