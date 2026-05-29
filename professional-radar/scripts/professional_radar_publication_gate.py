#!/usr/bin/env python3
"""Professional Radar — Publication Safety Gate.

Deterministic gate for Product Radar candidates before they become
site-ready or LinkedIn-ready.

Usage:
    python professional_radar_publication_gate.py --candidate <json_file>
    python professional_radar_publication_gate.py --test
"""

import argparse
import json
import sys
from datetime import datetime, timezone


HYPE_PHRASES = [
    "game changer", "revolutionary", "groundbreaking", "unprecedented",
    "cutting edge", "state of the art", "world class", "best in class",
    "leading", "premier", "top tier", "industry leading"
]

CLAIM_MARKERS = ["guarantee", "100%", "always", "never", "impossible", "certain"]

PROMO_WORDS = ["buy", "purchase", "discount", "offer", "limited", "exclusive", "sign up"]

PROFESSIONAL_ANGLE_WORDS = [
    "practical", "implementation", "deployment", "integration",
    "workflow", "architecture", "pattern", "approach", "method",
    "lesson", "experience", "case", "project", "team", "process"
]


def evaluate_candidate(candidate):
    """Evaluate a candidate and return a gate decision.

    Decisions: publishable, needs_edit, digest_only, reject
    """
    decision = "publishable"
    reasons = []

    # 1. Source check
    source_url = candidate.get("source_url") or candidate.get("item_url")
    if not source_url:
        decision = "reject"
        reasons.append("Missing source URL")

    # 2. Confidence check
    confidence = candidate.get("confidence", "").lower()
    if confidence == "low":
        decision = "reject"
        reasons.append("Low confidence")
    elif confidence == "medium":
        if decision == "publishable":
            decision = "needs_edit"
        reasons.append("Medium confidence — needs review")

    # 3. Practical impact check
    has_impact = bool(
        candidate.get("practical_impact") or 
        candidate.get("key_points") or
        candidate.get("summary")
    )
    if not has_impact:
        if decision in ("publishable", "needs_edit"):
            decision = "needs_edit"
        reasons.append("Missing practical impact")

    # 4. Content quality — anti-spam checks
    title = candidate.get("title", "")
    summary = candidate.get("summary", "") or candidate.get("short_summary", "")
    full_text = (title + " " + summary).lower()

    for phrase in HYPE_PHRASES:
        if phrase in full_text:
            if decision == "publishable":
                decision = "needs_edit"
            reasons.append("Generic hype detected: '" + phrase + "'")

    for marker in CLAIM_MARKERS:
        if marker in full_text:
            if decision == "publishable":
                decision = "needs_edit"
            reasons.append("Potentially unsupported claim: '" + marker + "'")

    has_angle = any(word in full_text for word in PROFESSIONAL_ANGLE_WORDS)
    if not has_angle:
        if decision == "publishable":
            decision = "needs_edit"
        reasons.append("Missing human/professional angle")

    for word in PROMO_WORDS:
        if word in full_text:
            if decision in ("publishable", "needs_edit"):
                decision = "digest_only"
            reasons.append("Promotional language detected")

    return {
        "decision": decision,
        "reasons": reasons,
        "candidate_id": candidate.get("signal_id", candidate.get("id", "unknown")),
        "title": candidate.get("title", "Untitled"),
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
    }


def run_tests():
    """Run built-in test cases."""
    tests = [
        {
            "name": "High-confidence sourced signal",
            "candidate": {
                "signal_id": "test-001",
                "title": "SAP Clean Core Implementation Patterns",
                "source_url": "https://example.com/sap-clean-core",
                "confidence": "high",
                "summary": "Practical patterns for SAP Clean Core implementation based on real project experience.",
                "practical_impact": "Reduces upgrade complexity by 30%.",
                "key_points": ["Use extensibility options", "Separate custom code"]
            },
            "expected": "publishable"
        },
        {
            "name": "Low-confidence signal",
            "candidate": {
                "signal_id": "test-002",
                "title": "Some AI Thing",
                "source_url": "https://example.com/ai",
                "confidence": "low",
                "summary": "Might be useful."
            },
            "expected": "reject"
        },
        {
            "name": "Generic hype",
            "candidate": {
                "signal_id": "test-004",
                "title": "Revolutionary Platform",
                "source_url": "https://example.com/platform",
                "confidence": "high",
                "summary": "This is a groundbreaking and world-class platform."
            },
            "expected": "needs_edit"
        },
        {
            "name": "Missing source",
            "candidate": {
                "signal_id": "test-005",
                "title": "Unknown Source Signal",
                "confidence": "high",
                "summary": "Something happened."
            },
            "expected": "reject"
        },
        {
            "name": "No practical impact",
            "candidate": {
                "signal_id": "test-006",
                "title": "AI News",
                "source_url": "https://example.com/ai-news",
                "confidence": "high",
                "summary": "AI is being used in many places."
            },
            "expected": "needs_edit"
        },
    ]

    passed = 0
    failed = 0
    for test in tests:
        result = evaluate_candidate(test["candidate"])
        actual = result["decision"]
        expected = test["expected"]
        if actual == expected:
            passed += 1
            print("PASS: " + test["name"] + " -> " + actual)
        else:
            failed += 1
            print("FAIL: " + test["name"] + " -> expected " + expected + ", got " + actual)
            print("  Reasons: " + str(result["reasons"]))

    print("\n" + str(passed) + "/" + str(len(tests)) + " tests passed")
    return failed == 0


def main():
    parser = argparse.ArgumentParser(description="Publication Safety Gate")
    parser.add_argument("--candidate", help="Path to candidate JSON file")
    parser.add_argument("--test", action="store_true", help="Run built-in tests")
    args = parser.parse_args()

    if args.test:
        ok = run_tests()
        sys.exit(0 if ok else 1)

    if args.candidate:
        with open(args.candidate) as f:
            candidate = json.load(f)
        result = evaluate_candidate(candidate)
        print(json.dumps(result, indent=2))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
