---
layout: default
title: "Integration Ownership Model"
permalink: /atlas/concepts/integration-ownership-model/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/maps/integration-monitoring-reliability-map/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
---

# Integration Ownership Model

> **Status**: Skeleton — under review.  
> **Scope**: Clear ownership boundaries for SAP integration architecture and operations.

## What it is

An integration ownership model defines who owns APIs, events, contracts, middleware infrastructure, monitoring, and incident response. It prevents gaps where no team is responsible for failing interfaces.

## When to use it

- Operating 50+ integrations across multiple domains and platforms
- Migrating from central integration team to domain-oriented ownership
- Establishing AMS runbooks and escalation paths
- Defining integration governance in a data mesh or federated architecture

## When not to use it

- Small landscapes with <10 integrations managed by a single team
- Temporary project integrations with known sunset dates
- Organizations where central IT owns all integration end-to-end

## SAP landscape fit

- **Domain-oriented**: Each business domain (sales, procurement, manufacturing) owns its APIs and events
- **Platform-oriented**: Central team owns SAP Integration Suite, Event Mesh, and Cloud Connector
- **AMS-oriented**: Operations team owns monitoring, incident response, and retry/DLQ management
- **Hybrid**: Domain owns contracts and consumer onboarding; platform owns infrastructure; AMS owns runtime

## Ownership matrix

| Asset | Domain Owner | Platform Owner | AMS Owner |
|-------|-------------|--------------|-----------|
| API schema | Producer domain | Governance enforcement | — |
| Event contract | Producer domain | Broker infrastructure | Consumer retry/DLQ |
| Middleware (iFlow) | — | Integration platform team | Monitoring, patching |
| Cloud Connector | — | Platform/Network team | Health checks, cert renewal |
| Monitoring dashboards | Consumer domains | Platform team | 24/7 alerting, incident response |
| Security (OAuth, certs) | Domain (app-level) | Platform (infra-level) | Expiry tracking, rotation |

## Design decisions

- **Producer owns contract**: Schema, versioning, deprecation, and documentation
- **Platform owns infrastructure**: Middleware, brokers, gateways, and connectivity
- **Consumer owns integration**: Client code, retry logic, idempotency, and testing
- **AMS owns runtime**: Monitoring, alerting, incident response, and capacity

## Operational failure modes

- No owner for shared integration → prolonged outages, no root cause analysis
- Domain team lacks integration expertise → poor contract design, frequent breaking changes
- Platform team lacks domain context → infrastructure changes break business flows
- AMS team lacks contract visibility → cannot diagnose consumer-side errors

## Monitoring/support model

- Integration catalog with ownership tags and contact information
- Automated ownership validation in CI (every API/event must have owner)
- Escalation matrix with primary, secondary, and platform contacts
- Regular ownership audit for orphaned integrations

## AMS incident patterns

- Integration fails; no owner in catalog → escalate to integration governance team
- Domain owner unavailable → platform team provides temporary workaround
- Certificate expires → AMS alert should have fired; review monitoring coverage
- Breaking change deployed → verify consumer notification and migration timeline

## AI/agent opportunity

- Auto-discover integrations and suggest ownership from code and commit history
- Validate ownership completeness in integration catalog
- Predict ownership gaps from team churn and integration age
- Generate escalation runbooks from ownership matrix

## Related Atlas pages

- [SAP Integration Architecture](/atlas/concepts/sap-integration-architecture/)
- [Integration Architecture Map](/atlas/maps/integration-architecture-map/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [Data Mesh Principles — Martin Fowler](https://martinfowler.com/articles/data-monolith-to-mesh.html)

## Verification limitations

- Ownership models are organization-specific; this provides a template, not a mandate.
- Content is synthesized from public SAP documentation and architecture practice.
- No private implementation details are included.
