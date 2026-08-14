---
layout: default
title: "SAP Industry Solutions — Enterprise Context Lab"
description: "A compact map of SAP industry-specific process and logistics patterns for automotive, retail, fashion, industrial manufacturing, and mill products."
permalink: /labs/enterprise-context/industries/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
---

{% assign topic = site.data.labs.enterprise_context.topics.industry_solution_landscape %}
{% assign deployments = site.data.labs.enterprise_context.topics.deployment_models %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Industries</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Industry solutions</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#industry-map">Open the industry map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Industry map status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.industries | size }}</strong><small>Industry patterns</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>3</strong><small>S/4 deployment models</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">factory</span>
    <p><strong>Remember:</strong> industry is an overlay. Keep the standard process, then add industry differences and deployment constraints.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare Public, Private, and On-Premise <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="industry-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Industry map</p>
      <h2>Learn the difference that changes the process.</h2>
      <p>Start with the memory line, then connect it to the standard SAP process.</p>
    </header>
    <div class="research-route-list">
      {% for industry in topic.industries %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>IND</span><strong>{{ industry.title }}</strong><small><b>{{ industry.remember }}</b> {{ industry.what_changes }}</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Deployment lens</p>
      <h2>Same industry, different design freedom.</h2>
      <p>Check the edition before assuming a feature, add-on, or extension is available.</p>
    </header>
    <div class="research-route-list">
      {% for model in deployments.deployment_models %}
      <a href="/labs/enterprise-context/deployment-models/"><span>DEP</span><strong>{{ model.short_title }}</strong><small><b>{{ model.remember }}</b> {{ model.industry_support }}</small><i class="material-symbols-outlined" aria-hidden="true">cloud_queue</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lead focus</p>
      <h2>Know the standard process and the industry delta.</h2>
      <p>Explain what changes in data, documents, planning, logistics, integration, and deployment.</p>
    </header>
    <div class="research-route-list">
      {% for industry in topic.industries %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>→</span><strong>{{ industry.title }}</strong><small>{{ industry.lead_focus }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Term check</p>
      <h2>SMD is not modeled as an industry.</h2>
      <p>Official SAP sources use SMD for Solution Manager Diagnostics and, in older documentation, Shared Master Data.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.term_checks %}
      <a href="/labs/enterprise-context/data/catalog.json"><span>?</span><strong>{{ item.term }}</strong><small>{{ item.note }}</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
