#!/usr/bin/env python3
"""Generate Atlas update proposals from research pages.

Scans the research/ section, reads frontmatter, matches against the Atlas compact
index, and writes structured proposal candidates to ai/research-atlas-proposals.json.

Safety:
- Never edits Atlas pages.
- Never marks content as verified.
- Never creates public pages.
- Research pages remain noindex.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[1]
BASE_URL = "https://dkharlanau.github.io"
RESEARCH_DIR = REPO_ROOT / "research"
ATLAS_INDEX_PATH = REPO_ROOT / "ai" / "atlas-compact-index.json"
OUTPUT_PATH = REPO_ROOT / "ai" / "research-atlas-proposals.json"

# Thresholds aligned with match_atlas_signal.py
UPDATE_THRESHOLD = 0.34
REVIEW_THRESHOLD = 0.18


def load_json(path: Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return data


def parse_frontmatter(path: Path) -> tuple[dict[str, Any], str]:
    """Extract YAML frontmatter and body from a Markdown file."""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if not content.startswith("---"):
        return {}, content

    end = content.find("---", 3)
    if end == -1:
        return {}, content

    fm_text = content[3:end].strip()
    body = content[end + 3:].strip()

    try:
        fm = yaml.safe_load(fm_text) or {}
    except Exception as e:
        print(f"YAML parse error in {path}: {e}", file=sys.stderr)
        fm = {}

    return fm, body


def discover_research_pages() -> list[dict[str, Any]]:
    """Discover all research pages under research/."""
    pages = []
    for subdir in ["briefs", "comparisons", "watchlists"]:
        dir_path = RESEARCH_DIR / subdir
        if not dir_path.exists():
            continue
        for md_path in sorted(dir_path.glob("*.md")):
            rel_path = md_path.relative_to(REPO_ROOT).as_posix()
            fm, body = parse_frontmatter(md_path)
            if not fm:
                continue
            # Skip non-research pages (e.g., index if it were in subdir)
            if fm.get("type") not in {"research_brief", "comparison", "watchlist", "source_map"}:
                continue
            pages.append({
                "path": rel_path,
                "fm": fm,
                "body": body,
            })
    return pages


def token_set(texts: list[str]) -> set[str]:
    tokens: set[str] = set()
    stopwords = {
        "the", "and", "for", "with", "from", "that", "this", "how", "when",
        "where", "what", "why", "into", "page", "sap", "are", "is", "not",
        "but", "or", "to", "of", "in", "on", "at", "by", "as", "a", "an",
    }
    for text in texts:
        for token in re.findall(r"[a-z0-9][a-z0-9+.-]{2,}", text.lower()):
            if token not in stopwords:
                tokens.add(token)
    return tokens


def match_research_to_atlas(research: dict[str, Any], index: dict[str, Any]) -> dict[str, Any]:
    """Match a research page against the Atlas compact index.

    Returns matcher-style result with candidates and decision.
    """
    fm = research["fm"]
    title = fm.get("title", "")
    topics = fm.get("topics", []) or []
    description = fm.get("description", "")
    related_atlas = fm.get("related_atlas", []) or []
    canonical_related_atlas = {
        value if value.startswith("http") else f"{BASE_URL}{value}"
        for value in related_atlas
    }

    query_tokens = token_set([title, description] + topics)
    entries = index.get("entries", [])
    candidates = []

    for entry in entries:
        entry_tokens = set(entry.get("matching_terms", []))
        if not entry_tokens:
            continue

        overlap = query_tokens & entry_tokens
        if not overlap:
            continue

        score = len(overlap) / max(len(query_tokens), 1)

        match_reasons = []
        if overlap:
            match_reasons.append(f"term overlap: {', '.join(sorted(overlap)[:5])}")

        # Boost if explicitly linked from research frontmatter
        if entry.get("url", "") in canonical_related_atlas:
            score = max(score, UPDATE_THRESHOLD + 0.01)
            match_reasons.append("explicitly linked in research frontmatter")

        candidates.append({
            "path": entry.get("path", ""),
            "url": entry.get("url", ""),
            "title": entry.get("title", ""),
            "score": round(score, 3),
            "match_reasons": match_reasons,
        })

    candidates.sort(key=lambda c: c["score"], reverse=True)
    top = candidates[:5]

    if top and top[0]["score"] >= UPDATE_THRESHOLD:
        decision = {
            "target_decision": "update_existing_page",
            "confidence": "high" if top[0]["score"] >= 0.5 else "medium",
            "review_status": "draft",
            "reason": "Top Atlas candidate clears update threshold.",
        }
    elif top and top[0]["score"] >= REVIEW_THRESHOLD:
        decision = {
            "target_decision": "needs_research",
            "confidence": "low",
            "review_status": "draft",
            "reason": "Candidate above review threshold but below update threshold; needs human review.",
        }
    else:
        decision = {
            "target_decision": "create_new_page_candidate",
            "confidence": "low",
            "review_status": "draft",
            "reason": "No existing Atlas page clears the review threshold; candidate for new page if evidence is strong.",
        }

    return {
        "decision": decision,
        "candidates": top,
    }


def determine_action(research: dict[str, Any], match_result: dict[str, Any]) -> str:
    """Determine proposed action from research metadata and match result."""
    fm = research["fm"]
    evidence_level = fm.get("evidence_level", "low")
    source_count = fm.get("source_count", 0)
    related_atlas = fm.get("related_atlas", []) or []
    decision = match_result["decision"]["target_decision"]

    # Low evidence or few sources → needs_review
    if evidence_level == "low" or source_count < 2:
        return "needs_review"

    # Explicit related_atlas links with decent evidence → extend
    if related_atlas and evidence_level in {"high", "medium"}:
        return "extend"

    # Strong matcher result → extend
    if decision == "update_existing_page" and match_result["candidates"]:
        return "extend"

    # No match but high evidence → create
    if decision == "create_new_page_candidate" and evidence_level == "high" and source_count >= 3:
        return "create"

    # Medium evidence, no strong match → needs_review
    if evidence_level == "medium":
        return "needs_review"

    return "ignore"


def build_proposal(research: dict[str, Any], match_result: dict[str, Any]) -> dict[str, Any]:
    """Build a single research-to-Atlas proposal."""
    fm = research["fm"]
    path = research["path"]
    permalink = fm.get("permalink", "")
    title = fm.get("title", "")
    evidence_level = fm.get("evidence_level", "low")
    source_count = fm.get("source_count", 0)
    related_atlas = fm.get("related_atlas", []) or []
    topics = fm.get("topics", []) or []
    action = determine_action(research, match_result)
    decision = match_result["decision"]
    candidates = match_result["candidates"]

    # Confidence based on evidence and match quality
    if evidence_level == "high" and candidates and candidates[0]["score"] >= UPDATE_THRESHOLD:
        confidence = "high"
    elif evidence_level == "medium" and candidates and candidates[0]["score"] >= REVIEW_THRESHOLD:
        confidence = "medium"
    else:
        confidence = "low"

    # Source confidence warnings
    warnings: list[str] = []
    if evidence_level == "low":
        warnings.append("Research evidence level is low; claims need verification before Atlas promotion.")
    if source_count < 3:
        warnings.append(f"Only {source_count} source(s) cited; prefer 3+ for Atlas content.")
    if not fm.get("source_body_opened", True):
        warnings.append("Source body was not fully opened; verify claims against primary sources.")

    # Rationale
    rationale_parts = [f"Research page '{title}' has evidence_level={evidence_level} and source_count={source_count}."]
    if related_atlas:
        rationale_parts.append(f"Explicitly links to Atlas pages: {', '.join(related_atlas)}.")
    if candidates:
        rationale_parts.append(
            f"Top Atlas match: {candidates[0]['title']} (score={candidates[0]['score']})."
        )
    rationale_parts.append(f"Matcher decision: {decision['target_decision']} ({decision['confidence']}).")
    rationale = " ".join(rationale_parts)

    # Candidate target
    candidate_target = None
    if related_atlas:
        # Prefer first explicitly linked Atlas page
        candidate_target = {
            "url": related_atlas[0],
            "path": related_atlas[0].strip("/") + ".md",
            "title": None,  # Will be resolved later if needed
        }
    elif candidates:
        candidate_target = {
            "url": candidates[0]["url"],
            "path": candidates[0]["path"],
            "title": candidates[0]["title"],
        }

    proposal: dict[str, Any] = {
        "schema": "dkharlanau.research_atlas_proposal",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_research_page": {
            "path": path,
            "url": permalink,
            "title": title,
            "type": fm.get("type", ""),
            "evidence_level": evidence_level,
            "source_count": source_count,
            "topics": topics,
        },
        "proposed_action": action,
        "rationale": rationale,
        "confidence": confidence,
        "source_confidence_warnings": warnings,
        "matcher_result": {
            "decision": decision,
            "candidates": candidates,
        },
        "safety": {
            "direct_page_edits": False,
            "auto_publish": False,
            "requires_human_review": True,
            "noindex": True,
            "marks_verified": False,
        },
    }

    if candidate_target:
        proposal["candidate_atlas_target"] = candidate_target

    return proposal


def generate_proposals(check_mode: bool = False) -> dict[str, Any]:
    """Scan research pages and generate proposals."""
    index = load_json(ATLAS_INDEX_PATH)
    research_pages = discover_research_pages()
    proposals = []

    for research in research_pages:
        match_result = match_research_to_atlas(research, index)
        proposal = build_proposal(research, match_result)
        proposals.append(proposal)

    output = {
        "schema": "dkharlanau.research_atlas_proposals",
        "schema_version": "1.0",
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "canonical_url": "https://dkharlanau.github.io/ai/research-atlas-proposals.json",
        "description": (
            "Structured Atlas update candidates generated from research pages. "
            "These are proposals only; no Atlas pages have been edited or published."
        ),
        "count": len(proposals),
        "proposals": proposals,
    }

    if not check_mode:
        OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)

    return output


def validate_proposals(output: dict[str, Any]) -> list[str]:
    """Validate proposal output against safety and schema rules."""
    issues = []
    proposals = output.get("proposals", [])

    for i, proposal in enumerate(proposals):
        prefix = f"proposal[{i}]"

        # Schema
        if proposal.get("schema") != "dkharlanau.research_atlas_proposal":
            issues.append(f"{prefix}: invalid schema")

        # Required fields
        for field in ["source_research_page", "proposed_action", "rationale", "confidence", "source_confidence_warnings", "safety"]:
            if field not in proposal:
                issues.append(f"{prefix}: missing field '{field}'")

        # Safety rules
        safety = proposal.get("safety", {})
        if safety.get("direct_page_edits") is not False:
            issues.append(f"{prefix}: safety.direct_page_edits must be False")
        if safety.get("auto_publish") is not False:
            issues.append(f"{prefix}: safety.auto_publish must be False")
        if safety.get("requires_human_review") is not True:
            issues.append(f"{prefix}: safety.requires_human_review must be True")
        if safety.get("noindex") is not True:
            issues.append(f"{prefix}: safety.noindex must be True")
        if safety.get("marks_verified") is not False:
            issues.append(f"{prefix}: safety.marks_verified must be False")

        # Action values
        action = proposal.get("proposed_action", "")
        if action not in {"create", "extend", "ignore", "needs_review"}:
            issues.append(f"{prefix}: invalid action '{action}'")

        # Confidence values
        confidence = proposal.get("confidence", "")
        if confidence not in {"high", "medium", "low"}:
            issues.append(f"{prefix}: invalid confidence '{confidence}'")

        # Source research page must be noindex in reality
        src = proposal.get("source_research_page", {})
        if not src.get("path", "").startswith("research/"):
            issues.append(f"{prefix}: source path must be under research/")

    return issues


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="Validate existing proposals without regenerating.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Override output path (default: ai/research-atlas-proposals.json).",
    )
    args = parser.parse_args()

    global OUTPUT_PATH
    if args.output:
        OUTPUT_PATH = args.output

    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"CHECK FAILED: {OUTPUT_PATH} does not exist.", file=sys.stderr)
            return 1
        output = load_json(OUTPUT_PATH)
        issues = validate_proposals(output)
        if issues:
            print(f"CHECK FAILED — {len(issues)} issue(s):")
            for issue in issues:
                print(f"  ✗ {issue}")
            return 1
        print(f"CHECK PASSED — {output.get('count', 0)} proposals valid and safe.")
        return 0

    output = generate_proposals()
    issues = validate_proposals(output)
    if issues:
        print(f"GENERATION FAILED — {len(issues)} issue(s):")
        for issue in issues:
            print(f"  ✗ {issue}")
        return 1

    print(f"Generated {output['count']} research-to-Atlas proposals.")
    print(f"Output: {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
