---
name: integration-observability
description: Use when business users report missing data before any technical alert fires, when middleware logs show errors but no one reviews them, or when a new integration is going live without monitoring. Produces an Alert Matrix and diagnostic runbooks. Do not use for general system monitoring or infrastructure capacity planning.
---

# Integration Observability

## Purpose

Build monitoring that catches integration failures before business impact, and create diagnostic runbooks so the first responder knows exactly what to check.

## Use when

- A new integration is going live and monitoring is "to be defined later."
- Business users report missing data before any technical alert fires.
- Middleware logs show errors but no one reviews them until a business escalation.
- An AMS handover requires operational documentation for existing integrations.
- A middleware or platform upgrade changes logging and alerting behavior.
- SLAs are being defined and you need to prove they can be monitored.

## Do not use when

- The problem is general system or infrastructure monitoring (CPU, memory, disk) with no integration dimension.
- You are designing the integration itself (use API design or event-driven architecture skills).
- You need a high-level observability strategy without specific interfaces to monitor.

## Required inputs

- Interface inventory with ownership matrix.
- SLA requirements: availability, latency, throughput, freshness.
- Middleware monitoring capabilities: dashboards, metrics, log aggregation.
- SAP monitoring tools and transactions: SM58, SMQ1, SMQ2, BD87, WE02, SXI_MONITOR, AIF.
- Alerting infrastructure: email, SMS, paging, ticketing integration.
- Runbook templates or existing operational documentation.
- Business impact mapping: which processes fail when each interface fails.
- Historical incident data: how past failures were detected and resolved.

## Workflow

1. **Map each interface to business impact.** For every interface, document the business process affected, the symptom of failure, and the cost or risk per hour of downtime.
2. **Define failure modes per interface.** List the ways this interface can fail: timeout, schema mismatch, auth failure, data validation error, rate limit, downstream unavailable, silent data loss.
3. **Choose detection method per failure mode.** Match the failure to a detectable signal: HTTP status code, queue depth, IDoc status, file absence, data volume anomaly, latency spike.
4. **Set alert thresholds.** Define the metric, threshold, evaluation window, and severity. Base thresholds on SLA and historical baseline, not guesswork.
5. **Assign alert recipients.** Each alert goes to a named person or team with accountability, not a broad distribution list.
6. **Create diagnostic runbook per alert.** For each alert, write: what to check first, which transactions or logs to open, common causes, escalation criteria, and safe actions.
7. **Test alert with simulated failure.** Trigger each failure mode in a controlled way. Verify the alert fires, the recipient receives it, and the runbook leads to diagnosis.
8. **Review weekly for the first month after go-live.** Tune thresholds, fix false positives, and update runbooks based on real incidents.

## Decision rules

- If business impact exceeds $10,000 per hour, alert within 5 minutes of failure detection.
- If the failure is silent (no error code), use data volume, latency, or freshness anomaly detection.
- If SAP is involved, monitor SM58 (tRFC errors), SMQ1/SMQ2 (qRFC queues), BD87/WE02 (IDoc status), and AIF errors.
- If middleware is involved, monitor queue depth, error rate, latency, and consumer lag.
- If an alert fires more than three times per week without action, tune the threshold or fix the root cause.
- If no runbook exists for an alert, create one before the interface goes live.
- If an alert goes to a distribution list with more than five people, replace it with a named owner and an escalation path.
- If a file transfer is involved, monitor file arrival time, file size, and record count, not just job completion.

## Output format

Produce an **Alert Matrix** and **Diagnostic Runbooks**:

```markdown
---
artifact: Alert Matrix
id: ALM-001
date: YYYY-MM-DD
scope: Integration landscape | Project | Domain
---

## Alert definitions

| Alert ID | Interface | Failure Mode | Detection Method | Metric | Threshold | Window | Severity | Recipient | Escalation | Runbook |
|----------|-----------|--------------|------------------|--------|-----------|--------|----------|-----------|------------|---------|
| AL-001 | SAP→CRM Customer API | Timeout / 5xx | HTTP status | Error rate | > 1% | 5 min | P1 | <name> | <name> | RB-001 |

## Runbook index

| Runbook ID | Alert IDs | First Check | Key Transactions / Logs | Common Causes | Safe Actions | Escalation Criteria |
|------------|-----------|-------------|---------------------------|---------------|--------------|---------------------|
| RB-001 | AL-001 | Middleware health dashboard | API gateway logs, SAP SM58 | Auth expiry, SAP overload | Check SM58, verify token | > 3 failures in 1h |

## Review log
| Date | Action | Owner |
|------|--------|-------|
| <date> | Initial creation | <name> |
```

Also produce a **Monitoring Configuration Specification** and an **Integration Health Dashboard Definition**.

## Quality gates

- [ ] Every critical interface has at least one alert.
- [ ] Every alert has a defined threshold and evaluation window.
- [ ] Every alert has a named recipient with accountability.
- [ ] A runbook exists for every alert that pages outside business hours.
- [ ] False positive rate is under 20% after the first month.
- [ ] Business impact is documented per interface.
- [ ] Simulated failure test confirmed alert delivery and runbook accuracy.
- [ ] Dashboard shows both technical health and business outcome indicators.

## References

- `references/method.md` — Detailed failure mode analysis, threshold tuning, and runbook writing.
- `references/templates.md` — Copy-ready templates for Alert Matrix, Runbook, and Dashboard Definition.
- `references/examples.md` — Good and bad examples from SAP IDoc monitoring, file transfer, and API gateway contexts.

## Safety rules

- Separate facts from assumptions. Label assumptions about baseline metrics and SLA values.
- Separate decisions from open questions. List open questions about monitoring infrastructure gaps.
- Do not expose client names, vendor names, or proprietary SLA terms.
- Do not copy proprietary framework text. Use your own words.
