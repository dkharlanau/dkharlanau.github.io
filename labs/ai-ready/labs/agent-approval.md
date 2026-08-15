---
layout: default
title: "AI Ready Lab — Agent with Approval"
description: "A hands-on lab for a bounded investigation agent that can read, prepare a change, and execute only after explicit approval."
permalink: /labs/ai-ready/labs/agent-approval/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, lab, agents, approval, tools, security]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/labs/ai-ready/">AI Ready</a></li><li><a href="/labs/ai-ready/deep-dives/">Deep Dives</a></li><li aria-current="page">Agent with Approval</li></ol>
</nav>

# Lab 03: Agent with Approval

Build an operations assistant that may investigate with read-only tools and prepare a change, but cannot execute a risky write without a separate approval state.

## Scenario

Use synthetic sales-order data. The user asks:

> Why is order 4711 blocked, and can we release it?

Possible causes include credit, delivery block, material status, ATP, or an integration problem.

## Tool set

Read tools:

```text
get_sales_order(order_id)
get_credit_status(order_id)
get_delivery_blocks(order_id)
get_atp_snapshot(order_id)
get_material_status(order_id)
get_integration_events(order_id)
```

Write path:

```text
prepare_block_removal(order_id, block_type, reason)
approve_change(change_id)
execute_approved_change(change_id, request_id)
```

Do not expose one generic `update_order` tool.

## Agent loop

```text
request
 -> choose read tool
 -> validate authorization
 -> run tool
 -> add evidence
 -> decide: another read / resolved / approval required / stop
```

Limits for the lab:

- maximum 8 tool calls;
- maximum 2 retries per transient failure;
- read-only allowlist during investigation;
- no write tool until a prepared change exists;
- explicit stop reason required.

## Prepared change

The model may propose:

```json
{
  "action": "remove_delivery_block",
  "order_id": "4711",
  "block_type": "Z1",
  "reason": "block no longer matches current policy",
  "evidence_ids": ["order:4711", "policy:block-z1:v3"],
  "expected_effect": "delivery processing may continue"
}
```

The application validates the proposal and creates a `change_id`. The user approves that exact change. Approval should expire and should include the current object version or another precondition.

## Execution

Execution receives only an approved change ID plus an idempotency/request ID. It checks:

- approval exists and is not expired;
- target object has not changed unexpectedly;
- requester and executor are allowed;
- action has not already been committed;
- backend result can be linked to the change record.

## Test cases

1. Root cause is found after one read.
2. Two causes are possible and another read is needed.
3. Credit data is forbidden for the user.
4. One tool times out and succeeds on retry.
5. Tool result contains prompt-injection text.
6. No evidence supports a safe conclusion.
7. Agent proposes a write without enough evidence.
8. User rejects approval.
9. Approval expires.
10. Same execution request is sent twice.
11. Order changes after approval but before execution.
12. Step budget is exhausted.

## Trace model

Each run should capture:

```text
trace_id
case/user identity
model + prompt version
tool call + sanitized args
authorization result
tool evidence IDs
agent decision
budget remaining
prepared change ID
approval event
execution result
stop reason
```

## Done when

The assistant can investigate several root causes, but there is no conversational trick that lets it bypass the application approval gate. Duplicate execution is safe, and every conclusion can be connected to evidence.

Read first: [Agent Architecture](/labs/ai-ready/agent-architecture/) · [Security and Governance](/labs/ai-ready/security-governance/) · [Tools and MCP](/labs/ai-ready/tools-mcp/)