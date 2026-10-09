---
layout: default
title: "SAP Joule"
description: "Review a specific Joule capability: its task, data access, execution identity, product limits, and evidence of completion."
permalink: /atlas/sap/sap-joule/
atlas_section: sap
domain: SAP operations
subdomain: AI copilot
concept_type: product
sap_area: "SAP Joule"
business_process: "AI-assisted operations"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
last_modified_at: 2026-10-07
author: Dzmitryi Kharlanau

tags:
  - sap-joule
  - generative-ai
  - copilot
related:
  - /atlas/maps/sap-s4hana-landscape-map/
  - /atlas/maps/sap-product-landscape-map/
  - /atlas/maps/sap-technology-landscape-map/
  - /atlas/sap/sap-btp/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/sap-build/
  - /atlas/sap/sap-analytics-cloud/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP Joule</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP Joule</h1>
    <p class="note-subtitle">SAP's AI user experience for questions, navigation, supported tasks, skills, and agents.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>AI-assisted operations</dd></div>
      <div><dt>SAP area</dt><dd>SAP Joule</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>Assess one Joule capability at a time. Joule is SAP's AI interaction layer across supported products; its behavior depends on the application, edition, entitlement, region, and capability. A similar chat panel can expose very different data and actions.</p>

    <h2>Identify what the capability does</h2>
    <p>SAP's <a href="https://help.sap.com/docs/joule/capabilities-guide/about-this-document">capability guide</a> distinguishes informational, navigational, transactional, and analytical capabilities. An answer from documentation, a link to an application, and a business-data update have different evidence and control needs.</p>
    <ul>
      <li><strong>Information:</strong> identify the source and check whether it is current and relevant to the question.</li>
      <li><strong>Navigation:</strong> check the destination and the task the user must still complete there.</li>
      <li><strong>Transaction:</strong> identify the business object, allowed operation, execution identity, and result check.</li>
      <li><strong>Analysis:</strong> check the data scope, definitions, and limits before using the result in a decision.</li>
    </ul>

    <h2>Trace authority through to the business system</h2>
    <p>For Joule in the SAP BTP cockpit, SAP explicitly states that <a href="https://help.sap.com/docs/btp/sap-business-technology-platform/access-joule">actions are bound to the user's cockpit authorization</a>. Treat that as a documented example, not proof that every Joule integration uses the same identity flow.</p>
    <p>For the capability under review, establish who reads the data, who calls the tool, which backend authorization applies, and where any required approval occurs. Test restricted users as well as administrators. A successful model response does not grant business permission.</p>

    <h2>Custom skills and agents need a lifecycle</h2>
    <p>A bounded skill and an agent that selects several steps need different tests. Use the <a href="/atlas/sap/ai-agents/">agent design guide</a> to define decision freedom and stopping rules rather than inferring them from the Joule name.</p>
    <p>SAP documents <a href="https://help.sap.com/docs/joule-studio-classic/joule-studio-classic-edition/manage-joule-skills-and-agents-across-environments">management of custom skills and agents across environments</a> in Joule Studio, classic edition. The page covers capability versions, environments, stopping, and deployment-status mismatches. Check the guide for the edition you actually use.</p>
    <p>Keep an owner for instructions, schemas, tools, identities, dependencies, deployment state, monitoring, and recovery. A custom capability remains an integration that needs change control.</p>

    <h2>Finish with a capability record</h2>
    <p><strong>Synthetic review:</strong> for a request to change a business object, record the exact supported operation, target, permissions, approval policy, and how completion will be verified. If the capability only navigates to the relevant app, record that limit instead of promising an automated change.</p>
    <p>The useful output is one capability record with evidence and unresolved checks. No universal read-only or write-enabled label fits all Joule experiences. Verify current product documentation and the target tenant before implementation; this page is an architecture review guide, not a certification of a deployment.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-business-ai/">SAP Business AI</a></li>
      <li><a href="/atlas/sap/ai-agents/">AI Agents</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/human-approval-workflows/">Human Approval Workflows</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
