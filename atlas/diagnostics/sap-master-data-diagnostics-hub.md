---
layout: default
title: "SAP Master Data Diagnostics Hub"
description: "A review-candidate hub mapping MDG, BP, CVI, key mapping, and replication symptoms to SAP master data checks."
permalink: /atlas/diagnostics/sap-master-data-diagnostics-hub/
last_modified_at: 2026-06-13
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "MDG / BP / CVI / Replication"
business_process: "Master data governance"
status: needs_verification
verified: false
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau
tags:
  - sap-ams
  - master-data
  - mdg
  - cvi
related:
  - /atlas/data-quality/
  - /atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/diagnostics/sap-master-data-duplicate-diagnostics/
robots: noindex,follow
sitemap: false
---

**Source:** Practical pattern derived from SAP support experience. Not yet verified against public SAP documentation.
**Date checked:** 2026-06-13
**Confidence:** medium
**Related page/topic:** /atlas/data-quality/sap-master-data-quality/
**Practical implication:** Separate governance (MDG), synchronization (CVI), and replication (distribution) before collecting evidence; each layer has different owners and tools.
**Tags:** sap-ams, master-data, mdg, cvi

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Master Data Diagnostics Hub</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic Hub</p>
    <h1>SAP Master Data Diagnostics Hub</h1>
    <p class="note-subtitle">A first-pass workflow for MDG activation, BP/customer/vendor replication, CVI synchronization, key mapping, and duplicate detection.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>MDG / BP / CVI / Replication</dd></div>
      <div><dt>Reviewed</dt><dd>13 Jun 2026</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Master data incidents usually fall into three layers: governance (MDG change request, approval, activation), synchronization (CVI between BP and customer/vendor), and replication (distribution to downstream systems). Duplicates and key mapping failures cut across all three. This hub helps the responder decide which layer to investigate first.</p>

    <h2>Symptom-to-check matrix</h2>
    <table>
      <thead>
        <tr><th>Symptom</th><th>Layer</th><th>Typical SAP touchpoints</th></tr>
      </thead>
      <tbody>
        <tr><td>Change request stuck or activation fails</td><td>MDG governance</td><td>MDG change request, workflow log, staging, validation messages</td></tr>
        <tr><td>BP created but customer/vendor not synchronized</td><td>CVI synchronization</td><td>BP role, CVI link tables, direction settings</td></tr>
        <tr><td>Record not replicated to target system</td><td>Replication</td><td>Distribution model, IDoc/ALE, replication log, key mapping</td></tr>
        <tr><td>Same real-world object has multiple keys</td><td>Duplicate detection</td><td>Duplicate check rules, match codes, key mapping tables</td></tr>
        <tr><td>Different keys for the same object across systems</td><td>Key mapping</td><td>Key mapping tables, ID mapping, cross-system identifiers</td></tr>
        <tr><td>Missing organizational assignment</td><td>Master data extension</td><td>Org-level views, roles, authorization</td></tr>
        <tr><td>Document cannot be created due to master data</td><td>Operational validation</td><td>Material, vendor, customer, account validation</td></tr>
      </tbody>
    </table>

    <h2>Evidence to collect</h2>
    <ul>
      <li>Object type and key: business partner, customer, vendor, material, or account (use synthetic keys only).</li>
      <li>Source and target system roles if replication is involved.</li>
      <li>MDG change request status and workflow step when governance is involved.</li>
      <li>CVI link status and direction for BP/customer/vendor issues.</li>
      <li>Distribution model, message type, and IDoc or replication log reference.</li>
      <li>Duplicate-check rule and match-code result.</li>
    </ul>

    <h2>Related diagnostics</h2>
    <div class="atlas-card-grid">
      <a class="atlas-card" href="/atlas/diagnostics/sap-mdg-to-s4-replication-diagnostics/">
        <h2>MDG to S/4 Replication</h2>
        <p>Approved master data does not appear in target systems.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">
        <h2>CVI Synchronization</h2>
        <p>BP, customer, or vendor not synchronized.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-key-mapping-diagnostics/">
        <h2>Key Mapping</h2>
        <p>Different keys across systems cause duplicates or failed replications.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">
        <h2>Master Data Duplicates</h2>
        <p>Duplicate records and prevention.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">
        <h2>Business Partner Replication</h2>
        <p>BP not replicated or incomplete.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-vendor-master-replication-diagnostics/">
        <h2>Vendor Master Replication</h2>
        <p>Vendor not replicated or duplicated.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-customer-master-replication-diagnostics/">
        <h2>Customer Master Replication</h2>
        <p>Customer not replicated or duplicated.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
      <a class="atlas-card" href="/atlas/diagnostics/sap-material-master-extension-diagnostics/">
        <h2>Material Master Extension</h2>
        <p>Material cannot be extended to a new org level.</p>
        <span class="link-arrow">Read diagnostic</span>
      </a>
    </div>

    <h2>Related maps and concepts</h2>
    <ul>
      <li><a href="/atlas/data-quality/">Data Quality Atlas</a> — verified section index.</li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — verified.</li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a> — verified.</li>
    </ul>

    <h2>Boundaries and escalation</h2>
    <p>This hub is for diagnostic triage only. MDG workflow changes, CVI direction changes, key-mapping corrections, and duplicate merges are operational or functional changes that need owner approval and often data governance sign-off. Escalate when the issue affects multiple systems, involves legal-entity data, or requires mass correction.</p>

    <h2>Safe automation opportunity</h2>
    <p>A support agent can compare BP, customer, and vendor keys across linked systems and flag missing CVI links or potential duplicates for human review. It should not create, change, or merge master data records.</p>
  </div>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
