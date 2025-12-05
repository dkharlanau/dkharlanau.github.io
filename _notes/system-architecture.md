---
title: "Operating a Neubrutalist design system"
description: "Neubrutalist SAP site playbook: declarative data, reusable sections, and machine-readable feeds that keep AI copilots aligned with event-driven integrations."
eyebrow: "Practitioner note"
subtitle: "How the CV AI site stays modular, observable, and ready for AI copilots."
permalink: /notes/system-architecture/
date: 2025-02-01
published: 2025-02-01
updated: 2025-02-03
tags:
  - architecture
  - design-system
  - ai-ops
summary: "Key principles that keep the site structure extensible for new services, notes, and AI-driven experiences."
further_reading:
  - label: "Blend SAP AI/ML sidecars with event-driven clean core integrations"
    url: "/notes/ai-ml/"
  - label: "Architect composable ERP guardrails for SAP order-to-cash programmes"
    url: "/notes/composable-erp/"
  - label: "Prototype SAP mini apps that extend UX without breaking portability"
    url: "/notes/tools-mini-apps/"
---

The Neubrutalist system lives on three pillars: declarative data, componentised sections, and machine-readable exports.

1. **Declarative data** routes all repeatable copy through `_data` so homepage edits never mean touching HTML.
2. **Componentised sections** inside `_includes/sections` make each block reusable across landing pages.
3. **Machine-readable exports** in `/ai` mirror the content model so copilots can brief themselves before helping prospects.

Future updates should continue this pattern: describe content in data, reference it from a dedicated include, and emit a JSON or YAML twin in `ai/` for automation hooks.
