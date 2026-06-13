---
layout: default
title: "Retry and Error Handling"
description: "Retry and error handling patterns ensure transient failures (network timeouts, temporary unavailability) are recovered automatically while permanent failures."
tags:
  - concept
  - sap-integration
  - ai-operations
  - integration
  - data-architecture
permalink: /atlas/concepts/retry-and-error-handling/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/concepts/integration-ownership-model/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
  - /atlas/sap/business-events/
---


# Retry and Error Handling

> **Status**: Skeleton — under review.  
> **Scope**: Retry policies, circuit breakers, and error handling for SAP integrations.

## What it is

Retry and error handling patterns ensure transient failures (network timeouts, temporary unavailability) are recovered automatically while permanent failures (bad requests, authentication errors) fail fast. Circuit breakers prevent cascading overload.

## When to use it

- Cloud Integration iFlows calling external APIs
- Event consumers processing messages from Event Mesh
- IDoc reprocessing after temporary partner system outage
- OData calls from Fiori apps or external consumers

## When not to use it

- Permanent errors (400 Bad Request, 401 Unauthorized) should not be retried
- Financial postings where duplicate risk from retry exceeds manual recovery cost
- Real-time user-facing paths where retry latency degrades experience

## SAP landscape fit

- **Cloud Integration**: Built-in retry with exponential backoff; configurable max retries and interval
- **Event Mesh**: Consumer retry with DLQ after max attempts
- **IDoc**: Manual reprocess via BD87; status 51 requires correction before retry
- **OData**: Gateway timeout handling; client-side retry with idempotency key

## Design decisions

| Pattern | Behavior | SAP Fit |
|---------|----------|---------|
| Exponential backoff | Double wait interval between retries (100ms → 200ms → 400ms) | Cloud Integration, custom consumers |
| Jitter | Add random variance to prevent thundering herd | High-volume consumers, Kafka |
| Circuit breaker | Open after threshold failures; fast-fail for cooldown period | External API calls, BTP CAP |
| Retry budget | Limit retry traffic to ≤10% of total | Google SRE pattern; custom implementation |
| DLQ | Route failed messages after max retries for manual inspection | Event Mesh, SQS, Kafka |

## Operational failure modes

- Uncapped exponential backoff → 64s → 128s → 256s delays; always set max ceiling (30-60s)
- Retrying non-idempotent POST → duplicate side effects
- Circuit breaker too sensitive → unnecessary fast-fails during brief blips
- Missing DLQ → poison messages block entire queue

## Monitoring/support model

- Track retry rate, DLQ depth, and circuit breaker state
- Monitor API error rate by status code (5xx vs 4xx)
- Alert on DLQ growth and message age
- Log correlation IDs for end-to-end traceability

## Ownership model

- **Consumer domain**: owns retry logic, idempotency, and DLQ processing
- **Producer domain**: owns error response clarity and status code correctness
- **Platform team**: owns circuit breaker configuration and broker health

## AMS incident patterns

- iFlow repeatedly fails with 503 → check backend health and circuit breaker state
- Event consumer lag grows → verify retry loop is not stuck on poison message
- IDoc status 51 after retry → fix application error before reprocess
- OAuth 401 after token refresh → check clock skew and certificate validity

## AI/agent opportunity

- Classify errors as transient vs permanent from status code and payload patterns
- Recommend optimal retry parameters from historical success rates
- Auto-generate DLQ processing runbooks from error type distributions
- Predict circuit breaker trips from latency trend analysis

## Related Atlas pages

- [Idempotency](/atlas/concepts/idempotency/)
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/)
- [Integration Monitoring and Reliability Map](/atlas/maps/integration-monitoring-reliability-map/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- Content is synthesized from public SAP documentation and SRE practice.
- Retry behavior varies by SAP product and configuration.
- No private implementation details are included.
