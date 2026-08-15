---
layout: default
title: "Enterprise AI Technology Landscape — Business AI Lab"
description: "A vendor-neutral map of enterprise AI technology families, platform roles, fit conditions, limits, and official source references."
permalink: /labs/business-ai/technologies/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - enterprise-ai
  - platforms
  - agents
  - architecture
---

{% assign tech = site.data.labs.business_ai.technology_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Technologies</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / enterprise technology landscape</p>
      <h1>Choose a capability.<br />Not a logo.</h1>
      <p>Enterprise AI is a stack of different jobs: model access, prediction, optimization, document intelligence, retrieval, workflow, agents, integration, data, evaluation, and governance. One platform can cover several jobs, but no platform removes the need to design the process boundary.</p>
      <a class="research-canvas__button" href="#family-list">Open technology families <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Technology map</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ tech.families | size }}</strong><small>Capability families</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ tech.platforms | size }}</strong><small>Platform examples</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ tech.source_registry | size }}</strong><small>Primary sources</small></div>
      <em>Platform names change faster than business patterns. Capability families are the more stable layer.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Problem:</strong> enterprise AI architecture becomes vendor-led when teams select a platform before separating prediction, language, workflow, integration, deterministic rules, and process ownership.</p>
    <p><strong>Selection rule:</strong> start from the business pattern and required controls. Then map the smallest technology set that can implement it.</p>
    <p><strong>Composition rule:</strong> a serious solution often combines several families. Example: document extraction → deterministic validation → workflow → human approval → ERP posting.</p>
    <a href="/labs/business-ai/domains/">Map technologies to business domains <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="family-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Capability families</p>
      <h2>Stable architecture categories.</h2>
      <p>The family describes the technical job. Products are examples, not the ontology.</p>
    </header>
    <div class="research-route-list">
      {% for family in tech.families %}
      <a href="#{{ family.id }}"><span>{{ forloop.index }}</span><strong>{{ family.title }}</strong><small>{{ family.job }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for family in tech.families %}
  <section class="research-canvas__inventory" id="{{ family.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Technology family / {{ family.id }}</p>
      <h2>{{ family.title }}</h2>
      <p>{{ family.job }}</p>
    </header>
    <div class="research-route-list">
      <a href="#{{ family.id }}"><span>FIT</span><strong>Use when</strong><small>{{ family.use_when | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#{{ family.id }}"><span>NO</span><strong>Not enough when</strong><small>{{ family.not_enough_when | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="#{{ family.id }}"><span>EX</span><strong>Platform and technology examples</strong><small>{{ family.platform_examples | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__inventory" id="platforms" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Platform examples</p>
      <h2>Compare by role in the architecture.</h2>
      <p>The list mixes horizontal AI platforms and application-native platforms on purpose. They solve different layers of the same enterprise problem.</p>
    </header>
    <div class="research-route-list">
      {% for platform in tech.platforms %}
        {% assign source = nil %}
        {% for item in tech.source_registry %}
          {% if item.id == platform.source_id %}{% assign source = item %}{% endif %}
        {% endfor %}
        {% if source %}
        <a href="{{ source.url }}" target="_blank" rel="noopener"><span>{{ platform.category | slice: 0, 3 | upcase }}</span><strong>{{ platform.name }}</strong><small>{{ platform.role }} · Source: {{ source.publisher }} · reviewed {{ source.reviewed_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
        {% else %}
        <a href="#platforms"><span>SYS</span><strong>{{ platform.name }}</strong><small>{{ platform.role }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
        {% endif %}
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Architecture sequence</p><h2>Separate four decisions.</h2></div>
    <ol>
      <li><span>01</span><strong>Business pattern</strong><p>What task or decision changes, and how will the business measure it?</p></li>
      <li><span>02</span><strong>System boundary</strong><p>Where do identity, rules, records, approvals, and side effects remain deterministic?</p></li>
      <li><span>03</span><strong>AI capability</strong><p>Which uncertain part needs extraction, retrieval, prediction, optimization, generation, or agentic planning?</p></li>
      <li><span>04</span><strong>Platform fit</strong><p>Choose products by integration, security, operating model, skills, cost, and lifecycle requirements.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
