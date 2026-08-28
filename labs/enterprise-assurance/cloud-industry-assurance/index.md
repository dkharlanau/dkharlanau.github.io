---
layout: default
title: "Cloud and Industry Assurance — Enterprise Assurance"
description: "A practical guide to PCI DSS, TISAX, BSI C5, CSA STAR, ISO cloud controls, operational management standards, automotive assurance and industrial cybersecurity."
permalink: /labs/enterprise-assurance/cloud-industry-assurance/
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
      <h1>Generic assurance is not always enough.</h1>
      <p>Payment data, automotive information, public cloud services, industrial environments, and regulated operations can require evidence that goes deeper than a general quality or security certificate.</p>
      <a class="research-canvas__button" href="#sector-map">Open the sector map <span class="material-symbols-outlined" aria-hidden="true">arrow_downward</span></a>
    </div>
    <div class="research-canvas__signal" aria-label="Cloud and industry assurance summary">
      <p>Decision path</p>
      <div class="research-canvas__signal-line"><span>01</span><strong>Data</strong><small>What information is exposed?</small></div>
      <div class="research-canvas__signal-line"><span>02</span><strong>Sector</strong><small>Which industry rules matter?</small></div>
      <div class="research-canvas__signal-line"><span>03</span><strong>Evidence</strong><small>What assessment is accepted?</small></div>
      <em>Checked 28 Aug 2026 · draft learning material</em>
    </div>
  </header>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">filter_alt</span>
    <p><strong>Simple rule:</strong> add sector-specific evidence when the business risk is sector-specific. More badges do not automatically mean more assurance.</p>
  </section>

  <section class="research-canvas__inventory" id="sector-map" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Core schemes</p>
      <h2>Five assurance routes worth knowing.</h2>
      <p>Each route exists because a particular risk, industry, or cloud context needs a more specific control model.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">PCI</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Payment card security</p>
          <h3>PCI DSS v4.0.1</h3>
          <p><strong>Question:</strong> does the environment store, process, transmit cardholder data, or otherwise affect the security of the cardholder data environment?</p>
          <p><strong>Use:</strong> payment platforms, e-commerce, payment integrations, call centers, infrastructure, service providers, and SAP-connected payment processes where PCI scope applies.</p>
          <p><strong>Current status:</strong> PCI DSS v4.0.1 is the active version in 2026. PCI DSS v4.0 was retired at the end of 2024.</p>
          <p><strong>Do not assume:</strong> that an ERP system becomes “PCI compliant” because a payment service provider is compliant. Scope, segmentation, integrations, logs, access, storage, and customer responsibilities still matter.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">TISAX</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Automotive information security</p>
          <h3>TISAX</h3>
          <p><strong>Question:</strong> can an automotive partner demonstrate an accepted information-security assessment level for the information it exchanges with OEMs and suppliers?</p>
          <p><strong>Use:</strong> prototypes, development information, personal data, production information, supplier collaboration, engineering services, and other sensitive automotive relationships.</p>
          <p><strong>How it works:</strong> TISAX uses the VDA Information Security Assessment and an ENX-governed assessment and result-exchange model.</p>
          <p><strong>2026 note:</strong> ISA 6.0.1 remains relevant for assessments in 2026. ENX has announced the ISA 2027 transition for assessments ordered from 2027, so version and assessment timing should be checked.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">C5</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud assurance</p>
          <h3>BSI C5</h3>
          <p><strong>Question:</strong> what evidence exists that a cloud provider’s controls meet the German BSI cloud security criteria?</p>
          <p><strong>Use:</strong> cloud-provider due diligence, especially in German and European enterprise or regulated contexts where C5 is requested or expected.</p>
          <p><strong>Important:</strong> C5 is based on an attestation engagement by independent auditors. It is not a “BSI certificate”.</p>
          <p><strong>Type 1 vs Type 2:</strong> a Type 1 report addresses control design at a date. A Type 2 report adds operating effectiveness over a period and gives stronger operational evidence. BSI guidance treats Type 2 as the more informative route for ongoing assurance.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">STAR</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud transparency</p>
          <h3>CSA STAR</h3>
          <p><strong>Question:</strong> how does a cloud provider demonstrate controls against the Cloud Security Alliance Cloud Controls Matrix?</p>
          <p><strong>Level 1:</strong> self-assessment and public transparency. Useful for discovery, but it is not independent assurance.</p>
          <p><strong>Level 2:</strong> third-party assurance. STAR Certification combines ISO/IEC 27001 with the CCM; STAR Attestation uses a SOC 2 engagement with the CCM.</p>
          <p><strong>AI extension:</strong> CSA has also introduced STAR for AI assurance routes. Treat this as an additional cloud/AI control layer, not a replacement for use-case evaluation or regulation.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">ISO</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Cloud control guidance</p>
          <h3>ISO/IEC 27017:2026 and ISO/IEC 27018:2025</h3>
          <p><strong>27017:</strong> adds cloud-specific information-security controls and guidance for cloud service providers and cloud service customers.</p>
          <p><strong>27018:</strong> adds guidance for protecting personally identifiable information when a public cloud provider acts as a PII processor.</p>
          <p><strong>Use:</strong> deepen an ISO/IEC 27001-based cloud assessment and clarify shared-control responsibilities.</p>
          <p><strong>Boundary:</strong> these are not substitutes for checking the provider’s exact service scope, customer configuration, contracts, data flows, access design, or regulatory obligations.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Scenario routing</p>
      <h2>Start from the information and business context.</h2>
    </header>
    <div class="research-route-list">
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>CARD</span><strong>SAP order-to-cash with card payments</strong><small>Identify the cardholder data environment and connected systems first. Use PCI DSS evidence for the components and providers inside or affecting that scope.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>AUTO</span><strong>Automotive supplier collaboration</strong><small>When OEM requirements include TISAX, verify the assessment objective, participant, location, scope, label validity, and the information being exchanged.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>DE</span><strong>Cloud service for a German enterprise</strong><small>C5 can provide detailed cloud assurance. Combine it with service-specific contracts, architecture, resilience, data-protection, and customer-control evidence.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
      <a href="/labs/enterprise-assurance/vendor-due-diligence/"><span>CLOUD</span><strong>Multi-cloud supplier comparison</strong><small>CSA STAR can add a common cloud-control view. Distinguish Level 1 self-assessment from Level 2 independent assurance before comparing providers.</small><i class="material-symbols-outlined" aria-hidden="true">arrow_forward</i></a>
    </div>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Evidence strength</p>
      <h2>The same logo can hide different levels of evidence.</h2>
      <p>Before comparing vendors, normalize what each provider has actually supplied.</p>
    </header>
    <div class="ecg-memory-grid">
      <article class="ecg-memory-card"><span>SELF</span><strong>Self-assessment</strong><h3>The provider describes its own control position.</h3><p>Useful for transparency and early screening. It is weaker than independent assurance.</p></article>
      <article class="ecg-memory-card"><span>CERT</span><strong>Certification</strong><h3>An independent certification body confirms conformity to a certifiable standard within a defined scope.</h3><p>Good management-system evidence, but still read the certificate boundary.</p></article>
      <article class="ecg-memory-card"><span>AUDIT</span><strong>Independent attestation</strong><h3>An auditor reports on defined controls, criteria, tests, and often operating effectiveness.</h3><p>Can provide deeper evidence for a service boundary, especially in Type 2 engagements.</p></article>
      <article class="ecg-memory-card"><span>TEST</span><strong>Technical evidence</strong><h3>Penetration tests, vulnerability evidence, resilience tests, configurations, logs, or control samples answer technical questions a badge cannot.</h3><p>Use them when the decision needs proof below the management-system or assurance-report layer.</p></article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">warning</span>
    <p><strong>Do not stack badges blindly:</strong> ISO/IEC 27001 + SOC 2 + C5 + STAR may be useful for one provider, but the value comes from complementary scope and evidence. Four overlapping artifacts with the wrong service boundary can still leave the main risk unproven.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Beyond cloud and IT</p>
      <h2>A standard can drive ERP requirements without certifying the ERP system.</h2>
      <p>Enterprise systems also support environmental, safety, energy, anti-bribery, automotive, and industrial-control obligations. These standards often shape master data, approvals, evidence, traceability, workflows, reporting, and supplier requirements.</p>
    </header>
    <div class="ecg-determination-list">
      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">14001</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Environmental management</p>
          <h3>ISO 14001:2026</h3>
          <p><strong>Question:</strong> can the organization systematically manage environmental aspects, obligations, objectives, performance, and continual improvement?</p>
          <p><strong>System connection:</strong> SAP EHS, waste and emissions data, purchasing requirements, material data, plant processes, compliance tasks, environmental KPIs, and audit evidence can support the management system.</p>
          <p><strong>2026 change:</strong> ISO 14001:2026 was published in April 2026 and replaced ISO 14001:2015. This is another reason to check the edition rather than repeat an old certificate reference.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">45001</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Occupational health and safety</p>
          <h3>ISO 45001:2018</h3>
          <p><strong>Question:</strong> does the organization manage occupational health and safety risks through a structured management system?</p>
          <p><strong>System connection:</strong> incidents, hazards, risk assessments, training, permits, corrective actions, contractor data, and EHS workflows can become ERP or EHS-system requirements.</p>
          <p><strong>Version note:</strong> ISO 45001:2018 is still current on 28 August 2026, but a second edition is already at Draft International Standard stage. Treat the edition as a live transition topic.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">50001</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Energy management</p>
          <h3>ISO 50001:2018</h3>
          <p><strong>Question:</strong> can the organization systematically improve energy performance, including energy efficiency, use, and consumption?</p>
          <p><strong>System connection:</strong> meters, equipment, production volumes, energy baselines, energy-performance indicators, maintenance data, and analytics may need integration across ERP, manufacturing, IoT, and reporting platforms.</p>
          <p><strong>Boundary:</strong> the standard defines the management system. A dashboard alone is not an energy management system.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">37001</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Anti-bribery</p>
          <h3>ISO 37001:2025</h3>
          <p><strong>Question:</strong> can the organization prevent, detect, and respond to bribery through policies, due diligence, financial and non-financial controls, monitoring, and improvement?</p>
          <p><strong>System connection:</strong> supplier onboarding, third-party due diligence, approval limits, payments, gifts and benefits, conflicts, audit trails, purchasing controls, and exception workflows can support the anti-bribery control model.</p>
          <p><strong>Version check:</strong> ISO 37001:2025 replaced the 2016 edition.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">AUTO</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Automotive quality and product engineering</p>
          <h3>IATF 16949:2016, ISO/SAE 21434:2021, and ISO 26262:2018</h3>
          <p><strong>IATF 16949:</strong> automotive quality management and supplier-chain discipline. As of August 2026, the 2016 first edition remains published while IATF is actively preparing the second edition.</p>
          <p><strong>ISO/SAE 21434:</strong> cybersecurity engineering across the road-vehicle lifecycle. <strong>ISO 26262:</strong> functional safety for safety-related electrical and electronic vehicle systems.</p>
          <p><strong>System connection:</strong> SAP QM, PP, batch and serial traceability, change records, supplier quality, document control, complaints, production evidence, and integration with engineering systems can support required evidence. They do not make SAP itself “ISO 26262 certified”.</p>
        </div>
      </article>

      <article class="ecg-determination-card">
        <div class="ecg-determination-card__index">62443</div>
        <div class="ecg-determination-card__copy">
          <p class="research-canvas__eyebrow">Industrial and OT cybersecurity</p>
          <h3>IEC 62443 series</h3>
          <p><strong>Question:</strong> how should asset owners, service providers, product suppliers, and industrial automation components manage cybersecurity across industrial automation and control systems?</p>
          <p><strong>Useful parts:</strong> IEC 62443-2-1 covers asset-owner security programs, IEC 62443-2-4 covers IACS service providers, IEC 62443-4-1 covers secure product development lifecycle requirements, and IEC 62443-4-2 covers technical security requirements for components.</p>
          <p><strong>System connection:</strong> this becomes important when ERP, MES, integration platforms, maintenance systems, historians, plant connectivity, or remote services cross the IT/OT boundary.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="research-canvas__boundary" data-reveal>
    <span class="material-symbols-outlined" aria-hidden="true">factory</span>
    <p><strong>Lead distinction:</strong> ISO 14001, ISO 45001, ISO 50001, IATF 16949, ISO 26262, and similar frameworks can create system requirements and audit-evidence needs. That does not mean the ERP application itself receives the organization’s management-system certification.</p>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">SAP connection</p>
      <h2>Use the assurance scheme as one layer of the architecture decision.</h2>
      <p>SAP Trust Center currently exposes several cloud assurance schemes across its portfolio, including PCI DSS, TISAX, BSI C5, CSA STAR and cloud-related ISO standards. The presence of a scheme in the portfolio does not mean every SAP offering has the same assessment scope.</p>
    </header>
    <ol class="research-canvas__steps">
      <li><span>01</span><strong>Find the exact SAP offering</strong><p>Use SAP Compliance Finder rather than relying on a general SAP compliance page.</p></li>
      <li><span>02</span><strong>Find the compliance entity</strong><p>Check the legal or operational entity connected to the service.</p></li>
      <li><span>03</span><strong>Find the period or issue date</strong><p>Assurance evidence is time-bound. Record the period you are relying on.</p></li>
      <li><span>04</span><strong>Map customer responsibilities</strong><p>Connect provider assurance to your SAP roles, integrations, data, configuration, business controls, and operations.</p></li>
    </ol>
  </section>

  <section class="research-canvas__inventory" data-reveal>
    <header>
      <p class="research-canvas__eyebrow">Official source desk</p>
      <h2>Use the scheme owner for current requirements.</h2>
    </header>
    <ul>
      <li><a href="https://www.pcisecuritystandards.org/document_library/?class=pcidss&amp;doc=pci_dss" rel="noopener">PCI Security Standards Council — PCI DSS</a></li>
      <li><a href="https://www.enx.com/en-US/TISAX/" rel="noopener">ENX — TISAX</a></li>
      <li><a href="https://portal.enx.com/en-US/TISAX/isa/" rel="noopener">ENX — Information Security Assessment and transition information</a></li>
      <li><a href="https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html" rel="noopener">German BSI — C5</a></li>
      <li><a href="https://cloudsecurityalliance.org/star" rel="noopener">Cloud Security Alliance — STAR</a></li>
      <li><a href="https://www.iso.org/standard/76559.html" rel="noopener">ISO/IEC 27017:2026</a></li>
      <li><a href="https://www.iso.org/standard/76560.html" rel="noopener">ISO/IEC 27018:2025</a></li>
      <li><a href="https://www.iso.org/standard/14001" rel="noopener">ISO 14001:2026</a></li>
      <li><a href="https://www.iso.org/standard/63787.html" rel="noopener">ISO 45001:2018</a></li>
      <li><a href="https://www.iso.org/standard/69426.html" rel="noopener">ISO 50001:2018</a></li>
      <li><a href="https://www.iso.org/standard/37001" rel="noopener">ISO 37001:2025</a></li>
      <li><a href="https://www.iatfglobaloversight.org/iatf-publications/" rel="noopener">IATF — IATF 16949 publications</a></li>
      <li><a href="https://www.iatfglobaloversight.org/news/30-july-2026-iatf-stakeholder-communique-iatf-16949-2nd-edition-update-information/" rel="noopener">IATF — 2026 second-edition status</a></li>
      <li><a href="https://www.iso.org/standard/70918.html" rel="noopener">ISO/SAE 21434:2021</a></li>
      <li><a href="https://www.iso.org/publication/PUB200262.html" rel="noopener">ISO 26262:2018 series</a></li>
      <li><a href="https://webstore.iec.ch/en/publication/33615" rel="noopener">IEC 62443-4-1:2018</a></li>
      <li><a href="https://webstore.iec.ch/en/publication/67631" rel="noopener">IEC 62443-2-4:2023</a></li>
      <li><a href="https://www.sap.com/about/trust-center/certification-compliance.html" rel="noopener">SAP Trust Center — certifications and compliance</a></li>
    </ul>
  </section>
</div>
