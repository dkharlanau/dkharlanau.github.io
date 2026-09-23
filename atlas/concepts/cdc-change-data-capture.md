---
layout: default
title: "Change Data Capture (CDC)"
description: "Change Data Capture (CDC) in SAP landscapes: initial load, delta capture, ABAP CDS extraction, SLT, SAP Datasphere replication flows, and consistency boundaries."
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
status: needs_verification
verified: false
last_reviewed: 2026-09-23
robots: noindex, follow
sitemap: false
related:
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/data-product/
  - /atlas/concepts/sap-data-product/
  - /atlas/concepts/data-federation/
  - /atlas/sap/business-events/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
---

# Change Data Capture (CDC)

Change Data Capture is a way to keep a target copy of data current by moving the changes that happened after a known point, rather than reading the whole source again. In practice, the useful model is not simply “real-time replication.” It is a chain: establish a consistent starting state, capture inserts, updates, and deletes, move them in the right sequence, and apply them to the target without losing or duplicating changes.

That distinction matters in SAP landscapes because several technologies can participate in that chain. ABAP CDS extraction, SAP Landscape Transformation Replication Server (SLT), SAP Datasphere replication flows, and other data-provisioning mechanisms do not all capture changes in the same way. “CDC” describes the change-capture pattern; it does not name one universal SAP product or protocol.

## The initial load and the delta belong to one consistency problem

A CDC process normally starts with an initial load. That gives the target its baseline. After that point, delta processing applies only records that changed. The difficult part is the boundary between the two: changes can continue in the source while the initial copy is being built, so the capture mechanism must make sure those changes are not lost during the handover.

The target also needs enough information to reproduce the source state. An insert must create a record, an update must identify the record that changed, and a delete must remove or invalidate the corresponding target record. Keys, change order, delete handling, and restart behavior therefore matter as much as replication speed. A pipeline that is only “fast” can still be wrong if it misses deletes or resumes from the wrong position.

## CDC is not the same as polling or a business event

Polling repeatedly asks the source for its current state. CDC records or exposes what changed, which can reduce the amount of data that needs to be read after the initial load. The exact mechanism can be database triggers, a source-specific change log, an extraction framework, or another delta implementation.

A [business event](/atlas/sap/business-events/) solves a different problem. It tells a consumer that a meaningful business change happened. CDC is usually concerned with data-state changes needed for replication. A table-level change saying that one row was updated does not automatically tell a consumer why the business object changed or which business action should follow. Event-driven integration and CDC can complement each other, but they should not be treated as synonyms.

## SAP has several CDC paths

In an SAP S/4HANA landscape, the right mechanism depends on the source object and the consumer.

**ABAP CDS extraction** can expose delta-capable views. SAP documents a trigger-based CDC mechanism for CDS extraction in which changes to the underlying tables are recorded. For simple projection-style views, the mapping between the CDS view and the underlying table keys can be derived automatically. More complex views, especially those with joins, can require explicit mapping through the `Analytics.dataExtraction.delta.changeDataCapture.mapping` annotation. This is why “it is a CDS view” is not enough to conclude that the view is suitable for CDC.

**SAP SLT Replication Server** works closer to the table layer. In real-time replication mode, SAP describes SLT as trigger-based: database triggers record table changes for later transfer to the target. The same product can also run replication on a schedule. This is a useful reminder that the capture mechanism and the delivery frequency are separate design choices.

**SAP Datasphere replication flows** orchestrate movement from supported sources to supported targets. Current SAP Datasphere documentation distinguishes Initial Only, Initial and Delta, and Delta Only load types. Initial and Delta performs the baseline load and then copies inserted, updated, or deleted records at configured intervals or scheduled times. Whether a given object supports a delta load depends on the source and target combination; the replication flow does not create delta capability where the source cannot provide it.

## The CDS model determines what can be captured safely

CDS-based CDC is often misunderstood as a switch that can be added to any view. The mapping has to let the framework relate changes in the underlying tables back to the extracted CDS records. SAP's current ABAP documentation distinguishes automatic mapping for simple cases from explicit mapping for more complex joins.

This has an architectural consequence: an analytical view designed for rich consumption is not automatically a good extraction contract. A wide view with joins, calculated semantics, and many associations may be convenient for a report but difficult or unsupported for delta capture. Sometimes a simpler extraction view is the better boundary, with semantic enrichment applied later in the data platform.

