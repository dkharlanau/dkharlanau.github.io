---
layout: default
title: "SAP MDG Extension Matrix — Enterprise Context Lab"
description: "A practical SAP MDG extension matrix for fields, validations, workflow, nodes, UI, and side-by-side applications across classic, cloud-ready, and cloud edition."
permalink: /labs/enterprise-context/mdg/extensions/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags: [sap, mdg, extensibility, rap, abap-cloud, clean-core, architecture]
---

{% assign topic = site.data.labs.enterprise_context.topics.mdg_object_contracts %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li><a href="/labs/enterprise-context/mdg/">MDG</a></li><li aria-current="page">Extensions</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">MDG / extension decisions</p>
      <h1>Extend the governed object, not every nearby requirement.</h1>
      <p>Use configuration first. Then choose a released field, logic, node, or service extension. If the responsibility is no longer master-data governance, keep it side-by-side.</p>
      <a class="research-canvas__button" href="#matrix">Open the decision matrix <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Extension order</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Config</strong><small>No code if possible</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Extend</strong><small>Released points only</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Separate</strong><small>Side-by-side when needed</small></div>
      <em>{{ topic.memory_model.extension_phrase }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">extension</span>
    <p><strong>Problem:</strong> MDG extensions become expensive when a requirement is implemented in the wrong layer or breaks cloud-ready boundaries.</p>
    <p><strong>Cloud-ready rule:</strong> RAP extensibility is opt-in. Data model, behavior, nodes, and service exposure must be explicitly enabled by the business-object provider.</p>
    <p><strong>Architecture rule:</strong> a technical extension point does not prove that the requirement belongs inside MDG.</p>
    <a href="/labs/enterprise-context/mdg/architecture/">See the full solution architecture <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="matrix" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Extension matrix</p>
      <h2>Requirement → deployment → safest extension boundary.</h2>
      <p>The same business request can require a different technical answer in classic MDG, cloud-ready mode, or SAP MDG cloud edition.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.extension_matrix %}
      <a href="/labs/enterprise-context/data/topics.json"><span>DEC</span><strong>{{ decision.requirement }}</strong><small><b>Classic:</b> {{ decision.classic_s4.preferred }} <b>Cloud-ready:</b> {{ decision.cloud_ready.preferred }} <b>Cloud edition:</b> {{ decision.cloud_edition.preferred }}</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      {% endfor %}
    </div>
  </section>

  {% for decision in topic.extension_matrix %}
  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">{{ decision.id }}</p>
      <h2>{{ decision.requirement }}</h2>
      <p>{{ decision.cross_cutting_rule }}</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/mdg/deployments/"><span>S4</span><strong>Classic S/4HANA MDG</strong><small>{{ decision.classic_s4.preferred }} <b>Check:</b> {{ decision.classic_s4.check }}</small><i class="material-symbols-outlined" aria-hidden="true">dns</i></a>
      <a href="/labs/enterprise-context/mdg/architecture/"><span>RAP</span><strong>Cloud-ready MDG</strong><small>{{ decision.cloud_ready.preferred }} <b>Check:</b> {{ decision.cloud_ready.check }}</small><i class="material-symbols-outlined" aria-hidden="true">code</i></a>
      <a href="/labs/enterprise-context/mdg/deployments/"><span>CE</span><strong>MDG cloud edition</strong><small>{{ decision.cloud_edition.preferred }} <b>Check:</b> {{ decision.cloud_edition.check }}</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Assessment answer:</strong> {{ topic.lead_assessment_patterns[1].answer }}</p>
    <a href="/labs/enterprise-context/mdg/interfaces/">Return to object contracts <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
