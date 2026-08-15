---
layout: default
title: "AI Ready Lab — RAG with Evals"
description: "A hands-on lab for building a small retrieval system with metadata, hybrid search, citations, and regression evals."
permalink: /labs/ai-ready/labs/rag-evals/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, lab, rag, retrieval, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">RAG with Evals</li></ol>
</nav>

# Lab 02: RAG with Evals

Build a small retrieval system where every answer can be traced to source evidence. The point is not to collect vector-database screenshots. The point is to know why retrieval succeeded or failed.

## Scenario

Create a synthetic product-and-team knowledge corpus with 20–40 short documents. Example topics:

- authentication rules;
- deployment procedure;
- refund policy;
- API version migration;
- incident escalation;
- project naming rules;
- obsolete and current versions of the same policy.

Do not use private client or employer documents.

## Target architecture

```text
Markdown/JSON sources
   -> normalize
   -> metadata
   -> lexical index
   -> optional vector index
   -> retrieval
   -> optional rerank
   -> context builder
   -> model answer + source IDs
   -> eval runner
```

## Step 1: define source metadata

Minimum fields:

```json
{
  "source_id": "auth-policy-002",
  "title": "Authentication Token Policy",
  "domain": "platform",
  "version": "2.0",
  "valid_from": "2026-07-01",
  "status": "current",
  "security_class": "training-public"
}
```

Create one obsolete version on purpose. Retrieval must prefer the current source when the question is about current policy.

## Step 2: create the baseline

Start with lexical search. Test exact identifiers, terms, and phrases. Record the result before adding embeddings.

Questions should include exact and semantic wording:

- “Which rule covers `ERR_AUTH_403`?”
- “Why do users lose access after token refresh?”

If lexical search already works well, keep that evidence. Architecture is allowed to remain simple.

## Step 3: add semantic retrieval only for a measured gap

Add vector search when paraphrases or concept matching are weak. If both exact IDs and semantic language matter, compare hybrid retrieval against the lexical baseline.

Do not tune by intuition. Keep the same eval cases across variants.

## Step 4: build a golden set

Create at least 20 cases with:

```json
{
  "id": "rag-007",
  "question": "Which current rule applies to token refresh?",
  "expected_source_ids": ["auth-policy-002"],
  "forbidden_source_ids": ["auth-policy-001"],
  "expected_behavior": "answer_with_citation"
}
```

Include exact match, paraphrase, obsolete version, conflicting sources, missing answer, forbidden source, similar-but-wrong topic, and a question requiring two sources.

## Step 5: evaluate retrieval before generation

Check expected source in top K, wrong version rejection, forbidden-source rejection, no-answer behavior, and latency per retrieval stage.

Only after retrieval is acceptable should you judge answer quality.

## Step 6: generate with citations

Give the model selected evidence with stable source IDs. Require the answer to include supporting IDs or links. If evidence is not enough, return an explicit `insufficient_evidence` state.

## Step 7: break it deliberately

Change one thing at a time: chunk size, metadata filter, embedding model, top K, reranker, prompt, or model. Run the same eval set and record quality, latency, and cost.

## Done when

You can answer:

1. What is the lexical baseline?
2. Which cases need semantic retrieval?
3. Does hybrid search improve those cases?
4. Can obsolete or forbidden sources leak into answers?
5. What happens when no source supports the answer?
6. Can you explain a regression from the trace?

Read first: [Data and RAG](/labs/ai-ready/data-rag/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)
