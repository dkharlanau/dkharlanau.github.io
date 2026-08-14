---
layout: default
title: "Enterprise Business Domains — Enterprise Context Lab"
description: "A simple enterprise map that separates business ownership from processes, SAP products, and platform capabilities."
permalink: /labs/enterprise-context/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-14
hide_global_cta: true
---

{% assign topic = site.data.labs.enterprise_context.topics.business_domain_taxonomy %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Domains</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Business domains</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#business-domains">Open the domain map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Domain model status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.business_domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.platform_domains | size }}</strong><small>Platform domains</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Remember:</strong> business domain = ownership. Process = work. Solution domain = function. Application = technology.</p>
    <a href="/labs/enterprise-context/deployment-models/">Compare S/4HANA deployment models <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="business-domains" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business domains</p>
      <h2>What does the business own?</h2>
      <p>The domain stays stable even when the SAP landscape changes.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.business_domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>BDOM</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Platform domains</p>
      <h2>Capabilities used across the business.</h2>
      <p>Data, integration, AI, security, and transformation support many domains.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.platform_domains %}
      <a href="{% if domain.id == 'BDOM-BUSINESS-AI' %}/labs/enterprise-context/business-ai/{% else %}/labs/enterprise-context/data/topics.json{% endif %}"><span>BDOM</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How to answer</p>
      <h2>Ownership → process → system.</h2>
      <p>Keep these three levels separate in an architecture discussion.</p>
    </header>
    <div class="research-route-list">
      {% for item in topic.decision_guide %}
      <a href="/labs/enterprise-context/model/"><span>→</span><strong>{{ item.question }}</strong><small>{{ item.guidance }}</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      {% endfor %}
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
