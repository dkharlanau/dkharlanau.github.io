---
layout: default
title: "Embedded Analytics"
description: "SAP S/4HANA Embedded Analytics explained: CDS-based analytical models, analytical queries, multidimensional consumption, and the boundary with external analytics platforms."
permalink: /atlas/sap/embedded-analytics/
atlas_section: sap
domain: SAP operations
subdomain: Data and analytics
concept_type: technology
sap_area: "Embedded Analytics"
business_process: "Analytics and reporting"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - embedded-analytics
  - s4hana
  - real-time-analytics
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/cds-views/
  - /atlas/sap/cds-analytical-views/
  - /atlas/sap/sap-analytics-cloud/
  - /atlas/sap/sap-datasphere/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Embedded Analytics</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Embedded Analytics</h1>
    <p class="note-subtitle">Operational analytics that stays close to SAP S/4HANA business data instead of starting with a separate warehouse copy.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Analytics and reporting</dd></div>
      <div><dt>SAP area</dt><dd>Embedded Analytics</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until analytics claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP S/4HANA Embedded Analytics is the analytical layer built into the S/4HANA application environment. Its main value is proximity to operational data: an analytical consumer can evaluate current business data through the S/4HANA analytical model without first building a separate replicated reporting store for every operational question.</p>

    <p>That does not mean every report in S/4HANA is “embedded analytics,” nor does it mean an embedded query is automatically the right answer for enterprise reporting. The useful distinction is architectural: embedded analytics models and consumes S/4HANA business data close to the transactional system; products such as SAP Datasphere and SAP Analytics Cloud can add cross-system modeling, broader consumption, planning, or enterprise analytics around it.</p>

    <h2>The analytical model comes before the chart</h2>
    <p>The foundation is SAP's virtual data model and CDS-based analytical content. Reusable CDS entities describe business semantics, relationships, dimensions, and measures. Analytical cubes and queries then define how that data should behave when a consumer filters, aggregates, drills down, or changes dimensions.</p>

    <p>This is why embedded analytics should not be reduced to “KPI tiles.” A tile, chart, table, or multidimensional report is a consumer of an analytical model. If a number is wrong, the cause may sit in the underlying CDS provider, analytical semantics, filters, authorizations, or query definition rather than in the visualization itself.</p>

    <h2>Analytical queries are the consumption contract</h2>
    <p>An analytical query presents a business-oriented view of an analytical provider. It can define dimensions, measures, filters, formulas, hierarchies, and other query behavior for analytical consumers. In current SAP tooling, delivered or custom analytical queries can be previewed through Multidimensional Analysis and related analytical applications.</p>

    <p>The important point is that the query is not simply another SQL-style view. The ABAP analytical engine evaluates analytical semantics such as aggregation. That is why a seemingly small modeling decision can change totals, exception aggregation, or drill-down behavior across several consumers.</p>

    <h2>“Real time” means close to operational data, not unlimited analytics</h2>
    <p>Embedded analytics can read current S/4HANA data without an additional extraction-and-load cycle for that query. This is useful for operational questions such as open orders, current receivables, inventory positions, or process exceptions where freshness matters.</p>

    <p>But proximity to the transaction system is also a boundary. A query still needs a suitable data model and selective filters, and not every historical, cross-system, planning, or harmonization requirement belongs inside S/4HANA. Moving a complex enterprise data model into an embedded query simply because the source data is available there can make ownership and semantics harder rather than simpler.</p>

    <h2>Consumption can stay in S/4HANA or extend outside it</h2>
    <p>S/4HANA provides analytical consumption through Fiori-based analytical applications and multidimensional analysis. Current SAP documentation also supports external analytical consumption in defined scenarios. For example, SAP Analytics Cloud can use live connections to S/4HANA analytical queries and released CDS content when the required connection and release conditions are met.</p>

    <p>This separation helps us reason about the stack. CDS and the analytical engine define the business model; the analytical query shapes consumption; a Fiori analytical application, multidimensional report, or external analytical client presents it. A problem in one layer should not be diagnosed by changing another layer blindly.</p>

    <h2>Use embedded analytics for the questions it answers well</h2>
    <p>Embedded analytics is strongest when the question belongs to one S/4HANA business context and the user benefits from current operational data. A sales manager checking open order value, a buyer reviewing purchasing exceptions, or a finance user drilling into current balances are natural examples when SAP provides the right analytical model.</p>

    <p>When the question requires harmonizing several source systems, long historical integration, a shared enterprise semantic layer, or complex planning, the architecture usually grows beyond embedded analytics. The better design is not “embedded versus warehouse” as a product contest. It is deciding where each analytical responsibility belongs.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/a630d57fc5004c6383e7a81efee7a8bb/599db5e2921c46ac95475567b9aa68c2.html">Analytics Architecture</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6b356c79dea443c4bbeeaf0865e04207/7faf5a28ddb4477f91e9d424e8968c25.html">How to Preview Multidimensional Analysis</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/r/b5670aaaa2364a29935f40b16499972d/202310.000/en-US/e30de6eae4d24d70b65996ac8ff88848.html">Custom CDS Views</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Available analytical content, authoring apps, CDS release contracts, query features, and external consumption options differ across SAP S/4HANA products and releases. Verify the exact analytical provider and consumer path in the target landscape.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
      <li><a href="/atlas/sap/cds-analytical-views/">CDS Analytical Views</a></li>
      <li><a href="/atlas/sap/sap-analytics-cloud/">SAP Analytics Cloud</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
