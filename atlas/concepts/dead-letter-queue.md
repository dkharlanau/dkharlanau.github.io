---
layout: default
title: "Dead Letter Queue"
description: "A Dead Letter Queue (DLQ) is a secondary queue that receives messages after they have failed processing in the primary queue beyond a configured max retry."
tags:
  - concept
  - sap-sd
  - ai-operations
  - integration
  - data-architecture
permalink: /atlas/concepts/dead-letter-queue/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/business-events/
---


# Dead Letter Queue

> **Status**: Skeleton — under review.  
> **Scope**: DLQ patterns for SAP event-driven and messaging integrations.

## What it is

A Dead Letter Queue (DLQ) is a secondary queue that receives messages after they have failed processing in the primary queue beyond a configured max retry limit. It isolates poison-pill messages so they do not block healthy messages.

## When to use it

- Event consumers in SAP Event Mesh or Advanced Event Mesh
- Cloud Integration iFlows with JMS or AMQP queues
- Kafka consumers with retry topics and final dead-letter topic
- Any asynchronous integration where poison messages could block processing

## When not to use it

- Synchronous HTTP APIs where immediate error response is preferred
- Low-volume, manually monitored queues where direct inspection suffices
- Scenarios where message loss is preferable to operational complexity

## SAP landscape fit

- **SAP Event Mesh**: Supports DLQ configuration per queue; messages moved after max redelivery
- **Advanced Event Mesh**: Enhanced DLQ with replay capabilities and longer retention
- **Cloud Integration**: JMS adapter supports dead letter queue configuration
- **Kafka**: Not native; implement via retry topics and final dead-letter topic manually

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Max retries | 3-5 attempts with exponential backoff |
| DLQ retention | Longer than source queue (e.g., 14 days vs 7 days) |
| Alerting | Alert on DLQ depth > 0 and message age > 1 hour |
| Redrive | Manual inspection → fix root cause → replay or discard |
| Audit | Log all DLQ insertions with failure reason and original trace ID |

## Operational failure modes

- DLQ becomes a graveyard → no operational process to inspect and replay
- Retention shorter than investigation time → messages expire before root cause found
- DLQ depth grows silently → systemic consumer bug or downstream outage
- Replay without fixing root cause → message returns to DLQ immediately

## Monitoring/support model

- Monitor DLQ depth, message age, and insertion rate
- Classify DLQ messages by error type (schema, downstream, timeout, auth)
- Establish SLA for DLQ inspection (e.g., 4 hours for production)
- Maintain runbook for common DLQ scenarios and redrive procedures

## Ownership model

- **Consumer domain**: owns DLQ processing, classification, and redrive
- **Platform team**: owns DLQ infrastructure, retention, and alerting
- **Producer domain**: owns schema correctness and payload validation

## AMS incident patterns

- DLQ depth spikes after deployment → check for schema change or consumer version mismatch
- Message stuck in DLQ with schema error → verify producer schema registry and consumer version
- DLQ message with downstream 503 → wait for backend recovery, then redrive
- Auth error in DLQ → check consumer credentials and permission changes

## AI/agent opportunity

- Auto-classify DLQ messages by failure pattern and suggest remediation
- Predict DLQ growth from deployment and schema change events
- Generate redrive commands with safety checks (idempotency verified)
- Correlate DLQ spikes with upstream changes and alert proactively

## Related Atlas pages

- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Idempotency](/atlas/concepts/idempotency/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [Integration Monitoring and Reliability Map](/atlas/maps/integration-monitoring-reliability-map/)

## Source references

- [AWS SQS Dead Letter Queues Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- DLQ capabilities vary by SAP product edition and broker type.
- Content is synthesized from public documentation and operations practice.
- No private implementation details are included.
