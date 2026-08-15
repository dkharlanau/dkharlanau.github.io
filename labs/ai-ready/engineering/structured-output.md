---
layout: default
title: "AI Ready — Structured Output"
description: "A practical guide to JSON schemas, validation, enums, identifiers, business checks, repair, and reliable model-to-software interfaces."
permalink: /labs/ai-ready/engineering/structured-output/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, structured-output, json, schema, validation, contracts]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/engineering/">Engineering</a></li><li aria-current="page">Structured Output</li></ol>
</nav>

# Structured Output

When software consumes model output, prose is not an interface. Use a schema, validate it, and keep business rules outside the model.

## Start from the consumer

Ask what the next component needs.

Example result:

```json
{
  "category": "bug",
  "priority": "high",
  "summary": "Login fails after password reset",
  "evidence_ids": ["msg-17", "log-22"],
  "needs_human_review": false
}
```

The schema should describe required fields, types, allowed values, limits, and null behavior.

## Schema-valid is not business-valid

A result can match JSON perfectly and still be wrong.

Validate in layers:

```text
parse
 -> schema validation
 -> identifier validation
 -> authorization/policy checks
 -> business preconditions
 -> use result
```

Examples:

- `priority` is a valid enum, but the user is not allowed to change it;
- `project_id` is a string, but the project does not exist;
- `amount` is numeric, but outside the allowed range;
- `evidence_ids` exist, but do not support the conclusion.

## Prefer enums over vague labels

Bad:

```json
{"status":"looks mostly okay"}
```

Better:

```json
{"status":"pass"}
```

with a known set such as `pass`, `fail`, `needs_review`, `insufficient_evidence`.

Stable enums are easier to test, route, and monitor.

## Separate data from explanation

One useful shape is:

```json
{
  "decision": "needs_review",
  "reason_code": "conflicting_sources",
  "evidence_ids": ["doc-a", "doc-b"],
  "explanation": "Two current sources disagree on the limit."
}
```

Software uses the deterministic fields. A person reads the explanation.

## Repair carefully

If output is malformed, you can retry or run a repair step for low-risk tasks. Do not silently repair high-impact tool arguments and then execute them.

Useful policy:

- syntax/schema error -> one bounded repair attempt;
- missing required business ID -> ask or stop;
- unauthorized value -> reject;
- ambiguous high-impact action -> require clarification or review.

## Structured output vs tool call

Structured output returns a typed decision or object to your application.

A tool call asks your application to invoke an external capability.

They often work together:

```text
model -> structured proposed action
application -> validates
application -> tool call
```

Do not treat “JSON that says delete_project” as authorization to delete a project.

## Decision card

**Use structured output when:** software must route, store, calculate, validate, or call another component from model output.

**Keep free text when:** the output is only a human explanation and no downstream contract needs it.

**Add deterministic validation when:** IDs, permissions, ranges, state transitions, money, access, or side effects matter.

## Runnable example

See [`structured_output_validation.py`](/labs/ai-ready/examples/structured_output_validation.py). It validates model-like JSON with standard Python only and then applies a separate business rule.

## Test cases

- valid response;
- invalid JSON;
- missing required field;
- unknown enum;
- wrong type;
- invented ID;
- schema-valid but forbidden action;
- conflicting evidence;
- null where the consumer does not allow null.

Next: [Embeddings and Vector Search](/labs/ai-ready/engineering/embeddings-vector-search/) · [Tools and MCP](/labs/ai-ready/tools-mcp/)
