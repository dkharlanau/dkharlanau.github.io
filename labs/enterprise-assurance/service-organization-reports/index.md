---
layout: default
title: "ISAE 3402 and SOC Reports — Enterprise Assurance"
description: "A practical guide to ISAE 3402, SOC 1, SOC 2 and SOC 3 reports, including report purpose, Type 1 vs Type 2, scope, exceptions and customer controls."
permalink: /labs/enterprise-assurance/service-organization-reports/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-23
last_reviewed: 2026-09-23
hide_global_cta: true
career_impact: mapped
career_skills:
  - lead-evidence
  - integration-deployment
  - integration-ownership
tags:
  - isae-3402
  - soc-1
  - soc-2
  - audit
  - internal-controls
  - vendor-assurance
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-assurance/">Enterprise Assurance</a></li><li aria-current="page">ISAE and SOC Reports</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Service organizations / auditor evidence</p>
      <h1>Start with the question the report is meant to answer.</h1>
      <p>SOC 1, SOC 2 and ISAE 3402 are often grouped together as “compliance reports”. That label is too broad to be useful. The first distinction is purpose: <strong>SOC 1 and ISAE 3402 address controls relevant to financial reporting, while SOC 2 addresses controls against the Trust Services Criteria.</strong></p>
      <a class="research-canvas__button" href="#report-map">Understand the reports <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Service organization reports summary">
      <p>Read in this order</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Purpose</strong><small>What question does the report answer?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Scope</strong><small>Which service, entity and period are covered?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Evidence</strong><small>What was designed, tested and excepted?</small></div>
      <em>Reviewed 23 Sep 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__inventory" id="report-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">The useful distinction</p>
      <h2>Similar report names, different assurance questions.</h2>
      <p>We get more value from these reports when we stop treating the label as the evidence. The report matters only if its purpose, system boundary and period match the risk we are trying to understand.</p>
    </header>

    <div class="ecg-memory-grid">
      <article class="ecg-memory-card">
        <span>SOC 1</span>
        <strong>Financial-reporting controls</strong>
        <h3>Controls at a service organization that are likely to be relevant to a user entity’s internal control over financial reporting.</h3>
        <p>Typical examples include payroll, transaction processing and other outsourced services that can affect financial statements or the controls around them.</p>
      </article>

      <article class="ecg-memory-card">
        <span>ISAE</span>
        <strong>ISAE 3402</strong>
        <h3>The international assurance standard for reporting on controls at a service organization when those controls are relevant to user entities and their auditors.</h3>
        <p>Its role is close to SOC 1 in the question it serves: how much assurance can users place on controls in an outsourced service that matters to financial reporting?</p>
      </article>

      <article class="ecg-memory-card">
        <span>SOC 2</span>
        <strong>Trust Services Criteria</strong>
        <h3>Controls relevant to security, availability, processing integrity, confidentiality or privacy.</h3>
        <p>This makes SOC 2 useful for cloud and technology services, but the report still has a specific system description, criteria, period and control boundary. “SOC 2” is not shorthand for every security question.</p>
      </article>

      <article class="ecg-memory-card">
        <span>SOC 3</span>
        <strong>General-use trust report</strong>
        <h3>A general-use report covering the same broad Trust Services Criteria area as SOC 2, without the same detailed control and test information.</h3>
        <p>It is useful as a public assurance signal. It is much less useful when due diligence depends on control descriptions, test procedures, exceptions and customer responsibilities.</p>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Type 1 and Type 2</p>
      <h2>Design at a date is different from operation over a period.</h2>
      <p>This distinction changes how much we can infer from the report. A point-in-time view can show that controls are described and designed for their stated purpose. Period-based evidence goes further by addressing how those controls operated during the covered period.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">T1</div>
        <div class="ecg-determination-card__copy">
          <h3>Type 1 — a specified date</h3>
          <p>Use it when the question is mainly whether the described control framework exists and is suitably designed at that point in time. It does not give the same evidence about consistent operation across months.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">T2</div>
        <div class="ecg-determination-card__copy">
          <h3>Type 2 — a specified period</h3>
          <p>Type 2 adds evidence about operating effectiveness over the defined period. For an enterprise relying on a provider’s controls in an ongoing process, that period and the related test results often matter more than the report title itself.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">How to read the report</p>
      <h2>The important evidence is inside the boundary.</h2>
      <p>A report can be valid and still be the wrong evidence for our use case. We therefore read it as a description of what the auditor examined — and just as importantly, what the auditor did not examine.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">01</div>
        <div class="ecg-determination-card__copy">
          <h3>Service, entity and system boundary</h3>
          <p>Confirm that the legal entity, service, locations and system description match what the enterprise actually uses. A strong report for another service does not provide assurance for yours.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">02</div>
        <div class="ecg-determination-card__copy">
          <h3>Period and reliance date</h3>
          <p>For period-based reports, record the start and end dates. If the report ends well before the date when we need to rely on it, the gap becomes a separate evidence question rather than an invisible extension of the audit period.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">03</div>
        <div class="ecg-determination-card__copy">
          <h3>Opinion, tests and exceptions</h3>
          <p>An unmodified opinion does not mean that every tested control had a perfect result. In a Type 2 report, the detailed test results and exceptions can be more useful to an architecture or control owner than the headline opinion.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">04</div>
        <div class="ecg-determination-card__copy">
          <h3>Customer responsibilities</h3>
          <p>Complementary user entity controls matter because the provider’s assurance may assume that the customer operates specific controls. Roles, approvals, configuration, reconciliations and monitoring can remain our responsibility even when the provider has a strong report.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">05</div>
        <div class="ecg-determination-card__copy">
          <h3>Subservice organizations</h3>
          <p>Important subcontractors may be included in the report or treated using a carve-out approach. If a material dependency sits outside the tested boundary, the assurance chain continues rather than ending at the first report.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP cloud context</p>
      <h2>Match the report to the SAP service you actually use.</h2>
      <p>SAP publishes certifications, attestations and SOC reports through its Trust Center and makes entitled compliance documents available through SAP for Me. The current Compliance Documents Finder supports filters such as compliance offering, compliance entity and assessment period or issue date.</p>
    </header>

    <p>That detail matters because an SAP brand name is not a control boundary. A report can apply to one cloud service, entity or audit period without covering another. For financially significant services we may need financial-reporting assurance; for security and availability questions we may need different evidence. In either case, provider reports do not replace customer-side control design.</p>

    <p>For example, a hosted SAP service may have strong provider assurance while the customer still owns business roles, segregation of duties, approvals, master data, interface monitoring and reconciliations. The assurance report is one layer in the end-to-end control model, not the whole model.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Questions for review</p>
      <h2>Check whether the distinction is clear.</h2>
    </header>

    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>Q1</span><strong>Why is SOC 1 not a generic security report?</strong><h3>Because its purpose is controls relevant to user entities’ internal control over financial reporting.</h3><p>Security controls can appear where they support that purpose, but financial-reporting relevance defines the engagement.</p></article>
      <article class="ecg-memory-card"><span>Q2</span><strong>Why can a Type 2 report be more useful than Type 1?</strong><h3>It adds evidence about operating effectiveness across a defined period.</h3><p>That matters when the enterprise depends on the provider control over time rather than only at one date.</p></article>
      <article class="ecg-memory-card"><span>Q3</span><strong>What is the first thing to check in an SAP compliance report?</strong><h3>Whether the service, entity and period match the service you rely on.</h3><p>The report title is secondary to the actual scope.</p></article>
      <article class="ecg-memory-card"><span>Q4</span><strong>What remains ours after the provider supplies a strong report?</strong><h3>Any customer controls and business responsibilities outside the provider’s tested boundary.</h3><p>That can include roles, approvals, configuration, reconciliations, monitoring and controls assumed by the report.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Primary sources</p>
      <h2>Use the frameworks, not secondary summaries.</h2>
    </header>
    <ul>
      <li><a href="https://www.iaasb.org/publications/staff-overview-international-standard-assurance-engagements-isae-3402-assurance-reports-controls" rel="noopener">IAASB — ISAE 3402 staff overview</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-1" rel="noopener">AICPA &amp; CIMA — SOC 1</a></li>
      <li><a href="https://www.aicpa-cima.com/cpe-learning/publication/soc-2-reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-security-availability-processing-integrity-confidentiality-or-privacy" rel="noopener">AICPA &amp; CIMA — SOC 2 reporting guide</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3" rel="noopener">AICPA &amp; CIMA — SOC 3</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance.html" rel="noopener">SAP Trust Center — Certifications and Compliance</a></li>
      <li><a href="https://support.sap.com/content/s4m/help/portfolio/compdocsfind.html" rel="noopener">SAP for Me — Compliance Documents Finder</a></li>
    </ul>
  </section>
</div>
