---
layout: default
title: "SAP Business AI and AI Platform Landscape — Enterprise Context Lab"
description: "A simple map of Joule, agents, Joule Studio, AI Core, Generative AI Hub, business grounding, and AI governance."
permalink: /labs/enterprise-context/business-ai/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
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
      <a class="research-canvas__button" href="#ai-layers">See the AI map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
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
    <p><strong>Remember the split.</strong> Joule is the experience. Joule Studio builds. AI Core runs. Generative AI Hub connects to models. Business Data Cloud grounds. AI Agent Hub governs.</p>
    <a href="/labs/enterprise-context/domains/">Open enterprise domains <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="ai-layers" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">AI layers</p>
      <h2>Use, build, run, ground, and govern.</h2>
      <p>Start with the responsibility. Then choose the component.</p>
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
      <h2>One component, one job.</h2>
      <p>Use the memory line first. Open the SAP source when you need the detail.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>{% if component.type == 'ai_asset' %}AI{% else %}PLT{% endif %}</span><strong>{{ component.title }}</strong><small><b>{{ component.remember }}</b> {{ component.description }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Decision guide</p>
      <h2>Choose by the job to be done.</h2>
      <p>This is the short version to remember for design discussions and assessment answers.</p>
    </header>
    <div class="research-route-list">
      {% for decision in topic.decision_guide %}
      {% assign selected = nil %}
      {% for component in topic.components %}{% if component.id == decision.primary_choice %}{% assign selected = component %}{% endif %}{% endfor %}
      <a href="{% if selected %}{{ selected.official_docs_url }}{% else %}/labs/enterprise-context/data/topics.json{% endif %}" target="_blank" rel="noopener"><span>→</span><strong>{{ decision.need }}</strong><small>{% if selected %}{{ selected.title }}. {% endif %}{{ decision.why }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Boundaries</p>
      <h2>Know what each component is not.</h2>
      <p>This prevents the common mistake of turning one AI component into the whole architecture.</p>
    </header>
    <div class="research-route-list">
      {% for component in topic.components %}
      <a href="{{ component.official_docs_url }}" target="_blank" rel="noopener"><span>!</span><strong>{{ component.title }}</strong><small>{{ component.not_for }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Licensing</p>
      <h2>Know the commercial boundary.</h2>
      <p>Use these as signals only. The customer contract remains the source of truth.</p>
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
      <p>Use these to remember how the layers connect.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in topic.reference_patterns %}
      <a href="/labs/enterprise-context/data/topics.json"><span>PATH</span><strong>{{ pattern.name }}</strong><small>{{ pattern.path }} · {{ pattern.fit }}</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
