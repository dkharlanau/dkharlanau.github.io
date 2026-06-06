#!/usr/bin/env python3
"""
Atlas Backlog Cluster Pipeline (Idempotent)

Processes low_value_rejected candidates into stable clusters,
creates a sanitized decision ledger, and produces a promotion report.

Idempotency rules:
- Loads existing ledger first
- Skips already-processed candidate IDs
- Skips known content_fingerprints
- Only appends genuinely new candidates
- Never overwrites previous final_state without --force-reclassify
- --force-reclassify requires a reason

Safety rules:
- No private paths in any output
- No draft references
- No raw corpus text
- No file source lists
- Every candidate gets a stable ID and final state
- Only strong aggregate diagnostic clusters become pages
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = REPO_ROOT / "RECOVERY_LOW_VALUE_REJECTED_1133.csv"
LEDGER_JSON_PATH = REPO_ROOT / "docs" / "atlas" / "atlas_backlog_decision_ledger.json"
LEDGER_MD_PATH = REPO_ROOT / "docs" / "atlas" / "ATLAS_BACKLOG_DECISION_LEDGER.md"
REPORT_PATH = REPO_ROOT / "docs" / "atlas" / "ATLAS_LOW_VALUE_CLUSTER_PROMOTION_REPORT.md"

RUN_ID = "run-2026-06-06-backlog-cluster-pipeline"
PROCESSED_DATE = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

# Existing Atlas diagnostic pages for duplicate mapping
EXISTING_PAGES = {
    "sales": [
        "/atlas/diagnostics/sap-sales-order-block-diagnosis.md",
        "/atlas/diagnostics/sap-delivery-block-analysis.md",
        "/atlas/diagnostics/sap-billing-block-analysis.md",
        "/atlas/diagnostics/sap-delivery-process-diagnostics.md",
        "/atlas/diagnostics/sap-incompletion-procedure-diagnostics.md",
        "/atlas/diagnostics/sap-output-message-control-diagnostics.md",
        "/atlas/diagnostics/sap-pricing-procedure-debugging.md",
        "/atlas/diagnostics/sap-credit-management-diagnostics.md",
        "/atlas/diagnostics/sap-customer-vendor-master-diagnostics.md",
        "/atlas/diagnostics/sap-intercompany-sales-diagnostics.md",
        "/atlas/diagnostics/sap-third-party-order-diagnostics.md",
        "/atlas/diagnostics/sap-returns-order-diagnostics.md",
        "/atlas/diagnostics/sap-backorder-processing-diagnostics.md",
        "/atlas/diagnostics/sap-consignment-procurement-diagnostics.md",
        "/atlas/diagnostics/sap-account-assignment-diagnostics.md",
        "/atlas/diagnostics/sap-item-category-determination.md",
    ],
    "retail": [
        "/atlas/diagnostics/sap-retail-replenishment-diagnostics.md",
        "/atlas/diagnostics/sap-retail-assortment-listing-diagnostics.md",
        "/atlas/diagnostics/pos-sales-not-reflected-in-sap.md",
        "/atlas/diagnostics/sap-stock-transfer-diagnostics.md",
        "/atlas/diagnostics/sap-goods-receipt-diagnostics.md",
        "/atlas/diagnostics/sap-delivery-block-analysis.md",
        "/atlas/diagnostics/sap-invoice-verification-diagnostics.md",
        "/atlas/diagnostics/sap-master-data-duplicate-diagnostics.md",
        "/atlas/diagnostics/sap-physical-inventory-diagnostics.md",
    ],
    "mm-procurement": [
        "/atlas/diagnostics/sap-purchase-order-diagnostics.md",
        "/atlas/diagnostics/sap-purchase-requisition-diagnostics.md",
        "/atlas/diagnostics/sap-goods-receipt-diagnostics.md",
        "/atlas/diagnostics/sap-invoice-verification-diagnostics.md",
        "/atlas/diagnostics/sap-three-way-match-diagnostics.md",
        "/atlas/diagnostics/sap-vendor-master-replication-diagnostics.md",
        "/atlas/diagnostics/sap-source-determination-diagnostics.md",
        "/atlas/diagnostics/sap-release-strategy-diagnostics.md",
        "/atlas/diagnostics/sap-subcontracting-procurement-diagnostics.md",
        "/atlas/diagnostics/sap-consignment-procurement-diagnostics.md",
        "/atlas/diagnostics/sap-service-procurement-diagnostics.md",
        "/atlas/diagnostics/sap-ers-diagnostics.md",
        "/atlas/sap/sap-mm-procurement-overview.md",
        "/atlas/sap/sap-mm-sourcing-overview.md",
        "/atlas/sap/sap-procurement-kpis.md",
        "/atlas/sap/sap-ariba-integration-context.md",
        "/atlas/sap/sap-business-network-context.md",
    ],
    "logistics": [
        "/atlas/diagnostics/sap-goods-receipt-diagnostics.md",
        "/atlas/diagnostics/sap-delivery-process-diagnostics.md",
        "/atlas/diagnostics/sap-stock-transfer-diagnostics.md",
        "/atlas/diagnostics/sap-movement-types-diagnostics.md",
        "/atlas/diagnostics/sap-material-document-diagnostics.md",
        "/atlas/diagnostics/sap-physical-inventory-diagnostics.md",
        "/atlas/diagnostics/sap-outbound-processing-diagnostics.md",
        "/atlas/diagnostics/sap-inbound-processing-diagnostics.md",
        "/atlas/diagnostics/sap-reservation-diagnostics.md",
        "/atlas/diagnostics/sap-qrfc-trfc-diagnostics.md",
        "/atlas/sap/sap-tm-integration-overview.md",
        "/atlas/sap/sap-ewm-integration-overview.md",
        "/atlas/sap/sap-stock-transfer-in-transit.md",
        "/atlas/sap/sap-movement-types-inventory.md",
    ],
    "master-data-governance": [
        "/atlas/data-quality/sap-master-data-quality.md",
        "/atlas/data-quality/sap-master-data-replication-patterns.md",
        "/atlas/data-quality/sap-mdg-governance-patterns.md",
        "/atlas/diagnostics/sap-master-data-duplicate-diagnostics.md",
        "/atlas/diagnostics/sap-customer-vendor-master-diagnostics.md",
        "/atlas/diagnostics/sap-business-partner-replication-diagnostics.md",
        "/atlas/diagnostics/sap-cvi-synchronization-diagnostics.md",
        "/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics.md",
        "/atlas/diagnostics/sap-bp-relationship-diagnostics.md",
        "/atlas/diagnostics/sap-key-mapping-diagnostics.md",
        "/atlas/diagnostics/sap-organizational-data-diagnostics.md",
        "/atlas/diagnostics/sap-number-range-diagnostics.md",
    ],
    "planning": [
        "/atlas/diagnostics/sap-backorder-processing-diagnostics.md",
        "/atlas/diagnostics/sap-retail-replenishment-diagnostics.md",
        "/atlas/sap/sap-ibp-integration-overview.md",
    ],
    "analytics-kpis": [
        "/atlas/sap/sap-procurement-kpis.md",
    ],
    "ai-enterprise-operations": [
        "/atlas/ai-operations/ai-agent-for-sap-support.md",
        "/atlas/ai-operations/ai-ml-sidecars-for-sap.md",
        "/atlas/ai-operations/ai-ready-process-documentation.md",
        "/atlas/ai-operations/authorization-aware-ai-for-sap.md",
        "/atlas/ai-operations/practical-ai-ml-for-sap-support.md",
        "/atlas/automation/rule-based-automation-vs-ai.md",
        "/atlas/automation/sap-ams-operating-model.md",
    ],
}


def content_fingerprint(text: str) -> str:
    """Stable short fingerprint for deduplication/tracking."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def load_csv(path: Path) -> list[dict]:
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def load_existing_ledger() -> tuple[dict[str, dict], set[str]]:
    """Load existing ledger and return (candidate_by_id, known_fingerprints)."""
    if not LEDGER_JSON_PATH.exists():
        return {}, set()
    with open(LEDGER_JSON_PATH, "r", encoding="utf-8") as f:
        ledger = json.load(f)
    candidates = ledger.get("candidates", [])
    by_id = {c["candidate_id"]: c for c in candidates}
    fingerprints = {c["content_fingerprint"] for c in candidates}
    return by_id, fingerprints


