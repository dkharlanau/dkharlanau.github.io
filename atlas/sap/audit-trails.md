---
layout: default
title: "Audit Trails"
description: "Analytical overview of Audit Trails in SAP: what they are, where they sit, and how they break."
permalink: /atlas/sap/audit-trails/
atlas_section: sap
domain: SAP operations
subdomain: Operations and observability
concept_type: technology
sap_area: "Audit Trails"
business_process: "Operations and observability"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - audit-trails
  - compliance
  - sap-security
related:
  - /atlas/sap/identity-access/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-mdg/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Audit Trails</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Audit Trails</h1>
    <p class="note-subtitle">Recording who did what, when, and why in SAP systems.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Operations and observability</dd></div>
      <div><dt>SAP area</dt><dd>Audit Trails</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>Audit trails are the mechanisms that record user and system activities in SAP. They capture change documents, table logging, security audit logs, read access logging, and application logs to provide an evidence trail for compliance, forensics, and troubleshooting.</p>

    <h2>Business purpose</h2>
    <p>Support regulatory compliance (SOX, GDPR, industry-specific mandates). Enable forensic analysis after security incidents or data inconsistencies. Detect unauthorized changes and support internal control audits.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Audit trails are embedded in the SAP kernel and application layer. Security audit log and read access logging are configured in transaction RSAU. Change documents and table logging are application-specific. In cloud landscapes, SAP Cloud Identity and BTP subaccount audit logs extend coverage.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>Change documents: before/after values for critical business objects.</li>
      <li>Table logging: direct table updates logged via SCU3.</li>
      <li>Security audit log: logon, transaction start, report execution.</li>
      <li>Read access logging: sensitive data read by users.</li>
      <li>Application log: program-specific events and errors (SLG1).</li>
      <li>Audit log files: OS-level files managed by the kernel.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: change documents for master data and transactional objects.</li>
      <li>GRC: access control and risk analysis using audit data.</li>
      <li>BTP: subaccount audit logs and Cloud Identity events.</li>
      <li>External: SIEM, log aggregators, and compliance reporting tools.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom change document objects for bespoke applications.</li>
      <li>Additional fields in read access logging for sensitive data.</li>
      <li>Log export to external SIEM or long-term archive.</li>
      <li>Alert rules for suspicious patterns in audit data.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>RSAU — security audit log analysis and configuration.</li>
      <li>SCU3 — table logging display and comparison.</li>
      <li>SLG1 — application log for program-specific events.</li>
      <li>Change document analysis — object class, key, and time range.</li>
      <li>Log file health — size, rotation, and retention compliance.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Native mechanisms cover most compliance requirements without add-ons.</li>
      <li>Change documents provide before/after evidence for audits.</li>
      <li>Security audit log captures low-level system access.</li>
      <li>Read access logging supports GDPR data protection accountability.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Audit log volume can grow rapidly and impact performance.</li>
      <li>Not all tables or fields are logged by default.</li>
      <li>Log tampering is possible if OS-level access is not restricted.</li>
      <li>Retention policies vary by system and are often misconfigured.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>Unauthorized change — change document reveals unexpected update.</li>
      <li>Audit log full — disk space or performance issue from excessive logging.</li>
      <li>Missing evidence — required log not enabled or already deleted.</li>
      <li>Read access alert — sensitive data queried outside business need.</li>
      <li>Compliance gap — auditor finds incomplete trail for critical process.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/identity-access/">Identity and Access</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Security Audit Log — <a href="https://help.sap.com/docs/sap-netweaver/sap-netweaver-750/security-audit-log">SAP Help Portal</a>.</li>
      <li>SAP Read Access Logging — <a href="https://help.sap.com/docs/sap-btp/sap-btp/read-access-logging">SAP Help Portal</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Audit log availability, retention, and performance impact vary by release and customer configuration and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/identity-access/">Identity and Access</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
