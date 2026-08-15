---
layout: default
title: "SAP MDG Interface Contracts — Enterprise Context Lab"
description: "Problem-first SAP MDG interface contracts for BP, Customer, Supplier, and Material with mapping, errors, reconciliation, and business proof."
permalink: /labs/enterprise-context/mdg/interfaces/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags: [sap, mdg, integration, drf, soap, idoc, mdi, master-data]
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_object_contracts %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Interfaces</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / object interface contracts</p>
      <h1>An interface is finished when the consumer can use the object.</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#contracts">Open the contracts <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Memory model</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Owner</strong><small>Who is authoritative?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Contract</strong><small>What is transported?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Proof</strong><small>Can the consumer use it?</small></div>
      <em>{{ topic.memory_model.phrase }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">sync_alt</span>
    <p><strong>Boundary:</strong> a successful message is not the business outcome. The target still has to identify the object, map codes, accept the data, and use it in a transaction.</p>
    <p><strong>Material warning:</strong> one business object can require several technical messages. MATMAS alone must not be assumed to cover classification, revision, quality, or every dependent data set.</p>
    <a href="/labs/enterprise-context/mdg/extensions/">Choose an extension path <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="contracts" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Object contracts</p>
      <h2>Start from the governed object, not from middleware.</h2>
      <p>Each contract records ownership, transport, mappings, failure modes, monitoring, and a downstream proof of use.</p>
    </header>
    <div class="research-route-list">
      {% for contract in topic.object_contracts %}
      <a href="/labs/enterprise-context/data/topics.json"><span>INT</span><strong>{{ contract.title }}</strong><small>{{ contract.purpose }}{% if contract.architecture_boundary %} <b>Boundary:</b> {{ contract.architecture_boundary }}{% endif %}{% if contract.deployment_boundary %} <b>Boundary:</b> {{ contract.deployment_boundary }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  {% for contract in topic.object_contracts %}
  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">{{ contract.governed_object }}</p>
      <h2>{{ contract.title }}</h2>
      <p>{{ contract.purpose }}</p>
    </header>
    <div class="research-route-list">
      {% if contract.mappings %}<a href="/labs/enterprise-context/data/topics.json"><span>MAP</span><strong>Mappings</strong><small>{{ contract.mappings | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">conversion_path</i></a>{% endif %}
      {% if contract.failure_modes %}<a href="/labs/enterprise-context/data/topics.json"><span>!</span><strong>Failure model</strong><small>{{ contract.failure_modes | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>{% endif %}
      {% if contract.monitoring %}<a href="/labs/enterprise-context/data/topics.json"><span>OPS</span><strong>Monitoring and reconciliation</strong><small>{{ contract.monitoring | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>{% endif %}
      {% if contract.proof_of_use %}<a href="/labs/enterprise-context/mdg/scenario/"><span>TEST</span><strong>Business proof</strong><small>{{ contract.proof_of_use | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>{% endif %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Design checklist</p>
      <h2>Eleven questions before an interface is called complete.</h2>
      <p>This checklist works for SOAP, IDoc/ALE, MDI, files, or application APIs.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.contract_design_checklist %}
      <a href="/labs/enterprise-context/data/topics.json"><span>{{ forloop.index }}</span><strong>{{ item }}</strong><small>Capture the answer in the object contract and operating model.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Assessment answer:</strong> {{ topic.lead_assessment_patterns[0].answer }}</p>
    <a href="/labs/enterprise-context/mdg/scenario/">Run the synthetic Material case <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