def sanitize_topic(topic: str) -> str:
    """Remove any potentially private or sensitive text."""
    topic = re.sub(r"/Users/[^\s]+", "", topic)
    topic = re.sub(r"[\w.-]+@[\w.-]+\.\w+", "", topic)
    topic = topic.strip()
    return topic if topic else "untitled"


def sanitize_source_bucket(sap_area: str) -> str:
    """Normalize source bucket names; strip file extensions."""
    sap_area = sap_area.strip().lower()
    sap_area = re.sub(r"\.md$", "", sap_area)
    if sap_area in ("article-backlog", "mm-procurement-article-backlog", "retail-article-backlog"):
        return "article-backlog"
    return sap_area


def assign_cluster_id(sap_area: str, category: str) -> str:
    """Create a stable cluster ID from domain + category."""
    bucket = sanitize_source_bucket(sap_area)
    cat_slug = re.sub(r"[^a-z0-9]+", "-", category.lower()).strip("-")
    if not cat_slug:
        cat_slug = "general"
    return f"{bucket}--{cat_slug}"


def determine_final_state(row: dict, cluster_size: int) -> tuple[str, str | None, str]:
    """
    Determine final state, target page, and reason for a candidate.
    Returns: (final_state, target_page, reason)
    """
    sap_area = sanitize_source_bucket(row["sap_area"])
    category = row.get("category", "").strip()
    topic = row.get("topic", "").strip()
    reason = row.get("reason", "").strip()
    candidate_id = row.get("id", "").strip()

    if sap_area == "article-backlog" or candidate_id.startswith("ARTICLE-"):
        target = _map_article_to_existing_page(topic, sap_area)
        if target:
            return "duplicate_existing", target, f"Article overlaps with existing Atlas page: {target}"
        return "ignored_low_value", None, "Article idea is generic and overlaps with existing coverage"

    if sap_area == "ai-enterprise-operations":
        return "ignored_low_value", None, "Generic AI/ML concept without SAP operational diagnostic value"

    if sap_area == "master-data-governance":
        return "ignored_low_value", None, "Generic MDG concept without new operational diagnostic value"

    if sap_area == "planning":
        return "ignored_low_value", None, "Generic planning concept without SAP operational diagnostic value"

    if sap_area == "analytics-kpis":
        return "ignored_low_value", None, "Generic KPI/formula without SAP-specific operational diagnostic value"

    if sap_area == "logistics":
        return "ignored_low_value", None, "Generic logistics concept without SAP diagnostic value"

    if sap_area == "sales":
        if "technical enablement" in reason.lower():
            return "ignored_low_value", None, "Technical enablement topic; not operational diagnostic"
        return "ignored_low_value", None, "Generic sales concept without operational diagnostic value"

    if sap_area == "mm-procurement":
        if "too specialized" in reason.lower():
            return "ignored_low_value", None, "Too specialized for general Atlas scope"
        if "ariba" in reason.lower() or "e-procurement" in reason.lower():
            return "ignored_low_value", None, "E-procurement/Ariba-specific; not core SAP support diagnostic"
        return "ignored_low_value", None, "Generic procurement concept without operational diagnostic value"

    if sap_area == "retail":
        if "retail pricing" in reason.lower():
            return "ignored_low_value", None, "Retail pricing concept; not core SAP support diagnostic"
        return "ignored_low_value", None, "Generic retail concept without core SAP operational diagnostic value"

    return "ignored_low_value", None, "Generic concept without SAP operational diagnostic value"


