---
layout: default
title: "Labs — Enterprise Context and AI"
description: "Practical maps for SAP domains, deployment models, industries, processes, applications, integrations, data, Business AI, and AI architecture."
permalink: /labs/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - sap
  - enterprise-architecture
  - research
  - business-ai
---

{% assign business_ai_catalog = site.data.labs.business_ai.catalog %}
{% assign business_ai_expansion = site.data.labs.business_ai.expansion_2026_08_15 %}
{% assign business_ai_expansion_b = site.data.labs.business_ai.expansion_2026_08_15_b %}
{% assign business_ai_domain_map = site.data.labs.business_ai.domain_map %}
{% assign business_ai_cases = business_ai_catalog.cases | concat: business_ai_expansion.cases | concat: business_ai_expansion_b.cases %}
{% assign business_ai_patterns = business_ai_catalog.patterns | concat: business_ai_expansion.patterns | concat: business_ai_expansion_b.patterns %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li aria-current="page">Labs</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Labs / practical architecture maps</p>
      <h1>Understand the business.<br />Then map the architecture.</h1>
      <p>Simple, source-tracked maps of business domains, SAP landscapes, integrations, data, AI systems, implementation cases, and the decisions that connect them.</p>
      <a class="research-canvas__button" href="#labs-inventory">Open the labs <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Current labs">
      <p>Current inventory</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>3</strong><small>Active labs</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>19+</strong><small>Architecture and case views</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>8+</strong><small>Machine endpoints</small></div>
      <em>Working material is public but remains noindex until reviewed.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Lab boundary">
    <span class="material-symbols-outlined" aria-hidden="true">science</span>
    <p><strong>Problem:</strong> product-first learning makes it hard to connect business ownership, process, architecture, evidence, and operational controls.</p>
    <p><strong>Working rule.</strong> Facts, expert judgment, synthetic examples, and fast-moving technology notes stay separate.</p>
    <a href="/research/">Open Research <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <p><strong>Publication rule.</strong> Vendor and primary sources verify facts; explanations stay independently written. See the <a href="/legal/research-attribution/">Research and Attribution Policy</a>.</p>

  <section class="research-canvas__inventory" id="labs-inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lab 01 / Enterprise Context</p>
      <h2>Business first, system second.</h2>
      <p>Move from business ownership and industry context to deployment model, process, SAP component, integration, data, and AI responsibility.</p>
    </header>

    <div class="research-route-list">
      <a href="/labs/enterprise-context/"><span>01</span><strong>Enterprise Context Graph</strong><small>Sales, Supply Chain, processes, applications, boundaries, licensing, and sources.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/domains/"><span>02</span><strong>Enterprise Business Domains</strong><small>What the business owns, separate from processes and SAP products.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/enterprise-context/deployment-models/"><span>03</span><strong>SAP S/4HANA Deployment Models</strong><small>Public Cloud, Private Cloud, and On-Premise.</small><i class="material-symbols-outlined" aria-hidden="true">cloud</i></a>
      <a href="/labs/enterprise-context/industries/"><span>04</span><strong>SAP Industry Solutions</strong><small>Automotive, retail, fashion, industrial manufacturing, and mill products.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="/labs/enterprise-context/business-ai/"><span>05</span><strong>SAP Business AI Technology Landscape</strong><small>Joule, agents, build tools, runtime, model access, grounding, and governance. Use the separate Business AI Lab for implementation cases and reusable patterns.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/labs/enterprise-context/integrations/"><span>06</span><strong>SAP Integration Architecture</strong><small>APIs, IDocs, RFC, events, Kafka, queues, files, B2B, middleware, logistics, and master-data distribution.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="/labs/enterprise-context/model/"><span>07</span><strong>Model and authoring rules</strong><small>IDs, node types, relationships, evidence, dates, and maturity gates.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/data/catalog.json"><span>08</span><strong>Machine-readable catalog</strong><small>JSON for tools, AI experiments, and structured analysis.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lab 02 / AI Ready</p>
      <h2>Build AI systems, not isolated demos.</h2>
      <p>A vendor-neutral architecture map for data, retrieval, tools, MCP, agents, evaluations, security, deployment, and production decisions.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/ai-ready/"><span>AI</span><strong>AI Ready Architecture Lab</strong><small>Foundations, RAG, MCP, agents, evals, security, deployment, decision matrix, and hands-on track.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
      <a href="/labs/ai-ready/data/catalog.json"><span>JSON</span><strong>AI architecture catalog</strong><small>Dated tracks, decision rules, production rules, labs, and primary-source registry.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/ai-ready/data/eval-sample.jsonl"><span>EVAL</span><strong>Sample eval dataset</strong><small>Architecture cases with expected patterns, controls, and failure signals.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Lab 03 / Business AI</p>
      <h2>Start from the business job. Keep the evidence attached.</h2>
      <p>A growing catalog of public implementation evidence across Sales, O2C, Procurement, Supply Chain Planning, Manufacturing, Service, Knowledge Work, Logistics, and Master Data.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/"><span>AI</span><strong>Business AI Lab</strong><small>Business-first map of patterns, cases, evidence grades, technologies, metrics, limits, and cross-links to SAP and vendor-neutral architecture.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/labs/business-ai/domains/"><span>DOM</span><strong>Business AI by Domain</strong><small>{{ business_ai_domain_map.domains | size }} Lead-level domain views with business jobs, SAP touchpoints, architecture questions, and linked implementation cases.</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      <a href="/labs/business-ai/cases/"><span>CASE</span><strong>Implementation cases</strong><small>{{ business_ai_cases | size }} working cases across customer service, sales, O2C, procurement, demand planning, manufacturing, logistics, knowledge work, and master-data foundations.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="/labs/business-ai/patterns/"><span>PAT</span><strong>Reusable patterns</strong><small>{{ business_ai_patterns | size }} working patterns including conversation automation, document-to-workflow, forecasting, guided selling, cross-system copilots, optimization, embodied logistics, manufacturing quality, and trusted master data.</small><i class="material-symbols-outlined" aria-hidden="true">account_tree</i></a>
      <a href="/labs/business-ai/model/"><span>GRAPH</span><strong>Graph model</strong><small>Node and edge types for companies, cases, domains, processes, patterns, technologies, metrics, evidence sources, limitations, and case kinds.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/business-ai/data/catalog.json"><span>JSON</span><strong>Business AI catalog</strong><small>Machine-readable cases, patterns, source registry, evidence model, technologies, KPIs, limitations, consultant notes, and case classification.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
      <a href="/labs/business-ai/data/domains.json"><span>MAP</span><strong>Business AI domain data</strong><small>Machine-readable business jobs, SAP touchpoints, Lead questions, and case IDs by domain.</small><i class="material-symbols-outlined" aria-hidden="true">data_object</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Method</p><h2>Model, connect, exercise.</h2></div>
    <ol>
      <li><span>01</span><strong>Model</strong><p>Define the problem, owners, data, rules, systems, and boundaries.</p></li>
      <li><span>02</span><strong>Connect</strong><p>Link integrations, tools, failures, controls, tests, evidence, and related implementation cases.</p></li>
      <li><span>03</span><strong>Exercise</strong><p>Use synthetic cases, build small systems, and test the reasoning.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>