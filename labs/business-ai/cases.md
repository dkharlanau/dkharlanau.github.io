---
layout: default
title: "Business AI Implementation Cases — Business AI Lab"
description: "Public Business AI implementation cases with process context, technology stack, reported metrics, evidence grade, limitations, and consultant notes."
permalink: /labs/business-ai/cases/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
last_reviewed: 2026-09-22
hide_global_cta: true
tags:
  - business-ai
  - ai-use-cases
  - procurement
  - supply-chain
  - customer-service
  - sales
  - manufacturing
  - master-data
---

{% assign catalog = site.data.labs.business_ai.catalog %}
{% assign expansion = site.data.labs.business_ai.expansion_2026_08_15 %}
{% assign expansion_b = site.data.labs.business_ai.expansion_2026_08_15_b %}
{% assign all_cases = catalog.cases | concat: expansion.cases | concat: expansion_b.cases %}
{% assign all_sources = catalog.source_registry | concat: expansion.source_registry | concat: expansion_b.source_registry %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Cases</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / implementation cases</p>
      <h1>Read the case.<br />Keep the evidence separate.</h1>
      <p>We use public implementation stories to understand what a company tried, where AI entered the process, and what result was reported. The useful part is not the headline number by itself. It is the combination of process context, implementation detail, source quality, and the limits that remain visible around the claim.</p>
      <a class="research-canvas__button" href="#case-list">Open cases <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Evidence set</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ all_cases | size }}</strong><small>Cases</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ all_sources | size }}</strong><small>Sources</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>0</strong><small>Grade A so far</small></div>
      <em>That zero is useful. Public case studies often describe outcomes without enough measurement detail for the strongest evidence grade.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">fact_check</span>
    <div>
      <p><strong>A case study is evidence, but it is not neutral evidence.</strong> Vendor and customer stories can show that a solution existed, which process it touched, and what the participants reported. They do not automatically tell us what would happen in another company.</p>
      <p>For every result we therefore keep the source owner, reported metric, known baseline or period, and the missing pieces visible when the source provides them. We do not turn an absent KPI into an estimate.</p>
    </div>
    <a href="/labs/business-ai/patterns/">Open reusable patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="case-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Case index</p>
      <h2>Different processes, different reasons to use AI.</h2>
      <p>The collection spans sales, procurement, planning, manufacturing, service, master data, and other enterprise work. It also mixes several technical approaches: generative AI, document processing, forecasting, recommendation, optimization, and data foundations. We keep them together because the business job is the more useful comparison point than the technology label.</p>
    </header>
    <div class="research-route-list">
      {% for item in all_cases %}
      <a href="#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>{{ item.process }} · Pattern: {{ item.pattern }}{% if item.case_kind %} · {{ item.case_kind }}{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for item in all_cases %}
  <section class="research-canvas__inventory" id="{{ item.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Case / evidence {{ item.evidence_grade }} / {{ item.industry }}{% if item.case_kind %} / {{ item.case_kind }}{% endif %}</p>
      <h2>{{ item.company }} · {{ item.title }}</h2>
      <p><strong>Process:</strong> {{ item.process }}. <strong>Problem:</strong> {{ item.problem }}</p>
    </header>

    <div class="case-evidence-list">
      <a href="/labs/business-ai/patterns/#{{ item.pattern }}"><span>PAT</span><strong>Primary pattern</strong><small>{{ item.pattern }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      {% if item.secondary_patterns %}
      <div class="case-evidence-row"><span>PAT+</span><strong>Secondary patterns</strong><small>{{ item.secondary_patterns | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></div>
      {% endif %}
      <div class="case-evidence-row"><span>SYS</span><strong>Implementation</strong><small>{{ item.implementation }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></div>
      <div class="case-evidence-row"><span>TECH</span><strong>Technology</strong><small>{{ item.technology.vendors | join: ", " }} · {{ item.technology.products | join: ", " }} · Models: {{ item.technology.models | join: ", " }}</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></div>
      <div class="case-evidence-row"><span>INT</span><strong>Integration note</strong><small>{{ item.technology.integration_notes }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></div>
      {% for result in item.reported_results %}
      <div class="case-evidence-row case-evidence-row--metric"><span>KPI</span><strong>{{ result.metric }}</strong><small>{{ result.value }} · {{ result.claim_type }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></div>
      {% endfor %}
      <div class="case-evidence-row case-evidence-row--boundary"><span>!</span><strong>Limits</strong><small>{{ item.limits | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></div>
      <aside class="case-evidence-row case-evidence-row--commentary"><span>NOTE</span><strong>Consultant perspective</strong><small>{{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">comment</i></aside>
      {% for source_id in item.source_ids %}
        {% for source in all_sources %}
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
      <h2>The source tells us how confidently we can read the result.</h2>
      <p>The grade does not score the company or the technology. It describes how much support the public material gives to the reported outcome. That distinction matters when we compare a measured deployment with a polished customer story that gives only a headline claim.</p>
    </header>
    <div class="case-evidence-list case-evidence-list--grades">
      {% for grade_pair in catalog.evidence_grades %}
      {% assign grade_id = grade_pair[0] %}
      {% assign grade = grade_pair[1] %}
      <div class="case-evidence-row"><span>{{ grade_id }}</span><strong>{{ grade.label }}</strong><small>{{ grade.rule }}</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></div>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
