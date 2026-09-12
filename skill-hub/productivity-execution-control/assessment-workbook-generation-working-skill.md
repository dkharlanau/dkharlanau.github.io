---
layout: default
title: "Assessment Workbook Generation Working Skill"
description: "Generate an assessment workbook from a required-topic syllabus, a career capability model, and a live knowledge-base inventory."
permalink: /skill-hub/productivity-execution-control/assessment-workbook-generation-working-skill/
last_modified_at: 2026-09-10
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/skill-hub/">Skill Hub</a></li><li><a href="/skill-hub/productivity-execution-control/">Productivity and Execution Control</a></li><li aria-current="page">Assessment Workbook Generation</li></ol>
</nav>

<article class="section note-detail atlas-page">
  <p class="eyebrow">Skill Hub — Productivity and Execution Control</p>
  <h1>Assessment Workbook Generation Working Skill</h1>
  <p class="lead">Turn a changing knowledge base into a current preparation workbook without maintaining a second manual checklist.</p>

  <section>
    <h2>Use three source layers</h2>
    <p>A useful preparation workbook should not treat every page as mandatory and should not reduce a large subject to a few broad skills. Keep three models separate:</p>
    <ol>
      <li><strong>Assessment Requirements</strong> — the detailed syllabus: what the candidate must know.</li>
      <li><strong>Career Roadmap</strong> — broad capabilities: what the candidate must be able to explain, diagnose, design, and lead.</li>
      <li><strong>Career Factory</strong> — the live knowledge inventory: what material currently exists on the site.</li>
    </ol>
  </section>

  <section>
    <h2>Inputs</h2>
    <ul>
      <li><code>_data/career/assessment_requirements.yml</code> — detailed SAP Lead assessment topics, domain, component, priority, prompt, and source routes.</li>
      <li><code>_data/career/roadmap.yml</code> — Lead tracks, skills, tiers, capabilities, interview signals, and sources.</li>
      <li><code>/ai/career-factory.json</code> — generated inventory of Lab pages and career mapping state.</li>
      <li>Preparation fields — confidence, status, review dates, project example, and notes.</li>
    </ul>
  </section>

  <section>
    <h2>Working method</h2>
    <ol>
      <li><strong>Define the syllabus first.</strong> Add a required topic because it matters for the target role, not because a page happens to exist.</li>
      <li><strong>Link real source pages.</strong> A requirement should point to the best Lab material when that material exists.</li>
      <li><strong>Keep capability and detail separate.</strong> A topic such as SM12 or Variant Configuration can be detailed syllabus content while a broader career skill covers diagnosis or solution leadership.</li>
      <li><strong>Read Career Factory at generation time.</strong> Do not keep a copied list of Lab pages in JavaScript or Excel.</li>
      <li><strong>Group the inventory into components.</strong> Make SD, Pricing, ATP/aATP, MM, Inventory, EWM, TM, PP, QM, MDG/DRF, AIF, Integration, Migration, Performance, AI, and other areas easy to filter.</li>
      <li><strong>Expose gaps.</strong> Keep Lab pages with <code>needs_decision</code> visible instead of silently dropping them.</li>
      <li><strong>Add execution fields.</strong> Confidence, status, project evidence, and review dates turn an inventory into a preparation system.</li>
      <li><strong>Validate source counts.</strong> Generated workbook counts must match the three source models used for generation.</li>
    </ol>
  </section>

  <section>
    <h2>Workbook contract</h2>
    <ul>
      <li><strong>Dashboard</strong> — requirement, P1, skill, Lab-page, and mapping-gap counts.</li>
      <li><strong>Required Topics</strong> — the complete detailed syllabus with source coverage.</li>
      <li><strong>Domain sheets</strong> — assessment topics grouped into practical preparation areas.</li>
      <li><strong>Lead Skills</strong> — the stable capability model.</li>
      <li><strong>Site Topics</strong> — every current Lab page.</li>
      <li><strong>Components</strong> — required-topic and site-page counts side by side.</li>
      <li><strong>Needs Mapping</strong> — knowledge pages that still need a career decision.</li>
      <li><strong>Daily Sprint</strong> — a small preparation queue.</li>
      <li><strong>How to Use</strong> — rules for turning reading into recall and project evidence.</li>
    </ul>
  </section>

  <section>
    <h2>Decision rules</h2>
    <ul>
      <li>If a topic is required for the target role, put it in Assessment Requirements even when site coverage is incomplete.</li>
      <li>If a new Lab adds detail to an existing capability, map the page to that capability instead of creating a duplicate skill.</li>
      <li>If new content introduces a genuinely new Lead capability, update the Career Roadmap and then regenerate Career Factory.</li>
      <li>If a Lab page has no career decision, keep it visible in Needs Mapping.</li>
      <li>If the workbook contains a copied page list instead of live Career Factory data, the implementation is stale by design.</li>
      <li>If the candidate can only recognize a topic after reading it, the status is not Ready.</li>
    </ul>
  </section>

  <section>
    <h2>Ready definition</h2>
    <p>For a P1 topic, Ready means the candidate can explain the business purpose, process or architecture, one important design decision, one realistic failure path, and one real project example. A Lead answer should also make ownership and trade-offs clear.</p>
  </section>

  <section>
    <h2>Quality checks</h2>
    <ul>
      <li>All current Assessment Requirements are present.</li>
      <li>All current Career Roadmap skills are present.</li>
      <li>All current Career Factory Lab pages are present.</li>
      <li>P1/P2/P3 priorities come from the source model, not spreadsheet formatting.</li>
      <li>Source routes are visible and usable from the workbook.</li>
      <li>Component and domain views do not hide the underlying requirement or Lab row.</li>
      <li>Unmapped content remains visible.</li>
      <li>The workbook can be regenerated after site changes without editing the topic list by hand.</li>
    </ul>
  </section>

  <section>
    <h2>Agent instructions</h2>
    <p>When changing the generator, preserve the three-layer model. Never hard-code the current number of requirements, skills, or pages. Read Assessment Requirements and the Career Roadmap from Jekyll data and Career Factory at runtime. Do not auto-promote every new Lab page into the required syllabus. Do not hide <code>needs_decision</code> pages. If career coverage changes, follow the Labs Agent Contract and regenerate Career Factory.</p>
  </section>

  <section>
    <h2>Implementation</h2>
    <p><a href="/labs/templates/sap-lead-assessment-prep/">Open the SAP Lead Assessment Master Workbook generator →</a></p>
  </section>

  <section>
    <h2>Limitations</h2>
    <p>The syllabus is a working SAP Lead preparation model, not official SAP certification content. Component grouping is a navigation aid; one page or requirement can cross several SAP modules and technical boundaries.</p>
  </section>
</article>
