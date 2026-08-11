---

title: Authorization-Aware AI for SAP
layout: default
description: A practical authorization-aware AI pattern for SAP retrieval, generation, recommendations, actions, logs, and tests across enterprise data boundaries.
permalink: /atlas/ai-operations/authorization-aware-ai-for-sap/
atlas_section: ai-operations
domain: AI-assisted operations
subdomain: AI governance
concept_type: AI operations
sap_area: Security / authorization-aware retrieval
business_process: Support operations
status: reviewed
verified: true
level: 2
last_reviewed: 2026-06-13
last_modified_at: 2026-08-11

tags:
  - ai-operations
  - sap-ams
  - data-quality
  - ai-in-business
  - ai-governance
related: 
  - "/atlas/concepts/enterprise-ai-around-sap-decision-framework/"
  - "/atlas/ai-operations/ai-agent-for-sap-support/"
  - "/atlas/data-quality/sap-master-data-quality/"
  - "/atlas/ai-operations/ai-ready-process-documentation/"
robots: index,follow
sitemap: true
short_title: Authorization-Aware AI
h1: Authorization-aware AI for SAP
subtitle: An AI support layer must respect the same access boundaries that protect SAP data from human misuse.
author: Dzmitryi Kharlanau
---

<nav class="breadcrumbs" aria-label="Breadcrumb"><ol><li><a href="/">Home</a></li><li><a href="/atlas/">Knowledge Atlas</a></li><li><a href="/atlas/ai-operations/">Ai Operations</a></li><li aria-current="page">Authorization-Aware AI</li></ol></nav>

<article class="section note-detail atlas-page">

<header class="note-header">

<p class="eyebrow">Knowledge Atlas</p>

<h1>Authorization-aware AI for SAP</h1>

<p class="note-subtitle">An AI support layer must respect the same access boundaries that protect SAP data from human misuse.</p>

<div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>

</header>

<aside class="atlas-meta-panel"><dl><div><dt>Domain</dt><dd>AI-assisted operations</dd></div><div><dt>Type</dt><dd>AI operations</dd></div><div><dt>Reviewed</dt><dd>2026-06-13</dd></div><div><dt>Updated</dt><dd>2026-08-11</dd></div></dl></aside>

<div class="note-body">

<p><strong>Primary sources:</strong> <a href="https://csrc.nist.gov/pubs/sp/800/207/final" target="_blank" rel="noopener noreferrer">NIST SP 800-207, Zero Trust Architecture</a>; <a href="https://airc.nist.gov/airmf-resources/airmf/5-sec-core/" target="_blank" rel="noopener noreferrer">NIST AI Risk Management Framework Core</a>; <a href="https://www.oecd.org/en/topics/ai-principles.html" target="_blank" rel="noopener noreferrer">OECD AI Principles</a>.</p>
<p><strong>Date checked:</strong> 2026-08-11</p>
<p><strong>Confidence:</strong> high for the identity, resource, lifecycle, and traceability principles; medium for implementation details because SAP products, identity systems, retrieval stacks, and local roles vary.</p>
<p><strong>Practical implication:</strong> An AI layer must not turn broad service-account access into broader access for the requester. Enforce policy before retrieval and before action, then test what the response can reveal indirectly.</p>

<h2>Problem this pattern addresses</h2>

<p>An AI assistant can combine data from more systems and documents than a user normally sees in one application. If the integration retrieves with a broad technical account and applies access checks only after generation, it can disclose restricted facts through answers, citations, counts, or suggested actions. Authorization therefore has to follow the request across the full AI workflow.</p>

<h2>Where this fits</h2>

<p>Authorization-aware AI belongs in any SAP support assistant, retrieval workflow, ticket summarizer, analytics interface, or agent that reads operational data. NIST's zero-trust architecture focuses protection on users, assets, and resources rather than assuming trust from network location. For AI, the relevant resource includes source documents, business records, retrieved fragments, generated answers, tool calls, and logs.</p>

<h2>The boundary has six stages</h2>

<table>
  <thead><tr><th>Stage</th><th>Required control question</th><th>Failure example</th></tr></thead>
  <tbody>
    <tr><td>Identity</td><td>Which person or workload is making the request?</td><td>A shared assistant session loses the real requester identity.</td></tr>
    <tr><td>Intent and scope</td><td>Which business purpose, system, organization, and time range are allowed?</td><td>A support question silently expands across company codes.</td></tr>
    <tr><td>Retrieval</td><td>May this identity discover and read every returned source?</td><td>Search metadata reveals a restricted customer or personnel record.</td></tr>
    <tr><td>Generation</td><td>Can the answer expose, combine, or infer restricted information?</td><td>An aggregate or summary reveals data not visible in the source UI.</td></tr>
    <tr><td>Action</td><td>Is this identity allowed to perform this exact operation now?</td><td>A broad technical user bypasses the requester's SAP authorization.</td></tr>
    <tr><td>Evidence</td><td>Who may inspect prompts, sources, outputs, approvals, and logs?</td><td>An audit log becomes a second uncontrolled data store.</td></tr>
  </tbody>
