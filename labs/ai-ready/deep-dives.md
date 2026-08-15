---
layout: default
title: "AI Ready — Deep Dives"
description: "A practical navigation map for AI architecture decisions, failure modes, controls, and hands-on labs."
permalink: /labs/ai-ready/deep-dives/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags: [ai, architecture, mcp, rag, agents, evals, security]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/ai-ready/">AI Ready</a></li><li aria-current="page">Deep Dives</li></ol>
</nav>

# AI Ready: Deep Dives

The overview tells you what exists. These pages are for architecture decisions. Each topic answers the same questions: what problem it solves, when to use it, when not to use it, what can fail, which controls matter, and how to test the design.

## Architecture pages

| Area | Main question | Page |
|---|---|---|
| System boundaries | What belongs to the model, application, data layer, or deterministic code? | [System Boundaries](/labs/ai-ready/system-boundaries/) |
| Data and RAG | How do we use fresh or private knowledge without turning search into magic? | [Data and RAG](/labs/ai-ready/data-rag/) |
| Tools and MCP | When is a direct tool enough, and when does MCP create real reuse? | [Tools and MCP](/labs/ai-ready/tools-mcp/) |
| Agent architecture | When should the system choose the next action instead of following a fixed workflow? | [Agent Architecture](/labs/ai-ready/agent-architecture/) |
| Evals | How do we know a model, prompt, retrieval change, or tool change is better? | [Evals and Reliability](/labs/ai-ready/evals-reliability/) |
| Security | How do we keep untrusted content away from permissions and sensitive actions? | [Security and Governance](/labs/ai-ready/security-governance/) |
| Production | How do we deploy, observe, version, and roll back an AI service? | [Build and Operate](/labs/ai-ready/build-operate/) |

## Three rules worth remembering

**Known next step → workflow.** If the process is stable, code the sequence and let the model handle only the uncertain parts.

**Fresh fact → retrieval or tool.** Do not ask model memory to act like a database.

**Risky write → application control.** The model can propose an action. Authorization, approval, validation, idempotency, and audit stay outside the model.

## Hands-on path

1. [SAP Diagnostics MCP](/mcp/sap-diagnostics-mcp/) — inspect a read-only tool boundary.
2. [RAG with Evals](/labs/ai-ready/labs/rag-evals/) — build retrieval and test it with a golden set.
3. [Agent with Approval](/labs/ai-ready/labs/agent-approval/) — investigate freely, write only through an approval gate.
4. [Production Readiness](/labs/ai-ready/labs/production-readiness/) — add traces, budgets, deployment gates, and rollback.

## Machine-readable layer

The human pages and the data layer should tell the same story:

- [Architecture catalog](/labs/ai-ready/data/catalog.json)
- [Architecture patterns](/labs/ai-ready/data/architecture-patterns.json)
- [Eval cases](/labs/ai-ready/data/eval-sample.jsonl)

The dataset is not decorative. New cases should come from real design mistakes, ambiguous choices, and failure paths.