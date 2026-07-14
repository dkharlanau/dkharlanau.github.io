---
name: sap-interface-monitoring
description: Build an evidence-first interface monitoring checklist.
---
# SAP Interface Monitoring

Trigger on interface delay, failed message, queue, API, RFC, SOAP, or middleware ownership issue.

Inputs: interface name, direction, timestamps, error text, correlation ID when authorized, and business impact.

Workflow: locate the failure layer; compare expected and observed flow; collect technical and business evidence; state the handoff owner.

Safety: no queue deletion, retry, endpoint change, or credential rotation. Escalate data-loss, security, and cross-team ownership ambiguity.

Output: monitoring checklist, chronology, hypotheses, and limitation statement.

Atlas: `/atlas/diagnostics/sap-interface-monitoring-diagnostics/`, `/atlas/diagnostics/sap-integration-diagnostics-hub/`.

## Purpose
Build an auditable interface monitoring checklist.
## Use when
Use when an interface is delayed or fails.
## Do not use when
Do not use to retry, delete queues, or change endpoints.
## Required inputs
Interface, direction, chronology, error, and business impact.
## Workflow
Locate the layer, compare expected flow, gather evidence, route owner.
## Decision rules
Do not confuse technical recovery with business reconciliation.
## Output format
Chronology, checklist, hypotheses, owner, limitations.
## Quality gates
No credential exposure or operational action.
## References
See `references/` and linked Atlas pages.
