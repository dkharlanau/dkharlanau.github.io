---
layout: default
title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
description: "A compact map of SAP Business AI, Joule, agents, Joule Studio, AI Core, AI Launchpad, generative AI hub, grounding, and governance."
permalink: /labs/enterprise-context/business-ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
tags:
  - sap
  - business-ai
  - joule
  - btp
  - architecture
---

{% assign topic = site.data.labs.enterprise_context.topics.business_ai_platform_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Business AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Business AI</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#ai-layers">Open the AI map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Review status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.layers | size }}</strong><small>AI layers</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.components | size }}</strong><small>Components</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Problem:</strong> SAP Business AI names overlap, so architecture responsibilities are easy to mix up.</p>
    <p><strong>Remember:</strong> use AI, build AI, run AI, ground AI, and govern AI. Keep these responsibilities separate.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare S/4HANA deployment models <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="ai-layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">AI layers</p>
      <h2>Start with the job, not the product name.</h2>
      <p>Each layer answers one question: use, act, build, run, ground, or govern.</p>
    </header>
    <div class="research-route-list">
      {% for layer in topic.layers %}
      <a href="#components"><span>AI</span><strong>{{ layer.title }}</strong><small>{{ layer.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">layers</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="components" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Components</p>
      <h2>One component, one memory hook.</h2>
      <p>Use the short line first. Open the SAP source when you need the deeper detail.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>{% if component.type == 'ai_asset' %}AI{% else %}PLT{% endif %}</span><strong>{{ component.title }}</strong><small><b>{% if component.remember %}{{ component.remember }}{% else %}{{ component.architecture_role }}{% endif %}</b> {{ component.description }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Which component owns the job?</h2>
      <p>Several components can work together. Pick the primary owner for the responsibility.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      {% assign selected = nil %}
      {% for component in topic.components %}{% if component.id == decision.primary_choice %}{% assign selected = component %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}{{ selected.title }} · {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Boundaries</p>
      <h2>Do not make one component the whole AI stack.</h2>
      <p>Joule is not AI Core. AI Core is not the Generative AI Hub. Joule Studio is not Integration Suite.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ component.title }}</strong><small>{{ component.not_for }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Licensing signals</p>
      <h2>Check the service you actually use.</h2>
      <p>Licensing can come from Joule, SAP Build, BTP services, AI Units, model usage, data services, and application rights.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_commercial_url }}" target="_blank" rel="noopener"><span>LIC</span><strong>{{ component.title }}</strong><small>{{ component.licensing.commercial_model }}{% if component.licensing.metric %} · {{ component.licensing.metric }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">contract</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference patterns</p>
      <h2>Typical combinations.</h2>
      <p>Use the pattern to remember ownership. Validate APIs, authorization, grounding, and evaluation separately.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.reference_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
