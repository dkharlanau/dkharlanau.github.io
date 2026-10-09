---
layout: default
btp_reader: true
hide_global_cta: true
hide_site_share: true
title: "SAP BTP — Decisions, Services and Working Architectures"
description: "16 decision trees for SAP BTP: Cloud Foundry vs Kyma, CAP/RAP, mobile SDKs and offline, 94 service-map entries, minimum solution stacks, contract gates and eight practical pilots."
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
author: BTP Architecture Lab
robots: noindex,follow
sitemap: false
tags: [sap-btp, solution-architecture, kyma, cloud-foundry, mobile, offline, integration, clean-core, cap, governance]
related:
  - /atlas/sap/sap-signavio/
  - /atlas/sap/sap-integration-suite/
  - /atlas/sap/cap/
  - /atlas/sap/rap/
  - /atlas/sap/sap-datasphere/
  - /labs/assessment/
---
<link rel="stylesheet" href="{{ '/assets/page-faq.css' | relative_url }}" />
<link rel="stylesheet" href="{{ '/assets/btp-handbook.css' | relative_url }}?v=20261009" />
<script src="{{ '/assets/btp-handbook.js' | relative_url }}?v=20261009" defer></script>
<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/labs/">Learning Labs</a></li><li aria-current="page">BTP Architecture</li></ol></nav>
<article class="research-canvas signavio-reader btp-reader btp-handbook btp-decisions" aria-label="SAP BTP decisions and working architectures">
<header class="research-canvas__hero signavio-reader__hero">
<div class="research-canvas__hero-copy"><p class="research-canvas__eyebrow">SAP BTP / Practical architecture</p><h1>Choose the right service.<br />Know how it works.</h1><p>From a business requirement to a small, defensible architecture: decisions, dependencies, configuration and failure tests.</p><div class="btp-actions"><a href="#runtime-tree">Cloud Foundry or Kyma?</a><a href="#mobile">Mobile and offline</a><a href="#service-map">Explore 94 entries</a><a href="#practice">Build a pilot</a></div></div>
<aside class="research-canvas__signal" aria-label="Guide contents"><p>The working map</p><div class="research-canvas__signal-line"><span>16</span><strong>Decision trees</strong></div><div class="research-canvas__signal-line"><span>94</span><strong>Service-map entries</strong></div><div class="research-canvas__signal-line"><span>06</span><strong>Minimum compositions</strong></div><div class="research-canvas__signal-line"><span>08</span><strong>Practical pilots</strong></div></aside>
</header>
<nav class="research-canvas__inventory signavio-reader__toc" id="reading-map" aria-label="Architecture questions"><header><p class="research-canvas__eyebrow">Reading routes</p><h2>Open the decision you cannot yet explain.</h2></header><div class="signavio-reader__toc-grid">
<section class="signavio-reader__toc-group"><h3>Choose</h3><ol><li><a href="#start">Separate the platform layers</a></li><li><a href="#architecture">Standard, in-app or side-by-side</a></li><li><a href="#build">CF, Kyma, ABAP and CAP/RAP</a></li><li><a href="#experience">Web UI and application entry</a></li></ol></section>
<section class="signavio-reader__toc-group"><h3>Connect and protect</h3><ol><li><a href="#integration">Direct API, iFlow or events</a></li><li><a href="#security">Network, identity and authorisation</a></li><li><a href="#data">Persistence and data products</a></li><li><a href="#ai">AI, workflow and agent boundaries</a></li></ol></section>
<section class="signavio-reader__toc-group"><h3>Go deeper</h3><ol><li><a href="#accounts">Landscape and tenant isolation</a></li><li><a href="#mobile">MDK, native SDKs and offline</a></li><li><a href="#service-map">Search the service map</a></li><li><a href="#recipes">Required, conditional and optional</a></li></ol></section>
<section class="signavio-reader__toc-group"><h3>Deliver</h3><ol><li><a href="#operations">Delivery, recovery and acceptance</a></li><li><a href="#commercial">Contract, entitlement and cost</a></li><li><a href="#practice">Eight pilot projects</a></li><li><a href="#methods">Architecture pack and practice</a></li></ol></section>
<section class="signavio-reader__toc-group"><h3>Look up</h3><ol><li><a href="#glossary">140 terms, explained and contrasted</a></li><li><a href="#sources">Product and API references</a></li><li><a href="#contract-exercise">Local recovery exercise</a></li></ol></section>
</div></nav>
{% include btp-handbook/decisions.html %}
{% include btp-handbook/mobile-decisions.html %}
{% include btp-handbook/service-map.html %}
{% include btp-handbook/delivery-decisions.html %}
<details class="page-faq__item btp-reference-drawer" id="glossary-drawer"><summary>Terminology reference — 140 terms</summary>
{% include btp-handbook/glossary.html %}
</details>
{% include btp-handbook/decision-references.html %}
<section class="research-canvas__inventory signavio-reader__related" aria-labelledby="related-title"><header><h2 id="related-title">Related implementation topics</h2></header><p><a href="/atlas/sap/sap-integration-suite/">Integration Suite</a> · <a href="/atlas/sap/cap/">CAP</a> · <a href="/atlas/sap/rap/">RAP</a> · <a href="/atlas/sap/sap-datasphere/">Datasphere</a> · <a href="/labs/assessment/">Architecture practice</a></p></section>
</article>
