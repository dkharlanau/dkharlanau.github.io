---
layout: default
title: "SAP Retail Assortment and Listing Diagnostics"
description: "A conservative diagnostic frame for retail assortment and listing issues in SAP."
permalink: /atlas/diagnostics/sap-retail-assortment-listing-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Retail operations
concept_type: diagnostic guide
sap_area: "SAP Retail / S/4HANA Retail"
business_process: Retail operations
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - retail
  - sap-sd
  - diagnostics
  - master-data
related:
  - /atlas/concepts/store-receiving-sap-retail/
  - /atlas/diagnostics/pos-sales-not-reflected-in-sap/
  - /atlas/diagnostics/sap-master-data-duplicate-diagnostics/
  - /atlas/diagnostics/sap-business-partner-replication-diagnostics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Retail Assortment and Listing Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP retail assortment and listing diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a product is not available for procurement or sale at a store, DC, or channel.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Retail operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP Retail / S/4HANA Retail</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until assortment and listing behavior claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>In SAP Retail, a product must be in assortment and listed before it can be procured, sold, or counted at a site. Assortment defines which products are intended for which sites. Listing controls whether the product-site combination is currently valid. A product can be in assortment but not listed, or listed but not in assortment, and both states block transactions. The support goal is to identify which control is missing and whether the gap is in master data, timing, or configuration.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>A product is in the DC but the store cannot order or sell it.</li>
      <li>A new product launch fails because the product is not found at the store POS or in store inventory.</li>
      <li>Procurement cannot create a purchase order for a product at a specific site.</li>
      <li>A product appears in the article master but is not available for goods receipt at the expected site.</li>
      <li>Store staff report the product is "not in the system" despite being created centrally.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Assortment missing:</strong> the product was never assigned to the site's assortment, or the assortment assignment has an incorrect validity period.</li>
      <li><strong>Listing condition missing:</strong> the listing procedure did not generate a listing condition for the product-site combination, or the condition was deactivated.</li>
      <li><strong>Timing gap:</strong> the assortment or listing validity start date is in the future, or the end date has passed.</li>
      <li><strong>Listing procedure mismatch:</strong> the listing procedure assigned to the assortment type does not match the product or site characteristics, so listing is not triggered.</li>
      <li><strong>Site master issue:</strong> the site (store or DC) is not correctly configured as an assortment user, or the site master is missing required organizational data.</li>
      <li><strong>Article master incomplete:</strong> the article master is missing a required view, organizational extension, or status that prevents listing.</li>
      <li><strong>Replication delay:</strong> the assortment or listing data was created centrally but has not replicated to the site or POS system.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>WSOA1 / WSOA2 — assortment assignment and display per site or site group.</li>
      <li>WSOA3 — listing condition display for article-site combinations.</li>
      <li>WSOA5 — listing procedure and condition overview.</li>
      <li>WSOA7 — assortment user assignment.</li>
      <li>MM43 / MM03 — article master status and views.</li>
      <li>WE02 / WE05 — IDoc status if assortment or listing changes are distributed via IDoc.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>WSOA1 / WSOA2</strong> — assortment assignment transactions.</li>
      <li><strong>WSOA3</strong> — listing condition display.</li>
      <li><strong>T023T / T023</strong> — material group / merchandise category tables.</li>
      <li><strong>WRS1 / WRS2</strong> — assortment header and item tables.</li>
      <li><strong>WLIST</strong> — listing condition table.</li>
      <li><strong>WRF1</strong> — site master (retail-specific plant data).</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Confirm the article number and the site (store or DC) where the issue is reported.</li>
      <li>Check WSOA2 to see if the article is assigned to the site's assortment. Verify the validity period.</li>
      <li>If the article is in assortment, check WSOA3 for a valid listing condition at the site.</li>
      <li>If listing is missing, check the listing procedure (WSOA5) to see if the article and site match the procedure rules.</li>
      <li>Check the article master (MM43) for missing views, organizational extensions, or blocking statuses.</li>
      <li>Check the site master (WRF1) for correct assortment user assignment and organizational data.</li>
      <li>If master data looks correct, check WE02 for IDoc errors if assortment or listing is distributed from a central system.</li>
      <li>If the product is a new launch, verify that the assortment and listing jobs have run since the article was created.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Add the article to the site's assortment with the correct validity period if it is missing.</li>
      <li>Trigger or wait for the listing procedure to generate the listing condition.</li>
      <li>Correct the article master or site master data that prevents listing.</li>
      <li>Reprocess failed IDocs if the issue is replication-related.</li>
      <li>Escalate to the merchandising or master data team if the assortment strategy itself needs to change.</li>
    </ul>

    <h2>Support takeaway</h2>
    <p>Assortment and listing issues are usually master data or timing gaps, not system errors. A useful ticket should include: article number, site number, the transaction that failed (PO creation, sales, goods receipt), the error message or symptom, and whether the product is a new launch or an existing product that recently stopped working.</p>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not an assortment or listing configuration guide. It does not cover assortment module design, listing procedure configuration, or planogram integration. It does not replace SAP Retail documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/concepts/store-receiving-sap-retail/">Store Receiving in SAP Retail</a></li>
      <li><a href="/atlas/diagnostics/pos-sales-not-reflected-in-sap/">POS Sales Not Reflected in SAP</a></li>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
