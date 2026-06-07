---
layout: atlas
title: "SAP Integration Architecture"
permalink: /atlas/concepts/sap-integration-architecture/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
  - /atlas/concepts/synchronous-vs-asynchronous-integration/
  - /atlas/concepts/point-to-point-vs-middleware-vs-event-bus/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/sap-btp/
  - /atlas/sap/cloud-connector/
  - /atlas/sap/odata/
  - /atlas/sap/idoc/
  - /atlas/sap/business-events/
  - /atlas/sap/integration-monitoring/
---

# SAP Integration Architecture

> **Status**: Skeleton — under review.  
> **Scope**: Enterprise integration architecture for SAP-centric landscapes.

## What it is

SAP Integration Architecture defines how SAP and non-SAP systems exchange data and orchestrate processes. It spans protocols (OData, IDoc, SOAP, REST, EDI), platforms (SAP Integration Suite, SAP BTP), and patterns (synchronous, asynchronous, event-driven).

## When to use it

- Designing new interfaces between S/4HANA and external systems
- Migrating from legacy PI/PO to cloud-native integration
- Establishing API-first or event-first integration strategies
- Consolidating point-to-point connections into a managed middleware layer

## When not to use it

- For simple, stable, low-volume bilateral interfaces where middleware adds operational overhead
- When real-time synchronous coupling is unnecessary and batch/file transfer suffices
- If the organization lacks integration operations capacity to manage an iPaaS

## SAP landscape fit

- **S/4HANA Cloud Public Edition**: OData APIs and Business Events are the sanctioned interfaces; IDoc support is limited
- **S/4HANA On-Premise**: Full protocol support including IDoc, SOAP, OData, RFC, and custom BAPIs
- **SAP BTP**: Cloud Integration (iFlow), API Management, Event Mesh, and Destination/Connectivity services
- **Hybrid**: Cloud Connector enables secure cloud-to-on-premise connectivity without inbound firewall rules

## Design decisions

| Decision | Options | SAP Recommendation |
|----------|---------|-------------------|
| Protocol | OData, REST, SOAP, IDoc, EDI, Events | OData/REST for new; IDoc for legacy; Events for decoupling |
| Platform | Cloud Integration, third-party iPaaS, custom | SAP Integration Suite for SAP-centric landscapes |
| Coupling | Synchronous, Asynchronous, Event-driven | Async for cross-domain; sync for user-facing queries |
| Security | OAuth2, X.509, SAML, Basic | OAuth2SAMLBearerAssertion for principal propagation |

## Operational failure modes

- Cloud Connector downtime blocks all hybrid cloud-to-on-premise traffic
- Misconfigured partner profiles (WE20) cause IDoc transmission failures
- OAuth token expiration in long-running iFlows produces intermittent 401 errors
- Missing idempotency handling creates duplicate records during retry storms

## Monitoring/support model

- SAP Integration Suite Monitoring Dashboard for iFlow execution traces
- IDoc status monitoring via WE02/WE05/BD87
- API Management analytics for rate limiting and error trends
- Cloud Connector health checks and audit logging

## Ownership model

- **Domain teams**: own API/event contracts and consumer onboarding
- **Integration platform team**: owns middleware infrastructure, security, and governance
- **AMS team**: owns monitoring, incident response, and retry/DLQ management

## AMS incident patterns

- IDoc stuck in status 51 (application error) → check partner profile and segment mapping
- iFlow HTTP 503 → check backend system availability and Cloud Connector status
- Event loss → verify Event Mesh queue depth, consumer bindings, and daemon user authorization
- OAuth failures → check Destination service configuration and certificate validity

## AI/agent opportunity

- Auto-classify integration errors by error code and payload signature
- Suggest remediation steps from OSS notes and runbooks
- Predict Cloud Connector capacity issues from throughput trends
- Generate API contract drafts from CDS view metadata

## Related Atlas pages

- [Integration Architecture Map](/atlas/maps/integration-architecture-map/)
- [Integration Pattern Decision Matrix](/atlas/concepts/integration-pattern-decision-matrix/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)
- [SAP BTP](/atlas/sap/sap-btp/)
- [Cloud Connector](/atlas/sap/cloud-connector/)
- [OData](/atlas/sap/odata/)
- [IDoc](/atlas/sap/idoc/)
- [Business Events](/atlas/sap/business-events/)
- [Integration Monitoring](/atlas/sap/integration-monitoring/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [SAP BTP documentation](https://help.sap.com/docs/btp)
- [SAP API Business Hub](https://api.sap.com)

## Verification limitations

- Content is synthesized from public SAP documentation and architecture practice.
- Specific feature availability depends on SAP Integration Suite edition and S/4HANA release.
- No private implementation details are included.