</table>

<h2>Preserve the requester context</h2>

<p>Do not authorize a response only because the integration can reach the data. Carry a verified requester or workload identity through the retrieval and tool boundary. Map it to the business scope required for the use case, such as system, client, company code, sales organization, purchasing organization, plant, data domain, or support assignment.</p>

<p>Use separate technical credentials where the platform requires them, but apply policy using the requester, resource, action, and context. Re-evaluate authorization for each sensitive retrieval or action instead of treating the first chat login as permanent permission.</p>

<h2>Filter before generation</h2>

<p>Access checks should occur before restricted material enters the model context. Filtering only the final answer is weaker because the system has already processed data outside the intended boundary and may reveal it indirectly.</p>

<ul>
  <li>Apply document- and record-level policy before retrieval results are assembled.</li>
  <li>Treat titles, snippets, embeddings, metadata, counts, and citations as potentially sensitive.</li>
  <li>Keep approved operating instructions separate from private tickets and case evidence.</li>
  <li>When sources have mixed authorization, exclude or redact the restricted fragment before generation.</li>
  <li>Return a clear “insufficient authorized evidence” result instead of silently widening access.</li>
</ul>

<h2>Separate recommendation from execution</h2>

<p>A model may be permitted to explain an approved procedure without being permitted to execute it. Treat read, recommend, prepare, approve, execute, and verify as separate capabilities. The person who can view a sales-order status may not be allowed to change the order; the person who can diagnose master data may not be allowed to create or approve it.</p>

<p>For any change-capable tool, validate structured inputs, re-check authorization at execution time, show the reviewer the exact proposed action and affected objects, record approval, and verify the postcondition. High-impact actions should remain unavailable when the assistant cannot establish scope or when the request depends on inferred permission.</p>

<h2>Test for direct and indirect disclosure</h2>

<ol>
  <li>Create identities with deliberately different organizational and document access.</li>
  <li>Test exact identifiers, broad questions, summaries, comparisons, counts, and follow-up questions.</li>
  <li>Test whether citations, autocomplete, errors, and “no result” behavior reveal restricted existence.</li>
  <li>Test retrieved documents that contain both public operating guidance and restricted case evidence.</li>
  <li>Test role removal, temporary access expiry, user transfer, and source reclassification.</li>
  <li>Repeat the action test independently from the retrieval test.</li>
</ol>

<h2>Evidence to retain</h2>

<ul>
  <li>Identity and authorization policy version used for the request.</li>
  <li>Resource identifiers and classifications considered by retrieval.</li>
  <li>Allowed and rejected sources without copying sensitive values into broad logs.</li>
  <li>Model and retrieval configuration, response, reviewer, approval, tool call, and result.</li>
  <li>Access-test cases, failures, remediation, and retest date.</li>
</ul>

<h2>Operational ownership</h2>

<p>Security or identity teams can define controls, but the process owner must still decide the legitimate business purpose and data scope. Knowledge owners classify sources; SAP role owners define source-system access; the AI service owner implements and monitors enforcement; reviewers remain accountable for decisions. NIST's AI RMF treats governance as cross-cutting, which is a better fit than assigning all AI risk to one technical component.</p>

<h2>Boundaries</h2>

<p>This pattern is architectural guidance, not a completed authorization design. It does not map specific SAP roles or certify compliance. Use current product and identity-platform documentation, local security policy, privacy requirements, and legal review. Retest whenever roles, source classifications, retrieval configuration, model providers, tools, or logging change. The <a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-ready documentation pattern</a> covers source status and classification; the <a href="/atlas/concepts/enterprise-ai-around-sap-decision-framework/">AI in Business Decision Framework</a> covers business approval and pilot gates.</p>

</div>

<section class="atlas-related"><h2>Related pages</h2><ul>

<li><a href="/atlas/ai-operations/">AI in Business for SAP Operations cluster</a></li>
<li><a href="/atlas/concepts/enterprise-ai-around-sap-decision-framework/">AI in Business Decision Framework</a></li>
<li><a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a></li>
<li><a href="/atlas/ai-operations/ai-agent-for-sap-support/">AI Agent for SAP Support</a></li>
<li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a></li>
<li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a></li>

</ul></section>

{% include atlas/author-block.html %}

{% include atlas/disclaimer.html %}

</article>
