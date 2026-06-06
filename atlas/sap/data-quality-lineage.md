---
layout: default
title: "Data Quality and Lineage"
description: "Analytical overview of Data Quality and Lineage in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/data-quality-lineage/
atlas_section: sap
domain: SAP operations
subdomain: Data and analytics
concept_type: technology
sap_area: "Data Quality"
business_process: "Data governance and compliance"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - data-quality
  - data-lineage
  - data-governance
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-mdg/
  - /atlas/sap/sap-datasphere/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/cds-views/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Data Quality and Lineage</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Data Quality and Lineage</h1>
    <p class="note-subtitle">Data quality rules, validation, profiling, and lineage tracking across SAP systems.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Data governance and compliance</dd></div>
      <div><dt>SAP area</dt><dd>Data Quality</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>Data Quality and Lineage covers the frameworks for enforcing data quality rules, validation, profiling, and tracking data origin and transformations in SAP. It spans Data Quality Management in MDG, Datasphere data quality features, custom validation rules, and lineage graphs that show where data originated, what transformations were applied, and who changed it.</p>

    <h2>Business purpose</h2>
    <p>Ensure data is accurate, complete, consistent, and traceable. Critical for regulatory compliance, auditing, operational trust, and reliable analytics.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Data quality and lineage span the full data lifecycle: entry via MDG or Fiori, integration through SLT or Datasphere, storage in S/4HANA and Datasphere, and consumption in Analytics Cloud and reporting tools.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Validation rule: constraint checked at entry or sync.</li>
      <li>Data quality score: aggregated metric of rule compliance.</li>
      <li>Lineage graph: visual map of data origin and transformations.</li>
      <li>Profiling result: statistical summary of column values.</li>
      <li>Duplicate check: matching logic for master data.</li>
      <li>Custom validation routine: ABAP or SQL-based rule.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>SAP MDG: Data Quality Management, duplicate check, validation.</li>
      <li>Datasphere: data quality rules, profiling, and monitoring.</li>
      <li>S/4HANA: custom validation in transactions and CDS views.</li>
      <li>Analytics Cloud: data quality indicators in reports.</li>
      <li>Data Intelligence: advanced profiling and lineage.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom validation rules in MDG and S/4HANA.</li>
      <li>BAdIs for data quality checks and enrichment.</li>
      <li>Custom data quality workflows and approval steps.</li>
      <li>Side-by-side profiling apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Data quality score trends over time.</li>
      <li>Validation failure rates by object and rule.</li>
      <li>Lineage completeness: gaps in transformation tracking.</li>
      <li>Profiling coverage: which tables and fields are analyzed.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Integrated with SAP data flows and master data processes.</li>
      <li>Traceable lineage supports compliance and root-cause analysis.</li>
      <li>MDG provides robust duplicate checking and validation.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Limited out-of-the-box coverage for custom tables.</li>
      <li>Custom rules require ongoing maintenance and testing.</li>
      <li>Lineage gaps for external or non-SAP systems.</li>
      <li>Performance impact of real-time validation on high-volume processes.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Data quality rule blocking postings — overly strict validation.</li>
      <li>Lineage graph incomplete after migration — missing metadata.</li>
      <li>Validation performance degradation — complex ABAP routine.</li>
      <li>Master data sync failure — quality check rejecting records.</li>
      <li>Duplicate check false positives — matching logic too broad.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/cds-views/">CDS Views</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Master Data Governance Data Quality — <a href="https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE/data-quality.html">SAP Help Portal</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Data quality features, lineage depth, and integration behavior vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a></li>
      <li><a href="/atlas/sap/sap-datasphere/">SAP Datasphere</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
