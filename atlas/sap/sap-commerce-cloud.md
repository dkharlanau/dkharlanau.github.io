---
layout: default
title: "SAP Commerce Cloud"
description: "SAP's B2B and B2C e-commerce platform (formerly Hybris) — catalog, pricing, order management, and omnichannel storefronts."
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
last_reviewed: 2026-07-14
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
    <p class="note-subtitle">SAP's B2B and B2C e-commerce platform (formerly Hybris) — catalog, pricing, order management, and omnichannel storefronts.</p>
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
    <h2>What it is</h2>
    <p>SAP Commerce Cloud is SAP's e-commerce platform for complex B2B and B2C selling — the product formerly known as Hybris. It handles the product catalog, pricing, promotions, order management, and the storefront layer. It is built for scenarios where the buying journey is too involved for a simple web shop: contract pricing, approval workflows, punchout, and multi-site catalogs.</p>

    <h2>Business purpose</h2>
    <p>Give customers a digital channel to find products, see the right price, and place orders that flow cleanly into fulfillment. For B2B, the point is to mirror the negotiated commercial terms — customer-specific assortments and prices — rather than a generic retail catalog.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Commerce Cloud is a front-end sales channel. It is not the system of record for fulfillment — it connects to S/4HANA for order capture handoff, pricing, and inventory availability. The catalog and customer data typically originate in backend systems and are replicated into Commerce.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Product catalog — categories, products, variants, media, classifications.</li>
      <li>Price lists and customer-specific price rows.</li>
      <li>Customer segments and accounts.</li>
      <li>Shopping carts and saved carts.</li>
      <li>Orders and order history.</li>
      <li>Promotions and vouchers.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA — order-to-cash handoff, pricing, and ATP checks.</li>
      <li>SAP Customer Data Cloud — identity and consent management.</li>
      <li>Payment gateways — authorization and capture.</li>
      <li>Content delivery networks — storefront performance and caching.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Extension and addon model — custom business logic and integrations.</li>
      <li>Composable storefront (Spartacus) — headless Angular storefront.</li>
      <li>REST/OCC APIs — integrate external touchpoints and services.</li>
      <li>Side-by-side — BTP services for search, personalization, and orchestration.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Order sync logs — which orders reached S/4HANA and which failed.</li>
      <li>Catalog replication jobs — product and price import status.</li>
      <li>Pricing cache health — stale or inconsistent price resolution.</li>
      <li>Storefront performance — page load and checkout latency.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Handles genuinely complex B2B selling models out of the box.</li>
      <li>Tight order-to-cash alignment with S/4HANA.</li>
      <li>Mature catalog and promotion engine.</li>
      <li>Headless option for custom storefronts.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Implementation is heavy — catalog and pricing modeling takes real effort.</li>
      <li>Pricing logic duplicated between Commerce and S/4HANA drifts easily.</li>
      <li>Upgrade and addon compatibility burden on a large codebase.</li>
      <li>Performance tuning is non-trivial under catalog volume.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Catalog sync failures between Commerce and S/4HANA.</li>
      <li>Pricing discrepancies between storefront and backend.</li>
      <li>Order import errors into S/4HANA.</li>
      <li>Session and cart abandonment issues under load.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/sap-product-portfolio/">SAP Product Portfolio</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Commerce Cloud product documentation — SAP Help Portal (help.sap.com), public-safe topic discovery only.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Specific storefront options, licensing, and integration patterns must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
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
