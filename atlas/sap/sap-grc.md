---
layout: default
title: "SAP GRC (Governance, Risk, and Compliance)"
description: "SAP GRC explained: Access Control, Process Control, and Risk Management, with clear boundaries between access risk, controls, and enterprise risk."
permalink: /atlas/sap/sap-grc/
atlas_section: sap
domain: SAP operations
subdomain: Governance risk and compliance
concept_type: product
sap_area: "GRC"
business_process: "Governance and compliance"
status: needs_verification
verified: false
last_synced: 2026-07-14
last_reviewed: 2026-09-23
author: Dzmitryi Kharlanau

tags:
  - sap-grc
  - access-control
  - segregation-of-duties
related:
  - /atlas/sap/sap-product-portfolio/
  - /atlas/sap/sap-s4hana/
  - /atlas/sap/identity-access/
  - /atlas/sap/audit-trails/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/atlas/">Knowledge Atlas</a></li>
    <li><a href="/atlas/sap/">SAP</a></li>
    <li aria-current="page">SAP GRC</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Atlas Product</p>
    <h1>SAP GRC (Governance, Risk, and Compliance)</h1>
    <p class="note-subtitle">A family of governance applications for access risk, internal controls, and enterprise risk rather than one universal compliance monitor.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Governance and compliance</dd></div>
      <div><dt>SAP area</dt><dd>GRC</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until product claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <p>“SAP GRC” is often used as if it were one application, but the useful model is a set of related governance products. <strong>SAP Access Control</strong> focuses on access risk and governed access processes. <strong>SAP Process Control</strong> manages internal controls and their testing or monitoring. <strong>SAP Risk Management</strong> manages business risks, assessments, responses, and residual risk. They can work together, but they do not answer the same question.</p>

    <p>This distinction matters in practice. A segregation-of-duties conflict is not the same object as a failed financial control, and neither is the same as an enterprise risk such as supplier disruption. Calling all three “a GRC issue” hides the evidence, owner, and remediation path that actually matter.</p>

    <h2>Access Control evaluates what a user or role could do</h2>
    <p>SAP Access Control analyzes access against configured rules for segregation of duties (SoD), critical access, and related access risks. A rule set represents the organization's control policy: it defines which combinations of functions or permissions should be treated as risky. The quality of that model is fundamental because the analysis can only detect risks that the rules describe correctly.</p>

    <p>That is why a reported conflict is not automatically proof of misuse. Access risk analysis shows that a user, role, or profile has a risky combination of capabilities. Organizational rules can narrow false positives for valid organizational separation, but SAP explicitly warns that incorrect filters can hide real concerns. When a conflict cannot reasonably be removed, a mitigating control can document how the remaining risk is owned, monitored, and limited for a defined period.</p>

    <h2>Access requests and emergency access govern different situations</h2>
    <p>Access Control can also govern access requests, approvals, role-related processes, and periodic certifications. These workflows help decide whether access should be granted or retained; the target system still enforces the resulting authorizations. This keeps the boundary with identity and authorization architecture clear: GRC governs the access decision, while the application ultimately checks what the user can do.</p>

    <p>Emergency Access Management addresses temporary elevated access. SAP's current Access Control documentation describes self-service requests, owner approval, and review of emergency-access usage and logs. The control value is not simply that a “firefighter” account exists. The assignment, reason, duration, activity evidence, and review process have to form a defensible chain.</p>

    <h2>Process Control asks whether a business control operated</h2>
    <p>SAP Process Control works from a control and compliance structure rather than from an SoD rule set. Controls can be assessed manually or supported by automated monitoring. In continuous monitoring, SAP documents a flow in which data sources feed business rules, business rules identify exceptions, rules are assigned to controls, and scheduled monitoring can create issues for review and remediation.</p>

    <p>This is more precise than saying that GRC “monitors all transactions.” Monitoring only sees the configured source, rule, scope, and schedule. A healthy technical job is not proof that the control design is correct, and a good control definition is not useful if its data source stopped producing evidence. Operations therefore has to preserve both the control meaning and the execution trail.</p>

    <h2>Risk Management works at the risk-and-response level</h2>
    <p>SAP Risk Management represents risks and opportunities, their probability and impact, assessment activities, incidents, and planned responses. SAP distinguishes <strong>inherent risk</strong> before mitigation from <strong>residual risk</strong> after responses or controls are considered. Assessments can be qualitative or quantitative depending on the configured method.</p>

    <p>Process Control and Risk Management can meet at the mitigation boundary: a control can contribute to the response to a business risk. That relationship is useful, but the objects remain different. The risk explains the uncertain business outcome; the control describes an activity intended to prevent, detect, or respond to a condition.</p>

    <h2>GRC does not replace the systems it governs</h2>
    <p>Access Control depends on target-system roles, users, and authorization data. Process Control depends on business-system evidence and configured monitoring logic. Risk Management depends on an explicit risk taxonomy, assessment method, ownership, and responses. None of these products turns an unclear operating model into good governance automatically.</p>

    <p>For investigation, we therefore start from the governance object. For an SoD finding, inspect the rule, functions, user or role assignments, organizational scope, and mitigation. For a control exception, trace the data source, business rule, execution result, and issue workflow. For a risk question, inspect the assessment basis, probability and impact, response, and residual-risk calculation. The product label is less useful than the object chain.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP Access Control 12.0 SP31 — <a href="https://help.sap.com/docs/SAP_ACCESS_CONTROL/90e3fa2293374b0aac35f916f33954e6/3e5b13840a8b49bf8208c046d5bddbaf.html">Getting Started with Emergency Access Management</a>.</li>
      <li>SAP Access Control 12.0 SP31 — <a href="https://help.sap.com/docs/SAP_ACCESS_CONTROL/5cae1bc9a72348389e91183714220e30/b790eb4fa7b94a59e10000000a445394.html">Mitigated Access</a>.</li>
      <li>SAP Access Control 12.0 SP31 — <a href="https://help.sap.com/docs/SAP_ACCESS_CONTROL/5cae1bc9a72348389e91183714220e30/8716ea4f962a2e74e10000000a44176f.html">Organization Rules</a>.</li>
      <li>SAP Process Control 12.0 SP27 — <a href="https://help.sap.com/docs/SAP_PROCESS_CONTROL/f77342ea45c24d3f81032575e6f50d8b/49e1c5c6bfc749cc90a5ac460f3ae53f.html">Continuous Monitoring Overview</a>.</li>
      <li>SAP Risk Management 12.0 SP29 — <a href="https://help.sap.com/docs/SAP_RISK_MANAGEMENT/51bbedc6646d4ff5b35b9d883be390a6/c17c9f5ef1944de5b15635c9831e7563.html">Risk Assessments</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>SAP GRC product versions, connector coverage, rule content, workflows, monitoring subscenarios, and integration with target systems vary by implementation. Verify the exact Access Control, Process Control, or Risk Management release and customer configuration before treating this page as a control design or audit procedure.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/sap-product-portfolio/">SAP Product Portfolio</a></li>
      <li><a href="/atlas/sap/identity-access/">Identity and Access</a></li>
      <li><a href="/atlas/sap/audit-trails/">Audit Trails</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
