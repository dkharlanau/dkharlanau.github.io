# Business AI Data and Graph Contract

Status: canonical technical contract  
Roadmap: #315  
Canonical machine definition: `_data/labs/business_ai/contract.yml`  
Updated: 2026-08-18

## Purpose

Business AI already has useful cases, processes, scenarios, technologies, decision profiles, controls, and evidence. This contract gives those sources one stable agreement for IDs, entity types, relationships, evidence fields, review state, and generated views.

The YAML contract is the source of truth for these rules. This document explains how to use it. Do not copy its vocabularies into a second schema file.

## Source and output boundary

Canonical content stays under `_data/labs/business_ai/`. The contract maps each existing dataset to a role rather than replacing those datasets with a new database.

The files under `labs/business-ai/data/*.json` are Jekyll-rendered machine views. They are outputs over canonical YAML sources. Change the YAML source or the rendering template, not the rendered JSON result.

This keeps the current pages working while later roadmap tasks can build a normalized graph, coverage analytics, and agent context packs over the same model.

## Stable identity

Entity and relationship IDs use lowercase kebab-case. IDs are public identity, not display text.

A title may change without changing its ID. Retired IDs are not reused. Cross-dataset references use IDs instead of titles when a stable ID exists.

A breaking ID change, required-field removal, or controlled-vocabulary removal requires a major contract version. Additive optional fields and new relationship types may use a minor version.

## Controlled vocabularies

The contract owns shared values that cross datasets:

- case kind;
- evidence grade;
- source confidence;
- review state;
- autonomy level;
- outcome state;
- evidence level.

Existing Business AI semantics are reused. Case kinds remain `ai_implementation`, `ai_foundation`, and `solution_evidence`. Evidence grades remain A/B/C/S. Autonomy remains L0-L5 from the existing assessment matrix.

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

## Graph contract

The contract uses the existing Business AI graph model. It defines typed entities such as process, process stage, pattern, platform, case, outcome, failure, decision profile, metric, evidence source, control, and limitation.

Relationships are typed and directional. A relationship is valid only when both referenced nodes exist and their entity types match the relationship definition. This allows CI to reject a graph that looks syntactically correct but connects the wrong concepts.

## Consumers

Jekyll continues to read canonical YAML and render human and machine views. Machine artifacts preserve stable IDs and declare their contract version. Agents consume the same contract plus generated context packs. Analysis views consume normalized graph and coverage outputs.

Agents may propose new records or relationships. They do not promote their own evidence to an approved state when human review is required.

## Validation

`scripts/check_business_ai_contract.py` validates the contract, a normalized graph fixture, and alignment with existing catalog and autonomy vocabularies. `tests/test_business_ai_contract.py` also proves that invalid IDs, wrong edge type pairs, and invalid evidence grades fail validation.

The repository CI already installs PyYAML and runs the full `tests/` suite. No separate Business AI workflow is required.

## Compatibility with the roadmap

This contract is the base for:

- #316 machine-readable graph artifacts;
- #317 graph integrity and evidence coverage gates;
- #319 upgraded case intelligence;
- #321 portfolio coverage analytics;
- #325 role-specific agent context packs.

Those tasks should extend this contract or generate views from it. They should not create a competing Business AI source model.
