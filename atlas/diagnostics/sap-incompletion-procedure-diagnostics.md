---
layout: default
title: "SAP Incompletion Procedure Diagnostics"
description: "Diagnose incomplete SAP sales documents by tracing the missing field, incompletion procedure, status consequence, and blocked follow-on step."
permalink: /atlas/diagnostics/sap-incompletion-procedure-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Document completeness
concept_type: diagnostic guide
sap_area: "Sales document incompleteness"
business_process: Order to cash
status: needs_verification
verified: false
last_reviewed: 2026-09-24
last_modified_at: 2026-09-29
author: Dzmitryi Kharlanau
sales_preparation: sales

tags:
  - order-to-cash
  - sap-sd
  - diagnostics
  - master-data
related:
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /atlas/diagnostics/sap-delivery-block-analysis/
  - /atlas/sap/sap-partner-determination-failures/
  - /labs/enterprise-context/sales-order/
  - /labs/enterprise-context/sales-processes/mechanisms/
  - /labs/assessment/sales-certification/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Incompletion Procedure Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP incompletion procedure diagnostics</h1>
    <p class="note-subtitle">A saved sales document can still be incomplete. Trace the missing data, the configured consequence, and the first follow-on step that cannot continue.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order to cash</dd></div>
      <div><dt>SAP area</dt><dd>Sales document incompleteness</dd></div>
      <div><dt>Indexing</dt><dd>Noindex; editorially reviewed, still awaiting human verification.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>Incompletion is not a generic “order block.” It is a configured check that asks whether required information is present at a particular document level and, if it is missing, which later business functions should be restricted. For Sales preparation, the useful chain is <strong>document level → incompletion procedure → missing field → status group → follow-on consequence</strong>.</p>

    <p>This distinction matters because an order can exist in the system and still be unready for delivery or another later step. Saving proves that the document was persisted. It does not prove that every configured completeness requirement for fulfillment, billing, or other processing has been met.</p>

    <h2>What the incompletion mechanism actually controls</h2>
    <p>In SAP S/4HANA Cloud Public Edition Sales, incompleteness checks can apply to the sales-document header, items, schedule lines, and partner functions. Delivery documents have their own completeness checks. SAP's current Sales configuration course separates two configuration objects: the <strong>incompletion procedure</strong> defines which fields are checked, while the <strong>status group</strong> defines the consequence when one of those fields is missing.</p>

    <p>That gives us a better diagnostic question than “which field is empty?” We also need to know <em>why that field is part of this procedure</em> and <em>what the assigned status group is supposed to stop</em>. Two missing fields can therefore produce different business effects.</p>


    <h2>Build the control chain: group → procedure → field → status group → runtime status</h2>
    <p>The classic SD configuration is easier to understand when we separate five layers. A <strong>group</strong> identifies the document object, such as sales header or delivery item. An <strong>incompletion procedure</strong> is a reusable list of fields for that object. Each <strong>field entry</strong> tells SAP what to check and how to guide the user back to the missing value. The assigned <strong>status group</strong> defines which business status becomes incomplete. At runtime, the document carries the resulting incompletion status and the log keeps the missing-field evidence.</p>

    <p>This is the key design point: <strong>the procedure finds the missing data; the status group decides the business consequence.</strong> Do not use one large procedure to express every process rule. A field can be important for reporting but harmless for delivery, while another field can be a hard prerequisite for delivery or billing.</p>

    <h3>Incompletion groups</h3>
    <p>In classic SD Customizing, procedures are organized by object group. The group determines what kind of document data the procedure can check.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="SAP incompletion groups">
      <table class="study-table__table">
        <thead><tr><th>Group</th><th>Object</th><th>Typical data level</th></tr></thead>
        <tbody>
          <tr><td><code>A</code></td><td>Sales – Header</td><td>Sales-document header</td></tr>
          <tr><td><code>B</code></td><td>Sales – Item</td><td>Sales-document item</td></tr>
          <tr><td><code>C</code></td><td>Sales – Schedule Line</td><td>Schedule-line data</td></tr>
          <tr><td><code>D</code></td><td>Partner</td><td>Partner-function data</td></tr>
          <tr><td><code>F</code></td><td>Sales Activity</td><td>Sales-activity data in classic SD</td></tr>
          <tr><td><code>G</code></td><td>Delivery – Header</td><td>Delivery header</td></tr>
          <tr><td><code>H</code></td><td>Delivery – Item</td><td>Delivery item</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Status groups are business consequences, not message severities</h3>
    <p>A status group is assigned to a field inside the incompletion procedure. Its indicators decide which status dimensions become incomplete when that field is empty. The exact set depends on the document object. Sales documents commonly use general, delivery, billing, and pricing completeness. Delivery incompletion can also control execution steps such as picking or putaway, packing, goods movement, and billing.</p>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Status group effects">
      <table class="study-table__table">
        <thead><tr><th>Status dimension</th><th>What it means when incomplete</th><th>Diagnostic question</th></tr></thead>
        <tbody>
          <tr><td>General</td><td>The document or item is visibly incomplete in the general completeness status.</td><td>Do we need a reporting or control signal even if later processing is still allowed?</td></tr>
          <tr><td>Delivery</td><td>The sales document is incomplete for delivery processing.</td><td>Is this value a real prerequisite for creating or processing the delivery?</td></tr>
          <tr><td>Billing</td><td>The document is incomplete for billing.</td><td>Would invoicing without this value create a commercial or accounting problem?</td></tr>
          <tr><td>Pricing</td><td>The document is incomplete for pricing.</td><td>Is the missing value required to produce a valid price result?</td></tr>
          <tr><td>Picking / Putaway</td><td>A delivery cannot complete the relevant warehouse execution step.</td><td>Is the missing information needed before physical execution can continue?</td></tr>
          <tr><td>Packing</td><td>The delivery is incomplete for packing.</td><td>Is the missing information required before handling-unit or packing processing?</td></tr>
          <tr><td>Goods movement</td><td>The delivery is incomplete for goods issue or goods receipt, depending on direction.</td><td>Would posting the material movement with this data missing be unsafe?</td></tr>
        </tbody>
      </table>
    </div>

    <p><strong>Do not memorize the status-group number.</strong> The number is only a key. Read the indicators configured inside the group. If a plant field is assigned to a status group that marks the document incomplete for delivery, a missing plant can prevent delivery creation. A different field in the same procedure can use another status group and have a smaller effect.</p>

    <h3>Why status group 00 and 01 can look similar</h3>
    <p>One classic SD pattern is useful for understanding the difference between the log and the status. With a status group that has no status indicators selected, the field can still appear in the incompletion log while the general item status remains complete. With a group that sets only the <strong>General</strong> indicator, the same missing field can set the general incompletion status while still allowing delivery and billing if those dimensions are not selected.</p>

    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Classic status group 00 and 01 example">
      <table class="study-table__table">
        <thead><tr><th>Classic example</th><th>General status effect</th><th>Business meaning</th></tr></thead>
        <tbody>
          <tr><td><code>00</code> with no indicators</td><td>In a common classic setup, item <code>UVALL</code> can remain <code>C</code> even though a VBUV log entry exists.</td><td>Useful when the missing field should be visible in the log but should not mark the item generally incomplete.</td></tr>
          <tr><td><code>01</code> with General selected</td><td>In the same classic pattern, item <code>UVALL</code> can become <code>A</code>.</td><td>Useful when the missing field should also be visible through general incompletion status and reporting.</td></tr>
        </tbody>
      </table>
    </div>
    <p><strong>Boundary:</strong> treat 00/01 as a classic configuration example, not as a universal rule for every system. Status-group content is configuration, and SAP S/4HANA changed the physical SD status data model. Verify the active group flags and the runtime status in the target system.</p>

    <h3>What one field entry contains</h3>
    <p>The field list in the procedure is more than a list of technical names. Each entry connects a missing value to navigation, status, user feedback, and check order.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Incompletion procedure field attributes">
      <table class="study-table__table">
        <thead><tr><th>Attribute</th><th>Why it matters</th></tr></thead>
        <tbody>
          <tr><td>Table</td><td>Identifies the document structure that owns the field, for example <code>VBAK</code>, <code>VBAP</code>, or <code>VBEP</code>.</td></tr>
          <tr><td>Field</td><td>The technical field that SAP checks for an empty or incomplete value.</td></tr>
          <tr><td>Description</td><td>The business-facing text shown in the incompletion log.</td></tr>
          <tr><td>Screen / function code</td><td>Tells the log where to navigate when the user chooses to complete the missing data. If no suitable function code exists, direct navigation may not be possible.</td></tr>
          <tr><td>Status group</td><td>Maps the missing field to the affected completeness dimensions such as delivery, billing, or pricing.</td></tr>
          <tr><td>Warning indicator</td><td>For supported sales-document fields, controls whether the user receives a warning during processing. SAP documentation notes that this warning function is not available in delivery processing.</td></tr>
          <tr><td>Sequence</td><td>Controls the order in which incomplete fields are processed in the log.</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Classic configuration map</h3>
    <p>For Private Edition, on-premise, and older ECC-style GUI work, the following transactions are useful landmarks. They are <strong>not</strong> a Public Edition navigation guide.</p>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Classic SAP incompletion configuration transactions">
      <table class="study-table__table">
        <thead><tr><th>Task</th><th>Classic transaction</th><th>Object</th></tr></thead>
        <tbody>
          <tr><td>Define status groups</td><td><code>OVA0</code></td><td>Status consequences</td></tr>
          <tr><td>Define procedures and fields</td><td><code>OVA2</code></td><td>Incompletion procedure</td></tr>
          <tr><td>Assign to sales document type</td><td><code>VUA2</code></td><td>Sales header</td></tr>
          <tr><td>Assign to item category</td><td><code>VUP2</code></td><td>Sales item</td></tr>
          <tr><td>Assign to schedule-line category</td><td><code>VUE2</code></td><td>Schedule line</td></tr>
          <tr><td>Assign to delivery type</td><td><code>VUA4</code></td><td>Delivery header</td></tr>
          <tr><td>Assign to partner function</td><td><code>VUPA</code></td><td>Partner</td></tr>
          <tr><td>Assign to sales activity</td><td><code>VUC2</code></td><td>Classic sales activity</td></tr>
          <tr><td>List incomplete sales orders</td><td><code>V.02</code></td><td>Operational worklist</td></tr>
        </tbody>
      </table>
    </div>

    <h3>Technical objects: know the ECC model and the S/4HANA boundary</h3>
    <div class="table-scroll study-table" tabindex="0" role="region" aria-label="Technical objects for SAP incompletion">
      <table class="study-table__table">
        <thead><tr><th>Object</th><th>Role</th><th>Important boundary</th></tr></thead>
        <tbody>
          <tr><td><code>TVUVG</code></td><td>Incompletion object groups.</td><td>Classic Customizing structure.</td></tr>
          <tr><td><code>TVUV</code></td><td>Incompletion procedures.</td><td>Classic Customizing structure.</td></tr>
          <tr><td><code>TVUVF</code></td><td>Fields per procedure, including status group, function code, warning indicator, and sequence.</td><td>SAP Signavio technical content still exposes fields such as <code>STATG</code> for ECC and S/4HANA source systems.</td></tr>
          <tr><td><code>TVUVS</code></td><td>Status-group indicators such as general, billing, pricing, packing, or picking/putaway completeness.</td><td>Read the configured indicators; the status-group key alone is not the behavior.</td></tr>
          <tr><td><code>TVUVFC</code></td><td>Function codes used to navigate from the incompletion log to the correction screen.</td><td>Relevant mainly to classic GUI navigation.</td></tr>
          <tr><td><code>VBUV</code></td><td>Sales-document incompletion log entries.</td><td>SAP Process Insights documentation still identifies incomplete sales-document items through <code>VBUV</code>.</td></tr>
          <tr><td><code>VBUK</code> / <code>VBUP</code></td><td>Classic header and item status tables, including incompletion statuses such as <code>UVALL</code>, <code>UVVLK</code>, <code>UVFAK</code>, and <code>UVPRS</code>.</td><td>In SAP S/4HANA, the physical status tables were eliminated and status fields moved into the corresponding document header/item tables. Legacy names can still appear in compatibility and extraction contexts, so custom code must be release-aware.</td></tr>
          <tr><td><code>V50UC</code></td><td>Dynamic field structure used by delivery incompletion checks.</td><td>Do not describe it as the persisted delivery incompletion-log database table; it is a structure used by delivery processing.</td></tr>
        </tbody>
      </table>
    </div>

    <p><strong>Lead-level rule:</strong> when an order is incomplete, do not stop at “field X is empty.” Trace <strong>assignment → procedure → field → status group → runtime status → blocked function → source of the missing value</strong>. That chain tells us whether the fix belongs in master data, determination, interface mapping, user input, or Customizing.</p>

    <h2>Read the incompletion log before chasing the downstream symptom</h2>
    <p>Start with the incompletion evidence on the document itself. In Public Edition, SAP provides the <strong>List Incomplete Sales Documents</strong> app for supported sales-document categories and links from the result to the incompletion log. Current SAP documentation includes inquiries, quotations, orders, contracts, returns, orders without charge, credit memo requests, and debit memo requests among the supported categories.</p>

    <p>For one failing document, capture the exact missing field and its level: header, item, schedule line, or partner. Then ask where that value should have come from. The root cause may be missing master data, failed determination, data that was expected from a reference document, manual entry that was skipped, or a configuration rule that is too strict for the intended process. The incompletion log identifies the missing requirement; it does not by itself prove why the value is missing.</p>

    <h2>Worked example: the order exists, but delivery cannot start</h2>
    <p>Assume a standard sales order has one item with product and quantity, but the plant is empty. The order can be found by number, so a user says, “the order was created successfully.” The incompletion log shows the plant as missing at item level, and the configured status consequence makes the item incomplete for delivery.</p>

    <p>The useful analysis is not to enter any plant just to clear the status. First determine why the expected plant was not available: was it supposed to be derived from master data or another determination rule, copied from a preceding document, or entered for this scenario? After the correct plant is supplied, rerun the completeness check and then test the next business result. A clean incompletion log does not guarantee ATP, scheduling, shipping-point determination, credit, or delivery creation will succeed; it only proves that this completeness control is no longer the first known stop.</p>

    <h2>Do not confuse incompletion with other controls</h2>
    <p>A delivery block is an explicit control field. Credit status comes from credit processing. Copy control governs transfer between documents. Partner determination proposes or requires partners. Incompletion can expose the absence of data produced by one of those mechanisms, but it is not the same mechanism.</p>

    <p>This is particularly useful in assessment answers. If a ship-to party is missing and the document is incomplete, the symptom belongs to incompletion, but the root cause may still be partner determination or Business Partner data. If a document contains all required fields but has a delivery block, clearing incompletion will not remove that separate control.</p>

    <h2>A compact diagnostic sequence</h2>
    <ol>
      <li><strong>Name the first missing business result.</strong> Is the problem document completion itself, delivery creation, billing, or another follow-on step?</li>
      <li><strong>Open the incompletion evidence.</strong> Record the missing field and whether it belongs to the header, item, schedule line, partner, or delivery.</li>
      <li><strong>Identify the configured consequence.</strong> Determine which status or subsequent function the missing field is intended to affect.</li>
      <li><strong>Trace the field's expected source.</strong> Check master data, determination, reference-document transfer, manual input, or approved extension logic as appropriate.</li>
      <li><strong>Compare with a working document.</strong> Use the same document type and a similar customer/product/sales-area context where possible; do not compare unrelated scenarios.</li>
      <li><strong>Correct the source, then retest.</strong> Confirm that the incompletion entry disappears and that the intended next process step is now eligible to continue.</li>
    </ol>

    <h2>Public Edition boundary</h2>
    <p>For C_S4CS preparation, use the Public Edition Sales configuration model and Fiori apps documented in the current SAP Learning Journey. Classic transactions and IMG paths can still help explain SD concepts in other deployment models, but they are not evidence that the same navigation or configuration surface is available in SAP S/4HANA Cloud Public Edition.</p>

    <p>The current Public Edition configuration course explicitly includes <strong>Using and Configuring Incompleteness Check</strong> as a Sales configuration unit. It also documents configuration activities for defining incompleteness procedures, assigning them to relevant sales-document objects, and defining status groups. Keep that implementation layer separate from the operational question on this page: why is this particular document incomplete, and what does that incompleteness prevent?</p>

    <h2>Safety and proof</h2>
    <p>Do not populate a business-critical field with a convenient value merely to make the incompletion status disappear. A wrong plant, partner, payment term, or other field can move the process forward with incorrect commercial or logistical consequences. If configuration is changed, test representative document variants and retain the previous setting so the change can be reversed if it creates new false positives or allows documents to progress with missing data.</p>

    <p>For the incident record, keep the before/after evidence small: document and item, missing field, document level, expected source, incompletion consequence, correction, and the result of the next process step. That is enough to show whether the incompletion mechanism was the actual boundary.</p>

    <h2>Recall</h2>
    <ul>
      <li><strong>Why can a sales order be saved and still fail later?</strong> Persistence and process completeness are different checks. The configured status consequence can make the document incomplete for a later function even though the document exists.</li>
      <li><strong>Does an incompletion entry prove the root cause?</strong> No. It proves that required data is missing for the active check. The missing value may originate from master data, determination, reference-document transfer, manual entry, or extension logic.</li>
      <li><strong>Is incompletion the same as a delivery block?</strong> No. They are separate controls. Incompletion may prevent delivery processing, but an explicit delivery block can exist independently.</li>
    </ul>

    <h2>Sources and study boundary</h2>
    <ul>
      <li>SAP Learning — <a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-public-edition-sales-configuration">Implementing SAP S/4HANA Cloud Public Edition, Sales Configuration</a> — current course scope includes incompleteness check, copy control, pricing, and output.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/s4hana-cloud-best-practices/sales-order-fulfillment-monitoring-and-operations-bkk-no/list-incomplete-sales-documents">List Incomplete Sales Documents</a> — Public Edition best-practice flow using the F2430 app and incompletion log.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/7b24a64d9d0941bda1afa753263d9e39/8aadbe956f074188befb9516d320e5a9.html">List Incomplete Sales Documents</a> — current S/4HANA on-premise app behavior and navigation to the incompletion log.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_TREASURY_G-INVOICING/7d8821a6dcc94e8496f75a0606fad865/4fb70e1ff21144b7a048a70aa8ade245.html">Define Incompleteness Procedures</a> — field grouping, status-group consequence, warning behavior, and classic SD Customizing path.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_ERP_SPV/3d9b4e6529de433bac82328613bca800/e466b65334e6b54ce10000000a174cb4.html">Displaying Incompletion Status</a> — shows that status screens identify which subsequent functions are prevented by incompleteness.</li>
      <li>SAP Help Portal / Signavio Process Insights — technical mappings for <code>TVUVF</code>, <code>TVUVS</code>, and <code>VBUV</code>; used here to keep the configuration and runtime model separate.</li>
      <li>SAP Community — <a href="https://community.sap.com/t5/enterprise-resource-planning-q-a/difference-between-sd-incompletion-log-status-groups-00-and-01/qaa-p/11251740/highlight/true">status groups 00 and 01 discussion</a> — classic behavior example for <code>VBUP-UVALL</code>; treated as a system-specific example, not current product documentation.</li>
      <li><a href="/labs/assessment/sales-certification/">C_S4CS Sales preparation hub</a> — use this page as the diagnostic companion to the official configuration lesson, not as a replacement for it.</li>
    </ul>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis. Verification and indexing boundaries remain unchanged.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-sales-order-block-diagnosis/">SAP Sales Order Block Diagnosis</a> — broader triage when the first stopping control is not yet known.</li>
      <li><a href="/atlas/diagnostics/sap-delivery-block-analysis/">SAP Delivery Block Analysis</a> — when an explicit delivery block is the evidence.</li>
      <li><a href="/atlas/sap/sap-partner-determination-failures/">SAP Partner Determination Failures</a> — when missing partner data is the likely source of incompleteness.</li>
      <li><a href="/labs/enterprise-context/sales-order/">Sales Order Decision Map</a> — place incompleteness beside item category, schedule line, copy control, and output.</li>
      <li><a href="/labs/enterprise-context/sales-processes/mechanisms/#mec-sd-incomp">Sales Mechanism Library</a> — compact mechanism card with configuration surfaces, failure traces, tests, and classic transaction landmarks.</li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
