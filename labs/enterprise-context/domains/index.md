---
layout: default
title: "Enterprise Business Domains — Enterprise Context Lab"
description: "A practical enterprise map that separates business ownership from processes, SAP products, data objects, decisions, scenarios, and platform capabilities."
permalink: /labs/enterprise-context/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-22
last_reviewed: 2026-09-22
hide_global_cta: true
tags:
  - sap
  - enterprise-architecture
  - business-domains
  - operating-model
  - data-management
---

{% assign topic = site.data.labs.enterprise_context.topics.business_domain_taxonomy %}
{% assign data_topic = site.data.labs.enterprise_context.topics.data_governance_landscape %}

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">Enterprise Context</a></li><li aria-current="page">Domains</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Enterprise Context Lab / Business domains</p>
      <h1>{{ topic.title }}</h1>
      <p>An enterprise map becomes confusing when it puts business ownership, SAP modules, products, data objects, and technical platforms on the same level. This page keeps those layers separate. We start with who owns a business capability, then connect the processes, data, decisions, and systems that support it.</p>
      <a class="research-canvas__button" href="#business-domains">Open the domain map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Domain model status">
      <p>Research status</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>{{ topic.business_domains | size }}</strong><small>Business domains</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>{{ topic.platform_domains | size }}</strong><small>Platform areas</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>{{ topic.maturity.gates_complete }}/{{ topic.maturity.gates_total }}</strong><small>Maturity gates</small></div>
      <em>Last reviewed together {{ topic.reviewed_together_at }}</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <div>
      <p><strong>A business domain is mainly about ownership and responsibility.</strong> It is not another name for a SAP module. Sales can remain a business domain even if the implementation moves from one application landscape to another.</p>
      <p>Cross-cutting areas such as data, integration, security, and AI are different again: they support several domains and need their own platform or governance view.</p>
    </div>
    <a href="/labs/enterprise-context/data-governance/">See the data-governance example <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="business-domains" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business ownership</p>
      <h2>Start with what the business is responsible for.</h2>
      <p>The point of a domain is to create a stable place for accountability. Processes, systems, and data structures may change more often. Master-data dependencies are shown because they explain why a defect owned elsewhere can surface inside the domain's day-to-day process.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.business_domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>BDOM</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}{% if domain.master_data_dependencies %} Master data: {{ domain.master_data_dependencies | join: ", " }}.{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Cross-cutting platform areas</p>
      <h2>Some capabilities belong across the enterprise, not inside one process silo.</h2>
      <p>Data, integration, AI, security, and transformation all cross business-domain boundaries. We therefore treat them as platform or enterprise capabilities and then decompose them into more specific solution domains and applications.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.platform_domains %}
      {% assign platform_href = "/labs/enterprise-context/data/topics.json" %}
      {% if domain.id == "BDOM-BUSINESS-AI" %}{% assign platform_href = "/labs/enterprise-context/business-ai/" %}{% endif %}
      {% if domain.id == "BDOM-DATA-ANALYTICS" %}{% assign platform_href = "/labs/enterprise-context/data-governance/" %}{% endif %}
      <a href="{{ platform_href }}"><span>AREA</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="data-drilldown" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">One example: data</p>
      <h2>From enterprise concern to product without collapsing the layers.</h2>
      <p>The data area shows why the distinction matters. Data governance is the enterprise concern; master-data governance is one domain inside it; SAP MDG is an application family that supports parts of that domain; Business Partner, material, supplier, customer, and other entities are governed business objects.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/data-governance/"><span>01</span><strong>{{ data_topic.hierarchy.area.title }}</strong><small>Cross-cutting enterprise area. {{ data_topic.hierarchy.area.role }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% for domain in data_topic.hierarchy.domains %}
      <a href="/labs/enterprise-context/data-governance/"><span>02</span><strong>{{ domain.title }}</strong><small>{{ domain.remember }} {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      {% endfor %}
      <a href="/labs/enterprise-context/mdg/"><span>03</span><strong>SAP Master Data Governance</strong><small>Application family supporting governance, consolidation, quality, mass processing, and replication capabilities for relevant master-data domains.</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% for object in data_topic.master_data_objects %}
      <a href="/labs/enterprise-context/data-governance/#objects"><span>04</span><strong>{{ object.title }}</strong><small>{{ object.business_role }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="knowledge-chain" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">From map to useful knowledge</p>
      <h2>A domain tells us where the problem belongs; the rest of the site explains what to do with it.</h2>
      <p>Once ownership is clear, a decision page can frame a design choice, a scenario can test it in an end-to-end flow, and reviewed Atlas material can provide the technical explanation or evidence. Keeping those roles distinct makes navigation and reasoning cleaner.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/domains/"><span>01</span><strong>Domain</strong><small>Business ownership or a cross-cutting platform concern.</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      <a href="/labs/enterprise-context/decisions/"><span>02</span><strong>Decision</strong><small>A design question with explicit drivers, constraints, and exceptions.</small><i class="material-symbols-outlined" aria-hidden="true">fork_right</i></a>
      <a href="/scenarios/"><span>03</span><strong>Scenario</strong><small>An end-to-end process, incident, integration flow, or transformation case where the decision has consequences.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/atlas/"><span>04</span><strong>Evidence and explanation</strong><small>Reviewed knowledge used to understand the objects, mechanisms, dependencies, and technical facts behind the scenario.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Questions for review</p>
      <h2>Three distinctions prevent most taxonomy confusion.</h2>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Is a business domain the same as a SAP module?</h3><p>No. A domain represents business responsibility. SAP modules and products are implementation choices that can support that responsibility.</p></div>
      <div><h3>Where do data and integration belong?</h3><p>They are cross-cutting enterprise capabilities because several business domains depend on them.</p></div>
      <div><h3>Why separate an application from the governed object?</h3><p>Because the same business object can exist across several systems, while the governance product is only one part of how the enterprise owns and controls that object.</p></div>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
