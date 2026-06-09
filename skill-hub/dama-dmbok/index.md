---
layout: default
title: "DAMA / Data — Practical Working Skills"
description: "Practical working skills for data governance, quality root cause, metadata, master data, lineage, reference data, and integration interoperability. Usable tomorrow."
permalink: /skill-hub/dama-dmbok/
last_modified_at: 2026-06-09
status: reviewed
verified: true
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li aria-current="page">DAMA / Data</li>
  </ol>
</nav>

<section class="section atlas-hero">
  <p class="eyebrow">Skill Hub — Data &amp; DAMA</p>
  <h1>DAMA / Data skills</h1>
  <p class="lead">Practical working skills for data governance, quality diagnostics, metadata, master data, lineage, reference data, and integration interoperability. Not framework summaries. Real methods, decision rules, and artifact templates.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>What this skill group covers</h2>
  </header>
  <p>This group covers the data management work that happens between "we have a data problem" and "the data problem is fixed and won't recur." It focuses on operational skills: diagnosing why data is wrong, deciding who owns it, tracing where it came from, and building controls that survive the next project cycle.</p>
  <p>These skills are designed for enterprise data consultants, SAP data stewards, integration analysts, and AI agents that need to produce structured data artifacts instead of generic explanations.</p>
</section>

<section class="section">
  <header class="section-heading">
    <h2>When to use this group</h2>
  </header>
  <ul>
    <li>A business process fails and the root cause is data, not code or configuration.</li>
    <li>Master data changes in one system but does not propagate correctly to another.</li>
    <li>A report is wrong and no one can explain which source system the number came from.</li>
    <li>A data quality initiative stalls because ownership, rules, or enforcement are undefined.</li>
    <li>An integration fails and the data payload is malformed, incomplete, or mapped to the wrong target field.</li>
    <li>You need to document data lineage, metadata, or reference data for compliance, migration, or AI readiness.</li>
  </ul>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Skills in this group</h2>
  </header>
  <div class="topic-grid">
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a></h3>
      <p>Diagnose missing ownership, undefined rules, and unenforced policies. Produce a governance action plan with named owners, decision rights, and enforcement mechanisms.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a></h3>
      <p>Trace a data defect from symptom to entry point. Classify the root cause type. Produce a correction plan and a prevention control.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a></h3>
      <p>Map master data domains, identify duplication and fragmentation, define golden record logic, and design replication governance.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/metadata-management-working-skill/">Metadata Management</a></h3>
      <p>Catalog business, technical, and operational metadata. Identify gaps that block reporting, integration, or AI readiness. Produce a metadata inventory with ownership.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a></h3>
      <p>Trace data from source to consumer. Document transformations, hops, and ownership at each stage. Identify lineage gaps that create audit or trust risk.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/reference-data-management-working-skill/">Reference Data Management</a></h3>
      <p>Manage code lists, status values, and classification schemes. Prevent drift between systems. Design distribution and change control for reference data.</p>
    </div>
    <div class="topic-card">
      <h3><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration &amp; Interoperability</a></h3>
      <p>Diagnose integration failures caused by data mismatch, schema drift, or mapping errors. Define data contracts and validation rules at interface boundaries.</p>
    </div>
  </div>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Recommended paths</h2>
  </header>

  <h3>Data quality incident path</h3>
  <ol>
    <li><a href="/skill-hub/dama-dmbok/data-quality-root-cause-working-skill/">Data Quality Root Cause</a></li>
    <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — if ownership or rules are missing</li>
    <li><a href="/skill-hub/dama-dmbok/master-data-management-working-skill/">Master Data Management</a> — if the defect is in master data</li>
    <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — if the source is unknown</li>
  </ol>

  <h3>Integration failure path</h3>
  <ol>
    <li><a href="/skill-hub/dama-dmbok/data-integration-interoperability-working-skill/">Data Integration &amp; Interoperability</a></li>
    <li><a href="/skill-hub/dama-dmbok/reference-data-management-working-skill/">Reference Data Management</a> — if code values mismatch</li>
    <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a> — if the data path is unclear</li>
  </ol>

  <h3>AI readiness path</h3>
  <ol>
    <li><a href="/skill-hub/dama-dmbok/metadata-management-working-skill/">Metadata Management</a></li>
    <li><a href="/skill-hub/dama-dmbok/data-lineage-working-skill/">Data Lineage</a></li>
    <li><a href="/skill-hub/dama-dmbok/data-governance-working-skill/">Data Governance</a> — if ownership is unclear</li>
  </ol>
</section>

<section class="section">
  <header class="section-heading">
    <h2>Status and limitations</h2>
  </header>
  <p>This skill group is a public working interpretation of data management practice. It is not official DAMA-DMBOK documentation. It draws on DAMA knowledge areas but translates them into operational skills for enterprise consultants and AI agents.</p>
  <p>Some skills are more mature than others. Data Quality Root Cause and Master Data Management have been tested in SAP support contexts. Metadata Management and Data Lineage are more conceptual and may need adaptation to specific tool landscapes.</p>
  <p>All skills assume you have access to systems, stakeholders, and data samples. They do not replace vendor documentation or specialized data quality tooling.</p>
</section>
