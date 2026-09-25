---
layout: default
title: "AI Ready — System Boundaries"
description: "A practical guide to splitting responsibility between the model, deterministic code, data, tools, state, and human control."
permalink: /labs/ai-ready/system-boundaries/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
hide_global_cta: true
tags: [ai, architecture, workflow, structured-output, state]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">System Boundaries</li></ol>
</nav>

# System Boundaries

A useful AI architecture begins with a simple question: **what should the model decide, and what should the application decide?**

This boundary matters more than the size of the prompt. A model is good at interpreting language, comparing imperfect evidence, and choosing among uncertain options. Normal software is better at exact rules, permissions, calculations, transactions, and durable state. When we mix these responsibilities, a demo may still work, but the production system becomes difficult to test and control.

## Give uncertainty to the model, not authority

A practical split looks like this:

```text
User / Event
    |
Application boundary
    |-- identity and authorization
    |-- deterministic rules
    |-- state and transaction control
    |-- tool validation
    |
Model
    |-- interpret messy input
    |-- classify and extract
    |-- compare evidence
    |-- propose the next useful step
    |
Data / Tools
    |-- current facts
    |-- external actions
    |-- durable records
```

The model can answer questions such as “What does this request mean?”, “Which known workflow fits?”, or “Which source should we read next?”. It should not decide whether a user is allowed to change an account, whether a financial limit has been exceeded, or whether a transaction has already been committed.

A prompt that says *never skip approval* is useful guidance. It is not an approval control. If approval is mandatory, the application should make the write impossible until an approved state exists.

## Where the model earns its place

Models are most useful when the input is irregular but the intended outcome is still clear. A support request may describe the same incident in ten different ways. A document may contain the fields we need, but not in a fixed layout. Several sources may disagree and require a reasoned summary.

In those cases the model can interpret, extract, classify, compare, or explain. It can also choose the next **read** when an investigation cannot be planned completely in advance.

The surrounding application should keep the exact parts exact: authorization, thresholds, duplicate protection, secret handling, transaction state, mandatory process steps, and validation of tool inputs and outputs. This division is not about distrusting the model. It is about using each component for the kind of problem it handles best.

## State is more than chat history

AI systems often call every stored value “memory”. That makes architecture discussions unnecessarily vague. Different kinds of state have different owners and different retention rules.

| State | Example | Typical lifetime |
|---|---|---|
| Request context | Current question and retrieved evidence | One request |
| Conversation state | Previous turns and tool results | Session or thread |
| User preference | Preferred language or output format | Long-lived |
| Application record | Task, order, approval, incident | System of record |
| Cache | Tool catalog or recent read result | Short-lived |
| Trace | Model and tool calls, timings, decisions | Operational retention period |

Conversation state can help the model understand what happened earlier. It should not silently become the source of truth for an order, approval, ticket, or account state. Those facts belong in the system that owns them.

The same distinction helps with privacy. A value that is safe to use for one request may not be safe to retain in a long-lived trace. We should decide storage and access rules per state type rather than treating the whole model context as one bucket.

## Structured output connects reasoning to software

When another program consumes the model result, prose is usually the wrong contract. Ask for structured output and validate it outside the model.

A weak boundary is:

```text
Model: "This account should probably be suspended."
Application: suspends account.
```

A stronger boundary separates recommendation from execution:

```text
Model -> {
  "recommendation": "suspend",
  "reason_code": "policy_violation",
  "confidence": 0.78
}

Application -> validate evidence
            -> check authorization and policy
            -> require approval if needed
            -> execute or reject
```

The schema does not make the model correct. It makes the hand-off explicit. We can validate required fields, allowed values, identifiers, ranges, and missing data before anything downstream acts on the result.

## Workflow and agent are different control shapes

If the next steps are known, a workflow is usually easier to understand and test. Converting an approved form into a structured record, validating it, and saving it is mainly a workflow even if a model extracts the fields.

An agent loop becomes useful when the next sensible action depends on what we discover. Investigating a failed deployment is a good example: one log may point to configuration, a configuration check may point to a recent change, and the next read cannot be chosen reliably before the investigation starts.

The important boundary stays the same. The agent may choose among allowed reads, but permissions, budgets, write controls, and transaction state remain outside the model.

## A useful design test

Before adding another model call, we ask what uncertainty it removes. If the answer is “none — the rule is already known”, ordinary code is probably the better component. If the model is needed, we should still know where the fact comes from, who can authorize an action, what state must survive the request, and what happens when a tool times out or the same request is retried.

That is the practical meaning of an AI system boundary: the model handles ambiguity; the application preserves control.

## Further reading

- [OpenAI — A practical guide to building AI agents](https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/)
- [Anthropic — Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents)

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [Data and RAG](/labs/ai-ready/data-rag/) · [Agent Architecture](/labs/ai-ready/agent-architecture/)
