---
layout: default
title: "AI Ready Practice — Retrieval Benchmark"
description: "Compare lexical, semantic-style vector, and hybrid retrieval on the same small query set."
permalink: /labs/ai-ready/practice/retrieval-benchmark/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, practice, retrieval, embeddings, vector-search, rag, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/practice/">Practice</a></li><li aria-current="page">Retrieval Benchmark</li></ol>
</nav>

# Retrieval Benchmark

Vector search is useful when meaning matters more than exact wording. It is not a ceremonial database that every AI project must acquire.

This project compares three retrievers against the same relevance labels:

- lexical overlap;
- a small deterministic semantic vector;
- hybrid scoring.

The semantic vector is deliberately a toy. It makes cosine similarity visible without an API key or a hidden embedding SDK.

## Run it

```bash
python3 labs/ai-ready/practice/retrieval-benchmark/retrieval_benchmark.py
python3 labs/ai-ready/practice/retrieval-benchmark/retrieval_benchmark.py --self-test
```

The query set includes vocabulary mismatch such as **“undo a bad rollout”** versus a document about rolling back a failed release.

Metrics include `hit@1`, `recall@3`, and MRR.

## Replace the toy layer

Keep the evaluation harness and replace only `embed()`:

```text
query
 -> embedding model
 -> vector
 -> cosine / vector database
 -> ranked document IDs
 -> same relevance metrics
```

That separation matters. If a real embedding model does not improve the cases that matter, the correct architectural response may be to keep lexical search.

## Experiments

1. remove semantic concepts and see which queries fail;
2. change hybrid weights;
3. add near-duplicate documents;
4. add metadata filtering before ranking;
5. replace the toy vectors with a real embedding service and record its version.

Related: [Embeddings and Vector Search](/labs/ai-ready/engineering/embeddings-vector-search/) · [RAG](/labs/ai-ready/data-rag/)
