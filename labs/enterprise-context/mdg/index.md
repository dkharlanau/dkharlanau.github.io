---
layout: default
title: "SAP Master Data Governance — Enterprise Context Lab"
description: "A practical SAP MDG Data Book: products, governance processes, data-model anatomy, ownership, process impact, solution architecture, interface contracts, extensibility, implementation, and assessment reasoning."
permalink: /labs/enterprise-context/mdg/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
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
{% assign data_model = site.data.labs.enterprise_context.topics.mdg_data_model_anatomy %}
{% assign impact = site.data.labs.enterprise_context.topics.mdg_attribute_process_impact %}
{% assign ownership = site.data.labs.enterprise_context.topics.mdg_ownership_federation %}
{% assign reasoning = site.data.labs.enterprise_context.topics.mdg_assessment_reasoning %}

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
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ contracts.object_contracts | size }}</strong><small>Object contracts</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ impact.impact_traces | size }}</strong><small>Attribute impact traces</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ reasoning.cases | size }}</strong><small>Reasoning cases</small></div>
      <em>Source scan {{ reasoning.source_reviewed_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">menu_book</span>
    <p><strong>Data Book:</strong> {{ topic.memory_model.data_book }}</p>
    <p><strong>Knowledge path:</strong> Object structure → attribute impact → ownership → governance → integration → business proof.</p>
    <a href="/labs/enterprise-context/mdg/reasoning/">Test the model with Explain, Compare, Design, and Diagnose cases <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="mdg-graph" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">MDG graph spine</p>
      <h2>Do not start with a screen. Start with the object and its owner.</h2>
      <p>The useful graph connects the business reason to the governed object, entity structure, attribute impact, decision owner, change process, quality controls, active record, interface contract, extension boundary, and every consumer that depends on it.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/deployments/"><span>01</span><strong>Business need → Product and deployment</strong><small>Choose S/4HANA MDG, cloud edition, or Public Edition capabilities by domain and ownership model.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/mdg/processes/"><span>02</span><strong>Domain → Governance capability → Process</strong><small>Central Governance, Consolidation, Mass Processing, and Data Quality solve different problems.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/mdg/data-model/"><span>03</span><strong>Root → Entity → Attribute → Active state</strong><small>Understand storage/use types, keys, relationships, staging, active-area decisions, and the Material model anatomy.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/mdg/ownership/"><span>04</span><strong>Core identity → Application ownership → Federation</strong><small>Separate shared Business Partner identity from Sales, Procurement, and Finance decision rights.</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="/labs/enterprise-context/mdg/impact/"><span>05</span><strong>Attribute → Determination → Process → Failure</strong><small>Trace loading group, shipping condition, MRP type, sales-area data, and purchasing-organization data into business execution.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/mdg/logistics/"><span>06</span><strong>Master data → Logistics dependency → Business impact</strong><small>Trace Customer, Supplier, and Material into O2C, P2P, planning, warehouse, transport, and finance consequences.</small><i class="material-symbols-outlined" aria-hidden="true">local_shipping</i></a>
      <a href="/labs/enterprise-context/mdg/architecture/"><span>07</span><strong>Application → Runtime → Integration → Operations</strong><small>See how Fiori, data models, workflow, DRF, SOAP, MDI, RAP, ABAP Cloud, roles, and monitoring form one solution.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/mdg/interfaces/"><span>08</span><strong>Object → Contract → Mapping → Consumer</strong><small>Use object-level contracts for Business Partner, Customer, Supplier, and Material instead of designing only from middleware.</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      <a href="/labs/enterprise-context/mdg/extensions/"><span>09</span><strong>Requirement → Extension boundary</strong><small>Choose configuration, field, logic, node, service, or side-by-side patterns across classic, cloud-ready, and cloud edition.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
      <a href="/labs/enterprise-context/mdg/scenario/"><span>10</span><strong>Govern → Replicate → Reconcile → Prove</strong><small>Run a synthetic Material case through procurement, planning, sales, warehouse, and finance.</small><i class="material-symbols-outlined" aria-hidden="true">science</i></a>
      <a href="/labs/enterprise-context/mdg/implementation/"><span>11</span><strong>Ownership → Data model → Workflow → Quality → Operations</strong><small>Implementation succeeds when these decisions are coherent. Configuration alone is not a governance model.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="/labs/enterprise-context/mdg/reasoning/"><span>12</span><strong>Fact → Boundary → Decision → Proof</strong><small>Practice Explain, Compare, Design, and Diagnose answers and score reasoning instead of vocabulary.</small><i class="material-symbols-outlined" aria-hidden="true">school</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Knowledge model</p>
      <h2>Four questions make the subject easier to reason about.</h2>
      <p>These views turn product facts into a reusable model for design and diagnosis.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/data-model/"><span>MODEL</span><strong>{{ data_model.business_question }}</strong><small>{{ data_model.memory_model.phrase }}</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/mdg/impact/"><span>IMPACT</span><strong>{{ impact.business_question }}</strong><small>{{ impact.memory_model.phrase }}</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      <a href="/labs/enterprise-context/mdg/ownership/"><span>OWNER</span><strong>{{ ownership.business_question }}</strong><small>{{ ownership.memory_model.phrase }}</small><i class="material-symbols-outlined" aria-hidden="true">person_check</i></a>
      <a href="/labs/enterprise-context/mdg/reasoning/"><span>LEAD</span><strong>{{ reasoning.business_question }}</strong><small>{{ reasoning.memory_model.phrase }}</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
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
