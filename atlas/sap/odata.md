---
layout: default
title: "OData"
description: "Analytical overview of OData in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/odata/
atlas_section: sap
domain: SAP operations
subdomain: API protocol
concept_type: technology
sap_area: "OData"
business_process: "System integration"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - odata
  - api
  - integration
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/cds-views/
  - /atlas/sap/rap/
  - /atlas/sap/cap/
  - /atlas/sap/fiori-ui5/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">OData</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>OData</h1>
    <p class="note-subtitle">RESTful API protocol for SAP data access, Fiori, and third-party integration.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>System integration</dd></div>
      <div><dt>SAP area</dt><dd>OData</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>OData (Open Data Protocol) is SAP's standard RESTful API protocol for exposing and consuming business data. It provides a uniform way to query, create, update, and delete data via HTTP, with metadata-driven service definitions.</p>

    <h2>Business purpose</h2>
    <p>Enable real-time data access for Fiori apps, third-party integrations, and mobile applications. Replace RFC and SOAP for modern, web-friendly integration patterns.</p>

    <h2>Where it sits in the landscape</h2>
    <p>OData is the primary API layer for S/4HANA and BTP. It sits between the backend (CDS views, business objects) and consumers (Fiori, mobile apps, external systems). SAP Gateway or Cloud Integration handles the protocol translation.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Service metadata: entity types, properties, navigation, associations.</li>
      <li>Entity set: collection of business objects (sales orders, materials).</li>
      <li>Navigation property: linked entities (order → items → schedule lines).</li>
      <li>Query options: $filter, $expand, $select, $orderby, $top, $skip.</li>
      <li>Batch request: multiple operations in a single HTTP call.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: CDS-based OData services, custom OData services.</li>
      <li>BTP: CAP-generated OData, API management.</li>
      <li>Fiori: UI5 apps consuming OData via data binding.</li>
      <li>External: third-party ERP, CRM, mobile apps, Power BI.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom OData services from CDS or RFC.</li>
      <li>Custom query options and filters.</li>
      <li>Side-by-side apps on BTP consuming OData.</li>
      <li>API policies via Integration Suite.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Service performance: response time, throughput, error rate.</li>
      <li>Query complexity: expand depth, filter selectivity.</li>
      <li>Authentication: token, SAML, OAuth failures.</li>
      <li>Gateway health: SAP Gateway or Cloud Integration status.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Standard REST protocol with broad tool support.</li>
      <li>Metadata-driven, self-describing services.</li>
      <li>Deep navigation for complex business objects.</li>
      <li>Native Fiori and UI5 integration.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Deep $expand queries degrade performance.</li>
      <li>Large result sets without pagination cause timeouts.</li>
      <li>Complex filter expressions are hard to optimize.</li>
      <li>Version compatibility between OData 2.0, 4.0, and SAP extensions.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>OData timeout — deep expand, large volume, or missing filter.</li>
      <li>404 Not Found — entity set or navigation property mismatch.</li>
      <li>401 Unauthorized — token expired, role missing, or SAML issue.</li>
      <li>500 Internal Error — backend dump or metadata mismatch.</li>
      <li>Batch request failed — partial success, rollback issue.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. OData service availability, version, and performance characteristics vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
