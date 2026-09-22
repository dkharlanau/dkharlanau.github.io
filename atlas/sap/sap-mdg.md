---
layout: default
title: "SAP MDG"
description: "SAP Master Data Governance explained: change requests, staging, validation, activation, data models, and governed distribution."
permalink: /atlas/sap/sap-mdg/
atlas_section: sap
domain: SAP operations
subdomain: Master data governance
concept_type: product
sap_area: "MDG"
business_process: "Master data governance"
status: needs_verification
verified: false
last_reviewed: 2026-09-22
author: Dzmitryi Kharlanau

tags:
  - sap-mdg
  - master-data
  - governance
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/data-mesh-architecture-map/
  - /atlas/maps/sap-data-products-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/sap-mdg-governance-patterns/
  - /atlas/concepts/data-mesh-for-sap-landscapes/
  - /atlas/concepts/sap-data-product/
  - /atlas/concepts/data-quality-controls/
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
    <p class="note-subtitle">A governance layer for changing master data before the change becomes active and spreads through the landscape.</p>
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
    <p>SAP Master Data Governance (MDG) is easiest to understand as a controlled path from a proposed master-data change to active, usable data. The important idea is not simply that MDG stores master data. It gives an organization a place to apply ownership, checks, workflow, and approval before a change is activated.</p>

    <h2>The change request is the center of the governance flow</h2>
    <p>In central governance, a user does not normally change the active record directly. The user creates a change request. The proposed data is held in a staging area while the request moves through the configured workflow. Checks can run during that process, including required-field checks, validations, and duplicate checks. When the request is approved, the governed data is activated.</p>

    <p>This separation between <em>proposed</em> data and <em>active</em> data is what makes MDG different from an ordinary maintenance screen. It gives reviewers a stable object to discuss, reject, correct, or approve without treating every intermediate edit as production master data.</p>

    <h2>Data model, rules, and workflow solve different problems</h2>
    <p>The MDG data model describes the entities, attributes, and relationships that belong to the governed object. Business rules and checks decide whether a proposed change is acceptable. Workflow decides who must act and in which order. These layers work together, but they are not interchangeable.</p>

    <p>For example, a Business Partner change can contain general data and role-specific or organizational data. The model defines what can be represented; validation can reject inconsistent values; workflow can route the request to the responsible steward. If approval succeeds, activation makes the accepted version available in the active area.</p>

    <h2>Activation and distribution are separate concerns</h2>
    <p>Approval answers the governance question: <em>may this change become active?</em> Distribution answers a different question: <em>which other systems need the active data, and in what representation?</em> In a multi-system landscape, replication therefore needs its own configuration, filters, mappings, and monitoring.</p>

    <p>That distinction matters in support. A successful change request does not by itself prove that every downstream target received and accepted the record. Likewise, a replication error does not necessarily mean that the governance workflow was wrong. We get a clearer diagnosis when we first separate the lifecycle of the change request from the lifecycle of the replicated message.</p>

    <h2>MDG is broader than one governance pattern</h2>
    <p>Central Governance is the best-known pattern, but SAP MDG also provides capabilities for consolidating and mass-processing master data. These solve a different class of problem: bringing existing records together, matching or standardizing them, and applying controlled changes at scale. The exact capabilities available depend on the MDG product and release, so they should not be treated as one universal workflow.</p>

    <h2>What good governance changes</h2>
    <p>A useful MDG design makes responsibility visible. It becomes clear who proposes a change, which rules are checked, who approves it, when it becomes active, and how it reaches the systems that depend on it. That traceability is more valuable than simply centralizing fields in one application.</p>

    <p>It also changes the way we investigate master-data incidents. Instead of asking only whether a field is correct in the final table, we can ask where the record is in its lifecycle: still staged, rejected, approved but not activated, active but not replicated, or replicated but rejected by a target system. Those are different states and require different fixes.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE/1b769cd8013643adac309014c812427e/77f5b94bdfcf4a2fa40d82098354fa11.html">Change Request Processing</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_MASTER_DATA_GOVERNANCE/38e78d5fbde74325885af5a4e7a4acf6/cf9b0955b37e3d6ae10000000a44176d.html">Data Modeling</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>MDG data models, workflow steps, validation logic, activation behavior, replication technologies, and available applications vary by object, product version, and deployment. This page explains the durable governance model rather than a release-specific configuration recipe.</p>
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
