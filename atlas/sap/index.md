---
author: "Dzmitryi Kharlanau"
layout: default
title: "Atlas SAP Section — Configuration and Support Concepts"
description: "Curated SAP support and configuration explanations with conservative boundaries."
permalink: /atlas/sap/
last_modified_at: 2026-07-14
status: reviewed
verified: true
tags:
  - sap
  - sap-ams
  - configuration
related:
  - /atlas/concepts/sap-atp-is-not-inventory/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/ai-operations/authorization-aware-ai-for-sap/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li aria-current="page">SAP</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">SAP Section</p>
  <h1>SAP concepts with enough context to diagnose, not enough false certainty to mislead.</h1>
  <p class="lead">This section is for practical SAP support and configuration explanations. It avoids release-specific certainty unless a claim has been verified against public vendor documentation.</p>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Pilot Page</p>
    <h2>Reviewed SAP topic</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/sap/sap-pricing-procedure-debugging/">
      <h2>SAP Pricing Procedure Debugging</h2>
      <p>A support-oriented frame for checking where pricing went wrong without assuming every landscape follows the same configuration.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-partner-determination-failures/">
      <h2>SAP Partner Determination Failures</h2>
      <p>Diagnose missing or wrong sold-to, ship-to, bill-to, payer, or related partner roles.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-item-category-determination/">
      <h2>SAP Item Category Determination</h2>
      <p>Why a small item category value can change pricing, delivery, billing, and schedule behavior.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/gr-ir-clearing-explained/">
      <h2>SAP GR/IR Clearing Explained</h2>
      <p>The accounting bridge between received goods and supplier invoices.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-mm-procurement-overview/">
      <h2>SAP MM Procurement Overview</h2>
      <p>The procure-to-pay chain in SAP MM, where it breaks, and what to check first.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-pricing-condition-technique/">
      <h2>SAP Pricing Condition Technique</h2>
      <p>How SAP assembles a sales price from conditions, and why the chain breaks more often than individual settings.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-account-determination-diagnostics/">
      <h2>SAP Account Determination Diagnostics</h2>
      <p>A first-pass structure for finding why a sales transaction posts to the wrong revenue or clearing account.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Product Portfolio</p>
    <h2>SAP products — what they do and where they fit</h2>
  </header>
  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/sap/sap-product-portfolio/">
      <h2>SAP Product Portfolio</h2>
      <p>Every major SAP product organized by category, with plain-language notes on what each one does and who it is for.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-successfactors/">
      <h2>SAP SuccessFactors</h2>
      <p>Cloud HCM suite — core HR, talent management, payroll, and workforce analytics.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-commerce-cloud/">
      <h2>SAP Commerce Cloud</h2>
      <p>B2B and B2C e-commerce platform (formerly Hybris) — catalog, pricing, order management, omnichannel.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-concur/">
      <h2>SAP Concur</h2>
      <p>Travel and expense management — expense reporting, travel booking, invoice processing.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-fieldglass/">
      <h2>SAP Fieldglass</h2>
      <p>External workforce management — contingent workers, consultants, service procurement.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-business-one/">
      <h2>SAP Business One</h2>
      <p>ERP for small businesses — finance, sales, purchasing, inventory, light manufacturing.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-grc/">
      <h2>SAP GRC</h2>
      <p>Governance, risk, and compliance — access control, SoD analysis, automated monitoring, audit readiness.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/sap-business-network/">
      <h2>SAP Business Network</h2>
      <p>B2B collaboration network — supplier catalogs, logistics coordination, asset data sharing.</p>
      <span class="link-arrow">Read SAP page</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Related</p>
    <h2>Related Atlas pages</h2>
  </header>
  <ul>
    <li><a href="/atlas/concepts/sap-atp-is-not-inventory/">SAP ATP Is Not Inventory</a></li>
    <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
    <li><a href="/atlas/ai-operations/authorization-aware-ai-for-sap/">Authorization-Aware AI for SAP</a></li>
  </ul>
</section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
