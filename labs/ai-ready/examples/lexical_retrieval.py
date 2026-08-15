"""A tiny lexical retrieval baseline using TF-IDF style scoring.

No external packages are required.
Run:
    python3 lexical_retrieval.py
"""

from collections import Counter
import math
import re

DOCUMENTS = [
    {"id": "doc-1", "text": "Password reset can cause login failure when the session token is stale."},
    {"id": "doc-2", "text": "API rate limit errors return status 429 and should use exponential backoff."},
    {"id": "doc-3", "text": "Project deletion requires owner approval and an active change record."},
    {"id": "doc-4", "text": "Login issues after credential changes may require the user to start a new session."},
]


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def build_index(documents):
    doc_tokens = {doc["id"]: tokens(doc["text"]) for doc in documents}
    document_frequency = Counter()

    for terms in doc_tokens.values():
        document_frequency.update(set(terms))

    return doc_tokens, document_frequency


def search(query: str, top_k: int = 3):
    doc_tokens, df = build_index(DOCUMENTS)
    n_docs = len(DOCUMENTS)
    query_terms = tokens(query)
    results = []

    for doc in DOCUMENTS:
        counts = Counter(doc_tokens[doc["id"]])
        score = 0.0

        for term in query_terms:
            if counts[term] == 0:
                continue
            tf = 1 + math.log(counts[term])
            idf = math.log((n_docs + 1) / (df[term] + 1)) + 1
            score += tf * idf

        if score > 0:
            results.append((score, doc))

    return sorted(results, key=lambda item: item[0], reverse=True)[:top_k]


if __name__ == "__main__":
    queries = [
        "login failure after password reset",
        "429 rate limit",
        "delete project approval",
        "people cannot sign in after credentials changed",
    ]

    for query in queries:
        print(f"\nQUERY: {query}")
        matches = search(query)
        if not matches:
            print("  no lexical match")
            continue
        for score, doc in matches:
            print(f"  {score:.2f}  {doc['id']}  {doc['text']}")

    print("\nNotice the last query. A semantic retriever may help when wording changes too much.")
