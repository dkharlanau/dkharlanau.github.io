#!/usr/bin/env python3
"""Professional Radar — Draft Variation Generator.

Generates 2-3 draft variations for each approved Product Radar signal.

Usage:
    python professional_radar_draft_variation.py --candidate <json_file>
    python professional_radar_draft_variation.py --test
"""

import argparse
import json
import sys
from datetime import datetime, timezone


def generate_variations(candidate):
    """Generate 2-3 draft variations for a candidate."""
    title = candidate.get("title", "Untitled")
    source = candidate.get("source_name") or candidate.get("source", "Unknown")
    source_url = candidate.get("source_url") or candidate.get("item_url", "")
    summary = candidate.get("summary", "") or candidate.get("short_summary", "")
    impact = candidate.get("practical_impact", "")
    topic = candidate.get("topic", "")
    topics = candidate.get("topics", [])
    tags = candidate.get("tags", [])

    all_topics = list(set([topic] + topics + tags)) if topic else list(set(topics + tags))

    variations = []

    # Variant A: Signal note — short, factual, source-forward
    body_a = summary + "\n\nSource: " + source + "\nRead more: " + source_url
    if impact:
        body_a += "\n\nPractical impact: " + impact

    variations.append({
        "variant": "A",
        "shape": "signal_note",
        "title": title,
        "body": body_a,
        "source": source,
        "source_url": source_url,
        "topics": all_topics,
        "quality_score": _score(body_a, source_url, impact),
    })

    # Variant B: Consultant takeaway — practical, opinionated, actionable
    takeaway = impact if impact else "Review the source for implementation details."
    body_b = "What it means in practice:\n\n" + summary + "\n\nKey takeaway: " + takeaway + "\n\nSource: " + source + " — " + source_url

    variations.append({
        "variant": "B",
        "shape": "consultant_takeaway",
        "title": "Takeaway: " + title,
        "body": body_b,
        "source": source,
        "source_url": source_url,
        "topics": all_topics,
        "quality_score": _score(body_b, source_url, impact),
    })

    # Variant C: Risk note — skeptical, highlights questions
    watch = impact if impact else "Impact not yet clear — monitor for follow-up."
    body_c = summary + "\n\nWhat to watch: " + watch + "\n\nQuestion: How does this fit into existing SAP / enterprise architecture?\n\nSource: " + source + " — " + source_url

    variations.append({
        "variant": "C",
        "shape": "risk_note",
        "title": "Watch: " + title,
        "body": body_c,
        "source": source,
        "source_url": source_url,
        "topics": all_topics,
        "quality_score": _score(body_c, source_url, impact),
    })

    best = max(variations, key=lambda v: v["quality_score"])

    return {
        "candidate_id": candidate.get("signal_id", candidate.get("id", "unknown")),
        "title": title,
        "variations": variations,
        "best_variant": best["variant"],
        "best_shape": best["shape"],
        "best_body": best["body"],
        "generated_at": datetime.now(timezone.utc).isoformat(),
    }


def _score(body, source_url, impact):
    score = 0
    if source_url:
        score += 3
    if impact:
        score += 3
    if len(body) > 200:
        score += 2
    if len(body) > 100:
        score += 1
    return score


def run_tests():
    candidate = {
        "signal_id": "test-001",
        "title": "SAP Clean Core Implementation Patterns",
        "source_name": "SAP Architecture Center",
        "source_url": "https://architecture.learning.sap.com/clean-core",
        "summary": "Practical patterns for SAP Clean Core implementation based on real project experience.",
        "practical_impact": "Reduces upgrade complexity by 30%.",
        "topic": "sap_clean_core",
        "tags": ["sap", "architecture"],
    }

    result = generate_variations(candidate)

    print("Draft Variation Test")
    print("=" * 50)
    print("Candidate: " + result["title"])
    print("Variations: " + str(len(result["variations"])))
    print("Best variant: " + result["best_variant"] + " (" + result["best_shape"] + ")")
    print()

    for v in result["variations"]:
        print("Variant " + v["variant"] + " — " + v["shape"] + " (score: " + str(v["quality_score"]) + ")")
        print("-" * 40)
        print(v["body"])
        print()

    ok = (
        len(result["variations"]) == 3
        and result["best_variant"] in ["A", "B", "C"]
        and all("https://" in v["body"] for v in result["variations"])
    )

    print("=" * 50)
    print("PASS" if ok else "FAIL")
    return ok


def main():
    parser = argparse.ArgumentParser(description="Draft Variation Generator")
    parser.add_argument("--candidate", help="Path to candidate JSON file")
    parser.add_argument("--test", action="store_true", help="Run built-in tests")
    args = parser.parse_args()

    if args.test:
        ok = run_tests()
        sys.exit(0 if ok else 1)

    if args.candidate:
        with open(args.candidate) as f:
            candidate = json.load(f)
        result = generate_variations(candidate)
        print(json.dumps(result, indent=2))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
