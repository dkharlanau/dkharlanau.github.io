---
layout: default
title: "SAP Analytics Cloud"
description: "SAP Analytics Cloud explained: stories, models, live and imported data, planning, and its role in an SAP analytics landscape."
permalink: /atlas/sap/sap-analytics-cloud/
atlas_section: sap
domain: SAP operations
subdomain: Business intelligence
concept_type: product
sap_area: "Analytics Cloud"
business_process: "Reporting and analytics"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-analytics-cloud
  - bi
  - analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/data-analytics-landscape-map/
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/sap/analytics-technology-domain/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-datasphere/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/semantic-layer/
  - /atlas/concepts/sap-data-product/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Analytics Cloud</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Analytics Cloud</h1>
    <p class="note-subtitle">SAP's cloud experience for business intelligence, analytical applications, and planning.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Reporting and analytics</dd></div>
      <div><dt>SAP area</dt><dd>Analytics Cloud</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Analytics Cloud (SAC) is the user-facing analytics and planning layer in many SAP landscapes. It can present interactive stories, work with analytical models, support planning processes, and connect to SAP and non-SAP data sources. The important point is that SAC does not imply one fixed data architecture: the data may remain in a source system, be imported into SAC, or be consumed through newer live-data-access patterns.</p>

    <h2>A story is the experience, not the source of truth</h2>
    <p>A story brings charts, tables, filters, input controls, and other analytical elements together for a user. It is where people explore a result, but the meaning of that result should normally come from the model underneath it. If revenue, margin, product hierarchy, or fiscal-period logic is recreated differently in every story, the landscape becomes difficult to reconcile.</p>

    <p>We therefore separate presentation problems from model problems. A chart can be configured incorrectly even when the source is correct. The model can contain the wrong measure or filter even when the chart is fine. And the source query can be wrong or incomplete before SAC receives anything. This separation makes troubleshooting much faster than treating every wrong number as a “SAC issue.”</p>

    <h2>Live and imported data have different operating models</h2>
    <p>With supported <strong>live connections</strong>, business data remains in the source and SAC sends queries to that source. For SAP S/4HANA, SAP documents live access based on released analytical CDS content and queries. This can avoid another data copy, but performance, authorizations, network configuration, and source-system availability remain part of the user experience.</p>

    <p>With an <strong>import connection</strong>, data is copied into SAC. Changes in the source do not automatically change the already imported dataset; refresh behavior becomes part of the design. Import can give the analytical model more local control, but it also introduces data-loading and freshness responsibilities.</p>

    <p>SAP also supports <strong>live data access</strong> for selected sources. In this model, SAC can keep the model structure locally while accessing remote fact data without replicating those facts. This is different from the older concept of a live remote model where both data and model structure are held in the remote source. The exact capabilities depend on the source and tenant, so “live” should not be used as one generic technical label.</p>

    <h2>Planning adds write-oriented business processes</h2>
    <p>Planning changes the nature of the solution. Users are no longer only reading governed facts; they are creating plan versions, entering assumptions, running calculations or data actions, and coordinating a business process over time. Locking, versions, ownership, calendars, and data movement can therefore matter as much as visualization.</p>

    <p>This is why we do not describe SAC planning as a generic “write-back to S/4HANA.” The write path depends on the planning architecture. Plan data may live in SAC models or participate in supported integration and seamless-planning scenarios. A solution design should name the model, storage location, integration path, and system of record instead of assuming that planning changes are written directly into an ERP transaction.</p>

    <h2>Performance follows the whole query path</h2>
    <p>When a story is slow, the visible page is only the end of the path. We check how much the story requests, which model serves it, whether the connection is live or imported, where calculations run, and whether the source query is selective. A heavily joined source model or an unfiltered analytical query cannot be repaired by changing chart colors or page layout.</p>

    <p>The same principle applies to security. Story sharing, SAC roles, model permissions, source-system authorization, and identity configuration can all participate in the final access decision. A user who can open a story may still see no data because the source rejects the query; another user may have source access but no permission to the SAC content.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Analytics Cloud — <a href="https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/d2a1edf7cda74315a2c5052de8a3a4eb.html">Live Data Connections to SAP S/4HANA</a>.</li>
      <li>SAP Analytics Cloud — <a href="https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/5339a2395ccd4befb047c625a15f8481.html">Import Data Connection Overview</a>.</li>
      <li>SAP Analytics Cloud — <a href="https://help.sap.com/docs/SAP_ANALYTICS_CLOUD/00f68c2e08b941f081002fd3691d86a7/4a573d78d2da4642b6f374d377c2f4a0.html">About Live Data Access</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAC connection types, planning features, tenant capabilities, licensing, and supported source combinations change over time. Verify the current documentation for the exact tenant and source system before turning these architectural distinctions into an implementation design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/analytics-technology-domain/">Analytics Technology Domain</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/concepts/semantic-layer/">Semantic Layer</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
