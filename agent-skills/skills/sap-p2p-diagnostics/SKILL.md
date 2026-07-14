---
name: sap-p2p-diagnostics
description: Create a controlled first-pass diagnostic for procure-to-pay issues.
---
# SAP P2P Diagnostics

Trigger on requisition, PO, goods receipt, invoice, release, supplier, or account-assignment issues.

Inputs: process step, document status, affected item, error text, dates, and known integration context.

Workflow: locate the process stage; split master-data, release/configuration, posting, and integration hypotheses; list evidence before remediation.

Safety: no PO changes, release, goods movement, invoice posting, or configuration changes. Escalate valuation, tax, payment, or authorization decisions.

Output: diagnostic checklist, facts/hypotheses separation, owner, next Atlas links.

Atlas: `/atlas/diagnostics/sap-procurement-diagnostics-hub/`.

## Purpose
Create an evidence-first P2P diagnostic.
## Use when
Use when procurement process status is unclear.
## Do not use when
Do not use to post or release documents.
## Required inputs
Process step, document state, error, and scope.
## Workflow
Locate stage, group hypotheses, request evidence, route owner.
## Decision rules
Separate master data, configuration, posting, and interface issues.
## Output format
Checklist, hypotheses, escalation boundary, sources.
## Quality gates
No business posting or configuration instruction.
## References
See `references/` and linked Atlas pages.
