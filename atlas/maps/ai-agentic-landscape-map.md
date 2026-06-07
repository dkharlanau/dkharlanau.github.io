---
layout: default
title: "AI and Agentic Technology Landscape Map"
description: "A landscape map of AI and agentic technologies in the SAP ecosystem for operational navigation."
permalink: /atlas/maps/ai-agentic-landscape-map/
atlas_section: maps
domain: SAP operations
subdomain: AI and agentic landscape
concept_type: map
sap_area: "AI and agentic technologies"
business_process: "AI-assisted operations"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - ai-agentic
  - landscape-map
  - sap-joule
related:
  - /atlas/maps/data-analytics-landscape-map/
  - /atlas/maps/developer-tooling-landscape-map/
  - /atlas/maps/operations-observability-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-business-ai/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/maps/">Maps</a></li>
    <li aria-current="page">AI and Agentic Technology Landscape Map</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Map</p>
    <h1>AI and agentic technology landscape map</h1>
    <p class="note-subtitle">A navigation frame for AI and agentic technologies in the SAP landscape.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Domain</dt><dd>SAP operations</dd></div>
      <div><dt>Type</dt><dd>landscape map</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until AI product positioning and capability claims are verified.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What this map is</h2>
    <p>An AI-layer view of the SAP landscape. It separates copilot interfaces, platform services, retrieval patterns, and operational controls without replacing SAP product documentation.</p>

    <h2>Business purpose</h2>
    <p>Help architects and operations teams understand where AI capabilities sit, how they retrieve context, and what controls are needed for safe deployment.</p>

    <h2>Where it sits in the landscape</h2>
    <p><a href="/atlas/sap/sap-joule/">SAP Joule</a> is the copilot interface. <a href="/atlas/sap/sap-business-ai/">SAP Business AI</a> is the underlying platform. <a href="/atlas/sap/rag/">RAG</a> is the primary retrieval pattern. Agent memory and <a href="/atlas/sap/evaluation-guardrails/">evaluation guardrails</a> are operational concerns that span all layers.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Copilot: Joule skills, natural language prompts, user sessions.</li>
      <li>Platform: Business AI services, foundation models, embeddings.</li>
      <li>Retrieval: <a href="/atlas/sap/vector-search/">vector search</a> indexes, document chunks, CDS view contexts.</li>
      <li>Controls: guardrails, evaluation metrics, <a href="/atlas/sap/human-approval-workflows/">human approval workflows</a>.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>Joule → S/4HANA transactions and Fiori apps for task execution.</li>
      <li>Business AI → BTP services and SAP AI Core for model hosting.</li>
      <li>RAG → Datasphere, document repositories, and <a href="/atlas/sap/ai-agents/">AI agents</a> knowledge bases.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom Joule skills for domain-specific workflows.</li>
      <li>Custom RAG pipelines with enterprise document stores.</li>
      <li>Agent orchestration via BTP and third-party frameworks.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Joule interaction logs and skill execution traces.</li>
      <li>RAG retrieval accuracy and relevance scoring.</li>
      <li>Guardrail trigger rates and approval workflow bottlenecks.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Natural language interface lowers barrier for occasional users.</li>
      <li>RAG grounds responses in enterprise data rather than model hallucinations.</li>
      <li>Guardrails and approval workflows provide operational safety.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Model behavior drift across releases.</li>
      <li>RAG quality depends on document freshness and chunking strategy.</li>
      <li>Latency in copilot responses for complex multi-step tasks.</li>
      <li>Compliance and data residency constraints for AI processing.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Joule skill fails after S/4HANA upgrade due to API changes.</li>
      <li>RAG returns outdated answers because vector index is stale.</li>
      <li>Guardrails block legitimate workflows due to overly restrictive thresholds.</li>
      <li>AI-generated recommendation conflicts with existing business rules.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/sap-joule/">SAP Joule</a></li>
      <li><a href="/atlas/sap/sap-business-ai/">SAP Business AI</a></li>
      <li><a href="/atlas/sap/ai-agents/">AI Agents</a></li>
      <li><a href="/atlas/sap/rag/">RAG</a></li>
      <li><a href="/atlas/sap/vector-search/">Vector Search</a></li>
      <li>Agent Memory</li>
      <li><a href="/atlas/sap/evaluation-guardrails/">Evaluation and Guardrails</a></li>
      <li><a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This map is a skeleton based on public SAP documentation. AI feature availability, model versions, and integration paths must be verified against the customer's S/4HANA release, BTP subaccount, and Joule tenant configuration.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/data-analytics-landscape-map/">Data and Analytics Landscape Map</a></li>
      <li><a href="/atlas/maps/developer-tooling-landscape-map/">Developer Tooling Landscape Map</a></li>
      <li><a href="/atlas/maps/operations-observability-landscape-map/">Operations and Observability Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-technology-landscape-map/">SAP Technology Landscape Map</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
