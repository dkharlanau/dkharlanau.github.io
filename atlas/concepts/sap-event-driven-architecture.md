---
layout: default
title: "SAP Event-Driven Architecture"
permalink: /atlas/concepts/sap-event-driven-architecture/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/event-driven-architecture-map/
  - /atlas/concepts/event-driven-architecture/
  - /atlas/concepts/event-contracts/
  - /atlas/concepts/event-catalog/
  - /atlas/concepts/idempotency/
  - /atlas/concepts/retry-and-error-handling/
  - /atlas/concepts/dead-letter-queue/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-integration-suite/
---

# SAP Event-Driven Architecture

> **Status**: Skeleton — under review.  
> **Scope**: SAP-specific event-driven architecture patterns, capabilities, and operational guidance.

## What it is

SAP Event-Driven Architecture leverages S/4HANA Business Events, SAP Event Mesh, and CloudEvents standards to enable real-time, decoupled integration between SAP and non-SAP systems. It is SAP's strategic direction for modern, cloud-native integration.

## When to use it

- Real-time inventory updates to warehouse management and e-commerce
- Business partner changes propagated to CRM, analytics, and external systems
- Financial posting notifications to consolidation and tax systems
- Decoupling S/4HANA from microservices and sidecar applications on BTP

## When not to use it

- Scenarios requiring synchronous confirmation (e.g., credit check during order creation)
- Legacy ECC landscapes without Enterprise Event Enablement or Event Add-on
- Low-volume, stable, bilateral integrations where IDoc or batch is sufficient
- Teams without broker operational capacity

## SAP capabilities

| Component | Capability | Notes |
|-----------|-----------|-------|
| S/4HANA Business Events | 600+ CloudEvents-compliant events | BusinessPartner.Created, SalesOrder.Changed, etc. |
| Enterprise Event Enablement | RAP-based event emission | ABAP Development Tools for consumer generation |
| SAP Event Mesh | Managed AMQP broker on BTP | Queues, topics, webhooks; 1MB/10GB limits |
| Advanced Event Mesh | Enterprise-grade successor | Multi-cloud, 30MB messages, 6TB spool, replay |
| CAP Messaging | Native CloudEvents support | `messaging.format: "cloudevents"` |
| Kyma Eventing | Automatic CloudEvents conversion | Legacy event normalization |

## EDA readiness checklist

| Check | Requirement | SAP Implementation |
|-------|-------------|-------------------|
| Event owner | Named team per event type | Domain team in event catalog |
| Event contract | Schema, versioning, compatibility | AsyncAPI + JSON Schema; CloudEvents envelope |
| Schema/versioning | Semantic versioning; tolerant reader | Major version in event type; optional fields additive |
| Idempotent consumer | Deduplication or state-based check | Check `eventId` in consumer database |
| Retry policy | Exponential backoff with max ceiling | Cloud Integration or consumer code |
| DLQ | Poison message isolation after max retries | Event Mesh DLQ; custom Kafka dead-letter topic |
| Observability | Consumer lag, broker metrics, distributed tracing | Event Mesh dashboard; OpenTelemetry trace context |
| Replay | Reprocess events for recovery | Advanced Event Mesh replay; Kafka offset reset |
| Security | AuthZ, encryption, audit | OAuth2, TLS, SAP BTP Destination service |
| Auditability | Event log for compliance | Broker retention logs; application audit tables |

## Design decisions

| Decision | SAP Recommendation |
|----------|-------------------|
| Event payload | Notification-only (lightweight) vs state transfer (full entity) |
| Consumer generation | ABAP Development Tools from AsyncAPI specs in API Business Hub |
| Broker choice | Event Mesh for BTP-centric; Advanced Event Mesh for hybrid/multi-cloud |
| Error handling | DLQ after 3-5 retries; manual inspection and redrive |
| Monitoring | Event Mesh dashboard + OpenTelemetry trace propagation |

## Operational failure modes

- Custom events require ABAP development and daemon-user authorization; misconfiguration causes silent loss
- Event payloads may be shallow (notification-only) or deep (full entity); consumers must handle both
- Event Mesh 1.0 limits (1MB message, 10GB spool) may be exceeded by large state-transfer events
- Event Portal 1.0 reached end of support March 2025; migrate to Event Portal 2.0

## Monitoring/support model

- Event Mesh dashboard: queue depth, consumer lag, message rates
- OpenTelemetry traces propagated through CloudEvents extensions
- AsyncAPI validation in CI/CD for schema compliance
- Event catalog for ownership, discoverability, and lifecycle tracking

## Ownership model

- **Domain team**: owns event definition, schema, and producer configuration
- **Integration platform team**: owns Event Mesh infrastructure, security, and governance
- **Consumer teams**: own subscription management, idempotency, retry, and DLQ processing

## AMS incident patterns

- Events not emitted → check RAP business object event linkage and daemon user
- Consumer lag spike → verify processing throughput, batch size, and downstream latency
- DLQ accumulation → classify by schema error, downstream failure, or auth issue
- Duplicate processing → validate idempotency key handling in consumer

## AI/agent opportunity

- Auto-generate event consumers from AsyncAPI specifications
- Predict event volume spikes from business calendar patterns
- Detect schema drift between S/4HANA release upgrades and consumer versions
- Generate event catalog entries from RAP business object metadata

## Related Atlas pages

- [Event-Driven Architecture](/atlas/concepts/event-driven-architecture/)
- [Event Contracts](/atlas/concepts/event-contracts/)
- [Event Catalog](/atlas/concepts/event-catalog/)
- [Idempotency](/atlas/concepts/idempotency/)
- [Retry and Error Handling](/atlas/concepts/retry-and-error-handling/)
- [Dead Letter Queue](/atlas/concepts/dead-letter-queue/)
- [Business Events](/atlas/sap/business-events/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)

## Source references

- [SAP Event Mesh documentation](https://help.sap.com/docs/event-mesh)
- [SAP Help — Enterprise Event Enablement](https://help.sap.com/docs/sap-btp-abap-environment/enterprise-event-enablement)
- [CloudEvents Specification](https://cloudevents.io)

## Verification limitations

- Event Mesh capabilities vary by service plan and region.
- Content is synthesized from public SAP documentation and standards.
- No private implementation details are included.
