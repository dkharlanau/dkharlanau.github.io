---
layout: default
title: "Fix Retrieval Before Buying a Smarter Model"
description: "Practical AI Engineer video lesson on RAG, multimodal retrieval, citations, evals; includes decisions, a synthetic SAP case, evaluation and implementation steps."
permalink: /labs/ai-ready/video-lessons/retrieval-before-model-upgrade/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-retrieval, ai-evaluation, ai-data-governance]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Fix Retrieval Before Buying a Smarter Model

An AI agent answers a question about a supplier contract. It produces a reasonable answer, but quotes conditions from **last year's version**. A larger model may make the answer sound better without finding the right document.

In [Better Search Took This AI Agent From 36% to 98% Accuracy](https://aietalks.com/talks/better-search-took-this-ai-agent-from-36-to-98-accuracy), Aamir Shakir (Mixedbread) argues that retrieval is often the bottleneck. He reports a customer's improvement from 36% to 98% after a change to its retrieval stack. This is a **speaker-reported vendor/customer result**, not a benchmark you should expect on SAP content.

## A retrieval pipeline loses information at each boundary

The familiar path looks simple:

~~~text
Document -> text extraction -> chunks -> embeddings -> vector search
         -> reranking -> evidence -> language model -> answer
~~~

But real documents include tables, scanned images, diagrams, superseded versions and layout-dependent meaning. OCR can remove the relationship between a caption and its table. Chunking can split a condition from its exception. An embedding may represent multiple important concepts in one vector.

Multimodal retrieval and **late interaction** are alternatives: richer document/page representations can preserve more visual and token-level evidence. They also introduce storage cost, ingestion choices and infrastructure complexity. They are not a universal replacement for exact lookup.

## Route each question to the right evidence access

| Question | Good first retrieval method | Reason |
| --- | --- | --- |
| What is the current value for customer X? | Authorized live SAP/API read | Search indexes may be stale |
| Does an integration error mention code ABC? | Exact/lexical search | Error codes must match exactly |
| Which runbook explains a family of route errors? | Semantic + lexical search | Wording varies |
| Which clause in a scanned contract governs payment terms? | Layout-aware / multimodal retrieval | Tables and page structure matter |
| Which procedure applied on a historic cutover date? | Versioned retrieval with effective dates | Latest document may be wrong |
| Which source-to-target mapping produced a field? | Structured mapping or lineage lookup | Relationships matter more than prose |

The hard part is **retrieval routing** and evidence preservation. Use a structured data tool for exact values; use semantic retrieval where meaning is uncertain; use a version filter where time changes the answer.

## The SAP master-data example

**Synthetic scenario:** The target system has a blank delivery-related field. Your knowledge assistant retrieves a guide saying the field must be filled for certain sales scenarios. That guide is *not* proof of the field's value, nor of which master-data change request updated it.

Separate three sources: policy ("when required"), observation ("what the system currently contains") and history ("what changed and when"). The answer should name each source and say what remains unverified.

A typed response helps:

~~~json
{
  "question": "Why is the value blank?",
  "rule_source": "rule/customer-shipping-v2",
  "observed_value": null,
  "observation_as_of": "2026-11-11T08:00:00Z",
  "replication_trace": null,
  "conclusion": "insufficient_evidence",
  "next_read": "authorized_target_snapshot"
}
~~~

This is an educational output contract, not a SAP API. Never let the model invent the missing observation.

## An experiment worth running

Build a **30-question golden set**: ten exact identifiers, ten semantic questions, five table/figure questions and five version-sensitive questions.

Test three candidates on the same corpus: lexical search, ordinary hybrid RAG, and layout-/multimodal-aware retrieval. Track **Hit@3**, evidence span correctness, answer correctness, stale version errors, median latency and total cost per correct answer. Review the actual citations manually for a subset.

The key diagnostic is not "which model scored highest?" Ask: "Was the evidence absent from the retrieved set, or did the model misread available evidence?" Those are different root causes and require different fixes.

**Architect challenge:** A supplier of retrieval software promises a 98% accuracy score. Which five questions would you ask before recommending it to a customer?

Related: [Data and RAG](/labs/ai-ready/data-rag/) · [Retrieval Benchmark](/labs/ai-ready/practice/retrieval-benchmark/) · [Speaker transcript](https://ainotes.us/summary/better-search-took-this-ai-agent-from-36-to-98-accuracy-aamir-shakir-mixedbread).

**Source boundary:** The headline improvement and retrieval architecture are speaker claims; all SAP examples and test targets are illustrative.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
