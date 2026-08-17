---
layout: default
title: "Enterprise Business Domains — Enterprise Context Lab"
description: "A simple enterprise map that separates business ownership from processes, SAP products, data objects, decisions, scenarios, and platform capabilities."
permalink: /labs/enterprise-context/domains/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-17
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
      <p>{{ topic.summary }}</p>
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
    <p><strong>Problem:</strong> business domains, data domains, processes, SAP modules, and products are often mixed into one map.</p>
    <p><strong>Remember:</strong> business domain = ownership. Platform area = cross-cutting concern. Solution domain = function. Application = technology. Master-data object = shared business entity.</p>
    <a href="/labs/enterprise-context/data-governance/">Open Data, Master Data and Governance <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="business-domains" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business domains</p>
      <h2>What does the business own?</h2>
      <p>The domain stays stable even when the SAP landscape changes. The master-data dependencies show where a cross-cutting data problem can surface as a business-process problem.</p>
    </header>
    <div class="research-route-list">
      {% for domain in topic.business_domains %}
      <a href="/labs/enterprise-context/data/topics.json"><span>BDOM</span><strong>{{ domain.title }}</strong><small><b>{{ domain.remember }}</b> {{ domain.purpose }}{% if domain.master_data_dependencies %} Master data: {{ domain.master_data_dependencies | join: ", " }}.{% endif %}</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Platform areas</p>
      <h2>Capabilities used across the business.</h2>
      <p>Data, integration, AI, security, and transformation cross business-domain boundaries. Each area should then be decomposed into solution domains and concrete applications.</p>
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
      <p class="research-canvas__eyebrow">Data area drill-down</p>
      <h2>Area → domain → application → object.</h2>
      <p>MDG now sits inside the Enterprise Context graph rather than next to it. This keeps the product, governance problem, and governed business object separate.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/data-governance/"><span>01</span><strong>{{ data_topic.hierarchy.area.title }}</strong><small>Cross-cutting enterprise area. {{ data_topic.hierarchy.area.role }}</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      {% for domain in data_topic.hierarchy.domains %}
      <a href="/labs/enterprise-context/data-governance/"><span>02</span><strong>{{ domain.title }}</strong><small>{{ domain.remember }} {{ domain.purpose }}</small><i class="material-symbols-outlined" aria-hidden="true">category</i></a>
      {% endfor %}
      <a href="/labs/enterprise-context/mdg/"><span>03</span><strong>SAP Master Data Governance</strong><small>Application family implementing governance, consolidation, quality, mass processing, and replication capabilities within the relevant data domains.</small><i class="material-symbols-outlined" aria-hidden="true">deployed_code</i></a>
      {% for object in data_topic.master_data_objects %}
      <a href="/labs/enterprise-context/data-governance/#objects"><span>04</span><strong>{{ object.title }}</strong><small>{{ object.business_role }}</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      {% endfor %}
    </div>
  </section>

  <section class="research-canvas__inventory" id="knowledge-chain" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Knowledge chain</p>
      <h2>Domain → decision → scenario → evidence.</h2>
      <p>A domain tells us who owns the problem. A decision explains the choice. A scenario tests the choice in a real flow. Evidence shows why the answer is credible. Keeping these levels connected makes the site easier to use for assessment preparation, architecture work, search, and AI retrieval.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/domains/"><span>01</span><strong>Domain</strong><small>Start with business ownership or a cross-cutting platform concern. Do not start with the SAP product name.</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      <a href="/labs/enterprise-context/decisions/"><span>02</span><strong>Decision</strong><small>State the design question, decision drivers, default answer, exceptions, and failure owner.</small><i class="material-symbols-outlined" aria-hidden="true">fork_right</i></a>
      <a href="/scenarios/"><span>03</span><strong>Scenario</strong><small>Apply the decision to an end-to-end process, incident, integration flow, or transformation case.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="/atlas/"><span>04</span><strong>Evidence</strong><small>Use reviewed Atlas pages, field notes, datasets, publications, and verified professional evidence for factual support.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How to answer</p>
      <h2>Ownership → process → data → system.</h2>
      <p>Keep these levels separate in an architecture discussion. It makes the explanation shorter and the design more precise.</p>
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
