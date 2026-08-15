---
layout: default
title: "AI Ready — Embeddings and Vector Search"
description: "A practical guide to embeddings, similarity search, vector databases, metadata filters, hybrid retrieval, and when exact search is better."
permalink: /labs/ai-ready/engineering/embeddings-vector-search/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, embeddings, vector-search, vector-database, retrieval, hybrid-search]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Embeddings and Vector Search</li></ol>
</nav>

# Embeddings and Vector Search

An embedding turns content into a numeric representation that can be compared by similarity. It is useful for semantic search. It is not a truth score and it does not replace normal database filters.

## The basic flow

```text
document -> embedding model -> vector
query    -> embedding model -> vector
                           -> similarity search
                           -> candidate documents
```

Similar meaning should produce nearby vectors. The exact behavior depends on the embedding model and the data.

## Start with lexical search

Before adding a vector database, test a simple lexical baseline.

Lexical search is often strong for:

- names;
- IDs;
- error codes;
- version strings;
- API routes;
- product codes;
- exact legal or policy terms.

Semantic search is often stronger for paraphrases:

```text
"people cannot sign in after reset"
```

may find:

```text
"password-reset login failure"
```

even when the wording differs.

## Vector database is storage plus search infrastructure

A vector database or vector-capable search engine commonly stores:

- vector;
- source/chunk ID;
- original or referenced text;
- metadata;
- access fields;
- timestamps/version fields.

Do not store only vectors. You still need provenance and filters.

## Metadata matters

Useful filters may include:

```text
tenant_id
project_id
language
status
valid_from
valid_to
security_class
source_type
version
```

Apply access and validity rules before or during retrieval, not after sensitive content is already placed in context.

## Hybrid search

Hybrid retrieval combines lexical and semantic signals.

Use it when eval cases show both needs:

```text
exact identifiers + natural-language paraphrases
```

Do not add hybrid search because the diagram looks more complete. Compare it with the lexical and vector baselines using the same questions.

## Similarity score is not confidence

A high similarity score means the vectors are close under that retrieval method. It does not prove:

- the source is correct;
- the source is current;
- the user may see it;
- the source supports the final claim.

Those controls live elsewhere.

## Chunking changes search behavior

Too-large chunks may contain many topics. Too-small chunks may lose the header or context that gives a sentence meaning.

Prefer semantic units such as:

- one procedure;
- one concept;
- one FAQ answer;
- one decision rule;
- one table with its header;
- one incident pattern.

Test chunking against retrieval evals rather than copying a fixed token number from a tutorial.

## Decision card

**Use lexical search when:** exact terms are strong signals.

**Use vector search when:** users describe the same concept with different wording.

**Use hybrid search when:** both methods solve different important eval cases.

**Do not use a vector database when:** a small exact dataset, SQL query, key-value lookup, or normal search already solves the task.

## Practice

Create ten short documents. Ask five exact-term questions and five paraphrase questions. Record which cases lexical search solves. Only then add semantic similarity and compare the delta.

See [`lexical_retrieval.py`](/labs/ai-ready/examples/lexical_retrieval.py) for a small baseline you can run with standard Python.

Next: [Data and RAG](/labs/ai-ready/data-rag/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/)
