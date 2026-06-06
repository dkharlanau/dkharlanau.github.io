#!/usr/bin/env python3
"""Validate the Atlas backlog decision ledger for correctness and safety."""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

LEDGER_JSON = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
LEDGER_MD = REPO_ROOT / "docs" / "atlas" / "ATLAS_BACKLOG_DECISION_LEDGER.md"
REPORT_MD = REPO_ROOT / "docs" / "atlas" / "ATLAS_LOW_VALUE_CLUSTER_PROMOTION_REPORT.md"

EXPECTED_TOTAL = 1133

FORBIDDEN_PATTERNS = [
    "source_files",
    "kb-drafts",
    "/Users/",
    "private draft",
    "Kimi_Agent_SAP Atlas Expansion",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")


def main() -> int:
    errors = []

    # 1. Ledger JSON must exist
    if not LEDGER_JSON.exists():
        errors.append(f"Ledger JSON missing: {LEDGER_JSON}")
        # Can't continue without JSON
        for e in errors:
            fail(e)
        return 1

    with open(LEDGER_JSON, "r", encoding="utf-8") as f:
        ledger = json.load(f)

    candidates = ledger.get("candidates", [])

    # 2. Total count
    if len(candidates) != EXPECTED_TOTAL:
        errors.append(f"Expected {EXPECTED_TOTAL} candidates, got {len(candidates)}")

    # 3. No duplicate candidate IDs
    ids = [c["candidate_id"] for c in candidates]
    if len(ids) != len(set(ids)):
        dupes = [item for item, count in Counter(ids).items() if count > 1]
        errors.append(f"Duplicate candidate IDs: {dupes}")

    # 4. Every candidate has final_state
    missing_state = [c["candidate_id"] for c in candidates if not c.get("final_state")]
    if missing_state:
        errors.append(f"Candidates missing final_state: {missing_state[:10]}")

    # 5. promoted_page / merged_existing must have target_page
    missing_target = [
        c["candidate_id"]
        for c in candidates
        if c.get("final_state") in ("promoted_page", "merged_existing")
        and not c.get("target_page")
    ]
    if missing_target:
        errors.append(f"promoted_page/merged_existing missing target_page: {missing_target[:10]}")

    # 6. Every cluster has at least one candidate
    clusters = ledger.get("clusters", {})
    empty_clusters = [cid for cid, c in clusters.items() if c.get("candidate_count", 0) == 0]
    if empty_clusters:
        errors.append(f"Empty clusters: {empty_clusters[:10]}")

    # 7. Safety: no forbidden patterns in ledger outputs
    for path in (LEDGER_JSON, LEDGER_MD, REPORT_MD):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                errors.append(f"{path.name} contains forbidden pattern: {pattern}")

    # 8. No private paths in candidate fields
    for c in candidates:
        for field in ("sanitized_topic", "sanitized_source_bucket", "reason", "target_page"):
            val = c.get(field) or ""
            if "/Users/" in val or "/private/" in val or ".env" in val:
                errors.append(f"Candidate {c['candidate_id']} field {field} contains private path")

    # 9. No raw private text markers
    raw_markers = ["raw corpus", "private excerpt", "kb-draft", "source file"]
    for path in (LEDGER_JSON, LEDGER_MD, REPORT_MD):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for marker in raw_markers:
            if marker in text.lower():
                # Allow safety-note denials like "no raw corpus" or "no private excerpts"
                if f"no {marker}" in text.lower() or f"no {marker}s" in text.lower():
                    continue
                errors.append(f"{path.name} contains raw private text marker: {marker}")

    if errors:
        print("Atlas backlog ledger validation FAILED:")
        for e in errors:
            fail(e)
        return 1

    print(f"Atlas backlog ledger validation PASSED for {len(candidates)} candidates.")
    print(f"  Clusters: {len(clusters)}")
    states = Counter(c["final_state"] for c in candidates)
    for state, count in states.most_common():
        print(f"    {state}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
