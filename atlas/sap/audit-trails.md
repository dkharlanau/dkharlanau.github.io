---
layout: default
title: "Audit Trails"
description: "SAP audit evidence explained: security audit logs, change documents, table logging, read access logging, and transport history."
permalink: /atlas/sap/audit-trails/
atlas_section: sap
domain: SAP operations
subdomain: Operations and observability
concept_type: technology
sap_area: "Audit Trails"
business_process: "Operations and observability"
status: needs_verification
verified: false
last_reviewed: 2026-09-23
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
    <p class="note-subtitle">SAP does not have one universal audit log: different mechanisms record different kinds of evidence.</p>
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
    <p>When someone asks for “the SAP audit trail,” the first useful question is: <strong>audit trail for what?</strong> A changed business field, a security-relevant logon, a read of sensitive data, a customizing table update, and a transported repository object are different events. SAP records them through different mechanisms, with different configuration and retention rules.</p>

    <p>This matters during an audit and during incident analysis. If the required mechanism was not active when an event occurred, the missing evidence cannot simply be reconstructed later by looking in another generic log. Auditability has to be designed before it is needed.</p>

    <h2>Change documents explain business-object changes</h2>
    <p>Many SAP applications use <strong>change documents</strong> to record changes to business objects. Depending on the object and application implementation, a change document can identify who changed an object, when it changed, and the old and new values of relevant fields. Product master data is a familiar example: SAP documents a change history with user, time, old value, new value, and the channel through which the change was made.</p>

    <p>Change documents are application-aware evidence. They are usually more meaningful for a business question than raw table history because the application has defined which object and fields belong to the change. But coverage is not universal: a change document object has to exist and the application has to use it for the relevant data.</p>

    <h2>Table logging records selected technical data changes</h2>
    <p>ABAP table logging is a different mechanism. SAP documents that table-change logging requires both an appropriate table logging setting and the relevant <code>rec/client</code> profile configuration. Logged table changes can then be evaluated, for example with <code>SCU3</code>. Audit Trail configuration also provides tools for controlling table or data-element logging in supported scenarios.</p>

    <p>We do not enable table logging indiscriminately. It produces technical evidence and can add volume and operational cost. The decision should follow the audit requirement: which data needs evidence, which mechanism already covers it, how long the evidence must remain available, and who is allowed to administer or read it.</p>

    <h2>The Security Audit Log records security-relevant events</h2>
    <p>The <strong>Security Audit Log</strong> focuses on security-relevant activity in the ABAP platform. SAP lists examples such as successful and unsuccessful logon attempts, transaction starts, and security-related system changes. Which events are recorded and displayed depends on the audit configuration and filters.</p>

    <p>This log answers a different question from a business change document. A successful transaction start can show that a user entered a transaction; it does not by itself explain every business field that the user changed. Conversely, a business change document is not a substitute for security-event logging.</p>

    <h2>Read Access Logging covers selected reads of sensitive data</h2>
    <p>Normal change logging is about modification. Privacy and compliance requirements may also ask who <em>read</em> sensitive information. SAP Read Access Logging (RAL) is designed for selected read-access scenarios and is configured around logging purposes, log domains, and channel-specific configurations.</p>

    <p>RAL is therefore not “log every read in the system.” Its value comes from defining which sensitive access matters and under which conditions it should be recorded. SAP also records administrative access to RAL configuration and logs in the Security Audit Log, which helps protect the evidence mechanism itself.</p>

    <h2>Transport and repository history provide another evidence layer</h2>
    <p>Changes delivered through the Change and Transport System have their own history. SAP documents CTS/TMS logs and transport metadata as part of the evidence for productive-system changes, while ABAP version management records repository-object history. This is the trail we follow when the question is how a development or configuration change reached a system, rather than who changed a business master record.</p>

    <h2>Audit evidence only works as a chain</h2>
    <p>A useful audit trail connects an event to an identity, timestamp, object, action, and retained evidence. It also protects the logging configuration and the logs themselves. For a critical process, we therefore map the requirement to the specific SAP evidence source instead of assuming that one central log captures everything.</p>

    <p>The same model helps troubleshooting. If a value changed unexpectedly, we first identify the business object and its change history. If the concern is unauthorized system access, we move to security audit evidence. If the issue is a transported change, we inspect transport and repository history. The investigation becomes much faster once the question and the log type match.</p>

    <h2>Source references</h2>
    <ul>
      <li>SAP ABAP Platform — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/025d1fb2f02c42c097f04f45df09106a/7eed4aba8bcb4d7091e289cf0dc00cf4.html">Display Security Audit Log</a>.</li>
      <li>SAP ABAP Platform Security Guide — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/864321b9b3dd487d94c70f6a007b0397/c769bcd2f36611d3a6510000e835363f.html">Logging Changes to Table Data</a>.</li>
      <li>SAP ABAP Platform — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/025d1fb2f02c42c097f04f45df09106a/7e0b7b1d831b495b8ea0141038bcab55.html">Configuring Read Access Logging</a>.</li>
      <li>SAP ABAP Platform Security Guide — <a href="https://help.sap.com/docs/ABAP_PLATFORM_NEW/864321b9b3dd487d94c70f6a007b0397/c769bcd5f36611d3a6510000e835363f.html">Logging Changes Made Using the Change & Transport System</a>.</li>
    </ul>

    <h2>Verification limitations</h2>
    <p>Logging coverage, configuration tools, storage, retention, and application-specific change-document behavior depend on the SAP product and release. Verify the concrete mechanism in the target system and confirm that it was enabled for the relevant object and period before treating the absence of a record as evidence that an event did not occur.</p>
  </div>

  <section class="atlas-related">
    <h2>Related pages</h2>
    <ul>
      <li><a href="/atlas/sap/identity-access/">Identity and Access</a></li>
      <li><a href="/atlas/sap/sap-s4hana/">SAP S/4HANA</a></li>
      <li><a href="/atlas/sap/sap-btp/">SAP BTP</a></li>
      <li><a href="/atlas/sap/sap-mdg/">SAP MDG</a></li>
    </ul>
  </section>

  {% include atlas/author-block.html %}
  {% include atlas/disclaimer.html %}
</article>
