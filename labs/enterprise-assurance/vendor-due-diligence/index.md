---
layout: default
title: "Vendor Due Diligence — Enterprise Assurance"
description: "A practical vendor-assurance guide for SAP, SaaS, cloud, AI and outsourced services: match business risk to evidence, service scope, customer controls and residual risk."
permalink: /labs/enterprise-assurance/vendor-due-diligence/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-23
last_reviewed: 2026-09-23
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-decision
  - lead-evidence
  - integration-ownership
tags:
  - vendor-due-diligence
  - vendor-risk
  - sap-cloud
  - assurance
  - procurement
  - architecture
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-assurance/">Enterprise Assurance</a></li><li aria-current="page">Vendor Due Diligence</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Vendor assurance / decision evidence</p>
      <h1>A certificate is evidence. The decision is still ours.</h1>
      <p>Vendor due diligence is useful when it connects a business risk to the exact service we intend to use, tests whether the supplied evidence really covers that service, and makes the remaining customer responsibilities visible. A folder of certificates cannot do that on its own.</p>
      <a class="research-canvas__button" href="#decision-flow">Follow the decision flow <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Vendor assurance decision model">
      <p>Decision chain</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Risk</strong><small>What can the service affect?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Proof</strong><small>What evidence covers it?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Gap</strong><small>What remains with us?</small></div>
      <em>Reviewed 23 Sep 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Provider assurance narrows uncertainty; it does not outsource accountability.</strong> Even strong independent evidence has a scope, a period and a boundary. Customer configuration, identities, integrations, data use, business controls and operational decisions can remain outside that boundary.</p>
  </section>

  <section class="research-canvas__inventory" id="decision-flow" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">From risk to evidence</p>
      <h2>Start with the business dependency, not the compliance catalogue.</h2>
      <p>The same vendor can require very different evidence for two services. A public information site, a payment component and a financially significant ERP service do not create the same risk simply because they carry the same company logo.</p>
    </header>

    <ol class="research-canvas__steps">
      <li><span>01</span><strong>Define the dependency</strong><p>Name the business process, data and operational outcome that depend on the vendor. This gives the review a reason: financial reporting, confidentiality, privacy, continuity, service delivery, AI governance or another concrete risk.</p></li>
      <li><span>02</span><strong>Fix the service boundary</strong><p>Record the actual product or service, contractual entity, deployment model, region and material subprocessors or subservice organizations. Evidence for the right vendor but the wrong service is still the wrong evidence.</p></li>
      <li><span>03</span><strong>Choose evidence that answers the risk</strong><p>A management-system certificate, a SOC or ISAE report, an industry attestation, a technical test, recovery evidence and contractual commitments answer different questions. Use the smallest combination that covers the material risks instead of requesting every document available.</p></li>
      <li><span>04</span><strong>Read the evidence, not its label</strong><p>Check the edition or framework, issuing or auditing party, entity, service scope, assessment period, exceptions, exclusions and dependencies. For reports, understand customer controls and how subservice organizations are treated.</p></li>
      <li><span>05</span><strong>Close the customer side</strong><p>Map the controls that remain with the enterprise: role design, approvals, tenant configuration, integrations, reconciliations, monitoring, data retention, recovery, change management and other responsibilities relevant to the service.</p></li>
      <li><span>06</span><strong>Record the residual decision</strong><p>State what the evidence supports, what it does not support, the mitigation or acceptance owner, and when the evidence must be reviewed again. This turns assurance into lifecycle governance rather than a procurement snapshot.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">What the main evidence families tell us</p>
      <h2>Do not make one artifact answer a question it was not designed to answer.</h2>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>ISO</span><strong>Management-system certification</strong><h3>How does the organization manage a defined area?</h3><p>Useful for quality, information security, continuity, service management, privacy or AI governance when the certificate scope matches the service. It does not prove every service-level control or customer configuration.</p></article>
      <article class="ecg-memory-card"><span>SOC / ISAE</span><strong>Service-organization reports</strong><h3>Which controls were described and tested for a defined service and period?</h3><p>Read the report type, system boundary, auditor opinion, test exceptions, complementary user controls and subservice treatment rather than treating “SOC” as a generic badge.</p></article>
      <article class="ecg-memory-card"><span>SECTOR</span><strong>Cloud and industry assurance</strong><h3>Does a sector or cloud-specific scheme apply to this service?</h3><p>PCI DSS, TISAX, BSI C5 and CSA STAR serve different purposes. Applicability comes from architecture, data, geography, customer requirements and regulation, not from a desire to collect more logos.</p></article>
      <article class="ecg-memory-card"><span>TECH</span><strong>Technical and operational evidence</strong><h3>Can the actual service meet the design and operating requirement?</h3><p>Architecture reviews, penetration testing, recovery exercises, service measurements, incident evidence and contract terms can answer questions that certification and assurance reports leave open.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP example</p>
      <h2>For an SAP cloud service, match the document to the service before reading the result.</h2>
      <p>SAP's Compliance Finder is useful because the assurance portfolio is broad. It lets us narrow documents by compliance offering, compliance entity and assessment period or issue date, with regional filtering where relevant. That helps locate evidence; it does not make the reliance decision for us.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">01</div>
        <div class="ecg-determination-card__copy">
          <h3>Identify the exact SAP service in the architecture.</h3>
          <p>“SAP cloud” is too broad. The evidence must correspond to the service, entity and region that support the process under review.</p>
        </div>
      </article>
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">02</div>
        <div class="ecg-determination-card__copy">
          <h3>Select evidence from the business risk.</h3>
          <p>A financially significant process may need controls assurance; an integration carrying personal data may put more weight on security and privacy; a critical operation may need additional continuity and recovery evidence.</p>
        </div>
      </article>
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">03</div>
        <div class="ecg-determination-card__copy">
          <h3>Join provider and customer controls into one process view.</h3>
          <p>Provider evidence can cover the service boundary while the enterprise still owns roles, approvals, interfaces, master data, reconciliations, tenant settings and parts of recovery. The decision is stronger when both sides are visible in the same control model.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">A small assurance record</p>
      <h2>Keep the conclusion with the evidence.</h2>
      <p>The useful record is not a PDF name. It is enough context for another reviewer to understand why the evidence was accepted and what still needs attention.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>RISK</span><strong>Business dependency</strong><h3>What process, data or outcome depends on the service?</h3></article>
      <article class="ecg-memory-card"><span>SCOPE</span><strong>Service boundary</strong><h3>Which service, entity, locations and period does the evidence cover?</h3></article>
      <article class="ecg-memory-card"><span>PROOF</span><strong>Evidence and finding</strong><h3>What was reviewed, and what does it actually support?</h3></article>
      <article class="ecg-memory-card"><span>GAP</span><strong>Customer responsibility</strong><h3>Which material controls or dependencies remain outside provider evidence?</h3></article>
      <article class="ecg-memory-card"><span>OWNER</span><strong>Decision and review date</strong><h3>Who owns mitigation or acceptance, and when must the evidence be revisited?</h3></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Go deeper</p>
      <h2>Use the evidence-specific page when the artifact itself needs interpretation.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-assurance/iso-management-systems/"><span>ISO</span><strong>ISO management systems</strong><small>Interpret management-system scope, editions and what certification can and cannot establish.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/service-organization-reports/"><span>SOC</span><strong>SOC and ISAE reports</strong><small>Read Type 1 and Type 2 reports, periods, exceptions, complementary user controls and subservice organizations.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/cloud-industry-assurance/"><span>SECTOR</span><strong>Cloud and industry assurance</strong><small>Understand PCI DSS, TISAX, BSI C5, CSA STAR and cloud-specific ISO guidance.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Validate current evidence before relying on it.</h2>
    </header>
    <ul>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance/compliance-finder.html" rel="noopener">SAP Compliance Finder</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance.html" rel="noopener">SAP Trust Center — certifications and compliance</a></li>
      <li><a href="https://www.iso.org/certification.html" rel="noopener">ISO — certification and conformity assessment</a></li>
      <li><a href="https://www.iaasb.org/publications/staff-overview-international-standard-assurance-engagements-isae-3402-assurance-reports-controls" rel="noopener">IAASB — ISAE 3402</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2/" rel="noopener">AICPA-CIMA — SOC 2</a></li>
    </ul>
  </section>
</div>