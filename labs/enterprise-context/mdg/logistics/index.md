---
layout: default
title: "SAP MDG for Logistics — Enterprise Context Lab"
description: "How Business Partner, Customer, Supplier, and Material master data connect to O2C, P2P, planning, warehouse, transport, and finance processes."
permalink: /labs/enterprise-context/mdg/logistics/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags: [sap, mdg, logistics, material, business-partner, o2c, p2p]
---

{% assign topic = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Logistics</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / logistics</p>
      <h1>Master data is upstream of almost every logistics exception.</h1>
      <p>A sales order, purchase order, MRP run, warehouse task, or freight document may fail far away from the place where the wrong master-data decision was made.</p>
      <a class="research-canvas__button" href="#dependencies">Trace the dependencies <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Four questions</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Who?</strong><small>Customer / Supplier / BP</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>What?</strong><small>Material / Product</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Where?</strong><small>Plant / sales / purchasing context</small></div>
      <div class="research-canvas__signal-line"><span>04</span><strong>Can it flow?</strong><small>Replicated and compatible?</small></div>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">hub</span>
    <p><strong>Design rule:</strong> central governance should own the attributes that need enterprise control. Application-specific attributes should stay with the system or role that understands their business logic unless the selected MDG scope intentionally governs them.</p>
    <p><strong>Cloud consequence:</strong> current MDG cloud edition is a core Business Partner solution. It does not remove the need to decide who owns supplier, customer, material, plant, sales-area, and purchasing-organization application data.</p>
    <a href="/labs/enterprise-context/mdg/deployments/">Compare deployment boundaries <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deep domain engineering</p>
      <h2>Start with grain, then connect it to the process.</h2>
      <p>The domain layer separates enterprise identity from plant, sales-area, company-code, purchasing-organization, valuation and warehouse meaning before workflow or replication is designed.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>MAT</span><strong>Material Domain</strong><small>Global identity, plant, sales, purchasing, storage, valuation, quality and warehouse grains.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/mdg/domains/business-partner/"><span>BP</span><strong>Business Partner / Customer / Supplier</strong><small>Shared party identity, roles, company code, sales area and purchasing organization.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/cases/"><span>CASE</span><strong>End-to-End Logistics Cases</strong><small>Trace governed data into O2C, P2P, MRP, EWM and Quality business proof.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/labs/enterprise-context/mdg/domains/"><span>MAP</span><strong>MDG Domain Engineering Hub</strong><small>Connect domain models to workflow, replication, consolidation and migration.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Logistics use cases</p>
      <h2>Govern the object, then trace the business process.</h2>
    </header>
    <div class="research-route-list">
      {% for use_case in topic.logistics_use_cases %}
      <a href="/labs/enterprise-context/data/topics.json"><span>SCN</span><strong>{{ use_case.title }}</strong><small><b>Path:</b> {{ use_case.path }} · {{ use_case.value }}{% if use_case.cloud_boundary %} <b>Cloud boundary:</b> {{ use_case.cloud_boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="dependencies" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Process dependency map</p>
      <h2>Bad master data appears downstream as “process trouble”.</h2>
      <p>This is the useful assessment and support view: identify the process symptom, walk upstream to the master data, then decide whether the defect is data, governance, replication, or local application logic.</p>
    </header>
    <div class="research-route-list">
      {% for dependency in topic.logistics_dependencies %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PROC</span><strong>{{ dependency.process }}</strong><small><b>Depends on:</b> {{ dependency.depends_on | join: ", " }}. <b>Typical impact:</b> {{ dependency.typical_impact }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Material / Product</p>
      <h2>One object, many business owners.</h2>
      <p>A material can be technically created and still be commercially useless. Logistics needs the correct organizational views and attributes for the intended process.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>CORE</span><strong>Basic identity</strong><small>Description, type, base unit, classification and other enterprise-level attributes define what the object is.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>PLAN</span><strong>Plant and planning context</strong><small>MRP and plant data determine whether the material can be planned and executed in the intended location.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>BUY</span><strong>Purchasing context</strong><small>Procurement needs the correct ordering, units, purchasing, and supplier-related data.</small><i class="material-symbols-outlined" aria-hidden="true">shopping_cart</i></a>
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>SELL</span><strong>Sales and shipping context</strong><small>Sales and delivery execution depend on usable sales, shipping, unit, weight, and related logistics attributes.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="/labs/enterprise-context/mdg/domains/material/"><span>VAL</span><strong>Valuation and accounting context</strong><small>The material must also be financially usable. Missing or incorrect valuation data can stop postings after logistics execution has already started.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business Partner</p>
      <h2>Core identity and application role are different layers.</h2>
      <p>This distinction matters most in federated MDG. A clean name and address do not automatically create a usable customer or supplier in every consuming application.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/domains/business-partner/"><span>BP</span><strong>Core Business Partner</strong><small>Identity, addresses, relationships, and shared attributes can be centrally governed as enterprise core data.</small><i class="material-symbols-outlined" aria-hidden="true">badge</i></a>
      <a href="/labs/enterprise-context/mdg/domains/business-partner/"><span>CUST</span><strong>Customer layer</strong><small>Sales-area and company-specific attributes belong to the application context and must have an explicit owner.</small><i class="material-symbols-outlined" aria-hidden="true">storefront</i></a>
      <a href="/labs/enterprise-context/mdg/domains/business-partner/"><span>SUP</span><strong>Supplier layer</strong><small>Purchasing-organization and company-specific attributes need the same ownership decision on the procurement side.</small><i class="material-symbols-outlined" aria-hidden="true">handshake</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Consumers</p>
      <h2>MDG does not own every downstream business rule.</h2>
      <p>S/4HANA, EWM, TM, IBP, Ariba, Business Network, analytics, and non-SAP applications can all consume master data. The exact integration route depends on the landscape. The important design question is who owns each attribute and how approved values stay synchronized.</p>
    </header>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>