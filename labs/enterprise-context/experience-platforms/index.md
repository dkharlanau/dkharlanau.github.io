---
layout: default
title: "Experience Platforms — Enterprise Context Lab"
description: "Learn enterprise experience platforms: central entry points, digital workplaces, task access, mobile entry, and SAP Build Work Zone."
permalink: /labs/enterprise-context/experience-platforms/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-23
last_reviewed: 2026-09-03
publication_wave: "sap-experience-review-2026-09"
review_method: "current SAP Build Work Zone and SAP Task Center primary sources + architecture-boundary review"
search_intent: "SAP enterprise experience platform Work Zone Fiori launchpad SAP Start Task Center digital workplace"
structured_data:
  type: TechArticle
primary_topic: "sap-integration"
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
  - title: "Identity Access Management in SAP S/4HANA Cloud Private Edition"
    url: "https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/describing-an-overview-of-identity-access-management_d1f2c3d3-7316-4eb0-bc20-87b70fec72b0"
  - title: "Managing Content on the SAP Fiori Launchpad"
    url: "https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/managing-content-on-the-sap-fiori-launchpad_fee1a412-019b-4b6f-9d31-65b63e896453"
  - title: "Navigating the SAP Fiori Launchpad"
    url: "https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/navigating-the-sap-fiori-launchpad_dfb26034-4672-4530-bfb1-e4cf9859c9e4"
