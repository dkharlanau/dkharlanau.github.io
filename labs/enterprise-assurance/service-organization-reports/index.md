---
layout: default
title: "ISAE 3402 and SOC Reports — Enterprise Assurance"
description: "A practical guide to ISAE 3402, SOC 1, SOC 2 and SOC 3 reports, including Type 1 vs Type 2, control exceptions, user controls and subservice organizations."
permalink: /labs/enterprise-assurance/service-organization-reports/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-28
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
      <h1>Ask what the report is designed to prove.</h1>
      <p>ISAE 3402, SOC 1, and SOC 2 are often placed in one “compliance” folder. That hides the main difference: <strong>SOC 1 and ISAE 3402 focus on controls relevant to financial reporting, while SOC 2 focuses on trust services criteria such as security.</strong></p>
      <a class="research-canvas__button" href="#report-map">Compare the reports <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Service organization reports summary">
      <p>Three questions</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Purpose</strong><small>Financial controls or system trust?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Type</strong><small>Point in time or period?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Boundary</strong><small>Who and what is included?</small></div>
      <em>Checked 28 Aug 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">account_balance</span>
    <p><strong>Simple rule:</strong> if an outsourced service can affect your internal control over financial reporting, think ISAE 3402 or SOC 1. If you need assurance about security and related system criteria, think SOC 2. The exact report still needs a scope check.</p>
  </section>

  <section class="research-canvas__inventory" id="report-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Report map</p>
      <h2>Four names, different audiences and questions.</h2>
      <p>The label is only the start. The auditor opinion, system description, criteria, period, test results, and exceptions carry the real evidence.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card">
        <span>ISAE</span>
        <strong>ISAE 3402</strong>
        <h3>Assurance on controls at a service organization that are likely to be relevant to user entities’ internal control over financial reporting.</h3>
        <p>Common in international outsourcing and cloud/service-provider assurance. It is issued by a service auditor under the international assurance standard.</p>
      </article>
      <article class="ecg-memory-card">
        <span>SOC 1</span>
        <strong>SOC 1</strong>
        <h3>The US service-organization reporting route for controls relevant to user entities’ internal control over financial reporting.</h3>
        <p>Think payroll processing, transaction processing, financially significant hosting or services, and other outsourced activities that can affect financial reporting controls.</p>
      </article>
      <article class="ecg-memory-card">
        <span>SOC 2</span>
        <strong>SOC 2</strong>
        <h3>Controls relevant to security and, when included, availability, processing integrity, confidentiality, and privacy.</h3>
        <p>Useful for technology and cloud services. Security is always central; the other trust services categories depend on the scope of the engagement.</p>
      </article>
      <article class="ecg-memory-card">
        <span>SOC 3</span>
        <strong>SOC 3</strong>
        <h3>A general-use report based on the same trust services area as SOC 2, but without the detailed control and test information of a SOC 2 report.</h3>
        <p>Useful as a public trust signal. It is usually not enough for detailed enterprise due diligence when you need to review controls, tests, and exceptions.</p>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Type 1 vs Type 2</p>
      <h2>Design at a date is not the same as operation over time.</h2>
      <p>This distinction is one of the most useful assurance concepts for enterprise architecture and vendor reviews.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">T1</div>
        <div class="ecg-determination-card__copy">
          <h3>Type 1 — specified date</h3>
          <p>The report addresses the service organization’s system description and whether controls were suitably designed at a specified date. It can show that a control framework exists and is designed for the stated objective.</p>
          <p><strong>Boundary:</strong> it does not provide the same evidence that controls operated effectively across a period.</p>
        </div>
      </article>
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">T2</div>
        <div class="ecg-determination-card__copy">
          <h3>Type 2 — specified period</h3>
          <p>The report adds assurance over operating effectiveness for a defined period and includes the service auditor’s tests and results.</p>
          <p><strong>Lead use:</strong> when you want evidence that controls were not only designed but actually operated, Type 2 is normally more useful.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Report anatomy</p>
      <h2>Do not stop at the auditor opinion.</h2>
      <p>Read the report as a control boundary. The following items often change the decision.</p>
    </header>
    <ol class="research-canvas__steps">
      <li><span>01</span><strong>Service and legal entity</strong><p>Confirm the exact service organization, product or system, legal entity, locations, and service boundary covered by the report.</p></li>
      <li><span>02</span><strong>Report period</strong><p>For Type 2, record the start and end date. Check whether the period reaches the date when your enterprise will rely on the report.</p></li>
      <li><span>03</span><strong>Auditor opinion</strong><p>Read whether the opinion is unmodified or qualified and understand the reason for any qualification.</p></li>
      <li><span>04</span><strong>Control objectives or criteria</strong><p>Check what the controls are intended to achieve. A report can be valid but still not cover the control objective you need.</p></li>
      <li><span>05</span><strong>Tests and exceptions</strong><p>For Type 2, read what the auditor tested, the test result, and every exception relevant to your risk. “One exception” can be important if it affects a key control.</p></li>
      <li><span>06</span><strong>Complementary user entity controls</strong><p>These are controls the provider assumes the customer will operate. If your enterprise does not implement them, the provider report does not close the control gap.</p></li>
      <li><span>07</span><strong>Subservice organizations</strong><p>Check whether important subcontractors are included in the report or carved out. A carve-out can move part of the evidence problem to another provider.</p></li>
      <li><span>08</span><strong>Changes after the period</strong><p>If there is a time gap between the report end date and your reliance date, ask what materially changed and whether a bridge letter or updated evidence is available.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP and ERP scenarios</p>
      <h2>Choose the report from the business consequence.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>FI</span><strong>Cloud service supporting financial reporting</strong><small>Ask whether a SOC 1 or ISAE 3402 Type 2 report covers the exact service and period. Then map provider controls and customer controls to your financial-control design.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>SEC</span><strong>SaaS platform handling sensitive enterprise data</strong><small>SOC 2 can provide detailed security assurance. Check criteria in scope, exceptions, customer controls, subservice organizations, and the exact system boundary.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>PAY</span><strong>Outsourced payroll or transaction processing</strong><small>If the service affects financial reporting, SOC 1 or ISAE 3402 may be directly relevant. Privacy and security risks can still require additional evidence.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>BTP</span><strong>Integration platform</strong><small>SOC 2 can support security assurance, but architecture review must still cover identities, destinations, secrets, APIs, logging, data flows, customer configuration, and recovery.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP Trust Center example</p>
      <h2>SAP separates SOC 1 and SOC 2 for a reason.</h2>
      <p>SAP Trust Center describes SOC 1 as assurance over controls relevant to customers’ internal control over financial reporting and SOC 2 as assurance using trust services criteria. SAP also provides a Compliance Finder so customers can search by offering, compliance entity, and assessment period or issue date.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>01</span><strong>Do not generalize across SAP</strong><h3>A report for one SAP cloud offering does not automatically cover every SAP product or service.</h3><p>Use the compliance offering and entity filters and read the report scope.</p></article>
      <article class="ecg-memory-card"><span>02</span><strong>Do not generalize across time</strong><h3>A valid Type 2 report has a defined period.</h3><p>If your reliance date falls later, review changes and bridge evidence rather than pretending the period is open-ended.</p></article>
      <article class="ecg-memory-card"><span>03</span><strong>Do not outsource your controls</strong><h3>Customer responsibilities remain customer responsibilities.</h3><p>Roles, approvals, segregation of duties, interface controls, data quality, monitoring, and business reconciliation can remain on your side even when the provider has a strong report.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
    <p><strong>Lead answer pattern:</strong> “I first decide whether I need financial-reporting assurance or broader system trust. Then I prefer period-based operating evidence where the risk requires it, read exceptions and subservice boundaries, and map complementary user controls to our own control owners.”</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Common traps</p>
      <h2>Five weak shortcuts.</h2>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">01</div><div class="ecg-determination-card__copy"><h3>“SOC 1 is a security certificate.”</h3><p>No. Its purpose is controls relevant to user entities’ internal control over financial reporting.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">02</div><div class="ecg-determination-card__copy"><h3>“SOC 2 covers everything.”</h3><p>No. Read the trust services criteria actually included, system boundary, period, exceptions, and customer responsibilities.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">03</div><div class="ecg-determination-card__copy"><h3>“Type 1 proves the controls worked all year.”</h3><p>No. Type 1 is a point-in-time design view. Type 2 provides operating-effectiveness evidence over a period.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">04</div><div class="ecg-determination-card__copy"><h3>“No qualified opinion means no relevant exceptions.”</h3><p>Not necessarily. Read the detailed test results and evaluate exceptions against your own risk and control dependencies.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">05</div><div class="ecg-determination-card__copy"><h3>“The provider controls the full process.”</h3><p>Complementary user controls and carved-out subservice organizations can leave important control responsibilities outside the provider’s tested boundary.</p></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Official source desk</p>
      <h2>Read the reporting frameworks and current provider scope.</h2>
    </header>
    <ul>
      <li><a href="https://www.iaasb.org/publications/staff-overview-international-standard-assurance-engagements-isae-3402-assurance-reports-controls" rel="noopener">IAASB — ISAE 3402 staff overview</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-1" rel="noopener">AICPA — SOC 1</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2/" rel="noopener">AICPA — SOC 2</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-3" rel="noopener">AICPA — SOC 3</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance.html" rel="noopener">SAP Trust Center — certifications and compliance</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance/compliance-finder.html" rel="noopener">SAP Compliance Finder</a></li>
    </ul>
  </section>
</div>
