---
layout: default
title: "ABAP Cloud"
description: "Analytical overview of ABAP Cloud: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/abap-cloud/
atlas_section: sap
domain: SAP operations
subdomain: Cloud development
concept_type: technology
sap_area: "ABAP Cloud"
business_process: "Platform and development"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - abap-cloud
  - cloud-development
  - clean-core
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/abap-platform/
  - /atlas/sap/rap/
  - /atlas/sap/cds-views/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">ABAP Cloud</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>ABAP Cloud</h1>
    <p class="note-subtitle">Cloud-ready ABAP development model with restricted language scope for Clean Core.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Platform and development</dd></div>
      <div><dt>SAP area</dt><dd>ABAP Cloud</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>ABAP Cloud is a restricted ABAP development model designed for cloud readiness and Clean Core compliance. It limits language constructs that break upgrade stability, enforces API-based access, and supports both in-app and side-by-side extensions.</p>

    <h2>Business purpose</h2>
    <p>Enable custom development that survives upgrades without modification. Keep the S/4HANA core stable by restricting direct database access, dynpro usage, and other legacy patterns.</p>

    <h2>Where it sits in the landscape</h2>
    <p>ABAP Cloud runs within S/4HANA (in-app) and on BTP (side-by-side). It is the development model for RAP business objects and CAP services. It replaces classical ABAP for new extensions.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>ABAP Cloud project: development artifact with restricted scope.</li>
      <li>Released APIs: stable, versioned interfaces for custom code.</li>
      <li>Extension points: CDS extensions, BAdIs, custom fields.</li>
      <li>Business objects: RAP entities with behavior definition.</li>
      <li>Service bindings: OData, REST, UI5 exposure.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: in-app extensions via released APIs.</li>
      <li>BTP: side-by-side extensions via CAP and RAP.</li>
      <li>Fiori: UI5 apps consuming ABAP Cloud services.</li>
      <li>External: OData, REST, events.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom business objects with RAP.</li>
      <li>CDS view extensions.</li>
      <li>Custom fields and logic via extension points.</li>
      <li>Side-by-side apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>ABAP Cloud readiness check: custom code analysis.</li>
      <li>Released API usage: compliance with stable interfaces.</li>
      <li>Service performance: OData response time, throughput.</li>
      <li>Extension stability: upgrade impact analysis.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Upgrade-stable custom code via released APIs.</li>
      <li>Modern language features and development tools.</li>
      <li>Unified with RAP for business object development.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Restricted language scope blocks some legacy patterns.</li>
      <li>Migration from classical ABAP is non-trivial.</li>
      <li>Released API coverage may not cover all use cases.</li>
      <li>Steep learning curve for classical ABAP developers.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Custom service fails after upgrade — API change or deprecation.</li>
      <li>ABAP Cloud readiness check flags critical custom code.</li>
      <li>Performance issue — inefficient CDS view or service implementation.</li>
      <li>Authorization failure — new authorization object in restricted model.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. ABAP Cloud availability, restrictions, and released APIs vary by S/4HANA release and deployment option.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/abap-platform/">ABAP Platform</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
