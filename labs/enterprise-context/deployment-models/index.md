---
layout: default
title: "SAP S/4HANA Deployment Models — Enterprise Context Lab"
description: "A compact comparison of SAP S/4HANA Cloud Public Edition, SAP S/4HANA Cloud Private Edition, and SAP S/4HANA on-premise."
permalink: /labs/enterprise-context/deployment-models/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
---

{% assign topic = site.data.labs.enterprise_context.topics.deployment_models %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Deployment Models</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Deployment models</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#deployment-models">Compare the three models <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Deployment model status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>3</strong><small>Deployment models</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.memory_compare | size }}</strong><small>Comparison points</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">cloud</span>
    <p><strong>Remember:</strong> deployment changes scope, extensions, upgrades, and operations. It does not replace the business-process model.</p>
    <a href="/labs/enterprise-context/industries/">Open industry solutions <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="deployment-models" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Three S/4HANA models</p>
      <h2>Public = standardize. Private = flexible cloud. On-Premise = full control.</h2>
      <p>Start with the memory line, then check scope, extensibility, upgrades, and operations.</p>
    </header>
    <div class="research-route-list">
      {% for model in topic.deployment_models %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>DEP</span><strong>{{ model.short_title }}</strong><small><b>{{ model.remember }}</b> {{ model.what_it_is }}</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">What changes</p>
      <h2>Five things to compare first.</h2>
      <p>These dimensions usually decide the architecture faster than product-name debates.</p>
    </header>
    <div class="research-route-list">
      {% for row in topic.memory_compare %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>↔</span><strong>{{ row.dimension }}</strong><small>Public: {{ row.public }} · Private: {{ row.private }} · On-Premise: {{ row.onprem }}</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Choose the operating model after the business need.</h2>
      <p>{{ topic.lead_answer }}</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      {% assign selected = nil %}
      {% for model in topic.deployment_models %}{% if model.id == decision.primary_choice %}{% assign selected = model %}{% endif %}{% endfor %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}Primary: {{ selected.short_title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Watch-outs</p>
      <h2>The same S/4HANA name does not mean the same design freedom.</h2>
      <p>Always validate the exact feature, release, add-on, and extension path.</p>
    </header>
    <div class="research-route-list">
      {% for model in topic.deployment_models %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>!</span><strong>{{ model.short_title }}</strong><small>{{ model.watch_out }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
