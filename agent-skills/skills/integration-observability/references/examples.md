# Integration Observability — Examples

## Good Example: Customer Orders Stop Flowing to Warehouse

**Situation:** Orders from e-commerce to SAP S/4 are processed successfully, but the warehouse file transfer from SAP to the logistics system stops. No alert fires because the file transfer job does not have monitoring.

**Business impact mapping:**
- Process: Picking list generation
- Symptom: Picking lists do not print
- Cost: $5,000 per hour of warehouse downtime

**Failure modes and detection:**
- File missing: monitor file arrival time
- File empty: monitor file size and record count
- Job failure: monitor job completion status

**Alert design:**
- AL-003: File age > 2 hours → P1 → AMS Team → Finance Manager escalation
- Threshold based on SLA: warehouse needs files by 06:00

**Runbook:**
- First check: file transfer job log
- Key logs: job scheduler, file system
- Common causes: network issue, job failure, path change
- Safe action: verify job status, check path
- Escalation: file > 4 hours missing → Finance Manager

**Why this is good:** Monitoring is tied to business outcome (picking lists), not just job completion. File size and record count detect empty files.

---

## Bad Example: Middleware Logs Show 500 Errors but No One Acts

**Situation:** The API gateway logs hundreds of 500 errors per day for a customer lookup API. The errors are visible in a dashboard but not alerted.

**Monitoring design:**
- Dashboard shows error count
- No alert threshold
- No recipient
- No runbook

**Result:** Business team assumes SAP is slow. SAP team assumes middleware is misconfigured. No one owns the alert. Real customer-facing failures are buried in noise.

**Why this is bad:**
- No alert threshold → no one is notified
- No named recipient → no accountability
- No runbook → no one knows what to check
- No business impact mapping → no one knows if this matters

**Good design:**
- Alert: error rate > 1% in 5-minute window → P1
- Recipient: AMS Lead
- Escalation: Integration Manager after 3 failures in 1 hour
- Runbook: check SM58 for tRFC errors, verify API token expiry

---

## Good Example: New Integration Launched Without Monitoring

**Situation:** A project delivers a new billing integration on time. The go-live checklist has a monitoring item marked "post-go-live." After go-live, the project team disbands. The integration runs silently for two weeks, then fails.

**Prevention:**
- Monitoring is a go-live gate, not a post-go-live task
- Alert matrix must be approved before go-live
- Runbook must be tested with simulated failure before go-live
- Operational owner must be named and trained before go-live

**Why this is good:** Monitoring is treated as part of the deliverable, not an afterthought. The operational owner is ready before the first failure.

---

## Bad Example: Alerting on Every Error

**Situation:** An integration generates 50 transient timeout errors per day during peak hours. All 50 trigger alerts.

**Result:** Alert fatigue. The AMS team creates an email filter. When a real failure occurs (100% error rate for 30 minutes), it is buried in the noise and not acted on for 2 hours.

**Why this is bad:**
- Threshold is too low (any error triggers)
- No evaluation window (single error = alert)
- No severity differentiation (transient vs sustained)
- No tuning process (alerts are never reviewed)

**Good design:**
- Threshold: error rate > 5% over 10-minute window
- P2 for sustained elevated error rate
- P1 for 100% error rate over 5 minutes
- Weekly review for first month to tune thresholds
