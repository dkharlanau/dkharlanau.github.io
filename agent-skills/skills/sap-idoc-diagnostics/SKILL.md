---
name: sap-idoc-diagnostics
description: Structure evidence collection and next checks for SAP IDoc failures.
---
# SAP IDoc Diagnostics

Trigger on IDoc status, ALE, EDI, inbound/outbound, partner-profile, or reprocessing requests.

Inputs: IDoc number if authorized, direction, message type, partner, current status, error text, time range, and affected volume.

Workflow: separate status observation from cause; use the status history to choose application, queue, port, partner, or scheduling checks; collect evidence before recommending reprocessing.

Evidence: capture status history, error text, timestamps, message type, partner, and related queue/application-log reference. Do not publish identifiers or payloads.

Safety: do not run BD87, change partner profiles, or resend messages without explicit human approval and a confirmed cause. Escalate cross-system or data-correction cases.

Output: status-based checklist, hypotheses, owner boundary, and source-linked limitations.

Atlas: `/atlas/diagnostics/sap-idoc-status-diagnostics/`, `/atlas/diagnostics/sap-idoc-diagnostics/`.

## Purpose
Organize IDoc evidence before remediation.
## Use when
Use when an IDoc or ALE status is reported.
## Do not use when
Do not use to execute reprocessing or configuration changes.
## Required inputs
Status, message type, direction, error, and time range.
## Workflow
Classify the status layer, gather evidence, and identify owner.
## Decision rules
Fix the cause before any reprocessing decision.
## Output format
Checklist, hypotheses, owner boundary, sources, limitations.
## Quality gates
No payload exposure or unsupported status interpretation.
## References
See `references/` and linked Atlas pages.
