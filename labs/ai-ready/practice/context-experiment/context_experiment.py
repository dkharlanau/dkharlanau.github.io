#!/usr/bin/env python3
"""Compare full-context stuffing with selected, trust-filtered context."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STOP = {
    "a","an","the","is","are","to","of","and","or","for","in","on","at","do","i",
    "what","how","can","when","should","after","it","be","user","directly"
}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokens(text: str) -> set[str]:
    return {
        token for token in re.findall(r"[a-z0-9]+", text.lower())
        if token not in STOP and len(token) > 1
    }


def lexical_score(question: str, document: str) -> float:
    q = tokens(question)
    d = tokens(document)
    if not q or not d:
        return 0.0
    return len(q & d) / len(q)


def select_context(question: str, documents: list[dict], top_k: int = 2) -> list[dict]:
    ranked = []
    for doc in documents:
        if doc.get("trust") != "trusted":
            continue
        score = lexical_score(question, doc["text"])
        if score > 0:
            ranked.append((score, doc["id"], doc))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [item[2] for item in ranked[:top_k]]


def all_context(_: str, documents: list[dict]) -> list[dict]:
    return list(documents)


def evaluate(strategy, cases: list[dict], documents: list[dict]) -> dict:
    recalls = []
    precisions = []
    context_words = []
    untrusted_exposures = 0
    no_evidence_checks = []

    for case in cases:
        selected = strategy(case["question"], documents)
        selected_ids = {doc["id"] for doc in selected}
        expected = set(case["expected_evidence"])

        if expected:
            recalls.append(len(expected & selected_ids) / len(expected))
            precisions.append(len(expected & selected_ids) / len(selected_ids) if selected_ids else 0.0)
        else:
            recalls.append(1.0 if not selected_ids else 0.0)
            precisions.append(1.0 if not selected_ids else 0.0)

        context_words.append(sum(len(doc["text"].split()) for doc in selected))
        untrusted_exposures += sum(doc.get("trust") != "trusted" for doc in selected)
        if case.get("expected_no_evidence"):
            no_evidence_checks.append(not selected)

    n = len(cases) or 1
    return {
        "mean_evidence_recall": sum(recalls) / n,
        "mean_evidence_precision": sum(precisions) / n,
        "average_context_words": sum(context_words) / n,
        "untrusted_exposures": untrusted_exposures,
        "no_evidence_accuracy": (
            sum(no_evidence_checks) / len(no_evidence_checks)
            if no_evidence_checks else None
        ),
    }


def self_test() -> None:
    docs = read_jsonl(BASE_DIR / "documents.jsonl")
    cases = read_jsonl(BASE_DIR / "cases.jsonl")
    full = evaluate(all_context, cases, docs)
    selected = evaluate(select_context, cases, docs)
    assert selected["mean_evidence_recall"] == 1.0
    assert selected["untrusted_exposures"] == 0
    assert selected["no_evidence_accuracy"] == 1.0
    assert selected["average_context_words"] < full["average_context_words"]
    assert selected["mean_evidence_precision"] > full["mean_evidence_precision"]
    print("context-experiment self-test: ok")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0

    docs = read_jsonl(BASE_DIR / "documents.jsonl")
    cases = read_jsonl(BASE_DIR / "cases.jsonl")
    print(json.dumps({
        "all_context": evaluate(all_context, cases, docs),
        "selected_context": evaluate(select_context, cases, docs),
        "lesson": "Context quality is selection plus trust boundaries, not maximum token count."
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
