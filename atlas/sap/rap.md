---
layout: default
title: "RAP"
description: "Analytical overview of RAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/rap/
atlas_section: sap
domain: SAP operations
subdomain: Development framework
concept_type: technology
sap_area: "RAP"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - rap
  - abap-cloud
  - development
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/abap-cloud/
  - /atlas/sap/cds-views/
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
    <li aria-current="page">RAP</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>RAP</h1>
    <p class="note-subtitle">RESTful Application Programming model for in-app extensions in S/4HANA.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>RAP</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>RAP (RESTful Application Programming Model) is SAP's framework for building business objects and services in S/4HANA. It combines CDS views for data modeling, behavior definitions for business logic, and service bindings for OData exposure.</p>

    <h2>Business purpose</h2>
    <p>Enable structured, upgrade-stable development of custom business objects inside S/4HANA. Reduce boilerplate by generating persistence, validation, and service layers from declarative definitions.</p>

    <h2>Where it sits in the landscape</h2>
    <p>RAP sits within ABAP Cloud in S/4HANA. It is the recommended development model for in-app extensions, custom business objects, and Fiori app backends. It replaces BOPF and legacy custom development patterns.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>CDS entity: data model with associations and annotations.</li>
      <li>Behavior definition: create, update, delete, validation, determination.</li>
      <li>Behavior implementation: ABAP classes for custom logic.</li>
      <li>Service definition: OData service metadata.</li>
      <li>Service binding: UI or Web API exposure.</li>
      <li>Draft handling: temporary data before activation.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: in-app extensions, custom business objects.</li>
      <li>Fiori: UI5 apps via OData services.</li>
      <li>BTP: side-by-side consumption of RAP services.</li>
      <li>External: OData APIs for third-party access.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom entities and behavior definitions.</li>
      <li>Custom validations and determinations.</li>
      <li>Service extensions and custom actions.</li>
      <li>Side-by-side apps consuming RAP OData services.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Service performance: OData response time, throughput.</li>
      <li>Draft stability: lock conflicts, activation failures.</li>
      <li>Behavior implementation errors: validation, determination.</li>
      <li>Upgrade impact: API stability, deprecated features.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Declarative development reduces boilerplate.</li>
      <li>Upgrade-stable via released APIs and ABAP Cloud.</li>
      <li>Native Fiori integration via OData and annotations.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Learning curve from classical ABAP to declarative model.</li>
      <li>Draft handling complexity for multi-user scenarios.</li>
      <li>Debugging is different from classical ABAP.</li>
      <li>Not all S/4HANA objects have RAP equivalents yet.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Custom RAP service fails after upgrade — behavior or annotation change.</li>
      <li>Draft lock conflict — user cannot edit, activation blocked.</li>
      <li>OData metadata mismatch — UI5 app fails to load.</li>
      <li>Validation error — custom logic rejecting valid data.</li>
      <li>Performance degradation — inefficient CDS view or association.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. RAP availability, features, and supported objects vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/abap-cloud/">ABAP Cloud</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
