#!/usr/bin/env python3
"""Dry-run matcher from an enriched professional signal to Atlas pages.

Reads one signal JSON and the compact public Atlas index. It does not read full
page bodies and does not edit public pages.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INDEX = REPO_ROOT / "ai" / "atlas-compact-index.json"

UPDATE_THRESHOLD = 0.34
REVIEW_THRESHOLD = 0.18

STOPWORDS = {
    "and",
    "for",
    "from",
    "into",
    "that",
    "the",
    "this",
    "with",
    "what",
    "when",
    "where",
    "why",
}


def load_json(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def normalize_phrase(value: Any) -> str:
    text = str(value or "").lower()
    text = re.sub(r"[^a-z0-9+/#.-]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def token_set(values: list[str]) -> set[str]:
    tokens: set[str] = set()
    for value in values:
        for token in re.findall(r"[a-z0-9][a-z0-9+.-]{2,}", value.lower()):
            if token not in STOPWORDS:
                tokens.add(token)
    return tokens


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def nested(signal: dict[str, Any], key: str, default: Any = "") -> Any:
    return signal.get(key, default)


def normalized_signal(raw: dict[str, Any]) -> dict[str, Any]:
    signal = raw.get("signal", raw)
    evidence = raw.get("evidence", raw.get("source_evidence", {}))
    classification = raw.get("classification", raw)

    concrete_facts = as_list(evidence.get("concrete_facts", raw.get("concrete_facts", [])))
    product_names = as_list(evidence.get("product_names", raw.get("product_names", [])))
    named_components = as_list(evidence.get("named_components", raw.get("named_components", [])))
    tags = as_list(classification.get("tags", raw.get("tags", [])))

    return {
        "record_id": raw.get("record_id", raw.get("signal_id", "signal")),
        "title": nested(signal, "title", raw.get("title", "")),
        "summary": raw.get("summary", raw.get("content_snippet", "")),
        "source_url": nested(signal, "source_url", raw.get("source_url", "")),
        "source_name": nested(signal, "source_name", raw.get("source_name", "")),
        "source_date": nested(signal, "source_date", raw.get("source_date", "")),
        "source_body_opened": bool(evidence.get("source_body_opened", raw.get("source_body_opened", False))),
        "concrete_facts": [str(item) for item in concrete_facts if str(item).strip()],
        "product_names": [str(item) for item in product_names if str(item).strip()],
        "named_components": [str(item) for item in named_components if str(item).strip()],
        "sap_domain": classification.get("sap_domain", raw.get("sap_domain", "")),
        "business_process": classification.get("business_process", raw.get("business_process", "")),
        "technology_area": classification.get("technology_area", raw.get("technology_area", "")),
        "operational_implication": classification.get("operational_implication", raw.get("operational_implication", "")),
        "tags": [normalize_phrase(item) for item in tags if str(item).strip()],
    }


def evidence_failures(signal: dict[str, Any]) -> list[str]:
    failures = []
    if not signal["source_url"]:
        failures.append("missing source_url")
    if not signal["source_body_opened"]:
        failures.append("source body was not opened")
    if len(signal["concrete_facts"]) < 2:
        failures.append("fewer than two concrete facts")
    return failures


def signal_terms(signal: dict[str, Any]) -> tuple[set[str], set[str]]:
    phrase_values = [
        signal["title"],
        signal["summary"],
        signal["sap_domain"],
        signal["business_process"],
        signal["technology_area"],
        signal["operational_implication"],
        *signal["tags"],
        *signal["product_names"],
        *signal["named_components"],
        *signal["concrete_facts"],
    ]
    phrases = {normalize_phrase(value) for value in phrase_values if normalize_phrase(value)}
    tokens = token_set(list(phrases))
    return phrases, tokens


def entry_terms(entry: dict[str, Any]) -> tuple[set[str], set[str]]:
    values = [
        entry.get("title", ""),
        entry.get("description", ""),
        entry.get("atlas_section", ""),
        entry.get("domain", ""),
        entry.get("subdomain", ""),
        entry.get("concept_type", ""),
        entry.get("sap_area", ""),
        entry.get("business_process", ""),
        *as_list(entry.get("tags", [])),
        *as_list(entry.get("headings", [])),
        *as_list(entry.get("sap_domain_keywords", [])),
        *as_list(entry.get("matching_terms", [])),
    ]
    phrases = {normalize_phrase(value) for value in values if normalize_phrase(value)}
    tokens = token_set(list(phrases))
    return phrases, tokens


def score_entry(signal: dict[str, Any], entry: dict[str, Any]) -> dict[str, Any]:
    sig_phrases, sig_tokens = signal_terms(signal)
    ent_phrases, ent_tokens = entry_terms(entry)

    phrase_overlap = sorted(sig_phrases & ent_phrases)
    token_overlap = sorted(sig_tokens & ent_tokens)
    tag_overlap = sorted(set(signal["tags"]) & {normalize_phrase(t) for t in as_list(entry.get("tags", []))})
    product_overlap = sorted(
        {normalize_phrase(p) for p in signal["product_names"] + signal["named_components"]}
        & ent_phrases
    )

    raw_score = 0.0
    raw_score += min(len(phrase_overlap), 5) * 0.11
    raw_score += min(len(tag_overlap), 4) * 0.12
    raw_score += min(len(product_overlap), 3) * 0.14
    raw_score += min(len(token_overlap), 12) * 0.025
    if normalize_phrase(signal["title"]) == normalize_phrase(entry.get("title", "")):
        raw_score += 0.25

    reasons = []
    if tag_overlap:
        reasons.append(f"tag overlap: {', '.join(tag_overlap[:4])}")
    if product_overlap:
        reasons.append(f"product/component overlap: {', '.join(product_overlap[:3])}")
    if phrase_overlap:
        reasons.append(f"phrase overlap: {', '.join(phrase_overlap[:4])}")
    if token_overlap:
        reasons.append(f"term overlap: {', '.join(token_overlap[:8])}")

    return {
        "path": entry.get("path", ""),
        "url": entry.get("url", ""),
        "title": entry.get("title", ""),
        "score": round(min(raw_score, 1.0), 3),
        "match_reasons": reasons[:6],
    }


def match_signal(raw_signal: dict[str, Any], index: dict[str, Any], top_n: int = 5) -> dict[str, Any]:
    signal = normalized_signal(raw_signal)
    failures = evidence_failures(signal)
    entries = index.get("entries", [])

    candidates = sorted(
        (score_entry(signal, entry) for entry in entries),
        key=lambda item: (-item["score"], item["path"]),
    )[:top_n]
    candidates = [item for item in candidates if item["score"] > 0]

    if failures:
        decision = {
            "target_decision": "reject",
            "confidence": "high",
            "review_status": "rejected",
            "reason": "Weak source evidence: " + "; ".join(failures),
        }
    elif candidates and candidates[0]["score"] >= UPDATE_THRESHOLD:
        decision = {
            "target_decision": "update_existing_page",
            "confidence": "high" if candidates[0]["score"] >= 0.55 else "medium",
            "review_status": "draft",
            "reason": "Top Atlas candidate clears update threshold.",
        }
    elif candidates and candidates[0]["score"] >= REVIEW_THRESHOLD:
        decision = {
            "target_decision": "needs_research",
            "confidence": "low",
            "review_status": "needs_research",
            "reason": "Candidate exists but score is below update threshold; human review needed.",
        }
    else:
        decision = {
            "target_decision": "create_new_page_candidate",
            "confidence": "low",
            "review_status": "draft",
            "reason": "Strong source evidence but no existing Atlas page clears the review threshold.",
        }

    return {
        "schema": "dkharlanau.atlas_matcher_result",
        "schema_version": "1.0",
        "signal_id": signal["record_id"],
        "decision": decision,
        "candidates": candidates,
        "evidence_summary": {
            "source_url": signal["source_url"],
            "source_body_opened": signal["source_body_opened"],
            "concrete_fact_count": len(signal["concrete_facts"]),
            "tags": signal["tags"],
        },
        "safety": {
            "index_path": "ai/atlas-compact-index.json",
            "index_entries_loaded": len(entries),
            "full_site_content_loaded": False,
            "page_edits_performed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Dry-run match one signal to Atlas pages.")
    parser.add_argument("--signal", required=True, type=Path, help="Path to enriched signal JSON.")
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX, help="Compact Atlas index JSON.")
    parser.add_argument("--output", type=Path, help="Optional path to write matcher result JSON.")
    parser.add_argument("--top-n", type=int, default=5, help="Number of candidates to return.")
    args = parser.parse_args()

    raw_signal = load_json(args.signal)
    index = load_json(args.index)
    result = match_signal(raw_signal, index, top_n=args.top_n)
    text = json.dumps(result, indent=2, ensure_ascii=False)

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)

    return 0


if __name__ == "__main__":
    sys.exit(main())
