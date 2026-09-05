---
layout: default
title: "SAP S/4HANA 2025 Release Readiness Playbook"
description: "A practical SAP Lead playbook for checking whether an S/4HANA 2025 feature is released, supported, convertible, and safe to design around."
permalink: /labs/enterprise-context/release-readiness/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-04
last_reviewed: 2026-09-04
publication_wave: "release-readiness-wave-01"
review_method: "SAP S/4HANA 2025 Restriction Note + SAP Help conversion guidance + editorial review"
search_intent: "SAP S/4HANA 2025 restriction note conversion readiness release restrictions logistics aATP procurement intercompany variant configuration"
hide_global_cta: true
structured_data:
  type: TechArticle
tags: [sap, s4hana, release-readiness, conversion, upgrade, logistics, sales, procurement, aatp, integration, variant-configuration]
# ai-discovery-managed:start
primary_topic: "sap-s4hana"
ai_sidecar: "/ai/pages/labs--enterprise-context--release-readiness.json"
entity_mentions:
  - "sap-sales"
  - "sap-procurement"
  - "advanced-atp"
  - "sap-integration"
semantic_links:
  - type: "related_topic"
    title: "SAP Decision Cards — Enterprise Context Lab"
    url: "/labs/enterprise-context/decisions/"
  - type: "related_topic"
    title: "STO or Intercompany Sales? — SAP Logistics Decision Card"
    url: "/labs/enterprise-context/decisions/sto-vs-intercompany/"
  - type: "same_domain"
    title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
    url: "/labs/enterprise-context/deployment-models/"
  - type: "integrates_with"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
  - type: "related_topic"
    title: "SAP Testing Strategy for S/4HANA Delivery"
    url: "/labs/enterprise-context/testing/"
  - type: "same_domain"
    title: "SAP Development Architecture — RAP, CAP, ABAP Cloud and Clean Core"
    url: "/labs/enterprise-context/development/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Release Readiness</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context / Lead playbook</p>
      <h1>The feature exists.<br />Can we actually use it?</h1>
      <p>A strong SAP Lead separates product capability from release support, conversion readiness, and integration impact. This page uses SAP S/4HANA 2025 on-premise as the working example.</p>
      <a class="research-canvas__button" href="#five-gates">Run the five-gate check <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Release readiness model">
      <p>Lead answer pattern</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Product</strong><small>Which deployment and release?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Support</strong><small>What is released now?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Path</strong><small>Can this system get there?</small></div>
      <em>Last reviewed 2026-09-04 · restriction notes can change after release.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>The trap is simple:</strong> “I can switch it on” is not the same as “SAP released and supports this design.”</p>
    <p><strong>Scope matters:</strong> SAP Note 3549655 is for SAP S/4HANA 2025 on-premise. SAP points Private Edition 2025 to a different restriction note, 3659273. Do not mix deployment models.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare deployment models <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three questions</p>
      <h2>Capability, release support, and conversion are different questions.</h2>
      <p>Teams often answer the first question and assume the other two are also green. That is where avoidable project risk starts.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/3493301" target="_blank" rel="noopener"><span>01</span><strong>Does the product have the capability?</strong><small>Start with release information and feature scope. This tells you what exists in the product family.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="https://me.sap.com/notes/3549655" target="_blank" rel="noopener"><span>02</span><strong>Is this exact use released without a blocking restriction?</strong><small>Check the restriction note and the application-specific note for your release and feature package stack.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2025/en-US/CONV_OP2025.pdf" target="_blank" rel="noopener"><span>03</span><strong>Can the current customer system reach that target safely?</strong><small>Now check source release, add-ons, Business Functions, simplification items, custom code, and data consistency.</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>
    </div>
  </section>

  <section class="research-canvas__method" id="five-gates" data-reveal>
    <div>
      <p class="research-canvas__eyebrow">Five-gate check</p>
      <h2>Do not say “supported” until all five gates are clear.</h2>
      <p>This is the reusable assessment and project pattern.</p>
    </div>
    <ol>
      <li><span>01</span><strong>Deployment</strong><p>On-premise, Private Edition, or Public Edition? Use the correct documentation set.</p></li>
      <li><span>02</span><strong>Release + FPS</strong><p>Confirm the exact target release and feature package stack. Restrictions can be FPS-specific.</p></li>
      <li><span>03</span><strong>Restriction</strong><p>Read the general restriction note and the application-specific note. “Technically possible” is not enough.</p></li>
      <li><span>04</span><strong>Conversion</strong><p>Check Business Functions, add-ons, simplification items, data prerequisites, and custom code.</p></li>
      <li><span>05</span><strong>Landscape</strong><p>Check interfaces, extensions, external systems, security, operations, and regression impact.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Which SAP tool answers what?</p>
      <h2>Do not use one tool as proof for everything.</h2>
      <p>The tools overlap, but they solve different parts of the problem.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/3549655" target="_blank" rel="noopener"><span>NOTE</span><strong>Restriction Note</strong><small>Release-level boundaries and links to application-specific restrictions. For 2025 on-premise, start with SAP Note 3549655.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="https://help.sap.com/docs/SAP_READINESS_CHECK" target="_blank" rel="noopener"><span>PLAN</span><strong>SAP Readiness Check</strong><small>Early project view: relevant simplification items, high-level custom-code impact, add-on compatibility, sizing, and other conversion topics.</small><i class="material-symbols-outlined" aria-hidden="true">dashboard</i></a>
      <a href="https://help.sap.com/maintenanceplanner" target="_blank" rel="noopener"><span>PATH</span><strong>Maintenance Planner</strong><small>Checks whether installed add-ons, active Business Functions, and other software dependencies have a valid target path. It also creates stack.xml for SUM.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2025/en-US/CONV_OP2025.pdf" target="_blank" rel="noopener"><span>SI</span><strong>Simplification Item Check</strong><small>Detailed consistency work for relevant simplification items. The report can be run as /SDF/RC_START_CHECK and is used again by SUM.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW" target="_blank" rel="noopener"><span>CODE</span><strong>ATC / Custom Code Checks</strong><small>Find custom code that depends on changed data models, removed functions, incompatible objects, or HANA-sensitive patterns.</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics risk radar</p>
      <h2>The 2025 restriction note is especially useful around cross-process features.</h2>
      <p>These are not reasons to avoid the functions. They are reasons to check the exact note before final design and estimation.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/3493689" target="_blank" rel="noopener"><span>ATP</span><strong>advanced Available-to-Promise</strong><small>SAP Note 3493689. Treat aATP design as release-specific, especially when combining advanced confirmation logic with other fulfillment features.</small><i class="material-symbols-outlined" aria-hidden="true">inventory</i></a>
      <a href="https://me.sap.com/notes/3644701" target="_blank" rel="noopener"><span>SD</span><strong>Advanced Intercompany Sales</strong><small>SAP Note 3644701. A process can be available and still have boundaries in a specific 2025 combination.</small><i class="material-symbols-outlined" aria-hidden="true">swap_horiz</i></a>
      <a href="https://me.sap.com/notes/3672804" target="_blank" rel="noopener"><span>SD</span><strong>Multistage Intercompany Sales</strong><small>SAP Note 3672804 for 2025 FPS01. This is a good example of why the FPS belongs in the architecture question.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://me.sap.com/notes/3081750" target="_blank" rel="noopener"><span>BP</span><strong>Multiple Address Handling in SD Documents</strong><small>SAP Note 3081750. Business Partner capability and SD document behavior must be checked together.</small><i class="material-symbols-outlined" aria-hidden="true">location_on</i></a>
      <a href="https://me.sap.com/notes/3234357" target="_blank" rel="noopener"><span>MM</span><strong>Manage Supplier Confirmations</strong><small>SAP Note 3234357. Procurement Fiori capability has its own restriction boundary.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="https://me.sap.com/notes/3244356" target="_blank" rel="noopener"><span>MM</span><strong>Item Hierarchies in Purchase Orders</strong><small>SAP Note 3244356. Do not assume every advanced PO structure behaves like a standard item list.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="https://me.sap.com/notes/3366080" target="_blank" rel="noopener"><span>MM</span><strong>Advanced Intercompany Stock Transfer</strong><small>SAP Note 3366080. Check the full company, stock, document, and integration chain.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="https://me.sap.com/notes/3686533" target="_blank" rel="noopener"><span>SEC</span><strong>Central Purchase Contract — Copy authorization</strong><small>SAP Note 3686533 documents a missing authorization check on the Copy action. A release restriction can be a control topic, not only a functional limitation.</small><i class="material-symbols-outlined" aria-hidden="true">security</i></a>
      <a href="https://me.sap.com/notes/3244652" target="_blank" rel="noopener"><span>INT</span><strong>Ariba Integration with S/4HANA</strong><small>SAP Note 3244652. Integration compatibility is part of release fit, not a task to leave until interface testing.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="https://me.sap.com/notes/3636337" target="_blank" rel="noopener"><span>EWM</span><strong>Embedded EWM</strong><small>SAP Note 3636337 covers release information and restrictions for EWM in SAP S/4HANA 2025 FPS00.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="https://me.sap.com/notes/3636370" target="_blank" rel="noopener"><span>EWM</span><strong>Decentralized EWM</strong><small>SAP Note 3636370. Embedded and decentralized EWM do not share one identical restriction set.</small><i class="material-symbols-outlined" aria-hidden="true">warehouse</i></a>
      <a href="https://me.sap.com/notes/3615236" target="_blank" rel="noopener"><span>TM</span><strong>Transportation Management</strong><small>SAP Note 3615236. Treat TM release fit as part of the fulfillment architecture, not a separate transport workstream.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="https://me.sap.com/notes/3631486" target="_blank" rel="noopener"><span>AVC</span><strong>Advanced Variant Configuration</strong><small>SAP Note 3631486 covers restrictions for AVC in SAP S/4HANA 2025. Product configuration needs the same release discipline as SD and manufacturing.</small><i class="material-symbols-outlined" aria-hidden="true">tune</i></a>
      <a href="https://me.sap.com/notes/3630131" target="_blank" rel="noopener"><span>MDG</span><strong>MDG for Material</strong><small>SAP Note 3630131. Master-data governance restrictions can become logistics execution problems later.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="https://me.sap.com/notes/3646221" target="_blank" rel="noopener"><span>MDG</span><strong>MDG for BP / Customer / Supplier</strong><small>SAP Note 3646221. BP restrictions matter directly to Sales and Procurement design.</small><i class="material-symbols-outlined" aria-hidden="true">groups</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Conversion traps</p>
      <h2>Greenfield thinking is not enough for a conversion.</h2>
      <p>The target design may be fine while the current system still has no direct path to it.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/2240359" target="_blank" rel="noopener"><span>BF</span><strong>Always-Off Business Functions can block conversion</strong><small>If a Business Function is active in the source but defined as always off in the target, the conversion is not possible for that target release at that point.</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="https://me.sap.com/notes/2240360" target="_blank" rel="noopener"><span>BF</span><strong>Always-On functions can activate during conversion</strong><small>If the source has a function off but the target defines it as always on, the function is activated during conversion. That changes testing scope.</small><i class="material-symbols-outlined" aria-hidden="true">toggle_on</i></a>
      <a href="https://me.sap.com/notes/2214409" target="_blank" rel="noopener"><span>ADD</span><strong>Add-ons need a valid target path</strong><small>Some old add-ons cannot move to S/4HANA 2025 in one step. The restriction note lists examples that need an intermediate upgrade.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="https://me.sap.com/notes/2383051" target="_blank" rel="noopener"><span>BP</span><strong>Old vendor/contact data can create prerequisites</strong><small>For older source releases with vendors linked to contacts, the note defines minimum support-package and correction requirements. KNVK-LIFNR is one concrete data check mentioned by SAP.</small><i class="material-symbols-outlined" aria-hidden="true">manage_search</i></a>
      <a href="https://me.sap.com/notes/2233100" target="_blank" rel="noopener"><span>40</span><strong>A 40-character material number is a landscape change</strong><small>S/4HANA supports the longer material number, but downstream interfaces, extensions, files, mappings, and external systems may still assume the old length.</small><i class="material-symbols-outlined" aria-hidden="true">straighten</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment scenarios</p>
      <h2>Answer like a Lead: verify the boundary before promising the design.</h2>
      <p>The point is not to memorize note numbers. The point is to know when a note changes the architecture decision.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/atp/"><span>A</span><strong>“Can we use advanced intercompany sales with aATP?”</strong><small>Do not answer from feature knowledge alone. Confirm deployment, 2025 FPS, Note 3644701, Note 3493689, the process combination, and downstream fulfillment impact.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
      <a href="/labs/enterprise-context/procurement/"><span>B</span><strong>“The Fiori app has a Copy button. Is the control model fine?”</strong><small>No assumption. Check the release restriction. Note 3686533 turns a UI-looking detail into an authorization and governance question.</small><i class="material-symbols-outlined" aria-hidden="true">verified_user</i></a>
      <a href="/labs/enterprise-context/integrations/"><span>C</span><strong>“S/4 supports 40-character material numbers, so migration is safe?”</strong><small>No. SAP capability is only one side. Check IDocs, APIs, middleware mappings, custom tables, labels, files, partner systems, and test data.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/development/"><span>D</span><strong>“The switch is technically available. Can we activate it?”</strong><small>Not until release status is clear. SAP explicitly says some Business Functions must not be switched on even when activation is technically possible.</small><i class="material-symbols-outlined" aria-hidden="true">toggle_off</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
    <p><strong>30-second Lead answer:</strong> “When someone asks if S/4HANA 2025 can do something, I separate capability from release support. I confirm the deployment model and FPS, check the restriction and application notes, then check conversion blockers and interfaces. If something is technically possible but not released, I do not design around it. I document the restriction, the impact, and the fallback.”</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Keep the evidence fresh</p>
      <h2>A restriction note is a living project input.</h2>
      <p>SAP Note 3549655 explicitly says it can change and records important changes after the S/4HANA 2025 release. Re-check it at architecture freeze, conversion planning, regression planning, and before go-live.</p>
    </header>
    <div class="research-route-list">
      <a href="https://me.sap.com/notes/3549655" target="_blank" rel="noopener"><span>01</span><strong>Restriction Note 3549655</strong><small>General and application-area restrictions for SAP S/4HANA 2025 on-premise.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://me.sap.com/notes/3493301" target="_blank" rel="noopener"><span>02</span><strong>Release Information Note 3493301</strong><small>Release-level information for SAP S/4HANA 2025.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="https://help.sap.com/doc/2b87656c4eee4284a5eb8976c0fe88fc/2025/en-US/CONV_OP2025.pdf" target="_blank" rel="noopener"><span>03</span><strong>Conversion Guide for SAP S/4HANA 2025</strong><small>Conversion process, Maintenance Planner, Readiness Check, SI-Check, and other preparation activities.</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      <a href="/lab/"><span>CAREER</span><strong>Back to Career Lab</strong><small>Use this page as a Lead-level architecture and transformation skill: prove support before committing to a solution.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
