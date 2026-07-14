---
name: sap-o2c-diagnostics
description: Create a controlled first-pass diagnostic for order-to-cash issues.
---
# SAP O2C Diagnostics

Trigger on sales order, ATP, delivery, billing, pricing, output, credit, or customer symptoms.

Inputs: process stage, document status, error text, time range, affected scope, and integration context.

Workflow: separate order, availability, delivery, billing, master-data, configuration, and interface evidence; state what must be checked in the landscape.

Safety: no order changes, delivery creation, billing, credit release, or condition changes. Escalate pricing, tax, and financial postings.

Output: evidence checklist, hypotheses, owner boundary, and linked diagnostic route.

Atlas: `/atlas/diagnostics/sap-sd-order-to-cash-diagnostics-hub/`.

## Purpose
Create an evidence-first O2C diagnostic.
## Use when
Use when an order-to-cash step fails.
## Do not use when
Do not use to alter order, delivery, or billing data.
## Required inputs
Process stage, status, error, and impact.
## Workflow
Collect stage-specific evidence and identify the accountable owner.
## Decision rules
Treat pricing, tax, and finance as controlled decisions.
## Output format
Facts, hypotheses, checklist, sources, limitations.
## Quality gates
No customer data exposure or posting instruction.
## References
See `references/` and linked Atlas pages.
