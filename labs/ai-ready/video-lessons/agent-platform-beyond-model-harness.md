---
layout: default
title: "The Agent Was Fine. The Platform Failed."
description: "How to build reliable agent platforms with sandboxes, durable state, scheduling, tenancy and recovery for enterprise work."
permalink: /labs/ai-ready/video-lessons/agent-platform-beyond-model-harness/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, architecture, sap, evaluation]
career_impact: mapped
career_skills: [delivery-cicd, delivery-observability, ai-security]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# The Agent Was Fine. The Platform Failed.

The agent can read code, write a patch and run tests. Yet production work fails because its workspace disappears, its secret expires, two agents edit the same branch, or a burst of tasks overloads a shared service. The model may be doing exactly what it was asked to do. **The operating platform is not ready.**

Two November talks expose the boundary from different sides: Joey Wang (Harvey), [The Agents Were Fine. Everything Around Them Broke](https://aietalks.com/talks/the-agents-were-fine-everything-around-them-broke), and Akshat Bubna (Modal), [Don't Vibe Code Your Agent Infrastructure](https://aietalks.com/talks/dont-vibe-code-your-agent-infrastructure). Both are vendor perspectives; their architecture problems are general.

## Separate three layers

| Layer | Owns | Does not automatically own |
| --- | --- | --- |
| **Agent harness** | Model turns, tool choice, context, task state, stop logic | Durable secure machine, credentials, actual SAP state |
| **Execution environment** | Sandboxed compute, files, process isolation, network restrictions | Business authority and user approval |
| **Control plane** | Identity, jobs, scheduling, quotas, telemetry, deployments, audit | Semantic correctness of a business decision |

A persistent workspace **does not require** a continuously running machine. A platform can separate storage from transient compute. That design must still handle locks, stale state, shared files, credential scope and recovery after interruption.

Harvey describes a shared agent platform after many coding PRs: different agent clients, common cloud setup, CI follow-up loops and review controls. When actions became callable at scale, alert storms and task bursts needed deduplication and scheduling. Modal emphasizes that building the isolation, file persistence, scaling, network and observability infrastructure yourself creates a major ongoing engineering obligation.

## A safe enterprise architecture

~~~text
Authorized task request
   -> policy / scope / budget
   -> durable job and evidence record
   -> short-lived isolated workspace
   -> agent harness + approved tools
   -> test / validate / produce artifacts
   -> reviewer decision
   -> clean up workspace; retain governed evidence
~~~

For SAP work, the workspace should receive **synthetic data by default**. Production read access requires an approved adapter, minimal scope and auditable identity; production write access is separate and narrowly approved. Avoid putting a privileged SAP credential into a general-purpose sandbox environment.

## Four uncomfortable design questions

**Who owns the job after the model process crashes?** The durable job record and orchestrator, not the conversation alone.

**What if an agent runs the same task twice?** Use stable operation IDs and duplicate protection at the action boundary.

**What if ten agents use one repository?** Define branch/worktree isolation, ownership and merge gates. A common filesystem without coordination is not collaboration.

**How do we know it improved delivery?** Measure completed/accepted tasks, CI rework, review time, failures, resource use and cost. Agent output volume is not business value.

## 45-minute tabletop test

Simulate four incidents in a synthetic agent platform: a sandbox crash after an output file is written, a lost result after a downstream tool call, two agents editing one file, and an overloaded queue.

For each, write the **durable state**, what is safe to retry, who owns recovery and what trace is required. Compare building the environment yourself against managed execution. Add estimated maintenance cost and operational ownership, not just instance pricing.

**Architect question:** A self-hosted sandbox looks cheaper per hour than a managed platform. Which hidden costs could reverse your decision over 12 months?

Related: [Build and Operate](/labs/ai-ready/build-operate/) · [Safe Handoffs](/labs/ai-ready/video-lessons/safe-multi-agent-handoffs/) · [Security](/labs/ai-ready/security-governance/).

**Source boundary:** Harvey/Modal product experience is speaker-reported; all SAP restrictions, platform choices and failure drills are independent architecture exercises.

*Editorial status: working study material, pending human review; noindex. All SAP scenarios are synthetic.*
