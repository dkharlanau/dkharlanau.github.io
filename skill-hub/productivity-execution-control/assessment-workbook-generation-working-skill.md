---
layout: default
title: "Assessment Workbook Generation Working Skill"
description: "Turn a live knowledge base and career roadmap into an Excel preparation workbook without maintaining a second manual topic list."
permalink: /skill-hub/productivity-execution-control/assessment-workbook-generation-working-skill/
last_modified_at: 2026-09-10
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/skill-hub/">Skill Hub</a></li>
    <li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li>
    <li aria-current="page">Assessment Workbook Generation</li>
  </ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Assessment Workbook Generation Working Skill</h1>
  <p class="lead">Generate a preparation workbook from the current knowledge base instead of maintaining a second checklist by hand.</p>

  <section>
    <h2>What this skill is for</h2>
    <p>A study checklist becomes unreliable when the site changes faster than the spreadsheet. New SAP pages appear, old topics move, and interview priorities change. This skill treats the workbook as a generated view of the source knowledge model.</p>
    <p>On this site, the source model is the SAP Lead Career Roadmap plus Career Factory. The roadmap says what a Lead should be able to do. Career Factory says which Lab pages exist and whether they are mapped to those skills.</p>
  </section>

  <section>
    <h2>Inputs required</h2>
    <ul>
      <li><code>_data/career/roadmap.yml</code> — tracks, skills, tiers, capabilities, interview signals, and sources.</li>
      <li><code>/ai/career-factory.json</code> — generated inventory of all Lab pages and their mapping state.</li>
      <li>A priority rule — on this site, Core = P1, Cross-boundary = P2, Differentiator = P3.</li>
      <li>A preparation state model — confidence, status, project example, and notes.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Read the roadmap.</strong> Treat skill IDs as the stable assessment capability model.</li>
      <li><strong>Read Career Factory.</strong> Use the generated Lab inventory instead of scanning selected folders manually.</li>
      <li><strong>Keep both views.</strong> Do not merge a broad Lead skill and a detailed Lab page into one row. They answer different questions.</li>
      <li><strong>Derive component groups.</strong> Use routes and titles to group detailed pages into areas such as SD, Pricing, ATP, MM, Inventory, EWM, TM, PP, QM, MDG/DRF, AIF, Integration, Migration, Performance, AI, and delivery.</li>
      <li><strong>Expose mapping gaps.</strong> Put <code>needs_decision</code> pages in a separate sheet. A workbook should show content debt, not hide it.</li>
      <li><strong>Add preparation fields.</strong> Confidence, status, project evidence, and notes turn an inventory into an execution tool.</li>
      <li><strong>Generate the workbook.</strong> Build it from the current source data when the user asks for it.</li>
      <li><strong>Validate counts.</strong> The workbook skill count and Lab-page count must match the source data used for generation.</li>
    </ol>
  </section>

  <section>
    <h2>Workbook contract</h2>
    <p>A strong assessment workbook contains at least these views:</p>
    <ul>
      <li><strong>Dashboard</strong> — skills, pages, mapping gaps, and preparation guidance.</li>
      <li><strong>Lead Skills</strong> — the stable capability model for the interview.</li>
      <li><strong>Site Topics</strong> — every detailed source page with URL and mapping state.</li>
      <li><strong>Components</strong> — grouped technical and business areas.</li>
      <li><strong>Needs Mapping</strong> — pages that still need a career decision.</li>
      <li><strong>Track sheets</strong> — Sales, Logistics, Integration, AI & Data, Delivery, and Leadership.</li>
      <li><strong>Daily Sprint</strong> — a small working queue for actual preparation.</li>
      <li><strong>How to Use</strong> — simple rules for turning reading into interview-ready recall.</li>
    </ul>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a topic exists only in a manually maintained spreadsheet, it is not a reliable source of truth.</li>
      <li>If a Lab page exists but has no career decision, keep it visible as a mapping gap.</li>
      <li>If a new Lab introduces a new interview capability, update the Career Roadmap first; do not invent a workbook-only skill.</li>
      <li>If a page is useful detail for an existing skill, map it to that skill instead of creating duplicate capability names.</li>
      <li>If workbook counts do not match Career Factory and the roadmap, generation has failed.</li>
      <li>If a candidate only reads pages but cannot recall, diagnose, design, or lead through the topic, the preparation status is not Ready.</li>
    </ul>
  </section>

  <section>
    <h2>Quality checklist</h2>
    <ul>
      <li>All current roadmap skills are present.</li>
      <li>All current Career Factory Lab pages are present.</li>
      <li>Every row contains a stable route or skill ID where available.</li>
      <li>Source URLs are usable from the workbook.</li>
      <li>Core skills are easy to filter as P1.</li>
      <li>Unmapped pages are visible in a dedicated backlog.</li>
      <li>Detailed pages are grouped into understandable components or areas.</li>
      <li>The workbook can be regenerated after site changes without hand-editing the topic list.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When changing this generator, preserve the separation between career skills and Lab inventory. Do not hard-code the current number of pages. Read the current Career Factory payload at generation time. Use roadmap tiers for priority. Keep <code>needs_decision</code> pages visible. When a new Lab changes career coverage, follow the Labs Agent Contract and regenerate Career Factory before treating the workbook as current.</p>
  </section>

  <section>
    <h2>Use the implementation</h2>
    <p><a href="/labs/templates/sap-lead-assessment-prep/">Open the SAP Lead Assessment Master Workbook generator →</a></p>
  </section>

  <section>
    <h2>Status and limitations</h2>
    <p>The component grouping is a practical navigation layer based on page routes and titles. It does not replace SAP product documentation or the Career Roadmap. A page can also belong to more than one business or technical area even when the workbook shows one primary component.</p>
  </section>
</article>
