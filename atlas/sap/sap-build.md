---
layout: default
title: "SAP Build"
description: "Analytical overview of SAP Build: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-build/
atlas_section: sap
domain: SAP operations
subdomain: Low-code development
concept_type: product
sap_area: "SAP Build"
business_process: "Application development"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-build
  - low-code
  - btp
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
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
    <li aria-current="page">SAP Build</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Build</h1>
    <p class="note-subtitle">Low-code platform on BTP for building apps, automating processes, and designing business sites.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Application development</dd></div>
      <div><dt>SAP area</dt><dd>SAP Build</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP Build is a low-code development platform running on SAP BTP. It enables citizen developers and IT teams to create applications, automate business processes, and design enterprise sites without deep coding expertise.</p>

    <h2>Business purpose</h2>
    <p>Reduce IT backlog by empowering business users to build apps and workflows. Accelerate digital transformation with visual development tools. Provide a unified environment for app creation, process automation, and site design.</p>

    <h2>Where it sits in the landscape</h2>
    <p>SAP Build sits within the SAP BTP ecosystem alongside CAP, Kyma, and Fiori. It connects to S/4HANA for data and processes, and integrates with SAP Integration Suite for cross-system workflows. It is the citizen-developer complement to pro-code tools on BTP.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Apps: mobile and web applications built with visual composers.</li>
      <li>Processes: workflows and automations with forms, rules, and approvals.</li>
      <li>Sites: enterprise portals and intranets (Build Work Zone).</li>
      <li>Forms: data collection interfaces linked to processes and apps.</li>
      <li>Connectors: prebuilt and custom adapters to SAP and non-SAP systems.</li>
      <li>Data models: entities, relationships, and validations for app data.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData services, RFC, business events for data and process.</li>
      <li>BTP: destinations, cloud connector, SAP Integration Suite.</li>
      <li>Fiori: embedded apps and launchpad integration.</li>
      <li>External: REST, SOAP, OData, cloud storage, email.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom connectors for non-standard systems.</li>
      <li>Custom UI components and themes.</li>
      <li>Process extensions with business rules and scripts.</li>
      <li>API integration with side-by-side BTP applications.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>App analytics: usage, performance, errors.</li>
      <li>Process monitoring: instance status, bottlenecks, failures.</li>
      <li>Site analytics: page views, user engagement.</li>
      <li>BTP cockpit: service health, quota, and logs.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Rapid development with visual, drag-and-drop tools.</li>
      <li>Citizen-developer friendly with guardrails and governance.</li>
      <li>Prebuilt connectors reduce integration effort.</li>
      <li>Unified BTP experience with single sign-on and identity.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Complex business logic may exceed low-code capabilities.</li>
      <li>Vendor lock-in to BTP runtime and licensing model.</li>
      <li>Performance limits under high-volume transactional loads.</li>
      <li>Per-user licensing can scale costs quickly.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Connector failure — destination, credential, or network issue.</li>
      <li>Process instance stuck — approval rule or data validation error.</li>
      <li>App deployment error — quota exceeded or dependency missing.</li>
      <li>Permission issue — missing role collection in BTP.</li>
      <li>Data sync lag — OData timeout or large payload.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-product-landscape-map/">SAP Product Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/cap/">CAP</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Build Documentation — <a href="https://help.sap.com/docs/build">help.sap.com/docs/build</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. SAP Build module scope, licensing, and feature availability vary by release and region and must be verified against SAP's current product documentation.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
