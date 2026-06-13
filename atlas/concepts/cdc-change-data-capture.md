---
layout: default
title: "Change Data Capture (CDC)"
description: "Change Data Capture (CDC) captures inserts, updates, and deletes in real time or near-real time, enabling incremental data replication without full reloads."
tags:
  - concept
  - sap-wm
  - sap-s4hana
  - sap-datasphere
  - ai-operations
  - integration
  - data-architecture
permalink: /atlas/concepts/cdc-change-data-capture/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-product/
  - /atlas/concepts/sap-data-product/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
---


# Change Data Capture (CDC)

> **Status**: Skeleton — under review.  
> **Scope**: Real-time data replication patterns for SAP landscapes.

## What it is

Change Data Capture (CDC) captures inserts, updates, and deletes in real time or near-real time, enabling incremental data replication without full reloads. It is essential for operational reporting, data warehousing, and analytics synchronization.

## When to use it

- Real-time operational reporting requiring fresh transactional data
- Data warehouse loading where full extracts are too slow or resource-intensive
- Keeping analytics systems synchronized with S/4HANA
- Event-driven architectures requiring data change notifications

## When not to use it

- Small tables where full extract is faster and simpler
- Scenarios where real-time synchronization is unnecessary (nightly batch suffices)
- Source systems where trigger-based CDC overhead is unacceptable
- Tables without primary keys or delta-enabled annotations

## SAP landscape fit

- **SAP SLT (Landscape Transformation Replication Server)**: Trigger-based CDC for HANA and non-HANA targets
- **SAP Datasphere Replication Flows**: Cloud-native CDC for mass data replication without Data Provisioning Agent for many scenarios
- **ODP (Operational Data Provisioning)**: CDC for ABAP CDS views and extractors; replaces RSA7 delta queue
- **SAP Data Intelligence**: Data flows with CDC capabilities for complex transformations

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| CDC mechanism | SLT for on-premise HANA; Datasphere Replication Flows for cloud |
| Delta interval | Default 60 minutes; tune to 0 minutes for near-real-time (increases load) |
| Source readiness | Primary keys and delta annotations required for CDS view CDC |
| Target | Datasphere for analytics; HANA Cloud for operational; Kafka for event streaming |

## Operational failure modes

- Trigger-based CDC adds minimal but non-zero overhead on source database
- Not all S/4HANA tables or views support CDC (redirect views, cluster tables)
- Aggressive delta intervals increase source system load and network traffic
- Source schema changes (new columns, type changes) may break replication

## Monitoring/support model

- Monitor replication latency and row counts vs source system
- Alert on replication flow failures and error logs
- Track source system CPU and memory impact from triggers
- Validate data consistency between source and target periodically

## AI/agent opportunity

- Predict replication lag from source system load and network metrics
- Recommend optimal delta intervals from historical throughput
- Detect schema changes that would break replication before deployment
- Auto-generate CDC configurations from CDS view metadata

## Related Atlas pages

- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Product](/atlas/concepts/data-product/)
- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP S/4HANA](/atlas/sap/sap-s4hana/)

## Source references

- [SAP Community — CDS-based Data Extraction](https://community.sap.com/t5/technology-blog-posts-by-sap/cds-based-data-extraction-part-i-overview/ba-p/13425314)
- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)

## Verification limitations

- CDC capabilities vary by SAP release, product edition, and source object type.
- Content is synthesized from public SAP documentation and community content.
- No private implementation details are included.
