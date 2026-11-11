---
layout: default
title: "AI Engineer Video Lessons — Applied AI Systems, Not Just Demos"
description: "22 source-backed lessons from October–November 2026 on agent architecture, tools, data, RAG, graph engineering, costs, evaluations and operating AI in SAP environments."
permalink: /labs/ai-ready/video-lessons/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, video-learning, agents, sap, architecture, security, evaluation, tools]
career_impact: mapped
career_skills: [ai-agents-mcp, ai-security, ai-evaluation]
---

[AI Ready](/labs/ai-ready/) / Video Lessons

# AI Engineer: 22 Lessons to Build Better AI Systems

**From an interesting talk to a decision you can defend and an experiment you can run.**

*Curated from AI Engineer talks published in the 12 October–11 November 2026 window. Research cut-off: 11 November 2026.*

An LLM can write an impressive answer. The engineering work starts when that answer must use the right data, preserve state, handle tool failures, respect permissions, and deliver a business result. These lessons focus on **practical agent use, tooling, evaluation, documentation and enterprise process design**.

Each article is an original, B2-English interpretation of its source talk. It includes what the speaker reports, a practical explanation, a **synthetic SAP or engineering scenario**, a measurable exercise, and a question an architect should be able to defend. The articles are not transcripts and do not claim independent verification of vendor performance.

## Want to build something now?

Start with [**Tool Selection Playbook**](/labs/ai-ready/video-lessons/tool-selection-playbook/). It compares LangGraph, Phoenix, Braintrust, DSPy/GEPA, Neo4j GraphRAG, LiteLLM, vLLM, Standard Agents and reusable source-owned data tools. It includes three bounded experiments with cost, quality and risk decisions.