# ai-discovery-managed:start
primary_topic: "sap-integration"
ai_sidecar: "/ai/pages/labs--enterprise-context--experience-platforms.json"
semantic_links:
  - type: "deep_dive"
    title: "SAP Build Work Zone — Enterprise Context Lab"
    url: "/labs/enterprise-context/experience-platforms/sap-build-work-zone/"
  - type: "integrates_with"
    title: "Integration Operations & Recovery — Enterprise Context Lab"
    url: "/labs/enterprise-context/integration-operations/"
  - type: "integrates_with"
    title: "SAP Integration Architecture — Logistics, Events and Data Distribution"
    url: "/labs/enterprise-context/integrations/"
  - type: "integrates_with"
    title: "SAP Data Migration and Controlled Bulk Loading"
    url: "/labs/enterprise-context/integrations/data-migration/"
  - type: "integrates_with"
    title: "SAP DRF — Data Replication Framework"
    url: "/labs/enterprise-context/integrations/drf/"
  - type: "integrates_with"
    title: "SAP Sales Integration Map — IDocs, APIs, Events and Handoffs"
    url: "/labs/enterprise-context/sales-processes/integrations/"
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


  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Fiori authorization model</p>
      <h2>Permission and placement are two different chains.</h2>
      <p>This distinction prevents many launchpad problems. A user can be authorized for an app and still not see it on a page. We should always check both access and layout.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>USER</span><strong>Business User</strong><h3>The person doing business work.</h3><p>A business user receives one or more business roles. Employee data can be replicated from the HR system of record; SAP recommends SAP SuccessFactors Employee Central as one option.</p></article>
      <article class="ecg-memory-card"><span>ROLE</span><strong>Business Role</strong><h3>The job-shaped access container.</h3><p>A business role groups the catalogs and launchpad structure needed for a person's responsibilities. SAP role templates can be copied and adapted instead of changing the delivered template directly.</p></article>
      <article class="ecg-memory-card"><span>CAT</span><strong>Business Catalog</strong><h3>Grants access to a coherent set of apps.</h3><p>A catalog can contain SAP Fiori apps as well as classic UI content such as SAP GUI, Web Dynpro ABAP, or WebClient applications.</p></article>
      <article class="ecg-memory-card"><span>SPACE</span><strong>Space</strong><h3>Groups one or more pages for a business role.</h3><p>The space gives the role a navigation structure. Without a space, authorized apps may not appear visibly on the launchpad.</p></article>
      <article class="ecg-memory-card"><span>PAGE</span><strong>Page</strong><h3>Places selected apps into sections.</h3><p>A page controls what the user sees first. It is a presentation decision, not the authorization source.</p></article>
      <article class="ecg-memory-card"><span>PFCG</span><strong>PFCG role</strong><h3>Implements runtime authorization in Private Edition.</h3><p>Catalogs and spaces are assigned through the security role so the user receives both application access and the intended launchpad structure.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">lock_open</span>
    <p><strong>Access chain:</strong> Business User → Business Role / PFCG role → Business Catalog → App.</p>
    <p><strong>Display chain:</strong> Business Role / PFCG role → Space → Page → selected apps.</p>
    <p><strong>Diagnostic rule:</strong> if the app is missing, ask two questions: “Is the user authorized?” and “Is the app placed on a page assigned to the same role?”</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Business vs technical catalog</p>
      <h2>The technical catalog is the repository. The business catalog is the role-specific selection.</h2>
      <p>Keeping these two layers separate makes launchpad content easier to reuse and maintain.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">TC</div><div class="ecg-determination-card__copy"><h3>Technical Catalog</h3><p>Contains the original launchpad app descriptor items, tiles, and target mappings. One technical catalog can contain many apps.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">BC</div><div class="ecg-determination-card__copy"><h3>Business Catalog</h3><p>Contains references to the app content required by a business role. It is normally a subset of technical-catalog content.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">WHY</div><div class="ecg-determination-card__copy"><h3>Why references matter</h3><p>One original app definition can be reused by several business catalogs. Changes to the original definition remain centrally maintainable.</p></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Which tool manages what?</p>
      <h2>Do not use one launchpad tool for every content object.</h2>
      <p>The tools overlap in navigation, but their ownership is different.</p>
    </header>
    <div class="research-route-list">
      <a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/managing-content-on-the-sap-fiori-launchpad_fee1a412-019b-4b6f-9d31-65b63e896453" target="_blank" rel="noopener"><span>APP</span><strong>Launchpad App Manager · /UI2/FLPAM</strong><small>Manage technical catalogs and launchpad app descriptor items. It supersedes the old Mass Maintenance naming and complements the Content Manager.</small><i class="material-symbols-outlined" aria-hidden="true">apps</i></a>
      <a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/managing-content-on-the-sap-fiori-launchpad_fee1a412-019b-4b6f-9d31-65b63e896453" target="_blank" rel="noopener"><span>CONTENT</span><strong>Launchpad Content Manager</strong><small>Manage business catalogs, references to tiles and target mappings, copies, transport, and usage analysis.</small><i class="material-symbols-outlined" aria-hidden="true">inventory_2</i></a>
      <a href="https://learning.sap.com/courses/implementing-sap-s-4hana-cloud-private-edition/navigating-the-sap-fiori-launchpad_dfb26034-4672-4530-bfb1-e4cf9859c9e4" target="_blank" rel="noopener"><span>LAYOUT</span><strong>Manage Launchpad Spaces / Pages</strong><small>Define how authorized apps are organized and displayed for the role.</small><i class="material-symbols-outlined" aria-hidden="true">dashboard_customize</i></a>
      <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/a7b390faab1140c087b8926571e942b7/845a5491e0804e548cdc1ea41bdc0f11.html" target="_blank" rel="noopener"><span>ROLE</span><strong>PFCG</strong><small>Assign catalogs, spaces, and the required authorizations to the runtime role used by the business user.</small><i class="material-symbols-outlined" aria-hidden="true">admin_panel_settings</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Assessment FAQ</p>
      <h2>Four distinctions worth remembering.</h2>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q1</div><div class="ecg-determination-card__copy"><h3>Does a Space authorize an app?</h3><p>No. The business catalog provides the application authorization. Space and page define where the app is displayed.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q2</div><div class="ecg-determination-card__copy"><h3>What happens if a role has catalogs but no Space?</h3><p>The user may still be able to find authorized apps through search, but the launchpad has no intended page structure for that role.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q3</div><div class="ecg-determination-card__copy"><h3>Which tool owns technical catalogs?</h3><p>Launchpad App Manager. Launchpad Content Manager is focused on business catalogs and references.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q4</div><div class="ecg-determination-card__copy"><h3>Should we edit SAP-delivered role templates directly?</h3><p>No. Use the SAP role as a starting point, copy it, and adapt the customer role while keeping least-privilege and upgrade review in mind.</p></div></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">psychology</span>
    <p><strong>Lead memory rule:</strong> central experience does not mean central execution.</p>
    <a href="/labs/enterprise-context/experience-platforms/sap-build-work-zone/">Open the Work Zone deep dive <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>
</div>
