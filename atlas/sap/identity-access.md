---
layout: default
title: "Identity and Access"
description: "Analytical overview of Identity and Access in SAP: what it is, where it sits, and how it breaks."
permalink: /atlas/sap/identity-access/
atlas_section: sap
domain: SAP operations
subdomain: Operations and observability
concept_type: technology
sap_area: "Identity and Access"
business_process: "Operations and observability"
status: needs_verification
verified: false
last_reviewed: 2026-06-06
author: Dzmitryi Kharlanau

tags:
  - identity-access
  - sap-security
  - authorization
related:
  - /atlas/sap/audit-trails/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-btp/
  - /atlas/sap/fiori-ui5/
  - /atlas/sap/sap-business-ai/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">Identity and Access</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Technology</p>
    <h1>Identity and Access</h1>
    <p class="note-subtitle">Managing user identities and access rights in SAP landscapes.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Operations and observability</dd></div>
      <div><dt>SAP area</dt><dd>Identity and Access</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until technology claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>What it is</h2>
    <p>Identity and access management in SAP covers user provisioning, authentication, authorization, and governance across on-premise and cloud systems. It includes SAP Cloud Identity, SAML, OAuth, role-based access control, and privilege escalation detection.</p>

    <h2>Business purpose</h2>
    <p>Ensure the right users have the right access at the right time. Prevent unauthorized access to sensitive business data. Support compliance with segregation of duties, periodic access reviews, and automated provisioning.</p>

    <h2>Where it sits in the landscape</h2>
    <p>Identity and access spans S/4HANA authorizations (PFCG, SU01), BTP subaccount roles, and the Fiori launchpad. SAP Cloud Identity Services provides centralized identity and SSO. GRC and IAG add policy enforcement and access request workflows.</p>

    <h2>Main objects / data</h2>
    <ul>
      <li>User master: SU01 — user ID, type, validity, and defaults.</li>
      <li>Role: PFCG — composite and single roles with authorization profiles.</li>
      <li>Authorization object: field-level permission check (e.g., S_TCODE).</li>
      <li>Identity provider: SAP Cloud Identity, Microsoft Entra ID, Okta.</li>
      <li>Trust configuration: SAML 2.0 or OAuth 2.0 between systems.</li>
      <li>Access request: workflow-driven provisioning and recertification.</li>
    </ul>

    <h2>Integrations</h2>
    <ul>
      <li>S/4HANA: Fiori launchpad access, backend authorizations, business roles.</li>
      <li>BTP: subaccount roles, space roles, and service broker access.</li>
      <li>Fiori: catalog and group assignment via business roles.</li>
      <li>GRC/IAG: risk analysis, access request, and emergency access.</li>
    </ul>

    <h2>Extension points</h2>
    <ul>
      <li>Custom authorization objects and checks in ABAP.</li>
      <li>BTP role collections mapped to identity provider groups.</li>
      <li>Fiori business roles extended with custom catalogs and groups.</li>
      <li>API-based provisioning from HR or identity governance tools.</li>
    </ul>

    <h2>Monitoring / diagnostics</h2>
    <ul>
      <li>SU01 / SUIM — user and authorization reports.</li>
      <li>ST01 — authorization trace for missing permissions.</li>
      <li>SLG1 — identity provider and SSO error logs.</li>
      <li>GRC risk analysis — SoD and critical permission conflicts.</li>
      <li>Login audit: failed attempts, lockouts, and anomaly detection.</li>
    </ul>

    <h2>Strong sides</h2>
    <ul>
      <li>Granular authorization model down to field and organizational level.</li>
      <li>Centralized SSO via SAP Cloud Identity reduces password sprawl.</li>
      <li>GRC integration automates risk analysis and recertification.</li>
      <li>Fiori business roles align UX and authorization.</li>
    </ul>

    <h2>Weak sides / risks</h2>
    <ul>
      <li>Role design complexity leads to over-authorization or broken access.</li>
      <li>SSO token issues can lock out entire user populations.</li>
      <li>Privilege escalation via composite role or profile manipulation.</li>
      <li>Cloud and on-premise identity models are not always synchronized.</li>
    </ul>

    <h2>AMS incident patterns</h2>
    <ul>
      <li>User locked or expired — password policy, idle timeout, or admin error.</li>
      <li>Authorization missing — new role not assigned or profile not generated.</li>
      <li>SSO failure — SAML certificate expiry, IdP misconfiguration, or clock skew.</li>
      <li>Fiori tile missing — catalog/group assignment or cache issue.</li>
      <li>SoD violation — conflicting roles assigned via emergency access.</li>
    </ul>

    <h2>Related Atlas links</h2>
    <ul>
      <li><a href="/atlas/sap/audit-trails/">Audit Trails</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
      <li><a href="/atlas/sap/sap-business-ai/">SAP Business AI</a></li>
    </ul>

    <h2>Source references</h2>
    <ul>
      <li>SAP Cloud Identity Services — <a href="https://help.sap.com/docs/cloud-identity">SAP Help Portal</a>.</li>
      <li>SAP BTP Role Collections — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/role-collections-and-roles-in-sap-btp">SAP Help Portal</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>This page is a skeleton based on public SAP documentation. Identity provider configuration, role design, and authorization behavior vary by customer and must be verified against the customer's system.</p>

    <p class="disclaimer">This is not official SAP documentation and not a replacement for system-specific analysis.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/audit-trails/">Audit Trails</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
