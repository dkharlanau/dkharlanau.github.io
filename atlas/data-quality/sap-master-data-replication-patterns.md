---
layout: default
title: "SAP Master Data Replication Patterns"
description: "How master data moves between SAP systems, how DRF, ALE/IDoc, SLT, and CVI differ, and how to locate the first failed boundary."
permalink: /atlas/data-quality/sap-master-data-replication-patterns/
atlas_section: data-quality
domain: Data operations
subdomain: Master data distribution
concept_type: data quality
sap_area: MDG / DRF / ALE / IDoc / replication
business_process: Cross-process operations
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-09-23
author: Dzmitryi Kharlanau
tags:
  - master-data
  - data-quality
  - replication
  - integration
  - idoc
related:
  - /atlas/data-quality/sap-mdg-governance-patterns/
  - /atlas/diagnostics/idoc-aif-integration-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/data-quality/">Data Quality</a></li>
    <li aria-current="page">SAP Master Data Replication Patterns</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Data Quality Note</p>
    <h1>SAP master data replication patterns</h1>
    <p class="note-subtitle">Replication incidents become easier when we separate the governed business object, the distribution rule, the transport mechanism, and the target business state.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Cross-process operations</dd></div>
      <div><dt>SAP area</dt><dd>MDG / DRF / ALE / IDoc / replication</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Replication is not one technical step</h2>
    <p>When someone says that a customer, supplier, material, or business partner "did not replicate", the first task is to identify what kind of replication they mean. SAP landscapes can distribute business objects through the Data Replication Framework (DRF), send ALE/IDoc messages, call service interfaces, replicate database tables with SAP Landscape Transformation Replication Server (SLT), and synchronize related master-data representations through Customer/Vendor Integration (CVI). These mechanisms solve different problems and leave different evidence.</p>

    <p>A useful model is:</p>

    <p><strong>source business state → selection and distribution rule → outbound artifact → transport → target processing → target business state</strong></p>

    <p>The record is not "replicated" simply because one middle step succeeded. A message can leave the source and still be rejected by the target. A target table can contain data while the business object is not usable in the required role or organizational context. Conversely, a record can be intentionally excluded by a filter, so the absence of an outbound message may be correct behavior rather than a failure.</p>

    <h2>DRF distributes business objects, not arbitrary table changes</h2>
    <p>In SAP Master Data Governance and other SAP scenarios, DRF provides the distribution layer around a business object. A replication model combines outbound implementations with target systems; filters can determine which business objects are in scope. The outbound implementation also defines how the selected object is transferred for that scenario.</p>

    <p>This matters because a DRF incident has several separate questions. Was the active object eligible for replication? Did the configured filter include it? Was the intended target assigned to the replication model and outbound implementation? Was an outbound request produced, and what did the target return? Jumping directly to middleware logs skips the decisions that may have prevented a message from being created at all.</p>

    <p>For Business Partner in current SAP MDG documentation, DRF is the controlled outbound mechanism. SAP explicitly warns against leaving parallel automatic BP distribution paths active in that setup because they can compete with the governed replication flow.</p>

    <h2>ALE and IDoc add a message-processing chain</h2>
    <p>ALE distribution uses a distribution model to define which data is sent between logical systems. Depending on the master-data scenario, message types, filters, partner profiles, ports, and process codes then shape the IDoc path. The distribution model does not define individual IDoc segments; segment structure belongs to the IDoc type and its extensions. That distinction is important when diagnosing an "incomplete IDoc".</p>

    <p>If no outbound IDoc exists, inspect the source-side selection and distribution conditions before assuming a transport problem. If an IDoc exists, its control record, data records, status history, partner profile, and receiving application become the relevant evidence. An IDoc that reached the receiver is still only a technical checkpoint: the target application may reject the data or create an object that is incomplete for the intended business process.</p>

    <p>The exact message types are object-specific. For example, SAP's MDG material documentation describes ALE-based replication with material-related message types such as MATMAS and classification messages. Supplier and Business Partner scenarios use different outbound implementations and interfaces. There is no universal "master-data IDoc" that covers every object.</p>

    <h2>SLT is table replication, not business-object distribution</h2>
    <p>SAP LT Replication Server works at table level. In trigger-based replication, SLT creates logging tables and database triggers in the source so that table changes can be captured and transferred to a target. Current SAP documentation describes the trigger-based approach explicitly as a table-based concept.</p>

    <p>That makes SLT useful for data movement, analytics, sidecar databases, and other replication scenarios, but it gives a different guarantee from DRF or an application interface. SLT can show that rows were loaded or replicated. By itself, that does not prove that a target application accepted a business object through its normal application logic, nor does it express the same object-level scope as a Business Partner or material replication contract.</p>

    <p>When SLT is the actual path, investigate the replication configuration, source and target tables, initial-load state, delta processing, transformation rules, and table-structure changes. Do not diagnose it with IDoc assumptions merely because the data happens to be master data.</p>

    <h2>CVI is synchronization inside the business-partner model</h2>
    <p>Customer/Vendor Integration is often mentioned in the same incidents as replication, but it is a different boundary. CVI synchronizes Business Partner with the customer and supplier representations used by SAP applications. In SAP S/4HANA, Business Partner is the leading object and the single entry point for maintaining Business Partner, Customer, and Supplier master data.</p>

    <p>CVI therefore should not be treated as the cross-system transport itself. A landscape can first receive Business Partner data through DRF, ALE, or a service and then depend on CVI-related configuration and mappings inside the target system. A failure after technical delivery may therefore be a local synchronization or master-data-model problem rather than a network or middleware problem.</p>

    <h2>The same incident can cross several boundaries</h2>
    <div class="decision-table">
      <table>
        <thead>
          <tr><th>Observed state</th><th>Boundary to test next</th><th>Useful evidence</th></tr>
        </thead>
        <tbody>
          <tr><td>Active source record exists, but no outbound request is visible</td><td>Selection and distribution</td><td>Replication model, outbound implementation, target assignment, object filters, change or manual replication trigger.</td></tr>
          <tr><td>Outbound request exists, but nothing reaches the target runtime</td><td>Transport</td><td>IDoc status or service message, destination, partner or endpoint, connectivity, middleware evidence where it is actually part of the path.</td></tr>
          <tr><td>Target receives the message but rejects it</td><td>Application acceptance</td><td>Target error, required master data and Customizing, mapping, identifiers, roles, organizational data, and application log.</td></tr>
          <tr><td>Target record exists but differs from the governed source</td><td>Mapping or local synchronization</td><td>Key/value mapping, target-side derivation, CVI-related mapping where relevant, field ownership, and subsequent local changes.</td></tr>
          <tr><td>Rows are present in a replicated database, but the application object is not usable</td><td>Replication mechanism mismatch</td><td>Confirm whether the path is SLT/table replication or application-level replication and what business semantics the target expects.</td></tr>
        </tbody>
      </table>
    </div>

    <h2>A Business Partner example</h2>
    <p>Consider a Business Partner approved and activated in an MDG hub but missing from one SAP S/4HANA target. The useful trace is not "check DRF" as one large step. First confirm that the active BP is in scope for the configured replication model and target. Then confirm that the expected outbound implementation produced the message or service request. Follow that artifact through the configured communication channel. Finally, verify that the target accepted the Business Partner and created the required roles and customer or supplier state for the business process.</p>

    <p>The communication technology matters. Current SAP MDG documentation still documents ALE-based Business Partner replication, but for replication to SAP S/4HANA SAP recommends SOA-based replication because ALE does not cover all Business Partner-related attributes. That is exactly why the replication method must be identified rather than inferred from an old landscape pattern.</p>

    <h2>What to capture before recovery</h2>
    <p>A useful replication incident record names the source and target systems, business object and key, expected organizational scope, source state, replication method, target business state, and the first boundary that is not proven. Add the concrete technical identifier only after the path is known: IDoc number, DRF log or replication run, service message, or SLT configuration and table.</p>

    <p>Do not mass-reprocess because "the customer is missing". First establish whether the object was never selected, was already delivered under another key, failed in the target, or was partially created. Recovery is safest when the original outcome and duplicate risk are known.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/1a0f845270a9836ae10000000a423f68.html">Event Control</a> — current MDG guidance that Business Partner distribution uses DRF and that parallel automatic BP replication paths must be controlled.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/7cf3abc6109c462f904642e63a763a78-158.html">Data Replication Framework Configuration</a> — replication models, outbound implementations, target systems, and business-object filters.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE/5df72ff3c1664986b19a10e3721fe297/64a5cb5285135721e10000000a423f68.html">Set Up Data Replication</a> — ALE and DRF setup for material master data, including distribution models and object-specific message types.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_LANDSCAPE_TRANSFORMATION_REPLICATION_SERVER/cbff2cb61a354e778fda3f73d75b90f6/b52869563b6de65ae10000000a44147b.html?version=3.0">Considerations for Software Maintenance Events</a> — SLT logging tables, database triggers, and table-structure effects during trigger-based replication.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/doc/0df2ffddebab40cf9338488b2f18dc41/2025.latest/en-US/SIMPL_OP2025.pdf">SAP S/4HANA 2025 FPS01 Simplification List</a> — Business Partner as the leading object and single entry point for Business Partner, Customer, and Supplier master data in SAP S/4HANA.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/6fe343fea9b943f4875eb4425f19ed43.html">Data Replication of Business Partner Master Data Using ALE</a> — ALE support and SAP's SOA recommendation for replication to SAP S/4HANA.</li>
    </ul>
    <p><strong>Source check:</strong> 23 September 2026. Replication objects, outbound implementations, interfaces, applications, and monitoring options vary by SAP product and release.</p>

    <h2>Verification limitations</h2>
    <p>This page explains diagnostic boundaries rather than configuration steps. It does not assume that every landscape uses MDG, DRF, ALE, SLT, CVI, middleware, or the same communication channel. Confirm the governed object, source-of-truth design, product release, and configured replication path before changing filters, mappings, partner profiles, or target data.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a></li>
      <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
