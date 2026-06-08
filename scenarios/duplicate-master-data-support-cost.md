---
layout: default
title: "How duplicate master data drives hidden support cost"
description: "Duplicate customers, vendors, or materials create confusion in transactions, reporting, and interfaces, inflating support tickets and reconciliation effort."
permalink: /scenarios/duplicate-master-data-support-cost/
scenario_cluster: Master Data Pain
domain: SAP AMS
subdomain: Master data quality
concept_type: business scenario
sap_area: "Master data quality / duplicates"
business_process: Master data governance
status: needs_verification
verified: false
last_reviewed: 2026-06-09
author: Dzmitryi Kharlanau
tags:
  - master-data
  - data-quality
  - sap-mdg
  - diagnostics
related:
  - /atlas/diagnostics/sap-master-data-duplicate-diagnostics/
  - /atlas/diagnostics/sap-key-mapping-diagnostics/
  - /atlas/diagnostics/sap-number-range-diagnostics/
  - /atlas/data-quality/sap-master-data-quality/
  - /atlas/data-quality/master-data-governance-failure-modes/
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/scenarios/">Scenarios</a></li>
    <li aria-current="page">How duplicate master data drives hidden support cost</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <header class="note-header">
    <p class="eyebrow">Scenario — Master Data Pain</p>
    <h1>How duplicate master data drives hidden support cost</h1>
    <p class="note-subtitle">Duplicate customers, vendors, or materials create confusion in transactions, reporting, and interfaces, inflating support tickets and reconciliation effort.</p>
    <div class="atlas-pill-row">{% include atlas/status-badge.html %}</div>
  </header>

  <aside class="atlas-meta-panel">
    <dl>
      <div><dt>Process</dt><dd>Master data governance</dd></div>
      <div><dt>SAP area</dt><dd>Master data quality / duplicates</dd></div>
      <div><dt>Indexing</dt><dd>Noindex until scenario claims are verified against public SAP docs.</dd></div>
    </dl>
  </aside>

  <div class="note-body">
    <h2>Business pain</h2>
    <p>One real business entity has multiple SAP records. A customer exists twice under slightly different names. A vendor was created again because the first record had a typo in the search term. A material was duplicated during a plant extension. Transactions split across these records. Reporting shows inconsistent totals. Interfaces create even more duplicates because they cannot match the "right" record. Support teams spend hours answering "which record is correct?"</p>

    <h2>Process context</h2>
    <p>Duplicates originate at master data creation — manual entry, batch upload, or interface replication — and propagate through transactions, reporting, and further integrations. The cost is rarely visible as a single line item. It appears as support tickets, reporting reconciliation projects, payment errors, and inventory discrepancies that are blamed on "system issues" rather than data quality.</p>

    <h2>Typical symptoms</h2>
    <ul>
      <li>Sales order created under the "wrong" customer number; collections team cannot find open items.</li>
      <li>Vendor paid from duplicate account; payment history split across records.</li>
      <li>Material availability shows stock on one material number but not the other.</li>
      <li>Management reports with multiple rows for what appears to be the same entity.</li>
      <li>Interface creates new records instead of updating existing ones.</li>
      <li>Support tickets asking "which customer/vendor/material should I use?"</li>
      <li>Periodic "data cleansing" projects that merge or archive duplicates.</li>
    </ul>

    <h2>SAP touchpoints</h2>
    <ul>
      <li><strong>BP / XD01 / XD02</strong> — Business Partner and customer master maintenance.</li>
      <li><strong>BP / XK01 / XK02</strong> — Business Partner and vendor master maintenance.</li>
      <li><strong>MM01 / MM02</strong> — Material master creation and change.</li>
      <li><strong>BUPA_PRE_DA</strong> — Duplicate check for business partners.</li>
      <li><strong>ICM_RULESET</strong> — Information Consistency Management rules for duplicate detection.</li>
      <li><strong>BUT000 / BUT001</strong> — Business Partner general data tables.</li>
      <li><strong>KNA1 / LFA1 / MARA</strong> — Customer, vendor, and material master tables.</li>
      <li><strong>MDG key mapping</strong> — Mapping between MDG and operational system keys.</li>
    </ul>

    <h2>Master data / configuration / integration touchpoints</h2>
    <ul>
      <li>Duplicate check rules and activation (ICM_RULESET, BUPA_PRE_DA, SA17/SA24).</li>
      <li>Number range configuration and overlap between systems or organizational units.</li>
      <li>Key mapping integrity for objects replicated from MDG or legacy systems.</li>
      <li>Search matchcode settings and search help behavior.</li>
      <li>Interface logic: create versus update decision based on external ID or key mapping.</li>
      <li>Data migration cleansing rules and merge logic.</li>
      <li>User authorization to create master data without mandatory duplicate check.</li>
    </ul>

    <h2>Cost drivers</h2>
    <ul>
      <li>Support tickets for "wrong" record selection and transaction correction.</li>
      <li>Reporting reconciliation between duplicate records.</li>
      <li>Merge and data cleansing projects, often requiring custom programs or third-party tools.</li>
      <li>Payment errors and collection delays due to split vendor or customer accounts.</li>
      <li>Interface rework to handle duplicates or prevent new ones.</li>
      <li>Inventory valuation discrepancies from split material records.</li>
    </ul>

    <h2>Root cause patterns</h2>
    <ul>
      <li><strong>Manual entry without search.</strong> User creates a new record instead of finding the existing one due to poor search habits or time pressure.</li>
      <li><strong>Replication without key mapping.</strong> Interface or MDG replication cannot match the source key to the target key, so it creates a new record.</li>
      <li><strong>Number range overlap.</strong> Same number range used in multiple systems or org units, causing collision or confusion.</li>
      <li><strong>Missing or inactive duplicate check.</strong> Duplicate detection rules not configured, not activated, or threshold set too loosely.</li>
      <li><strong>Interface defaulting to create.</strong> Middleware or EDI logic creates a new record when an update would have been correct.</li>
      <li><strong>Migration data not cleansed.</strong> Legacy duplicates loaded into SAP without merge or mapping.</li>
      <li><strong>Temporary records becoming permanent.</strong> "Test" or "temp" records created in production and later used in transactions.</li>
    </ul>

    <h2>Diagnostic workflow</h2>
    <p>A practical approach to quantify and prioritize duplicate issues:</p>
    <ol>
      <li>Identify duplicate clusters: same name, tax ID, address, phone, or external reference ID.</li>
      <li>Check BP, customer, vendor, or material tables for matching fields and creation sources.</li>
      <li>Review number range assignment and check for overlap across company codes or systems.</li>
      <li>Verify duplicate check configuration (ICM_RULESET, BUPA_PRE_DA) and activation status.</li>
      <li>Inspect interface logic for the create-versus-update decision path.</li>
      <li>Assess key mapping integrity for replicated objects.</li>
      <li>Quantify transaction split: how many orders, invoices, or movements sit on each duplicate.</li>
      <li>Prioritize merge or archival candidates based on transaction volume and business impact.</li>
    </ol>

    <h2>Solution patterns</h2>
    <ul>
      <li>Enforce duplicate check at every creation point: dialog transaction, batch input, and interface.</li>
      <li>Standardize number ranges across the system landscape with clear ownership.</li>
      <li>Implement key mapping for all objects replicated between MDG and operational systems.</li>
      <li>Run regular duplicate monitoring reports and assign stewardship for resolution.</li>
      <li>Establish a data stewardship process with authority to decide merge versus archive.</li>
      <li>Change interface logic to search-before-create using stable identifiers (tax ID, GLN, DUNS).</li>
    </ul>

    <h2>AI / automation / workflow opportunity</h2>
    <p>Fuzzy duplicate detection across name, address, and tax ID fields can surface clusters that exact-match rules miss. Automated duplicate scoring and merge recommendations reduce the manual effort of data stewardship. A search-before-create interface pre-check can block new records when a high-confidence match exists. Support ticket classification can automatically link "wrong record" tickets to duplicate root cause, helping AMS teams track duplicate-driven volume. Predictive reporting reconciliation alerts can flag when duplicate records are causing variance before month-end close.</p>

    <h2>Related Atlas pages</h2>
    <ul>
      <li><a href="/atlas/diagnostics/sap-master-data-duplicate-diagnostics/">SAP Master Data Duplicate Diagnostics</a> — Tools and queries for finding duplicate customers, vendors, and materials.</li>
      <li><a href="/atlas/diagnostics/sap-key-mapping-diagnostics/">SAP Key Mapping Diagnostics</a> — Key mapping integrity checks for replicated objects.</li>
      <li><a href="/atlas/diagnostics/sap-number-range-diagnostics/">SAP Number Range Diagnostics</a> — Number range overlap and configuration analysis.</li>
      <li><a href="/atlas/data-quality/sap-master-data-quality/">SAP Master Data Quality</a> — Data quality dimensions, measurement, and improvement patterns.</li>
      <li><a href="/atlas/data-quality/master-data-governance-failure-modes/">Master Data Governance Failure Modes</a> — Governance breakdowns that allow duplicates to enter the system.</li>
    </ul>

    <h2>Public references</h2>
    <p>No verified public references included. Validate specific duplicate check behavior and SAP Note applicability in your SAP landscape and official SAP documentation.</p>

    <h2>Verification status and limitations</h2>
    <p>This scenario is a structured working hypothesis based on operational patterns observed in SAP AMS support. Specific cost figures, transaction behavior, and configuration details vary by SAP release, industry solution, and custom enhancement. Validate in your own landscape and official SAP documentation before acting on diagnostic recommendations.</p>
  </div>
</article>

{% include atlas/author-block.html %}
{% include atlas/disclaimer.html %}
