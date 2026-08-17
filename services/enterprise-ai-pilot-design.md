---
layout: default
title: "Enterprise AI Pilot Design for ERP — Documents, Agents, Controls"
description: "Enterprise AI pilot design for ERP and document workflows, covering architecture, controls, evaluation, integration, and safe production boundaries."
permalink: /services/enterprise-ai-pilot-design/
last_modified_at: 2026-08-17
---

<section class="section note-detail">
  <article class="note-article neub-card">
    <header class="note-header">
      <p class="eyebrow">Service</p>
      <h1>Enterprise AI pilot design for ERP, documents, and agent workflows</h1>
      <p class="note-subtitle">Start with one business process. Define what AI may do, what the ERP must still decide, and what evidence would justify the next step.</p>
    </header>
    <div class="note-body">
      <p>This service is for teams exploring AI around SAP, Microsoft Dynamics 365, Oracle, or mixed ERP landscapes. The starting point is not a model shortlist. It is one business job where unstructured information, repeated analysis, or slow decisions create enough friction to justify a controlled experiment.</p>

      <h2>A pilot should answer a business question</h2>
      <p>Many AI pilots prove that a model can produce an answer. That is not enough. An enterprise pilot must also show whether the answer can be trusted inside a process, which system owns the truth, what happens when data conflicts, who approves risky actions, and how the result will be measured after the demo is over.</p>

      <div class="process-rail" aria-label="Enterprise AI pilot design">
        <div class="process-rail__step"><strong>Frame</strong><span>Name the process step, pain, owner, source of truth, and cost of error.</span></div>
        <div class="process-rail__step"><strong>Bound</strong><span>Separate AI judgment from deterministic rules, permissions, and transaction authority.</span></div>
        <div class="process-rail__step"><strong>Build</strong><span>Use the smallest architecture and dataset that can test the important assumption.</span></div>
        <div class="process-rail__step"><strong>Evaluate</strong><span>Test normal, difficult, and failure cases before deciding whether to scale.</span></div>
      </div>

      <h2>Typical pilot shapes</h2>
      <ul>
        <li>Document-to-ERP workflows for orders, invoices, confirmations, quotations, and other business documents.</li>
        <li>ERP assistants that retrieve context, explain business state, prepare actions, or use approved tools.</li>
        <li>Support and operations workflows that assemble evidence, classify exceptions, and propose next actions.</li>
        <li>Enterprise search and retrieval across process documentation, tickets, runbooks, and structured system data.</li>
        <li>Readiness assessments where the main question is whether AI is appropriate at all.</li>
      </ul>

      <h2>What the engagement covers</h2>
      <ul>
        <li>Business-process and decision boundary.</li>
        <li>Data, document, retrieval, and context requirements.</li>
        <li>ERP and integration interface options, including MCP where it fits.</li>
        <li>Identity, permissions, human approval, and forbidden actions.</li>
        <li>Evaluation cases, failure scenarios, metrics, and acceptance criteria.</li>
        <li>Build-versus-buy and vendor-specific considerations without forcing the design into one platform.</li>
      </ul>

      <h2>The control boundary matters more than the model name</h2>
      <p>A model may classify a document, explain an exception, or choose a tool. It should not silently become the owner of pricing rules, posting logic, master-data validity, authorization, or legal approval. Those controls belong in deterministic services, ERP configuration, policy layers, and accountable human workflows.</p>

      <h2>Expected outputs</h2>
      <ul>
        <li>A pilot charter with business objective, owner, scope, assumptions, and exit criteria.</li>
        <li>A reference architecture covering AI, data, tools, ERP integration, policy, approval, audit, and fallback.</li>
        <li>A representative test set with normal, ambiguous, and unsafe cases.</li>
        <li>An evaluation scorecard covering business validity, unsafe action rate, human correction, traceability, and operating cost.</li>
        <li>A recommendation to scale, redesign, keep AI assistive, fix foundations first, or stop.</li>
      </ul>

      <h2>When the answer should be “do not use AI”</h2>
      <p>If a rule, query, workflow, integration, or ordinary application solves the problem reliably, use it. AI becomes interesting when interpretation, unstructured evidence, uncertain classification, or context-heavy reasoning is the bottleneck. Adding a model to deterministic work does not make the process modern. It mostly adds another thing to monitor.</p>

      <h2>Public pilot work</h2>
      <p>The <a href="/labs/business-ai/pilots/">Open Enterprise AI Pilots</a> show the architecture style behind this service. The current flagship designs cover <a href="/labs/business-ai/document-to-erp-ai/">Document-to-ERP AI</a> and an <a href="/labs/business-ai/erp-agent-gateway/">ERP Agent Gateway</a>. The <a href="/labs/business-ai/open-research/">Open Research programme</a> extends the same work into evidence, safety benchmarks, readiness, and synthetic test data.</p>

      <h2>Related work</h2>
      <p><a href="/labs/business-ai/">Business AI Lab</a> · <a href="/labs/ai-ready/">AI Ready Architecture</a> · <a href="/labs/enterprise-context/integrations/">SAP integration</a> · <a href="/services/sap-ai-ml-enablement/">SAP AI and ML enablement</a> · <a href="/services/sap-integration-architecture/">SAP integration architecture</a></p>
    </div>
  </article>
</section>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "name": "Enterprise AI Pilot Design for ERP",
  "provider": {
    "@type": "Person",
    "@id": "https://dkharlanau.github.io/#dkharlanau"
  },
  "serviceType": "Enterprise AI pilot design for ERP and document workflows",
  "areaServed": "Global",
  "url": "https://dkharlanau.github.io/services/enterprise-ai-pilot-design/",
  "description": "Practical Enterprise AI pilot design for ERP, document, and agent workflows with architecture, controls, evaluation, and integration boundaries."
}
</script>

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {"@type": "ListItem","position": 1,"name": "Home","item": "https://dkharlanau.github.io/"},
    {"@type": "ListItem","position": 2,"name": "Services","item": "https://dkharlanau.github.io/services/"},
    {"@type": "ListItem","position": 3,"name": "Enterprise AI Pilot Design","item": "https://dkharlanau.github.io/services/enterprise-ai-pilot-design/"}
  ]
}
</script>
