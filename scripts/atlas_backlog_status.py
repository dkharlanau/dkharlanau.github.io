#!/usr/bin/env python3
"""
Atlas Backlog Status Tool

Lookup, summary, fingerprint, and new-candidate checking for the Atlas
backlog decision ledger.

Rules:
- Never writes raw private input into the repo
- Sanitizes all output
- Fails if private paths are detected in input
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LEDGER_JSON = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"

FORBIDDEN_INPUT_PATTERNS = [
    r"/Users/[^\s]+",
    r"kb-drafts",
    r"Kimi_Agent_SAP Atlas Expansion",
    r"\.env",
    r"source_files",
]


def _fail(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)


def _load_ledger() -> dict:
    if not LEDGER_JSON.exists():
        _fail(f"Ledger not found: {LEDGER_JSON}")
        sys.exit(1)
    with open(LEDGER_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def _sanitize(text: str) -> str:
    text = re.sub(r"/Users/[^\s]+", "", text)
    text = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "", text)
    return text.strip()


def _check_input_safety(text: str) -> list[str]:
    errors = []
    for pattern in FORBIDDEN_INPUT_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            errors.append(f"Input contains forbidden pattern: {pattern}")
    return errors


def _content_fingerprint(topic: str, domain: str, category: str, reason: str = "", candidate_id: str = "") -> str:
    """Compute fingerprint matching the pipeline formula."""
    text = f"{candidate_id}:{topic}:{category}:{reason}"
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def cmd_summary(args: argparse.Namespace) -> int:
    ledger = _load_ledger()
    candidates = ledger.get("candidates", [])
    clusters = ledger.get("clusters", {})

    print(f"Atlas Backlog Ledger Summary")
    print(f"  Schema:        {ledger.get('schema', 'unknown')}")
    print(f"  Version:       {ledger.get('version', 'unknown')}")
    print(f"  Run ID:        {ledger.get('run_id', 'unknown')}")
    print(f"  Processed:     {ledger.get('processed_date', 'unknown')}")
    print(f"  Candidates:    {len(candidates)}")
    print(f"  Clusters:      {len(clusters)}")
    print()

    state_counts = Counter(c["final_state"] for c in candidates)
    print("States:")
    for state, count in state_counts.most_common():
        print(f"  {state}: {count}")

    domain_counts = Counter(c["domain"] for c in candidates)
    print()
    print("Domains:")
    for domain, count in domain_counts.most_common():
        print(f"  {domain}: {count}")
    return 0


def cmd_lookup(args: argparse.Namespace) -> int:
    ledger = _load_ledger()
    candidates = ledger.get("candidates", [])

    if args.candidate_id:
        matches = [c for c in candidates if c["candidate_id"] == args.candidate_id]
    elif args.topic:
        topic = args.topic.lower()
        matches = [c for c in candidates if topic in c["sanitized_topic"].lower()]
    else:
        _fail("Provide --candidate-id or --topic")
        return 1

    if not matches:
        print("No matching candidate found.")
        return 0

    for c in matches:
        print(f"candidate_id:     {c['candidate_id']}")
        print(f"  topic:          {c['sanitized_topic']}")
        print(f"  domain:         {c['domain']}")
        print(f"  category:       {c['category']}")
        print(f"  cluster_id:     {c['cluster_id']}")
        print(f"  final_state:    {c['final_state']}")
        print(f"  target_page:    {c.get('target_page') or '—'}")
        print(f"  reason:         {c['reason']}")
        print(f"  fingerprint:    {c['content_fingerprint']}")
        print(f"  processed_date: {c['processed_date']}")
        print()
    return 0


def cmd_fingerprint(args: argparse.Namespace) -> int:
    topic = _sanitize(args.topic)
    domain = _sanitize(args.domain)
    category = _sanitize(args.category)

    errors = _check_input_safety(f"{topic} {domain} {category}")
    if errors:
        for e in errors:
            _fail(e)
        return 1

    fp = _content_fingerprint(topic, domain, category, reason="", candidate_id="")
    print(f"Fingerprint: {fp}")
    print(f"  topic:    {topic}")
    print(f"  domain:   {domain}")
    print(f"  category: {category}")

    # Check against ledger
    ledger = _load_ledger()
    candidates = ledger.get("candidates", [])
    matches = [c for c in candidates if c["content_fingerprint"] == fp]
    if matches:
        print(f"  status:   already_processed ({matches[0]['candidate_id']})")
    else:
        print(f"  status:   not in ledger")
    return 0


def cmd_check_new(args: argparse.Namespace) -> int:
    csv_path = Path(args.csv)
    if not csv_path.exists():
        _fail(f"CSV not found: {csv_path}")
        return 1

    ledger = _load_ledger()
    existing_ids = {c["candidate_id"] for c in ledger.get("candidates", [])}
    existing_fps = {c["content_fingerprint"] for c in ledger.get("candidates", [])}

    with open(csv_path, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    results = []
    for row in rows:
        raw_topic = row.get("topic", "")
        raw_domain = row.get("sap_area", "")
        raw_category = row.get("category", "")
        candidate_id = row.get("id", "").strip()

        # Safety check on RAW input (before sanitization)
        raw_text = f"{raw_topic} {raw_domain} {raw_category} {candidate_id}"
        safety_errors = _check_input_safety(raw_text)
        if safety_errors:
            results.append({
                "candidate_id": candidate_id or "unknown",
                "topic": _sanitize(raw_topic),
                "status": "blocked_private_risk",
                "reason": "; ".join(safety_errors),
            })
            continue

        topic = _sanitize(raw_topic)
        domain = _sanitize(raw_domain)
        category = _sanitize(raw_category)

        # Already processed by ID
        if candidate_id and candidate_id in existing_ids:
            results.append({
                "candidate_id": candidate_id,
                "topic": topic,
                "status": "already_processed",
                "reason": f"Candidate ID {candidate_id} exists in ledger",
            })
            continue

        # Check fingerprint
        reason = _sanitize(row.get("reason", ""))
        fp = _content_fingerprint(topic, domain, category, reason=reason, candidate_id=candidate_id)
        if fp in existing_fps:
            results.append({
                "candidate_id": candidate_id or "unknown",
                "topic": topic,
                "status": "possible_duplicate",
                "reason": f"Fingerprint matches existing ledger entry",
            })
            continue

        results.append({
            "candidate_id": candidate_id or "unknown",
            "topic": topic,
            "status": "new_candidate",
            "reason": "Not found in existing ledger",
        })

    # Print summary
    status_counts = Counter(r["status"] for r in results)
    print(f"Checked {len(rows)} rows against ledger:")
    for status, count in status_counts.most_common():
        print(f"  {status}: {count}")
    print()

    # Print details for non-new
    non_new = [r for r in results if r["status"] != "new_candidate"]
    if non_new:
        print("Non-new candidates:")
        for r in non_new[:20]:
            print(f"  {r['candidate_id']} | {r['status']} | {r['topic'][:50]} | {r['reason']}")
        if len(non_new) > 20:
            print(f"  ... and {len(non_new) - 20} more")
    return 0


def cmd_export_summary(args: argparse.Namespace) -> int:
    ledger = _load_ledger()
    candidates = ledger.get("candidates", [])
    clusters = ledger.get("clusters", {})

    output = {
        "schema": "dkharlanau.atlas.backlog_summary_export",
        "version": "1.0.0",
        "source_run_id": ledger.get("run_id"),
        "source_processed_date": ledger.get("processed_date"),
        "total_candidates": len(candidates),
        "total_clusters": len(clusters),
        "state_counts": dict(Counter(c["final_state"] for c in candidates)),
        "domain_counts": dict(Counter(c["domain"] for c in candidates)),
    }

    out_path = Path(args.output)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Summary exported to {out_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Atlas Backlog Status Tool")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("summary", help="Show ledger summary")

    lookup_parser = subparsers.add_parser("lookup", help="Lookup a candidate")
    lookup_parser.add_argument("--candidate-id", help="Candidate ID to lookup")
    lookup_parser.add_argument("--topic", help="Topic text to search")

    fp_parser = subparsers.add_parser("fingerprint", help="Compute content fingerprint")
    fp_parser.add_argument("--topic", required=True, help="Topic text")
    fp_parser.add_argument("--domain", required=True, help="Domain / SAP area")
    fp_parser.add_argument("--category", required=True, help="Category")

    check_parser = subparsers.add_parser("check-new", help="Check new CSV against ledger")
    check_parser.add_argument("--csv", required=True, help="Path to CSV file")

    export_parser = subparsers.add_parser("export-summary", help="Export summary JSON")
    export_parser.add_argument("--output", required=True, help="Output file path")

    args = parser.parse_args()

    if args.command == "summary":
        return cmd_summary(args)
    elif args.command == "lookup":
        return cmd_lookup(args)
    elif args.command == "fingerprint":
        return cmd_fingerprint(args)
    elif args.command == "check-new":
        return cmd_check_new(args)
    elif args.command == "export-summary":
        return cmd_export_summary(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
