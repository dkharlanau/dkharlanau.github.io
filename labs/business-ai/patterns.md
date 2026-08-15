---
layout: default
title: "Business AI Patterns — Business AI Lab"
description: "Reusable Business AI patterns with fit conditions, architecture shape, automation level, evaluation metrics, and public implementation examples."
permalink: /labs/business-ai/patterns/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - ai-patterns
  - enterprise-ai
  - architecture
---

{% assign catalog = site.data.labs.business_ai.catalog %}
{% assign expansion = site.data.labs.business_ai.expansion_2026_08_15 %}
{% assign expansion_b = site.data.labs.business_ai.expansion_2026_08_15_b %}
{% assign expansion_c = site.data.labs.business_ai.expansion_2026_08_15_c %}
{% assign all_patterns = catalog.patterns | concat: expansion.patterns | concat: expansion_b.patterns | concat: expansion_c.patterns %}
{% assign all_cases = catalog.cases | concat: expansion.cases | concat: expansion_b.cases %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Patterns</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / reusable patterns</p>
      <h1>Reuse the decision pattern.<br />Do not copy the demo.</h1>
      <p>A useful pattern describes the business job, minimum system shape, human boundary, failure modes, and evaluation. The vendor comes later.</p>
      <a class="research-canvas__button" href="#pattern-list">Open patterns <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Pattern set</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ all_patterns | size }}</strong><small>Patterns</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>7+</strong><small>Method families</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>1</strong><small>Rule: measure the business</small></div>
      <em>Generative AI is one method family, not the definition of Business AI.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">schema</span>
    <p><strong>Problem:</strong> product-led AI lists are hard to transfer between companies because they describe tools instead of business decisions and control boundaries.</p>
    <p><strong>Context:</strong> these patterns abstract public cases into reusable shapes that can survive a vendor, model, or platform change.</p>
    <p><strong>Pattern test:</strong> if the same business shape can be implemented with different vendors, models, or platforms, it is probably a useful pattern.</p>
    <p><strong>Anti-pattern:</strong> “Use an LLM for procurement” says almost nothing. “Compare supplier confirmations with ERP records and route only material differences to buyers” is an implementable shape.</p>
    <a href="/labs/business-ai/cases/">Compare with real cases <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="pattern-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Pattern index</p>
      <h2>{{ all_patterns | size }} working patterns.</h2>
      <p>This set grows only when a new case adds a genuinely different decision shape.</p>
    </header>
    <div class="research-route-list">
      {% for pattern in all_patterns %}
      <a href="#{{ pattern.id }}"><span>AI</span><strong>{{ pattern.title }}</strong><small>{{ pattern.business_job }} · {{ pattern.automation_level }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for pattern in all_patterns %}
  <section class="research-canvas__inventory" id="{{ pattern.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Pattern / {{ pattern.automation_level }}</p>
      <h2>{{ pattern.title }}</h2>
      <p>{{ pattern.business_job }}</p>
    </header>

    <div class="research-route-list">
      <a href="#{{ pattern.id }}"><span>FIT</span><strong>Good fit</strong><small>{{ pattern.good_fit_when | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">check_circle</i></a>
      <a href="#{{ pattern.id }}"><span>NO</span><strong>Bad fit</strong><small>{{ pattern.bad_fit_when | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">block</i></a>
      <a href="#{{ pattern.id }}"><span>SYS</span><strong>Architecture shape</strong><small>{{ pattern.architecture_shape | join: " → " }}</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="#{{ pattern.id }}"><span>KPI</span><strong>Evaluation</strong><small>{{ pattern.evaluation | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      {% for item in all_cases %}
        {% if item.pattern == pattern.id %}
        <a href="/labs/business-ai/cases/#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>{{ item.process }} · {{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">case_study</i></a>
        {% elsif item.secondary_patterns contains pattern.id %}
        <a href="/labs/business-ai/cases/#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>Secondary pattern · {{ item.process }} · {{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">case_study</i></a>
        {% endif %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Architecture rule</p><h2>Use the least magical component that works.</h2></div>
    <ol>
      <li><span>01</span><strong>Deterministic first</strong><p>Keep business rules, authorization, validation, calculations, and posting controls in deterministic systems when possible.</p></li>
      <li><span>02</span><strong>AI for uncertainty</strong><p>Use models for language, documents, prediction, classification, ranking, or uncertain decisions where rules alone are weak.</p></li>
      <li><span>03</span><strong>Measure the loop</strong><p>Evaluate the whole process: model output, integration, exception handling, human review, cost, quality, and business result.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
