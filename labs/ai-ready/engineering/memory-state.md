---
layout: default
title: "AI Ready — Memory and State"
description: "A practical guide to request context, conversation history, user preferences, application state, caches, summaries, and durable memory design."
permalink: /labs/ai-ready/engineering/memory-state/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, memory, state, context, persistence, cache]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Memory and State</li></ol>
</nav>

# Memory and State

“Memory” is often used for several different things. Split them before designing persistence.

## Six useful layers

| Layer | Example | Typical lifetime |
|---|---|---|
| request context | current question and evidence | one request |
| conversation history | recent turns and tool results | one thread/session |
| conversation summary | compressed older context | thread/session |
| user preference | language, format, saved choice | long-lived |
| application state | task status, approval, workflow step | business/application lifetime |
| cache | repeated lookup or tool catalog | short TTL |

A seventh layer is the operational trace. It exists for debugging and audit, not for helping the model “remember”.

## Context is not persistence

If a fact matters after the request ends, store it outside the model context.

Bad design:

```text
The approval is somewhere in chat history, so the agent remembers it.
```

Better design:

```text
approval_record(change_id, approver, timestamp, expiry, precondition)
```

The model can read the record. It does not own the state transition.

## Conversation history needs selection

Sending the whole thread forever creates noise and cost. A practical strategy can be:

```text
recent turns
+ selected durable facts
+ summary of older discussion
+ current evidence
```

Keep raw history when policy or audit needs it, but do not assume every old message belongs in every model call.

## User memory should be explicit

Store a preference when it is stable and useful, for example:

```json
{
  "preferred_language": "English",
  "answer_style": "concise",
  "default_timezone": "Europe/Berlin"
}
```

Do not infer sensitive traits and persist them casually. Define what may be stored, why, for how long, and how the user can change or remove it.

## Semantic memory is retrieval

Some systems store past facts or notes as searchable entries and retrieve them later by meaning. Treat this as a retrieval system:

- stable IDs;
- source/author;
- creation and update time;
- permissions;
- confidence or verification state if relevant;
- deletion/retention rules.

A vector index of old conversations is not magically correct memory.

## State machine beats chat history

For workflows and agents, represent important process state explicitly:

```text
new
-> investigating
-> insufficient_evidence
-> prepared_change
-> awaiting_approval
-> approved
-> executed
-> failed
```

This is easier to test, recover, and audit than asking a model to infer the current state from prose.

## Decision card

**Use conversation context for:** recent interaction needed to understand this request.

**Use durable memory for:** explicit facts or preferences needed across sessions.

**Use application state for:** workflow steps, approvals, locks, execution status, transactions.

**Use retrieval for:** searching a larger collection of past knowledge or notes.

**Use cache for:** performance where staleness rules are clear.

## Failure modes

- Entire chat history is treated as source of truth.
- A preference and a business record share the same storage model.
- Old inferred facts never expire.
- Sensitive context is copied into long-lived memory without purpose.
- Agent state disappears after process restart.
- A cached fact has no freshness rule.

## Practice

Take a support assistant. List every value it may keep and place each into one of the layers above. If a value has no clear owner, lifetime, or delete rule, its storage design is unfinished.

Next: [Evals and Reliability](/labs/ai-ready/evals-reliability/) · [Security and Governance](/labs/ai-ready/security-governance/)
