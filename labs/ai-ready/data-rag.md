---
layout: default
title: "AI Ready — Data and RAG"
description: "A practical architecture guide for retrieval, metadata, chunking, hybrid search, reranking, grounding, and retrieval evaluation."
permalink: /labs/ai-ready/data-rag/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, rag, retrieval, embeddings, data, evals]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Data and RAG</li></ol>
</nav>

# Data and RAG

RAG is not “put documents in a vector database”. It is a controlled way to find evidence at request time and give the model only the useful parts. The architecture begins with source ownership and permissions, not embeddings.

## Start from the fact

For every important answer, define:

- source system or document;
- business owner;
- effective date or version;
- access classification;
- stable source ID;
- how the fact becomes stale;
- how the user can trace the answer back to it.

If nobody knows which document owns the policy, a better embedding model will not settle the argument.

## Retrieval pipeline

```text
Question
  -> normalize / classify
  -> permission and metadata filters
  -> candidate retrieval
       lexical search
       vector search
       or both
  -> rerank
  -> context selection
  -> answer with source references
  -> eval + trace
```

Do not add every step by default. Start simple and add complexity only when an eval shows a real gap.

## Lexical, vector, or hybrid?

**Lexical search** is strong for exact terms: material numbers, error codes, table names, document types, legal phrases, transaction codes, and product names.

**Vector search** helps when the wording changes but the meaning is similar.

**Hybrid search** is useful when both exact enterprise identifiers and semantic language matter. SAP support is a good example: `VL02N`, an IDoc message type, and “delivery cannot be changed” should not compete under one matching method.

## Chunking is a content decision

Do not select a chunk size because a tutorial used it. Split content around useful meaning:

- one procedure step group;
- one configuration concept;
- one business rule;
- one error pattern and resolution;
- one table section with its header;
- one process branch.

Keep metadata beside the chunk. Useful fields often include domain, process, system/version, object, language, validity date, security class, source URL, and parent document.

## Reranking and context selection

Retrieval finds candidates. Reranking decides which candidates deserve the limited context budget. The final context builder should also remove duplicates, preserve source boundaries, and avoid mixing conflicting versions without telling the model.

A large context is not automatically a better context. Too much irrelevant evidence makes the answer harder to control and more expensive to test.

## Permissions follow the source

Do not create a vector index that quietly removes source permissions. A user who cannot read a document in the source system should not gain access because an embedding was stored elsewhere.

Think about four separate controls:

1. May this content be indexed?
2. May this user retrieve it?
3. May it be sent to the selected model/runtime?
4. May the answer expose the retrieved field?

## Retrieval evals

Measure retrieval separately from answer quality. Useful checks include:

- expected source appears in top K;
- forbidden source never appears;
- correct version wins over obsolete version;
- exact identifiers remain searchable;
- no-answer cases stay no-answer cases;
- citations point to evidence that supports the claim.

Then measure the final answer: factual support, completeness, unsafe guessing, citation quality, latency, and cost.

## SAP logistics example

Question: “Why was route ZEU2 selected for this sales order?”

A useful retrieval design may combine:

- current route determination documentation;
- configuration explanation for shipping conditions, transportation group, departure zone, destination zone;
- project-specific mapping rules;
- the actual order and master-data values through read tools.

Documentation explains the rule. Tools provide the current transactional facts. Mixing those two sources without labels is how a confident explanation becomes fiction with good typography.

## Failure modes

- Vector search is used for exact IDs and performs badly.
- Old and new policy versions are retrieved together without version metadata.
- Chunk text loses the table header that gave it meaning.
- Access rules exist in the UI but not in retrieval.
- The model answers when retrieval found no evidence.
- The team evaluates only final prose and never tests retrieval itself.

## Build checklist

- Define sources of truth.
- Classify data before indexing.
- Keep stable source IDs and provenance.
- Build lexical baseline first.
- Add vector/hybrid only against an eval gap.
- Test stale, conflicting, forbidden, and missing evidence.
- Trace query, filters, retrieved IDs, scores, reranking, and final citations.

Related: [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Security and Governance](/labs/ai-ready/security-governance/) · [RAG with Evals Lab](/labs/ai-ready/labs/rag-evals/)