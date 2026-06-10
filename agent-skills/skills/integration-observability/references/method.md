# Integration Observability — Detailed Method

## The Business-First Monitoring Method

Integration monitoring fails when it only watches middleware health. This method maps each interface to business impact first, then defines failure modes, detection methods, and runbooks.

### Step 1: Business Impact Mapping

For every interface, document:
- **Business process affected:** which process stops or slows when this interface fails
- **Symptom of failure:** what business users will observe
- **Cost or risk per hour:** quantified business impact

Example:
- Interface: SAP → Warehouse file transfer
- Process: Picking list generation
- Symptom: Picking lists do not print
- Cost: $5,000 per hour of warehouse downtime

### Step 2: Failure Mode Definition

List the ways this interface can fail:
- **Timeout:** no response within expected time
- **Schema mismatch:** sender and receiver disagree on format
- **Auth failure:** credentials expired or misconfigured
- **Data validation error:** payload contains invalid data
- **Rate limit:** sender exceeds receiver capacity
- **Downstream unavailable:** target system is down
- **Silent data loss:** messages appear successful but data is missing

For each failure mode, document the business symptom.

### Step 3: Detection Method Selection

Match each failure mode to a detectable signal:

| Failure Mode | Detection Method | SAP Transaction / Tool |
|--------------|------------------|------------------------|
| Timeout | HTTP status, latency spike | SM58 (tRFC errors) |
| Schema mismatch | Error rate, validation failure | WE02/WE05 (IDoc status 51) |
| Auth failure | HTTP 401/403, connection errors | SM58, API gateway logs |
| Data validation error | IDoc status 51, queue errors | BD87, AIF |
| Rate limit | Queue depth, consumer lag | SMQ1/SMQ2 |
| Downstream unavailable | Connection errors, timeout | SM58, middleware health |
| Silent data loss | Data volume anomaly, freshness | Custom volume check, file size |

### Step 4: Alert Threshold Setting

For each alert, define:
- **Metric:** what is measured
- **Threshold:** the value that triggers the alert
- **Evaluation window:** how long the threshold must be exceeded
- **Severity:** P1, P2, P3, P4
- **Recipient:** named person or team

Base thresholds on:
- SLA requirements
- Historical baseline (at least 30 days of data)
- Business impact (higher impact = lower threshold)

Avoid guesswork. If no baseline exists, start with a conservative threshold and tune after one week.

### Step 5: Runbook Creation

For each alert that pages outside business hours, create a runbook with:
- **First check:** what to look at first
- **Key transactions or logs:** which SAP transactions, middleware dashboards, or log files
- **Common causes:** the top 3 causes of this alert
- **Safe actions:** what the first responder can do without escalation
- **Escalation criteria:** when to escalate and to whom

### Step 6: Simulated Failure Testing

Trigger each failure mode in a controlled way:
1. Verify the alert fires
2. Verify the recipient receives it
3. Verify the runbook leads to correct diagnosis
4. Verify the safe action does not cause additional harm

Document test results and update thresholds or runbooks based on findings.

### Step 7: Post-Go-Live Review

For the first month after go-live:
- Review alerts weekly
- Tune false positives
- Update runbooks based on real incidents
- Verify business impact mapping is still accurate

## Common Observability Pitfalls

1. **Monitoring middleware health only, not business outcome.** The queue is healthy but no messages are flowing.
2. **Alerting on every error without threshold tuning.** Alert fatigue buries real failures.
3. **No runbook, so the recipient does not know what to do.** Alerts are acknowledged and ignored.
4. **Alert goes to a distribution list with no accountability.** Everyone assumes someone else will handle it.
5. **Monitoring job completion but not file content or record count.** Empty files or truncated transfers go undetected.
