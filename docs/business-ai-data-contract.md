---
layout: default
title: "Business AI Data and Graph Contract"
description: "Canonical technical contract for Business AI graph entities, relationships, evidence fields, review state, machine outputs, and SAP Enterprise context links."
permalink: /docs/strategy/business-ai-data-contract/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-18
hide_global_cta: true
tags:
  - business-ai
  - knowledge-graph
  - data-contract
  - machine-readable
---

# Business AI Data and Graph Contract

Status: canonical technical contract  
Roadmap: #315, #316, #317, #318  
Canonical machine definition: `_data/labs/business_ai/contract.yml`  
Current contract version: `1.1.0`  
Updated: 2026-08-18

## Purpose

Business AI has cases, processes, scenarios, technologies, decision profiles, controls, evidence, and SAP Enterprise context. This contract gives those sources one stable agreement for IDs, entity types, relationships, evidence fields, review state, and generated views.

The YAML contract is the source of truth for these rules. This document explains how to use it. Do not copy its vocabularies into a second schema file.

## Source and output boundary

Canonical content stays under `_data/labs/business_ai/`. The contract maps each dataset to a role rather than replacing those datasets with a new database.

The files under `labs/business-ai/data/*.json` and `machine/business-ai/*.json` are Jekyll-rendered machine views. They are outputs over canonical YAML sources. Change the YAML source or the rendering template, not a rendered JSON result.

`_data/labs/business_ai/enterprise_context_links.yml` is the canonical cross-product map between vendor-neutral Business AI processes and existing SAP Enterprise source pages. It links context. It does not copy SAP configuration content into Business AI.

## Stable identity

Entity and relationship IDs use lowercase kebab-case. IDs are public identity, not display text.

A title may change without changing its ID. Retired IDs are not reused. Cross-dataset references use IDs instead of titles when a stable ID exists.

A breaking ID change, required-field removal, or controlled-vocabulary removal requires a major contract version. Additive optional fields and new relationship types may use a minor version.

Generated graph nodes use type prefixes such as `process-`, `case-`, `pattern-`, and `evidence-` so IDs stay unique across entity types. Generated edge IDs are deterministic from their relationship and endpoint identities.

## Controlled vocabularies

The contract owns shared values that cross datasets:

- case kind;
- evidence grade;
- source confidence;
- review state;
- autonomy level;
- outcome state;
- evidence level.

The contract reuses current Business AI semantics where they already exist. Evidence grades remain A/B/C/D from the catalog. Autonomy remains L0-L5 from the assessment matrix. Case kind, review state, outcome state, source confidence, and evidence level are shared contract fields for normalized graph records and later case-review work.

The review-state vocabulary is defined now because graph and agent outputs need a stable field. The allowed transition lifecycle and human review rules are developed in roadmap issue #320.

## Evidence levels

Evidence level and evidence grade answer different questions.

**Evidence level** describes what kind of statement is being made:

- `source_fact` is directly visible in a source, configuration, log, test, scanner result, or provided material;
- `supported_inference` is a reasonable conclusion from available facts;
- `runtime_proof` is observed runtime evidence and is valid only when the activity was approved and observed;
- `unsupported_claim` goes beyond available evidence;
- `proof_gap` marks something that still needs evidence or review.

**Evidence grade** describes the strength of public result evidence already used by the Business AI catalog. A high grade does not turn an inference into runtime proof.

When an older canonical record does not yet contain a new contract field, a generated projection may use a conservative default only when it also publishes a `projection_flags` gap. A projection never changes the canonical source and never promotes evidence to `approved`.

## Graph contract

The contract uses the existing Business AI graph model. It defines typed entities such as process, process stage, pattern, platform, case, outcome, failure, decision profile, metric, evidence source, control, limitation, and Enterprise Context page.

Relationships are typed and directional. A relationship is valid only when both referenced nodes exist and their entity types match the relationship definition. This allows CI to reject a graph that looks syntactically correct but connects the wrong concepts.

Granularity matters. `process_map.yml` currently lists patterns and controls at process level, so the generated graph uses `process-uses-pattern` and `process-has-control`. It does not invent a pattern or control relationship for every stage. Stage-level links are emitted only when a canonical source names that stage relationship, such as SAP Enterprise context mappings.

## SAP Enterprise context

Business AI processes remain vendor neutral. SAP-specific implementation context is represented by `EnterpriseContextPage` nodes linked with `process-has-enterprise-context` and `stage-has-enterprise-context`.

The first map covers Lead-to-Cash / Order-to-Cash, Source-to-Pay, inventory and fulfilment, master-data change, and integration incident resolution. Each process mapping records data dependencies, integration boundaries, authority boundaries, control boundaries, business-rule areas, and key decision points.

Other ERP products can attach their own implementation-context nodes to the same Business AI process IDs. They must not reuse SAP-specific routes or imply that a vendor-neutral process concept belongs to SAP.

## Machine artifacts

The Machine layer exposes:

- `/machine/business-ai/manifest.json` for version, source revisions, counts, views, and quality policy;
- `/machine/business-ai/graph.json` for the full typed graph projection;
- `/machine/business-ai/views/process-context.json` for process and SAP Enterprise boundary analysis;
- `/machine/business-ai/views/case-evidence.json` for cases, reported metrics, evidence, limitations, review state, and proof gaps;
- `/machine/business-ai/` as the human-readable technical entry point.

These are generated projections. They are not a second source of truth and do not require a hosted graph database.

## Consumers

Jekyll reads canonical YAML and renders human and machine views. Machine artifacts preserve stable IDs and declare their contract version. Agents consume the same contract plus generated context packs. Analysis views consume the graph and coverage outputs.

Agents may propose new records or relationships. They do not promote their own evidence to an approved state when human review is required.

## Validation

`scripts/check_business_ai_contract.py` validates the canonical contract, graph type rules, stable IDs, controlled vocabularies, and source alignment.

`scripts/check_business_ai_graph_quality.py` adds graph and evidence quality rules. Structural failures are blocking: duplicate IDs, broken process or stage references, invalid graph edges, missing priority SAP links, missing enterprise boundaries, and broken SAP source routes. Coverage and evidence findings are advisory gaps: missing explicit review state, weak case-to-process coverage, missing stage coverage, unconnected secondary graph concepts, stale evidence, and similar research work.

The quality checker produces stable rule IDs and a JSON report. CI runs it after the Jekyll build so it validates the actual generated graph, not only the Liquid source template.

## Compatibility with the roadmap

The contract now supports the P0 machine graph, integrity gate, and SAP Enterprise links. The next roadmap work should extend the same model for:

- #319 upgraded case intelligence;
- #320 evidence-review lifecycle;
- #321 portfolio coverage analytics;
- #322 negative evidence and failure cases;
- #325 role-specific agent context packs.

Those tasks should extend this contract or generate views from it. They should not create a competing Business AI source model.
