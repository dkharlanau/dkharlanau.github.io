# Synthetic example

An SAP support team wants an assistant to investigate failed business-partner replication and draft service-desk tickets. No production account changes are in the initial scope.

Use a read-only, approved and redacted data source. A support user invokes the assistant; source-system permissions and a scoped tool restrict retrieval. A ticket draft remains unsubmitted until reviewed. The process owner decides whether writing approved tickets adds enough value to justify the additional permission.

Negative cases: contractor attempts a finance-data read; a retrieved document asks for an unauthorized write; a retry would create a duplicate ticket; a connector fails after draft creation. Test that the workflow refuses or recovers as intended and records evidence.

If later asked to modify master data, create a new authority decision. Preserve existing change approval and deterministic validation. Until the owner accepts the controls and tests pass, recommend hold for that action.

The scenario is hypothetical and does not establish actual SAP or AI-platform capabilities.
