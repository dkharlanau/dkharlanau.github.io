---
layout: default
title: "Data Federation"
description: "Data federation lets analytics query data where it lives instead of copying it first. This page explains remote access, pushdown, replication trade-offs, and SAP Datasphere."
tags:
  - concept
  - sap-s4hana
  - sap-datasphere
  - ai-operations
  - integration
  - data-architecture
permalink: /atlas/concepts/data-federation/
parent: Concepts
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau
robots: noindex, follow
sitemap: false
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

> **Status**: Needs verification.  
> **Scope**: Remote data access and federation decisions in SAP analytics landscapes.

Data federation lets a query use data held in another system without first creating a separate persisted copy in the analytical platform. The source remains where the data lives; the federating layer provides a virtual access path to it.

That sounds simple, but one distinction matters immediately: **federation is not the same thing as real-time replication**. A federated query reads the remote source when the query runs. Real-time replication copies source changes into a local replica, usually through change data capture. Both can provide fresh data, but they have different performance, availability, storage, and consistency characteristics.

## A remote table can be federated or replicated

SAP Datasphere makes this distinction visible through remote tables. When a supported remote table is deployed with remote data access, its data is read from the source through a virtual table and is not stored locally in Datasphere. SAP documents this as the default behavior for remote tables.

For supported connections, the same remote table can instead use replicated access. Datasphere can create a snapshot copy, refresh it on a schedule, or maintain a real-time replica where the source and connector support change data capture. Once that happens, queries read the replica table rather than the remote source.

This is why the object name alone is not enough. A “remote table” may currently be federated or replicated. The useful question is: **where will this query actually read the data from?**

## Federation moves query cost to runtime

Federation avoids a separate load pipeline and can reduce duplicated storage. It also keeps the data path close to the current source state. The trade-off is that every query depends more directly on the remote system and the connection to it.

Performance therefore depends on more than the analytical model. Network latency, source workload, adapter behavior, filters, joins, and query pushdown all matter. When the source and adapter can execute filters or aggregations remotely, less data needs to cross the connection. When pushdown is weak, a seemingly simple analytical request can move much more data than expected.

SAP's current Datasphere guidance reflects this difference. For SAP HANA sources, SAP recommends Smart Data Access for remote access because it can provide stronger query pushdown, while replication-oriented scenarios use other acquisition mechanisms where local copies are the goal. The architectural point is broader than one adapter: federation works best when the remote source can serve the analytical workload efficiently.

## Federation and replication solve different constraints

There is no reliable rule such as “federate small data, replicate big data.” Volume matters, but workload shape matters more.

| Requirement | Federation usually fits better when… | Replication usually fits better when… |
|---|---|---|
| Freshness | the query should read the current source state and the source can serve it | a local copy must stay close to the source through scheduled or real-time updates |
| Workload | queries are selective and the source can execute them efficiently | consumers repeatedly scan, join, or transform large datasets |
| Availability | the source and network can be available at query time | analytics should continue from a local copy when the source is unavailable |
| Data movement | avoiding another persisted copy is important | local processing, history, or transformation justifies the copy |
| Change capture | no local replica is required | change data capture is available and a continuously updated replica is useful |

The decision can also change over time. A remote table can start as federated access during exploration, then move to replication when repeated workloads begin to stress the source. The consumer-facing model does not necessarily have to change just because the physical access pattern changes.

## “Live” can hide more than one remote hop

Consider an SAP S/4HANA data source exposed to SAP Datasphere through a supported connection. Datasphere imports a source object as a remote table, a model is built on top of it, and SAP Analytics Cloud consumes that model through a live connection.

If the remote table remains federated, a user action in Analytics Cloud can ultimately cause Datasphere to query the S/4HANA-side source. If the remote table is switched to replicated access, the same analytical model may read the local replica instead. The word “live” at the consumption layer therefore does not tell us where every underlying dataset is physically read.

This also explains why capability restrictions must be checked at each boundary. For example, SAP's current documentation for live connections from SAP Analytics Cloud to SAP Datasphere lists planning and smart features as unsupported for that connection type. That is a consumption-layer limitation, not a general property of data federation itself.

## Virtual access does not create business semantics

Federation answers **how data is accessed**, not **what the data means**. A remote table can expose source fields without giving consumers a stable definition of revenue, open quantity, customer hierarchy, currency conversion, or fiscal period.

That semantic work still belongs in the appropriate source or modeling layer. In SAP Datasphere, views and analytic models can add reusable business structure on top of remote or replicated data. This separation is useful because the physical access strategy can change while the analytical contract remains stable.

The same caution applies to security. A federated path does not automatically mean that source-system business authorizations are reproduced unchanged in every consuming layer. Datasphere permissions, connection credentials, source privileges, and the identity model of the specific connector all remain part of the design.

## The support boundary follows the data path

Federation makes the runtime path part of analytics operations. A slow or failed query may originate in the consuming model, Datasphere query plan, remote-table configuration, connection or agent, network path, source authorization, or source workload. The most useful diagnosis follows that chain instead of treating the dashboard as the system where the problem must live.

That is also the main operational difference from replication. With federation, source availability and source performance are felt at query time. With replication, the analytical query is less dependent on the source at that moment, but the replication process introduces its own freshness, monitoring, and recovery responsibilities.

## Source references

- SAP Help Portal — [Monitoring Remote Tables](https://help.sap.com/docs/SAP_DATASPHERE/be5967d099974c69b77f4549425ca4c0/4dd95d7bff1f48b399c8b55dbdd34b9e.html).
- SAP Help Portal — [Acquiring Data](https://help.sap.com/docs/SAP_DATASPHERE/d4f3c5a0bb074d09ae9b42b2b9bd7a08/023bae1b232c426e98a06b969ae1a047.html).
- SAP BTP Guidance Framework — [Data Virtualization](https://help.sap.com/docs/sap-btp-guidance-framework/integration-architecture-guide/data-virtualization).
- SAP Help Portal — [Importing Entities with Semantics from SAP S/4HANA](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/845fedbd28574aa8b84239df848936f6.html).
- SAP Help Portal — [Live Data Connections to SAP Datasphere](https://help.sap.com/doc/00f68c2e08b941f081002fd3691d86a7/2023.20/en-US/ad4281e2875949f0b4d45d1072ff4c38.html).

## Verification limitations

Connection types, adapter capabilities, replication modes, query pushdown, identity handling, and SAP Analytics Cloud live-connection features vary by source and release. Verify the exact connection and product documentation before using this page as an implementation design.

## Related Atlas pages

- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Product](/atlas/concepts/data-product/)
- [Semantic Layer](/atlas/concepts/semantic-layer/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP Analytics Cloud](/atlas/sap/sap-analytics-cloud/)
