---
name: sap-bp-replication
description: Diagnose business-partner replication evidence without changing master data.
---
# SAP BP Replication

Trigger on BP, customer/vendor, CVI, MDG-to-S/4, or replication errors.

Inputs: direction, source and target role, object type, error text, timestamp, and approved identifiers.

Workflow: distinguish mapping, role, governance activation, integration, and target-validation symptoms; collect the object state and message evidence; route to the accountable master-data or integration owner.

Safety: never propose mass correction, reprocessing, or mapping changes without approval. Treat personal and supplier data as sensitive. Escalate duplicate or legal-entity conflicts.

Output: evidence checklist, cause categories, uncertainty, and related Atlas links.

Atlas: `/atlas/diagnostics/sap-business-partner-replication-diagnostics/`, `/atlas/diagnostics/sap-cvi-synchronization-diagnostics/`.

## Purpose
Frame BP replication diagnostics without changing data.
## Use when
Use when BP, CVI, or replication fails.
## Do not use when
Do not use for data correction or activation.
## Required inputs
Direction, object, role, error, time, permitted identifiers.
## Workflow
Separate mapping, workflow, and interface evidence; route ownership.
## Decision rules
Protect sensitive master data and require steward approval.
## Output format
Evidence gaps, hypotheses, owner, source links, limitations.
## Quality gates
No personal data or mass-correction instruction.
## References
See `references/` and linked Atlas pages.
