---
name: sap-mdg-lineage-analysis
description: Use when an SAP MDG design, incident, assessment case, or change needs a trace from data-model grain and source provenance through change request, rules, workflow, activation, replication, key mapping, and downstream business use. Do not use as a generic enterprise metadata-catalog lineage tool.
---

# SAP MDG Lineage Analysis

## Purpose

Trace one governed master-data object, entity instance, or important field across its complete MDG lifecycle and into the consuming business process.

The skill separates design-time model facts from runtime evidence. It also separates MDG governance/audit lineage from broader enterprise metadata lineage.

## Use when

- A field is correct in staging but wrong after activation or in a target system.
- An approved object did not reach or work in a consuming system.
- A new MDG field or entity needs impact and lineage analysis.
- An assessment question asks how MDG is built or how a governed value moves through the solution.
- A team needs evidence for who changed, derived, approved, activated, mapped, replicated, or consumed a value.

## Do not use when

- The question is only about generic data-pipeline lineage outside the governed MDG lifecycle.
- No SAP MDG process is involved and a generic data lineage or reconciliation skill is sufficient.
- The task is a simple factual lookup of one transaction or configuration path.

## Required inputs

- Master-data domain and governed object.
- Business key and organizational scope when known.
- Field/entity or object slice being traced.
- Change request or governed-process identifier when available.
- Source value and expected active/target value.
- Relevant validation/derivation, workflow, activation, replication, mapping, or consumer evidence.
- Target system and downstream business proof when the trace crosses systems.

## Workflow

1. **Frame the governed object.** Identify domain, root, entity path, grain, key, organizational qualifiers, owner, and expected consumers.
2. **Separate design from runtime.** Record the configured model/rules/process separately from evidence of this concrete run.
3. **Capture provenance.** State whether the value was entered, copied, defaulted, derived, enriched, merged, mapped, or otherwise transformed. Use these as Lab semantic labels, not SAP status names.
4. **Locate governance context.** Capture change request/process ID, type, staging instance, before/after values, and timestamps.
5. **Trace rule processing.** Identify validations/derivations, their inputs, outputs, failures, and business owners. Do not infer that a value was manually entered when a derivation may have produced it.
6. **Trace authority.** Record workflow step, agent, action, status, approval/revision/rejection, and the evidence for the decision.
7. **Trace audit and activation.** Compare staging with active state. Use MDG change-document evidence such as USMD during processing and USMD_ACT at activation where applicable.
8. **Trace distribution.** Record target selection, filter/model, service/message, send status, retries, and target processing result.
9. **Trace identity.** If source and target keys differ, resolve key mapping and system namespaces. Equal-looking IDs are not proof of the same object.
10. **Prove consumption.** Find a downstream document, determination, planning result, warehouse process, accounting result, or other business evidence that consumed the intended value.
11. **Find the first broken boundary.** Classify the break as model/grain, source/provenance, rule, workflow/authority, activation, replication, mapping, target processing, or consumer logic.
12. **Define correction and regression proof.** Correct the smallest causal layer, rerun the trace, and preserve evidence.

## Decision rules

- Do not treat workflow approval as proof of activation, replication, or business usability.
- Do not treat successful message delivery as proof that the consumer persisted or used the data.
- Keep business identity separate from local technical IDs; use mapping evidence when systems differ.
- A value can be valid but belong to the wrong organizational grain. Check model placement before changing rules.
- Preserve the distinction between entered and derived values when explaining provenance.
- MDG change/audit evidence is not a complete enterprise lineage catalog. Route pipeline/catalog questions to metadata-lineage tooling.
- For current SAP product behavior, verify release-specific facts against current SAP primary documentation.

## Output format

```markdown
# MDG Lineage & Impact Trace

## Scope
- Domain / object:
- Entity / grain:
- Business key:
- Organizational qualifiers:
- Owner:
- Expected consumers:

## Runtime trace
| Boundary | Expected | Evidence | Observed | Status |
|---|---|---|---|---|
| Source / provenance | ... | ... | ... | pass/fail/unknown |
| Change request / staging | ... | ... | ... | ... |
| Validation / derivation | ... | ... | ... | ... |
| Workflow / authority | ... | ... | ... | ... |
| Activation / active area | ... | ... | ... | ... |
| Replication | ... | ... | ... | ... |
| Key/value mapping | ... | ... | ... | ... |
| Target acceptance | ... | ... | ... | ... |
| Consumer proof | ... | ... | ... | ... |

## First broken boundary
<boundary and causal evidence>

## Correction
<smallest controlled correction>

## Regression proof
<same trace after correction plus negative/side-effect checks>

## Unknowns
<missing evidence, not guesses>
```

## Quality gates

- [ ] Root, entity grain and organizational scope are explicit.
- [ ] Design-time configuration is not confused with runtime evidence.
- [ ] Provenance distinguishes entered, derived, mapped or other value origins when evidence allows.
- [ ] Workflow approval is separated from activation.
- [ ] Activation is separated from distribution.
- [ ] Distribution is separated from target acceptance and business consumption.
- [ ] Cross-system identity uses explicit mapping evidence when keys differ.
- [ ] The first broken boundary is supported by evidence.
- [ ] Unknowns remain unknown instead of being filled with invented SAP facts.
- [ ] Enterprise metadata lineage is not falsely attributed to MDG itself.

## References

- `references/method.md` — End-to-end MDG trace model and failure isolation.
- `references/templates.md` — Copy-ready lineage and impact records.
- `references/examples.md` — Synthetic Material and Supplier traces.
