---
title: "Operating a Neubrutalist design system"
eyebrow: "Practitioner note"
subtitle: "How the CV AI site stays modular, observable, and ready for AI copilots."
date: 2025-02-01
published: 2025-02-01
updated: 2025-02-03
tags:
  - architecture
  - design-system
  - ai-ops
summary: "Key principles that keep the site structure extensible for new services, notes, and AI-driven experiences."
---

The Neubrutalist system lives on three pillars: declarative data, componentised sections, and machine-readable exports.

1. **Declarative data** routes all repeatable copy through `_data` so homepage edits never mean touching HTML.
2. **Componentised sections** inside `_includes/sections` make each block reusable across landing pages.
3. **Machine-readable exports** in `/ai` mirror the content model so copilots can brief themselves before helping prospects.

Future updates should continue this pattern: describe content in data, reference it from a dedicated include, and emit a JSON or YAML twin in `ai/` for automation hooks.
