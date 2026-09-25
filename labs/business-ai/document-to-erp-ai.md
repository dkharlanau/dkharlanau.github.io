---
layout: default
title: "Document-to-ERP AI Pilot — From PDF to Controlled Transaction"
description: "A vendor-neutral Enterprise AI pilot for turning business documents into validated ERP proposals with controls, approvals, metrics, and audit trails."
permalink: /labs/business-ai/document-to-erp-ai/
status: reviewed
verified: true
robots: index,follow
sitemap: true
last_modified_at: 2026-09-24
last_reviewed: 2026-09-24
hide_global_cta: true
publication_wave: "public-business-ai-pilots-01"
review_method: "current SAP Help primary sources + adjacent Labs review + full editorial pass"
evidence_review_mode: "selective_or_heuristic"
search_intent: "document to ERP AI, intelligent document processing ERP, AI document automation with human approval"
structured_data:
  type: TechArticle
tags:
  - business-ai
  - enterprise-ai
  - erp
  - document-ai
  - integration
  - ai-governance
source_links:
  - title: "SAP Document AI — What is SAP Document AI?"
    url: "https://help.sap.com/docs/document-information-extraction/document-information-extraction/what-is-document-information-extraction?locale=en-US"
  - title: "Supplier Invoice - OData V2"
    url: "https://help.sap.com/docs/SAP_S4HANA_CLOUD/bb9f1469daf04bd894ab2167f8132a1a/7bc52558ef790a02e10000000a44147b.html"
# ai-discovery-managed:start
primary_topic: "business-ai"
ai_sidecar: "/ai/pages/labs--business-ai--document-to-erp-ai.json"
entity_mentions:
  - "sap-integration"
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
    title: "ERP Agent Gateway Pilot — Safe AI Tool Access to Enterprise Systems"
    url: "/labs/business-ai/erp-agent-gateway/"
  - type: "related_topic"
    title: "Open Enterprise AI Research — ERP Evidence, Safety, and Readiness"
    url: "/labs/business-ai/open-research/"
  - type: "same_domain"
    title: "AI Governance and Data Boundaries — Ownership, Access, Action Risk and Validation"
    url: "/labs/business-ai/governance-data-boundaries/"
# ai-discovery-managed:end
---
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/business-ai/">Business AI</a></li><li><a href="/labs/business-ai/pilots/">Pilots</a></li><li aria-current="page">Document-to-ERP AI</li></ol>
</nav>

