---
layout: atlas
title: "REST vs OData vs SOAP vs IDoc vs Events"
permalink: /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/integration-pattern-decision-matrix/
  - /atlas/concepts/synchronous-vs-asynchronous-integration/
  - /atlas/sap/odata/
  - /atlas/sap/idoc/
  - /atlas/sap/business-events/
  - /atlas/sap/rest-apis/
  - /atlas/sap/soap/
---

# REST vs OData vs SOAP vs IDoc vs Events

> **Status**: Skeleton — under review.  
> **Scope**: Protocol comparison for SAP integration decisions.

## What it is

A comparative guide to the five most common integration protocols in SAP landscapes. Use this to evaluate protocol fit for new interfaces and migration decisions.

## Comparison

| Dimension | REST | OData | SOAP | IDoc | Events |
|-----------|------|-------|------|------|--------|
| **What it is** | HTTP-based resource API | SAP-standardized REST with metadata | XML-based web service (WSDL) | Flat-file async message format | Asynchronous pub/sub notification |
| **SAP native** | CAP, Cloud SDK | S/4HANA Gateway, RAP/CDS | Enterprise Services, SOAMANAGER | ALE, EDI, WE20/WE21 | Business Events, Event Mesh |
| **Latency** | Low | Low | Low-Medium | Medium-High | Near-realtime |
| **Coupling** | Tight | Tight | Tight | Loose | Very loose |
| **Schema** | Custom JSON | EDMX/CSDL metadata | WSDL XSD | IDoc segment structure | CloudEvents + custom payload |
| **Error handling** | HTTP status codes | HTTP + Gateway logs | SOAP Faults | IDoc status codes (01-75) | DLQ, consumer retry, broker metrics |
| **Monitoring** | API Gateway logs | /IWFND/ERROR_LOG | SOAMANAGER traces | WE02/WE05/BD87 | Event Mesh dashboard, consumer lag |
| **Best for** | Custom APIs, mobile, third-party | Fiori apps, S/4HANA extensions | Legacy integrations, complex stateful ops | ERP-to-ERP, B2B, high-volume batch | Real-time decoupling, multiple consumers |
| **Avoid when** | SAP-native metadata needed | Simple CRUD without SAP context | Greenfield projects | Cloud-only landscapes | Synchronous response required |

## SAP landscape fit

- **S/4HANA Cloud Public Edition**: OData and Events are primary; REST via CAP; IDoc limited; SOAP discouraged
- **S/4HANA On-Premise**: All protocols supported; OData recommended for new development
- **ECC**: IDoc and SOAP dominant; OData via Gateway add-on
- **BTP/CAP**: REST/OData native; Events via Event Mesh; Cloud SDK for consumption

## Design decisions

1. **New Fiori app → OData** (metadata-driven, filtering, sorting, draft handling)
2. **Third-party mobile app → REST** (lightweight, custom JSON, CAP-exposed)
3. **Legacy ERP bridge → IDoc** (proven, auditable, high volume)
4. **Real-time inventory broadcast → Events** (decoupled, multiple WMS consumers)
5. **Financial posting to external tax engine → SOAP** (if only WSDL interface available)

## Operational failure modes

- **REST/OData**: 503 backend unavailable, OAuth token expiry, metadata cache stale
- **SOAP**: WSDL version mismatch, WS-Security certificate expiry, XML parsing errors
- **IDoc**: Partner profile misconfiguration, segment reduction errors, status 51 application errors
- **Events**: Silent consumer failure, schema evolution breaking consumers, queue depth overflow

## AI/agent opportunity

- Auto-generate OData service definitions from CDS views
- Convert SOAP WSDL to OpenAPI specifications for modernization
- Predict IDoc failure patterns from historical status distributions
- Detect event schema drift between producer and consumer contracts

## Related Atlas pages

- [Integration Pattern Decision Matrix](/atlas/concepts/integration-pattern-decision-matrix/)
- [SAP Integration Architecture](/atlas/concepts/sap-integration-architecture/)
- [OData](/atlas/sap/odata/)
- [IDoc](/atlas/sap/idoc/)
- [Business Events](/atlas/sap/business-events/)
- [REST APIs](/atlas/sap/rest-apis/)
- [SOAP](/atlas/sap/soap/)

## Source references

- [SAP Help — OData Services](https://help.sap.com/docs/abap-cloud-development/sap-btp-abap-environment/developing-and-exposing-odata-services)
- [SAP Help — IDoc/ALE](https://help.sap.com/docs/sap-erp/ale-idoc-basic-components)
- [SAP Help — Enterprise Event Enablement](https://help.sap.com/docs/sap-btp-abap-environment/enterprise-event-enablement)

## Verification limitations

- Protocol availability varies by SAP release and edition.
- Content is synthesized from public SAP documentation.
- No private implementation details are included.
