---
layout: default
title: "Where Should Master-Data Validation Live? — SAP Decision Card"
description: "A compact decision model for placing master-data validation in governance, application, integration, or transaction controls."
permalink: /labs/enterprise-context/decisions/master-data-validation/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-17
last_reviewed: 2026-08-17
hide_global_cta: true
review_method: "authored decision model over reviewed master-data, MDG, integration, and process material"
structured_data:
  type: TechArticle
primary_topic: "sap-master-data-validation-boundary"
semantic_links:
  - type: "part_of"
    title: "SAP Decision Cards"
    url: "/labs/enterprise-context/decisions/"
  - type: "related_topic"
    title: "Master Data"
    url: "/labs/enterprise-context/master-data/"
  - type: "related_topic"
    title: "SAP Master Data Governance"
    url: "/labs/enterprise-context/mdg/"
  - type: "related_topic"
    title: "SAP Integration Architecture"
    url: "/labs/enterprise-context/integrations/"
tags: [sap, master-data, mdg, validation, governance, integration]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/decisions/">Decision Cards</a></li><li aria-current="page">Master-data validation</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">Decision Card / Data</p><h1>Where should<br />validation live?</h1><p>A validation rule is easy to add in the nearest screen or interface. That is also how the same business rule ends up implemented five times with five slightly different meanings.</p></div><div class="research-canvas__signal"><p>My default</p><div class="research-canvas__signal-line"><span>PREVENT</span><strong>Governance</strong><small>Stop bad master data early</small></div><div class="research-canvas__signal-line"><span>PROTECT</span><strong>Transaction</strong><small>Protect a business posting</small></div><div class="research-canvas__signal-line"><span>CONTRACT</span><strong>Integration</strong><small>Reject invalid exchange</small></div><em>One rule can need more than one control, but not more than one owner.</em></div></header>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">rule</span><p><strong>Decision in one sentence:</strong> put stable business-quality rules as early as possible in the master-data lifecycle, keep transaction-specific protection close to the transaction, and use integration validation to protect contracts rather than to become a second master-data governance system.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Control layers</p><h2>Separate prevention, protection, and contract validation.</h2></header><div class="ecg-decision-columns">
    <div><h3>Governance-time validation</h3><p>Use it when the rule defines whether the master record is fit for enterprise use: mandatory attributes, allowed combinations, stewardship rules, approval, duplicate control, or lifecycle state.</p></div>
    <div><h3>Application-time validation</h3><p>Use it when the rule belongs to one application context or local extension and should not redefine the enterprise master-data contract.</p></div>
    <div><h3>Transaction-time protection</h3><p>Use it when a sales order, purchase order, delivery, posting, or other business event must be protected from a risky state even if the master data already exists.</p></div>
    <div><h3>Integration-time validation</h3><p>Use it to enforce message structure, required identifiers, version compatibility, semantic contract, and receiver-specific prerequisites before data crosses the boundary.</p></div>
  </div></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Decision drivers</p><h2>Ask what the rule means, not where it is easiest to code.</h2></header><div class="research-route-list">
    <a href="#default"><span>01</span><strong>Is the rule globally true?</strong><small>If it should hold across consumers, prefer the governed master-data layer.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>02</span><strong>Does the rule protect one business event?</strong><small>Keep it near the transaction that would create the irreversible or risky result.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>03</span><strong>Is the rule about the exchange contract?</strong><small>Validate identifiers, structure, versions, and consumer prerequisites at the integration boundary.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>04</span><strong>Who can correct the cause?</strong><small>The team that owns correction should usually own the primary rule and stewardship process.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
  </div></section>

  <section class="research-canvas__inventory" id="default" data-reveal><header><p class="research-canvas__eyebrow">Default choice</p><h2>Prevent centrally, protect locally, validate contracts at the edge.</h2></header><div class="decision-table"><table><thead><tr><th>Rule type</th><th>Primary home</th><th>Why</th></tr></thead><tbody>
    <tr><td>Enterprise data quality</td><td><strong>Governance / MDG</strong></td><td>One definition, one steward, earlier correction, less downstream duplication.</td></tr>
    <tr><td>Process-specific safety</td><td><strong>Transaction or application</strong></td><td>The control depends on the business event and its local consequences.</td></tr>
    <tr><td>Interface contract</td><td><strong>Integration boundary</strong></td><td>The sender and receiver need an explicit, testable exchange agreement.</td></tr>
  </tbody></table></div></section>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">warning</span><p><strong>I change the default when:</strong> a source system is authoritative and cannot be governed centrally, a regulatory rule must stop a transaction even if the master record is valid, a migration needs temporary controls, or a consumer has a stricter contract than the enterprise model.</p><p><strong>Failure ownership:</strong> do not let every downstream team “fix” the same bad record independently. Capture the failing rule, identify the authoritative source, assign a correction owner, and preserve a reconciliation path for already distributed data.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Evidence path</p><h2>Follow the data from governance to consumption.</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/master-data/"><span>01</span><strong>Master Data</strong><small>Objects, dependencies, ownership, and process impact.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/mdg/"><span>02</span><strong>MDG</strong><small>Governance, change, validation, approval, distribution, and stewardship.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/integrations/"><span>03</span><strong>Integration</strong><small>Contract, delivery, recovery, and data-distribution boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></div></section>
</div>
