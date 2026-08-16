# Method

Treat an alert as an input to diagnosis, not as the diagnosis itself.

## Signal layers
Use several layers when relevant:
- infrastructure: CPU, memory, storage, node availability;
- service: latency, error rate, throughput, saturation;
- integration: failed messages, retry count, queue depth, age;
- business process: blocked orders, delayed confirmations, rejected invoices;
- data quality: duplicates, unmatched keys, rejected rows, reconciliation gaps.

## Triage sequence
1. confirm signal freshness and validity;
2. identify business outcome at risk;
3. define scope and duration;
4. correlate related signals and recent changes;
5. assign urgency;
6. route to the first suspected failing boundary;
7. act and validate;
8. assess alert quality;
9. tune monitoring.

## Alert quality
Useful alerts tell the operator what is wrong enough to choose a next step. Record whether an alert was early, late, noisy, duplicate, false-positive, or missing context.

## Tuning
Possible actions include threshold adjustment, time-window aggregation, deduplication, dependency correlation, business context enrichment, owner correction, runbook linking, or adding a missing outcome metric.

Do not tune an alert merely to make a dashboard quieter while the underlying failure remains poorly detected.
