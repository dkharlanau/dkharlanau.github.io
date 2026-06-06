---
layout: default
title: "SAP MDG"
description: "Analytical overview of SAP MDG: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/sap-mdg/
atlas_section: sap
domain: SAP operations
subdomain: Master data governance
concept_type: product
sap_area: "MDG"
business_process: "Master data governance"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - sap-mdg
  - master-data
  - governance
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/sap-mdg-governance-patterns/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP MDG</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP MDG</h1>
    <p class="note-subtitle">Master Data Governance for centralized creation, validation, and distribution.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>MDG</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>SAP MDG (Master Data Governance) is a centralized hub for creating, validating, and distributing master data across the enterprise. It ensures consistency of business partners, materials, customers, vendors, and other master objects.</p>

    <h2>Business purpose</h2>
    <p>Prevent master data fragmentation. Enforce validation rules before data enters downstream systems. Distribute governed master data to S/4HANA, satellite systems, and external partners.</p>

    <h2>Where it sits in the landscape</h2>
    <p>MDG sits upstream of S/4HANA and other target systems. It receives requests, runs workflows, applies validation, and replicates approved data. It is often the system of record for business partner and material master.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Business partner: customer, vendor, contact, employee.</li>
      <li>Material master: basic data, classification, units.</li>
      <li>Change request: workflow-driven master data changes.</li>
      <li>Data model: entity types, attributes, relationships, hierarchies.</li>
      <li>Replication model: filter, mapping, distribution rules.</li>
      <li>Key mapping: source-to-target identifier translation.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: direct replication, change pointers, ALE/IDoc.</li>
      <li>Satellite systems: CRM, SCM, external ERP via replication.</li>
      <li>External: data import, mass processing, API-based creation.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom data models and validation rules.</li>
      <li>Workflow enhancements and approval rules.</li>
      <li>Custom replication logic and key mapping.</li>
      <li>Side-by-side data quality apps on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Change request backlog: pending, rejected, approved.</li>
      <li>Replication log: success, error, retry status.</li>
      <li>Data quality score: validation rule violations.</li>
      <li>Key mapping completeness: missing or duplicate mappings.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Centralized governance reduces duplicate and inconsistent master data.</li>
      <li>Workflow-driven changes enforce approval and audit.</li>
      <li>Flexible data models for custom master objects.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Replication failures are common and hard to trace.</li>
      <li>Key mapping complexity increases with system count.</li>
      <li>Workflow configuration is release-specific and brittle.</li>
      <li>Data model changes require careful migration planning.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Business partner not replicated — model filter or key mapping.</li>
      <li>Duplicate master data — key mapping missing or wrong.</li>
      <li>Change request stuck — workflow rule or approver issue.</li>
      <li>Validation failure — custom rule too strict or data format mismatch.</li>
      <li>Replication performance — large data volume or network latency.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/data-quality/sap-mdg-governance-patterns/">SAP MDG Governance Patterns</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. MDG module scope, replication mechanisms, and configuration paths vary by release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
      <li><a href="/atlas/diagnostics/sap-business-partner-replication-diagnostics/">SAP Business Partner Replication Diagnostics</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
