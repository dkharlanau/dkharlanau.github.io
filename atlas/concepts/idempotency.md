---
layout: default
title: "Idempotency"
description: "Idempotency means processing the same event or request multiple times produces the same outcome as processing it once."
tags:
  - concept
  - sap-sd
  - sap-master-data
  - sap-wm
  - sap-retail
  - sap-s4hana
  - sap-integration
permalink: /atlas/concepts/idempotency/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---


# Idempotency

> **Status**: Skeleton — under review.  
> **Scope**: Idempotency patterns for SAP integration reliability.

## What it is

Idempotency means processing the same event or request multiple times produces the same outcome as processing it once. It is the pragmatic foundation for "exactly-once" semantics in at-least-once delivery systems.

## When to use it

- Event consumers in Event Mesh, Kafka, or S/4HANA Business Events
- REST API endpoints that may be retried (POST, PATCH)
- IDoc reprocessing scenarios (WE02/BD87)
- Financial postings, inventory updates, or master data replication

## When not to use it

- Read-only queries (GET) are naturally idempotent
- Append-only audit logs where duplicates are acceptable
- Scenarios where the cost of deduplication exceeds the cost of occasional duplicates

## SAP landscape fit

- **S/4HANA Business Events**: Consumers must implement idempotency; events include unique `eventId`
- **IDoc**: Status 53 (application document posted) prevents reprocessing; manual reprocess requires care
- **OData**: Use `If-Match` ETags for conditional updates; implement idempotency keys for POST
- **Cloud Integration**: Message ID can serve as idempotency key; configure duplicate check in iFlow

## Design decisions

| Pattern | Implementation | SAP Fit |
|---------|---------------|---------|
| Deduplication table | Atomic check-and-insert of event ID in consumer DB | Universal; works with any consumer |
| State-based | Only apply transition if current state allows it | S/4HANA document status workflows |
| ETag/If-Match | OData optimistic concurrency control | Fiori apps, REST APIs |
| Idempotency key | Client-generated key; server stores processed keys | Custom REST APIs, BTP CAP |

## Operational failure modes

- Missing idempotency key → duplicate records during retry storms
- Deduplication table grows unbounded → performance degradation, storage cost
- Out-of-order delivery → state-based idempotency rejects valid transitions
- Cross-tenant key collision → composite key (tenant + idempotencyKey) required

## Monitoring/support model

- Track duplicate detection rate and deduplication table size
- Monitor retry storms via API Gateway or Event Mesh metrics
- Alert on idempotency key collisions or deduplication failures

## Ownership model

- **Consumer domain**: owns idempotency implementation and deduplication storage
- **Producer domain**: owns stable unique key generation and propagation
- **Platform team**: owns monitoring and retry policy configuration

## AMS incident patterns

- Duplicate sales orders after event reprocessing → verify deduplication table and event ID stability
- Duplicate financial postings → check IDoc status 53 vs manual reprocess
- API consumer reports duplicates → validate idempotency key header and server-side storage

## AI/agent opportunity

- Detect missing idempotency patterns in consumer code during review
- Predict deduplication table growth and recommend TTL policies
- Generate idempotency key handling boilerplate for SAP event consumers
- Correlate duplicate incidents with retry storms and root cause

## Related Atlas pages

- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Business Events](/atlas/sap/business-events/)

## Source references

- [Microservices.io — Idempotent Consumer Pattern](https://microservices.io/patterns/communication/idempotent-consumer.html)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- Content is synthesized from public pattern literature and SAP documentation.
- Implementation details vary by programming language and database.
- No private implementation details are included.
