#!/usr/bin/env python3
"""Validate signal-driven Atlas update proposals.

This validator is a quality gate. It does not edit pages or publish content.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

from match_atlas_signal import load_json


REPO_ROOT = Path(__file__).resolve().parents[1]

PRIVATE_PATTERNS = [
    re.compile(r"/Users/[A-Za-z0-9._-]+"),
    re.compile(r"private-source", re.I),
    re.compile(r"kb-drafts", re.I),
    re.compile(r"\.env(?:\.|$)", re.I),
    re.compile(r"Basic_Link(?:ed)?InDataExport", re.I),
]

GENERIC_PATTERNS = [
    re.compile(r"\bAI is (?:changing|transforming|revolutionizing)\b", re.I),
    re.compile(r"\bgame changer\b", re.I),
    re.compile(r"\bparadigm shift\b", re.I),
    re.compile(r"\bthis changes everything\b", re.I),
    re.compile(r"\bSAP teams need to prepare\b", re.I),
]


def contains_private_pattern(text: str) -> str | None:
    for pattern in PRIVATE_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0)
    return None


def contains_generic_pattern(text: str) -> str | None:
    for pattern in GENERIC_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0)
    return None


def page_exists(path: str, repo_root: Path = REPO_ROOT) -> bool:
    if not path or Path(path).is_absolute() or ".." in Path(path).parts:
        return False
    return (repo_root / path).is_file()


def validate_proposal(proposal: dict[str, Any], repo_root: Path = REPO_ROOT) -> dict[str, Any]:
    issues: list[str] = []
    checks: dict[str, bool] = {}
    proposal_text = json.dumps(proposal, ensure_ascii=False)
    proposal_type = proposal.get("proposal_type", "")

    private_match = contains_private_pattern(proposal_text)
    checks["no_private_paths"] = private_match is None
    if private_match:
        issues.append(f"proposal contains private/local path pattern: {private_match}")

    signal = proposal.get("signal", {})
    evidence = proposal.get("evidence", {})
    source_url = signal.get("source_url", "")
    source_date = signal.get("source_date", "")
    facts = evidence.get("concrete_facts", []) or []

    checks["has_source_url"] = bool(source_url)
    checks["has_source_date"] = bool(source_date)
    checks["source_body_opened"] = bool(evidence.get("source_body_opened"))
    checks["has_two_concrete_facts"] = len(facts) >= 2

    if proposal_type in {"existing_page_update", "new_page_candidate"}:
        if not checks["has_source_url"]:
            issues.append("missing source URL")
        if not checks["has_source_date"]:
            issues.append("missing source date")
        if not checks["source_body_opened"]:
            issues.append("source body was not opened")
        if not checks["has_two_concrete_facts"]:
            issues.append("fewer than two concrete facts")

        content = proposal.get("proposed_content_block", "")
        attribution = proposal.get("source_attribution_block", "")
        generic_match = contains_generic_pattern(content)
        checks["has_proposed_content"] = len(content.strip()) >= 40
        checks["has_source_attribution"] = source_url in attribution or source_url in content
        checks["not_generic_commentary"] = generic_match is None

        if not checks["has_proposed_content"]:
            issues.append("missing compact proposed content block")
        if not checks["has_source_attribution"]:
            issues.append("missing source attribution URL")
        if generic_match:
            issues.append(f"generic commentary detected: {generic_match}")

    if proposal_type == "existing_page_update":
        target_path = proposal.get("target", {}).get("path", "")
        checks["target_page_exists"] = page_exists(target_path, repo_root)
        if not checks["target_page_exists"]:
            issues.append(f"target page does not exist: {target_path}")
        elif proposal.get("proposed_content_block", ""):
            target_text = (repo_root / target_path).read_text(encoding="utf-8")
            duplicate = proposal["proposed_content_block"].strip() in target_text
            checks["not_duplicate_existing_content"] = not duplicate
            if duplicate:
                issues.append("proposed content already appears in target page")

    if proposal_type == "new_page_candidate":
        new_page = proposal.get("proposed_new_page", {})
        proposed_path = new_page.get("proposed_path", "")
        checks["new_page_path_not_existing"] = not page_exists(proposed_path, repo_root)
        checks["new_page_noindex_until_reviewed"] = new_page.get("noindex_until_reviewed") is True
        if not checks["new_page_path_not_existing"]:
            issues.append(f"new page candidate path already exists: {proposed_path}")
        if not checks["new_page_noindex_until_reviewed"]:
            issues.append("new page candidate must remain noindex until reviewed")

        max_candidate_score = max(
            [candidate.get("score", 0) for candidate in proposal.get("atlas_candidates", [])] or [0]
        )
        checks["no_existing_page_above_update_threshold"] = max_candidate_score < 0.34
        if not checks["no_existing_page_above_update_threshold"]:
            issues.append("existing Atlas candidate is strong enough; new page should be downgraded")

    if proposal_type in {"reject", "needs_research"}:
        checks["no_public_content_for_rejected_signal"] = "proposed_content_block" not in proposal
        if not checks["no_public_content_for_rejected_signal"]:
            issues.append("rejected/research proposal must not include public content block")

    if proposal_type in {"reject", "needs_research"}:
        status = proposal_type
        passed = False
    else:
        passed = not issues and all(checks.values())
        status = "passed" if passed else "rejected"

    return {
        "schema": "dkharlanau.atlas_proposal_quality_result",
        "schema_version": "1.0",
        "proposal_type": proposal_type,
        "passed": passed,
        "status": status,
        "issues": issues,
        "checks": checks,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate an Atlas signal proposal.")
    parser.add_argument("--proposal", required=True, type=Path, help="Path to proposal JSON.")
    parser.add_argument("--output", type=Path, help="Optional path to write validation JSON.")
    args = parser.parse_args()

    result = validate_proposal(load_json(args.proposal))
    text = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
