# Business AI Data and Graph Contract

Status: canonical technical contract  
Roadmap: #315, #319, #320  
Canonical machine definition: `_data/labs/business_ai/contract.yml`  
Updated: 2026-08-18

## Purpose

Business AI already has useful cases, processes, scenarios, technologies, decision profiles, controls, and evidence. This contract gives those sources one stable agreement for IDs, entity types, relationships, case intelligence, evidence fields, review state, and generated views.

The YAML contract is the source of truth for these rules. This document explains how to use it. Do not copy its vocabularies into a second schema file.

## Source and output boundary

Canonical content stays under `_data/labs/business_ai/`. The contract maps each existing dataset to a role rather than replacing those datasets with a new database.

The files under `labs/business-ai/data/*.json` and `/ai/business-ai-graph.json` are Jekyll-rendered machine views. They are outputs over canonical YAML sources. Change the YAML source or the rendering template, not the rendered JSON result.

This keeps the current pages working while graph, coverage analytics, and agent context packs use the same model.

## Stable identity

Entity and relationship IDs use lowercase kebab-case. IDs are public identity, not display text.

A title may change without changing its ID. Retired IDs are not reused. Cross-dataset references use IDs instead of titles when a stable ID exists.

A breaking ID change, required-field removal, or controlled-vocabulary removal requires a major contract version. Additive optional fields, vocabulary values, relationship types, and review gates for states not reached by legacy records may use a minor version.

## Controlled vocabularies

The contract owns shared values that cross datasets, including case kind, evidence grade, source confidence and type, review state, autonomy level, implementation maturity, outcome state, evidence level, transferability, and measurement state.

The contract reuses current Business AI semantics where they already exist. Evidence grades remain A/B/C/D from the catalog. Autonomy remains L0-L5 from the assessment matrix.

`unknown` is not a weak fact. It means the field is not yet classified from available evidence. A `proof_gap` is different: it records a specific claim or decision that still needs evidence or review.

## Case intelligence schema

Case schema 2.0 extends a public AI case beyond company, title, pattern, and a result claim. A review-ready case should make the decision boundary inspectable.

It covers:

- business problem, end-to-end process, and stable process stage IDs;
- AI job and reusable pattern IDs;
- implementation maturity and autonomy level;
- systems of record, data dependencies, and integration boundaries;
- authority boundary, controls, and human review;
- metrics and measurement state;
- evidence grade, typed evidence claims, source IDs, and source types;
- limitations and proof gaps;
- transferability and failure notes;
- consultant interpretation kept separate from source facts.

Legacy fields remain readable through explicit aliases. Missing normalized values stay missing or `unknown`. Migration is not permission to infer production maturity, autonomy, measurement quality, or implementation type from a marketing story.

A legacy case receives a conservative review state only from existing structure: source IDs plus pattern plus evidence grade can be `structured`; source IDs alone can be `sourced`; otherwise the record remains `candidate`.

## Evidence levels

Evidence level and evidence grade answer different questions.

**Evidence level** describes what kind of statement is being made:

- `source_fact` is directly visible in a source, configuration, log, test, scanner result, or provided material;
- `supported_inference` is a reasonable conclusion from available facts;
- `runtime_proof` is observed runtime evidence and is valid only when the activity was approved and observed;
- `unsupported_claim` goes beyond available evidence;
- `proof_gap` marks something that still needs evidence or review.

**Evidence grade** describes the strength of public result evidence already used by the Business AI catalog. A high grade does not turn an inference into runtime proof.

A `runtime_proof` claim must record that runtime activity was both authorized and observed. If either condition is missing, the claim is invalid.

## Review lifecycle

The canonical lifecycle is:

`candidate -> sourced -> structured -> challenged -> review_ready -> approved`

`needs_more_evidence` and `rejected` are explicit branches, not hidden comments.

A record can move back from `approved` when evidence becomes stale or contradictory. The default approved-case freshness review is 180 days.

Agents may prepare, structure, and challenge cases and may move a complete record to `review_ready`. They cannot approve their own evidence. `approved` requires an identified human reviewer and review date.

A `review_ready` or `approved` case cannot contain an `unsupported_claim`. It must contain at least one `source_fact`, and critical fields such as case kind, implementation maturity, measurement state, and transferability cannot still be `unknown`.

Duplicate evidence about the same implementation updates the existing case. It does not create another record simply to increase the case count.

## Graph contract

The contract uses the existing Business AI graph model. It defines typed entities such as process, process stage, enterprise capability, pattern, platform, case, outcome, failure, decision profile, metric, evidence source, control, and limitation.

Relationships are typed and directional. A relationship is valid only when both referenced nodes exist and their entity types match the relationship definition. This allows CI to reject a graph that looks syntactically correct but connects the wrong concepts.

SAP-specific capabilities link to vendor-neutral process and stage IDs. Existing SAP Enterprise pages remain the implementation source. Other ERP platforms should use their own capability-link dataset against the same neutral process model.

## Consumers

Jekyll continues to read canonical YAML and render human and machine views. Machine artifacts preserve stable IDs and declare their contract version. Agents consume the same contract plus generated context packs. Analysis views consume normalized graph and coverage outputs.

Agents may propose new records or relationships. They do not promote their own evidence to an approved state when human review is required.

## Validation

`scripts/check_business_ai_contract.py` validates the core graph contract and alignment with existing source vocabularies. `scripts/check_business_ai_graph.py` validates graph references, SAP cross-product links, and strategic coverage gaps. `scripts/check_business_ai_cases.py` validates case schema, evidence claims, review transitions, runtime-proof rules, and human approval boundaries.

Pytest includes negative tests for invalid graph IDs, orphan relationships, unsupported review-ready claims, unapproved runtime proof, invalid lifecycle transitions, unknown critical review-ready fields, and agent-only approval.

The repository CI runs the full test suite plus Jekyll build, content quality, links, SEO, accessibility, and machine-endpoint validation. No separate Business AI workflow is required.

## Compatibility with the roadmap

This contract is the base for machine-readable graph artifacts, integrity gates, case intelligence, portfolio coverage analytics, failure intelligence, agent context packs, and decision-analysis views.

Later roadmap tasks should extend this contract or generate views from it. They should not create a competing Business AI source model.
