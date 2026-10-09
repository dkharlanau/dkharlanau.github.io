---
layout: default
btp_reader: true
hide_global_cta: true
hide_site_share: true
title: "SAP BTP & Business AI — Architect's Handbook"
description: "A practical SAP BTP and Business AI handbook: platform choices, licensing, integration, security, data, governance, diagrams, a tested local CAP policy lab and a working glossary."
permalink: /atlas/sap/sap-btp/
atlas_section: sap
domain: SAP operations
subdomain: SAP BTP and Business AI architecture
concept_type: product
sap_area: "SAP BTP"
business_process: "Enterprise and solution architecture"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-09
author: Dzmitryi Kharlanau
robots: noindex,follow
sitemap: false
tags: [sap-btp, sap-business-ai-platform, solution-architecture, integration, clean-core, cap, governance, assessment]
related:
  - /atlas/sap/sap-signavio/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/cap/
  - /atlas/sap/rap/
  - /atlas/sap/sap-datasphere/
  - /labs/assessment/
---
<link rel="stylesheet" href="{{ '/assets/page-faq.css' | relative_url }}" />
<link rel="stylesheet" href="{{ '/assets/btp-handbook.css' | relative_url }}?v={{ site.time | date: '%s' }}" />
<script src="{{ '/assets/btp-handbook.js' | relative_url }}?v={{ site.time | date: '%s' }}" defer></script>
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Learning Labs</a></li><li aria-current="page">BTP Architect's Handbook</li></ol></nav>
<article class="research-canvas signavio-reader btp-reader btp-handbook" aria-label="SAP BTP and Business AI Architect's Handbook">
<header class="research-canvas__hero signavio-reader__hero">
<div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">SAP Lead / Solution architecture</p><h1>SAP BTP &amp; Business AI</h1><p>From a business question to a design you can explain, challenge and test.</p><p class="btp-hero-note">Supplier onboarding is the running case. See how the application, identity, integrations, data and operating model fit together.</p>
<div class="btp-actions"><a href="#exam-brief">Before the exam</a><a href="#start">Start reading</a><a href="#development-lab">Open the lab</a><a href="#glossary">Find a term</a></div></div>
<aside class="research-canvas__signal" aria-label="Reading outcomes"><p>The questions to answer</p><div class="research-canvas__signal-line"><span>01</span><strong>What belongs in ERP?</strong></div><div class="research-canvas__signal-line"><span>02</span><strong>Why this service and plan?</strong></div><div class="research-canvas__signal-line"><span>03</span><strong>What proves the result?</strong></div><p class="btp-hero-note">Public documentation and original exercises. Product scope checked in October 2026; human editorial review remains pending.</p></aside>
</header>
<aside class="research-canvas__boundary" aria-label="Scope and evidence"><p><strong>The case boundary:</strong> the external specialist provides evidence; the manufacturer retains supplier-approval authority. The platform supports this process without becoming a second ERP.</p></aside>
<nav class="research-canvas__inventory signavio-reader__toc" id="reading-map" aria-label="Handbook chapters"><header><p class="research-canvas__eyebrow">Reading map</p><h2>Choose the question you need to answer.</h2><p>Read in order for the whole picture. Jump to a chapter when a case exposes a gap.</p></header><div class="signavio-reader__toc-grid"><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-0"><h3 id="handbook-route-0">Understand the platform</h3><ol><li><a href="#exam-brief">C_BAIPA: priorities and revision route</a></li><li><a href="#start">How to study this guide</a></li><li><a href="#platform-map">Platform and product map</a></li><li><a href="#architecture">Business and solution architecture</a></li><li><a href="#accounts">Accounts, services and environments</a></li></ol></section><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-1"><h3 id="handbook-route-1">Choose and connect</h3><ol><li><a href="#decision-workbench">Required components, request paths and license gates</a></li><li><a href="#commercial">Licensing, consumption and cost</a></li><li><a href="#build">Extensions, runtimes and development</a></li><li><a href="#integration">Integration patterns and components</a></li></ol></section><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-2"><h3 id="handbook-route-2">Protect and contextualize</h3><ol><li><a href="#security">Identity, access and connectivity</a></li><li><a href="#data">Data products and business meaning</a></li><li><a href="#ai">Models, grounding and agents</a></li></ol></section><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-3"><h3 id="handbook-route-3">Govern and operate</h3><ol><li><a href="#governance">Agent ownership and controls</a></li><li><a href="#operations">Delivery, monitoring and recovery</a></li><li><a href="#methods">Three SAP architecture methodologies</a></li></ol></section><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-4"><h3 id="handbook-route-4">See and do</h3><ol><li><a href="#diagrams">Six diagrams with notation keys</a></li><li><a href="#development-lab">Develop and test a supplier-review service</a></li><li><a href="#practice">Cases, design artifacts and oral practice</a></li></ol></section><section class="signavio-reader__toc-group" aria-labelledby="handbook-route-5"><h3 id="handbook-route-5">Recall and verify</h3><ol><li><a href="#glossary">126 terms, explained and contrasted</a></li><li><a href="#sources">Sources and important qualifications</a></li></ol></section></div></nav>
{% include btp-handbook/exam-brief.html %}
{% include btp-handbook/core.html %}
{% include btp-handbook/decision-workbench.html %}
{% include btp-handbook/commercial.html %}
{% include btp-handbook/build.html %}
{% include btp-handbook/integration.html %}
{% include btp-handbook/security.html %}
{% include btp-handbook/data.html %}
{% include btp-handbook/ai.html %}
{% include btp-handbook/governance.html %}
{% include btp-handbook/operations.html %}
{% include btp-handbook/methods.html %}
{% include btp-handbook/diagrams.html %}
{% include btp-handbook/lab.html %}
{% include btp-handbook/practice.html %}
{% include btp-handbook/glossary.html %}
{% include btp-handbook/sources.html %}
<section class="research-canvas__inventory signavio-reader__related" aria-labelledby="handbook-related-title"><header><h2 id="handbook-related-title">Keep the neighboring decisions in view</h2></header><p><a href="/atlas/sap/sap-signavio/">SAP Signavio</a> · <a href="/atlas/sap/sap-integration-suite/">SAP Integration Suite</a> · <a href="/atlas/sap/cap/">CAP</a> · <a href="/atlas/sap/rap/">RAP</a> · <a href="/labs/assessment/">SAP Lead assessment practice</a></p></section>
<div class="research-canvas__support">{% include atlas/author-block.html %}{% include atlas/disclaimer.html %}</div>
</article>
