---
layout: default
title: SAP ALE Distribution Model Diagnostics
description: Diagnose ALE master-data distribution by separating distribution scope, change detection, IDoc creation, partner routing, and target processing.
permalink: /atlas/diagnostics/sap-ale-distribution-model-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Integration and interfaces
concept_type: diagnostic guide
sap_area: ALE / master data distribution
business_process: Integration
status: reviewed
verified: true
last_reviewed: '2026-09-24'
last_modified_at: 2026-09-24
author: Dzmitryi Kharlanau
tags:
- integration
- sap-ale
- diagnostics
- master-data
related:
- /atlas/diagnostics/idoc-aif-integration-diagnostics/
- /atlas/diagnostics/sap-idoc-status-diagnostics/
- /atlas/diagnostics/sap-key-mapping-diagnostics/
robots: index,follow
sitemap: true
level: 2
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/diagnostics/">Diagnostics</a></li><li aria-current="page">SAP ALE Distribution Model Diagnostics</li></ol></nav>

<article class="section note-detail atlas-page">
<header class="note-header">
  <p class="eyebrow">Atlas Diagnostic</p>
  <h1>SAP ALE distribution model diagnostics</h1>
  <p class="note-subtitle">BD64 answers who may receive a message. Change pointers, IDoc generation, partner profiles, transport, and target posting answer different questions.</p>
  <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
</header>

<aside class="atlas-meta-panel"><dl><div><dt>Process</dt><dd>Integration</dd></div><div><dt>SAP area</dt><dd>ALE / master data distribution</dd></div><div><dt>Indexing</dt><dd>Index, reviewed</dd></div></dl></aside>

