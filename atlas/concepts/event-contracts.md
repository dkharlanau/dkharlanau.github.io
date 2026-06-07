---
layout: atlas
title: "Event Contracts"
permalink: /atlas/concepts/event-contracts/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/api-contracts/
  - /atlas/concepts/data-contracts/
  - /atlas/concepts/event-catalog/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---

# Event Contracts

> **Status**: Skeleton — under review.  
> **Scope**: Schema, versioning, and governance for event-driven integrations in SAP landscapes.

## What it is

An event contract defines the schema, semantics, and versioning rules for every event that crosses a service boundary. It specifies the event envelope (CloudEvents attributes), payload schema, required/optional fields, and compatibility guarantees.

## When to use it

- Publishing Business Events from S/4HANA to multiple consumers
- Defining AsyncAPI specifications for SAP Event Mesh topics
- Enforcing schema validation at the broker or consumer level
- Migrating from custom event formats to CloudEvents standard

## When not to use it

- Single-producer, single-consumer, tightly coupled event flows where informal agreement suffices
- Legacy IDoc scenarios where the format is fixed by industry standard
- Rapid prototyping phases where schema stability is not yet achievable

## SAP landscape fit

- **S/4HANA Business Events**: Emit CloudEvents 1.0-compliant events via Enterprise Event Enablement
- **SAP Event Mesh / Advanced Event Mesh**: Supports CloudEvents envelope and custom payload schemas
- **CAP**: `messaging.format: "cloudevents"` auto-populates mandatory headers
- **Kyma Eventing**: Converts legacy events to CloudEvents automatically

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Envelope standard | CloudEvents 1.0 for cross-platform interoperability |
| Schema format | AsyncAPI for documentation; JSON Schema for validation |
| Naming convention | `domain.subdomain.eventName` (e.g., `sales.order.created`) |
| Versioning | Semantic versioning for schema; major version in event type |
| Compatibility | Tolerant reader pattern: ignore unknown fields, supply defaults |

## Operational failure modes

- Schema evolution breaks consumer deserialization → consumer lag or DLQ accumulation
- Missing mandatory CloudEvents attribute → broker rejection or routing failure
- Event type typo → subscription mismatch, silent message loss
- Payload too large (>30MB for AEM) → broker rejection

## Monitoring/support model

- Schema registry validation logs (Confluent, Apicurio)
- Event Mesh queue depth and consumer lag metrics
- AsyncAPI linting in CI/CD pipeline
- Event catalog for discoverability and ownership tracking

## Ownership model

- **Event producer domain**: owns schema, versioning, and lifecycle
- **Event broker/platform team**: owns infrastructure, retention, and access control
- **Consumer domains**: own subscription management, idempotency, and retry logic

## AMS incident patterns

- Consumer stops processing → check schema registry compatibility, consumer version, and DLQ depth
- Event loss → verify producer daemon user authorization and event binding configuration
- Duplicate processing → validate idempotency key implementation and deduplication table
- Lag spike → review consumer throughput, batch size, and downstream latency

## AI/agent opportunity

- Auto-generate AsyncAPI specs from S/4HANA Business Event metadata
- Detect schema drift between producer and consumer repositories
- Suggest event naming conventions from domain taxonomy
- Generate consumer boilerplate with built-in idempotency and retry

## Related Atlas pages

- [API Contracts](/atlas/concepts/api-contracts/)
- [Data Contracts](/atlas/concepts/data-contracts/)
- [Event Catalog](/atlas/concepts/event-catalog/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Business Events](/atlas/sap/business-events/)

## Source references

- [CloudEvents Specification](https://cloudevents.io)
- [AsyncAPI Specification](https://www.asyncapi.com)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- CloudEvents adoption in SAP landscapes is growing but not universal.
- AsyncAPI tooling maturity lags behind OpenAPI.
- Content is synthesized from public standards and SAP documentation.