<div class="research-canvas">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Pilot 01 / documents → ERP</p>
      <h1>A document can be read correctly<br />and still produce the wrong transaction.</h1>
      <p>The difficult part of document automation is not extracting a supplier, quantity, date, or total. It is deciding what those values mean in the current business context, proving that the proposal is valid, and controlling the moment when ERP state changes.</p>
      <a class="research-canvas__button" href="#pilot-design">Follow the transaction boundary <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Document-to-ERP control chain">
      <p>Control chain</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Evidence</strong><small>What the document actually says</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Proposal</strong><small>What the system thinks it means</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Authority</strong><small>What may change ERP state</small></div>
      <em>Extraction confidence is evidence about reading. It is not permission to post.</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal aria-label="Problem statement">
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <div>
      <p><strong>The key separation:</strong> document evidence, business interpretation, and ERP execution are three different decisions.</p>
      <p>A model may read “100 EA” perfectly while the proposed material is blocked, the unit is invalid for that material, the supplier is ambiguous, the invoice already exists, or the accounting period is closed. Those are not OCR problems. They are enterprise-context problems.</p>
    </div>
  </section>

  <section class="research-canvas__inventory" id="pilot-design" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Reference flow</p>
      <h2>Turn the document into a proposal before you turn it into a transaction.</h2>
      <p>A useful pilot keeps uncertainty visible until the ERP boundary. The model reads and structures the document; deterministic checks compare the proposal with enterprise state; a person reviews material exceptions; only then does a narrow adapter call the target system.</p>
    </header>

    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Stage</th><th scope="col">What happens</th><th scope="col">What it must not claim</th></tr></thead>
        <tbody>
          <tr><th scope="row">1. Capture evidence</th><td>Keep the original file, document hash, page references, and extracted values. Normalize dates, amounts, units, and identifiers without losing where they came from.</td><td>That a well-read field is already valid business data.</td></tr>
          <tr><th scope="row">2. Build a proposal</th><td>Map the extracted values into a canonical business object such as a supplier-invoice proposal, sales-order request, or delivery confirmation.</td><td>That the model may invent a missing supplier, material, account, tax code, or organizational value.</td></tr>
          <tr><th scope="row">3. Validate in context</th><td>Compare the proposal with authoritative master data, referenced documents, current status, tolerances, duplicate checks, units, currencies, dates, and process rules.</td><td>That model confidence can replace ERP or business validation.</td></tr>
          <tr><th scope="row">4. Decide authority</th><td>Auto-accept low-risk cases only when policy permits it; otherwise present the evidence, mismatches, and proposed changes to a reviewer.</td><td>That every document needs the same approval path.</td></tr>
          <tr><th scope="row">5. Execute and reconcile</th><td>Use a narrow ERP interface, keep an idempotency key, capture the returned business document number or error, then verify the intended business state.</td><td>That an HTTP success or tool response is the business outcome.</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Concrete example</p>
      <h2>A supplier invoice shows why extraction and posting must stay separate.</h2>
      <p>Assume a PDF contains supplier reference <code>INV-1842</code>, a gross amount of EUR 11,900, two purchase-order references, and a tax amount. The extraction layer can identify those values. The transaction layer still has more work to do.</p>
    </header>
    <p>The proposal should resolve the invoicing party to an existing supplier, match the purchase-order references, compare quantities and values with the referenced purchasing history, normalize currency and tax data, and check whether the supplier reference has already been used. If one purchase-order item is already fully invoiced, that is a business exception even when every field in the PDF was read correctly.</p>
    <p>The reviewer should see the document evidence beside the proposed ERP values and the exact validation failures. The workflow should not ask a person to re-read the whole PDF merely because one line is uncertain. It should isolate the uncertainty: for example, “line 20 exceeds the remaining invoice quantity by 5 EA” or “two supplier records match the extracted name.”</p>
    <p>Only after the proposal is accepted does the adapter create or park the invoice. The returned ERP document number then becomes part of the audit trail, and the workflow verifies the resulting status instead of treating the API call itself as proof of success.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Authority boundary</p>
      <h2>Give each layer the job it is good at.</h2>
      <p>The design becomes easier to reason about when extraction, business validation, human judgment, and system execution do not compete for authority.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Model</h3><p>Read documents, normalize language, classify document type, propose structured values, and explain ambiguous evidence.</p></div>
      <div><h3>Rules and ERP state</h3><p>Check existence, status, units, organizational scope, tolerances, duplicate keys, reference documents, authorizations, and transaction preconditions.</p></div>
      <div><h3>Human</h3><p>Resolve business ambiguity, approve exceptions with material impact, and own policy decisions that cannot be reduced to a deterministic rule.</p></div>
    </div>
    <p class="ecg-caption">For the wider action-control model, see <a href="/labs/business-ai/erp-agent-gateway/">ERP Agent Gateway</a>. For ownership, access, data movement, and approval design, use <a href="/labs/business-ai/governance-data-boundaries/">Governance and Data Boundaries</a>.</p>
  </section>

  <section class="research-canvas__inventory" id="dataset" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Test data</p>
      <h2>Build the benchmark around business ambiguity, not pretty documents.</h2>
      <p>A clean invoice with obvious fields is useful as a baseline, but it does not test the part of the system that can create costly errors. The dataset should contain documents that are readable yet difficult to interpret correctly.</p>
    </header>
    <div class="research-canvas__table-wrap">
      <table>
        <thead><tr><th scope="col">Case family</th><th scope="col">What to vary</th><th scope="col">Expected behaviour</th></tr></thead>
        <tbody>
          <tr><th scope="row">Evidence noise</th><td>Scans, rotated pages, weak print, handwritten corrections, split tables, conflicting totals.</td><td>Extract what is supported; expose uncertainty instead of silently filling gaps.</td></tr>
          <tr><th scope="row">Master-data ambiguity</th><td>Similar supplier names, old material numbers, alternate units, incomplete addresses, duplicate references.</td><td>Resolve against authoritative data or escalate when the match is not unique.</td></tr>
          <tr><th scope="row">Process conflict</th><td>Closed periods, blocked suppliers, completed orders, exceeded quantities, invalid plants, stale prices.</td><td>Reject or route the proposal even when extraction quality is high.</td></tr>
          <tr><th scope="row">Retry and duplicate</th><td>Same file twice, timeout after posting, repeated workflow execution.</td><td>Do not create a second business transaction; reconcile the first result.</td></tr>
          <tr><th scope="row">Untrusted content</th><td>Instructions embedded in attachments or free text that try to alter system behaviour.</td><td>Treat document content as data, never as authority to change tools, policy, or approval rules.</td></tr>
        </tbody>
      </table>
    </div>
    <div class="research-canvas__boundary" aria-label="Dataset rule">
      <span class="material-symbols-outlined" aria-hidden="true">dataset</span>
      <div>
        <p><strong>Start synthetic.</strong> A public benchmark can model invoices, orders, confirmations, duplicates, and failure conditions without exposing customer documents.</p>
        <p><strong>Keep expected answers explicit.</strong> Each case should define the canonical proposal, expected validation result, required authority level, and expected final action.</p>
      </div>
    </div>
  </section>

  <section class="research-canvas__inventory" id="metrics" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evaluation</p>
      <h2>Measure the whole decision chain.</h2>
      <p>Field accuracy matters, but it can hide a weak system. A pilot is useful only if it can read the document, produce the right proposal, stop unsafe cases, and complete accepted cases with a traceable business result.</p>
    </header>
    <div class="ecg-decision-columns">
      <div><h3>Read correctly</h3><p>Measure required-field accuracy and evidence grounding separately for normal and difficult documents. Track missing, wrong, and unsupported values.</p></div>
      <div><h3>Decide correctly</h3><p>Measure business-valid proposal rate, duplicate detection, exception classification, human correction effort, and false approvals or false blocks.</p></div>
      <div><h3>Execute safely</h3><p>Measure unsafe-write rate, duplicate-write rate, successful reconciliation, recovery after timeouts, and audit completeness. For the pilot, any unsafe write is a release blocker.</p></div>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP implementation boundary</p>
      <h2>SAP already exposes both sides of this pattern: document extraction and controlled business APIs.</h2>
      <p>The useful architecture point is not to collapse them into one black box.</p>
    </header>
    <p><a href="https://help.sap.com/docs/document-information-extraction/document-information-extraction/what-is-document-information-extraction?locale=en-US" rel="nofollow noopener">SAP Document AI</a> is a document-information-extraction service with UI and API options for extracting information from business documents. Its output can feed the proposal layer, but the extracted structure still needs business validation before it becomes an ERP transaction.</p>
    <p>For one concrete SAP target, current SAP S/4HANA Cloud documentation for <a href="https://help.sap.com/docs/SAP_S4HANA_CLOUD/bb9f1469daf04bd894ab2167f8132a1a/7bc52558ef790a02e10000000a44147b.html" rel="nofollow noopener">Supplier Invoice - OData V2</a> documents creation of supplier invoices and preliminary states such as held or parked invoices, plus application checks for restricted values and authorizations. That makes “create immediately” only one possible execution policy. A pilot can deliberately stop at a proposal or preliminary ERP state until the required review is complete.</p>
    <p>The exact adapter depends on the process and landscape. An SAP implementation may use a released API or another supported interface; other ERP platforms have different contracts. Keep the canonical proposal and control model stable, then make the adapter responsible for target-specific semantics.</p>
  </section>

  <section class="research-canvas__boundary" data-reveal aria-label="Pilot outcome">
    <span class="material-symbols-outlined" aria-hidden="true">architecture</span>
    <div>
      <p><strong>A useful pilot output:</strong> a small canonical schema, synthetic benchmark, validation service, reviewer view, mock or real adapter, idempotency strategy, and evaluation report.</p>
      <p>The point is not to prove that AI can read a PDF. It is to prove that uncertain document evidence can cross into ERP without losing business rules, authority boundaries, or traceability.</p>
    </div>
  </section>

  <div class="research-canvas__support" data-reveal>
    {% include atlas/author-block.html %}
    {% include atlas/disclaimer.html %}
  </div>
</div>