The same caution applies to keys. “CDC requires a primary key” is too broad as a universal rule. SAP Datasphere documents limited replication-flow scenarios for source objects without primary keys, but current CDS-source rules restrict such objects to Initial Only. The safe question is therefore not whether CDC always requires one specific key structure, but whether the selected source object and connector can identify and apply changes unambiguously for the requested load type.

## Freshness is a run setting, not the definition of CDC

CDC is often sold internally as “real time,” but the practical freshness is controlled by capture delay, replication frequency, backlog, network time, and target processing. SAP Datasphere, for example, currently uses a 60-minute default delta-load frequency for long-running replication flows, but that setting can be changed. Setting the interval to zero tells the flow to replicate source changes immediately where the scenario supports it.

That does not make zero the correct default. SAP warns that delta frequency can materially affect system load, and Datasphere billing for replication-flow jobs is tied to job duration. A five-minute business freshness requirement and a nightly analytical requirement should not receive the same replication design merely because both can use CDC.

## A practical S/4HANA-to-Datasphere example

Assume a team needs sales-order item data in SAP Datasphere with frequent updates. A suitable extraction-enabled CDS view provides the source contract. The replication flow first performs the initial load. When quantities or dates later change in S/4HANA, the source delta mechanism records those changes and the replication flow consumes and applies them to the target according to its run settings.

If the target falls behind, the useful question is not simply “Is CDC running?” We need to locate the boundary that stopped moving: did the source record the change, is the delta-capable object still valid, is the replication flow active, is there a backlog between capture and consumption, and did the target apply the record successfully? That sequence turns an abstract “stale data” incident into a concrete consistency problem.

The same example also shows why CDC should not replace business semantics. A replicated change to an item quantity is data evidence. If another application needs to react to a business event such as an order being created or released, a business-event contract may be the clearer integration boundary.

## Source references

- SAP Help Portal — [Analytics Annotations](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44ec04bc8de24103b400d261fde99462/c2dd92fb83784c4a87e16e66abeeacbd.html), including `Analytics.dataExtraction` and trigger-based CDC annotations for ABAP CDS.
- SAP Help Portal — [Loading and Replicating Data from ABAP CDS Views in SAP S/4HANA](https://help.sap.com/docs/data-intelligence-cloud/sap-data-intelligence-abap-integration-guide/55b2a17f987744cba62903e97dd99aae.html), including automatic and explicit CDC mapping.
- SAP Help Portal — [Creating a Configuration](https://help.sap.com/docs/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER_FOR_SAP_S4HANA/6c1517d53535498181a2c12d31d1b54a/84f36f563126c31ee10000000a441470.html), describing SLT real-time trigger-based replication and scheduled alternatives.
- SAP Help Portal — [Configure the Run Settings of a Replication Flow](https://help.sap.com/docs/SAP_DATASPHERE/c8a54ee704e94e15926551293243fd1d/3f5ba0c5ae3944c1b7279bb989a2a5b5.html), covering Initial Only, Initial and Delta, Delta Only, and delta-load frequency.
- SAP Help Portal — [SAP S/4HANA and Other ABAP Sources for Replication Flows](https://help.sap.com/docs/PRODUCT_ID/c8a54ee704e94e15926551293243fd1d/3f70579c92434f4f88471bba2bd70893.html), including source-object and key restrictions for replication flows.

## Verification limitations

CDC capabilities vary by SAP product, release, source object, connector, and target. A supported delta mechanism in one extraction path does not imply support in another. Before implementation, verify the current source-object requirements, supported load type, restart behavior, and operational limits for the exact landscape.

## Related Atlas pages

- [Data Federation](/atlas/concepts/data-federation/)
- [Data Mesh for SAP Landscapes](/atlas/concepts/data-mesh-for-sap-landscapes/)
- [Data Product](/atlas/concepts/data-product/)
- [SAP Data Product](/atlas/concepts/sap-data-product/)
- [Business Events](/atlas/sap/business-events/)
- [SAP Datasphere](/atlas/sap/sap-datasphere/)
- [SAP S/4HANA](/atlas/sap/sap-s4hana/)
