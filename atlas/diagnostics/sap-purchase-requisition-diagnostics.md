---
layout: default
title: "SAP Purchase Requisition Diagnostics"
description: "A conservative diagnostic frame for purchase requisition issues in SAP MM, covering sourcing, approvals, account assignment, and master data gaps."
permalink: /atlas/diagnostics/sap-purchase-requisition-diagnostics/
atlas_section: diagnostics
domain: SAP AMS
subdomain: Procurement and logistics
concept_type: diagnostic guide
sap_area: "MM purchasing"
business_process: Procure to pay
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
author: Dzmitryi Kharlanau

tags:
  - procure-to-pay
  - sap-mm
  - diagnostics
  - purchasing
related:
  - /atlas/diagnostics/sap-purchase-order-creation-diagnostics/
  - /atlas/diagnostics/sap-release-strategy-diagnostics/
  - /atlas/diagnostics/sap-source-determination-diagnostics/
  - /atlas/sap/sap-mm-procurement-overview/
  - /atlas/maps/procure-to-pay-map/
robots: index,follow
sitemap: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/diagnostics/">Diagnostics</a></li>
    <li aria-current="page">SAP Purchase Requisition Diagnostics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Diagnostic</p>
    <h1>SAP purchase requisition diagnostics</h1>
    <p class="note-subtitle">A first-pass structure for finding why a purchase requisition cannot be created, approved, or converted to a purchase order.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Procure to pay</dd></div>
      <div><dt>SAP area</dt><dd>MM purchasing</dd></div>
      <div><dt>Indexing</dt><dd>Index, reviewed</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Core idea</h2>
    <p>Purchase requisition is the first document in the procure-to-pay chain. It captures internal demand but does not yet commit the organization to a supplier. When a PR is blocked, cannot be created, or fails conversion, the support goal is to identify whether the issue is in master data, account assignment, sourcing, release strategy, or user authorization.</p>
    <p>Most PR failures are not system errors: they are missing account assignments, unextended materials, or incomplete release strategies surfacing at the first document in the chain.</p>

    <h2>Common symptoms</h2>
    <ul>
      <li>ME51N fails to save or shows a hard error.</li>
      <li>PR is created but cannot be converted to PO (ME59N or ME21N).</li>
      <li>PR remains in status 'release strategy active' and cannot be approved.</li>
      <li>MRP-generated PR has wrong plant, quantity, or delivery date.</li>
      <li>PR account assignment is rejected during posting or conversion.</li>
    </ul>

    <h2>Likely causes</h2>
    <ul>
      <li><strong>Master data issue:</strong> material not extended to plant, supplier blocked, or purchasing organization mismatch.</li>
      <li><strong>Account assignment error:</strong> cost center, WBS element, or GL account is invalid or not open for posting.</li>
      <li><strong>Release strategy block:</strong> the PR value or material group triggers an approval path that is not complete.</li>
      <li><strong>Source determination failure:</strong> no valid info record, source list, or quota arrangement exists for automatic sourcing.</li>
      <li><strong>Authorization issue:</strong> the user lacks authorization to create PRs for the plant, material group, or account assignment type.</li>
      <li><strong>MRP parameter issue:</strong> lot size, safety stock, or planning horizon produced an unexpected PR quantity or date.</li>
    </ul>

    <h2>Where to check in SAP</h2>
    <ul>
      <li>ME53N — display PR and check status, account assignment, and source of supply.</li>
      <li>ME59N log — automatic PO creation rejection reasons.</li>
      <li>ME54N — PR release status.</li>
      <li>MD04 / MD05 — MRP list to see how the PR was generated.</li>
      <li>SU53 — authorization check after a failed transaction.</li>
    </ul>

    <h2>Key tables / transactions / objects</h2>
    <ul>
      <li><strong>EBAN / EBKN</strong> — PR header and items.</li>
      <li><strong>EKKO / EKPO</strong> — PO header and items (for converted PRs).</li>
      <li><strong>AUFK</strong> — WBS / internal order master.</li>
      <li><strong>CSKS</strong> — cost center master.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <ol>
      <li>Identify the PR number and the exact error or status that blocks progress.</li>
      <li>Check ME53N for PR details: material, plant, quantity, account assignment, and source of supply.</li>
      <li>Verify master data: material plant extension, supplier status, and purchasing organization.</li>
      <li>Check release status if the PR is blocked for approval.</li>
      <li>Check MRP parameters if the PR was system-generated and has unexpected values.</li>
      <li>Test manual PO creation (ME21N) from the PR to isolate conversion issues.</li>
    </ol>

    <h2>Typical fixes or next actions</h2>
    <ul>
      <li>Correct the account assignment if the cost center or WBS element is wrong.</li>
      <li>Extend the material to the plant or unblock the supplier master.</li>
      <li>Complete the release strategy approval if the PR is blocked.</li>
      <li>Create or update the source of supply if automatic sourcing fails.</li>
      <li>Adjust MRP parameters if system-generated PRs are consistently wrong.</li>
    </ul>

    <h2>What to capture first</h2>
    <p>PR blocks are usually upstream master data or account assignment problems. Capture: PR number, material, plant, error message, account assignment, and whether the issue is isolated or recurring.</p>

    <h2>When the PR came from MRP</h2>
    <p>If the requisition was system-generated, treat it as an MRP exception. Verify the exception message in MD04/MD05, then check whether the root cause is a demand signal change, a supply delay, or a planning parameter in the material master. For a full diagnostic frame, see <a href="/atlas/diagnostics/sap-mrp-exception-diagnostics/">SAP MRP Exception Diagnostics</a>.</p>

    <h2>Escalation signals</h2>
    <ul>
      <li>Requisitions are stuck across multiple users or plants, suggesting a release strategy or workflow failure.</li>
      <li>The requested material or service has no approved source, contract, or budget approval.</li>
      <li>MRP-generated requisitions repeatedly have wrong quantities, dates, or source of supply.</li>
      <li>The case requires a change to sourcing policy, approval limits, or procurement governance.</li>
    </ul>

    <h2>Boundaries and non-goals</h2>
    <p>This page is a diagnostic frame, not a PR configuration guide. It does not cover MRP logic, approval workflow design, or catalog integration. It does not replace SAP's purchasing documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Atlas Pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-purchase-order-creation-diagnostics/">SAP Purchase Order Creation Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-release-strategy-diagnostics/">SAP Release Strategy Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-source-determination-diagnostics/">SAP Source Determination Diagnostics</a></li>
      <li><a href="/atlas/diagnostics/sap-mrp-exception-diagnostics/">SAP MRP Exception Diagnostics</a></li>
      <li><a href="/atlas/sap/sap-mm-procurement-overview/">SAP Mm Procurement Overview</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
