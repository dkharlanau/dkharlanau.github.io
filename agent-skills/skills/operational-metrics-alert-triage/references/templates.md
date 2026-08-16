# Templates

## Operational Alert Triage Record

```text
Alert:
Timestamp:
Metric / signal:
Threshold / condition:
Signal freshness:
Signal validated: yes/no

Business service / process:
Business impact:
Scope:
Duration:
Data-integrity risk:
Related signals:
Recent changes:
First suspected boundary:
Owner:

Action:
Containment / recovery:
Validation:

Alert quality:
- useful | late | noisy | duplicate | missing context | false positive
Tuning action:
Runbook update:
Monitoring owner:
```

## Alert-quality review

| Alert | Failure detected | Time to detect | Business context present | Duplicate/noisy | Owner correct | Tuning action |
|---|---|---|---|---|---|---|

## New alert definition

```text
Business outcome protected:
Signal:
Threshold / condition:
Evaluation window:
Severity logic:
Dependencies / correlation:
Owner:
Runbook:
Suppression / deduplication:
Validation test:
```
