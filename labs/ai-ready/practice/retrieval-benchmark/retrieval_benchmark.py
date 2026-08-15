#!/usr/bin/env python3
"""Compare lexical, toy-vector, and hybrid retrieval.

The vector representation is intentionally tiny and deterministic. It teaches
cosine retrieval mechanics; it is not a production embedding model.
"""
from __future__ import annotations

import argparse
import json
import math
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STOP = {"a","an","the","is","are","to","of","and","or","for","in","on","after","from"}


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def tokens(text: str) -> list[str]:
    return [
        t for t in re.findall(r"[a-z0-9]+", text.lower())
        if t not in STOP and len(t) > 1
    ]


def lexical_score(query: str, text: str) -> float:
    q = set(tokens(query))
    d = set(tokens(text))
    if not q or not d:
        return 0.0
    return len(q & d) / math.sqrt(len(q) * len(d))


def embed(text: str, concepts: dict[str, list[str]]) -> list[float]:
    ts = set(tokens(text))
    vector = []
    for words in concepts.values():
        hits = sum(1 for word in words if word in ts)
        vector.append(float(hits))
    length = math.sqrt(sum(value * value for value in vector))
    return [value / length for value in vector] if length else vector


def cosine(a: list[float], b: list[float]) -> float:
    return sum(x * y for x, y in zip(a, b))


def rank(query: str, documents: list[dict], concepts: dict[str, list[str]], mode: str) -> list[tuple[str, float]]:
    q_vec = embed(query, concepts)
    rows = []
    for doc in documents:
        lexical = lexical_score(query, doc["text"])
        semantic = cosine(q_vec, embed(doc["text"], concepts))
        if mode == "lexical":
            score = lexical
        elif mode == "vector":
            score = semantic
        elif mode == "hybrid":
            score = 0.35 * lexical + 0.65 * semantic
        else:
            raise ValueError(f"unknown mode: {mode}")
        rows.append((doc["id"], score))
    rows.sort(key=lambda item: (-item[1], item[0]))
    return rows


def metrics(mode: str, queries: list[dict], documents: list[dict], concepts: dict[str, list[str]], k: int = 3) -> dict:
    hit1 = 0
    recall = 0.0
    rr = 0.0
    details = []
    for case in queries:
        ranked = rank(case["query"], documents, concepts, mode)
        ids = [doc_id for doc_id, _ in ranked]
        relevant = set(case["relevant"])
        hit1 += int(bool(ids and ids[0] in relevant))
        recall += len(relevant & set(ids[:k])) / len(relevant)
        first_rank = next((i + 1 for i, doc_id in enumerate(ids) if doc_id in relevant), None)
        rr += 1.0 / first_rank if first_rank else 0.0
        details.append({"id": case["id"], "top3": ids[:3], "first_relevant_rank": first_rank})
    n = len(queries) or 1
    return {
        "hit_at_1": hit1 / n,
        f"recall_at_{k}": recall / n,
        "mrr": rr / n,
        "details": details,
    }


def self_test() -> None:
    docs = read_jsonl(BASE_DIR / "documents.jsonl")
    queries = read_jsonl(BASE_DIR / "queries.jsonl")
    concepts = json.loads((BASE_DIR / "concepts.json").read_text(encoding="utf-8"))
    lexical = metrics("lexical", queries, docs, concepts)
    vector = metrics("vector", queries, docs, concepts)
    hybrid = metrics("hybrid", queries, docs, concepts)
    assert vector["hit_at_1"] > lexical["hit_at_1"]
    assert hybrid["hit_at_1"] >= vector["hit_at_1"]
    assert hybrid["recall_at_3"] == 1.0
    print("retrieval-benchmark self-test: ok")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0

    docs = read_jsonl(BASE_DIR / "documents.jsonl")
    queries = read_jsonl(BASE_DIR / "queries.jsonl")
    concepts = json.loads((BASE_DIR / "concepts.json").read_text(encoding="utf-8"))
    result = {
        mode: metrics(mode, queries, docs, concepts)
        for mode in ("lexical", "vector", "hybrid")
    }
    result["note"] = "The vector mode is a toy semantic representation for learning, not a real embedding benchmark."
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