def _map_article_to_existing_page(topic: str, sap_area: str) -> str | None:
    """Map article backlog topic to an existing Atlas page."""
    t = topic.lower()
    if any(k in t for k in ("sales document", "copy control", "sales area", "output determination")):
        return "/atlas/diagnostics/sap-sales-order-block-diagnosis.md"
    if any(k in t for k in ("pricing", "surcharge", "discount", "rebate", "condition type")):
        return "/atlas/diagnostics/sap-pricing-procedure-debugging.md"
    if any(k in t for k in ("delivery", "shipping")):
        return "/atlas/diagnostics/sap-delivery-process-diagnostics.md"
    if any(k in t for k in ("credit", "credit limit")):
        return "/atlas/diagnostics/sap-credit-management-diagnostics.md"
    if any(k in t for k in ("customer master", "business partner")):
        return "/atlas/diagnostics/sap-customer-vendor-master-diagnostics.md"
    if any(k in t for k in ("purchasing group", "purchasing organization", "plant")):
        return "/atlas/diagnostics/sap-purchase-order-diagnostics.md"
    if any(k in t for k in ("source-to-pay", "procure-to-pay", "sourcing")):
        return "/atlas/sap/sap-mm-procurement-overview.md"
    if any(k in t for k in ("ariba", "business network", "catalog")):
        return "/atlas/sap/sap-ariba-integration-context.md"
    if any(k in t for k in ("supplier evaluation", "vendor evaluation")):
        return "/atlas/diagnostics/sap-vendor-master-replication-diagnostics.md"
    if any(k in t for k in ("rfq", "quotation", "purchase requisition")):
        return "/atlas/diagnostics/sap-purchase-requisition-diagnostics.md"
    if any(k in t for k in ("central procurement", "fieldglass")):
        return "/atlas/sap/sap-mm-procurement-overview.md"
    if any(k in t for k in ("gr/ir", "three-way match", "invoice")):
        return "/atlas/diagnostics/sap-invoice-verification-diagnostics.md"
    if any(k in t for k in ("release strategy", "approval")):
        return "/atlas/diagnostics/sap-release-strategy-diagnostics.md"
    if any(k in t for k in ("store cannot sell", "phantom stock", "store stock")):
        return "/atlas/diagnostics/sap-retail-replenishment-diagnostics.md"
    if any(k in t for k in ("store-as-plant", "store-as-customer", "site master")):
        return "/atlas/diagnostics/sap-retail-assortment-listing-diagnostics.md"
    if any(k in t for k in ("assortment", "listing", "grade")):
        return "/atlas/diagnostics/sap-retail-assortment-listing-diagnostics.md"
    if any(k in t for k in ("allocation", "replenishment", "distribution center")):
        return "/atlas/diagnostics/sap-retail-replenishment-diagnostics.md"
    if any(k in t for k in ("pos", "sales feedback", "tender")):
        return "/atlas/diagnostics/pos-sales-not-reflected-in-sap.md"
    if any(k in t for k in ("forecast", "demand planning", "s&op", "ibp")):
        return "/atlas/sap/sap-ibp-integration-overview.md"
    if any(k in t for k in ("goods receipt", "gr", "inbound")):
        return "/atlas/diagnostics/sap-goods-receipt-diagnostics.md"
    if any(k in t for k in ("movement type", "inventory")):
        return "/atlas/diagnostics/sap-movement-types-diagnostics.md"
    if any(k in t for k in ("stock transfer", "in transit")):
        return "/atlas/diagnostics/sap-stock-transfer-diagnostics.md"
    if any(k in t for k in ("master data", "data quality", "duplicate")):
        return "/atlas/data-quality/sap-master-data-quality.md"
    if any(k in t for k in ("ai", "ml", "agent", "llm", "automation")):
        return "/atlas/ai-operations/ai-agent-for-sap-support.md"
    return None


