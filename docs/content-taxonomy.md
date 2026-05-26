# Professional Radar Content Taxonomy

## Overview

This document defines the content types for Professional Radar site output. Not every signal becomes "news." The taxonomy determines target collection, required metadata, and public presentation.

## Content Types

### 1. `signal` (aka `radar`)
**What:** Dated external event, market update, SAP release, or AI tooling change.
**Example:** SAP Business AI Q1 2026 release, S/4HANA compatibility pack announcement.
**Target:** `_news/` collection (Jekyll) → permalink `/news/:slug/`
**Filename:** `YYYY-MM-DD-slug.md` (date-prefixed, required)
**Front matter:**
```yaml
layout: note
title: "..."
date: YYYY-MM-DD
source_url: "..."
checked_at: YYYY-MM-DD
tags: [sap, ai, signal]
confidence: high
```
**Constraints:**
- No dates in visible title, H1, or card display
- Must have `source_url` and `checked_at`
- Maximum 3 signals per day, 5 per week

### 2. `knowledge_byte`
**What:** Evergreen explanatory note, how-to, or concept explanation.
**Example:** "How SAP Clean Core affects AMS teams," "GR/IR clearing explained."
**Target:** `_notes/` collection or Atlas pages
**Filename:** `slug.md` (no date prefix)
**Front matter:**
```yaml
layout: note
title: "..."
topic: "sap-ams"
tags: [sap, knowledge-byte]
```
**Constraints:**
- No date in filename or visible title
- Must be reviewable and updatable without creating a new URL

### 3. `article`
**What:** Longer opinion, analysis, or essay with personal take.
**Example:** "Why SAP AMS teams should adopt AI now — a practitioner's view."
**Target:** `_blog/` collection → permalink `/blog/:slug/`
**Filename:** `YYYY-MM-DD-slug.md` (date-prefixed, indicates original publication)
**Front matter:**
```yaml
layout: blog
title: "..."
date: YYYY-MM-DD
author: "Dzmitryi Kharlanau"
tags: [sap, analysis, opinion]
```
**Constraints:**
- Minimum 300 words
- Must include `my_take` and `evidence_basis`
- Date in filename only, not in visible title

### 4. `page_update`
**What:** Update to an existing public page (homepage section, Atlas page, service description).
**Example:** Update `/services/sap-ams-consulting/` with new capability.
**Target:** Direct file edit (no collection)
**Filename:** Existing page file
**Constraints:**
- Must preserve existing URL
- Homepage updates require explicit approval
- Must pass homepage protection validator

## Decision Flow

```
Signal comes in
    ↓
Scoring assigns decision: news / atlas_update / social_candidate / ignore / watch
    ↓
If news → classify as content type:
    - signal → _news/
    - knowledge_byte → _notes/ or atlas/
    - article → _blog/
    - page_update → direct edit
    ↓
Generate with appropriate template and metadata
    ↓
Validate against taxonomy rules
    ↓
PR for review
```

## Migration Notes

- `_news/` currently contains signals. Future migration to `_radar/` is planned (#14).
- Until migration, signals use `_news/` with `layout: note` and clear tagging.
- Knowledge bytes can be added to `_notes/` immediately.
- Articles can be added to `_blog/` immediately.

## Validation

Each content type has specific validation rules in `scripts/validate_site_content.py`:
- Signal: date-prefixed filename, source_url, checked_at, no date in title
- Knowledge byte: no date prefix, topic tag, evergreen topic
- Article: date prefix, minimum length, my_take present
- Page update: existing path, homepage protection check

## Related

- `docs/routing-contract.md` — decision vocabulary
- Issue #14 — `_news` → `_radar` migration
- Issue #15 — classification rules in generation pipeline
