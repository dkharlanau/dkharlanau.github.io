---

layout: default
title: "AI Agent for SAP Support"
description: "Design and test an evidence-first SAP support agent, comparing AI with deterministic workflows before enabling business actions."
search_intent: "How to evaluate a safe read-only AI agent for SAP SD/MM incident triage"
permalink: /atlas/ai-operations/ai-agent-for-sap-support/
atlas_section: ai-operations
domain: AI-assisted operations
subdomain: SAP AMS support
concept_type: operating pattern
sap_area: "SAP support / BTP-adjacent architecture"
business_process: Support operations
status: needs_verification
verified: false
level: 2
expert_context:
  enabled: true
  domain: ai-sap-operations
  topics:
    - AI-assisted SAP support
    - controlled workflows
    - support knowledge systems
  service_url: /services/sap-ai-ml-enablement/
  evidence_urls:
    - /atlas/ai-operations/authorization-aware-ai-for-sap/
    - /atlas/ai-operations/ai-ready-process-documentation/
    - /atlas/automation/operational-memory-for-sap-ams/
last_reviewed: 2026-05-06
last_modified_at: 2026-11-09
author: Dzmitryi Kharlanau

tags:
  - ai-operations
  - sap-ams
  - operational-memory
  - ai-in-business
related:
  - /atlas/concepts/enterprise-ai-around-sap-decision-framework/
  - /atlas/automation/rule-based-automation-vs-ai/
  - /atlas/diagnostics/sap-sales-order-block-diagnosis/
  - /ai/practical-ai-for-sap-support/
  - /services/sap-ai-ml-enablement/
  - /atlas/ai-operations/practical-ai-ml-for-sap-support/
  - /atlas/ai-operations/ai-ready-process-documentation/
  - /atlas/ai-operations/authorization-aware-ai-for-sap/
  - /atlas/automation/operational-memory-for-sap-ams/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/ai-operations/">AI Operations</a></li>
    <li aria-current="page">AI Agent for SAP Support</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas AI Operations</p>
    <h1>AI agent for SAP support</h1>
    <p class="note-subtitle">The useful agent is not the one that sounds confident. It is the one that knows what evidence to collect, what it may do, and when a human must decide.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Support operations</dd></div>
      <div><dt>Pattern</dt><dd>Evidence, retrieval, tools, approval, traceability</dd></div>
      <div><dt>Earlier review</dt><dd>06 May 2026 (pre-November content)</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>The problem this architecture solves</h2>
    <p>SAP support work is expensive when every incident starts with the same manual search: find the document, collect logs, identify the process owner, search old tickets, and decide which evidence matters. The problem is not a lack of chat. It is repeated context reconstruction across systems, teams, and years of operational history.</p>
    <p>An AI assistant can reduce that reconstruction work, but only if it respects access, evidence quality, and process ownership. Without those controls it may produce a faster answer while making the support decision less trustworthy.</p>

    <h2>Start with the support decision, not with the agent</h2>
    <p>“Build an SAP support agent” is too vague to be an architecture. A better starting point is a small support decision: classify an incident, collect missing evidence, find the right runbook, compare a failing document with a known pattern, or prepare an escalation.</p>
    <p>Once the decision is clear, the role of AI becomes easier to control. It can read more context than a person has time to read, structure the evidence, and suggest the next check. That is useful. Quietly changing ERP data because a language model found a plausible answer is a different category of risk.</p>

    {% include atlas/expert-context.html %}

    <h2>A practical architecture</h2>
    <div class="decision-table"><table><thead><tr><th>Layer</th><th>What it should do</th><th>What can go wrong</th></tr></thead><tbody>
      <tr><td>Identity and access</td><td>Know who is asking and which sources or tools that person may use.</td><td>The model retrieves data the user should not see or acts with a broader technical account.</td></tr>
      <tr><td>Context and retrieval</td><td>Bring in approved runbooks, process notes, incident history, system evidence, and product documentation.</td><td>Old or unrelated material is treated as current truth.</td></tr>
      <tr><td>Reasoning structure</td><td>Separate facts, assumptions, missing evidence, likely paths, and the next diagnostic step.</td><td>A fluent explanation hides that the key evidence is missing.</td></tr>
      <tr><td>Tools</td><td>Read statuses, search logs, create a draft ticket, or call approved services within a narrow contract.</td><td>A broad tool turns a suggestion into an uncontrolled business action.</td></tr>
      <tr><td>Approval</td><td>Pause before actions with financial, master-data, security, compliance, or process impact.</td><td>The human becomes a decorative click after the system has already decided.</td></tr>
      <tr><td>Record</td><td>Keep the evidence, source references, proposed action, approval, and result.</td><td>The team cannot explain later why the action was taken.</td></tr>
    </tbody></table></div>

    <h2>Read wide, act narrow</h2>
    <p>This is a useful design rule for enterprise support. The agent may read a broad set of permitted evidence, but its write actions should be much narrower. Reading a sales-order status is not the same risk as releasing a credit block. Drafting a change request is not the same as transporting configuration.</p>
    <p>Many early use cases need no autonomous write access at all. Ticket enrichment, incident summarization, runbook retrieval, duplicate detection, evidence checklists, and escalation drafts already remove a lot of repetitive support work.</p>

    <h2>Example: a blocked sales order</h2>
    <p>A useful agent does not jump from “order blocked” to “remove the block.” It first asks what should happen next, reads the available order context, identifies whether the evidence points to incompletion, credit, delivery, billing, or another control, and shows which facts are still missing.</p>
    <p>If the case needs a credit release or master-data correction, the agent can prepare the evidence for the responsible person. The approval still belongs to the process owner. This is slower than pretending the model is autonomous and considerably faster than cleaning up a bad autonomous decision.</p>

    <h2>Where AI helps and where rules are better</h2>
    <p>Use AI where the input is messy and interpretation has value: text classification, evidence extraction, semantic retrieval, summarization, comparison, and explanation. Use deterministic automation where the rule is stable and testable: required-field checks, routing by known codes, scheduled monitoring, exact validations, or a well-defined API workflow.</p>
    <p>A mature design often combines both. AI interprets the situation, a rule checks the boundary, a human approves the risky step, and deterministic automation executes the approved action.</p>

    <h2>What the agent should say when evidence is weak</h2>
    <p>Uncertainty should be visible in the output. A good response can state: what is known, what is only likely, which source supports the conclusion, what evidence is missing, and which next check would reduce uncertainty. That is far more useful in SAP support than a polished paragraph that quietly mixes facts and guesses.</p>

    <h2>Experiment: can read-only AI beat a deterministic support form?</h2>
    <p><strong>Proposed offline benchmark, not a delivered tool or proven efficiency gain:</strong> use 30 approved, de-identified historical SAP SD/MM incidents. If permitted records are unavailable, use synthetic fixtures and report the findings strictly as simulation results. Compare the team's current checklist, a deterministic evidence form and a retrieval-only AI assistant. All three methods receive the same case snapshots and approved runbooks; the AI has no ERP write capability and may not retrieve data outside the test user's permissions.</p>
    <p>Have an independent SAP reviewer establish the expected next check and essential evidence for each case <em>before</em> scoring the methods. Use paired cases, rotate method order to reduce learning bias, and report the five deliberately incomplete or contradictory cases as a separate stress-test subset rather than a representative incident frequency. A 30-case sample establishes feasibility, not statistical proof of production benefit.</p>
    <p>Use one structured response contract; the following is <strong>synthetic diagnostic JSON</strong>, not an SAP API response or an evaluated agent output:</p>
    <pre><code class="language-json">{
  "case_ref": "SYNTH-SD-001",
  "observed_facts": [
    {
      "statement": "sales document exists in the supplied snapshot",
      "source_ref": "approved-snapshot-01",
      "observed_at": "2026-11-07T10:00:00Z"
    }
  ],
  "hypotheses": [],
  "missing_evidence": ["current item and schedule-line status"],
  "next_check": "read the latest authorised sales-document status",
  "conclusion": "insufficient_evidence",
  "proposed_erp_change": null,
  "human_review_required": true,
  "write_allowed": false
}</code></pre>
    <p><strong>Score the whole workflow:</strong> evidence completeness, correct first next check against the reviewer reference, unsupported factual assertions, traceable source citations, total analyst preparation and correction time, and total cost (including model calls, infrastructure and human review). Record results per method and case, not only average model latency. For the five stressed cases, supply a second <em>offline</em> snapshot with changed or reconciled evidence and check whether the response updates its assessment without pretending the first hypothesis was proven.</p>
    <p><strong>Stop conditions:</strong> any cross-permission disclosure, attempted write, unverifiable source attribution, invented SAP status or material increase in net review effort. Continue past the pilot only if AI produces a reproducible improvement over the deterministic form without weakening evidence quality or access controls. The <a href="https://airc.nist.gov/">NIST AI Resource Center</a> provides resources for testing, evaluation, verification and validation (TEVV); NIST has not certified this pilot or its proposed scoring criteria.</p>
    <p><strong>Review boundary:</strong> this November 2026 benchmark and sample contract are pending human technical and editorial review. The 6 May 2026 review date applies to the pre-existing article, not to these additions. No experiment results, customer outcomes or production claims are asserted here.</p>

    <h2>Measure support value, not chat activity</h2>
    <p>The useful measures are operational: time to collect complete evidence, first-assignment accuracy, reduction in repeated investigation, escalation quality, runbook reuse, and safe resolution time. Message count and answer length tell very little about whether the support process improved.</p>

    <h2>The boundary that matters</h2>
    <p>An SAP support agent should make the team better at diagnosis before it is allowed to make the system different. If the architecture cannot explain who saw what, which evidence supported the recommendation, who approved the action, and what changed afterwards, the automation boundary is too loose.</p>
  </div>

  <section class="atlas-related">
    <h2>Related Pages</h2>
    <ul>
      <li><a href="/atlas/ai-operations/">AI in Business for SAP Operations cluster</a></li>
      <li><a href="/atlas/concepts/enterprise-ai-around-sap-decision-framework/">AI in Business Decision Framework</a></li>
      <li><a href="/atlas/automation/rule-based-automation-vs-ai/">Rule-Based Automation vs AI</a></li>
      <li><a href="/atlas/ai-operations/ai-ready-process-documentation/">AI-Ready Process Documentation</a></li>
      <li><a href="/atlas/ai-operations/authorization-aware-ai-for-sap/">Authorization-Aware AI for SAP</a></li>
      <li><a href="/atlas/automation/operational-memory-for-sap-ams/">Operational Memory for SAP AMS</a></li>
    </ul>
  </section>

  {% include atlas/expert-cta.html %}
  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
