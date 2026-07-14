---
name: sap-mdg-diagnostics
description: Frame MDG workflow and master-data quality diagnostics with governance boundaries.
---
# SAP MDG Diagnostics

Trigger on change request, activation, workflow, duplicate, governance, or master-data quality symptoms.

Inputs: object type, workflow state, error text, responsible data domain, timestamp, and permitted identifiers.

Workflow: identify whether the symptom is workflow, validation, derivation, activation, replication, or ownership; request audit-safe evidence.

Safety: no approval, activation, data merge, or workflow configuration change. Escalate policy and data-steward decisions.

Output: factual brief, evidence gaps, responsible owner, and related verified content.

Atlas: `/atlas/diagnostics/sap-master-data-governance-workflow-diagnostics/`, `/atlas/diagnostics/sap-master-data-activation-diagnostics/`.

## Purpose
Frame MDG workflow evidence and governance routing.
## Use when
Use when a change request or activation fails.
## Do not use when
Do not use to approve, activate, or merge data.
## Required inputs
Object type, workflow state, error, and data domain.
## Workflow
Identify workflow, validation, activation, or replication evidence.
## Decision rules
Data steward authority is required for governance action.
## Output format
Evidence list, hypotheses, owner, limitations, sources.
## Quality gates
No sensitive master-data disclosure or governance bypass.
## References
See `references/` and linked Atlas pages.
