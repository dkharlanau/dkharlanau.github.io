---
layout: default
title: "Integration Pattern Decision Matrix"
permalink: /atlas/concepts/integration-pattern-decision-matrix/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/integration-architecture-map/
  - /atlas/concepts/sap-integration-architecture/
  - /atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/
  - /atlas/concepts/synchronous-vs-asynchronous-integration/
  - /atlas/concepts/point-to-point-vs-middleware-vs-event-bus/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/odata/
  - /atlas/sap/idoc/
  - /atlas/sap/business-events/
---

# Integration Pattern Decision Matrix

> **Status**: Skeleton — under review.  
> **Scope**: Decision framework for selecting integration styles in SAP landscapes.

## What it is

A decision matrix comparing integration styles across latency, coupling, reliability, monitoring, ownership, SAP fit, and failure modes. Use this to justify protocol and pattern choices during architecture reviews.

## Integration style decision matrix

| Style | Latency | Coupling | Reliability | Monitoring | Ownership | SAP Fit | Failure Modes |
|-------|---------|----------|-------------|------------|-----------|---------|---------------|
| **REST** | Low | Tight (consumer knows endpoint) | Medium (retry needed) | HTTP status, logs | API provider | Excellent (S/4HANA Cloud, CAP) | 503/504 backend unavailable, timeout |
| **OData** | Low | Tight (schema contract) | Medium (metadata-driven) | Gateway traces, metrics | CDS/RAP owner | Excellent (native S/4HANA) | Metadata mismatch, authorization errors |
| **SOAP** | Low-Medium | Tight (WSDL contract) | Medium | SOAMANAGER logs | Enterprise Services owner | Legacy (still supported) | WSDL drift, WS-Security expiry |
| **IDoc/ALE** | Medium-High | Loose (queue-based) | High (status tracking) | WE02/WE05/BD87 | Basis/Integration team | Strong (on-premise, ECC legacy) | Partner profile errors, status 51/02 |
| **EDI** | High | Loose (file/queue exchange) | High (acknowledgments) | IDoc + TPM status | B2B integration team | Strong (Trading Partner Mgmt) | Standard variant mismatches, separator errors |
| **Events** | Near-realtime | Very loose (pub/sub) | High (broker durability) | Broker metrics, consumer lag | Event producer domain | Growing (S/4HANA Cloud, BTP) | Silent loss, consumer lag, schema drift |
| **Batch/File** | High | Very loose | Medium (file integrity) | File size, checksum, schedule | Data engineering team | Universal | File corruption, schedule drift, disk space |
| **Data Replication** | Near-realtime to batch | Loose (CDC-based) | High (SLT/DI reliability) | Replication latency, row counts | Data platform team | Strong (SLT, Datasphere) | Source schema change breaks replication, lag spikes |

## When to use which

| Scenario | Recommended Style | Rationale |
|----------|-----------------|-----------|
| Fiori app reads sales order | OData | Native S/4HANA exposure, metadata-rich, Fiori-optimized |
| Third-party e-commerce creates order | REST/OData | Standard HTTP, easy client libraries, API Business Hub discoverability |
| ERP-to-ERP material master sync | IDoc/ALE or Events | Reliable, auditable, handles high volume |
| B2B supplier invoice | EDI (X12/EDIFACT) | Industry standard, acknowledgment support, TPM mapping |
| Real-time inventory update to WMS | Events (Business Events) | Decoupled, low latency, multiple consumers |
| Monthly financial consolidation | Batch/File or Replication | Predictable schedule, high volume, checksum validation |
| Analytics data warehouse load | Data Replication (CDC) | Incremental, low source impact, Datasphere-native |

## Related Atlas pages

- [SAP Integration Architecture](/atlas/concepts/sap-integration-architecture/)
- [REST vs OData vs SOAP vs IDoc vs Events](/atlas/concepts/rest-vs-odata-vs-soap-vs-idoc-vs-events/)
- [Synchronous vs Asynchronous Integration](/atlas/concepts/synchronous-vs-asynchronous-integration/)
- [Point-to-Point vs Middleware vs Event Bus](/atlas/concepts/point-to-point-vs-middleware-vs-event-bus/)
- [SAP Integration Suite](/atlas/sap/sap-integration-suite/)

## Source references

- [SAP Integration Suite documentation](https://help.sap.com/docs/integration-suite)
- [SAP API Business Hub](https://api.sap.com)

## Verification limitations

- Matrix is directional; actual performance depends on network, payload size, and system load.
- Content is synthesized from public SAP documentation and architecture practice.
- No private benchmarking data is included.
