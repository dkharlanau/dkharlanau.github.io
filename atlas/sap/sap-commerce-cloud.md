---
layout: default
title: "SAP Commerce Cloud"
description: "SAP Commerce Cloud explained: commerce catalogs, carts and orders, composable storefronts, and the boundary with SAP S/4HANA pricing and fulfillment."
permalink: /atlas/sap/sap-commerce-cloud/
atlas_section: sap
domain: SAP operations
subdomain: Commerce and customer experience
concept_type: product
sap_area: "Commerce Cloud"
business_process: "Order-to-cash"
status: needs_verification
verified: false
last_synced: 2026-07-14
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-commerce-cloud
  - hybris
  - e-commerce
related:
  - /atlas/sap/sap-product-portfolio/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-integration-suite/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Commerce Cloud</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Commerce Cloud</h1>
    <p class="note-subtitle">A commerce platform for presenting products, building carts, calculating commercial terms, and handing customer orders into the fulfillment landscape.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Order-to-cash</dd></div>
      <div><dt>SAP area</dt><dd>Commerce Cloud</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Commerce Cloud is the commerce application behind B2C and B2B digital buying experiences. It manages commerce concepts such as product catalogs, customer accounts, carts, promotions, and orders, and it exposes services that a storefront or another digital channel can use. The older Hybris name still appears in historical material and technical lineage, but the current product is SAP Commerce Cloud.</p>

    <p>The important architectural point is that <strong>commerce does not automatically own every commercial fact</strong>. Product content may be maintained in one system, customer terms in another, pricing may run locally or in an SAP back end, and fulfillment may continue in SAP S/4HANA. A useful design states where each decision is made instead of describing Commerce Cloud simply as “the front end of S/4HANA.”</p>

    <h2>The commerce model exists before the storefront</h2>
    <p>Products and categories are organized in catalogs and catalog versions. Customer accounts and organizational structures can shape what a buyer may see or do. A cart collects the intended purchase before checkout, while an order records the submitted commercial request. Promotions, vouchers, stock information, prices, and delivery choices then participate according to the configured commerce scenario.</p>

    <p>This model supports both consumer and business commerce, but B2B is not just B2C with a company name. Business buying can introduce account structures, permissions, quotes, approval behavior, customer-specific assortment, and negotiated commercial terms. Those requirements affect both the Commerce data model and the integration boundary with the ERP landscape.</p>

    <h2>The storefront can be decoupled from the commerce backend</h2>
    <p>SAP's <strong>Composable Storefront</strong> separates the browser experience from the Commerce Cloud backend. The storefront consumes commerce capabilities through APIs rather than requiring presentation logic to live inside the commerce server. This makes it possible to evolve the customer experience separately while keeping catalog, cart, checkout, and order services behind a stable interface.</p>

    <p>OCC provides REST APIs for commerce capabilities and is a common contract for storefront and external-channel integration. That does not make every extension an API call: Commerce Cloud also has a server-side extension model for domain logic and configuration. We therefore distinguish storefront customization, backend extension, and cross-system integration instead of treating them as one customization layer.</p>

    <h2>Pricing and availability ownership is scenario-specific</h2>
    <p>A common source of confusion is the statement that either Commerce Cloud or S/4HANA “owns pricing.” SAP documents integration patterns where Commerce Cloud calculates prices locally and patterns where prices are requested synchronously from an SAP back end. Current SAP S/4HANA Order Management integration can also support synchronous checks such as stock availability and credit limit at defined catalog or cart stages.</p>

    <p>The consequence is practical: two storefronts can look similar while their runtime dependencies are very different. A locally calculated product page can continue to respond when the ERP is temporarily unavailable; a synchronous pricing or availability call puts the backend and integration path directly on the user's response-time path. We should diagnose wrong prices or slow checkout from the configured ownership model, not from the UI symptom alone.</p>

    <h2>Order capture and fulfillment are another explicit boundary</h2>
    <p>SAP documents both synchronous and asynchronous order-management integration patterns. In an asynchronous pattern, the commerce application can capture and store the order and transfer it to the SAP back end, where fulfillment activities such as shipping and billing continue. Other scenarios use tighter synchronous interaction with the backend during the buying process.</p>

    <p>This is why an order number in Commerce Cloud does not by itself prove that an ERP sales order exists or that fulfillment has started. For an incident, we follow the business document across the boundary: submitted cart, commerce order, outbound integration message or API call, ERP sales order, delivery, goods movement, and billing as applicable. The first missing or inconsistent object is usually more useful than a generic “order sync failed” label.</p>

    <h2>Current Commerce Cloud is a public-cloud product line</h2>
    <p>SAP's current 2211 documentation describes SAP Commerce Cloud 2211 as available for deployment on public-cloud infrastructure. The platform retains an extension-based application model, while release updates and supported integration modules have their own lifecycle and compatibility rules. Older Hybris or on-premise implementation assumptions should therefore not be copied into a current Commerce Cloud design without verification.</p>

    <p>The same caution applies to integration packs and storefront features. A capability may be valid only for a particular Commerce release, order-management pattern, customer type, or separately licensed service. Precise version and scenario names matter more here than a long list of theoretically possible integrations.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Commerce Cloud — <a href="https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/20125f0eca6340dba918bda360e3cdfa/280fc217b07d49c8b64cb4398ded3c7c.html">About SAP Commerce Cloud</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/crm/commerce-cloud/composable-storefront.html">Composable Storefront</a>.</li>
      <li>SAP Commerce Cloud — <a href="https://help.sap.com/docs/SAP_COMMERCE_CLOUD_PUBLIC_CLOUD/3476714bba0b4cb9b3eb58c270e44439/2948414bda21402e95840e93209d1d5d.html">OCC REST API documentation</a>.</li>
      <li>SAP S/4HANA Order Management Integration — <a href="https://help.sap.com/docs/SAP_COMMERCE_INTEGRATIONS/47ad58c1a27447949aad8addbee46fca/1ad1f75d5fe345189d75a2292e748014.html">Synchronous order-management configuration</a>.</li>
      <li>SAP Asynchronous Order Management Integration — <a href="https://help.sap.com/docs/SAP_COMMERCE_INTEGRATIONS/8ce6157b995e418093b6e5410bcd74b2/8bc19f9786691014b849cc9daf31e4d8.html">Functionality in Asynchronous Order Management</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Storefront capabilities, integration modules, pricing and availability patterns, extension compatibility, and commercial entitlements vary by SAP Commerce Cloud release and scenario. Verify the exact Commerce release and ERP integration pattern before using this page as an implementation specification.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-product-portfolio/">SAP Product Portfolio</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
