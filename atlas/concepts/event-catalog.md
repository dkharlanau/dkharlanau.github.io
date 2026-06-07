---
layout: default
title: "Event Catalog"
permalink: /atlas/concepts/event-catalog/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/sap-event-driven-architecture/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---

# Event Catalog

> **Status**: Skeleton — under review.  
> **Scope**: Event discoverability, schema registry, and governance for SAP landscapes.

## What it is

An event catalog is a centralized discoverability layer that documents every event type, its schema, ownership, producers, consumers, and lifecycle status. It connects to schema registries and AsyncAPI specifications for machine-readable contracts.

## When to use it

- Managing 50+ event types across multiple SAP and non-SAP domains
- Onboarding new consumers to existing event streams
- Enforcing naming conventions and schema governance
- Tracking event lifecycle (draft, stable, deprecated, retired)

## When not to use it

- Fewer than 10 event types with stable schemas and single consumers
- Rapid prototyping where event contracts are still evolving
- Organizations without dedicated integration governance capacity

## SAP landscape fit

- **SAP API Business Hub**: Discover S/4HANA Business Events with AsyncAPI specs
- **SAP Integration Suite, Advanced Event Mesh**: Event Portal 2.0 for topic management and discovery
- **EventCatalog (open source)**: Self-hosted option with AsyncAPI and visual diagrams
- **Confluent Schema Registry**: Runtime schema validation for Kafka-based landscapes

## Design decisions

| Component | Recommendation |
|-----------|---------------|
| Naming | `domain.subdomain.eventName` (e.g., `sales.order.created`) |
| Schema | AsyncAPI spec + JSON Schema payload |
| Ownership | Assigned team per event type with contact and SLA |
| Lifecycle | Draft → Stable → Deprecated → Retired with sunset dates |
| Discovery | Search by domain, producer, consumer, or schema field |

## Operational failure modes

- Catalog drifts out of sync with code → manual documentation abandoned
- Competing catalogs per business unit → fragmented discoverability
- Schema registry validates structure but misses semantic meaning
- Event ownership unclear → no one approves schema changes

## Monitoring/support model

- Automated catalog updates from CI/CD pipeline (AsyncAPI spec commits)
- Regular audit for orphaned events (no active producers or consumers)
- Governance review for new event types and breaking changes
- Integration with API Business Hub for SAP-native event discovery

## Ownership model

- **Integration governance team**: owns catalog platform, naming standards, and lifecycle policy
- **Event producer domains**: own event metadata, schema, and documentation accuracy
- **Consumer domains**: own subscription registration and consumer version tracking

## AMS incident patterns

- Consumer cannot find event schema → verify catalog sync and AsyncAPI spec availability
- Event type collision → enforce naming convention and domain prefix
- Deprecated event still consumed → track consumer migration and sunset enforcement
- Schema change breaks consumer → use catalog to notify registered consumers

## AI/agent opportunity

- Auto-generate catalog entries from S/4HANA Business Event metadata
- Detect orphaned events from log and subscription analysis
- Suggest event naming from domain taxonomy and existing patterns
- Generate consumer onboarding docs from catalog metadata

## Related Atlas pages

- [Event Contracts](/atlas/concepts/event-contracts/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [SAP Event-Driven Architecture](/atlas/concepts/sap-event-driven-architecture/)
- [Business Events](/atlas/sap/business-events/)

## Source references

- [EventCatalog](https://www.eventcatalog.dev)
- [AsyncAPI Specification](https://www.asyncapi.com)
- [SAP API Business Hub](https://api.sap.com)

## Verification limitations

- Event catalog tooling in SAP landscapes is evolving.
- Content is synthesized from open source and SAP documentation.
- No private implementation details are included.
