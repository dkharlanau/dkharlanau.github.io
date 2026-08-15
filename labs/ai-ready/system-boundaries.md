---
layout: default
title: "AI Ready — System Boundaries"
description: "A practical guide to splitting responsibility between the model, deterministic code, data, tools, state, and human control."
permalink: /labs/ai-ready/system-boundaries/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, architecture, workflow, structured-output, state]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">System Boundaries</li></ol>
</nav>

# System Boundaries

A useful AI architecture starts by deciding what the model is allowed to decide. The common mistake is to put rules, permissions, calculations, memory, and process control into one large prompt. It works in a demo because the happy path is polite. Production is less polite.

## The split

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
    |-- synthesize evidence
    |-- propose next action
    |
Data / Tools
    |-- current facts
    |-- external actions
    |-- durable records
```

The model is strongest where the input is uncertain. Deterministic software is strongest where the rule is exact.

## Put this in the model

Use the model for tasks such as:

- understanding a free-text request;
- mapping a question to a known workflow or tool;
- extracting structured fields from messy text;
- comparing several pieces of evidence;
- explaining a result in useful language;
- choosing the next read when the path is not known in advance.

## Keep this outside the model

Use normal application logic for:

- authorization and role checks;
- exact calculations and thresholds;
- transaction commits and locks;
- durable application state;
- duplicate protection;
- mandatory process steps;
- secret handling;
- validation of tool input and output.

A prompt saying “never skip the approval check” is not the same as code that makes approval impossible to skip.

## State is not one thing

Do not call every stored value “memory”. Separate at least these layers:

| Layer | Example | Typical lifetime |
|---|---|---|
| Request context | Current question and retrieved evidence | One request |
| Conversation state | Previous turns and tool results | Session or thread |
| User preference | Preferred language or output format | Long-lived |
| Application record | Task, ticket, order, approval, incident | System of record |
| Cache | Tool catalog or retrieval result | Short-lived |
| Trace | Model/tool calls and timings | Operational retention period |

Each layer needs its own owner, retention rule, and access model.

## Structured output is a contract

If software consumes the result, return a schema rather than prose and hope. Validate required fields, enums, IDs, ranges, and null behavior outside the model.

Bad boundary:

```text
Model: “It looks like this account should be suspended.”
Application: suspends account.
```

Better boundary:

```text
Model -> {"recommendation":"suspend","reason_code":"policy_violation","confidence":0.78}
Application -> validates evidence, authorization, policy and approval requirement
Application -> executes or rejects
```

## Workflow or agent?

Use a workflow when the next steps are known. Use an agent loop when the next useful action depends on evidence found during the task.

Example: converting an approved form into a structured record is mostly a workflow. Investigating why a deployment failed may need adaptive reads across build logs, configuration, recent commits, service health, and dependency status.

## Failure modes

- Important rules exist only in prompts.
- The model owns transaction state.
- Tool results are trusted without schema validation.
- Conversation history is treated as a source of truth.
- The application sends every available document “just in case”.
- One agent has read and write access to everything.

## Architecture checklist

Before adding another model call, answer:

1. Is the input uncertain enough to need a model?
2. Can deterministic code solve this more safely?
3. Where does the current fact come from?
4. Who authorizes the action?
5. What state must survive this request?
6. What happens on retry or timeout?
7. How will we test the boundary?

Related: [Practical Use Cases](/labs/ai-ready/use-cases/) · [Data and RAG](/labs/ai-ready/data-rag/) · [Agent Architecture](/labs/ai-ready/agent-architecture/)
