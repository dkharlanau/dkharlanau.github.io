---
layout: default
title: "SAP BP: Update Email with Remark using BUPA_C_CHANGEADDRESS"
description: "A tested SAP Business Partner pattern for updating an email address together with its communication remark using BUPA_C_CHANGEADDRESS."
permalink: /atlas/diagnostics/sap-bp-email-remark-update-bupa-c-changeaddress/
last_modified_at: 2026-08-28
atlas_section: diagnostics
domain: SAP Integration
subdomain: Business Partner communication data
concept_type: tested solution
sap_area: "Business Partner / ALE / IDoc"
business_process: "Business Partner address maintenance"
status: reviewed
verified: false
last_reviewed: 2026-08-28
author: Dzmitryi Kharlanau
tags:
  - sap
  - business-partner
  - idoc
  - ale
  - email
  - diagnostics
related:
  - /atlas/diagnostics/sap-master-data-diagnostics-hub/
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
robots: noindex,follow
sitemap: false
---

**Evidence:** Tested in a project environment on 28 Aug 2026.
**Observed result:** the Business Partner email and its remark were updated in one `BUPA_C_CHANGEADDRESS` request.
**Evidence boundary:** this page records the payload pattern that worked in the test. It is not a statement that the same operation flags are correct for every target record.

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li><a href="/atlas/diagnostics/sap-master-data-diagnostics-hub/">Master Data</a></li>
    <li aria-current="page">BP Email + Remark</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Tested solution / Business Partner</p>
    <h1>Update BP email and remark in one change message</h1>
    <p class="note-subtitle"><code>BUPA_C_CHANGEADDRESS</code> worked when the communication data and the related change-indicator segments were sent together.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <div class="note-body">
    <h2>Problem</h2>
    <p>The requirement was not only to change the Business Partner email address. The email remark had to be maintained in the same update.</p>

    <h2>Working pattern</h2>
    <table>
      <thead>
        <tr><th>Purpose</th><th>Segment used in the successful payload</th></tr>
      </thead>
      <tbody>
        <tr><td>Email address</td><td><code>E1BPADSMTP</code></td></tr>
        <tr><td>Communication remark</td><td><code>E1BPCOMREM</code></td></tr>
        <tr><td>Email change indicators</td><td><code>E1BPADSMTX</code></td></tr>
        <tr><td>Communication remark change indicators</td><td><code>E1BPCOMREX</code></td></tr>
        <tr><td>Address remark also present in the tested message</td><td><code>E1BPAD_REM</code></td></tr>
        <tr><td>Address remark change indicators</td><td><code>E1BPAD_REX</code></td></tr>
      </tbody>
    </table>

    <p><strong>Key point:</strong> sending the new value is only one half of the change. The related X/change segment must describe what SAP should process. In the successful test, both the data segments and their change-indicator segments were filled.</p>

    <h2>Operation flag</h2>
    <p>The tested payload contained an <code>I</code> operation indicator for the communication entries. Do not copy that flag automatically. Use the operation that matches the target state: for example, inserting a communication row is different from changing an existing row.</p>

    <h2>Fast diagnostic check</h2>
    <ol>
      <li>Confirm that the new email is present in <code>E1BPADSMTP</code>.</li>
      <li>Confirm that the email remark is present in <code>E1BPCOMREM</code>.</li>
      <li>Compare the data segments with <code>E1BPADSMTX</code> and <code>E1BPCOMREX</code>.</li>
      <li>If address-level remarks are also required, check <code>E1BPAD_REM</code> and <code>E1BPAD_REX</code>.</li>
      <li>Check that the operation indicator matches whether the target communication entry already exists.</li>
      <li>After processing, verify both the email and the remark in the Business Partner, not only the IDoc status.</li>
    </ol>

    <h2>Result from the test</h2>
    <p><strong>Passed:</strong> email and remark were updated together. This makes <code>BUPA_C_CHANGEADDRESS</code> a confirmed solution for this specific project scenario.</p>

    <h2>Reference for the segment model</h2>
    <p>SAP Help documents <code>E1BPADSMTP</code> as the BAPI structure for email addresses and includes the address and communication comment structures in the Business Address Services IDoc model.</p>
    <p><a href="https://help.sap.com/docs/SAP_NETWEAVER_731_BW_ABAP/a10e348e95cd4b679cc727859578c3ac/4e488f16fba71552e10000000a421937.html">SAP Help — Business Address Services: IDoc Type ADRMAS02 for Address Type 1</a></p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
