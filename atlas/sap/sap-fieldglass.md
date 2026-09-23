---
layout: default
title: "SAP Fieldglass"
description: "SAP Fieldglass explained: contingent workforce, statements of work, worker profiles, and the integration boundary with procurement and ERP."
permalink: /atlas/sap/sap-fieldglass/
atlas_section: sap
domain: SAP operations
subdomain: External workforce management
concept_type: product
sap_area: "Fieldglass"
business_process: "External workforce management"
status: needs_verification
verified: false
last_synced: 2026-07-14
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-fieldglass
  - contingent-workforce
  - services-procurement
related:
  - /atlas/sap/sap-product-portfolio/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-ariba/
  - /atlas/sap/sap-successfactors/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Fieldglass</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Fieldglass</h1>
    <p class="note-subtitle">Cloud applications for contingent workers, external services, and visibility over nonpayroll workers.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>External workforce management</dd></div>
      <div><dt>SAP area</dt><dd>Fieldglass</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>SAP Fieldglass is SAP's vendor-management portfolio for external labor and services. The important distinction is between <strong>contingent workforce management</strong>, where an individual worker is engaged for an assignment, and <strong>services procurement</strong>, where a supplier delivers work under a statement of work. SAP Fieldglass Worker Profile Management adds another use case: tracking nonpayroll workers who may not have entered through either sourcing flow.</p>

    <h2>Contingent labor follows a worker assignment</h2>
    <p>A standard contingent process can begin with a job posting and candidates or job seekers. After selection, a work order describes the commercial and operational terms of the assignment. SAP's current Fieldglass documentation shows that a work order can carry start and end dates, worker settings, time-sheet rules, rates, cost allocation, and a purchase-order reference, depending on company configuration.</p>

    <p>Once the assignment is active, the worker can record time or expenses when those processes are enabled. Approved quantities and rates can then contribute to invoicing. The useful model is therefore not simply “worker → invoice.” The job posting, work order, worker record, time or expense evidence, and invoice each answer a different question about demand, authorization, execution, and payment.</p>

    <h2>Services procurement starts from a statement of work</h2>
    <p>A statement of work (SOW) is a buyer-supplier agreement for services. SAP describes SOWs as suitable for larger or ongoing work outside the scope of one job posting. Multiple workers can be associated with an SOW, and payment can be driven by time sheets, events, fees, schedules, or milestones according to the configured commercial model.</p>

    <p>This is a different operating model from hiring one contingent worker. The SOW defines the service commitment and its invoicing rules; the evidence of delivery may be time, a completed event, a fee, or another approved service record. In integrated procurement scenarios, that evidence can be converted or mapped into ERP procurement documents such as service entry sheets, but the exact document path depends on the integration scenario.</p>

    <h2>Worker Profile Management solves a visibility problem</h2>
    <p>Not every external worker is sourced through a job posting or an SOW. SAP Fieldglass Worker Profile Management is designed to maintain standardized records for nonpayroll workers, including people who sit outside the normal vendor-management workflow. SAP positions it around visibility, onboarding and offboarding, access, certifications, and compliance.</p>

    <p>This matters when discussing “the Fieldglass worker.” A worker profile can be used for workforce visibility, while a work order represents a contingent assignment and an SOW represents a service agreement. Treating those objects as interchangeable makes integrations and reporting harder to reason about.</p>

    <h2>ERP integration is a document contract, not a generic sync</h2>
    <p>SAP provides Fieldglass integration with SAP ERP and SAP S/4HANA for supported editions and processes. Current SAP material describes exchanges that can include master data, purchase requisitions and purchase orders, time sheets, service entry sheets, invoices, and other procurement objects. Which documents actually move depends on whether the customer is running contingent workforce management, services procurement, or another supported integration scenario.</p>

    <p>Some current services-procurement scenarios also involve SAP Business Network and SAP Integration Suite, managed gateway for spend management and SAP Business Network. For example, SAP documents a 4R2 flow in which service documents move between S/4HANA Cloud, SAP Fieldglass, and SAP Business Network. That path should not be assumed for every Fieldglass implementation.</p>

    <h2>Start support from the business object</h2>
    <p>When an external-workforce process fails, the first question is which business model is in use. For contingent labor, we trace the job posting, work order, worker, submitted time or expense, approval, and invoice. For services procurement, we trace the SOW, its line items or events, the proof of service, invoicing state, and any ERP or Business Network document created from it.</p>

    <p>This avoids vague “Fieldglass integration” diagnosis. A missing worker, an incorrect rate, an unapproved time sheet, a service-entry mismatch, and an ERP invoice failure belong to different stages and often to different owners.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP — <a href="https://www.sap.com/products/spend-management/services-procurement.html">SAP Fieldglass Services Procurement</a>.</li>
      <li>SAP — <a href="https://www.sap.com/products/spend-management/worker-profile-management.html">SAP Fieldglass Worker Profile Management</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_Fieldglass/3b75472dc6104b0e8224345605250b54/3b4b67af57ee4f2e82949e1256fa735a.html">Work Order Field Definitions</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/SAP_Fieldglass/83ee364ad6f849fc82ad6e5dd1bef38a/28598019c7e644a2aa0bd1e04166ab81.html">Statements of Work</a>.</li>
      <li>SAP Help Portal — <a href="https://help.sap.com/docs/sisgw/sap-ariba-cloud-integration-gateway-overview-guide/service-procurement-with-ariba-network-and-sap-fieldglass-4r2">Service Procurement with SAP Business Network and SAP Fieldglass (4R2)</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP Fieldglass editions, workflow configuration, connectors, document mappings, and S/4HANA integration patterns vary by customer and release. Verify the subscribed Fieldglass solution and the exact integration scenario before treating these object relationships as a system-specific design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-product-portfolio/">SAP Product Portfolio</a></li>
      <li><a href="/atlas/sap/sap-ariba/">SAP Ariba</a></li>
      <li><a href="/atlas/sap/sap-successfactors/">SAP SuccessFactors</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
