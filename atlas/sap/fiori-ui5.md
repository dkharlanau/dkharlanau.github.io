---
layout: default
title: "Fiori / UI5"
description: "SAP Fiori and SAPUI5 explained: the UX design system, UI framework, Fiori elements, OData consumption, and launchpad context."
permalink: /atlas/sap/fiori-ui5/
atlas_section: sap
domain: SAP operations
subdomain: User experience
concept_type: technology
sap_area: "Fiori / UI5"
business_process: "User interface"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
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
    <p class="note-subtitle">SAP Fiori defines the user-experience model; SAPUI5 provides a web UI technology used to build many Fiori applications.</p>
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
    <p>SAP Fiori and SAPUI5 are closely related, but they are not the same thing. <strong>SAP Fiori</strong> is SAP's user-experience concept and design system. It defines principles such as role-based, adaptive, simple, and coherent interaction. <strong>SAPUI5</strong> is a client-side web UI technology based on JavaScript, CSS, and HTML5 that SAP uses to build many business applications.</p>

    <h2>Fiori describes how the experience should work</h2>
    <p>The Fiori design language is concerned with the user's task, information hierarchy, navigation, interaction patterns, visual consistency, and behavior across devices. It is therefore broader than a particular JavaScript library. A screen does not become a good Fiori application simply because it uses SAPUI5 controls.</p>

    <p>This distinction is useful in projects. A technical implementation can be correct while the user journey is still poor. Conversely, a clear Fiori design still needs an appropriate application architecture, data service, authorization model, and frontend implementation.</p>

    <h2>SAPUI5 is the application framework</h2>
    <p>SAPUI5 applications run in the browser. The framework provides UI controls, data binding, routing, component concepts, internationalization, accessibility support, and other capabilities needed for enterprise web applications. It can bind controls to different model types; OData is especially important in SAP business applications.</p>

    <p>In a freestyle SAPUI5 application, developers control the views, controllers, navigation, and application behavior directly. That gives flexibility, but it also means the project owns more frontend code and more design decisions.</p>

    <h2>Fiori elements moves more of the UI into metadata and annotations</h2>
    <p>SAP Fiori elements provides predefined application patterns such as list report and object page. Instead of coding every view from scratch, developers expose an OData service with metadata and annotations. The SAPUI5 runtime interprets that information and supplies much of the standard UI behavior.</p>

    <p>This is not the same as “no-code.” The backend service still needs a sound data model, semantics, actions, authorizations, and annotations. Extensions may still be required. The benefit is that standard application structure and behavior can be reused rather than recreated independently in every app.</p>

    <h2>The launchpad is the entry point, not the application logic</h2>
    <p>In many SAP landscapes, users reach Fiori applications through SAP Fiori launchpad or a related SAP workspace experience. The shell provides navigation and role-oriented access to applications. The application itself still has its own frontend runtime and backend services.</p>

    <p>Classic applications can also be launched from a Fiori launchpad. That is another reason not to equate “launchpad” with “Fiori app.” A SAP GUI or Web Dynpro application may be reachable from the same entry point without becoming a native Fiori application.</p>

    <h2>OData often connects the UI to the business service</h2>
    <p>Many Fiori applications consume OData services. In modern ABAP development, RAP can expose business services through OData service bindings; SAPUI5 or Fiori elements then consumes those services in the browser. The frontend and backend remain separate layers: a rendering problem, an OData contract problem, and a backend business-rule problem can produce very different symptoms even when they appear on the same screen.</p>

    <p>When we investigate a Fiori issue, that separation is more useful than starting from a long transaction-code checklist. First identify whether the failure belongs to navigation and content assignment, the frontend application, the OData request, authorization, or backend processing. The visible page is only the last layer in the chain.</p>

    <h2>Fiori is not a universal replacement for every classic UI</h2>
    <p>SAP Fiori is the strategic UX direction for many SAP products, but real landscapes still contain SAP GUI, Web Dynpro, and other technologies. The sensible question is not whether every old screen must disappear immediately. It is which user tasks benefit from a Fiori experience, which standard applications already exist, and where custom development or extension is justified.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/22bbe89ef68b4d0e98d05f0d56a7f6c8/85f167b1da3d46d98e26cf4cac4430f8.html">SAP Fiori Concept and Design</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_FIORI_OVERVIEW/a1482918da994432859015bf1a083d9b/b6edae41c9d64c4680c3c375063f016c.html">Develop SAP Fiori Apps with SAP Fiori Elements</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_NETWEAVER_AS_ABAP_FOR_SOH_740/468a97775123488ab3345a0c48cadd8f/b0569518-c059-4489-a3bc-da59043c92d9.html">UI Development Toolkit for HTML5 (SAPUI5)</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Available Fiori apps, launchpad/workspace products, SAPUI5 versions, supported floorplans, extension mechanisms, and deployment options vary by SAP product and release. Verify the target landscape before treating an implementation pattern as universal.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
      <li><a href="/atlas/sap/odata/">OData</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/rap/">RAP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
