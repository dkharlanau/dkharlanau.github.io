---
layout: default
title: "Business AI by Enterprise Domain — Business AI Lab"
description: "An enterprise-wide map of Business AI jobs, system touchpoints, technology families, architecture questions, and implementation cases."
permalink: /labs/business-ai/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
last_reviewed: 2026-09-22
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
      <h1>Start with the work.<br />Then place AI inside it.</h1>
      <p>Sales, procurement, planning, logistics, manufacturing, finance, HR, service, IT, legal, data, and knowledge work do not need AI for the same reason. We use the domain view to keep the business job, system context, and ownership visible before choosing a model, agent, or platform.</p>
      <a class="research-canvas__button" href="#domain-list">Open the domain map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Enterprise view</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ domain_map.domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ all_cases | size }}</strong><small>Evidence cases</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>5</strong><small>Questions per domain</small></div>
      <em>SAP may be central to the landscape, but the business domain is wider than one application.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <div>
      <p><strong>A domain gives us the business context in which an AI idea has to survive.</strong> The same technical capability can be useful in one process and inappropriate in another because the data, authority, timing, and consequence of an error are different.</p>
      <p>That is why the map keeps process ownership, enterprise systems, data, decisions, and controls next to the AI opportunity. Exact calculations, authorizations, accounting controls, master identity, and safety constraints still belong to the systems and rules that are designed to own them.</p>
    </div>
    <a href="/labs/business-ai/technologies/">Open the technology landscape <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="domain-list" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Domain index</p>
      <h2>{{ domain_map.domains | size }} views of enterprise work.</h2>
      <p>Across all of them we ask the same basic question: what job is being done, which data and systems carry the business truth, where judgment or uncertainty appears, and what evidence would show that an AI-assisted version is actually better.</p>
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
      <a href="#{{ domain.id }}"><span>?</span><strong>Question {{ forloop.index }}</strong><small>{{ question }}</small><i class="material-symbols-outlined" aria-hidden="true">help</i></a>
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
      <a href="#{{ domain.id }}"><span>GAP</span><strong>Evidence gap</strong><small>No case is linked yet. We keep the domain in the model so the research gap remains visible instead of disappearing from the map.</small><i class="material-symbols-outlined" aria-hidden="true">search</i></a>
      {% endif %}
    </div>
  </section>
  {% endfor %}

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">How to read the map</p><h2>Move from business context toward technology, not the other way around.</h2></div>
    <ol>
      <li><span>01</span><strong>Understand the business job</strong><p>Start with the process outcome and the information people or systems need to reach it.</p></li>
      <li><span>02</span><strong>Locate the business truth</strong><p>Identify the systems, data owners, rules, and approval boundaries that already decide what is valid.</p></li>
      <li><span>03</span><strong>Place AI in the uncertain part</strong><p>Extraction, retrieval, prediction, optimization, or agentic orchestration only make sense where they solve a real gap without replacing controls that should stay deterministic.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
