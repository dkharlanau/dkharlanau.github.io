# Professional Radar Templates

Status: internal reference
Purpose: reusable templates for agent-assisted site updates
Created for: issue #4
Last updated: 2026-05-26

## How to use these templates

1. Read `AGENTS.md`, `docs/content/author-editorial-profile.md`, `docs/site-content-design-contract.md`, and the relevant page template or collection rules before creating or editing article-like content.
2. Pick the template that matches the update type.
3. Copy the template file, replace all bracketed placeholders, and remove the `<!-- TEMPLATE: ... -->` comments.
4. Follow the content placement rules in `docs/site-content-design-contract.md` before choosing a target page.
5. Use `_data/atlas_index.yml` to find the correct target page by topic cluster.
6. Remove the `noindex` front matter only when the content is reviewed and ready for public indexing.

## Template inventory

| Template | Use when | Target location |
|---|---|---|
| `news-item.md` | A dated professional signal needs a short entry | News section (when created) or blog collection |
| `atlas-diagnostic-page.md` | A new SAP diagnostic page is needed | `atlas/diagnostics/<slug>.md` |
| `atlas-fact-update.md` | A durable Atlas page needs a factual correction or addition | Relevant `atlas/**/*.md` page |
| `source-addition.md` | A page needs a new source, citation, or reference | Any public knowledge page |
| `practical-process-note.md` | A new practical pattern, checklist, or process note is ready | Relevant `atlas/**/*.md` or `notes/` page |
| `weekly-signal-summary.md` | A weekly digest of signals is ready | News section or blog collection |

## Common front matter fields

All templates use these conventions:

```yaml
---
layout: default
title: "Clear, specific title"
description: "One-line summary for SEO and sharing."
permalink: /path/to/page/
last_modified_at: YYYY-MM-DD
robots: noindex,follow   # Remove only when reviewed and verified
sitemap: false           # Remove only when reviewed and verified
---
```

## Content rules

- Read the [Author and Editorial Profile](../content/author-editorial-profile.md) before writing or editing. It is mandatory input, not optional style advice.
- Use the profile as a decision system for voice, density, and what to remove. Do not copy phrases or repeat prior article patterns mechanically.
- No generic AI prose, filler, inflated adjectives, decorative introductions, or forced conclusions.
- No private or client-specific data. Use generic process language.
- No hype, no exclamation points, no promotional fluff.
- One claim per paragraph. Short sentences.
- Every factual claim needs a source.
- Confidence levels: `high` (verified against source), `medium` (plausible, one source), `low` (speculative, needs verification).
- An author perspective may appear near the end when it adds judgment, caution, or interpretation. It must be natural, integrated, and optional. Do not force it, do not use cliché labels such as "My take" or "Author's note" by default, and do not invent personal stories.
- Tag examples: `sap-ams`, `integration`, `master-data`, `ai-ops`, `diagnostics`, `o2c`, `p2p`.

## Article creation checklist

Before submitting a new or updated article:

- [ ] Profile read — `docs/content/author-editorial-profile.md` and `AGENTS.md` reviewed.
- [ ] Page type understood — template and collection rules match the content type.
- [ ] Facts/source boundaries respected — every factual claim has a source; no invented credentials, incidents, or client details.
- [ ] Author perspective decided — added only if it improves the page; omitted if it would add noise. No cliché labels such as "My take" or "Author's note" by default.
- [ ] No generic AI filler — vague adjectives, decorative introductions, repeated patterns, and forced conclusions removed.

## Sample output

See the bottom of each template file for a filled example.
