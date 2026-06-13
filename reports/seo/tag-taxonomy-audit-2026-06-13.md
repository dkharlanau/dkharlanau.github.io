# Tag / Taxonomy Audit Report

**Date:** 2026-06-13
**Branch:** `feat/seo-visibility-swarm`
**Site:** https://dkharlanau.github.io

---

## Summary

Tags are used inconsistently across the site. Atlas pages use kebab-case tags well, but some pages lack tags entirely, and there is no unified taxonomy. This is not an immediate SEO blocker, but normalizing tags will support future tag-index pages and internal navigation.

---

## Tag Coverage by Section

| Section | Pages with tags | Pages without tags | Quality |
|---------|----------------|-------------------|---------|
| Atlas (concepts) | ~25 | ~30 | Mixed — some have 3–5 good tags, some have none |
| Atlas (diagnostics) | ~55 | ~0 | Good — most have diagnostic + SAP module tags |
| Atlas (maps) | ~10 | ~0 | Good — landscape + domain tags |
| Atlas (sap) | ~50 | ~0 | Good — technology + domain tags |
| Atlas (ai-ops) | ~5 | ~0 | Good |
| Atlas (automation) | ~5 | ~0 | Good |
| Atlas (data-quality) | ~3 | ~0 | Good |
| Skill Hub | ~82 | ~0 | Good — most have working-skill + domain tags |
| Research | ~40 | ~0 | Mixed — some have tags, some are sparse |
| Scenarios | ~12 | ~0 | Good |

---

## Current Tag Patterns (sampled)

### SAP Domain Tags (good)

- `sap-ams`, `sap-sd`, `sap-mm`, `sap-mdg`, `sap-bp`, `sap-cvi`, `sap-idoc`, `sap-integration`, `sap-master-data`, `sap-procurement`, `sap-inventory`, `sap-pp`, `sap-ewm`, `sap-tm`, `sap-ariba`, `sap-btp`, `sap-s4hana`, `sap-ibp`

### Content Type Tags (good)

- `diagnostics`, `incident-triage`, `workflow`, `checklist`, `deep-dive`, `landscape-map`, `concept`, `review-candidate`, `verified`

### AI / Agent Tags (good)

- `ai-agents`, `agentic-workflows`, `knowledge-capture`, `support-automation`, `llmops`, `rag`, `sidecar-ai`

### Process / Integration Tags (good)

- `order-to-cash`, `procure-to-pay`, `batch-processing`, `event-driven`, `data-mesh`, `api-contracts`

### Issues Found

| Issue | Count | Example |
|-------|-------|---------|
| Missing tags | ~30 | `atlas/concepts/*.md` pages found in Atlas audit |
| Too many tags (>10) | ~5 | Some landscape maps have 8–10 tags |
| Duplicate concept | 2 | `delivery` vs `sap-le-delivery` |
| Broad tag | ~10 | `sap` is too broad when `sap-sd` exists |
| Inconsistent casing | ~3 | `SAP-SD` vs `sap-sd` (should be lowercase kebab-case) |

---

## Recommended Normalized Taxonomy

### SAP Domain Tags (11 tags)

```
sap-ams, sap-sd, sap-mm, sap-mdg, sap-bp, sap-cvi, sap-idoc,
sap-integration, sap-master-data, sap-procurement, sap-inventory
```

### Content Type Tags (7 tags)

```
diagnostics, incident-triage, workflow, checklist, deep-dive,
review-candidate, verified
```

### AI / Operating System Tags (5 tags)

```
ai-agents, agentic-workflows, knowledge-capture, support-automation, llmops
```

### Process Tags (6 tags)

```
order-to-cash, procure-to-pay, batch-processing, event-driven,
data-mesh, api-contracts
```

### Rules

- **3–7 tags per page.** No more than 7.
- **Lowercase kebab-case.** Example: `sap-sd`, not `SAP-SD` or `sap_sd`.
- **No tag spam.** Do not add tags just for SEO keyword stuffing.
- **One SAP domain tag per page.** If a page spans multiple domains, pick the primary one and add `sap-integration` if needed.
- **One content type tag per page.** Pick the best fit.
- **Tags support navigation.** Future tag index pages will group by tag.

---

## Immediate Actions

1. **Add missing tags** to the 30 Atlas concepts pages that lack them (from `atlas-indexation-candidates-2026-06-13.md`).
2. **Normalize casing** on any tags with uppercase or underscores.
3. **Remove redundant broad tags** (`sap` when `sap-sd` is present).
4. **Do not create tag index pages** in this PR — that is a follow-up feature.

---

## Tag Index Pages (Future)

When tag index pages are built, they should:

- Only show **verified** pages for each tag.
- Include a `noindex` tag filter view for internal use.
- Use `CollectionPage` schema with `ItemList`.
- Be linked from the Atlas index and Skill Hub index.

---

## Safety

- Tags do not affect indexing directly.
- Tags are for internal organization and future navigation.
- No private paths are exposed in tags.
- No client names or proprietary terms are used in tags.
