---
layout: default
title: "CDS Views"
description: "Analytical overview of CDS Views: what they are, where they sit, and how they break."
permalink: /atlas/sap/cds-views/
atlas_section: sap
domain: SAP operations
subdomain: Data modeling
concept_type: technology
sap_area: "CDS"
business_process: "Data access and analytics"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - cds-views
  - data-modeling
  - analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/rap/
  - /atlas/sap/odata/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CDS Views</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CDS Views</h1>
    <p class="note-subtitle">Core Data Services for semantic data modeling in SAP S/4HANA and BTP.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Data access and analytics</dd></div>
      <div><dt>SAP area</dt><dd>CDS</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>CDS (Core Data Services) Views are semantic data models that define how data is structured, related, and exposed in SAP systems. They serve as the foundation for transactional applications (RAP), analytics (Datasphere, Analytics Cloud), and API exposure (OData).</p>

    <h2>Business purpose</h2>
    <p>Provide a unified, business-friendly data layer that replaces direct table access. Enable consistent data definitions across transactions, reports, and integrations.</p>

    <h2>Where it sits in the landscape</h2>
    <p>CDS Views sit between the database (HANA) and consumers: Fiori apps, OData services, analytical tools, and custom programs. They are defined in ABAP (for S/4HANA) and in CAP (for BTP).</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>CDS entity: table-like view with fields, associations, annotations.</li>
      <li>Association: relationship between entities (1:1, 1:n).</li>
      <li>Annotation: UI, analytics, search, and service metadata.</li>
      <li>Projection: subset or transformation of a base entity.</li>
      <li>Extension: adding fields to a released CDS view.</li>
      <li>Table function: HANA-specific calculation logic.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: RAP business objects, analytical queries, custom reports.</li>
      <li>Datasphere: replication, remote access, semantic modeling.</li>
      <li>Analytics Cloud: live connection, import.</li>
      <li>OData: auto-generated service from CDS annotations.</li>
      <li>Fiori: UI5 elements driven by CDS annotations.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom CDS views extending standard views.</li>
      <li>Custom annotations for UI and analytics.</li>
      <li>Table functions for HANA-optimized calculations.</li>
      <li>Side-by-side consumption via OData.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Query performance: execution plan, filter pushdown.</li>
      <li>Association depth: excessive joins causing timeouts.</li>
      <li>Annotation consistency: UI5 rendering, analytics mapping.</li>
      <li>Extension stability: released view changes on upgrade.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Unified semantic layer for transactions and analytics.</li>
      <li>Declarative modeling reduces boilerplate SQL.</li>
      <li>Annotations drive UI and service generation.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Complex CDS views with deep associations perform poorly.</li>
      <li>Annotation errors are hard to debug.</li>
      <li>Released view changes can break extensions.</li>
      <li>HANA-specific features limit portability.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>CDS view timeout — missing filter, deep association, or large volume.</li>
      <li>Annotation mismatch — UI5 app not rendering expected fields.</li>
      <li>OData metadata error — CDS annotation or association issue.</li>
      <li>Extension broken — released view changed in upgrade.</li>
      <li>Wrong data — association cardinality or filter logic error.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. CDS view availability, annotations, and performance characteristics vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