A [dependency-free evaluation example](https://github.com/dkharlanau/dkharlanau.github.io/tree/main/labs/ai-ready/video-lessons/examples) shows how to score 12 synthetic SAP diagnostic outcomes. No production access is required.

## 1. Agent architecture and safe execution

| Learn | The engineering decision |
| --- | --- |
| [**Standard Agents: Small Specialists, One Controlled System**](/labs/ai-ready/standard-agents/) | Can an agent be a portable specialist, and what must the runtime enforce? |
| [**We Built Ten Agents. Then We Went Back to One**](/labs/ai-ready/video-lessons/agent-harness-rebuild/) | When does orchestration add more complexity than value? |
| [**Your Subagents Are a Distributed System**](/labs/ai-ready/video-lessons/safe-multi-agent-handoffs/) | What if a worker times out after a write actually succeeded? |
| [**Your AI Agent Used a Token. Who Actually Did the Work?**](/labs/ai-ready/video-lessons/agent-identity-delegation/) | Who requested the action, who executed it and who authorized it? |
| [**A Skill File Is Not a Security Review**](/labs/ai-ready/video-lessons/agent-skills-supply-chain/) | What is the complete executable supply chain behind one instruction file? |
| [**AI On-Call for SAP AMS**](/labs/ai-ready/video-lessons/ai-oncall-sap-ams/) | How can an agent earn higher autonomy without uncontrolled production actions? |
| [**Your Self-Hosted LLM Must Learn to Say No**](/labs/ai-ready/video-lessons/llm-admission-control/) | When should the inference service admit, defer or reject an agent request? |
| [**Not Every Agent Decision Needs a Language Model**](/labs/ai-ready/video-lessons/decision-models-before-llms/) | When do deterministic rules or narrow classifiers beat another LLM call? |

## 2. Knowledge, retrieval, graphs and business data

| Learn | The engineering decision |
| --- | --- |
| [**Documentation for Humans and Agents**](/labs/ai-ready/video-lessons/agent-first-documentation/) | How do short, useful docs serve people and retrieval without drifting? |
| [**Fix Retrieval Before Buying a Smarter Model**](/labs/ai-ready/video-lessons/retrieval-before-model-upgrade/) | Is the problem missing evidence or poor model reasoning? |
| [**Three Graphs Behind a Dependable Agent**](/labs/ai-ready/video-lessons/graph-engineering-execution-context/) | When should we model execution, context or procedure as a graph? |
| [**One Changed Cell, One Defensible Decision**](/labs/ai-ready/video-lessons/evidence-for-every-data-cell/) | Can an AI explain a mass-data correction without applying it? |
| [**Let Rules Prove Facts, AI Review Context, Humans Own Risk**](/labs/ai-ready/video-lessons/hybrid-ai-review-for-data-changes/) | Which data PR changes can safely pass without another human reviewer? |
| [**AI Can Translate Code. Can It Preserve the Business Process?**](/labs/ai-ready/video-lessons/graph-first-legacy-modernization/) | What dependencies and parity tests are needed before legacy modernization? |

## 3. Measure and improve the whole agent

| Learn | The engineering decision |
| --- | --- |
| [**A Cheap Model Can Still Run an Expensive Agent**](/labs/ai-ready/video-lessons/agent-caching-task-economics/) | Are we measuring tokens per call or cost per accepted business result? |
| [**Your Old Prompts May Be Slowing Down New Models**](/labs/ai-ready/video-lessons/modern-prompts-and-eval-hillclimbing/) | How do we remove prompt debt without overfitting an eval set? |
| [**How Do You Evaluate an Answer with No Single Right Answer?**](/labs/ai-ready/video-lessons/evaluating-answers-with-no-ground-truth/) | How do experts calibrate an LLM judge before trusting its scores? |
| [**Can an Agent Improve Itself Without Breaking Production?**](/labs/ai-ready/video-lessons/self-improving-agents-eval-gates/) | What stops a self-improvement loop from learning the wrong lesson? |

## 4. Engineering productivity and real adoption

| Learn | The engineering decision |
| --- | --- |
| [**Your PR Says Tests Passed. Show the Evidence.**](/labs/ai-ready/video-lessons/evidence-backed-ai-prs/) | What proof supports each generated change and its exact commit? |
| [**The Agent Was Fine. The Platform Failed.**](/labs/ai-ready/video-lessons/agent-platform-beyond-model-harness/) | Who owns sandboxes, durable state, quotas and recovery? |
| [**Stop Exposing Every API Method as an Agent Tool**](/labs/ai-ready/video-lessons/work-oriented-mcp-and-code-mode/) | Should an agent discover raw methods or use task-oriented tools and bounded code mode? |
| [**The Code Is Correct. Is It the Right Change?**](/labs/ai-ready/video-lessons/product-intent-for-coding-agents/) | How do agents preserve product intent, decisions and historical lessons? |
| [**One Consultant Gets Faster. Why Does the Team Still Work the Same?**](/labs/ai-ready/video-lessons/scaling-ai-beyond-the-power-user/) | How do AI practices improve end-to-end business flow, not only individual productivity? |

**Count note:** The original Standard Agents guide is a prerequisite, not one of the 22 video-lesson pages above. The page catalog contains **22 new and previously prepared video lessons** (7 architecture + 6 data + 4 evaluation + 5 engineering/product), plus the Standard Agents prerequisite and a separate Tool Selection Playbook.

## A four-week practice path

**Week 1 — Prove the architecture.** Compare one agent and several specialists for a synthetic SAP incident. Model the tool scope, identity, stop states, and retry after an unknown outcome. Deliver an architecture decision record.

**Week 2 — Give the agent the right evidence.** Take a public technical page and build a ten-question retrieval test. Compare lexical retrieval to a documented alternative. Build six source-backed dependency edges. Deliver a small evidence register.

**Week 3 — Improve without gaming the test.** Use the provided [12-case synthetic evaluation](https://github.com/dkharlanau/dkharlanau.github.io/tree/main/labs/ai-ready/video-lessons/examples). Add one unseen case, one tool-failure case and an unsafe-write case. Evaluate baseline vs candidate. Measure quality, cost and actual accepted cases.

**Week 4 — Production and leadership.** Propose a read-only SAP support pilot, a PR evidence gate, a limited execution platform and an approval model. Measure whether the process becomes faster **end to end**, not whether the agent emits more text.

The schedule is an optional learning plan, not a course completion claim or a certification.

## Practical lab: run the synthetic evaluator

From a checkout of the website repository:

~~~bash
python3 labs/ai-ready/video-lessons/examples/agent-eval.py
python3 labs/ai-ready/video-lessons/examples/agent-eval.py --json
python3 labs/ai-ready/video-lessons/examples/agent-eval.py --gate
~~~

The JSON fixture contains curated baseline and candidate outputs, **not real model results**. The evaluator checks expected status, required evidence, and unauthorized writes. The gate requires at least 90% accepted synthetic cases and zero unsafe candidate writes. Use it as a transparent starting contract, then replace illustrative outputs with observations from a real approved test harness.

A good result is not a perfect number on a toy dataset. It is an evaluation method that catches a regression before an agent gets access to a consequential operation.

## Capstone: a defensible SAP Solution Architect answer

**Simulated customer requirement:** “Build AI to diagnose customer-data replication problems, find the cause and correct them automatically.”

Before recommending technology, give five deliverables:

1. A job charter with business outcome, process owner, data sources and the cost of a wrong change.
2. Workflow vs one agent vs specialists, with measurable reasons to choose one.
3. Authorization, source evidence, step limits, unknown outcomes, duplicate protection and an approval boundary.
4. A golden set covering data differences, configuration gaps, stale evidence, timeout, injection and protected records.
5. Operating metrics: accepted diagnoses, time to evidence, correction rate, cost, incidents, reviewer effort and recovery ownership.

**Defend the trade-off in B2 English:** “I would start with a read-only diagnostic workflow. If evidence gathering needs adaptive decisions, I would add a bounded agent. I would consider specialists only when independent permissions or domain ownership justify their coordination cost. Any production write would remain behind a separately authorized and auditable path.”

## Editorial and source checks

This is a selective **October–November 2026 research archive** drawn from recent AI Engineer recordings and accompanying transcripts. It is not a complete list of the channel's uploads. Links to the speaker's talk or transcript live in every lesson.

Reported percentages, benchmark improvements and customer results remain **speaker claims** unless independent evidence is identified. Synthetic SAP exercises are clearly separated from supported product functionality, and precise API details should always be checked against the current product and deployment model.

All new pages are **draft, unverified, noindex** pending human editorial review. The goal is to teach better architecture decisions, not to convert conference marketing into established facts.

**Next:** [Tool Selection Playbook](/labs/ai-ready/video-lessons/tool-selection-playbook/) · [AI Ready Deep Dives](/labs/ai-ready/deep-dives/) · [Business AI](/labs/business-ai/) · [Agent Architecture](/labs/ai-ready/agent-architecture/).
