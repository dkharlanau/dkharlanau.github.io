---
layout: default
title: "Business AI Graph Model — Business AI Lab"
description: "The ontology and relationship model behind the Business AI case catalog: cases, patterns, processes, technologies, KPIs, evidence, limits, and cross-domain links."
permalink: /labs/business-ai/model/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-15
hide_global_cta: true
tags:
  - business-ai
  - knowledge-graph
  - ontology
  - ai-use-cases
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li aria-current="page">Graph Model</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / graph model</p>
      <h1>A case is a node.<br />The useful part is the edges.</h1>
      <p>The catalog is designed as a small knowledge graph. A company is linked to a case, the case to a business process and reusable pattern, the pattern to a system shape, and each reported result back to its evidence source.</p>
      <a class="research-canvas__button" href="#node-types">Open the model <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal">
      <p>Graph contract</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>10</strong><small>Core node types</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>12</strong><small>Core edge types</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>3</strong><small>Controlled case kinds</small></div>
      <em>The model stays simple enough to read as JSON and rich enough to connect across Lab domains.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_tree</span>
    <p><strong>Boundary:</strong> this graph models Business AI implementation knowledge. It does not replace the Enterprise Context graph or the AI Ready architecture model.</p>
    <p><strong>Cross-link rule.</strong> Business AI cases point outward to business domains, SAP processes, technologies, and architecture patterns instead of copying those models.</p>
    <a href="/labs/enterprise-context/">Open Enterprise Context <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span></a>
  </section>

  <section class="research-canvas__inventory" id="case-kinds" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Controlled case kinds</p>
      <h2>Not every useful case is the same type of evidence.</h2>
      <p>Case kind is a controlled property, not another graph node. It prevents an AI implementation, a data foundation, and a vendor solution example from being presented as equivalent proof.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/cases/"><span>AI</span><strong>ai_implementation</strong><small>A company is using AI, ML, optimization, document AI, or agentic logic inside a real business process.</small><i class="material-symbols-outlined" aria-hidden="true">psychology</i></a>
      <a href="/labs/business-ai/cases/#adani-master-data-foundation"><span>DATA</span><strong>ai_foundation</strong><small>A business capability such as governed master data is not AI by itself, but it is a prerequisite for reliable AI decisions and automation.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="/labs/business-ai/cases/#dataxstream-quote-order-ai"><span>SOL</span><strong>solution_evidence</strong><small>A product or partner example shows a useful architecture shape, but the public evidence is weaker than a named end-customer implementation.</small><i class="material-symbols-outlined" aria-hidden="true">extension</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="node-types" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Node types</p>
      <h2>What exists in the catalog.</h2>
      <p>Each node has a stable ID. Display names can change without breaking relationships.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/cases/"><span>CASE</span><strong>BusinessAICase</strong><small>A public implementation, foundation, or solution-evidence case in a defined company and process context.</small><i class="material-symbols-outlined" aria-hidden="true">case_study</i></a>
      <a href="/labs/business-ai/patterns/"><span>PAT</span><strong>Pattern</strong><small>A reusable business and architecture shape that can survive a vendor change.</small><i class="material-symbols-outlined" aria-hidden="true">schema</i></a>
      <a href="/labs/enterprise-context/domains/"><span>DOM</span><strong>BusinessDomain</strong><small>Sales, Procurement, Supply Chain, Finance, Service, Manufacturing, and other ownership areas.</small><i class="material-symbols-outlined" aria-hidden="true">domain</i></a>
      <a href="/labs/enterprise-context/"><span>PROC</span><strong>BusinessProcess</strong><small>The operational flow changed by the use case, such as supplier-invoice processing or customer service.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#node-types"><span>ORG</span><strong>Company</strong><small>The organization that reports or operates the implementation.</small><i class="material-symbols-outlined" aria-hidden="true">business</i></a>
      <a href="#node-types"><span>IND</span><strong>Industry</strong><small>Industry context used to test transferability.</small><i class="material-symbols-outlined" aria-hidden="true">factory</i></a>
      <a href="/labs/ai-ready/"><span>TECH</span><strong>Technology</strong><small>Models, platforms, ERP applications, optimization engines, document AI, integration components, and runtime services.</small><i class="material-symbols-outlined" aria-hidden="true">memory</i></a>
      <a href="#node-types"><span>KPI</span><strong>Metric</strong><small>A measured or reported result with claim type and baseline context where available.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#node-types"><span>SRC</span><strong>EvidenceSource</strong><small>The public source supporting a case, technology statement, or metric.</small><i class="material-symbols-outlined" aria-hidden="true">source</i></a>
      <a href="#node-types"><span>!</span><strong>Limitation</strong><small>A missing measurement, undisclosed stack detail, evidence weakness, or transferability risk.</small><i class="material-symbols-outlined" aria-hidden="true">warning</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="edge-types" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Edge types</p>
      <h2>How the knowledge connects.</h2>
      <p>Edges should describe a real relationship, not a vague similarity.</p>
    </header>
    <div class="research-route-list">
      <a href="#edge-types"><span>→</span><strong>Company IMPLEMENTS Case</strong><small>Who operates or publishes the implementation context.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case IMPLEMENTS_PATTERN Pattern</strong><small>The reusable decision and system shape behind the implementation.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case APPLIES_TO_PROCESS BusinessProcess</strong><small>The process where work or decisions changed.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>BusinessProcess BELONGS_TO BusinessDomain</strong><small>Connects the case back to Enterprise Context ownership.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case OCCURS_IN Industry</strong><small>Keeps industry context explicit without treating one industry result as universal.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case USES Technology</strong><small>Only technologies disclosed by a public source are attached.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case REPORTS Metric</strong><small>A business or operational result reported for the implementation.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Metric SUPPORTED_BY EvidenceSource</strong><small>Lets a reader trace a number back to the organization that published it.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case SUPPORTED_BY EvidenceSource</strong><small>Supports architecture and implementation statements that are not KPIs.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Case HAS_LIMITATION Limitation</strong><small>Keeps uncertainty in the graph instead of hiding it in prose.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="#edge-types"><span>→</span><strong>Pattern EVALUATED_BY Metric</strong><small>Defines which KPIs should decide whether the pattern works in another company.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-context/business-ai/"><span>→</span><strong>Technology MAPS_TO PlatformLandscape</strong><small>Connects implementation evidence to the separate SAP or vendor-neutral technology model.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Example path</p><h2>One case becomes a queryable chain.</h2></div>
    <ol>
      <li><span>01</span><strong>Lemvigh-Müller</strong><p>Company → implements → supplier-confirmation AI case.</p></li>
      <li><span>02</span><strong>Procurement pattern</strong><p>Case → implements pattern → agentic exception management → applies to Procurement.</p></li>
      <li><span>03</span><strong>Evidence and stack</strong><p>Case → uses → SAP AI Core / AI Launchpad / Cloud ERP Private; case → reports → matching accuracy and touchless rate → supported by → source.</p></li>
    </ol>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>