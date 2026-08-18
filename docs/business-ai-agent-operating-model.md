# Business AI Multi-Agent Operating Model

Status: working technical contract  
Canonical source: `_data/labs/business_ai/agent_operating_model.yml`  
Machine context: `/ai/business-ai-agent-context.json`  
Updated: 2026-08-18

## Purpose

The Decision Lab uses specialised agents because research, evidence review, graph maintenance, decision analysis, and assessment design have different failure modes. One broad agent with write access would make those boundaries hard to test.

The operating model defines six roles: Research Scout, Case Curator, Evidence Challenger, Graph Steward, Lead Decision Analyst, and Assessment Builder. A role is a responsibility and a contract, not a separate runtime service.

GitHub Pages does not execute these agents. Local tools or external agent runtimes may load the same public context packs and portable skills.

## Core boundary

Agents may research, structure, challenge, analyse, and propose changes. They may prepare evidence up to `review_ready`. They cannot set their own work to `approved`.

Missing evidence stays a proof gap. Runtime proof is valid only when runtime activity was explicitly authorised and observed. Tool access does not grant business authority.

Canonical public source data is not writable by default. Normal repository review remains the publication boundary.

## Roles

### Research Scout

Finds public evidence candidates that address a strategic gap. It checks existing case and source IDs before proposing a new record. It does not create an approved case or graph edge.

### Case Curator

Turns a source-backed candidate into a structured case proposal. It resolves process, stage, pattern, technology, evidence, limitation, and proof-gap fields against canonical IDs. It may stop or reject a candidate when the source cannot support the requested detail.

### Evidence Challenger

Tests material claims, metrics, transferability, authority, counter-evidence, and alternative explanations. It can recommend `review_ready`, `needs_more_evidence`, or rejection. It cannot approve the record it challenged.

### Graph Steward

Separates structural graph defects from useful research gaps. It may propose a relationship for review only when evidence supports it. Graph density is not a quality target.

### Lead Decision Analyst

Builds a traceable decision record from the relevant process subgraph, SAP Enterprise context, controls, cases, metrics, negative evidence, and proof gaps. It separates deterministic rules from probabilistic assistance and treats authority as an explicit design dimension.

### Assessment Builder

Creates review-ready SAP Lead practice cases from existing SAP Enterprise and Business AI sources. It reuses the existing assessment state and scoring model rather than creating another topic database.

## Default hand-off

`Research Scout -> Case Curator -> Evidence Challenger -> Graph Steward -> Lead Decision Analyst -> Assessment Builder`

The sequence is not mandatory for every task. A graph defect can go directly to Graph Steward. A decision question can start with Lead Decision Analyst when the required evidence already exists.

Every hand-off carries the role names, output type, canonical IDs, source IDs, evidence level, proof gaps, review state, and required human action. A downstream role must not silently remove an upstream proof gap.

## Stop behaviour

An agent stops instead of guessing when a required source cannot be resolved, a canonical ID is unknown, a material claim is unsupported, or a high-impact authority boundary has no accountable owner.

A role may return `needs_more_evidence`, a structural defect, a duplicate candidate, or a human decision request. These are useful outcomes, not agent failures.

## Skill composition

The model reuses existing portable skills for evidence-driven troubleshooting, authority design, failure-mode review, decision facilitation, business-rule ownership, integration change review, graph modelling, and SAP Lead assessment.

Four new skills provide the missing Decision Lab-specific contracts:

- `business-ai-case-curator`;
- `business-ai-lead-decision-analyst`;
- `business-ai-graph-steward`;
- `business-ai-assessment-builder`.

Research Scout and Evidence Challenger are role compositions of existing skills, so the repository does not gain two redundant copies of evidence and research instructions.

## Machine context packs

`/ai/business-ai-agent-context.json` exposes one compact pack per role. Each pack includes mission, source routes, context-selection rules, skill composition, allowed outputs, review boundary, stop conditions, and hand-off targets. The endpoint also exposes canonical ID indexes and the current evidence/review policy.

The pack is a generated Jekyll view. `_data/labs/business_ai/agent_operating_model.yml` owns the role contract. The Business AI contract and datasets own business facts.

## Validation

Validation should fail when a role references an unknown skill, lacks a review boundary, has no stop condition, allows approval promotion, or exposes a missing canonical source route. The rendered context endpoint must match the current Business AI contract version and operating-model review date.

Portable skill validation remains `python3 agent-skills/exporters/validate_agent_skills.py`.
