---
layout: default
title: "SAP Technology Landscape Map"
description: "A landscape map of SAP technologies, platforms, and development frameworks for operational navigation."
permalink: /atlas/maps/sap-technology-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: Technology landscape
concept_type: map
sap_area: "SAP technology stack"
business_process: "Enterprise operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-technology
  - landscape-map
  - development
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-btp/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">SAP Technology Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>SAP technology landscape map</h1>
    <p class="note-subtitle">A navigation frame for SAP technologies, platforms, and development frameworks.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology positioning and framework claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>A technology-level view of the SAP stack. It separates runtime platforms, development frameworks, data access technologies, and user interface layers.</p>

    <h2>Business purpose</h2>
    <p>Help architects and developers choose the right technology for an extension, integration, or reporting requirement without defaulting to legacy patterns.</p>

    <h2>Runtime platforms</h2>
    <ul>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a> — traditional ABAP runtime in S/4HANA (on-premise and private cloud).</li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a> — cloud-ready ABAP development model with restricted language scope.</li>
    </ul>

    <h2>Development frameworks</h2>
    <ul>
      <li><a href="/atlas/sap/rap/">RAP</a> — RESTful Application Programming model for in-app extensions.</li>
      <li><a href="/atlas/sap/cap/">CAP</a> — Cloud Application Programming model for side-by-side extensions on BTP.</li>
    </ul>

    <h2>Data access and modeling</h2>
    <ul>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a> — Core Data Services for semantic data modeling and analytics.</li>
      <li><a href="/atlas/sap/odata/">OData</a> — protocol for API exposure and Fiori data access.</li>
    </ul>

    <h2>User experience</h2>
    <ul>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a> — SAP's design system and UI framework for web and mobile.</li>
    </ul>

    <h2>Where they sit</h2>
    <p>ABAP Platform and ABAP Cloud are the runtime foundations. RAP and CAP are the development models. CDS Views and OData are the data access layer. Fiori/UI5 is the presentation layer. BTP hosts side-by-side extensions; S/4HANA hosts in-app extensions.</p>

    <h2>Extension decision frame</h2>
    <ul>
      <li>In-app, S/4HANA-hosted → ABAP Cloud + RAP + CDS.</li>
      <li>Side-by-side, BTP-hosted → CAP + OData + Fiori.</li>
      <li>Reporting-only → CDS Views + Datasphere + Analytics Cloud.</li>
      <li>Third-party integration → OData APIs + Business Events.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Clean separation between core and extensions.</li>
      <li>Modern development models (RAP, CAP) reduce boilerplate.</li>
      <li>CDS provides a unified semantic layer for transactions and analytics.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>ABAP Cloud restrictions can block legacy custom code migration.</li>
      <li>Steep learning curve from classical ABAP to RAP/CAP.</li>
      <li>Fiori adoption requires role redesign and change management.</li>
      <li>Version compatibility between UI5, gateway, and backend.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Custom RAP service fails after S/4HANA upgrade due to API changes.</li>
      <li>Fiori app shows blank tiles after UI5 library update.</li>
      <li>OData timeout on large CDS view result sets.</li>
      <li>ABAP Cloud authorization object changes blocking custom apps.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Technology descriptions are based on public SAP documentation and community knowledge. Release-specific behavior, supported feature sets, and compatibility matrices must be verified against the customer's S/4HANA release and BTP subaccount configuration.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
