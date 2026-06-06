---
layout: default
title: "Fiori / UI5"
description: "Analytical overview of Fiori and UI5 in SAP: what they are, where they sit, and how they break."
permalink: /atlas/sap/fiori-ui5/
atlas_section: sap
domain: SAP operations
subdomain: User experience
concept_type: technology
sap_area: "Fiori / UI5"
business_process: "User interface"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - fiori
  - ui5
  - user-experience
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/odata/
  - /atlas/sap/cds-views/
  - /atlas/sap/rap/
  - /atlas/sap/cap/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Fiori / UI5</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Fiori / UI5</h1>
    <p class="note-subtitle">SAP's design system and UI framework for modern web and mobile applications.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>User interface</dd></div>
      <div><dt>SAP area</dt><dd>Fiori / UI5</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP Fiori is SAP's design system for enterprise applications. SAP UI5 (SAPUI5 / OpenUI5) is the JavaScript framework that implements Fiori designs. Together they provide a consistent, role-based user experience across S/4HANA, BTP, and satellite products.</p>

    <h2>Business purpose</h2>
    <p>Replace SAP GUI with modern, web-based, responsive applications. Provide role-based access to tasks and data. Improve user adoption and reduce training time.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Fiori/UI5 is the presentation layer. It consumes OData services from S/4HANA (RAP, CDS) and BTP (CAP). It runs in browsers and mobile devices, managed by the Fiori Launchpad or BTP Launchpad.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Fiori app: standalone or launchpad-based application.</li>
      <li>UI5 view: XML, JavaScript, or JSON view definition.</li>
      <li>Controller: JavaScript logic for user interaction.</li>
      <li>Component: reusable UI5 application container.</li>
      <li>Launchpad: role-based entry point with catalogs and groups.</li>
      <li>Target mapping: navigation from launchpad to app.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: OData services from CDS, RAP, custom.</li>
      <li>BTP: CAP-generated OData, cloud services.</li>
      <li>Identity: SAML, OAuth, SAP Cloud Identity.</li>
      <li>Mobile: SAP Mobile Services, offline sync.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom Fiori apps (freestyle or Fiori elements).</li>
      <li>App extensions: custom fields, actions, views.</li>
      <li>Launchpad customization: catalogs, groups, themes.</li>
      <li>Side-by-side apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>App performance: load time, rendering, data fetch.</li>
      <li>OData errors: 404, 500, timeout, metadata mismatch.</li>
      <li>Launchpad: tile visibility, target mapping, cache.</li>
      <li>Browser console: JavaScript errors, network failures.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Consistent design language across SAP products.</li>
      <li>Responsive and mobile-ready.</li>
      <li>Deep integration with OData and CDS annotations.</li>
      <li>Role-based access via launchpad.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>UI5 library updates can break existing apps.</li>
      <li>Performance depends on OData service quality.</li>
      <li>Role and authorization redesign is required for launchpad.</li>
      <li>Custom apps require frontend development skills.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>App not visible in launchpad — catalog, group, or target mapping.</li>
      <li>Blank tile or screen — OData error, metadata, or authorization.</li>
      <li>App slow — large data set, deep expand, or missing filter.</li>
      <li>UI5 version conflict — after library update or patch.</li>
      <li>Mobile sync failure — offline store or network issue.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Fiori app availability, UI5 versions, and launchpad configuration vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
