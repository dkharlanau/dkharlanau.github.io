---
layout: default
title: "Data Federation"
permalink: /atlas/concepts/data-federation/
parent: Concepts
robots: noindex, follow
sitemap: false
verified: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-product/
  - /atlas/concepts/semantic-layer/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-s4hana/
---

# Data Federation

> **Status**: Skeleton — under review.  
> **Scope**: Virtual data integration patterns for SAP landscapes.

## What it is

Data federation enables virtual integration by leaving data in source systems and accessing it remotely in real time. It avoids replication and duplication, making it ideal for operational reporting on fresh data or when data residency policies prohibit copying.

## When to use it

- Operational reporting requiring real-time data without replication latency
- Small data subsets where replication overhead exceeds value
- Data residency policies prohibiting cloud copy of on-premise data
- Prototyping and exploratory analytics before committing to replication

## When not to use it

- High-volume analytical workloads where query performance is critical
- Scenarios requiring complex joins across multiple remote sources
- SAC planning and augmented analytics (require import connections)
- Unstable network conditions where remote query reliability is poor

## SAP landscape fit

- **SAP Datasphere**: Remote Tables based on HANA Smart Data Access (SDA) and Smart Data Integration (SDI)
- **S/4HANA**: Virtual Data Model (VDM) via CDS views for operational federation
- **BW Bridge**: Model Transfer approach imports metadata while virtually accessing data
- **SAC**: Live connections to Datasphere, S/4HANA, and BW/4HANA

## Design decisions

| Decision | Recommendation |
|----------|---------------|
| Federation vs replication | Federation for real-time, small volume; replication for high-volume analytics |
| Remote table design | Filter pushdown where supported; avoid large unfiltered selects |
| Performance | Monitor source system load; use materialized views for frequently accessed subsets |
| Security | Leverage S/4HANA authorization; propagate user context via SAML |

## Operational failure modes

- Performance depends on network latency, source system load, and query complexity
- Joins across federated sources can be slow or memory-intensive
- SAC planning and augmented analytics unavailable over live connections
- Filter pushdown limited for some adapters; full table scans may occur

## Monitoring/support model

- Monitor remote query response time and source system CPU/memory impact
- Track federation error rates (connection timeout, auth failure, source unavailable)
- Review query plans for pushdown effectiveness
- Alert on queries exceeding SLA thresholds

## AI/agent opportunity

- Recommend federation vs replication based on query patterns and volume
- Predict performance issues from query complexity and source system load
- Auto-generate remote table configurations from CDS view metadata
- Detect federation queries that should be migrated to replication

## Related Atlas pages

- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Product](/atlas/concepts/data-product/)
- [Semantic Layer](/atlas/concepts/semantic-layer/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP Analytics Cloud](/atlas/sap/sap-analytics-cloud/)

## Source references

- [SAP Community — Data Federation in Datasphere](https://community.sap.com/t5/technology-blogs-by-members/data-federation-in-datasphere/ba-p/13750166)
- [SAP Datasphere documentation](https://help.sap.com/docs/datasphere)

## Verification limitations

- Federation performance varies by network, source system, and query complexity.
- Content is synthesized from public SAP documentation and community content.
- No private implementation details are included.