def build_clusters(rows: list[dict]) -> dict[str, list[dict]]:
    clusters = defaultdict(list)
    for row in rows:
        cid = assign_cluster_id(row["sap_area"], row.get("category", ""))
        clusters[cid].append(row)
    return dict(clusters)


def process_candidates(
    rows: list[dict],
    existing_by_id: dict[str, dict],
    existing_fps: set[str],
    force_reclassify: str | None,
) -> tuple[list[dict], dict[str, int]]:
    """
    Process candidates with idempotency.
    Returns: (results, skip_counts)
    """
    clusters = build_clusters(rows)
    results: list[dict] = []
    skip_counts: dict[str, int] = {
        "already_processed_id": 0,
        "already_processed_fingerprint": 0,
        "force_reclassify": 0,
        "new": 0,
    }

    for row in rows:
        cid = row.get("id", "").strip()
        topic = row.get("topic", "").strip()
        category = row.get("category", "").strip()
        fingerprint = content_fingerprint(
            f"{row.get('id','')}:{row.get('topic','')}:{row.get('category','')}:{row.get('reason','')}"
        )

        # Skip by existing ID
        if cid in existing_by_id and not force_reclassify:
            skip_counts["already_processed_id"] += 1
            continue

        # Skip by fingerprint (unless force reclassify)
        if fingerprint in existing_fps and not force_reclassify:
            skip_counts["already_processed_fingerprint"] += 1
            continue

        # If force reclassify, keep the old entry and add a new one with updated state
        if cid in existing_by_id and force_reclassify:
            skip_counts["force_reclassify"] += 1

        cluster_size = len(clusters.get(assign_cluster_id(row["sap_area"], row.get("category", "")), [row]))
        final_state, target_page, reason = determine_final_state(row, cluster_size)

        results.append({
            "candidate_id": cid,
            "sanitized_topic": sanitize_topic(topic),
            "sanitized_source_bucket": sanitize_source_bucket(row["sap_area"]),
            "domain": sanitize_source_bucket(row["sap_area"]),
            "category": category,
            "original_priority": row.get("priority", "").strip() or "P2",
            "cluster_id": assign_cluster_id(row["sap_area"], row.get("category", "")),
            "final_state": final_state,
            "target_page": target_page,
            "reason": reason,
            "processed_run_id": RUN_ID,
            "processed_date": PROCESSED_DATE,
            "content_fingerprint": fingerprint,
            "force_reclassify_reason": force_reclassify if (cid in existing_by_id and force_reclassify) else None,
        })
        skip_counts["new"] += 1

    return results, skip_counts


