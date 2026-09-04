---
author: "Dzmitryi Kharlanau"
layout: default
title: "Knowledge Atlas — SAP, Operations, Data, Automation, and AI Support Concepts"
description: "Curated Knowledge Atlas for business, SAP, operations, data, automation, and AI-assisted support concepts."
permalink: /atlas/
last_modified_at: 2026-09-05
status: reviewed
verified: true
tags:
  - sap-ams
  - diagnostics
  - ai-operations
  - data-quality
  - automation
related:
  - /atlas/concepts/order-to-cash/
  - /atlas/ai-operations/ai-agent-for-sap-support/
  - /atlas/data-quality/sap-master-data-quality/
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li aria-current="page">Knowledge Atlas</li>
  </ol>
</nav>

<section class="section atlas-hero atlas-hero--focus">
  <p class="eyebrow">Knowledge Atlas</p>
  <h1>Find the SAP context before choosing the fix.</h1>
  <p class="lead">Reviewed public pages for SAP operations, process analysis, master data, integration, and controlled automation. Start with the observable problem, then follow the related process, data, and ownership checks.</p>
  <div class="atlas-hero__actions">
    <a class="button button--primary" href="#atlas-task-paths">Start with a problem</a>
    <a class="button" href="/atlas/concepts/">Browse concepts</a>
  </div>
  <nav class="atlas-hero__route" aria-label="Atlas routes">
    <a href="/atlas/diagnostics/">Diagnostics <span aria-hidden="true">→</span></a>
    <a href="/atlas/maps/">Maps <span aria-hidden="true">→</span></a>
    <a href="/atlas/data-quality/">Data quality <span aria-hidden="true">→</span></a>
    <a href="/atlas/ai-operations/">AI operations <span aria-hidden="true">→</span></a>
  </nav>
</section>

{% include knowledge-task-paths.html scope="atlas" %}

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Sections</p>
    <h2>Curated entry points</h2>
    <p class="lead">Each section is designed as an editorial surface, not a dump of draft notes. Pages are added only after they are useful, conservative, and safe to expose publicly.</p>
  </header>

  <div class="atlas-card-grid">
    <a class="atlas-card" href="/atlas/concepts/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">lightbulb</span>
      <h2>Concepts</h2>
      <p>Business and SAP concepts explained from the operational problem outward.</p>
      <span class="link-arrow">Open concepts</span>
    </a>
    <a class="atlas-card" href="/atlas/maps/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">account_tree</span>
      <h2>Maps</h2>
      <p>Process, document-flow, data dependency, and cross-domain navigation maps.</p>
      <span class="link-arrow">Open maps</span>
    </a>
    <a class="atlas-card" href="/atlas/sap/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">settings</span>
      <h2>SAP Notes</h2>
      <p>Curated SAP configuration and support explanations with conservative boundaries.</p>
      <span class="link-arrow">Open SAP section</span>
    </a>
    <a class="atlas-card" href="/atlas/diagnostics/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">troubleshoot</span>
      <h2>Diagnostics</h2>
      <p>Support-oriented diagnostic patterns for repeat incidents and process blockers.</p>
      <span class="link-arrow">Open diagnostics</span>
    </a>
    <a class="atlas-card" href="/scenarios/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">conversion_path</span>
      <h2>Scenarios</h2>
      <p>Business pain mapped to SAP process context, cost drivers, and diagnostic workflows.</p>
      <span class="link-arrow">Open scenarios</span>
    </a>
    <a class="atlas-card" href="/atlas/ai-operations/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">psychology</span>
      <h2>AI Operations</h2>
      <p>AI-assisted support, operational memory, governance, and human review patterns.</p>
      <span class="link-arrow">Open AI operations</span>
    </a>
    <a class="atlas-card" href="/atlas/ai-tools/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">terminal</span>
      <h2>AI Tools</h2>
      <p>Repository context packaging, coding agents, MCP, AI code review, testing, and security.</p>
      <span class="link-arrow">Open AI tools</span>
    </a>
    <a class="atlas-card" href="/atlas/data-quality/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">database</span>
      <h2>Data Quality</h2>
      <p>Master data, quality signals, governance failure modes, and operational data problems.</p>
      <span class="link-arrow">Open data quality</span>
    </a>
    <a class="atlas-card" href="/atlas/automation/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">precision_manufacturing</span>
      <h2>Automation</h2>
      <p>Support automation, operational memory, agentic workflows, and developer automation patterns.</p>
      <span class="link-arrow">Open automation</span>
    </a>
    <a class="atlas-card" href="/atlas/research-notes/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">science</span>
      <h2>Research Notes</h2>
      <p>Noindex working area for material that is useful but not ready to be treated as polished expert content.</p>
      <span class="link-arrow">Open research notes</span>
    </a>
    <a class="atlas-card" href="/atlas/links/">
      <span class="atlas-card__icon material-symbols-outlined" aria-hidden="true">link</span>
      <h2>Links</h2>
      <p>Reference routes to profile, services, datasets, and future curated sources.</p>
      <span class="link-arrow">Open links</span>
    </a>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Pilot Pages</p>
    <h2>Selected starting pages</h2>
    <p>Review status belongs to each page. Working diagnostics still need human review in the relevant SAP context.</p>
  </header>
  <div class="atlas-card-grid">
    {% assign pilot_urls = site.data.knowledge_paths.atlas_pilots %}
    {% assign pilot_pages = site.pages | where_exp: 'candidate', 'pilot_urls contains candidate.permalink' %}
    {% for pilot_url in pilot_urls %}
    {% assign pilot_page = pilot_pages | where: 'permalink', pilot_url | first %}
    <a class="atlas-card" href="{{ pilot_url }}">
      <h3>{{ pilot_page.short_title | default: pilot_page.title | escape }}</h3>
      <p>{{ pilot_page.description | escape }}</p>
      <span class="atlas-pill">{% if pilot_page.verified == true and pilot_page.status == 'reviewed' %}{% if pilot_page.robots contains 'noindex' %}Working · review pending{% else %}Reviewed{% endif %}{% else %}Working · review pending{% endif %}</span>
      <span class="link-arrow">Read page</span>
    </a>
    {% endfor %}
  </div>
</section>

<section class="section">
  <div class="section-shell section-shell--flat">
    <header class="section-heading">
      <p class="eyebrow">Context</p>
      <h2>How this Atlas should be read</h2>
    </header>
    <p class="lead">The Atlas is not official SAP documentation and it is not a replacement for system-specific analysis. It is a structured way to capture practical concepts, diagnostic questions, and operating patterns that help teams reason about SAP-heavy environments.</p>
    <div class="section-actions">
      <a class="button" href="/about/">Author profile</a>
      <a class="button" href="/services/sap-ams-consulting/">SAP AMS consulting</a>
      <a class="button" href="/services/sap-ai-ml-enablement/">SAP AI enablement</a>
      <a class="button" href="/ai/practical-ai-for-sap-support/">Practical AI for SAP support</a>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Related</p>
    <h2>Related Atlas pages</h2>
  </header>
  <ul>
    <li><a href="/atlas/concepts/order-to-cash/">Order to Cash concept</a></li>
    <li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI agent for SAP support</a></li>
    <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP master data quality</a></li>
    <li><a href="/atlas/concepts/sap-ams-cost-reduction-framework/">SAP AMS Cost Reduction Framework</a></li>
  </ul>
</section>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
