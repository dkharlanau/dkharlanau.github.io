---
layout: default
title: "Identity and Access"
description: "How identity, authentication, provisioning, roles, and authorizations fit together across SAP ABAP and SAP BTP landscapes."
permalink: /atlas/sap/identity-access/
atlas_section: sap
domain: SAP operations
subdomain: Operations and observability
concept_type: technology
sap_area: "Identity and Access"
business_process: "Operations and observability"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
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
    <p class="note-subtitle">From a person's identity to authentication, provisioning, roles, and the authorization checks that protect business data.</p>
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
    <p>Identity and access is not one SAP feature. It is a chain of decisions that starts with <strong>who the person or technical client is</strong>, continues with <strong>how that identity is authenticated and provisioned</strong>, and ends with <strong>what the target application authorizes it to do</strong>. Mixing those layers is one reason access incidents become difficult to diagnose.</p>

    <h2>Authentication proves identity; authorization decides access</h2>
    <p>An identity provider authenticates a user and supplies identity information to a relying application or platform. Single sign-on can make that authentication experience consistent across applications, but successful login does not grant every business permission. The target still evaluates its own authorization model.</p>

    <p>This distinction is especially visible in hybrid SAP landscapes. A corporate identity provider may authenticate the same employee for several SAP cloud applications, while an ABAP system checks PFCG-derived authorizations and a BTP application checks application roles delivered through role collections. One identity can therefore be authenticated successfully and still be blocked by a valid authorization check downstream.</p>

    <h2>ABAP authorization is built around roles and authorization objects</h2>
    <p>In the ABAP authorization concept, authorization objects define fields that an application can check. Authorizations contain allowed values for those fields, and roles collect the authorizations needed for a business activity. SAP recommends maintaining user authorization data through Role Maintenance (<code>PFCG</code>) rather than by manually maintaining profiles.</p>

    <p>The model is more precise than “user has transaction X.” A user may reach an application and then fail an authorization check for company code, plant, activity, document type, or another field. Good role design therefore starts from business responsibility and organizational scope, not from copying a large role until the error disappears.</p>

    <h2>Fiori navigation and backend authorization are related but not identical</h2>
    <p>Fiori content controls what applications are presented and how users navigate to them. Business catalogs and spaces/pages can be assigned through roles, while groups are deprecated in current launchpad guidance. But making an app visible does not by itself satisfy every backend authorization required by that app.</p>

    <p>This gives us a useful diagnostic split: <strong>Can the user see and launch the app?</strong> and <strong>Can the backend execute the requested business action?</strong> A missing catalog or target mapping produces a different class of problem from an ABAP authorization object rejecting a request.</p>

    <h2>SAP Cloud Identity Services handles identity services, not every application permission</h2>
    <p>SAP Cloud Identity Services includes capabilities such as Identity Authentication, Identity Provisioning, and an identity directory. Identity Authentication can participate in single sign-on and federation with a corporate identity provider. Identity Provisioning can synchronize users and groups to supported target systems through connectors and transformations.</p>

    <p>Provisioning should not be confused with the authorization decision itself. A provisioning process can create the user, send groups, or maintain assignments in a target. The target application or platform then interprets those assignments according to its authorization model. When access is wrong, we need to know whether the failure is in identity data, provisioning, trust, role mapping, or the final application check.</p>

    <h2>BTP adds its own trust and role-collection layer</h2>
    <p>SAP BTP subaccounts establish trust with identity providers. Role collections group authorizations for business users on BTP and can be assigned directly or mapped from identity-provider groups depending on the trust setup. Platform users and business users also have different administrative purposes and should not be treated as one generic user type.</p>

    <p>A typical access path might therefore be: corporate user → identity provider → BTP trust → group or user mapping → role collection → application role → backend API authorization. We diagnose the first broken contract in that chain rather than repeatedly changing roles at the final system.</p>

    <h2>Lifecycle matters as much as initial access</h2>
    <p>The security problem is not finished when onboarding works. Joiners, role changes, temporary access, and leavers all change what a person should be able to do. Central provisioning can help synchronize those changes, while governance processes such as segregation-of-duties analysis and access reviews address whether the assignments are appropriate.</p>

    <p>The practical goal is not “centralize everything.” It is to keep identity ownership, authentication, provisioning, and authorization responsibilities explicit enough that access can be granted, reviewed, removed, and explained later.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP ABAP Platform — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ad77b44570314f6d8c3a8a807273084c/4f4decf806b02892e10000000a42189b.html">ABAP Authorization Concept</a>.</li>
      <li>SAP ABAP Platform — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/ad77b44570314f6d8c3a8a807273084c/ed3fd088062d4eb09d84f90b24e7bdd0.html">Maintaining Authorizations in Roles for Productive Use</a>.</li>
      <li>SAP Cloud Identity Services — <a href="https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/onboarding-and-provisioning">Onboarding and Provisioning</a>.</li>
      <li>SAP BTP — <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/security-administration-managing-authentication-and-authorization">Security Administration: Managing Authentication and Authorization</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Identity architecture and authorization behavior vary by SAP product, edition, authentication method, application, and customer role design. Verify the concrete trust configuration, provisioning path, role model, and target-system authorization checks before applying this model to an incident or security design.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/audit-trails/">Audit Trails</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/fiori-ui5/">Fiori / UI5</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
