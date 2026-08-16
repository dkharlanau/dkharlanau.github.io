#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
from difflib import SequenceMatcher
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT_DATA = ROOT / "labs" / "assessment" / "data"
SEEDS_PATH = ASSESSMENT_DATA / "candidate-generation-seeds.json"
CASE_SETS_PATH = ASSESSMENT_DATA / "case-sets.json"
OUTPUT_PATH = ASSESSMENT_DATA / "question-candidates.json"
SOURCES_ROOT = ROOT / "_data" / "labs" / "enterprise_context" / "sources"

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "from",
    "has", "have", "in", "into", "is", "it", "of", "on", "or", "the", "to",
    "with", "without", "wrong", "expected", "business", "document", "message",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_yaml(path: Path) -> Any:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def normalize_words(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return [word for word in words if word not in STOPWORDS and len(word) > 1]


def normalize_text(text: str) -> str:
    return " ".join(normalize_words(text))


def similarity(left: str, right: str) -> float:
    left_words = normalize_words(left)
    right_words = normalize_words(right)
    if not left_words or not right_words:
        return 0.0
    left_set = set(left_words)
    right_set = set(right_words)
    union = left_set | right_set
    jaccard = len(left_set & right_set) / len(union) if union else 0.0
    sequence = SequenceMatcher(None, " ".join(left_words), " ".join(right_words)).ratio()
    return round(max(jaccard, sequence), 4)


def collect_source_ids(value: Any, result: set[str]) -> None:
    if isinstance(value, str):
        if value.startswith("SRC-"):
            result.add(value)
        return
    if isinstance(value, dict):
        for key, item in value.items():
            collect_source_ids(key, result)
            collect_source_ids(item, result)
        return
    if isinstance(value, list):
        for item in value:
            collect_source_ids(item, result)


def known_source_ids() -> set[str]:
    result: set[str] = set()
    for path in sorted(SOURCES_ROOT.rglob("*.yml")):
        collect_source_ids(load_yaml(path), result)
    return result


def existing_cases() -> list[dict[str, Any]]:
    manifest = load_json(CASE_SETS_PATH)
    rows: list[dict[str, Any]] = []
    for case_set in manifest["sets"]:
        path = ROOT / case_set["url"].lstrip("/")
        rows.extend(load_jsonl(path))
    return rows


def failure_by_id(graph: dict[str, Any], failure_id: str) -> dict[str, Any]:
    for failure in graph.get("failure_modes", []):
        if failure.get("id") == failure_id:
            return failure
    raise ValueError(f"Failure mode {failure_id} not found in graph {graph.get('id')}")


def candidate_id(prefix: str, failure_id: str) -> str:
    suffix = failure_id
    for marker in ("FAIL-SD-BILLING-", "INTOPS-FAIL-"):
        if suffix.startswith(marker):
            suffix = suffix[len(marker):]
            break
    suffix = re.sub(r"[^A-Z0-9]+", "-", suffix.upper()).strip("-")
    return f"{prefix}-{suffix}"


def compact_checks(checks: list[str], start: int, end: int) -> str:
    selected = checks[start:end]
    return ", ".join(selected)


def build_expected_points(failure: dict[str, Any]) -> list[str]:
    checks = [str(item) for item in failure.get("first_checks", [])]
    first = compact_checks(checks, 0, 3)
    second = compact_checks(checks, 3, 6)
    points = [
        "Start from the documented symptom and define the expected business state before changing downstream data or documents.",
        f"Use the first evidence checks before correction: {first}." if first else "Identify the first evidence that distinguishes the root cause from a downstream symptom.",
        f"Continue the hypothesis tree with: {second}." if second else "Trace the failure to the first wrong layer before choosing a recovery action.",
        "Name the owner of the first wrong layer and separate that responsibility from teams that only see the downstream symptom.",
        "Define proof of cause and proof of business completion before closing the case.",
    ]
    return points


def build_evidence_map(failure_id: str, source_refs: list[str], point_count: int) -> list[dict[str, Any]]:
    paths = [
        f"failure_modes.{failure_id}.symptom",
        f"failure_modes.{failure_id}.first_checks",
        f"failure_modes.{failure_id}.first_checks",
        "lead_lens",
        "lead_lens",
    ]
    return [
        {
            "expected_point_index": index,
            "graph_path": paths[min(index, len(paths) - 1)],
            "source_refs": source_refs,
        }
        for index in range(point_count)
    ]


def dedup_signature(graph_id: str, failure_id: str, symptom: str) -> str:
    raw = f"{graph_id}|{failure_id}|{normalize_text(symptom)}".encode("utf-8")
    return hashlib.sha256(raw).hexdigest()[:24]


def existing_case_similarity(symptom: str, cases: list[dict[str, Any]], threshold: float) -> tuple[float, list[str]]:
    scores: list[tuple[str, float]] = []
    for case in cases:
        comparison = f"{case.get('title', '')} {case.get('prompt', '')}"
        score = similarity(symptom, comparison)
        scores.append((case["id"], score))
    scores.sort(key=lambda item: item[1], reverse=True)
    max_score = scores[0][1] if scores else 0.0
    matches = [case_id for case_id, score in scores if score >= threshold]
    return max_score, matches


def build_candidate(
    graph: dict[str, Any],
    seed: dict[str, Any],
    failure_id: str,
    source_refs: list[str],
    cases: list[dict[str, Any]],
    threshold: float,
) -> dict[str, Any]:
    failure = failure_by_id(graph, failure_id)
    symptom = str(failure["symptom"]).strip()
    avoid = str(failure.get("avoid", "Do not repair the final symptom before proving the root cause.")).strip()
    expected = build_expected_points(failure)
    max_similarity, matches = existing_case_similarity(symptom, cases, threshold)
    status = "rejected_duplicate" if matches else "candidate"
    cid = candidate_id(seed["candidate_prefix"], failure_id)
    title = symptom.rstrip(".")
    if len(title) > 92:
        title = title[:89].rstrip() + "..."
    prompt = (
        f"Synthetic assessment candidate. {symptom} Build a Lead-level diagnosis. "
        "Find the first wrong layer, explain ownership, and define evidence that proves the cause before correction."
    )
    return {
        "id": cid,
        "status": status,
        "generation_pattern": "symptom_to_root_cause",
        "track": seed["track"],
        "level": seed["level"],
        "title": title,
        "prompt": prompt,
        "expected_points": expected,
        "follow_up_questions": [
            "Which check would most quickly separate the root cause from a downstream symptom?",
            "What evidence would prove the business process is complete after the fix?",
        ],
        "red_flags": [
            avoid,
            "Repairs the downstream symptom before proving the first wrong state.",
        ],
        "graph_refs": [graph["id"], failure_id],
        "human_refs": [seed["human_ref"]],
        "source_refs": source_refs,
        "evidence_map": build_evidence_map(failure_id, source_refs, len(expected)),
        "generation_reason": (
            f"Rejected before review because the failure symptom overlaps published case(s): {', '.join(matches)}."
            if matches
            else "New review-stage candidate from a whitelisted graph failure mode with explicit primary-source references."
        ),
        "dedup_signature": dedup_signature(graph["id"], failure_id, symptom),
        "dedup": {
            "max_similarity": max_similarity,
            "threshold": threshold,
            "matching_case_ids": matches,
        },
        "review": {"reviewer_note": "", "reviewed_at": None},
    }


def generate() -> dict[str, Any]:
    seeds = load_json(SEEDS_PATH)
    cases = existing_cases()
    sources = known_source_ids()
    threshold = float(seeds["dedup_threshold"])
    candidates: list[dict[str, Any]] = []

    for seed in seeds["graphs"]:
        graph_path = ROOT / seed["path"]
        graph = load_yaml(graph_path)
        if not isinstance(graph, dict) or not graph.get("id"):
            raise ValueError(f"Invalid graph file: {seed['path']}")
        for failure_id, source_refs in seed["failure_sources"].items():
            missing_sources = sorted(set(source_refs) - sources)
            if missing_sources:
                raise ValueError(f"Unknown source refs for {failure_id}: {missing_sources}")
            candidate = build_candidate(graph, seed, failure_id, list(source_refs), cases, threshold)
            candidates.append(candidate)

    candidates.sort(key=lambda item: item["id"])
    signatures = [item["dedup_signature"] for item in candidates]
    if len(signatures) != len(set(signatures)):
        raise ValueError("Candidate dedup signatures must be unique")

    published_ids = {case["id"] for case in cases}
    if any(item["id"] in published_ids for item in candidates):
        raise ValueError("Candidate IDs must not overlap published case IDs")

    return {
        "id": "sap-lead-question-candidate-inventory",
        "version": "1.0.0",
        "updated_at": seeds["updated_at"],
        "published_case_count": len(cases),
        "publication_boundary": "Candidate inventory is review-stage only and is not referenced by case-sets.json.",
        "candidate_count": sum(item["status"] == "candidate" for item in candidates),
        "rejected_duplicate_count": sum(item["status"] == "rejected_duplicate" for item in candidates),
        "items": candidates,
    }


def serialize(payload: dict[str, Any]) -> str:
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate graph-backed SAP Lead assessment question candidates.")
    parser.add_argument("--check", action="store_true", help="Verify the committed candidate inventory is current.")
    args = parser.parse_args()

    payload = generate()
    rendered = serialize(payload)
    if args.check:
        if not OUTPUT_PATH.exists():
            print(f"Missing generated candidate inventory: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        existing = OUTPUT_PATH.read_text(encoding="utf-8")
        if existing != rendered:
            print(f"Stale generated candidate inventory: {OUTPUT_PATH.relative_to(ROOT)}")
            return 2
        print(
            "Assessment candidate inventory is current: "
            f"{payload['candidate_count']} candidate(s), "
            f"{payload['rejected_duplicate_count']} duplicate rejection(s), "
            f"{payload['published_case_count']} published cases unchanged."
        )
        return 0

    OUTPUT_PATH.write_text(rendered, encoding="utf-8")
    print(
        f"Generated {OUTPUT_PATH.relative_to(ROOT)}: "
        f"{payload['candidate_count']} candidate(s), "
        f"{payload['rejected_duplicate_count']} duplicate rejection(s), "
        f"{payload['published_case_count']} published cases unchanged."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
