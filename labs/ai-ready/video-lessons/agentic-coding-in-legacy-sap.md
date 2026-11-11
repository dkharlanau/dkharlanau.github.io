---
layout: default
title: "AI Coding in Legacy Systems: Small Changes, Strong Evidence"
description: "A practical approach to agentic coding in mature SAP-adjacent repositories, inspired by AI Native DevCon's legacy-code and deterministic-agent sessions."
permalink: /labs/ai-ready/video-lessons/agentic-coding-in-legacy-sap/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, coding-agents, legacy-code, refactoring, sap, testing]
career_impact: mapped
career_skills: [delivery-testing, delivery-cicd, integration-development]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# AI Coding in Legacy Systems: Small Changes, Strong Evidence

*When AI makes code cheap, verification becomes the scarce resource.*

**Source boundary:** Original applied article informed by the confirmed [AI Native DevCon 2026 agenda](https://tessl.io/devcon), including “AI in Legacy Code: Small Steps, Deterministic Tools, Reusable Context” (Llewellyn Falco), “Stop Context Drift: Building Software with Deterministic Agents” (Tsvetan Tsvetanov), and “Building When Code is Cheap and Your Time is Not” (Aidan Cunniffe). This is **not** a claim to have watched these talks or a quotation of their content.

## The wrong way to modernize a mature system

A team asks a coding agent to “refactor all our migration validations and make them clean.” The agent rewrites 20 modules, improves naming, removes old branches and produces a polished PR. But one branch encoded a country-specific exception. No test covered it. The code looks better and the migration result is wrong.

The problem was not the model's ability to write code. It was an **undefined behavioral contract**.

## Start from a change envelope

Before the agent touches the repository, define:

| Boundary | What to specify | Example |
| --- | --- | --- |
| **Business invariant** | What must remain unchanged | Same input yields same mapping and error classification |
| **Allowed files** | Where the agent may edit | One validator module and its tests |
| **Forbidden changes** | What must not be altered | Production credentials, upload templates, release workflow |
| **Evidence** | What proves the change | Golden fixtures, schema comparison, test run on final commit |
| **Fallback** | How to stop and recover | Abort if unknown branch or missing mapping appears |
| **Reviewer** | Who owns correctness | Data migration functional lead + code reviewer |

This is a *change envelope*: a small, explicit boundary around a risky change.

## Example: a migration validator

The source and target files use different column names. The validator applies a mapping, checks required values and produces an update file. The agent is asked to optimize performance.

The **invariants** are more important than the code style:

- The output has the exact original upload-template columns, order and data types.
- Identical source inputs and mapping versions produce equivalent outputs.
- Unknown mappings are reported, not guessed.
- Only changed values are flagged; insert/update/delete classification is stable.
- Invalid rows are rejected with reproducible evidence.
- Existing special-case rules are preserved unless explicitly approved.

For a deterministic validation pipeline, an LLM is useful for explaining failures and proposing code, but **should not be the authority for field equality, output schema or arithmetic**.

## A good coding-agent loop

~~~text
Read repository contract
  -> inspect relevant code and tests
  -> reproduce current behavior
  -> write a minimal failing test
  -> implement one bounded change
  -> run targeted tests
  -> run integration/regression tests
  -> inspect diff and generated artifacts
  -> record exact commit and checks
  -> request review
~~~

The loop is intentionally unglamorous. It works because each stage leaves inspectable evidence. When the agent is uncertain about a legacy rule, it should preserve the rule and raise a question, not silently simplify it.

## Three useful agent roles

A small team can separate **research**, **implementation** and **review**, but do not assume three agents are always better. Independent review is valuable only when the reviewer checks **the actual diff, tests and business contract**, not when it repeats the implementer's explanation.

| Role | Deliverable | Not allowed |
| --- | --- | --- |
| Analyst | Current behavior, unknowns, change envelope | Modify production code |
| Implementer | Narrow diff and tests | Change business requirements |
| Reviewer | Evidence-backed findings and remaining risk | Declare tests passed without run evidence |

A single coding agent with deterministic CI may outperform a three-agent workflow. Compare both on representative tasks.

## A 60-minute practical exercise

Use a **synthetic** Python mapping validator. Create 12 fixture rows with four normal mappings, two unknown mappings, two duplicate identifiers, two blank required values and two legitimate no-op updates. Ask an agent to add a new source column while preserving the output template.

Make it run tests on the final commit and produce a PR evidence table: requirement, code change, test, result, SHA, remaining risk. Deliberately change a source column after the first test and see whether the agent recognizes the stale proof.

**Architect challenge:** Your agent rewrites a validator in half an hour instead of two days. The code is cleaner, but the regression set covers only 60% of business scenarios. Is this a successful delivery? Explain the release gate and what evidence is still missing.

**Related:** [Evidence-Backed PRs](/labs/ai-ready/video-lessons/evidence-backed-ai-prs/) · [Coding Agents Playbook](/labs/ai-ready/coding-agents/) · [Evals and Reliability](/labs/ai-ready/evals-reliability/).

*Editorial status: draft/noindex. All examples are synthetic and do not assert SAP release-specific behavior.*
