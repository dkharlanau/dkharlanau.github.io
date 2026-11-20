---
name: data-architecture-selection
description: Use when selecting or reviewing a warehouse, lakehouse, data fabric, data mesh, data integration, or SAP analytics architecture; produce an evidence-led option comparison and validation plan. Do not use as approval to change production infrastructure.
---

# Data Architecture Selection

Select a data architecture for a defined business decision, not for a technology label. This is the agent-facing companion to the [human skill](../../../skill-hub/architecture/data-architecture-selection-working-skill.md).

## Purpose

Produce an evidence-backed architecture decision and verification plan, keeping governance, ownership, storage, and data movement explicit.

## Use when

- A team needs a defensible choice between a warehouse, lakehouse, virtualized access, fabric capabilities or a mesh operating model.
- An integration or reporting design lacks freshness, history, ownership or reconciliation requirements.
- Stakeholders ask for an architecture review, alternative options or an ADR.
- An SAP/ERP landscape needs an analytical solution across governed master data and other sources.

## Do not use when

- The task is only to define a product feature, debug an individual record or change a production configuration.
- You lack a business consumer and decision: first run discovery.
- The user asks you to move private records to public infrastructure. Do not perform this action.

## Required inputs

- Business job, consumer, consequence of a wrong answer and representative query.
- Source inventory and system-of-record boundaries, entity keys, update/delete semantics.
- Freshness, volume, history, security, residency, uptime and recovery constraints.
- Users' skills and expected workload, cost/operations ownership, deadline.
- Current platform and data quality evidence, if known.

Missing inputs are **unknown**, not guessed or silently rated.

## Workflow

1. State a neutral architecture decision question and the business action it supports.
2. Separate observed facts, stakeholder claims, assumptions, unknowns and vendor capabilities.
3. Map one representative data element from system of record through ingestion, modeling and consumption.
4. Distinguish storage/compute (warehouse, lake, lakehouse), connective capabilities (fabric) and domain ownership (mesh). Compare combinations when appropriate.
5. Shortlist the status quo and at least two viable changes, or explain why fewer are feasible.
6. Compare correctness, model usability, data freshness, access control, lineage, failure recovery, skills, operating effort, portability and total cost. Support each rating.
7. Choose a bounded pilot with one source, one model, one consumer and a forced failure/replay test.
8. Draft an ADR and executable acceptance criteria. State conditions that would reverse the recommendation.
9. Stop before production access changes, data movements, vendor commitments or releases; obtain explicit human review.

## Decision rules

- If BI users need a stable business model, prioritize a semantic/serving layer, regardless of storage.
- If raw files and large-scale experimentation dominate, compare lake/lakehouse against managed-warehouse plus landing zone.
- If source access policies, lineage or discovery fail, evaluate fabric capabilities without presuming a storage rewrite.
- If domains lack funded data product owners and shared interoperability standards, do not recommend full Data Mesh.
- If copying is constrained, evaluate federation but test source load, latency and permissions.
- If a nightly refresh meets the business SLA, do not demand streaming.
- If CDC/change messages cannot represent deletions or reconstruct state, require a reconciliation and recovery design.
- For SAP customer data, do not equate Business Partner, customer number, sold-to and payer without proven mapping.

## Output format

Produce a **Data Architecture Decision Pack** using [templates.md](references/templates.md):
1. Decision statement and evidence/assumptions register.
2. Source-to-consumer diagram in text or Mermaid.
3. Options matrix with explicit disadvantages.
4. Proposed thin slice and pass/fail tests.
5. ADR summary, owner, risks and review trigger.

## Quality gates

- [ ] Decision is consumer-led and does not assume a preferred product.
- [ ] At least two options, including current state where appropriate.
- [ ] Missing evidence is visibly unknown, not invented.
- [ ] Distinct business identifiers and history are not flattened into “Customer 360”.
- [ ] Security, deletion, replay, traceability and recovery have tests.
- [ ] Fabric and Mesh are not described as mutually exclusive product purchases.
- [ ] Costs and performance are hypotheses until measured.
- [ ] Human approval is required for any irreversible or production-changing action.
- [ ] Source claims are traced to authoritative documents; examples are labeled synthetic.

## References

- [Method and trade-off lenses](references/method.md)
- [Templates](references/templates.md)
- [Synthetic examples and anti-patterns](references/examples.md)
- [Public knowledge guide](../../../atlas/concepts/data-architecture-field-guide.md)
- James Serra, *Deciphering Data Architectures* (O'Reilly, 2024); original synthesis, not reproduced content.
