---
layout: default
title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
description: "An open research programme for ERP and Enterprise AI covering evidence quality, agent safety, AI readiness, document benchmarks, and reproducible tests."
permalink: /labs/business-ai/open-research/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-08-17
last_reviewed: 2026-08-17
hide_global_cta: true
publication_wave: "public-business-ai-pilots-01"
review_method: "author-defined research protocol + primary-source evidence review"
evidence_review_mode: "selective_or_heuristic"
search_intent: "open ERP AI research, enterprise AI evidence registry, ERP agent safety benchmark, ERP AI readiness assessment"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - enterprise-ai
  - erp
  - research
  - benchmarking
  - ai-governance
  - agents
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--open-research.json"
semantic_links:
  - type: "parent_context"
    title: "Business AI Lab — Processes, Patterns, Technologies, Evidence"
    url: "/labs/business-ai/"
  - type: "related_topic"
    title: "AI Ready — Practical AI Architecture Lab"
    url: "/labs/ai-ready/"
  - type: "integrates_with"
    title: "Enterprise Agent Architecture — Tools, Identity, Autonomy and Governance"
    url: "/labs/enterprise-context/business-ai/agents/"
  - type: "related_topic"
    title: "Open Enterprise AI Pilots — ERP, Documents, Agents, and Controls"
    url: "/labs/business-ai/pilots/"
  - type: "related_topic"
    title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
    url: "/labs/business-ai/document-to-erp-ai/"
  - type: "related_topic"
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "same_domain"
    title: "AI Governance and Data Boundaries — Ownership, Access, Action Risk and Validation"
    url: "/labs/business-ai/governance-data-boundaries/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/pilots/">Pilots</a></li><li aria-current="page">Open Research</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Business AI / open research</p>
      <h1>I would rather publish<br />a failed test than a perfect slide.</h1>
      <p>Enterprise AI has enough promises. This programme is for the less glamorous part: checking claims, defining failure cases, building small benchmarks, and publishing what can and cannot be trusted.</p>
      <a class="research-canvas__button" href="#research-tracks">Open the research tracks <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Research principles">
      <p>Research rules</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Source</strong><small>Prefer primary evidence</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Test</strong><small>Make failure visible</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Share</strong><small>Publish reusable results</small></div>
      <em>No confidential production data is required. Synthetic examples are often better because anyone can repeat the test.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Research boundary">
    <span class="material-symbols-outlined" aria-hidden="true">science</span>
    <p><strong>This is not vendor ranking.</strong> A product can be strong in one process and weak in another. The useful unit of analysis is the business job, architecture boundary, control model, evidence, and measurable result.</p>
    <p><strong>This is not an anti-AI project.</strong> The point is to find where AI is useful enough to deserve production responsibility and where it should remain a suggestion layer.</p>
  </section>

  <section class="research-canvas__inventory" id="research-tracks" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Research map</p>
      <h2>Four tracks that can grow into reusable public evidence.</h2>
      <p>The tracks are connected. A vendor claim can become a benchmark question. A benchmark failure can become a readiness rule. A readiness gap can become the next pilot.</p>
    </header>
    <div class="research-route-list">
      <a href="#evidence-registry"><span>R1</span><strong>Enterprise AI Evidence Registry</strong><small>Claims, sources, reported outcomes, missing measurements, limitations, architecture dependencies, and verification dates.</small><i class="material-symbols-outlined" aria-hidden="true">fact_check</i></a>
      <a href="#safety-benchmark"><span>R2</span><strong>ERP Agent Safety Benchmark</strong><small>A repeatable pack for permission, tool-selection, injection, duplicate-action, stale-context, confirmation, and recovery tests.</small><i class="material-symbols-outlined" aria-hidden="true">shield</i></a>
      <a href="#readiness"><span>R3</span><strong>ERP AI Readiness Assessment</strong><small>A practical maturity model for process, data, documents, integration, security, observability, governance, and authority.</small><i class="material-symbols-outlined" aria-hidden="true">checklist</i></a>
      <a href="#document-benchmark"><span>R4</span><strong>Document-to-ERP Benchmark</strong><small>Synthetic business documents with expected canonical objects, validation outcomes, approvals, and safe final actions.</small><i class="material-symbols-outlined" aria-hidden="true">description</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="evidence-registry" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">R1 / evidence</p>
      <h2>Separate “available” from “proven useful”.</h2>
      <p>Enterprise AI announcements often mix product availability, planned features, customer stories, vendor estimates, and measured production results. They should not all receive the same evidence grade.</p>
    </header>
    <div class="research-route-list">
      <a href="#evidence-registry"><span>E1</span><strong>Claim</strong><small>What exactly is being claimed: capability, productivity, automation rate, quality, cost, user adoption, or business outcome?</small><i class="material-symbols-outlined" aria-hidden="true">subject</i></a>
      <a href="#evidence-registry"><span>E2</span><strong>Source type</strong><small>Official documentation, release plan, standard, customer case, research paper, benchmark, analyst note, or secondary report.</small><i class="material-symbols-outlined" aria-hidden="true">source</i></a>
      <a href="#evidence-registry"><span>E3</span><strong>Evidence status</strong><small>Confirmed capability, reported customer result, measured independent result, inference, planned feature, or unresolved claim.</small><i class="material-symbols-outlined" aria-hidden="true">verified</i></a>
      <a href="#evidence-registry"><span>E4</span><strong>Boundary</strong><small>Process, geography, release, data requirement, implementation condition, architecture dependency, and known limitation.</small><i class="material-symbols-outlined" aria-hidden="true">border_all</i></a>
      <a href="#evidence-registry"><span>E5</span><strong>What to test</strong><small>One practical experiment that would tell us whether the claim matters in an enterprise landscape.</small><i class="material-symbols-outlined" aria-hidden="true">experiment</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Evidence principle">
    <span class="material-symbols-outlined" aria-hidden="true">balance</span>
    <p><strong>Evidence rule.</strong> “The vendor supports this” is useful architecture information. It is not the same as “this creates measurable value in my process”. The registry should keep those statements separate.</p>
  </section>

  <section class="research-canvas__inventory" id="safety-benchmark" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">R2 / agent safety</p>
      <h2>Give the agent chances to make the wrong decision.</h2>
      <p>A benchmark with only happy paths measures obedience, not safety. The test pack should include conditions that force the system to deny, re-read, ask for approval, or stop.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/erp-agent-gateway/#tests"><span>S1</span><strong>Authorization tests</strong><small>Wrong company, wrong role, restricted object, restricted field, environment mismatch, and segregation-of-duties conflict.</small><i class="material-symbols-outlined" aria-hidden="true">lock</i></a>
      <a href="/labs/business-ai/erp-agent-gateway/#tests"><span>S2</span><strong>State tests</strong><small>Changed master data, stale order state, closed period, already-completed process, concurrent update, and duplicate retry.</small><i class="material-symbols-outlined" aria-hidden="true">sync_problem</i></a>
      <a href="/labs/business-ai/erp-agent-gateway/#tests"><span>S3</span><strong>Reasoning tests</strong><small>Ambiguous user request, wrong tool, missing parameter, conflicting instructions, and overconfident assumption.</small><i class="material-symbols-outlined" aria-hidden="true">psychology_alt</i></a>
      <a href="/labs/business-ai/erp-agent-gateway/#tests"><span>S4</span><strong>Adversarial tests</strong><small>Prompt injection through documents, notes, web content, tool descriptions, or untrusted external data.</small><i class="material-symbols-outlined" aria-hidden="true">security</i></a>
      <a href="/labs/business-ai/erp-agent-gateway/#tests"><span>S5</span><strong>Recovery tests</strong><small>Timeout, partial failure, ambiguous response, tool unavailability, rollback requirement, and human takeover.</small><i class="material-symbols-outlined" aria-hidden="true">settings_backup_restore</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" id="readiness" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">R3 / readiness</p>
      <h2>Do not start with “Which model should we buy?”</h2>
      <p>The readiness assessment starts from the process and authority model. A powerful model cannot repair unclear ownership, broken master data, missing interfaces, or an approval process that nobody can explain.</p>
    </header>
    <div class="research-route-list">
      <a href="#readiness"><span>A1</span><strong>Process</strong><small>Stable steps, clear exceptions, decision ownership, measurable pain, and known cost of error.</small><i class="material-symbols-outlined" aria-hidden="true">route</i></a>
      <a href="#readiness"><span>A2</span><strong>Data and documents</strong><small>Availability, quality, identity, lineage, master-data reliability, document variation, and retention constraints.</small><i class="material-symbols-outlined" aria-hidden="true">database</i></a>
      <a href="#readiness"><span>A3</span><strong>Integration</strong><small>Read and write interfaces, event availability, error semantics, idempotency, and system-of-record boundaries.</small><i class="material-symbols-outlined" aria-hidden="true">hub</i></a>
      <a href="#readiness"><span>A4</span><strong>Security and authority</strong><small>Identity, permissions, delegated access, sensitive data, tool scope, approval, and forbidden actions.</small><i class="material-symbols-outlined" aria-hidden="true">policy</i></a>
      <a href="#readiness"><span>A5</span><strong>Evaluation and operations</strong><small>Test cases, failure metrics, monitoring, traceability, fallback, support ownership, and change management.</small><i class="material-symbols-outlined" aria-hidden="true">monitoring</i></a>
      <a href="#readiness"><span>A6</span><strong>Economics</strong><small>Transaction volume, manual effort, exception rate, model/tool cost, integration cost, and value of avoided error.</small><i class="material-symbols-outlined" aria-hidden="true">payments</i></a>
    </div>
  </section>

  <section class="research-canvas__method" data-reveal>
    <div><p class="research-canvas__eyebrow">Assessment output</p><h2>Readiness should end with a decision, not a score.</h2></div>
    <ol>
      <li><span>01</span><strong>Ready for pilot</strong><p>The process has enough clarity, data, integration, and control to justify a limited experiment.</p></li>
      <li><span>02</span><strong>Fix foundations first</strong><p>The main blockers are process, master data, interface, identity, or observability problems that AI would only hide.</p></li>
      <li><span>03</span><strong>Assist, do not automate</strong><p>AI may help with retrieval, explanation, classification, or proposal generation, but transaction authority stays manual.</p></li>
      <li><span>04</span><strong>Do not pursue</strong><p>The expected value is too small, the risk is too high, or a simpler deterministic solution solves the problem better.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" id="document-benchmark" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">R4 / document benchmark</p>
      <h2>Make document automation testable without customer data.</h2>
      <p>The benchmark uses synthetic documents, expected business objects, and explicit process outcomes. This makes it possible to compare extraction, reasoning, validation, and control patterns without publishing anyone’s invoices or purchase orders to the internet, which tends to upset legal departments for surprisingly understandable reasons.</p>
    </header>
    <div class="research-route-list">
      <a href="/labs/business-ai/document-to-erp-ai/#dataset"><span>B1</span><strong>Synthetic document set</strong><small>Normal, noisy, ambiguous, duplicate, stale, and adversarial documents across common ERP process types.</small><i class="material-symbols-outlined" aria-hidden="true">dataset</i></a>
      <a href="/labs/business-ai/document-to-erp-ai/#metrics"><span>B2</span><strong>Expected outcomes</strong><small>Canonical object, valid/invalid state, required correction, required approval, and final safe action for every test item.</small><i class="material-symbols-outlined" aria-hidden="true">rule</i></a>
      <a href="/labs/business-ai/document-to-erp-ai/"><span>B3</span><strong>Reference architecture</strong><small>Extraction, validation, human review, transaction adapter, audit, and evaluation separated into explicit components.</small><i class="material-symbols-outlined" aria-hidden="true">architecture</i></a>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Collaboration model">
    <span class="material-symbols-outlined" aria-hidden="true">groups</span>
    <p><strong>Open collaboration.</strong> I am interested in small non-commercial research contributions: synthetic scenarios, public source checks, benchmark cases, control rules, architecture criticism, and adapters that can be shared openly.</p>
    <p><strong>No production secrets.</strong> Do not send customer data, credentials, internal screenshots, confidential architecture, proprietary prompts, or anything you are not allowed to publish. A good synthetic case is enough.</p>
    <p><strong>Useful contribution format.</strong> State the business problem, expected result, failure condition, source or assumption, and what a repeatable test should prove.</p>
  </section>

  <section class="research-canvas__inventory" id="questions" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Question backlog</p>
      <h2>Questions worth answering in public.</h2>
      <p>These are better research questions than “Which enterprise AI platform is best?” because they can produce a testable answer.</p>
    </header>
    <div class="research-route-list">
      <a href="#questions"><span>Q1</span><strong>When should an ERP agent receive write access?</strong><small>Which combination of process risk, user role, tool design, validation, and approval makes a write action acceptable?</small><i class="material-symbols-outlined" aria-hidden="true">edit</i></a>
      <a href="#questions"><span>Q2</span><strong>Which ERP tasks need an LLM at all?</strong><small>Compare generative reasoning with rules, search, workflow, optimization, classical ML, and ordinary automation.</small><i class="material-symbols-outlined" aria-hidden="true">compare_arrows</i></a>
      <a href="#questions"><span>Q3</span><strong>How much context is enough?</strong><small>Measure when more ERP, document, and knowledge context improves decisions and when it adds noise or risk.</small><i class="material-symbols-outlined" aria-hidden="true">filter_alt</i></a>
      <a href="#questions"><span>Q4</span><strong>What should be evaluated before production?</strong><small>Define the minimum test set for accuracy, business validity, permissions, recovery, traceability, cost, and operator trust.</small><i class="material-symbols-outlined" aria-hidden="true">task_alt</i></a>
      <a href="#questions"><span>Q5</span><strong>Can one agent pattern survive several ERP systems?</strong><small>Separate reusable process and control logic from SAP-, Dynamics-, Oracle-, and landscape-specific interfaces.</small><i class="material-symbols-outlined" aria-hidden="true">device_hub</i></a>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
