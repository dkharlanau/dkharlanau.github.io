---
layout: default
title: "SAP BP Relationship Diagnostics"
description: "A conservative diagnostic frame for business partner relationship issues in SAP S/4HANA."
permalink: /atlas/diagnostics/sap-bp-relationship-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Master data and MDG
concept_type: diagnostic guide
sap_area: "BP / relationships / CVI"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-05
author: Dzmitryi Kharlanau

tags:
  - master-data
  - sap-mdg
  - diagnostics
  - business-partner
related:
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
  - /atlas/diagnostics/sap-cvi-synchronization-diagnostics/
  - /atlas/sap/sap-partner-determination-failures/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP BP Relationship Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP BP relationship diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a business partner relationship is missing, invalid, or prevents transactions.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>BP / relationships / CVI</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until BP relationship behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Business partner relationships define how different BPs interact — employee-of, contact-for, subsidiary-of, and many others. When a relationship is missing, has the wrong type, or is not valid for a transaction, the support goal is to identify whether the issue is in the relationship creation, the validity period, the relationship category, or the transaction's expectation of which relationships are allowed.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>Transaction requires a contact person but none is found for the business partner.</li>
      <li>BP relationship exists but the transaction does not recognize it.</li>
      <li>Relationship was created with wrong type (e.g., 'contact' instead of 'employee').</li>
      <li>Relationship validity period has expired and the transaction fails.</li>
      <li>CVI synchronization did not replicate the relationship to the customer or vendor.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Missing relationship:</strong> the relationship was never created between the two business partners.</li>
      <li><strong>Wrong relationship category:</strong> the category does not match what the transaction expects.</li>
      <li><strong>Validity period expired:</strong> the relationship was valid in the past but not for the current transaction date.</li>
      <li><strong>Relationship not active:</strong> the relationship status is not active or is blocked.</li>
      <li><strong>CVI mapping issue:</strong> the relationship exists in BP but was not mapped correctly to the customer/vendor partner function.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>FLBP1 / FLBP2 — business partner display with relationship tab.</li>
      <li>BUPA_REL — relationship display and maintenance.</li>
      <li>BUPA_SEARCH — search for relationships by category and partner.</li>
      <li>XD03 / XK03 — customer/vendor display to check partner functions if CVI is involved.</li>
      <li>CVI_LINK — check BP-to-customer/vendor link if partner function issues exist.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>BUT050</strong> — BP relationships.</li>
      <li><strong>BUT051 / BUT052</strong> — BP relationship attributes.</li>
      <li><strong>TBZ9A / TBZ9B</strong> — relationship category definitions.</li>
      <li><strong>KNVP</strong> — customer partner functions (if CVI is used).</li>
      <li><strong>LFB1 / LFM1</strong> — vendor organizational data.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the business partner, the expected relationship, and the transaction that fails.</li>
      <li>Check FLBP1 or BUPA_REL for existing relationships and their categories.</li>
      <li>Verify the relationship validity period covers the transaction date.</li>
      <li>Check if the relationship category matches what the transaction expects.</li>
      <li>If CVI is involved, check XD03/XK03 for the corresponding partner function.</li>
      <li>If the relationship is missing, determine if it should be created manually or via replication.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Create the missing relationship with the correct category and validity period.</li>
      <li>Correct the relationship category if it was created with the wrong type.</li>
      <li>Extend the validity period if the relationship expired prematurely.</li>
      <li>Activate the relationship if it was created in an inactive status.</li>
      <li>Fix CVI mapping if the BP relationship is not correctly reflected in customer/vendor partner functions.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>BP relationship issues are usually missing data or category mismatches. A useful ticket should include: business partner number, expected relationship category, related business partner, transaction that fails, error message, and whether the relationship exists in BP but not in the transaction.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a BP relationship configuration guide. It does not cover relationship category design, CVI partner function mapping, or workflow-driven relationship creation. It does not replace SAP's business partner documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-cvi-synchronization-diagnostics/">SAP Cvi Synchronization Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-partner-determination-failures/">SAP Partner Determination Failures</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
