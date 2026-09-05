---
layout: default
title: "Experience Platforms — Enterprise Context Lab"
description: "Learn enterprise experience platforms: central entry points, digital workplaces, task access, mobile entry, and SAP Build Work Zone."
permalink: /labs/enterprise-context/experience-platforms/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-03
last_reviewed: 2026-09-03
publication_wave: "sap-experience-review-2026-09"
review_method: "current SAP Build Work Zone and SAP Task Center primary sources + architecture-boundary review"
search_intent: "SAP enterprise experience platform Work Zone Fiori launchpad SAP Start Task Center digital workplace"
structured_data:
  type: TechArticle
primary_topic: "sap-enterprise-experience-platforms"
hide_global_cta: true
career_impact: mapped
career_skills:
  - integration-patterns
  - integration-ownership
tags:
  - sap-btp
  - enterprise-experience
  - digital-workplace
  - fiori
  - integration-architecture
source_links:
  - title: "SAP Build Work Zone, standard edition"
    url: "https://help.sap.com/docs/build-work-zone-standard-edition/sap-build-work-zone-standard-edition"
  - title: "SAP Build Work Zone, advanced edition"
    url: "https://help.sap.com/docs/build-work-zone-advanced-edition/sap-build-work-zone-advanced-edition"
  - title: "SAP Task Center"
    url: "https://help.sap.com/docs/task-center/sap-task-center"
# ai-discovery-managed:start
primary_topic: "sap-enterprise-experience-platforms"
ai_sidecar: "/ai/pages/labs--enterprise-context--experience-platforms.json"
semantic_links:
  - type: "deep_dive"
    title: "SAP Build Work Zone — Enterprise Context Lab"
    url: "/labs/enterprise-context/experience-platforms/sap-build-work-zone/"
  - type: "related_topic"
    title: "SAP AIF — Configuration, Monitoring and Safe Reprocessing"
    url: "/labs/enterprise-context/aif/"
  - type: "related_topic"
    title: "SAP ATP and aATP Promise Engine — Enterprise Context Lab"
    url: "/labs/enterprise-context/atp/"
  - type: "related_topic"
    title: "Automotive JIT / JIS — Enterprise Context Lab"
    url: "/labs/enterprise-context/automotive-jit/"
  - type: "integrates_with"
    title: "IDoc, API, or Event? — SAP Integration Decision Card"
    url: "/labs/enterprise-context/decisions/idoc-api-event/"
  - type: "integrates_with"
    title: "Who Owns an IDoc Failure? — SAP Integration Decision Card"
    url: "/labs/enterprise-context/decisions/idoc-failure-ownership/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-context/">SAP Enterprise</a></li><li aria-current="page">Experience Platforms</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Experience platforms / the layer people actually enter</p>
      <h1>The business systems can be correct.<br />The workplace can still be broken.</h1>
      <p>A user may need S/4HANA, Ariba, SuccessFactors, IBP, custom BTP apps, and third-party tools in one day. An experience platform gives that user a simpler front door without pretending that all business logic lives in one system.</p>
      <a class="research-canvas__button" href="/labs/enterprise-context/experience-platforms/sap-build-work-zone/">Study SAP Build Work Zone <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Experience platform boundary">
      <p>Architecture class</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Engage</strong><small>User entry and experience</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Compose</strong><small>Apps, tasks, content</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Route</strong><small>Back to source systems</small></div>
      <em>The experience can be central while execution remains distributed.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">space_dashboard</span>
    <p><strong>Experience layer:</strong> how people find, enter, and move through work.</p>
    <p><strong>System of record:</strong> where the business object, transaction rules, and authoritative state live.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Why a separate branch</p>
      <h2>This problem is not owned by SD, MM, HR, or Finance.</h2>
      <p>Experience platforms sit across business domains. They matter when the user journey crosses products and systems. The architecture question changes from “Which module owns the transaction?” to “How does the user reach the right work without learning the whole landscape?”</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>ENTRY</span><strong>Central entry point</strong><h3>One role-based place to start work across several applications.</h3><p>The goal is faster access and clearer navigation, not a second copy of every backend.</p></article>
      <article class="ecg-memory-card"><span>WORK</span><strong>Digital workplace</strong><h3>Applications can sit next to information, collaboration, and business context.</h3><p>This is broader than an application launcher when the workplace itself must support teams and knowledge.</p></article>
      <article class="ecg-memory-card"><span>TASK</span><strong>Task aggregation</strong><h3>A single inbox can reduce task hunting across systems.</h3><p>The task aggregator does not become the workflow engine that created the task.</p></article>
      <article class="ecg-memory-card"><span>AI / MOBILE</span><strong>Alternative entry channels</strong><h3>Mobile and conversational entry can shorten the path to a business action.</h3><p>They still depend on identity, authorization, source applications, and reliable business services.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary deep dive</p>
      <h2>SAP Build Work Zone belongs here.</h2>
      <p>Study Work Zone as an enterprise experience and digital-workplace product, not as a sales or procurement module. That makes its boundaries much easier to remember.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-context/experience-platforms/sap-build-work-zone/"><span>WZ</span><strong>SAP Build Work Zone</strong><small>System class, goals, Standard vs Advanced, content federation, source-system boundaries, Fiori launchpad, SAP Start, Task Center, identity, Joule, mobile, diagnostics, and Lead assessment answers.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Adjacent components</p>
      <h2>Similar user surfaces can own different jobs.</h2>
      <p>Do not choose by product name. Start with the responsibility the component must own.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">01</div><div class="ecg-determination-card__copy"><h3>SAP Fiori launchpad</h3><p><strong>Think:</strong> application launchpad and shell. Work Zone can sit above several product launchpads as a cross-solution entry point.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">02</div><div class="ecg-determination-card__copy"><h3>SAP Start</h3><p><strong>Think:</strong> predefined SAP cloud entry point. Work Zone is more configurable and can cover SAP, custom, third-party, cloud, and on-premise content.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">03</div><div class="ecg-determination-card__copy"><h3>SAP Task Center</h3><p><strong>Think:</strong> aggregated tasks. It provides a common task inbox; Work Zone can provide the place where that inbox is reached.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">04</div><div class="ecg-determination-card__copy"><h3>Joule and mobile entry</h3><p><strong>Think:</strong> another way to reach work. Conversational or mobile entry does not move transaction ownership away from source applications.</p></div></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Lead memory rule:</strong> central experience does not mean central execution.</p>
    <a href="/labs/enterprise-context/experience-platforms/sap-build-work-zone/">Open the Work Zone deep dive <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>
</div>
