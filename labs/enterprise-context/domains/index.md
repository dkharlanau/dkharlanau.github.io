---
layout: default
title: "Enterprise Business Domain Taxonomy — Enterprise Context Lab"
description: "A stable enterprise business-domain model that separates business ownership from SAP products, modules, processes, and cross-cutting platform capabilities."
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
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Domain model</p>
      <h1>{{ topic.title }}</h1>
      <p>{{ topic.summary }}</p>
      <a class="research-canvas__button" href="#business-domains">Explore the taxonomy <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Domain model status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.business_domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.platform_domains | size }}</strong><small>Cross-cutting domains</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Modeling boundary.</strong> A business domain is an enduring area of business responsibility. SAP products, classic module names, application capabilities, and end-to-end process families are mapped to domains rather than used as the domain taxonomy itself.</p>
    <a href="/labs/enterprise-context/business-ai/">Open the Business AI landscape <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Modeling rules</p>
      <h2>Keep ownership, process, and technology as different axes.</h2>
      <p>The distinction matters because a process can cross several domains and one SAP product can support several domains.</p>
    </header>
    <div class="research-route-list">
      {% for rule in topic.modeling_rules %}
      <a href="/labs/enterprise-context/model/"><span>RULE</span><strong>Domain modeling rule</strong><small>{{ rule }}</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="business-domains" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business ownership domains</p>
      <h2>Stable responsibilities before SAP product names.</h2>
      <p>These domains describe what the enterprise owns and operates. They should remain useful even when the application portfolio changes.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.business_domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>BDOM</span><strong>{{ domain.title }}</strong><small>{{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-cutting platform domains</p>
      <h2>Capabilities that support several business domains.</h2>
      <p>Data, integration, AI, security, and transformation do not belong to one operational process. They provide reusable capabilities across the enterprise.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.platform_domains %}
      <a href="{% if domain.id == 'BDOM-BUSINESS-AI' %}/labs/enterprise-context/business-ai/{% else %}/labs/enterprise-context/data/topics.json{% endif %}"><span>BDOM</span><strong>{{ domain.title }}</strong><small>{{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How to use the taxonomy</p>
      <h2>Move from business ownership to process to system responsibility.</h2>
      <p>A Lead-level architecture discussion should be able to explain all three without collapsing them into one label.</p>
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
