---
layout: default
title: "From AI Coding to an Agentic SDLC: Who Owns the Release?"
description: "A practical architecture and leadership lesson on scaling coding agents through specifications, evidence, controls and delivery ownership."
permalink: /labs/ai-ready/video-lessons/agentic-sdlc-governance/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-11-11
hide_global_cta: true
tags: [ai, sdlc, software-factory, governance, release, leadership]
career_impact: mapped
career_skills: [delivery-cicd, lead-evidence, lead-team]
---

[AI Ready](/labs/ai-ready/) / [Video Lessons](/labs/ai-ready/video-lessons/)

# From AI Coding to an Agentic SDLC: Who Owns the Release?

*The bottleneck moves from writing code to deciding what can safely ship.*

**Source boundary:** Original analysis of themes in the confirmed [AI Native DevCon 2026 agenda](https://tessl.io/devcon): “From AI Coding to the Agentic SDLC: Booking.com's Journey Toward Autonomous Software Delivery” (Valerio Panzica), “1,000 Coding Agents, One Main” (Patrick Debois), “Minimize Review and Increase Trust: A Verification-Aware Process for Agentic Programming” (Fernanda Graciolli and Nada Amin), and “More Team Automation, Less Agent Autonomy” (Katharina Dzialets). **This is not a recap of the presentations or a claim that these organizations use the design below.**

## The change in economics

Imagine that an agent can prepare 50 code changes in a day. That sounds like a productivity win. But your team can safely review only five. You have not solved the delivery problem. You have moved the queue.

The right unit of productivity is **verified, useful change reaching its intended outcome**, not lines of code, number of PRs or agent-hours.

## The five ownership boundaries

| Boundary | Human or system owner | What the agent can contribute |
| --- | --- | --- |
| Business intent | Product owner / functional lead | Draft acceptance criteria and expose ambiguities |
| Design | Solution architect | Compare options, dependencies and risks |
| Implementation | Engineering owner | Generate bounded code changes and tests |
| Verification | CI + independent reviewer | Prepare fixtures, inspect failures, propose fixes |
| Release and operations | Release owner / support | Build release notes, monitor signals, prepare rollback |

These responsibilities can be delegated differently in different organizations, but **accountability must remain explicit**. “The agent did it” is not an ownership model.

## A change contract worth versioning

~~~yaml
change_id: SYN-VALIDATION-017
business_goal: "Reject missing mandatory mapping before upload"
owner: "data-migration-lead"
scope:
  allowed_paths: ["src/validator.py", "tests/test_validator.py"]
  forbidden: ["production-secrets", "deployment-config"]
acceptance:
  - "unknown mappings produce an explicit error"
  - "upload template columns remain unchanged"
  - "golden fixtures pass on the final commit"
review:
  required: true
release:
  mode: "manual"
  rollback: "revert commit and restore previous validator version"
~~~

This is a **sample contract**, not a supported schema of any vendor's coding agent. It becomes useful only when CI or policy software enforces the relevant rules.

## The PR is not the outcome

A successful pull request can still fail to improve the business process. Build a traceable chain:

~~~text
Business problem
  -> accepted requirement
  -> architecture decision
  -> change contract
  -> code + tests
  -> CI evidence on exact SHA
  -> approved release
  -> production observation
  -> business acceptance
~~~

The chain does not need a heavyweight graph database. A small manifest, stable identifiers and normal GitHub/CI artifacts may be enough. Add a graph when cross-repository traceability and dependency queries become too expensive otherwise.

## Measure the whole delivery system

A useful scorecard includes **lead time to accepted change**, change failure rate, time to restore service, review queue age, escaped defects, and the proportion of claims supported by exact test evidence.

Avoid using “number of AI-generated PRs” as the north-star metric. A hundred trivial PRs can consume more reviewer time than they save.

## 45-minute architect workshop

You lead an SAP-adjacent data migration team. The team introduces a coding agent for mapping scripts and validators. After two weeks, code throughput triples but UAT defect volume increases.

Do not immediately ban the agent or buy a stronger model. Ask: Which requirements are ambiguous? Which golden cases are missing? Did tests run on the final SHA? Who approves changes to mapping semantics? Which defects came from the agent, and which existed before?

Produce a **two-week correction plan**: freeze broad refactors, define a small change envelope, expand business regression fixtures, require exact-SHA evidence and review results before restoring autonomy.

**Lead interview question:** *“How would you scale AI-assisted engineering without turning your senior engineers into full-time reviewers?”* A strong answer will discuss task selection, automated checks, risk tiers, explicit ownership and meaningful outcome metrics.

**Related:** [Evidence-Backed PRs](/labs/ai-ready/video-lessons/evidence-backed-ai-prs/) · [Build and Operate](/labs/ai-ready/build-operate/) · [Agent Skills Supply Chain](/labs/ai-ready/video-lessons/agent-skills-supply-chain/).

*Editorial status: draft/noindex. All implementation contracts and SAP examples are synthetic.*
