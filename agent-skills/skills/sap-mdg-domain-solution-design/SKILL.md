---
name: sap-mdg-domain-solution-design
title: SAP MDG Domain Solution Design
category: sap-data-governance
---

## Purpose
Design or review an SAP MDG domain solution from business identity to organizational grain, governance process, rules, activation, distribution, migration and downstream business proof.

## Use when
- Designing Material, Business Partner, Customer or Supplier governance.
- Adding a new organizational extension or custom field/entity.
- Reviewing change-request and workflow architecture.
- Planning DRF distribution and target-system ownership.
- Planning migration or consolidation into MDG.
- Preparing a Lead/Architect assessment answer for MDG.

## Do not use when
- The task is only to diagnose one already-known lineage break. Use `sap-mdg-lineage-analysis`.
- The task is generic data governance with no SAP MDG architecture.
- Product-version facts cannot be verified and the decision depends on exact supported content.

## Required inputs
- Business object/domain.
- Business outcome or change scenario.
- Required organizations and consumers.
- Current source/active systems.
- Known ownership and approval constraints.
- Integration and migration context if relevant.

## Workflow
1. State the business outcome in one sentence.
2. Define enterprise identity and duplicate policy.
3. Decompose required data by business grain.
4. Decide attribute versus dependent/repeating entity versus separate business object.
5. Assign business owner, steward and approval authority per grain.
6. Define validations and derivations with deterministic tests.
7. Define change-request types and workflow decisions by risk and purpose.
8. Define active-area/activation boundary for the selected deployment.
9. Define distribution contract: population, DRF model, outbound implementation, filter, target, identity mapping and acceptance.
10. Define migration/consolidation path and reconciliation controls.
11. Define business-process proof in O2C, P2P, MRP, EWM, QM or other consumers.
12. Record risks, open assumptions and the first test that could falsify the design.

## Decision rules
- Screen location never proves data grain.
- A field changing by organization must carry that organizational qualifier unless a clear enterprise rule says otherwise.
- Do not pull a separate lifecycle object into Material/BP only because it references the master object.
- Workflow controls authority; validation controls allowed state; derivation calculates values.
- Activation is not replication success.
- Sent message is not target acceptance.
- Migration completion requires key-level reconciliation and business usability.
- Matching score is evidence, not automatic authority for an irreversible merge unless policy explicitly allows it.
- Prefer deterministic rules for exact business constraints; use human approval for judgment and authority.

## Output format
Produce an `SAP MDG Domain Solution Design` with:
1. Business outcome
2. Identity model
3. Grain/entity map
4. Ownership map
5. Rule catalog
6. Change-request/workflow model
7. Activation model
8. Distribution contract
9. Migration/consolidation plan
10. Business proof cases
11. Risks and open assumptions
12. Recommended next decision

## Quality gates
- Every field/entity has a declared grain.
- Every governed grain has a business owner.
- Important rules have positive and negative tests.
- Workflow decisions correspond to real authority.
- Target systems and identity strategy are explicit.
- Initialization/delta or migration cut-off has no unexplained gap.
- Reconciliation uses keys, not only counts.
- At least one real downstream process proves the design.
- SAP-version-dependent facts are sourced.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
- Human pages under `labs/enterprise-context/mdg/`.
