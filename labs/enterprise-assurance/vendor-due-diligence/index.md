---
layout: default
title: "Vendor Due Diligence — Enterprise Assurance"
description: "A practical evidence request pack for SAP, SaaS, cloud, AI, payment, automotive and outsourced-service vendor reviews."
permalink: /labs/enterprise-assurance/vendor-due-diligence/
status: draft
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-08-28
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
      <p class="research-canvas__eyebrow">Vendor review / evidence request pack</p>
      <h1>Turn compliance documents into a decision.</h1>
      <p>A strong vendor review does not collect every certificate available. It defines the business risk, requests evidence that matches that risk, checks the exact service boundary, and records what remains on the customer side.</p>
      <a class="research-canvas__button" href="#request-pack">Open the request pack <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Vendor due diligence summary">
      <p>Decision equation</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Risk</strong><small>Why do we need assurance?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Evidence</strong><small>What proves the control?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Owner</strong><small>Who accepts the remaining gap?</small></div>
      <em>Checked 28 Aug 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">rule</span>
    <p><strong>Lead principle:</strong> provider assurance reduces uncertainty. It does not transfer every enterprise responsibility to the provider.</p>
  </section>

  <section class="research-canvas__inventory" id="request-pack" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Ten checks</p>
      <h2>The evidence request pack.</h2>
      <p>Use this sequence for an RFP, architecture review, cloud onboarding, outsourcing decision, audit preparation, or contract renewal.</p>
    </header>
    <ol class="research-canvas__steps">
      <li><span>01</span><strong>State the risk</strong><p>Write the concrete reason for assurance: financial reporting, information security, privacy, continuity, AI governance, payment-card data, automotive information, service quality, or another business risk.</p></li>
      <li><span>02</span><strong>Name the exact service</strong><p>Record the product, service tier, cloud model, region, data center, subprocess, legal entity, and operating entity that your enterprise will actually use.</p></li>
      <li><span>03</span><strong>Request the right evidence</strong><p>Choose the artifact from the risk: ISO certificate, SOC or ISAE report, C5 attestation, PCI validation, TISAX result, CSA STAR entry, resilience evidence, technical test, contract, or a combination.</p></li>
      <li><span>04</span><strong>Check version and validity</strong><p>Confirm the current standard edition, certificate validity, report issue date, and assessment period. Reject outdated references that no longer represent the current framework.</p></li>
      <li><span>05</span><strong>Check scope match</strong><p>Does the evidence cover the exact service and entity? A valid document for the wrong service is still the wrong evidence.</p></li>
      <li><span>06</span><strong>Read exceptions and qualifications</strong><p>For auditor reports, review qualifications, test exceptions, failed controls, management responses, and whether the exception touches your key risk.</p></li>
      <li><span>07</span><strong>Map customer controls</strong><p>Identify complementary user controls, tenant configuration, access management, approvals, reconciliations, monitoring, retention, business roles, and other controls your enterprise must operate.</p></li>
      <li><span>08</span><strong>Map subservice organizations</strong><p>Find hosting providers, infrastructure providers, subprocessors, and other important third parties. Check whether they are included, excluded, or covered by separate evidence.</p></li>
      <li><span>09</span><strong>Close the time gap</strong><p>If a Type 2 report ended months ago, ask about material changes, incidents, control changes, and bridge evidence until a new report is available.</p></li>
      <li><span>10</span><strong>Record residual risk and owner</strong><p>State what is proven, what is not proven, the mitigation, the decision owner, and the date when evidence must be reviewed again.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence register</p>
      <h2>Keep one small record per assurance decision.</h2>
      <p>This is more useful than a shared folder full of PDFs with no decision context.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>RISK</span><strong>Risk and business process</strong><h3>What can go wrong and which process depends on the provider?</h3><p>Example: unauthorized access to employee data in a cloud HR integration.</p></article>
      <article class="ecg-memory-card"><span>REQ</span><strong>Required evidence</strong><h3>What evidence would be proportionate to this risk?</h3><p>Example: ISO/IEC 27001 scope, SOC 2 Type 2, privacy evidence, data-flow and access-control review.</p></article>
      <article class="ecg-memory-card"><span>GOT</span><strong>Provider evidence</strong><h3>What document or assessment did the provider actually supply?</h3><p>Record standard edition, report type, dates, entity, service and issuer or auditor.</p></article>
      <article class="ecg-memory-card"><span>MATCH</span><strong>Scope match</strong><h3>Does the supplied evidence cover our service, entity, location and period?</h3><p>Use a simple Yes / Partial / No result with a short reason.</p></article>
      <article class="ecg-memory-card"><span>GAP</span><strong>Proof gaps</strong><h3>What remains unsupported or outside the provider boundary?</h3><p>Examples: customer role design, a carved-out cloud subprocessor, report-period gap, or a missing recovery test.</p></article>
      <article class="ecg-memory-card"><span>OWN</span><strong>Owner and review date</strong><h3>Who owns mitigation or risk acceptance, and when does the evidence expire?</h3><p>Make assurance evidence part of lifecycle governance, not a one-time procurement exercise.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scenario packs</p>
      <h2>What would you request in a real enterprise system decision?</h2>
      <p>These are starting points, not universal checklists. Scope the final pack to the service, data, process, geography, regulation, and contract.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">S4</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">SAP cloud / financially significant ERP</p>
          <h3>SAP S/4HANA Cloud or RISE service supporting financial reporting</h3>
          <p><strong>Start with:</strong> relevant SOC 1 or ISAE 3402 Type 2 evidence for the exact service, plus ISO/IEC 27001 and continuity evidence where those risks are material.</p>
          <p><strong>Then map:</strong> customer SoD, business approvals, configuration, master data, interfaces, reconciliations, job monitoring, change controls, subservice organizations, and recovery responsibilities.</p>
          <p><strong>Decision test:</strong> can internal audit trace provider controls and customer controls into the same end-to-end financial process?</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">BTP</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Integration / PII</p>
          <h3>SAP BTP or another integration platform carrying personal data</h3>
          <p><strong>Start with:</strong> ISO/IEC 27001 and relevant SOC 2 assurance. Depending on the service and risk, add privacy and cloud-control evidence such as ISO/IEC 27701 or ISO/IEC 27018.</p>
          <p><strong>Then map:</strong> identity federation, technical users, destinations, secrets, certificates, API scopes, logging, retention, encryption, data residency, subprocessors, monitoring and recovery.</p>
          <p><strong>Decision test:</strong> does provider assurance match the exact runtime service, while customer configuration is covered by your own architecture and security evidence?</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">AI</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Enterprise AI</p>
          <h3>Joule, AI service, agent, or other enterprise AI capability</h3>
          <p><strong>Start with:</strong> ISO/IEC 42001 when it covers the provider or service, then add information-security and privacy assurance relevant to the architecture.</p>
          <p><strong>Do not stop there:</strong> review data sources, permissions, retention, model or service boundary, evaluations, failure classes, human oversight, tool permissions, logs, incident response and applicable legal obligations.</p>
          <p><strong>Regulatory boundary:</strong> the EU AI Act is regulation, not a certificate. A management-system certificate can support governance evidence but does not automatically establish regulatory compliance for one AI system.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">PCI</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Payments</p>
          <h3>Payment provider integrated with SAP sales or commerce</h3>
          <p><strong>Start with:</strong> current PCI DSS v4.0.1 validation for the provider and service where PCI scope applies.</p>
          <p><strong>Then map:</strong> tokenization, card-data flows, redirects or embedded components, logs, support access, integration payloads, storage, network scope and whether your own systems can affect cardholder-data security.</p>
          <p><strong>Decision test:</strong> has architecture minimized PCI scope instead of only collecting the provider’s compliance statement?</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">AUTO</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Automotive</p>
          <h3>Supplier or service provider exchanging sensitive OEM information</h3>
          <p><strong>Start with:</strong> TISAX evidence when required by the automotive relationship, with the correct participant, assessment objective, location and validity.</p>
          <p><strong>Then map:</strong> collaboration tools, SAP supplier processes, engineering integrations, prototype data, production information, identities, external users and subcontractors.</p>
          <p><strong>Decision test:</strong> does the TISAX scope match the sites and services that will actually handle the information?</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">C5</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">German cloud assurance</p>
          <h3>Cloud provider reviewed against BSI C5</h3>
          <p><strong>Start with:</strong> the C5 attestation report for the exact cloud service and prefer Type 2 operating-effectiveness evidence when ongoing reliance is important.</p>
          <p><strong>Then map:</strong> report criteria, exceptions, subservice organizations, customer responsibilities, service location, contracts, resilience and any sector-specific requirements.</p>
          <p><strong>Decision test:</strong> are you reviewing the independent attestation itself rather than a marketing statement that says “C5 compliant”?</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Red flags</p>
      <h2>Evidence that looks complete but is not decision-ready.</h2>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>OLD</span><strong>Outdated edition</strong><h3>The document names a withdrawn standard or old framework without a valid transition explanation.</h3><p>Example: presenting ISO 9001:2008 as a current certification basis.</p></article>
      <article class="ecg-memory-card"><span>ENTITY</span><strong>Wrong entity</strong><h3>The certificate belongs to a parent company, affiliate, or region that does not operate your service.</h3><p>A brand match is not a legal-entity match.</p></article>
      <article class="ecg-memory-card"><span>SCOPE</span><strong>Service missing from scope</strong><h3>The provider is certified, but the product or operation you buy is not clearly inside the certified boundary.</h3><p>Ask for the actual scope statement.</p></article>
      <article class="ecg-memory-card"><span>T1</span><strong>Type 1 used as operating proof</strong><h3>A point-in-time design report is presented as evidence that controls worked across the year.</h3><p>Ask for Type 2 where operating effectiveness matters.</p></article>
      <article class="ecg-memory-card"><span>GAP</span><strong>Report-period gap ignored</strong><h3>The Type 2 report ended long before the current reliance date.</h3><p>Request bridge evidence and material-change information.</p></article>
      <article class="ecg-memory-card"><span>EXC</span><strong>Exceptions not assessed</strong><h3>The report is filed as “passed” without checking control-test exceptions.</h3><p>Evaluate each relevant exception against your process and compensating controls.</p></article>
      <article class="ecg-memory-card"><span>CUEC</span><strong>Customer controls not owned</strong><h3>The report assumes customer controls that nobody in the enterprise has mapped or tested.</h3><p>Assign control owners before relying on the report.</p></article>
      <article class="ecg-memory-card"><span>SUB</span><strong>Carve-outs ignored</strong><h3>A critical subservice organization is excluded from the report and no additional evidence is reviewed.</h3><p>Trace the dependency until the material risk is covered.</p></article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP workflow</p>
      <h2>Use SAP Compliance Finder as a starting point, not the final decision.</h2>
      <p>SAP Compliance Finder lets you filter evidence by compliance offering, compliance entity, assessment period or issue date. That is useful because SAP’s assurance portfolio is broad and not every artifact applies to every service.</p>
    </header>
    <ol class="research-canvas__steps">
      <li><span>01</span><strong>Select the SAP offering</strong><p>Find the service your architecture actually uses.</p></li>
      <li><span>02</span><strong>Select the assurance family</strong><p>ISO, SOC, C5, PCI, TISAX or another relevant offering.</p></li>
      <li><span>03</span><strong>Match entity and period</strong><p>Confirm who operates the service and when the evidence applies.</p></li>
      <li><span>04</span><strong>Read the artifact</strong><p>Do not make the architecture decision from the search-result label alone.</p></li>
      <li><span>05</span><strong>Add customer evidence</strong><p>Close tenant, integration, business-process, data, identity, testing, operational and contractual controls on your side.</p></li>
    </ol>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">record_voice_over</span>
    <p><strong>60-second Lead answer:</strong> “For a critical vendor I define the business risk first, then request evidence that matches it. I verify the exact service, legal entity, edition and period, read exceptions and subservice boundaries, map customer controls, and record any proof gap. The final output is not a folder of certificates; it is a risk decision with an owner and a review date.”</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Continue</p>
      <h2>Go back to the evidence type when a document is unclear.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-assurance/iso-management-systems/"><span>ISO</span><strong>ISO management systems</strong><small>Interpret standard editions, certificate scope and what each management system can and cannot prove.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/service-organization-reports/"><span>SOC</span><strong>ISAE and SOC reports</strong><small>Read Type 1 and Type 2 reports, control exceptions, complementary user controls and subservice organizations.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/cloud-industry-assurance/"><span>SECTOR</span><strong>Cloud and industry assurance</strong><small>Understand PCI DSS, TISAX, BSI C5, CSA STAR and cloud-specific ISO guidance.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Official source desk</p>
      <h2>Validate current provider evidence before approval.</h2>
    </header>
    <ul>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance/compliance-finder.html" rel="noopener">SAP Compliance Finder</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance.html" rel="noopener">SAP Trust Center — certifications and compliance</a></li>
      <li><a href="https://www.iso.org/certification.html" rel="noopener">ISO — certification basics</a></li>
      <li><a href="https://www.iaasb.org/publications/staff-overview-international-standard-assurance-engagements-isae-3402-assurance-reports-controls" rel="noopener">IAASB — ISAE 3402</a></li>
      <li><a href="https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2/" rel="noopener">AICPA — SOC 2</a></li>
      <li><a href="https://www.pcisecuritystandards.org/document_library/?class=pcidss&amp;doc=pci_dss" rel="noopener">PCI Security Standards Council — PCI DSS</a></li>
      <li><a href="https://www.enx.com/en-US/TISAX/" rel="noopener">ENX — TISAX</a></li>
      <li><a href="https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html" rel="noopener">German BSI — C5</a></li>
    </ul>
  </section>
</div>
