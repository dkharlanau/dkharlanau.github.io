---
name: sap-mdg-domain-solution-design
title: SAP MDG Domain Solution Design
category: sap-data-governance
description: Use when an SAP MDG Material, Business Partner, Customer, or Supplier solution needs domain design across identity, technical entities, organizational grain, ownership, rules, change requests, workflow, activation, DRF distribution and recovery, consolidation, migration, and downstream logistics proof. Use for Lead or Architect assessment cases and solution reviews, not for a single already-isolated lineage incident.
---

## Purpose
Design or review an SAP MDG domain solution from business identity through technical entity/grain mapping, governance process, rules, activation, distribution/recovery, consolidation or migration, and downstream business proof.

## Use when
- Designing Material, Business Partner, Customer or Supplier governance.
- Adding a new organizational extension or custom field/entity.
- Reviewing change-request types, workflow and BRFplus rule architecture.
- Planning DRF distribution, replay, reconciliation and target-system ownership.
- Planning migration, matching or consolidation into MDG.
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
- Integration, migration or consolidation context if relevant.
- Product/release scope when exact delivered entities or CR types matter.

## Workflow
1. State the business outcome in one sentence.
2. Define enterprise identity, duplicate policy and key/number strategy.
3. Decompose required data by business grain.
4. Map critical grains to delivered technical entities; separate delivered entity, custom extension and separate lifecycle object.
5. Assign business owner, steward, proposal rights and approval authority per grain.
6. Select change-request patterns by purpose, allowed entity scope, risk, volume and authority.
7. Classify important rules as workflow routing, validation, derivation, authorization/scope or identity/matching; define deterministic tests.
8. Define active-area/activation boundary and a separate activation-error recovery path.
9. Define distribution contract: population, DRF model, outbound implementation, filter, target, identity mapping, acceptance and monitoring.
10. Define recovery semantics: replay, rebuild from current active truth, manual resolution or population reconciliation.
11. If consolidation applies, separate match decision from survivorship; define thresholds, review band, winning rules, provenance and duplicate strategy.
12. Define migration/initial-load population, reconciliation, delta cut-off and no-gap proof.
13. Define business-process proof in O2C, P2P, MRP, EWM, QM or other consumers.
14. Record risks, open assumptions and the first test that could falsify the design.

## Decision rules
- Screen location never proves data grain.
- Technical entity name never proves business ownership.
- A field changing by organization must carry that organizational qualifier unless a clear enterprise rule says otherwise.
- Do not pull a separate lifecycle object into Material/BP only because it references the master object.
- Split CR patterns when purpose, scope, authority, risk, volume or recovery behavior materially differs.
- Workflow controls authority and movement; validation controls allowed state; derivation calculates values.
- Keep business rejection, activation failure and replication failure as different states.
- Activation is not replication success.
- Sent message is not target acceptance.
- Do not replay historical payloads until current source state, target state, ordering and duplicate behavior are understood.
- Matching score is evidence, not automatic authority for an irreversible merge unless policy explicitly allows it.
- Matching decides identity similarity; survivorship decides value precedence.
- Migration completion requires key-level reconciliation, organizational-slice completeness and business usability.
- Prefer deterministic rules for exact business constraints; use human approval for judgment and authority.

## Output format
Produce an `SAP MDG Domain Solution Design` with:
1. Business outcome
2. Identity model
3. Grain and technical entity map
4. Ownership / decision-rights map
5. Change-request type matrix
6. Rule catalog
7. Workflow and activation model
8. Distribution and recovery contract
9. Matching / survivorship policy if applicable
10. Migration / initial-load / delta plan
11. Business proof cases
12. Operational metrics and exception ownership
13. Risks and open assumptions
14. Recommended next decision

## Quality gates
- Every critical field/entity has a declared business grain.
- Delivered entity references are release-scoped when exact product facts matter.
- Every governed grain has a business owner and explicit proposal/approval rights.
- CR types expose only the intended scope for their purpose and risk.
- Important rules have a business statement, owner, execution point, positive test and negative test.
- Workflow decisions correspond to real authority.
- Business rejection, activation error and replication error are not collapsed into one state.
- Target systems and identity strategy are explicit.
- Replay semantics include current-source and target-state checks.
- Matching and survivorship are separate decisions with provenance.
- Initialization/delta or migration cut-off has no unexplained gap.
- Reconciliation uses keys and slices, not only root-object counts.
- At least one real downstream process proves the design.
- SAP-version-dependent facts are sourced.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
- Human pages under `labs/enterprise-context/mdg/`.
