---
layout: default
title: "Business AI Implementation Cases — Business AI Lab"
description: "Public Business AI implementation cases with process context, technology stack, reported metrics, evidence grade, limitations, and consultant notes."
permalink: /labs/business-ai/cases/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - ai-use-cases
  - procurement
  - supply-chain
  - customer-service
---

{% assign catalog = site.data.labs.business_ai.catalog %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Cases</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / implementation cases</p>
      <h1>Collect evidence.<br />Keep the missing pieces visible.</h1>
      <p>These are not “best AI companies”. They are public cases that expose enough process, technology, or outcome detail to learn from. A missing KPI is recorded as a missing KPI, not repaired with imagination.</p>
      <a class="research-canvas__button" href="#case-list">Open cases <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Evidence set</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ catalog.cases | size }}</strong><small>Cases</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ catalog.source_registry | size }}</strong><small>Sources</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>0</strong><small>Grade A so far</small></div>
      <em>That zero is intentional. Public customer stories rarely disclose enough measurement detail for the strongest evidence grade.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
    <p><strong>Evidence rule:</strong> reported numbers are useful, but a vendor/customer case study is not the same thing as an audited experiment.</p>
    <p><strong>Catalog rule.</strong> For every strong-looking number, keep the source owner, baseline, time period, and missing measurement visible when known.</p>
    <a href="/labs/business-ai/patterns/">Open reusable patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="case-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Case index</p>
      <h2>From customer service to procurement and logistics.</h2>
      <p>The first set deliberately mixes generative AI, document AI, forecasting, and optimization. Business value does not care which technology category wins a conference slide.</p>
    </header>
    <div class="research-route-list">
      {% for item in catalog.cases %}
      <a href="#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>{{ item.process }} · Pattern: {{ item.pattern }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for item in catalog.cases %}
  <section class="research-canvas__inventory" id="{{ item.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Case / evidence {{ item.evidence_grade }} / {{ item.industry }}</p>
      <h2>{{ item.company }} · {{ item.title }}</h2>
      <p><strong>Process:</strong> {{ item.process }}. <strong>Problem:</strong> {{ item.problem }}</p>
    </header>

    <div class="research-route-list">
      <a href="/labs/business-ai/patterns/#{{ item.pattern }}"><span>PAT</span><strong>Pattern</strong><small>{{ item.pattern }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#{{ item.id }}"><span>SYS</span><strong>Implementation</strong><small>{{ item.implementation }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="#{{ item.id }}"><span>TECH</span><strong>Technology</strong><small>{{ item.technology.vendors | join: ", " }} · {{ item.technology.products | join: ", " }} · Models: {{ item.technology.models | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#{{ item.id }}"><span>INT</span><strong>Integration note</strong><small>{{ item.technology.integration_notes }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% for result in item.reported_results %}
      <a href="#{{ item.id }}"><span>KPI</span><strong>{{ result.metric }}</strong><small>{{ result.value }} · {{ result.claim_type }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      {% endfor %}
      <a href="#{{ item.id }}"><span>!</span><strong>Limits</strong><small>{{ item.limits | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
      <a href="#{{ item.id }}"><span>NOTE</span><strong>Consultant note</strong><small>{{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">comment</i></a>
      {% for source_id in item.source_ids %}
        {% for source in catalog.source_registry %}
          {% if source.id == source_id %}
          <a href="{{ source.url }}" target="_blank" rel="noopener"><span>SRC</span><strong>{{ source.publisher }} · {{ source.title }}</strong><small>{{ source.source_type }}{% if source.published_at %} · {{ source.published_at }}{% endif %} · reviewed {{ source.reviewed_at }}</small><i class="material-symbols-outlined" aria-hidden="true">open_in_new</i></a>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__inventory" id="evidence-grades" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence model</p>
      <h2>Do not give every source the same weight.</h2>
      <p>The grade is about the evidence behind the result, not about whether the company or technology is good.</p>
    </header>
    <div class="research-route-list">
      {% for grade_pair in catalog.evidence_grades %}
      {% assign grade_id = grade_pair[0] %}
      {% assign grade = grade_pair[1] %}
      <a href="#evidence-grades"><span>{{ grade_id }}</span><strong>{{ grade.label }}</strong><small>{{ grade.rule }}</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
