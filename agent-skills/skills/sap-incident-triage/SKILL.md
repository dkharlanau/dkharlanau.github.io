---
name: sap-incident-triage
description: Turn a SAP support symptom into an evidence-based incident brief without changing a system.
---
# SAP Incident Triage

Use when a support request has an observed symptom but the cause and ownership are unclear.

Required inputs: symptom, affected business process, timeframe, known document or message identifiers, and access boundary.

Workflow: retrieve reviewed Atlas material first; classify facts, gaps, and hypotheses; request the smallest useful evidence set; identify the next diagnostic owner; produce an incident brief. Do not invent log values, configuration, client data, or root causes.

Evidence rules: preserve source URL, verification state, timestamps, and whether evidence is direct or reported. Use public Atlas pages only when no private authorization exists.

Safety: read-only by default. No reprocessing, configuration change, transport, or business posting. Escalate when a production write, sensitive data, or unsupported claim is required.

Output: concise incident brief with facts, hypotheses, evidence checklist, owner, limitations, and related verified Atlas links.

Atlas: `/atlas/diagnostics/sap-incident-triage-diagnostics/`, `/atlas/diagnostics/`.

## Purpose
Create a safe first-pass incident brief.
## Use when
Use when facts and ownership are incomplete.
## Do not use when
Do not use to authorize system changes.
## Required inputs
Symptom, scope, time, and access boundary.
## Workflow
Retrieve reviewed content, collect evidence, classify uncertainty, and route.
## Decision rules
Prefer evidence over inference and read-only over action.
## Output format
Facts, hypotheses, checklist, owner, sources, limitations.
## Quality gates
No private data, invented cause, or write instruction.
## References
See `references/` and linked Atlas pages.
