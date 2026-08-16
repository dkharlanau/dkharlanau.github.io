# Examples

## Material plant extension
Outcome: plan and procure an existing Material in Plant 2000.

Do not create another Material identity. Confirm the existing `MATERIAL` root, map required plant meaning to plant entities such as `MARCBASIC` and the relevant MRP/purchasing/quality segments, assign planning/procurement ownership, use an organizational-extension CR path, activate, distribute if the consumer is remote, then prove MRP and PO creation.

A weak answer says “extend the Material views”. A stronger answer names the business grain, technical entity family, owner, rule, CR pattern and downstream proof.

## Customer sales-area extension
Outcome: enable an existing BP/customer for a new sales area.

Preserve shared BP identity. Add the required customer sales-area grain, apply commercial completeness rules, approve with the correct sales authority, activate, distribute and prove sales-order behavior. Shared BP identity fields should not become editable merely because the same CR opens a customer extension.

## Sensitive supplier bank change
Outcome: change supplier bank data without turning the normal supplier-maintenance workflow into a high-risk catch-all.

Classify the change as sensitive, restrict the CR scope, preserve old/new evidence, route to the required authority, apply deterministic validation, activate, distribute and test the payment-side consumer. Keep business rejection separate from activation or replication failure.

## DRF target outage
Outcome: recover changes after a target system was unavailable while later changes may already have succeeded.

Do not replay everything. Freeze the affected object/population and target, prove current active source state, check target persistence and later changes, inspect idempotency and ordering, then choose safe replay, rebuild from current truth, manual resolution or stop-and-reconcile. Close only after source/target reconciliation and business-consumer proof.

## Duplicate supplier consolidation
Outcome: resolve two supplier identities while preserving business continuity.

First decide whether the records represent the same real-world party using strong identity evidence and the configured review policy. Then calculate survivorship separately using explicit source, recency, completeness or domain rules. Preserve provenance and manual overrides. Choose Remove Duplicates, Improve Best Record or Improve All Records only after checking key mapping, transaction history and downstream behavior.

## Automotive multi-plant rollout
Outcome: centralize Material and Supplier governance across 12 plants and 7 consuming systems.

Use one shared identity model but not one universal workflow. Separate global Material/BP ownership from plant, sales-area, company-code, purchasing-org and warehouse grains. Define CR patterns for creation, organizational extension, sensitive change and mass change. Build DRF populations/filters per consumer, reconcile the initial load to the first delta, and prove representative O2C, P2P, MRP and EWM processes before rollout acceptance.
