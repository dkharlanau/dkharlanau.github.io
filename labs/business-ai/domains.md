---
layout: default
title: "Business AI by Enterprise Domain — Business AI Lab"
description: "An enterprise-wide map of Business AI jobs, system touchpoints, technology families, architecture questions, and implementation cases."
permalink: /labs/business-ai/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - enterprise-ai
  - assessment
  - processes
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
      <p class="research-canvas__eyebrow">Business AI / enterprise domain view</p>
      <h1>Map the process first.<br />Then choose the technology.</h1>
      <p>Business AI crosses the whole company: sales, procurement, planning, logistics, manufacturing, finance, HR, service, IT, legal, data, and knowledge work. Each domain starts from a business job and control boundary, not from one vendor platform.</p>
      <a class="research-canvas__button" href="#domain-list">Open the domain map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Enterprise view</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ domain_map.domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ all_cases | size }}</strong><small>Evidence cases</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>5</strong><small>Control questions per domain</small></div>
      <em>SAP is one important system landscape. It is not the definition of Business AI.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Context:</strong> this view supports enterprise architecture and Lead assessment. It connects business jobs to system touchpoints, AI technology families, control questions, and evidence-backed cases.</p>
    <p><strong>Lead rule:</strong> start with process ownership, data, system of record, decision rights, and KPI. AI enters only where uncertainty, documents, language, prediction, ranking, optimization, or adaptive orchestration create a real gap.</p>
    <p><strong>Control rule.</strong> Keep authorization, exact calculations, hard constraints, accounting controls, master identity, and physical safety outside free-form model behavior.</p>
    <a href="/labs/business-ai/technologies/">Open the technology landscape <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="domain-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Domain index</p>
      <h2>{{ domain_map.domains | size }} enterprise domains.</h2>
      <p>The method stays stable across domains: business job → data and systems → decision → action → controls → evidence.</p>
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
      <a href="#{{ domain.id }}"><span>SYS</span><strong>Enterprise system touchpoints</strong><small>{{ domain.system_touchpoints | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/business-ai/technologies/"><span>TECH</span><strong>Useful technology families</strong><small>{{ domain.technology_families | join: " · " }}</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      {% for question in domain.lead_questions %}
      <a href="#{{ domain.id }}"><span>?</span><strong>Architecture question {{ forloop.index }}</strong><small>{{ question }}</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
      {% endfor %}
      {% if domain.case_ids.size > 0 %}
        {% for case_id in domain.case_ids %}
          {% for item in all_cases %}
            {% if item.id == case_id %}
            <a href="/labs/business-ai/cases/#{{ item.id }}"><span>{{ item.evidence_grade }}</span><strong>{{ item.company }} · {{ item.title }}</strong><small>{{ item.process }} · {{ item.consultant_note }}</small><i class="material-symbols-outlined" aria-hidden="true">case_study</i></a>
            {% endif %}
          {% endfor %}
        {% endfor %}
      {% else %}
      <a href="#{{ domain.id }}"><span>GAP</span><strong>Evidence gap</strong><small>No case is linked yet. The domain stays in the model so research gaps remain visible instead of disappearing from the map.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      {% endif %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Assessment answer shape</p><h2>Answer from business control to technology.</h2></div>
    <ol>
      <li><span>01</span><strong>Business outcome</strong><p>Name the process problem and KPI before naming a model or platform.</p></li>
      <li><span>02</span><strong>Ownership and boundary</strong><p>Explain the system of record, data ownership, deterministic rules, authorization, human approval, and failure path.</p></li>
      <li><span>03</span><strong>Technology choice</strong><p>Choose extraction, retrieval, prediction, optimization, workflow, agents, RPA, or no AI based on the actual uncertain part of the job.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
