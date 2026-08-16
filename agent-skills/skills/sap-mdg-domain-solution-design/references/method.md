# Method

Use this chain:

`Outcome → Identity → Grain → Technical Entity → Ownership → CR Pattern → Rule → Workflow → Activation → Distribution/Recovery → Consolidation/Migration → Business Proof`

The most important question is still grain. If a value means something different by plant, sales area, company code or purchasing organization, model that qualifier explicitly.

## 1. Identity and grain

Define the real-world object first. Then split global identity from organizational behavior.

For Material, separate global identity from plant, sales area, storage location, valuation and warehouse contexts.

For Business Partner, separate shared party identity from customer/supplier roles and company-code, sales-area or purchasing-organization behavior.

## 2. Technical entity checkpoint

Map critical business grains to delivered MDG entities before inventing custom storage.

Ask:
- Which delivered entity represents this grain?
- Is the attribute already supported in the selected release/scope?
- Is this really an attribute, a repeating/dependent entity or a separate lifecycle object?
- Does the technical entity contain attributes with different business owners?

Technical entity names describe modeling. They do not assign business authority.

## 3. Change-request pattern

Choose CR types by purpose, scope, risk, authority and volume.

Useful patterns:
- new identity;
- organizational extension;
- sensitive attribute change;
- low-risk correction;
- block/unblock/deletion;
- mass change;
- emergency correction.

Do not build one universal CR type merely because one workflow is easier to maintain.

## 4. Rule catalog

Classify each important rule:
- workflow routing;
- validation;
- derivation;
- authorization/scope;
- duplicate/identity.

Every important rule needs a business statement, grain, inputs, output, execution point, owner and positive/negative tests.

## 5. Activation and distribution

Keep four proofs separate:

1. Governance proof: the right authority approved the right scope.
2. Activation proof: the intended value became active truth.
3. Distribution proof: the intended consumer accepted and persisted it.
4. Business proof: the process actually used it.

For DRF, trace:

`Active source → Selection → Payload → Transport → Identity mapping → Target acceptance → Persistence → Consumer`

## 6. Recovery

Before replay, prove:
- current active source state;
- target state after the failed/timed-out attempt;
- idempotency or duplicate behavior;
- ordering against later changes;
- population scope.

Then choose:
- safe replay;
- rebuild from current active truth;
- manual controlled resolution;
- stop and reconcile the population.

## 7. Consolidation

Keep two decisions separate:

`Matching = same identity?`

`Survivorship = which value wins?`

Define automatic-match, review and non-match bands. Then define source priority, recency, completeness or domain-specific precedence per table/field. Preserve provenance and manual override reason.

## 8. Migration and cut-off

Reconcile by identity and required organizational slices, not only root-object counts.

For initial load to delta, prove:

`Baseline population → selected → sent → accepted → persisted → mapping coverage → cut-off → first delta → no-gap reconciliation`

## 9. Business proof

End with the consuming process. Examples:
- Material plant extension → MRP / production / purchasing proof.
- Customer sales-area extension → sales order / delivery proof.
- Supplier purchasing-org extension → purchase order / invoice proof.
- Warehouse-relevant product → EWM execution proof.

The design is not complete until the governed value changes the intended business behavior.
