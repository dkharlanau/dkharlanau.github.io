---
layout: default
title: "Cloud and Industry Assurance — Enterprise Assurance"
description: "A practical guide to PCI DSS, TISAX, BSI C5, CSA STAR and ISO cloud controls for enterprise vendor and architecture decisions."
permalink: /labs/enterprise-assurance/cloud-industry-assurance/
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
  - ai-security
tags:
  - cloud-security
  - pci-dss
  - tisax
  - bsi-c5
  - csa-star
  - vendor-assurance
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/enterprise-assurance/">Enterprise Assurance</a></li><li aria-current="page">Cloud and Industry Assurance</li></ol>
</nav>

<div class="research-canvas context-graph">
  <header class="research-canvas__hero" data-reveal>
    <div class="research-canvas__hero-copy">
      <p class="research-canvas__eyebrow">Cloud and industry / specific evidence</p>
      <h1>Choose assurance from the risk, not from the logo.</h1>
      <p>A general security certificate may be useful, but it does not answer every cloud or industry question. Payment data, automotive information and cloud services each bring their own scope rules, control models and forms of evidence.</p>
      <a class="research-canvas__button" href="#sector-map">See the assurance routes <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Cloud and industry assurance summary">
      <p>Decision path</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Risk</strong><small>What are we trying to prove?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Scope</strong><small>Which service and data are in scope?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Evidence</strong><small>What kind of assessment exists?</small></div>
      <em>Reviewed 23 Sep 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">filter_alt</span>
    <p><strong>The useful distinction is not “compliant or not”.</strong> We need to know which risk the scheme addresses, which service boundary it covers, how the evidence was produced, and which controls still belong to the customer.</p>
  </section>

  <section class="research-canvas__inventory" id="sector-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Five routes</p>
      <h2>Different schemes answer different assurance questions.</h2>
      <p>They can complement one another, but they are not interchangeable. A payment-security standard, an automotive assessment and a cloud-control attestation prove different things.</p>
    </header>

    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">PCI</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Payment-card security</p>
          <h3>PCI DSS v4.0.1</h3>
          <p>PCI DSS applies to entities that store, process or transmit cardholder data or sensitive authentication data, and to environments that can affect the security of the cardholder data environment. Version 4.0.1 is the active PCI DSS version; version 4.0 was retired on 31 December 2024.</p>
          <p>For an SAP-connected payment flow, the important work is scope. We trace where card data can appear, whether tokenization or redirect patterns keep SAP components outside the cardholder data environment, which integrations can affect that environment, and who operates the security controls.</p>
          <p>A payment provider's PCI evidence does not automatically make the surrounding ERP process compliant. Customer architecture, access, logging, network boundaries and operating practices still matter.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">TISAX</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Automotive information security</p>
          <h3>TISAX</h3>
          <p>TISAX provides a common assessment and exchange model for information security in automotive relationships. It uses the VDA Information Security Assessment catalogue and an ENX-governed process for assessment and result exchange.</p>
          <p>The version transition matters in 2026. ISA2027 has been published, but it becomes the basis for TISAX assessments ordered from 1 January 2027. Existing labels keep their validity, and assessments already started under ISA 6 follow the ENX transition rules.</p>
          <p>For a supplier or service provider, we therefore check more than the existence of a TISAX label. We match the participant, assessment scope, locations, assessment objectives and the information actually exchanged with the OEM or supplier network.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">C5</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud control evidence</p>
          <h3>BSI C5</h3>
          <p>The German Federal Office for Information Security (BSI) publishes the C5 criteria for cloud services, but a C5 report is not a BSI product certificate. Independent auditors perform the attestation engagement against the criteria.</p>
          <p>BSI distinguishes Type 1 and Type 2 reporting. Type 1 examines the description, implementation and design of controls at a point in time. Type 2 adds testing of operating effectiveness over a period, which makes it the stronger basis when we want evidence that controls actually operated.</p>
          <p>The report still needs to match the cloud service we use. We read the system description, criteria, auditor results, exceptions, subservice organizations and customer responsibilities instead of reducing the decision to “C5 compliant”.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">STAR</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud transparency and assurance</p>
          <h3>CSA STAR</h3>
          <p>CSA STAR uses the Cloud Controls Matrix as a common cloud-security frame. Level 1 is a provider self-assessment published in the STAR Registry. It is useful for transparency and early comparison, but it is not independent assurance.</p>
          <p>Level 2 adds third-party assessment. STAR Certification combines ISO/IEC 27001 with the Cloud Controls Matrix; STAR Attestation extends a SOC 2 engagement with the Cloud Controls Matrix. The registry shows which route and version applies to a specific provider or service.</p>
          <p>The practical value is comparability. We can use one cloud-control model to ask better questions across providers, while still checking the exact certification or attestation scope.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">ISO</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud-specific control guidance</p>
          <h3>ISO/IEC 27017:2026 and ISO/IEC 27018:2025</h3>
          <p>ISO/IEC 27017:2026 builds on ISO/IEC 27002 with cloud-specific security guidance and controls for both cloud service customers and providers. It applies across public, private and hybrid cloud models.</p>
          <p>ISO/IEC 27018:2025 focuses on protecting personally identifiable information when a public cloud provider acts as a PII processor. It complements an ISO/IEC 27001-based information security management system; it does not replace privacy law, contracts or customer-side data governance.</p>
          <p>These standards are especially useful for clarifying shared responsibility. They help us ask who should operate a control, but the answer must still be mapped to the actual service, contract, tenant configuration and data flow.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence shape</p>
      <h2>The assurance method matters as much as the framework name.</h2>
      <p>Two providers may mention the same framework while offering very different evidence. Before comparing them, normalize what you actually received.</p>
    </header>

    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>SELF</span><strong>Self-assessment</strong><h3>The provider describes its own control position.</h3><p>Useful for transparency and screening. The customer still needs to decide how much independent evidence the risk requires.</p></article>
      <article class="ecg-memory-card"><span>CERT</span><strong>Certification</strong><h3>A certification body confirms conformity within a defined scope.</h3><p>Read the certified entity, services, locations, standard edition and validity rather than relying on the logo.</p></article>
      <article class="ecg-memory-card"><span>ATTEST</span><strong>Independent attestation</strong><h3>An auditor reports against stated criteria and controls.</h3><p>For Type 2 engagements, operating-effectiveness testing can show whether controls worked over the assessment period.</p></article>
      <article class="ecg-memory-card"><span>TECH</span><strong>Technical evidence</strong><h3>Tests and operational records answer questions above frameworks alone.</h3><p>Penetration tests, recovery exercises, configuration evidence, vulnerability results and logs may be needed when the decision depends on technical behavior.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Do not stack badges blindly.</strong> ISO/IEC 27001, SOC 2, C5 and STAR can complement one another, but four artifacts with the wrong service boundary can still leave the main risk unproven.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP connection</p>
      <h2>For SAP cloud services, start with the exact offering.</h2>
      <p>SAP's Trust Center portfolio includes schemes such as BSI C5, CSA STAR, PCI DSS, TISAX, ISO/IEC 27017 and ISO/IEC 27018. Coverage is not uniform across every SAP product, entity, region or period.</p>
    </header>

    <ol class="research-canvas__steps">
      <li><span>01</span><strong>Identify the service</strong><p>Use the SAP Compliance Finder for the product or cloud service that is actually in scope, not the SAP brand in general.</p></li>
      <li><span>02</span><strong>Match the compliance entity</strong><p>Confirm that the document covers the SAP entity, service boundary and region relevant to the architecture.</p></li>
      <li><span>03</span><strong>Match the date</strong><p>Certificates, attestations and assessment reports are time-bound. Record the issue date or assessment period relied on for the decision.</p></li>
      <li><span>04</span><strong>Map the customer side</strong><p>Provider evidence does not prove customer role design, integrations, configuration, business approvals, data handling or operational monitoring. Those controls need their own owners and evidence.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Questions for review</p>
      <h2>Can you explain the boundary without the badge?</h2>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q1</div><div class="ecg-determination-card__copy"><h3>Why is a provider's PCI DSS evidence not enough for an SAP payment process?</h3><p>Because PCI scope follows the card-data environment and systems that can affect its security. Customer integrations, access, logging, storage and network design may remain in scope.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q2</div><div class="ecg-determination-card__copy"><h3>What does a C5 Type 2 report add over Type 1?</h3><p>Type 2 adds testing of operating effectiveness over a period. Type 1 focuses on description, implementation and control design at a point in time.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q3</div><div class="ecg-determination-card__copy"><h3>What is the difference between STAR Level 1 and Level 2?</h3><p>Level 1 is provider self-assessment and transparency. Level 2 uses third-party certification or attestation built around the Cloud Controls Matrix.</p></div></article>
      <article class="ecg-determination-card"><div class="ecg-determination-card__index">Q4</div><div class="ecg-determination-card__copy"><h3>Why do ISO/IEC 27017 and 27018 not settle the whole cloud-risk decision?</h3><p>They provide cloud-security and privacy guidance, but the real control boundary still depends on the service, contract, configuration, data flow and customer responsibilities.</p></div></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Related assurance work</p>
      <h2>Keep the scheme in its proper layer.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-assurance/service-organization-reports/"><span>SOC</span><strong>Service-organization reports</strong><small>Understand SOC 1, SOC 2, SOC 3 and ISAE 3402 evidence before relying on an attestation report.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/iso-management-systems/"><span>ISO</span><strong>ISO management systems</strong><small>Use the management-system guide for ISO/IEC 27001, ISO 22301, ISO/IEC 42001 and related organizational standards.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>VENDOR</span><strong>Vendor due diligence</strong><small>Turn the assurance artifact into a scoped risk and procurement decision.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Official sources</p>
      <h2>Use the scheme owner for current requirements.</h2>
    </header>
    <ul>
      <li><a href="https://blog.pcisecuritystandards.org/just-published-pci-dss-v4-0-1" rel="noopener">PCI Security Standards Council — PCI DSS v4.0.1 and v4.0 retirement</a></li>
      <li><a href="https://portal.enx.com/en-US/news/isa2027/" rel="noopener">ENX — ISA2027 transition for TISAX assessments</a></li>
      <li><a href="https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Publications/CloudComputing/ComplianceControlsCatalogue-Cloud_Computing-C5.pdf" rel="noopener">German BSI — Cloud Computing Compliance Criteria Catalogue (C5)</a></li>
      <li><a href="https://cloudsecurityalliance.org/star" rel="noopener">Cloud Security Alliance — STAR levels and assurance routes</a></li>
      <li><a href="https://www.iso.org/standard/27017" rel="noopener">ISO — ISO/IEC 27017:2026</a></li>
      <li><a href="https://www.iso.org/standard/27018" rel="noopener">ISO — ISO/IEC 27018:2025</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance/compliance-finder.html" rel="noopener">SAP Trust Center — Compliance Finder</a></li>
    </ul>
  </section>
</div>
