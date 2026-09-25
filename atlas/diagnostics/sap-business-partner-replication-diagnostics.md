---
layout: default
title: "SAP Business Partner Replication Diagnostics"
description: "A source-backed SAP Business Partner replication guide for DRF selection, SOAP or ALE delivery, confirmations, key mapping, and duplicates."
permalink: /atlas/diagnostics/sap-business-partner-replication-diagnostics/
last_modified_at: 2026-09-24
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "BP / MDG / replication"
business_process: Master data governance
status: reviewed
verified: true
level: 2
expert_context:
  enabled: true
  domain: sap-master-data
  topics:
    - Business Partner replication
    - master-data governance
    - customer and supplier data
  service_url: /services/sap-master-data-stability-assessment/
  evidence_urls:
    - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
    - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
    - /atlas/data-quality/sap-master-data-quality/
last_reviewed: 2026-09-24
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - replication
related:
  - /atlas/diagnostics/sap-vendor-master-replication-diagnostics/
  - /atlas/diagnostics/sap-customer-master-replication-diagnostics/
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/data-quality/master-data-governance-failure-modes/
robots: index,follow
sitemap: true
---

**Sources:** [SAP APIs for Business Partner](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/9fca825858239244e10000000a4450e5.html), [SAP Business Partner replication using ALE](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/6fe343fea9b943f4875eb4425f19ed43.html), and [SAP Object Replication Status](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/543df06bbf584228ad293552d4ece873.html).
**Date checked:** 2026-09-24
**Confidence:** high for the DRF, SOAP, and ALE diagnostic boundaries; medium for mapping and target behavior that depend on the configured landscape.
**Practical implication:** Follow one BP to the first unproven handoff before changing master data or resending it.

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Business Partner Replication Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP business partner replication diagnostics</h1>
    <p class="note-subtitle">Trace one business partner from replication scope to the target object, without confusing source selection, transport, inbound processing, and cross-system identity.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>BP / MDG / replication</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Replication is a chain, not one status</h2>
    <p>A Business Partner can be correct in the source system and still be absent, incomplete, or duplicated in the target. The useful question is not simply whether “replication worked.” We need to know which decision in the chain was last proven.</p>
    <p>For a DRF-based landscape, a practical model is:</p>
    <p><strong>source BP → replication model and filters → outbound implementation → SOAP or IDoc delivery → target inbound processing → target identity and confirmation</strong></p>
    <p>Each boundary has different evidence. A successful source-side replication run does not by itself prove that the receiving system created or updated the intended BP.</p>

    <h2>Find the first unproven handoff</h2>
    <div class="decision-table"><table><thead><tr><th>Boundary</th><th>Question</th><th>Useful evidence</th></tr></thead><tbody>
      <tr><td>Source object</td><td>Is this the correct BP version and is it ready for the configured replication process?</td><td>BP number and UUID where available, roles, activation/change context, expected target.</td></tr>
      <tr><td>DRF scope</td><td>Did the active replication model and its filters select this object for this target?</td><td>Replication model, outbound implementation, target business system, filter values, replication run/log.</td></tr>
      <tr><td>Outbound message</td><td>Was a message actually created through the configured channel?</td><td>Run ID, message or IDoc identifier, sender/receiver, timestamp.</td></tr>
      <tr><td>Technical delivery</td><td>Did the message reach the receiving system?</td><td>SOAP runtime evidence or IDoc status according to the channel.</td></tr>
      <tr><td>Target processing</td><td>Did the target accept the payload and apply the relevant BP segments?</td><td>Inbound message result, application log, target BP, roles and organizational segments.</td></tr>
      <tr><td>Identity</td><td>Did both systems agree which source and target records represent the same BP?</td><td>Confirmation, source/receiver identifiers, key mapping, duplicate evidence.</td></tr>
    </tbody></table></div>

    {% include atlas/expert-context.html %}

    <h2>Start with the architecture that actually ran</h2>
    <p>SAP S/4HANA supports Business Partner integration through several interfaces, including SOAP, IDoc, and OData. In MDG scenarios, the Data Replication Framework is commonly the selection and orchestration layer, but DRF does not imply one transport technology. SAP also documents DRF-based BP replication through IDoc for ALE scenarios.</p>
    <p>This matters during support. If the configured outbound implementation uses SOAP, an empty IDoc monitor tells us nothing. If it uses ALE, a SOAP monitor is the wrong place to start. First identify the replication model, outbound implementation, target business system, and communication channel. Then follow the evidence produced by that path.</p>
    <p>For replication to SAP S/4HANA, SAP currently recommends SOA-based BP replication when possible because ALE does not cover all Business Partner-related attributes. Existing ALE landscapes are still valid scenarios, but a missing attribute can be a channel-scope issue rather than a failed resend.</p>

    <h2>DRF selection is not target success</h2>
    <p>The replication model answers who should receive which business object under which filters. The outbound implementation determines how that object is prepared and sent. Object Replication Status and its replication log can then show the progress and result of a replication run for a business object and business system.</p>
    <p>Once an outbound message exists, switch from configuration to runtime evidence. For SOAP-based BP replication, SAP documents the <code>BusinessPartnerSUITEBulkReplicateRequest</code> service and message monitoring in <code>SRT_MONI</code>. For ALE, follow the actual IDoc control record and status history. Do not keep changing DRF filters after the correct object and target have already produced a message.</p>

    <h2>When the BP exists but some data is missing</h2>
    <p>An incomplete target BP is not automatically a transport failure. The current SOAP Business Partner service has segment-level behavior, and SAP supports partial-data handling through DRF segment filters and Complete Transmission Indicators (CTI). A role, tax number, address usage, customer sales-area partner function, or another segment may therefore be absent because it was outside the selected payload scope or handled differently by the target.</p>
    <p>Compare the source data, the outbound payload, and the target result at the first missing segment. If the field was not sent, investigate selection or service scope. If it was sent but rejected or transformed, move to target validation, value mapping, or application logic.</p>
    <p>Relationships also deserve their own trace. SAP exposes separate SOAP services for Business Partner relationships, and relationship processing can depend on the main BP message. A BP that exists correctly while its contact or other relationship is missing is therefore a different incident from a missing BP header.</p>

    <h2>Identity must be proven before a resend</h2>
    <p>Different BP numbers across systems can be intentional. Key mapping records that the source and receiver identifiers represent the same business object. SAP's SOAP confirmation service can return the receiver BP identifiers together with replication status, which is useful evidence when the target uses a different number.</p>
    <p>This makes blind resends risky. If the first message created a target BP but the confirmation or key mapping did not complete as expected, another send may not follow the same identity path. Before replaying, establish whether a target object already exists, which source and receiver IDs are linked, and whether the previous confirmation was processed. For deeper identity analysis, use the <a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a>.</p>

    <h2>A practical trace</h2>
    <ol>
      <li><strong>Define one case.</strong> Capture the source BP number and UUID where available, expected target, required roles or segments, and the business change that should have replicated.</li>
      <li><strong>Prove DRF scope.</strong> Confirm the active model, outbound implementation, target business system, and filter values for this BP. If the object was not selected, stay on the source side.</li>
      <li><strong>Capture the outbound identity.</strong> Record the replication run and the actual SOAP message or IDoc identifier. This is the handoff from configuration to runtime evidence.</li>
      <li><strong>Follow the configured channel.</strong> For SOAP, trace the web-service message and its receiver result. For ALE, follow the IDoc and its statuses. If middleware is present, use the same message or correlation identity across the hop.</li>
      <li><strong>Inspect the target object.</strong> Compare the required BP roles, customer or supplier segments, addresses, identifiers, relationships, and other relevant data with what the payload contained.</li>
      <li><strong>Close the identity loop.</strong> Check confirmation and key mapping where the scenario uses them. Only then decide whether a resend, mapping correction, source-data correction, or target-side fix is appropriate.</li>
    </ol>

    <h2>Four patterns that look similar but are not</h2>
    <p><strong>No outbound message exists.</strong> Stay with source readiness, replication model selection, filters, and the outbound implementation. Transport is not yet the problem.</p>
    <p><strong>The message exists but never reaches the target.</strong> Follow the configured SOAP, middleware, or ALE route. This is a delivery problem until evidence shows otherwise.</p>
    <p><strong>The target BP exists but one role or segment is missing.</strong> Compare payload scope with target processing. Check DRF segment filters, service coverage, CTI behavior where relevant, mapping, and target validation before resending the full BP.</p>
    <p><strong>A duplicate BP appears.</strong> Stop treating the incident as simple delivery. Establish source and target identifiers, confirmation history, key mapping, and how the target decided between create and update. Duplicate remediation can affect downstream documents and usually needs master-data governance ownership.</p>

    <h2>Official references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/9fca825858239244e10000000a4450e5.html">APIs for Business Partner</a> (SAP S/4HANA 2025 FPS01).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/f4edce62151b421bbb45d4c92a98b9fc.html">Business Partner – Replicate to Client</a> (SOAP).</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/f69dc6a7cd2f418f9ae309b2906f2c57.html">Business Partner – Receive Confirmation from Client</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/44e06f22436c43e582db6ccd5250e29b/511df2733fab4fcba3c1b0eaae97b0c8.html">Business Partner – Partial Data Model</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/6fe343fea9b943f4875eb4425f19ed43.html">Data Replication of Business Partner Master Data Using ALE</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/8308e6d301d54584a33cd04a9861bc52/543df06bbf584228ad293552d4ece873.html">Display of Object Replication Status</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/8f3d0f8274e642b5aed793f4f4f8e5a4.html">Key Mapping</a>.</li>
    </ul>

    <h2>Boundary</h2>
    <p>This page covers the end-to-end diagnostic boundary for Business Partner replication. Exact outbound implementations, filters, service versions, middleware routes, target validation, number assignment, and key-harmonization rules depend on the product and release. The customer- and supplier-specific pages cover their organizational segments; the <a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">CVI diagnostic</a> covers synchronization between BP and customer or supplier objects inside an SAP system.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">SAP Vendor Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">SAP Customer Master Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    </ul>
  </section>

  {% include atlas/expert-cta.html %}
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
