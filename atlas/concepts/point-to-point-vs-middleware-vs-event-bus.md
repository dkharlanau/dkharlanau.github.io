---
layout: atlas
title: "Point-to-Point vs Middleware vs Event Bus"
permalink: /atlas/concepts/point-to-point-vs-middleware-vs-event-bus/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/synchronous-vs-asynchronous-integration/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/ipaas-middleware/
---

# Point-to-Point vs Middleware vs Event Bus

> **Status**: Skeleton — under review.  
> **Scope**: Topology comparison for SAP integration architecture.

## What it is

Three integration topologies with different coupling, scalability, and operational characteristics. Point-to-point is direct system-to-system connection. Middleware introduces a central integration layer. Event bus uses pub/sub brokers for maximum decoupling.

## Comparison

| Dimension | Point-to-Point | Middleware (iPaaS) | Event Bus |
|-----------|---------------|---------------------|-----------|
| **Topology** | Direct connection | Central hub with adapters | Pub/sub broker with topics |
| **Coupling** | Tight (N×M connections) | Medium (N+M adapters) | Loose (producer unaware of consumers) |
| **Scalability** | Poor (connection explosion) | Good (hub scales horizontally) | Excellent (consumer groups scale) |
| **Governance** | Weak (hidden dependencies) | Strong (central monitoring) | Medium (topic governance needed) |
| **SAP examples** | Direct RFC, custom proxy | SAP Integration Suite, PI/PO | SAP Event Mesh, Kafka, Advanced Event Mesh |
| **Best for** | Simple, stable, low-volume pairs | Complex transformations, protocol bridging | Multi-consumer real-time updates |
| **Risk** | Hidden dependency graph, upgrade cascade | Hub becomes single point of failure | Topic sprawl, schema drift, consumer lag |

## When to use point-to-point

- Two stable systems with simple, high-frequency, low-latency requirements
- Temporary migration bridges with known sunset dates
- Scenarios where middleware operational overhead is unjustified

## When to use middleware

- Protocol transformation required (e.g., REST to IDoc, EDI to XML)
- Complex routing, mapping, or enrichment logic
- Centralized monitoring, retry, and error handling required
- SAP Integration Suite already licensed and operational

## When to use event bus

- Multiple independent consumers need the same business event
- Real-time decoupling between operational and analytical systems
- Event sourcing or audit trail requirements
- Cloud-native architecture with microservices or sidecars

## SAP landscape fit

- **SAP PI/PO → Integration Suite**: Middleware migration path
- **SAP Event Mesh / Advanced Event Mesh**: Managed event bus on BTP
- **Cloud Connector**: Enables point-to-point hybrid connectivity
- **CAP messaging**: Native event bus abstraction for application events

## Design decisions

| Scenario | Topology | Rationale |
|----------|----------|-----------|
| S/4HANA → single WMS | Point-to-point (OData/RFC) | Simple, stable, low overhead |
| S/4HANA → 5 consumers (WMS, CRM, analytics, e-commerce, planning) | Event bus | Avoid 5×N connection explosion |
| EDI X12 → S/4HANA IDoc | Middleware (Integration Suite TPM) | Protocol transformation, partner management |
| Legacy SOAP → new REST consumers | Middleware (API Management) | Protocol bridging, rate limiting, security |

## Operational failure modes

- **Point-to-point**: Upgrade on one side breaks the other; dependency graph is invisible
- **Middleware**: Hub outage stops all traffic; adapter memory leaks; mapping errors
- **Event bus**: Topic misconfiguration causes broadcast storms; consumer group rebalance loops; retention expiry loses events

## AI/agent opportunity

- Discover hidden point-to-point connections from network and log analysis
- Recommend middleware vs event bus based on consumer count and latency requirements
- Predict topic sprawl from naming convention analysis
- Auto-generate adapter configurations from metadata

## Related Atlas pages

- [Integration Pattern Decision Matrix](/atlas/concepts/integration-pattern-decision-matrix/)
- [Synchronous vs Asynchronous Integration](/atlas/concepts/synchronous-vs-asynchronous-integration/)
- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)
- [iPaaS and Middleware](/atlas/sap/ipaas-middleware/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)

## Verification limitations

- Content is synthesized from public SAP documentation and architecture practice.
- Topology choice depends on organizational maturity and licensing.
- No private implementation details are included.
