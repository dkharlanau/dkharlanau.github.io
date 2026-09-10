---
layout: default
title: "SAP Lead Assessment Master Workbook"
description: "Generate a complete SAP Lead Excel preparation workbook from assessment requirements, the Career Roadmap, and every Lab page in Career Factory."
permalink: /labs/templates/sap-lead-assessment-prep/
status: needs_verification
verified: false
robots: noindex,follow
sitemap: false
last_modified_at: 2026-09-10
hide_global_cta: true
career_impact: none
career_reason: "Study utility generated from the assessment syllabus, career skills, and Lab inventory."
tags: [sap, interview, assessment, checklist, excel, template]
---

<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol><li><a href="/">Home</a></li><li><a href="/labs/">Labs</a></li><li><a href="/labs/templates/">Templates</a></li><li aria-current="page">SAP Lead Assessment Workbook</li></ol>
</nav>

# SAP Lead Assessment Master Workbook

Generate the workbook from the current site instead of maintaining a second checklist by hand.

The model now has three separate layers:

1. **Assessment Requirements** — the detailed syllabus: what a SAP Lead should know for Sales, Procurement, Logistics, Integration, Migration, Performance, AI, Delivery, and Leadership.
2. **Lead Skills** — the broader Career Roadmap capabilities: know, diagnose, design, and lead.
3. **Site Topics** — every current Lab page from Career Factory, including detailed SAP components and supporting material.

This separation matters. A new Lab page does not automatically become a mandatory interview topic, and a required assessment topic stays visible even if the site still needs better material for it.

<div class="research-canvas__metrics" aria-label="Workbook source metrics">
  <div><strong id="sap-lead-required-count">—</strong><span> required topics</span></div>
  <div><strong id="sap-lead-p1-count">—</strong><span> P1 topics</span></div>
  <div><strong id="sap-lead-skill-count">—</strong><span> Lead skills</span></div>
  <div><strong id="sap-lead-page-count">—</strong><span> Lab pages</span></div>
  <div><strong id="sap-lead-gap-count">—</strong><span> pages needing career mapping</span></div>
  <div><strong id="sap-lead-coverage">—</strong><span> career mapping coverage</span></div>
</div>

<button class="research-canvas__button" type="button" id="download-sap-lead-tracker">Generate current Excel workbook</button>
<span id="download-sap-lead-status" role="status" aria-live="polite"></span>

## What is inside

- **Dashboard** — current syllabus, skill, page, and mapping counts.
- **Required Topics** — the detailed assessment programme with P1/P2/P3 priority, assessment prompt, source pages, confidence, status, review dates, project example, and notes.
- **Domain sheets** — Sales and O2C; Procurement and Inventory; Warehouse, Production, Quality and Transport; Integration and Architecture; S/4HANA Migration; Performance and Operations; AI and Data; Delivery and Leadership.
- **Lead Skills** — the Career Roadmap capability model and interview signals.
- **Site Topics** — every Lab page from Career Factory, with component, route, career state, mapped skills, priority, URL, and preparation fields.
- **Components** — required-topic counts and site-page counts side by side. This makes areas such as SD, Pricing, ATP/aATP, MM, Inventory, EWM, TM, PP, QM, MDG/DRF, AIF, Integration Suite, Migration, Performance, AI, and operations visible in one place.
- **Needs Mapping** — existing Lab pages that still need a career decision.
- **Daily Sprint** — a small working queue for 20-minute review blocks.
- **How to Use** — the preparation rules.

The workbook is generated in the browser from the current `_data/career/assessment_requirements.yml`, `_data/career/roadmap.yml`, and `/ai/career-factory.json`. Preparation status stays in the downloaded workbook; it is not uploaded to the site.

## How to prepare

1. Open **Required Topics** and filter to **P1**.
2. Select three topics only.
3. Answer the assessment prompt without reading the source page.
4. Open the linked Lab material and correct only the weak parts of your answer.
5. Use **Lead Skills** to add architecture, diagnosis, trade-offs, and ownership.
6. Add one real project example before moving the topic to **Ready**.
7. Use **Site Topics** when you need deeper component material.

A topic is **Ready** when you can explain its business purpose, process or architecture, one important design decision, one realistic failure path, and one project example.

For site maintenance, use **Needs Mapping** as a backlog. A useful Lab page should map to a career skill or have an explicit reason why it is outside interview readiness.

The reusable method is documented in [Assessment Workbook Generation](/skill-hub/productivity-execution-control/assessment-workbook-generation-working-skill/).

<script type="application/json" id="sap-lead-roadmap-data">{{ site.data.career.roadmap | jsonify }}</script>
<script type="application/json" id="sap-lead-requirements-data">{{ site.data.career.assessment_requirements | jsonify }}</script>
<script src="https://cdn.sheetjs.com/xlsx-0.20.3/package/dist/xlsx.full.min.js"></script>
<script src="/assets/js/sap-lead-assessment-workbook-v2.js"></script>
