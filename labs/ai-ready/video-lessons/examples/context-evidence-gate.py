#!/usr/bin/env python3
"""Dependency-free synthetic context-lifecycle and SAP diagnostic evidence gate.

This is a training exercise. It does not call SAP or a model.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


def timestamp(value: str) -> datetime:
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("Evidence timestamps must include a timezone")
    return parsed.astimezone(timezone.utc)


def assess(case: dict, *, now: str) -> dict:
    """Check scoped, current, authoritative evidence before recommending a write."""
    current = timestamp(now)
    case_id = str(case["case_id"])
    findings: list[str] = []
    accepted: dict[str, dict] = {}
    for item in case.get("evidence", []):
        key = str(item["key"])
        if item.get("case_id") != case_id:
            findings.append(f"{key}: wrong case scope")
            continue
        if item.get("kind") != "source_evidence" or item.get("trust") != "authenticated_tool_result":
            findings.append(f"{key}: not an authoritative source observation")
            continue
        observed = timestamp(item["observed_at"])
        if observed > current:
            findings.append(f"{key}: observation is in the future")
            continue
        expires = timestamp(item["expires_at"])
        if expires <= current:
            findings.append(f"{key}: stale evidence")
            continue
        if not item.get("source_ref") or not item.get("source_system"):
            findings.append(f"{key}: missing source provenance")
            continue
        if key in accepted:
            findings.append(f"{key}: duplicate evidence key")
            accepted.pop(key)
            continue
        accepted[key] = item

    expected = [str(x) for x in case.get("required_keys", [])]
    missing = [key for key in expected if key not in accepted]
    if missing:
        findings.append("missing required current evidence: " + ", ".join(missing))

    allowed_to_diagnose = not findings and bool(expected)
    source = accepted.get("source_zone", {}).get("value")
    target = accepted.get("target_zone", {}).get("value")
    if allowed_to_diagnose and "source_zone" in expected and "target_zone" in expected:
        hypothesis = "source_target_mismatch" if source != target else "values_match_check_determination"
    else:
        hypothesis = "insufficient_evidence"

    return {
        "case_id": case_id,
        "status": "diagnostic_ready" if allowed_to_diagnose else "insufficient_evidence",
        "hypothesis": hypothesis,
        "evidence_refs": [accepted[k]["source_ref"] for k in expected if k in accepted],
        "findings": findings,
        "write_allowed": False,
        "next_action": "investigate_route_inputs" if allowed_to_diagnose else "request_authoritative_fresh_read",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cases", type=Path, default=Path(__file__).with_name("context-cases.json"))
    parser.add_argument("--now", default="2026-11-11T10:30:00Z")
    parser.add_argument("--gate", action="store_true", help="Require expected statuses and no writes")
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    outcomes = [assess(case, now=args.now) for case in cases]
    for result in outcomes:
        print(json.dumps(result, sort_keys=True))
    if args.gate:
        for case, outcome in zip(cases, outcomes):
            if outcome["status"] != case["expected_status"] or outcome["write_allowed"]:
                return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
