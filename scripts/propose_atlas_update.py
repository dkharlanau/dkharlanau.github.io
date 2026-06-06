#!/usr/bin/env python3
"""Generate reviewable Atlas update proposals from signals and matcher output.

The script writes proposal JSON only. It never edits Atlas pages.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from match_atlas_signal import load_json, normalized_signal


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "atlas-signal-candidate"


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def source_attribution(signal: dict[str, Any]) -> str:
    source_bits = [
        signal.get("source_name", "") or "source",
        signal.get("source_date", "") or "date unavailable",
        signal.get("source_url", "") or "URL unavailable",
    ]
    return " | ".join(source_bits)


def proposed_content_block(signal: dict[str, Any]) -> str:
    facts = signal.get("concrete_facts", [])
    fact_lines = "\n".join(f"- {fact}" for fact in facts[:4])
    products = ", ".join(signal.get("product_names", [])[:4]) or "not specified"
    components = ", ".join(signal.get("named_components", [])[:4]) or "not specified"
    implication = signal.get("operational_implication", "")
    return "\n".join([
        f"### Source-backed update candidate: {signal['title']}",
        "",
        "Concrete facts from the source:",
        fact_lines,
        "",
        f"Product/process context: {products}",
        f"Named components: {components}",
        f"Operational relevance: {implication}",
        "",
        f"Source: {source_attribution(signal)}",
    ]).strip()


def validation_checklist() -> list[str]:
    return [
        "source URL and date are present",
        "source body was opened",
        "at least two concrete facts are present",
        "target page or new-page rationale is present",
        "proposed content is compact and source-backed",
        "no private paths, local files, secrets, or runtime logs",
    ]


def proposal_risks(signal: dict[str, Any], matcher_result: dict[str, Any]) -> list[str]:
    risks = []
    if len(signal.get("concrete_facts", [])) < 3:
        risks.append("Only minimum source facts are available; reviewer should verify depth.")
    if matcher_result.get("decision", {}).get("confidence") == "low":
        risks.append("Matcher confidence is low; reviewer should confirm target page fit.")
    if not matcher_result.get("candidates"):
        risks.append("No existing Atlas candidate cleared scoring; new-page rationale needs review.")
    return risks


def build_new_page_candidate(signal: dict[str, Any], matcher_result: dict[str, Any]) -> dict[str, Any]:
    candidates = matcher_result.get("candidates", [])
    related_pages = [candidate["url"] for candidate in candidates[:3] if candidate.get("url")]
    if not related_pages:
        related_pages = ["/atlas/research-notes/"]
    return {
        "proposed_path": f"atlas/research-notes/{slugify(signal['title'])}.md",
        "title": signal["title"],
        "atlas_section": "research-notes",
        "noindex_until_reviewed": True,
        "related_pages": related_pages,
        "why_existing_pages_are_insufficient": (
            "The matcher did not find an existing Atlas page above the review "
            "threshold, so this should remain a noindex candidate until a "
            "human confirms it is not a compact update to an existing page."
        ),
    }


def build_proposal(raw_signal: dict[str, Any], matcher_result: dict[str, Any]) -> dict[str, Any]:
    signal = normalized_signal(raw_signal)
    decision = matcher_result.get("decision", {})
    target_decision = decision.get("target_decision", "needs_research")
    candidates = matcher_result.get("candidates", [])

    proposal: dict[str, Any] = {
        "schema": "dkharlanau.atlas_update_proposal",
        "schema_version": "1.0",
        "generated_at": utc_now(),
        "signal_id": signal["record_id"],
        "proposal_status": target_decision,
        "proposal_type": target_decision,
        "signal": {
            "title": signal["title"],
            "source_name": signal["source_name"],
            "source_url": signal["source_url"],
            "source_date": signal["source_date"],
        },
        "evidence": {
            "source_body_opened": signal["source_body_opened"],
            "concrete_facts": signal["concrete_facts"],
            "product_names": signal["product_names"],
            "named_components": signal["named_components"],
        },
        "classification": {
            "sap_domain": signal["sap_domain"],
            "business_process": signal["business_process"],
            "technology_area": signal["technology_area"],
            "operational_implication": signal["operational_implication"],
            "tags": signal["tags"],
        },
        "matcher_decision": decision,
        "atlas_candidates": candidates,
        "risks": proposal_risks(signal, matcher_result),
        "validation_checklist": validation_checklist(),
        "safety": {
            "direct_page_edits": False,
            "auto_publish": False,
            "requires_human_review": True,
        },
    }

    if target_decision == "update_existing_page" and candidates:
        target = candidates[0]
        proposal.update({
            "proposal_type": "existing_page_update",
            "target": {
                "path": target["path"],
                "url": target["url"],
                "title": target["title"],
            },
            "why_this_update_belongs_there": (
                f"The matcher ranked this page highest because: "
                f"{'; '.join(target.get('match_reasons', [])[:3])}."
            ),
            "proposed_content_block": proposed_content_block(signal),
            "source_attribution_block": source_attribution(signal),
        })
    elif target_decision == "create_new_page_candidate":
        proposal.update({
            "proposal_type": "new_page_candidate",
            "proposed_new_page": build_new_page_candidate(signal, matcher_result),
            "why_this_update_belongs_there": (
                "No existing Atlas page cleared the review threshold; keep this "
                "as a noindex candidate until reviewed."
            ),
            "proposed_content_block": proposed_content_block(signal),
            "source_attribution_block": source_attribution(signal),
        })
    else:
        proposal.update({
            "proposal_type": target_decision,
            "why_this_update_belongs_there": "No Atlas page update should be drafted for this decision.",
            "source_attribution_block": source_attribution(signal),
        })

    return proposal


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a reviewable Atlas update proposal.")
    parser.add_argument("--signal", required=True, type=Path, help="Path to enriched signal JSON.")
    parser.add_argument("--match", required=True, type=Path, help="Path to matcher result JSON.")
    parser.add_argument("--output", type=Path, help="Optional path to write proposal JSON.")
    args = parser.parse_args()

    proposal = build_proposal(load_json(args.signal), load_json(args.match))
    text = json.dumps(proposal, indent=2, ensure_ascii=False)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
