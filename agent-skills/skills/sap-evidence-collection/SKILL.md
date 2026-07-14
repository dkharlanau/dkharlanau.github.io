---
name: sap-evidence-collection
description: Collect minimal, auditable SAP incident evidence before escalation.
---
# SAP Evidence Collection

Trigger before escalation, root-cause analysis, or an agent-generated incident brief.

Inputs: symptom, process scope, time window, data classification, and allowed access.

Workflow: identify direct facts; record source, timestamp, and owner; request only evidence needed to separate hypotheses; redact or minimize identifiers.

Safety: never request credentials, unrestricted exports, personal data, or client secrets. Escalate if data classification or authorization is unclear.

Output: evidence log, gaps, facts versus hypotheses, and an escalation-ready summary.

Atlas: `/atlas/diagnostics/sap-incident-triage-diagnostics/`.

## Purpose
Collect minimal evidence for an auditable escalation.
## Use when
Use before escalation or root-cause analysis.
## Do not use when
Do not use to request unrestricted sensitive data.
## Required inputs
Symptom, time window, classification, and access boundary.
## Workflow
Record facts, source, timestamp, gaps, and uncertainty.
## Decision rules
Minimize data and preserve provenance.
## Output format
Evidence log, gaps, facts versus hypotheses, escalation summary.
## Quality gates
No credential, client, or personal-data leakage.
## References
See `references/` and linked Atlas pages.
