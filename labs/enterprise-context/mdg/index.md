---
layout: default
title: "SAP Master Data Governance — Enterprise Context Lab"
description: "A practical SAP MDG Data Book: product options, governance processes, data domains, solution architecture, interface contracts, extensibility, logistics dependencies, implementation rules, and presales decisions."
permalink: /labs/enterprise-context/mdg/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-16
hide_global_cta: true
tags:
  - sap
  - mdg
  - master-data
  - logistics
  - data-governance
---

{% assign topic = site.data.labs.enterprise_context.topics.master_data_governance_landscape %}
{% assign contracts = site.data.labs.enterprise_context.topics.mdg_object_contracts %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">MDG</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Master Data Governance</p>
      <h1>MDG is a control system for master data decisions.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#mdg-graph">Open the MDG graph <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="MDG research status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Core maturity gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ contracts.object_contracts | size }}</strong><small>Object contracts</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ contracts.extension_matrix | size }}</strong><small>Extension decisions</small></div>
      <em>Source scan {{ contracts.source_reviewed_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <p><strong>Data Book:</strong> {{ topic.memory_model.data_book }}</p>
    <p><strong>Memory line:</strong> {{ topic.memory_model.phrase }}.</p>
    <a href="/labs/enterprise-context/mdg/scenario/">Run one object from request to business proof <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header><p class="research-canvas__eyebrow">Governance completion model</p><h2>Approved data is not yet business proof.</h2><p>I separate governance completion into four checkpoints. The model is intentionally broader than one MDG workflow because the business value appears only when consumers use the governed object correctly.</p></header>
    <div class="ecg-control-stack">
      <article><span>REQUEST</span><h3>Change is governed</h3><p>The reason, object, ownership, required attributes, validations, and approvals are explicit.</p><strong>Proof: the request follows the intended governance process.</strong></article>
      <article><span>ACTIVE</span><h3>Record is activated</h3><p>The approved master data becomes the authoritative active record for the chosen governance model.</p><strong>Proof: active data matches the approved decision.</strong></article>
      <article><span>REPLICATE</span><h3>Consumers receive it</h3><p>Replication, mapping, filtering, interface ownership, and error handling deliver the expected object version.</p><strong>Proof: target systems reconcile to the governed source.</strong></article>
      <article><span>USE</span><h3>Business process proves it</h3><p>Sales, procurement, planning, warehouse, transport, or finance can use the object without local repair.</p><strong>Proof: the target process consumes the intended data and outcome.</strong></article>
    </div>
    <p class="ecg-caption"><strong>Lead signal:</strong> “workflow approved” proves a governance step. It does not prove replication or business usability.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">verified_user</span>
    <p><strong>Evidence boundary:</strong> claim-level review currently confirms the 2025 FPS01 classic/cloud-ready mode boundary and the effects of switching cloud-ready mode. The four-checkpoint governance model is an authored reasoning frame; domain, replication, extension, and consumer-process details still require page-level human review.</p>
    <a href="/labs/assessment/factual-review/">Open factual review <span class="material-symbols-outlined" aria-hidden="true">fact_check</span></a>
  </section>

  <section class="research-canvas__inventory" id="mdg-graph" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">MDG graph spine</p>
      <h2>Do not start with a screen. Start with ownership.</h2>
      <p>The useful graph is not “MDG → Fiori”. It connects the business reason to the governed object, change process, quality controls, active record, interface contract, extension boundary, and every consumer that depends on it.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/deployments/"><span>01</span><strong>Business need → Product and deployment</strong><small>Choose S/4HANA MDG, cloud edition, or Public Edition capabilities by domain and ownership model.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/mdg/processes/"><span>02</span><strong>Domain → Governance capability → Process</strong><small>Central Governance, Consolidation, Mass Processing, and Data Quality solve different problems.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>03</span><strong>Master data → Logistics dependency → Business impact</strong><small>Trace Customer, Supplier, and Material into O2C, P2P, planning, warehouse, transport, and finance consequences.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="/labs/enterprise-context/mdg/architecture/"><span>04</span><strong>Application → Runtime → Integration → Operations</strong><small>See how Fiori, data models, workflow, DRF, SOAP, MDI, RAP, ABAP Cloud, roles, and monitoring form one solution.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/mdg/interfaces/"><span>05</span><strong>Object → Contract → Mapping → Consumer</strong><small>Use object-level contracts for Business Partner, Customer, Supplier, and Material instead of designing only from middleware.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="/labs/enterprise-context/mdg/extensions/"><span>06</span><strong>Requirement → Extension boundary</strong><small>Choose configuration, field, logic, node, service, or side-by-side patterns across classic, cloud-ready, and cloud edition.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="/labs/enterprise-context/mdg/scenario/"><span>07</span><strong>Govern → Replicate → Reconcile → Prove</strong><small>Run a synthetic Material case through procurement, planning, sales, warehouse, and finance.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/enterprise-context/mdg/implementation/"><span>08</span><strong>Ownership → Data model → Workflow → Quality → Operations</strong><small>Implementation succeeds when these decisions are coherent. Configuration alone is not a governance model.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">What MDG is for</p>
      <h2>Four jobs, not one giant “master data” box.</h2>
      <p>Ask which problem you are solving before selecting the capability.</p>
    </header>
    <div class="research-route-list">
      {% for capability in topic.capabilities %}
      <a href="/labs/enterprise-context/mdg/processes/#{{ capability.id | downcase }}"><span>CAP</span><strong>{{ capability.title }}</strong><small><b>{{ capability.remember }}</b> {{ capability.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Master data domains</p>
      <h2>Which object are you actually governing?</h2>
      <p>Business Partner and Material look like “master data” in the same sentence, but they carry very different process dependencies and integration contracts.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.domains %}
      <a href="/labs/enterprise-context/mdg/logistics/"><span>MD</span><strong>{{ domain.title }}</strong><small>{{ domain.business_use }}{% if domain.boundary %} <b>Boundary:</b> {{ domain.boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Object contracts</p>
      <h2>Approved data still needs an integration contract.</h2>
      <p>Each object contract includes ownership, transport, mappings, failure handling, monitoring, reconciliation, and a business proof of use.</p>
    </header>
    <div class="research-route-list">
      {% for contract in contracts.object_contracts %}
      <a href="/labs/enterprise-context/mdg/interfaces/"><span>INT</span><strong>{{ contract.title }}</strong><small>{{ contract.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Presales memory</p>
      <h2>Sell the control model, not the acronym.</h2>
      <p>MDG becomes relevant when bad or slow master-data decisions create measurable process cost.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.presales_decision_guide %}
      <a href="/labs/enterprise-context/mdg/implementation/#presales"><span>?</span><strong>{{ item.question }}</strong><small>{{ item.guidance }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
