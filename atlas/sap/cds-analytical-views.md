---
layout: default
title: "CDS Analytical Views"
description: "ABAP CDS analytics explained: dimensions, cubes, measures, analytical queries, and how embedded analytics runs on transactional data."
permalink: /atlas/sap/cds-analytical-views/
atlas_section: sap
domain: SAP operations
subdomain: Data and analytics
concept_type: technology
sap_area: "CDS Analytical Views"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - cds-views
  - analytical-views
  - olap
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/cds-views/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/embedded-analytics/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">CDS Analytical Views</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>CDS Analytical Views</h1>
    <p class="note-subtitle">How ABAP CDS models transactional data as dimensions, cubes, measures, hierarchies, and analytical queries.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Analytics and reporting</dd></div>
      <div><dt>SAP area</dt><dd>CDS Analytical Views</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Analytics is a different way of reading the same business data</h2>
    <p>ABAP CDS analytics builds multidimensional models on data that already lives in the ABAP system. Instead of extracting every reporting use case into a separate warehouse first, embedded analytics can evaluate current operational data through the ABAP analytical engine. CDS supplies the semantic model that tells the engine which fields are dimensions, which values are measures, how entities relate, and how a query should aggregate them.</p>

    <p>This is why an analytical CDS model is more than a view that happens to contain numbers. The analytical semantics determine how the data behaves when a user filters, drills down, changes dimensions, or requests totals.</p>

    <h2>The model is layered</h2>
    <p>A useful analytical model normally separates reusable data providers from the query that a consumer sees. Dimensions describe business axes such as product, company code, customer, or time. Fact-style providers and cubes combine those dimensions with measurable values. Hierarchies define structured navigation where the business concept needs it. The analytical query then projects the model for consumption and defines query-level behavior such as measures and aggregation.</p>

    <p>SAP's current ABAP analytics documentation describes dimensions, facts, cubes, and hierarchies as CDS building blocks. The analytical engine operates on this model rather than treating every report as a standalone SQL statement.</p>

    <h2>An analytical query is not ordinary data retrieval</h2>
    <p>The name can be misleading. In ABAP CDS, an analytical query is modeled as an analytical projection and is evaluated by the ABAP Analytical Engine. It does not implement data retrieval in the same way as a normal SQL-oriented CDS entity. Its purpose is to describe how an analytical provider should be consumed.</p>

    <p>That distinction explains why debugging a wrong total often requires us to inspect more than the final query. The problem may come from the underlying cube, a relationship to a dimension, the definition of a measure, or the aggregation semantics applied at query level.</p>

    <h2>Aggregation is part of the business meaning</h2>
    <p>Not every numeric field can simply be summed. Quantity, amount, percentage, inventory balance, headcount, and price all have different aggregation rules. CDS analytics lets the model define measures and aggregation behavior so that consumers do not have to rediscover those rules independently.</p>

    <p>For example, a sales value may aggregate naturally across orders, while a unit price normally does not. A stock balance may need a time-dependent interpretation rather than a simple total across dates. If the analytical model gets this wrong, the report can look technically healthy while answering the business question incorrectly.</p>

    <h2>Embedded analytics is close to the transaction</h2>
    <p>The main architectural advantage of embedded analytics is proximity to operational data. The analytical engine works on the same persistence used by the transactional application, so a report can evaluate recent business changes without a separate replication step. This is useful for operational analysis where freshness matters.</p>

    <p>It does not mean that an embedded model replaces every data-warehouse scenario. Cross-system harmonization, historical integration, planning, and enterprise-wide semantic layers can still belong in products such as SAP Datasphere or SAP Analytics Cloud. The CDS model solves a different problem: giving the ABAP application a reusable analytical representation of its own business data.</p>

    <h2>Consumption comes after the model</h2>
    <p>An analytical CDS model can support Fiori analytical applications and other analytical consumers, but the CDS definition alone is not the whole delivery path. Depending on the scenario, service definitions, service bindings, application descriptors, or other exposure artifacts are needed. SAP's tooling can generate parts of this stack from a valid CDS-based analytical cube.</p>

    <p>In practice, we get better results when we treat the analytical model as a product in its own right. A clear cube with stable dimensions and well-defined measures is easier to reuse than a query built only to satisfy one dashboard.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-cloud/analytical-apps-and-services">Analytical Services</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-data-models/query-modeling">Query Modeling</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/abap-cloud/abap-development-tools-user-guide/generating-multi-dimensional-analysis-applications">Generating Multi-Dimensional Analysis Applications</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Available analytical annotations, projection capabilities, release contracts, and consumption options depend on the ABAP product and release. Verify the intended analytical provider and consumer path in the target environment.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/embedded-analytics/">Embedded Analytics</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
