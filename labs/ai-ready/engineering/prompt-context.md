---
layout: default
title: "AI Ready — Prompt and Context"
description: "A practical guide to instructions, examples, context selection, evidence packing, prompt boundaries, and prompt evaluation."
permalink: /labs/ai-ready/engineering/prompt-context/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, prompting, context, instructions, few-shot, context-engineering]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Prompt and Context</li></ol>
</nav>

# Prompt and Context

Prompt engineering is not writing a clever paragraph. It is designing the information boundary for one model call.

## Separate the layers

Keep these concerns distinct:

```text
system / application instructions
  -> stable role, safety, output rules

request instructions
  -> what this user wants now

context
  -> evidence, tool results, selected history

examples
  -> demonstrations of desired input/output behavior
```

Do not mix external documents into the same authority level as application instructions.

## Write instructions around decisions

Good instructions tell the model:

- the task;
- what evidence it may use;
- what to do when evidence is missing;
- required output shape;
- which actions are allowed or forbidden;
- when to stop or escalate.

Weak instruction:

```text
Be accurate and helpful.
```

Useful instruction:

```text
Answer only from the supplied evidence. If the evidence does not support the answer, return insufficient_evidence. Return JSON that matches the response schema.
```

## Context is a budget

A context window is not a database. More context can add noise, conflicting versions, irrelevant history, and cost.

Build context deliberately:

1. keep the user request;
2. retrieve or select relevant evidence;
3. preserve source boundaries;
4. remove duplicates;
5. prefer current versions;
6. include only needed history;
7. keep stable IDs for traceability.

## Examples are behavior tests in disguise

Few-shot examples can clarify formatting, edge cases, and decision boundaries. Keep them short and representative.

Include difficult examples, not only perfect happy paths:

- missing input;
- ambiguous request;
- unsupported answer;
- permission failure;
- conflicting evidence.

If one example becomes a hidden business rule, move that rule into deterministic code or policy.

## Context from tools and retrieval is untrusted

A webpage, file, email, database field, or tool result may contain hostile or irrelevant instructions. Treat it as data.

The application decides permissions and allowed actions. Retrieved content does not gain authority because it appears close to the model.

## Prompt versioning

A prompt change can change behavior without a code change. Store a prompt or instruction version in traces and eval runs.

Useful metadata:

```json
{
  "instruction_version": "research-07",
  "template_version": "answer-json-03",
  "context_builder_version": "context-11"
}
```

## Common failure modes

- One giant prompt contains policy, examples, data, and application state.
- The full chat history is always sent.
- Old and current evidence are mixed with no labels.
- Instructions say “never do X” but the tool layer still allows X.
- Prompt changes are shipped without the same regression cases.
- Important output requirements exist only as natural-language wishes.

## Decision card

**Use prompt changes for:** task clarity, output behavior, examples, tone, missing-evidence behavior.

**Use context changes for:** better evidence selection, less noise, better source boundaries.

**Do not use prompts for:** authorization, durable state, exact calculations, transaction safety, duplicate protection.

## Practice

Take one task such as “summarize a support incident”. Build three context versions:

- entire incident history;
- last five messages;
- selected evidence with IDs and timestamps.

Run the same eval questions against all three. Compare completeness, unsupported claims, latency, and cost.

Next: [Structured Output](/labs/ai-ready/engineering/structured-output/) · [System Boundaries](/labs/ai-ready/system-boundaries/)
