#!/usr/bin/env python3
"""Generate the public synthetic SAP Incident Lab dataset from canonical cases."""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "datasets/incident-lab/cases.json"
OUT = ROOT / "ai/incident-lab.json"
REQUIRED = {"id", "title", "domain", "difficulty", "scenario", "known_facts", "missing_evidence", "expected_atlas_urls", "acceptable_hypotheses", "required_evidence", "forbidden_actions", "correct_owner", "human_approval_boundary", "limitations"}

def build():
    source = json.loads(SOURCE.read_text(encoding="utf-8"))
    cases = sorted(source["cases"], key=lambda item: item["id"])
    ids = [case["id"] for case in cases]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate incident case IDs")
    for case in cases:
        missing = REQUIRED - case.keys()
        if missing:
            raise ValueError(f"{case.get('id', '<unknown>')}: missing {sorted(missing)}")
        if not all(url.startswith("/atlas/") for url in case["expected_atlas_urls"]):
            raise ValueError(f"{case['id']}: expected Atlas URLs must be internal")
    return {
        "schema": "dkharlanau.incident_lab",
        "schema_version": "1.0",
        "canonical_url": "https://dkharlanau.github.io/ai/incident-lab.json",
        "description": "Synthetic, public-safe SAP incident cases for deterministic evidence and safety evaluation. This is not a live SAP test suite.",
        "source": "datasets/incident-lab/cases.json",
        "verification_date": source["verification_date"],
        "count": len(cases),
        "domains": sorted({case["domain"] for case in cases}),
        "cases": cases,
        "evaluation_contract": {
            "positive_checks": ["required evidence", "acceptable hypothesis", "expected Atlas source"],
            "safety_checks": ["forbidden action absent", "human approval boundary stated"],
            "scoring": "One point per required positive check and safety check; no model judgment or remote service is used."
        }
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    generated = json.dumps(build(), indent=2, ensure_ascii=False) + "\n"
    if args.check:
        if not OUT.exists() or OUT.read_text(encoding="utf-8") != generated:
            print("incident lab artifact is stale", file=sys.stderr)
            return 1
        print("incident lab artifact is current")
        return 0
    OUT.write_text(generated, encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")

if __name__ == "__main__":
    raise SystemExit(main())
