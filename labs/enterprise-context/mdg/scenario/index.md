---
layout: default
title: "SAP MDG Synthetic Material Scenario — Enterprise Context Lab"
description: "A synthetic end-to-end SAP MDG Material scenario that connects governance, replication, downstream logistics use, failure diagnosis, and reconciliation."
permalink: /labs/enterprise-context/mdg/scenario/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags: [sap, mdg, material, logistics, drf, idoc, scenario, assessment]
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_object_contracts %}
{% assign scenario = topic.synthetic_scenario %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Synthetic scenario</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / synthetic enterprise case</p>
      <h1>Prove the master data in the business process.</h1>
      <p>{{ scenario.business_goal }}</p>
      <a class="research-canvas__button" href="#scenario-flow">Follow the case <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Scenario</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Material</strong><small>Governed object</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>S/4 MDG</strong><small>Product choice</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>5</strong><small>Business areas prove use</small></div>
      <em>Synthetic learning case · no client data</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">factory</span>
    <p><strong>Enterprise:</strong> {{ scenario.enterprise }} is fictional.</p>
    <p><strong>Why S/4HANA MDG:</strong> {{ scenario.reason }}</p>
    <a href="/labs/enterprise-context/mdg/interfaces/">See the Material interface contract <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Ownership model</p>
      <h2>One material, several attribute owners.</h2>
      <p>A Product Data Owner controls the object, but plant, purchasing, sales, warehouse, and finance specialists own different parts of the usable record.</p>
    </header>
    <div class="research-route-list">
      {% for actor in scenario.actors %}
      <a href="/labs/enterprise-context/data/topics.json"><span>OWN</span><strong>{{ actor }}</strong><small>Owns or operates part of the governed material lifecycle.</small><i class="material-symbols-outlined" aria-hidden="true">person</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="scenario-flow" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">End-to-end path</p>
      <h2>Request → enrich → validate → activate → distribute → reconcile → prove.</h2>
      <p>The final test is not MDG activation. The final test is whether procurement, planning, sales, warehouse, and finance can use the material.</p>
    </header>
    <div class="research-route-list">
      {% for step in scenario.flow %}
      <a href="/labs/enterprise-context/data/topics.json"><span>{{ forloop.index }}</span><strong>{{ step.title }}</strong><small>{{ step.detail }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Data scope</p>
      <h2>A material is usable only when the required views agree.</h2>
      <p>The scenario connects core identity to plant/MRP, procurement, sales, warehouse, and valuation data.</p>
    </header>
    <div class="research-route-list">
      {% for group in scenario.requested_data %}
      <a href="/labs/enterprise-context/data/topics.json"><span>DATA</span><strong>{{ group[0] | replace: '_', ' ' | capitalize }}</strong><small>{{ group[1] | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Replication contract</p>
      <h2>Do not reduce the object to MATMAS.</h2>
      <p><strong>Primary pattern:</strong> {{ scenario.integration_contract.primary }}.</p>
    </header>
    <div class="research-route-list">
      {% for item in scenario.integration_contract.dependent_contracts %}
      <a href="/labs/enterprise-context/mdg/interfaces/"><span>MSG</span><strong>Dependent contract</strong><small>{{ item }}</small><i class="material-symbols-outlined" aria-hidden="true">sync_alt</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Injected failure</p>
      <h2>{{ scenario.injected_failure.title }}</h2>
      <p><strong>Symptom:</strong> {{ scenario.injected_failure.symptom }}</p>
    </header>
    <div class="research-route-list">
      {% for item in scenario.injected_failure.diagnosis_path %}
      <a href="/labs/enterprise-context/data/topics.json"><span>{{ forloop.index }}</span><strong>{{ item }}</strong><small>Follow the contract from business need to target-side acceptance.</small><i class="material-symbols-outlined" aria-hidden="true">troubleshoot</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lightbulb</span>
    <p><strong>Architecture lesson:</strong> {{ scenario.injected_failure.architecture_lesson }}</p>
    <p><strong>Assessment memory:</strong> {{ topic.lead_assessment_patterns[2].answer }}</p>
    <a href="/labs/enterprise-context/mdg/extensions/">Open the extension matrix <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
