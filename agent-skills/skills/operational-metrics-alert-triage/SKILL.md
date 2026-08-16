---
name: operational-metrics-alert-triage
description: Use this skill when an operational alert fires, monitoring is noisy, business impact is unclear, or a new service needs actionable metrics. Validate the signal, translate it to business impact, correlate evidence, assign the right owner, act safely, and tune alerts from real outcomes.
---

# Operational Metrics & Alert Triage

## Purpose
Turn alerts and metrics into useful operational decisions by connecting technical signals to business impact, scope, evidence, ownership, action, and monitoring improvement.

## Use when
- An operational alert fires and impact is unclear.
- Monitoring produces duplicate, noisy, or low-value alerts.
- Technical health looks normal while business processing fails.
- A new service or flow needs an alert model.
- Incident review shows detection was late or misleading.

## Do not use when
- A specific incident already has a clear failing component and only technical diagnosis remains.
- The task is observability architecture design without a concrete operating model.
- The user only wants a dashboard layout or visualization.

## Required inputs
- Alert, metric, or missing-signal description.
- Timestamp and threshold/condition.
- Business service or process context.
- Related logs, traces, queues, jobs, deployments, or business exceptions where available.
- Known owners and runbooks.
- Recent changes.

## Workflow
1. Validate that the signal represents a current real condition rather than stale, duplicate, or broken monitoring.
2. Translate the signal into possible business impact: users, documents, messages, orders, jobs, data, or downstream outcomes.
3. Define scope and duration.
4. Correlate related service, integration, business, data-quality, deployment, and configuration signals.
5. Classify urgency using impact, criticality, duration, recoverability, and data-integrity risk.
6. Identify the first suspected failing boundary and route to the team able to investigate it.
7. Take controlled containment, investigation, recovery, or escalation action.
8. Validate recovery using the original business outcome and relevant metrics.
9. Classify alert quality: useful, late, noisy, duplicate, missing context, or false positive.
10. Tune threshold, aggregation, suppression, deduplication, owner, runbook, or business signal based on evidence.

## Decision rules
- Severity follows business impact, not dashboard color alone.
- A technically green service does not prove the business flow completed.
- Do not suppress noisy alerts without proving that meaningful failures remain detectable.
- Duplicate alerts from one failure should be correlated where practical.
- Every actionable alert needs an owner and an investigation path.
- Monitoring improvement is part of incident closure when detection quality was weak.

## Output format
Produce an **Operational Alert Triage Record** containing:
- alert, timestamp, metric, and threshold;
- signal validation result;
- business impact, scope, duration, and integrity risk;
- related signals and recent changes;
- first suspected boundary and owner;
- action, containment/recovery, and validation;
- alert-quality classification;
- tuning and runbook actions.

## Quality gates
- Business impact is stated or explicitly unknown.
- Technical and business signals are both considered where relevant.
- Urgency is evidence-based.
- Owner maps to the suspected failing boundary.
- Recovery is validated against business outcome.
- Alert tuning preserves detection of meaningful failures.

## References
- `references/method.md`
- `references/templates.md`
- `references/examples.md`
