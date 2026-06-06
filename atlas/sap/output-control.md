---
layout: default
title: "Output Control"
description: "Analytical overview of Output Control in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/output-control/
atlas_section: sap
domain: SAP operations
subdomain: Document output
concept_type: integration
sap_area: "Output Management"
business_process: "Document communication"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - output-control
  - document-output
  - communication
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-integration-landscape-map/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sales-domain/
  - /atlas/sap/sourcing-and-procurement-domain/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Output Control</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Integration</p>
    <h1>Output Control</h1>
    <p class="note-subtitle">SAP's mechanism for generating and distributing documents: print, email, PDF, and electronic output.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Document communication</dd></div>
      <div><dt>SAP area</dt><dd>Output Management</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until integration claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>Output Control is SAP's framework for determining when, how, and to whom business documents are output. It covers print, email, PDF generation, XML, and electronic submission. It applies to sales orders, invoices, purchase orders, delivery notes, and many other documents.</p>

    <h2>Business purpose</h2>
    <p>Automate document distribution to customers, suppliers, and internal stakeholders. Ensure the right document format reaches the right recipient at the right time. Support compliance with electronic invoicing and reporting requirements.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Output Control sits between document creation (SD, MM, FI) and distribution channels (printer, email, EDI, portal). It uses condition techniques, access sequences, and output types to determine output behavior.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Output type: what to output (invoice, order confirmation, delivery note).</li>
      <li>Condition technique: access sequence, condition table, output determination.</li>
      <li>Transmission medium: print, email, fax, EDI, XML, PDF.</li>
      <li>Partner function: who receives the output (sold-to, bill-to, vendor).</li>
      <li>Form: Smart Form, Adobe Form, or SAPscript.</li>
      <li>Spool request: print queue and status.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>SD/MM/FI: document creation triggers output determination.</li>
      <li>Email: SMTP configuration, address determination.</li>
      <li>EDI: IDoc output for trading partners.</li>
      <li>Adobe/Smart Forms: form design and rendering.</li>
      <li>External: electronic invoicing platforms, tax authorities.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom output types and condition tables.</li>
      <li>Custom form designs (Adobe, Smart Forms).</li>
      <li>Custom transmission mediums and channels.</li>
      <li>Side-by-side output management on BTP.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>Output log: SFP, NACE, or application-specific output logs.</li>
      <li>Spool monitor: SP01, SP02 for print status.</li>
      <li>Email queue: SOST, SCOT for email transmission.</li>
      <li>Form rendering: Adobe Document Services, Smart Forms trace.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Flexible condition-based output determination.</li>
      <li>Multiple transmission mediums in one framework.</li>
      <li>Integrated with SAP forms and document management.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Configuration is release-specific and often under-documented.</li>
      <li>Adobe Document Services requires separate setup and licensing.</li>
      <li>Email deliverability depends on SMTP and network.</li>
      <li>Output determination errors are hard to trace.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Output not generated — condition table, access sequence, or partner missing.</li>
      <li>Email not sent — SMTP error, address invalid, or queue blocked.</li>
      <li>Print spool stuck — printer offline, format mismatch, or authorization.</li>
      <li>Form not rendered — Adobe services, missing font, or form version.</li>
      <li>Duplicate output — condition or trigger misconfiguration.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/maps/sap-s4hana-landscape-map/">SAP S/4HANA Landscape Map</a></li>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sales-domain/">Sales Domain</a></li>
      <li><a href="/atlas/sap/sourcing-and-procurement-domain/">Sourcing and Procurement Domain</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP S/4HANA 2025 Feature Scope Description — <a href="https://help.sap.com/doc/e2048712f0ab45e791e6d15ba5e20c68/2025/en-US/FSD_OP2025_latest.pdf">FSD_OP2025_latest.pdf</a> (public-safe topic discovery only).</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Output Control configuration, form technologies, and transmission mechanisms vary by S/4HANA release and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/maps/sap-integration-landscape-map/">SAP Integration Landscape Map</a></li>
      <li><a href="/atlas/sap/sales-domain/">Sales Domain</a></li>
      <li><a href="/atlas/sap/sourcing-and-procurement-domain/">Sourcing and Procurement Domain</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
