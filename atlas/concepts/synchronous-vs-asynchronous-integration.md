---
layout: default
title: "Synchronous vs Asynchronous Integration"
permalink: /atlas/concepts/synchronous-vs-asynchronous-integration/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/point-to-point-vs-middleware-vs-event-bus/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/retry-and-error-handling/
---

# Synchronous vs Asynchronous Integration

> **Status**: Skeleton — under review.  
> **Scope**: Coupling and latency trade-offs in SAP integration design.

## What it is

Synchronous integration blocks the caller until the receiver responds. Asynchronous integration decouples producer and consumer through queues, topics, or batch files. Event-driven integration is a specialized form of async using pub/sub brokers.

## Comparison

| Dimension | Synchronous | Asynchronous | Event-Driven |
|-----------|-------------|--------------|--------------|
| **Response time** | Immediate (blocking) | Deferred (queued) | Near-realtime (pub/sub) |
| **Coupling** | Tight (caller waits) | Loose (queue buffers) | Very loose (topic broadcast) |
| **Scalability** | Limited by backend throughput | High (queue absorbs spikes) | High (consumer groups scale) |
| **Failure impact** | Immediate user-visible error | Queue backlog, eventual retry | Consumer lag, DLQ accumulation |
| **SAP examples** | OData read, SOAP call, RFC | IDoc, qRFC, batch jobs | Business Events, Event Mesh |
| **Best for** | User queries, real-time validation | Reliable delivery, high volume | Multi-consumer real-time updates |
| **Risk** | Cascading failure, timeout chains | Queue overflow, retry storms | Silent consumer failure, schema drift |

## When to use synchronous

- Fiori app fetching master data or transactional records
- Real-time credit check during sales order creation
- OAuth token validation and user authorization checks

## When to use asynchronous

- High-volume material master replication across systems
- End-of-day financial posting consolidation
- B2B EDI invoice exchange with acknowledgment requirements

## When to use event-driven

- Inventory update broadcast to WMS, e-commerce, and planning
- Business partner change notification to CRM and analytics
- Transport status update to multiple logistics consumers

## SAP landscape fit

- **S/4HANA OData**: Synchronous reads; async via batch changesets or events
- **IDoc/ALE**: Inherently async with status tracking and retry
- **Event Mesh**: Async pub/sub with AMQP 1.0 and REST APIs
- **Cloud Integration**: Supports both sync (HTTP) and async (JMS, AMQP) patterns

## Design decisions

| Scenario | Pattern | Rationale |
|----------|---------|-----------|
| User clicks "Save" and needs confirmation | Synchronous | Immediate feedback required |
| Nightly pricing update to 10 subsidiaries | Asynchronous (batch) | High volume, no immediate need |
| Stock change triggers WMS + e-commerce + analytics | Event-driven | Multiple consumers, real-time need |
| Payment authorization from external gateway | Synchronous with timeout | Financial risk, need immediate answer |

## Operational failure modes

- **Synchronous**: Timeout cascades, thread pool exhaustion, backend overload
- **Asynchronous**: Queue depth explosion, poison messages blocking processing, disk full
- **Event-driven**: Consumer group rebalance storms, partition skew, offset lag

## AI/agent opportunity

- Predict queue depth spikes from historical patterns
- Auto-tune consumer concurrency based on lag metrics
- Classify poison messages and route to DLQ with enrichment
- Recommend sync-to-async migration candidates from call frequency analysis

## Related Atlas pages

- [Integration Pattern Decision Matrix](/atlas/concepts/integration-pattern-decision-matrix/)
- [Point-to-Point vs Middleware vs Event Bus](/atlas/concepts/point-to-point-vs-middleware-vs-event-bus/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- Content is synthesized from public SAP documentation and architecture practice.
- Actual latency depends on network, payload, and system load.
- No private implementation details are included.