<div class="note-body">
  <h2>BD64 is only one decision point</h2>
  <p>When master data is missing in a receiving system, it is tempting to open the ALE distribution model and look for a missing entry. Sometimes that is the right place. Often it is not.</p>
  <p>The distribution model describes ALE message flows between logical systems. It can define a sender, receiver, message type or BAPI, and filters that restrict distribution. It does not prove that a source change was captured, that an IDoc was created, that the partner profile dispatched it successfully, or that the receiving application accepted it.</p>
  <p>A useful diagnosis therefore follows one business object through several separate decisions instead of treating “ALE” as one switch.</p>

  <h2>Separate scope, trigger, and transport</h2>
  <div class="decision-table"><table><thead><tr><th>Control</th><th>What it decides</th><th>Typical evidence</th></tr></thead><tbody>
    <tr><td>Distribution model</td><td>Which logical receiver is eligible for a message flow, including configured filters.</td><td>Sender, receiver, message type or BAPI, filter values, model view.</td></tr>
    <tr><td>Change detection</td><td>Whether a relevant source change creates outbound work when the scenario uses change pointers.</td><td>General and message-type activation, relevant changed fields, unprocessed change pointers.</td></tr>
    <tr><td>IDoc generation</td><td>Whether the application or change-pointer processor turns the business change into an outbound IDoc.</td><td>RBDMIDOC/BD21 result where applicable, IDoc number, creation time, message type.</td></tr>
    <tr><td>Partner and technical dispatch</td><td>How the logical message is sent and processed for the partner.</td><td>Partner profile, port or RFC context, output/processing mode, outbound status.</td></tr>
    <tr><td>Receiving application</td><td>Whether the target can identify and apply the business object.</td><td>Inbound IDoc status, application message, target object, key or validation error.</td></tr>
  </tbody></table></div>

  <h2>The distribution model decides receivers, not whether a field changed</h2>
  <p>SAP defines the distribution model as the description of ALE message flow between logical systems. The model can contain message types, BAPIs, and filters. Those filters help the ALE layer decide whether a receiver should receive a message for the current business data.</p>
  <p>This is different from change detection. A model can correctly contain the receiver while no outbound work is created because the source change was not relevant to the active message type, change pointers were not enabled for that scenario, or the application uses another trigger altogether. Conversely, a change pointer can exist while the distribution model yields no eligible receiver.</p>
  <p>This distinction is especially useful when one object replicates and another apparently similar object does not: compare the values that participate in receiver filtering before changing the model globally.</p>

  <h2>Change pointers are a worklist, not proof of delivery</h2>
  <p>For ALE master-data scenarios that use change pointers, the source application records relevant changes and a later process evaluates them. SAP documents <strong>RBDMIDOC</strong> (also available through <strong>BD21</strong>) as the standard report that creates IDocs for a specified message type from change pointers. The report determines recipient systems from the distribution model and marks processed pointers accordingly.</p>
  <p>That gives us an important diagnostic boundary. If a relevant change pointer never appears, stay with change detection. If a pointer exists but the expected IDoc is not created, inspect the message-type processing and receiver determination. Once an outbound IDoc exists, the change pointer is no longer the best evidence for what happened downstream; follow the IDoc and its technical route instead.</p>
  <p>Do not assume every ALE scenario uses change pointers. SAP also supports direct master-data sending and application-specific triggers. First identify the actual trigger used by the object and message type.</p>

  <h2>Partner profiles turn the logical flow into runtime processing</h2>
  <p>The distribution model and partner profiles are related but not interchangeable. SAP can generate partner profiles from the model, and its ALE consistency checks compare model flows with maintained partner profiles. At runtime, the partner profile contains processing parameters for the partner and message type, while the distribution model expresses the intended cross-system flow.</p>
  <p>This explains a common pattern: BD64 can look correct while the message still fails later because the partner profile, port, RFC destination, background-processing setup, or receiver-side parameters do not match the intended route. Once an IDoc has been created, use its actual control record and status history rather than inferring the route from configuration alone.</p>

  <h2>Trace one object until the first missing fact</h2>
  <ol>
    <li><strong>Name the exact case.</strong> Record the source object key, logical source system, expected receiver, message type, and the business change that should have been distributed.</li>
    <li><strong>Prove receiver scope.</strong> Check the relevant model view and filters for this object. An active model view does not mean every object is eligible for every receiver.</li>
    <li><strong>Prove the trigger.</strong> Establish whether this flow uses change pointers, a direct send, an application event, or another mechanism. For change-pointer flows, verify both activation and the relevant changed data.</li>
    <li><strong>Find the outbound IDoc.</strong> If none exists, stay on the source side. If it exists, capture its real receiver, message type, creation time, and status.</li>
    <li><strong>Follow the actual dispatch.</strong> Check the partner profile and technical path used by that IDoc. Do not diagnose from the intended architecture when runtime evidence says otherwise.</li>
    <li><strong>Finish at the business object.</strong> A technically transferred IDoc is not the same as a successfully applied master-data change. Confirm the inbound result and the target object.</li>
  </ol>

  <h2>Four symptoms that point to different layers</h2>
  <p><strong>The object changed, but there is no change pointer.</strong> Check whether this scenario uses change pointers at all. If it does, verify general activation, message-type activation, and whether the changed fields are relevant for that message type. Do not change BD64 first.</p>
  <p><strong>A change pointer exists, but no outbound IDoc appears.</strong> Check whether the change-pointer processor ran for the correct message type and whether receiver determination produced an eligible target. A processed worklist and a distribution model are separate pieces of evidence.</p>
  <p><strong>An outbound IDoc exists for the wrong receiver.</strong> Now the distribution model, filters, logical-system assignment, and partner configuration become central. Compare the IDoc control record with the intended sender/receiver relationship.</p>
  <p><strong>The correct receiver got the IDoc, but the master data is still missing.</strong> Move away from BD64. Read the inbound status and application error, then check identity/key mapping and target-side validation. The <a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">IDoc status diagnostic</a> covers that boundary in more detail.</p>

  <h2>A working object is often the fastest control</h2>
  <p>When one object works and another does not, compare them at the first uncertain layer: filter-relevant organizational data, changed fields, message type, receiver, partner profile, and target identity. This is more informative than comparing every ALE setting in the landscape.</p>
  <p>The comparison also prevents a risky fix. If the working object follows a different message type or receiver rule, copying its configuration may widen distribution rather than repair the failing case.</p>

  <h2>Official references</h2>
  <ul>
    <li>SAP Help Portal — <a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/8f3819b0c24149b5959ab31070b64058/4abb4af3479926c4e10000000a42189b.html">Distribution Model</a>.</li>
    <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/61af834e09164854993e81aa39be576d/94e2d63b8ad9c01ce10000000a11402f.html">Distributing the Model View</a> (SAP S/4HANA 2025 FPS01).</li>
    <li>SAP Help Portal — <a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/8f3819b0c24149b5959ab31070b64058/4abc3343d7583d86e10000000a421937.html">Analyze Change Pointers</a>.</li>
    <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/61af834e09164854993e81aa39be576d/556cf03b166c8d66e10000000a11402f.html">Changing Partner Profiles with Active Background Processing</a> (SAP S/4HANA 2025 FPS01).</li>
    <li>SAP Help Portal — <a href="https://help.sap.com/docs/ABAP_PLATFORM_BW4HANA/8f3819b0c24149b5959ab31070b64058/4abb4b70479926c4e10000000a42189b.html">Check Distribution Model</a>.</li>
  </ul>

  <h2>Boundary</h2>
  <p>This page covers classic ALE/IDoc distribution logic. Exact message types, filters, change-pointer relevance, transactions, processing modes, and target behavior depend on the object and release. Modern master-data replication can use DRF, SOA services, APIs, events, or application-specific frameworks instead. For example, SAP currently recommends SOA-based Business Partner replication to SAP S/4HANA because ALE does not cover all BP-related attributes. Confirm the active replication mechanism before applying an ALE-specific correction.</p>
</div>

<section class="atlas-related"><h2>Related Atlas Pages</h2><ul>
  <li><a href="/atlas/diagnostics/idoc-aif-integration-diagnostics/">IDoc and AIF Integration Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-idoc-status-diagnostics/">SAP IDoc Status Diagnostics</a></li>
  <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a></li>
</ul></section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
</article>