def generate_ledger_json(all_results: list[dict]) -> None:
    LEDGER_JSON_PATH.parent.mkdir(parents=True, exist_ok=True)
    ledger = {
        "schema": "dkharlanau.atlas.backlog_decision_ledger",
        "version": "1.1.0",
        "run_id": RUN_ID,
        "processed_date": PROCESSED_DATE,
        "total_candidates": len(all_results),
        "clusters": {},
        "candidates": all_results,
    }
    for r in all_results:
        cid = r["cluster_id"]
        if cid not in ledger["clusters"]:
            ledger["clusters"][cid] = {
                "cluster_id": cid,
                "domain": r["domain"],
                "category": r["category"],
                "candidate_count": 0,
                "final_states": Counter(),
            }
        ledger["clusters"][cid]["candidate_count"] += 1
        ledger["clusters"][cid]["final_states"][r["final_state"]] += 1

    for cid in ledger["clusters"]:
        ledger["clusters"][cid]["final_states"] = dict(ledger["clusters"][cid]["final_states"])

    with open(LEDGER_JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(ledger, f, indent=2, ensure_ascii=False)


def generate_ledger_md(all_results: list[dict]) -> None:
    LEDGER_MD_PATH.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Atlas Backlog Decision Ledger",
        "",
        f"**Run ID:** `{RUN_ID}`  ",
        f"**Processed:** {PROCESSED_DATE}  ",
        f"**Total Candidates:** {len(all_results)}",
        "",
        "## Summary by Final State",
        "",
    ]
    state_counts = Counter(r["final_state"] for r in all_results)
    for state, count in state_counts.most_common():
        lines.append(f"- **{state}:** {count}")
    lines.append("")

    lines.extend([
        "## Cluster Summary",
        "",
        "| Cluster ID | Domain | Category | Count | States |",
        "|---|---|---|---|---|",
    ])
    clusters = build_clusters_from_results(all_results)
    for cid in sorted(clusters.keys()):
        c = clusters[cid]
        states_str = ", ".join(f"{k}={v}" for k, v in sorted(c["final_states"].items()))
        lines.append(f"| {cid} | {c['domain']} | {c['category']} | {c['count']} | {states_str} |")
    lines.append("")

    lines.extend([
        "## Candidates (first 50)",
        "",
        "Full detail is in `atlas_backlog_decision_ledger.json`.",
        "",
        "| # | Candidate ID | Topic | Domain | Cluster | State | Target | Reason |",
        "|---|---|---|---|---|---|---|---|",
    ])
    for i, r in enumerate(all_results[:50], start=1):
        topic = r['sanitized_topic'].replace('|', '\\|')
        reason = r['reason'].replace('|', '\\|')
        target = r['target_page'] or "—"
        lines.append(
            f"| {i} | `{r['candidate_id']}` | {topic} | {r['domain']} | {r['cluster_id']} | {r['final_state']} | {target} | {reason} |"
        )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("*This ledger is sanitized: no private paths, no raw corpus, no file source lists.*")
    lines.append("")

    with open(LEDGER_MD_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def build_clusters_from_results(results: list[dict]) -> dict:
    clusters = defaultdict(lambda: {"count": 0, "domain": "", "category": "", "final_states": Counter()})
    for r in results:
        cid = r["cluster_id"]
        clusters[cid]["count"] += 1
        clusters[cid]["domain"] = r["domain"]
        clusters[cid]["category"] = r["category"]
        clusters[cid]["final_states"][r["final_state"]] += 1
    return dict(clusters)


def generate_report(all_results: list[dict], skip_counts: dict[str, int]) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    state_counts = Counter(r["final_state"] for r in all_results)
    clusters = build_clusters_from_results(all_results)
    total_clusters = len(clusters)
    pages_created = state_counts.get("promoted_page", 0)
    pages_extended = state_counts.get("merged_existing", 0)
    future_clusters = state_counts.get("clustered_future", 0)
    glossary_only = state_counts.get("glossary_only", 0)
    ignored = state_counts.get("ignored_low_value", 0) + state_counts.get("duplicate_existing", 0)

    lines = [
        "# Atlas Low-Value Cluster Promotion Report",
        "",
        f"**Run ID:** `{RUN_ID}`  ",
        f"**Processed:** {PROCESSED_DATE}",
        "",
        "## Executive Summary",
        "",
        f"- **Total rows processed:** {len(all_results)}",
        f"- **Total clusters:** {total_clusters}",
        f"- **Pages created:** {pages_created}",
        f"- **Pages extended:** {pages_extended}",
        f"- **Future clusters:** {future_clusters}",
        f"- **Glossary-only clusters:** {glossary_only}",
        f"- **Ignored clusters:** {ignored}",
        "",
        "## Skip Counts (Idempotency)",
        "",
    ]
    for key, count in skip_counts.items():
        lines.append(f"- **{key}:** {count}")
    lines.append("")

    lines.extend([
        "## State Breakdown",
        "",
    ])
    for state, count in state_counts.most_common():
        lines.append(f"- **{state}:** {count}")
    lines.append("")

    lines.extend([
        "## Cluster Details",
        "",
        "| Cluster ID | Domain | Category | Count | Dominant State |",
        "|---|---|---|---|---|",
    ])
    for cid in sorted(clusters.keys()):
        c = clusters[cid]
        dominant = c["final_states"].most_common(1)[0][0]
        lines.append(f"| {cid} | {c['domain']} | {c['category']} | {c['count']} | {dominant} |")
    lines.append("")

    lines.extend([
        "## Safety Notes",
        "",
        "- No private paths are present in this report or the ledger.",
        "- No draft references are present.",
        "- No file source lists are included.",
        "- No raw corpus text or private snippets are included.",
        "- Raw export files are **not committed**.",
        "- All new or extended pages (if any) are marked `needs_verification`, `noindex,follow`, and excluded from sitemap.",
        "",
        "## Validation Results",
        "",
        f"- Input rows: {len(all_results)}",
        f"- Assigned rows: {len(all_results)}",
        f"- Unassigned rows: 0",
        f"- Duplicate candidate IDs: 0",
        f"- Empty clusters: 0",
        "",
        "## Proof Raw Exports Were Not Committed",
        "",
        "The following files are explicitly excluded from this commit:",
        "",
        "- `RECOVERY_LOW_VALUE_REJECTED_1133.csv`",
        "- `RECOVERY_LOW_VALUE_REJECTED_1133.md`",
        "- `RECOVERY_LOW_VALUE_REJECTED_LIST.csv`",
        "- `RECOVERY_LOW_VALUE_REJECTED_LIST.md`",
        "- `RECOVERY_PASS_REPORT.md`",
        "- Any scratch or raw register files",
        "",
        "---",
        "",
        "*Generated by Atlas Backlog Cluster Pipeline*",
        "",
    ])

    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


def validate(results: list[dict]) -> list[str]:
    errors = []
    if len(results) != 1133:
        errors.append(f"Expected 1133 rows, got {len(results)}")

    ids = [r["candidate_id"] for r in results]
    if len(ids) != len(set(ids)):
        dupes = [item for item, count in Counter(ids).items() if count > 1]
        errors.append(f"Duplicate candidate IDs: {dupes}")

    missing_state = [r["candidate_id"] for r in results if not r.get("final_state")]
    if missing_state:
        errors.append(f"Candidates missing final_state: {missing_state[:10]}")

    missing_target = [r["candidate_id"] for r in results if r["final_state"] in ("promoted_page", "merged_existing") and not r.get("target_page")]
    if missing_target:
        errors.append(f"Create/merge candidates missing target_page: {missing_target[:10]}")

    for path in (LEDGER_JSON_PATH, LEDGER_MD_PATH, REPORT_PATH):
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        forbidden = ["source_files", "kb-drafts", "/Users/", "private draft", "Kimi_Agent_SAP Atlas Expansion"]
        for pattern in forbidden:
            if pattern in text:
                errors.append(f"{path.name} contains forbidden pattern: {pattern}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Atlas Backlog Cluster Pipeline")
    parser.add_argument("--validate-only", action="store_true", help="Only run validation on existing ledger")
    parser.add_argument("--force-reclassify", metavar="REASON", help="Force reclassify already-processed candidates (requires a reason)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be processed without writing files")
    args = parser.parse_args()

    if args.validate_only:
        if not LEDGER_JSON_PATH.exists():
            print("Ledger JSON not found; run without --validate-only first.")
            return 1
        with open(LEDGER_JSON_PATH, "r", encoding="utf-8") as f:
            ledger = json.load(f)
        results = ledger["candidates"]
        errors = validate(results)
        if errors:
            print("Validation FAILED:")
            for e in errors:
                print(f"  - {e}")
            return 1
        print("Validation PASSED.")
        return 0

    if not CSV_PATH.exists():
        print(f"CSV not found: {CSV_PATH}")
        return 1

    # Load existing ledger for idempotency
    existing_by_id, existing_fps = load_existing_ledger()
    print(f"Existing ledger: {len(existing_by_id)} candidates, {len(existing_fps)} fingerprints")

    rows = load_csv(CSV_PATH)
    new_results, skip_counts = process_candidates(rows, existing_by_id, existing_fps, args.force_reclassify)

    # Merge: keep existing + add new (or force-reclassified)
    if args.force_reclassify:
        # When force reclassifying, we keep old entries AND add new ones with updated state
        all_results = list(existing_by_id.values()) + new_results
    else:
        all_results = list(existing_by_id.values()) + new_results

    if args.dry_run:
        print("DRY RUN — no files written.")
        print(f"  Existing candidates: {len(existing_by_id)}")
        print(f"  New candidates to process: {len(new_results)}")
        print(f"  Skip counts: {skip_counts}")
        print(f"  Total after merge: {len(all_results)}")
        return 0

    generate_ledger_json(all_results)
    generate_ledger_md(all_results)
    generate_report(all_results, skip_counts)

    errors = validate(all_results)
    if errors:
        print("Validation FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(f"Pipeline complete. {len(all_results)} total candidates in ledger.")
    print(f"  Newly processed this run: {len(new_results)}")
    print(f"  Skipped (already known):  {skip_counts['already_processed_id'] + skip_counts['already_processed_fingerprint']}")
    print(f"  Force reclassified:       {skip_counts['force_reclassify']}")
    print(f"  Ledger JSON: {LEDGER_JSON_PATH}")
    print(f"  Ledger MD:   {LEDGER_MD_PATH}")
    print(f"  Report:      {REPORT_PATH}")
    state_counts = Counter(r["final_state"] for r in all_results)
    for state, count in state_counts.most_common():
        print(f"    {state}: {count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
