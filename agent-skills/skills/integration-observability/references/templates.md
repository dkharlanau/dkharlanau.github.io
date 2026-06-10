# Integration Observability — Templates

## Template 1: Alert Matrix

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
| AL-002 | SAP→WH IDoc | Status 51 | IDoc status | Status 51 count | > 0 | 15 min | P2 | <name> | <name> | RB-002 |
| AL-003 | Bank→SAP File | File missing | File arrival | File age | > 2h | 1h | P1 | <name> | <name> | RB-003 |
| AL-004 | Event: OrderConfirmed | Consumer lag | Kafka lag | Lag per partition | > 10,000 | 5 min | P2 | <name> | <name> | RB-004 |

## Runbook index

| Runbook ID | Alert IDs | First Check | Key Transactions / Logs | Common Causes | Safe Actions | Escalation Criteria |
|------------|-----------|-------------|---------------------------|---------------|--------------|---------------------|
| RB-001 | AL-001 | Middleware health dashboard | API gateway logs, SAP SM58 | Auth expiry, SAP overload | Check SM58, verify token | > 3 failures in 1h |
| RB-002 | AL-002 | BD87 / WE02 for status 51 | IDoc content, segment details | Data validation, missing mapping | Review IDoc, check AIF | > 10 IDocs stuck |
| RB-003 | AL-003 | File transfer job log | Job scheduler, file system | Network issue, job failure | Verify job status, check path | File > 4h missing |
| RB-004 | AL-004 | Kafka consumer group lag | Consumer metrics, logs | Consumer down, slow processing | Check consumer health, restart | Lag growing > 1h |

## Review log
| Date | Action | Owner |
|------|--------|-------|
| <date> | Initial creation | <name> |
```

## Template 2: Diagnostic Runbook

```markdown
---
artifact: Diagnostic Runbook
id: RB-001
date: YYYY-MM-DD
alert: AL-001
---

## Alert
<!-- Alert name and condition -->

## First check
<!-- What to check first when this alert fires -->

## Key transactions / logs
<!-- SAP transactions, middleware dashboards, log files -->

## Common causes
1. <cause>
2. <cause>
3. <cause>

## Safe actions
<!-- What the first responder can do without escalation -->

## Escalation criteria
<!-- When to escalate and to whom -->

## Related runbooks
<!-- Links to related runbooks -->
```

## Template 3: Monitoring Configuration Specification

```markdown
---
artifact: Monitoring Configuration Specification
id: MCS-001
date: YYYY-MM-DD
---

## Interface

| Interface ID | Metric | Threshold | Window | Severity | Recipient | Runbook |
|--------------|--------|-----------|--------|----------|-----------|---------|
| <ID> | <metric> | <threshold> | <window> | <severity> | <name> | <runbook> |

## Dashboard definition
- Refresh rate: <frequency>
- Audience: <who views this>
- Layout: <what to display>

## Alert routing
- P1: <routing>
- P2: <routing>
- P3: <routing>
```

## Template 4: Integration Health Dashboard Definition

```markdown
---
artifact: Integration Health Dashboard
id: IHD-001
date: YYYY-MM-DD
---

## Purpose
<!-- What this dashboard shows and who uses it -->

## Technical indicators
- <metric 1>
- <metric 2>

## Business outcome indicators
- <indicator 1>
- <indicator 2>

## Refresh rate
<!-- How often the dashboard updates -->

## Audience
<!-- Who views this dashboard -->
```
