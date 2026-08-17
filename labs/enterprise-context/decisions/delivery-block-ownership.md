---
layout: default
title: "Where Should Delivery Blocking Logic Live? — SAP Sales Decision Card"
description: "A compact SAP sales decision model for separating commercial, credit, compliance, data, and technical delivery blocks."
permalink: /labs/enterprise-context/decisions/delivery-block-ownership/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-17
last_reviewed: 2026-08-17
hide_global_cta: true
review_method: "authored decision model over reviewed sales, credit, master-data, and integration material"
structured_data:
  type: TechArticle
primary_topic: "sap-delivery-block-ownership"
semantic_links:
  - type: "part_of"
    title: "SAP Decision Cards"
    url: "/labs/enterprise-context/decisions/"
  - type: "related_topic"
    title: "Sales Processes"
    url: "/labs/enterprise-context/sales-processes/"
  - type: "related_topic"
    title: "SAP Credit Management"
    url: "/labs/enterprise-context/credit/"
  - type: "related_topic"
    title: "Master Data"
    url: "/labs/enterprise-context/master-data/"
tags: [sap, sales, delivery, controls, credit, master-data]
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/decisions/">Decision Cards</a></li><li aria-current="page">Delivery block ownership</li></ol></nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal><div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">Decision Card / Sales</p><h1>Where should delivery<br />blocking logic live?</h1><p>A single “delivery block” can hide several unrelated business controls. When every exception becomes the same block, support teams lose the reason, owner, and release rule.</p></div><div class="research-canvas__signal"><p>My default</p><div class="research-canvas__signal-line"><span>WHY</span><strong>Separate</strong><small>Reason classes</small></div><div class="research-canvas__signal-line"><span>WHO</span><strong>Assign</strong><small>Control owner</small></div><div class="research-canvas__signal-line"><span>HOW</span><strong>Release</strong><small>Evidence and authority</small></div><em>A block is a control, not a generic error flag.</em></div></header>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">rule</span><p><strong>Decision in one sentence:</strong> keep the blocking control with the business risk it represents, use explicit reason codes and owners, and avoid a custom central block that mixes commercial policy, credit, compliance, bad data, and technical failures.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Control classes</p><h2>The same symptom can have different owners.</h2></header><div class="ecg-decision-columns">
    <div><h3>Commercial policy</h3><p>Examples include manual approval, special terms, incomplete agreement, or an order that requires business review. Sales or commercial governance should own the release rule.</p></div>
    <div><h3>Credit risk</h3><p>Do not copy credit logic into a generic delivery-block enhancement. Let the credit process own the exposure, check, release authority, and audit trail.</p></div>
    <div><h3>Compliance or legal control</h3><p>Export, sanctions, product restrictions, or other regulated conditions need their own evidence and authorised release process.</p></div>
    <div><h3>Master-data quality</h3><p>If the order cannot proceed because a partner, material, shipping, tax, or other prerequisite is invalid, the durable fix belongs with the data owner even if the transaction is temporarily blocked.</p></div>
    <div><h3>Technical failure</h3><p>An interface error, failed enhancement, or unavailable service is an incident. Hiding it behind a business block makes the process appear controlled while the technical failure remains unresolved.</p></div>
  </div></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Decision drivers</p><h2>Four questions before adding another block.</h2></header><div class="research-route-list">
    <a href="#default"><span>01</span><strong>What risk is being stopped?</strong><small>Name the business consequence, not only the SAP field.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>02</span><strong>Who has authority to release it?</strong><small>If nobody can answer this, the control design is incomplete.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>03</span><strong>What evidence changes the state?</strong><small>Define the data, approval, payment, compliance result, or technical recovery that allows continuation.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
    <a href="#default"><span>04</span><strong>Is the block preventive or compensating?</strong><small>A temporary transaction block should not replace fixing the master data, configuration, integration, or policy that caused repeated failure.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
  </div></section>

  <section class="research-canvas__inventory" id="default" data-reveal><header><p class="research-canvas__eyebrow">Default choice</p><h2>One control purpose, one owner, one release rule.</h2></header><div class="decision-table"><table><thead><tr><th>Problem</th><th>Primary owner</th><th>Do not turn it into</th></tr></thead><tbody>
    <tr><td>Commercial approval</td><td><strong>Sales / commercial owner</strong></td><td>A technical workaround or credit substitute.</td></tr>
    <tr><td>Credit exposure</td><td><strong>Credit management</strong></td><td>Duplicate custom logic in delivery processing.</td></tr>
    <tr><td>Bad master data</td><td><strong>Data owner / governance</strong></td><td>A permanent manual release queue.</td></tr>
    <tr><td>Interface or code failure</td><td><strong>Application / integration operations</strong></td><td>A business approval step that hides an incident.</td></tr>
  </tbody></table></div></section>

  <section class="research-canvas__boundary" data-reveal><span class="material-symbols-outlined" aria-hidden="true">warning</span><p><strong>I change the default when:</strong> a regulated control requires a central hold, multiple checks must be combined into one auditable gate, or the process intentionally uses a shared orchestration layer with explicit reason codes and delegated ownership.</p><p><strong>Failure ownership:</strong> report blocked volume by reason and owner. A total count of blocked deliveries is operationally weak because it mixes business decisions with defects and data-quality debt.</p></section>

  <section class="research-canvas__inventory" data-reveal><header><p class="research-canvas__eyebrow">Evidence path</p><h2>Trace the reason behind the block.</h2></header><div class="research-route-list"><a href="/labs/enterprise-context/sales-processes/"><span>SD</span><strong>Sales processes</strong><small>Order, delivery, billing, determination, and special-process context.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/credit/"><span>CR</span><strong>Credit</strong><small>Credit checks, exposure, release, and ownership.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a><a href="/labs/enterprise-context/master-data/"><span>DATA</span><strong>Master Data</strong><small>Data prerequisites, ownership, and downstream process effects.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a></div></section>
</div>
