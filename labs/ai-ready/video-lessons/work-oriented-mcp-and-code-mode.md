---
layout: default
title: "Stop Exposing Every API Method as an Agent Tool"
description: "Practical AI Engineer lesson on MCP design, code mode, tool composition, sandboxes. Source-based insights, SAP decisions and an exercise."
permalink: /labs/ai-ready/video-lessons/work-oriented-mcp-and-code-mode/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [ai-agents-mcp, ai-security, integration-ownership]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# Stop Exposing Every API Method as an Agent Tool

A SAP integration has twenty technical endpoints. It is tempting to expose all twenty to an LLM and ask it to assemble a customer-update workflow. The demonstration looks impressive; the first real user says only "fix this customer's address," and the agent builds a workflow that nobody can explain.

That is close to the failure described by Abhi Arya (Reducto) in [Why We Deleted Our MCP Server and Rebuilt It](https://aietalks.com/talks/why-we-deleted-our-mcp-server-and-rebuilt-it). A related talk by Mikyo King (Arize AI), [Stop Giving Your Agent Tools. Give It a Sandbox](https://aietalks.com/talks/stop-giving-your-agent-tools-give-it-a-sandbox), explores **code mode**: let the agent discover and compose tools in an isolated programming environment instead of placing huge tool menus and results into the prompt.

These two proposals complement each other, but they are **not identical**.

## Two engineering levers

| Lever | Solves | Doesn't solve |
| --- | --- | --- |
| **Task-oriented MCP** | The model sees domain workflows, state and validators rather than a raw endpoint catalog | Authorization, source truth and transaction semantics still belong to services |
| **Code mode + sandbox** | Dynamic tool discovery, sequential/parallel calls, filtering large outputs | Sandbox escape risk, secrets, resource budgets, unbounded external actions |
| **Plain direct API** | One stable operation with minimal orchestration | Complex multi-step business process without external coordination |
| **Deterministic workflow** | Known sequence, fixed validation and recovery | Adaptive exploration when next evidence is uncertain |

Reducto's redesign used fewer, more meaningful tools and a **state snapshot** tool so agents could inspect the pipeline rather than guess its current state. Code mode, in Arize's account, can cut token-heavy tool catalogs, but requires real isolation, permission controls and careful failure handling. Reported token/cost savings from one benchmark are not portable guarantees.

## SAP tool design: expose the job, not the transaction dump

Instead of twenty raw technical methods, consider these **conceptual** read-only tools:

~~~text
get_customer_consistency_snapshot(customer_ref)
  -> source and target values, observation times, missing evidence

explain_replication_status(business_object_ref)
  -> message IDs, processing states, owner, safe next checks

validate_order_readiness(order_ref)
  -> required inputs, documented gaps, no write operation
~~~

These are **design names, not released SAP APIs or transactions**. The real implementation may call approved OData APIs, integration-monitoring services or existing internal adapters. Its business contract must not imply that a successful message proves an updated customer record.

A task-oriented wrapper can turn five noisy low-level responses into one small, typed result. That is valuable even without an LLM. But do not hide critical errors in a generic "OK" result.

## When code mode is appropriate

Use an isolated code environment when the agent must transform large synthetic files, combine several read tools, extract field-level differences, or run deterministic validations. Keep the high-risk endpoints outside the agent's unrestricted code environment.

For example, a sandbox can compare two synthetic CSV exports and return only mismatched rows and counts. The agent need not read thousands of unchanged customers into its prompt.

A programming shell with broad credentials, filesystem access and unrestricted network egress is **not** safe merely because it is called a sandbox. Set file scopes, allowlisted destinations, time/memory budgets, separate identities, and full tool traces.

## 50-minute exercise: redesign a tool catalog

Take six synthetic operations: read source BP, read target BP, list message status, get trace, resend message, change field. Build a task-oriented interface for **diagnosis only**.

Then compare:
1. Six generic operations directly offered to an agent.
2. One read-only snapshot tool that composes four reads in deterministic code.
3. A sandbox script with only the four read functions.

Measure which produces the most accurate evidence, fewest model tokens, clear error states and smallest permission surface. **Do not add resend or change-field actions to the experimental agent.**

**Architect question:** When should a tool return a structured state snapshot rather than let the LLM query all underlying APIs individually?

Related: [Tools and MCP](/labs/ai-ready/tools-mcp/) · [Agent with Approval](/labs/ai-ready/labs/agent-approval/) · [Reducto transcript](https://aietalks.com/talks/why-we-deleted-our-mcp-server-and-rebuilt-it).

**Source boundary:** Tool redesign and sandbox benefits are speaker-reported. SAP tools and interface names above are synthetic architecture sketches.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
