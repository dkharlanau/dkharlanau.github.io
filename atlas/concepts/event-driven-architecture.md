---
layout: atlas
title: "Event-Driven Architecture"
permalink: /atlas/concepts/event-driven-architecture/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/event-catalog/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---

# Event-Driven Architecture

> **Status**: Skeleton — under review.  
> **Scope**: Event-driven patterns, standards, and operational concerns for enterprise landscapes.

## What it is

Event-Driven Architecture (EDA) replaces synchronous request-response chains with asynchronous event publication and subscription. Producers emit facts about state changes; consumers react independently. Brokers act as shock absorbers, decoupling producers from consumer availability.

## When to use it

- Multiple independent services need to react to the same business occurrence
- Real-time decoupling between operational and analytical systems
- High-volume scenarios where synchronous coupling would create bottlenecks
- Event sourcing or audit trail requirements

## When not to use it

- Simple CRUD or request-response workflows where async adds unnecessary complexity
- Scenarios requiring immediate consistency guarantees across distributed systems
- Low-volume, stable, bilateral integrations where middleware overhead is unjustified
- Teams without operational capacity to manage brokers, consumer lag, and DLQs

## Core patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| Event Notification | Lightweight signal that something happened | Inventory changed, order placed |
| Event-Carried State Transfer | Event includes full entity state | Material master replication |
| Event Sourcing | Complete event log is system of record | Audit-heavy compliance systems |
| CQRS | Separate read and write models via events | High-read analytical projections |

## Standards

- **CloudEvents**: CNCF standard event envelope (id, source, type, time, specversion)
- **AsyncAPI**: OpenAPI equivalent for event-driven APIs; describes channels, operations, messages
- **OpenTelemetry**: Distributed tracing across producer, broker, and consumer boundaries

## Operational concerns

- **Idempotency**: Consumers must handle duplicate events gracefully
- **Retry**: Exponential backoff with jitter; circuit breakers for cascading failures
- **DLQ**: Isolate poison messages after max retries
- **Replay**: Reset consumer offsets for recovery (Kafka); not available in queue-based brokers
- **Observability**: Trace IDs propagated through message headers; consumer lag metrics

## SAP landscape fit

- **S/4HANA Business Events**: CloudEvents-compliant events for key object changes
- **SAP Event Mesh**: Managed AMQP broker on BTP for SAP-native pub/sub
- **Advanced Event Mesh**: Enterprise-grade with multi-cloud deployment, replay, and larger payloads
- **CAP**: Native CloudEvents formatting and messaging abstraction
- **Kyma Eventing**: Automatic CloudEvents conversion for legacy event sources

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Broker | Kafka for high-throughput replay; Event Mesh for SAP-native simplicity |
| Envelope | CloudEvents 1.0 for cross-platform interoperability |
| Schema | AsyncAPI + JSON Schema; register in schema registry |
| Consumer | Idempotent, tolerant reader, with retry and DLQ |
| Ordering | Partition by entity key; accept eventual ordering across partitions |

## Operational failure modes

- Silent event loss due to misconfigured bindings or daemon user auth
- Consumer lag grows unbounded due to slow processing or poison messages
- Schema evolution breaks consumers without versioning
- Replay from beginning takes hours for large topics

## AI/agent opportunity

- Auto-generate AsyncAPI specs from event metadata
- Detect schema drift between producer and consumer code
- Predict consumer lag from throughput trends
- Classify poison messages and suggest remediation

## Related Atlas pages

- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Event Contracts](/atlas/concepts/event-contracts/)
- [Event Catalog](/atlas/concepts/event-catalog/)
- [Idempotency](/atlas/concepts/idempotency/)
- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/)
- [Event-Driven Architecture Map](/atlas/maps/event-driven-architecture-map/)

## Source references

- [CloudEvents Specification](https://cloudevents.io)
- [AsyncAPI Specification](https://www.asyncapi.com)
- [OpenTelemetry Documentation](https://opentelemetry.io/docs)

## Verification limitations

- EDA adoption in SAP landscapes is growing but not universal.
- Content is synthesized from public standards and SAP documentation.
- No private implementation details are included.
