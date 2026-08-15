---
layout: default
title: "Business AI by Domain — Business AI Lab"
description: "A Lead-level map of Business AI opportunities, SAP touchpoints, architecture questions, and public cases across logistics and enterprise domains."
permalink: /labs/business-ai/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - sap
  - assessment
  - logistics
  - architecture
---

{% assign catalog = site.data.labs.business_ai.catalog %}
{% assign expansion = site.data.labs.business_ai.expansion_2026_08_15 %}
{% assign expansion_b = site.data.labs.business_ai.expansion_2026_08_15_b %}
{% assign domain_map = site.data.labs.business_ai.domain_map %}
{% assign all_cases = catalog.cases | concat: expansion.cases | concat: expansion_b.cases %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Domains</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / domain view</p>
      <h1>Do not ask where AI fits.<br />Ask which decision should improve.</h1>
      <p>This view connects Business AI to the SAP domains used in real logistics work. Each domain starts from a business job, then shows SAP touchpoints, Lead-level architecture questions, and cases with public evidence.</p>
      <a class="research-canvas__button" href="#domain-list">Open the domain map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Assessment view</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ domain_map.domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ all_cases | size }}</strong><small>Cases available</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>5</strong><small>Questions before technology</small></div>
      <em>The point is architecture judgment, not remembering a catalog of model names.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Context:</strong> this domain view is designed for SAP Lead assessment: business jobs, SAP touchpoints, control questions, and evidence-backed cases stay together.</p>
    <p><strong>Lead rule:</strong> start with process ownership, data, system of record, decision rights, and KPI. AI enters only where uncertainty, documents, language, prediction, ranking, or optimization create a real gap.</p>
    <p><strong>Control rule.</strong> Keep authorization, posting rules, hard constraints, financial controls, and physical safety outside free-form model behavior.</p>
    <a href="/labs/business-ai/model/">Open the graph model <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="domain-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Domain index</p>
      <h2>Seven views of the same architecture problem.</h2>
      <p>The useful question changes by domain, but the method stays stable: business job → data → decision → action → evidence.</p>
    </header>
    <div class="research-route-list">
      {% for domain in domain_map.domains %}
      <a href="#{{ domain.id }}"><span>{{ domain.case_ids | size }}</span><strong>{{ domain.title }}</strong><small>{{ domain.business_jobs | first }}</small><i class="material-symbols-outlined" aria-hidden="true">arrow_downward</i></a>
      {% endfor %}
    </div>
  </section>

  {% for domain in domain_map.domains %}
  <section class="research-canvas__inventory" id="{{ domain.id }}" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Domain / {{ domain.id }}</p>
      <h2>{{ domain.title }}</h2>
      <p>{{ domain.business_jobs | join: " · " }}</p>
    </header>
    <div class="research-route-list">
      <a href="#{{ domain.id }}"><span>SAP</span><strong>SAP touchpoints</strong><small>{{ domain.sap_touchpoints | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% for question in domain.lead_questions %}
      <a href="#{{ domain.id }}"><span>?</span><strong>Lead question {{ forloop.index }}</strong><small>{{ question }}</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      {% endfor %}
      {% for case_id in domain.case_ids %}
        {% for item in all_cases %}
          {% if item.id == case_id %}
          <a href="/labs/business-ai/cases/#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>{{ item.process }} · {{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">case_study</i></a>
          {% endif %}
        {% endfor %}
      {% endfor %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Assessment answer shape</p><h2>Answer from control to technology.</h2></div>
    <ol>
      <li><span>01</span><strong>Business outcome</strong><p>Name the process problem and KPI before naming an AI product.</p></li>
      <li><span>02</span><strong>Ownership and boundary</strong><p>Explain the system of record, data ownership, hard rules, authorization, human approval, and failure path.</p></li>
      <li><span>03</span><strong>AI choice</strong><p>Choose extraction, retrieval, prediction, optimization, recommendation, agentic orchestration, or no AI based on the uncertain part of the job.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
