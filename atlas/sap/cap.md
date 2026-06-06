---
layout: default
title: "CAP"
description: "Analytical overview of CAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/cap/
atlas_section: sap
domain: SAP operations
subdomain: Cloud development
concept_type: technology
sap_area: "CAP"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - cap
  - cloud-development
  - side-by-side
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-cloud/
  - /atlas/sap/odata/
  - /atlas/sap/fiori-ui5/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CAP</h1>
    <p class="note-subtitle">Cloud Application Programming model for side-by-side extensions on SAP BTP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>CAP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>CAP (Cloud Application Programming Model) is SAP's framework for building enterprise-grade applications on BTP. It supports Node.js and Java runtimes, provides a declarative data model (CDS), and generates OData services, database schemas, and Fiori UIs.</p>

    <h2>Business purpose</h2>
    <p>Build side-by-side extensions that keep S/4HANA core clean. Rapidly prototype and deploy business apps that integrate with SAP and non-SAP systems via OData, events, and REST.</p>

    <h2>Where it sits in the landscape</h2>
    <p>CAP runs on SAP BTP (Cloud Foundry or Kyma). It consumes S/4HANA data via OData and events, and can also integrate with Datasphere, Integration Suite, and external APIs. It is the side-by-side counterpart to RAP's in-app model.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>CDS model: entities, associations, annotations.</li>
      <li>Service: OData auto-generated from CDS model.</li>
      <li>Handler: custom business logic in Node.js or Java.</li>
      <li>Database: HANA Cloud, SQLite (dev), PostgreSQL.</li>
      <li>App: Fiori elements or freestyle UI5.</li>
      <li>Event: consumption and production of business events.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData, events, destinations.</li>
      <li>BTP: HANA Cloud, Integration Suite, AI Core.</li>
      <li>External: REST, SOAP, OData, message queues.</li>
      <li>Fiori: UI5 apps via generated OData services.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom handlers and service implementations.</li>
      <li>Custom event processing.</li>
      <li>Side-by-side data models extending S/4HANA entities.</li>
      <li>Integration with external AI/ML services.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Application logs: Cloud Foundry app logs, Kibana.</li>
      <li>Service performance: OData response time, throughput.</li>
      <li>Database: HANA Cloud query performance, connection pool.</li>
      <li>Event processing: lag, errors, retry.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Rapid development with generated OData and database layers.</li>
      <li>Cloud-native, elastic scaling on BTP.</li>
      <li>Multi-runtime support (Node.js, Java).</li>
      <li>Keeps S/4HANA core completely clean.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Latency between BTP and on-premise S/4HANA.</li>
      <li>Cloud connector dependency for on-premise access.</li>
      <li>Eventual consistency for event-driven architectures.</li>
      <li>Learning curve for ABAP developers new to Node.js/Java.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>App crash — memory limit, dependency failure, or unhandled exception.</li>
      <li>OData service error — destination, authentication, or schema mismatch.</li>
      <li>Event not processed — subscription, mapping, or handler error.</li>
      <li>Database connection pool exhausted — HANA Cloud limit.</li>
      <li>Cloud connector down — on-premise S/4HANA unreachable.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. CAP features, supported runtimes, and BTP services vary by release and must be verified against SAP's current documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
