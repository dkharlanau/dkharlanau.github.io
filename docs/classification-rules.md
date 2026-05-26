# Professional Radar Content Classification Rules

## Overview

This document defines the rules for classifying Professional Radar signals into content types before site generation.

## Classification Pipeline

```
Signal → Scoring → Decision → Classification → Target Collection
```

## Decision-to-Content-Type Mapping

| Decision | Content Type | Target | Example |
|---|---|---|---|
| `reject` | `reject` | Nothing | Low quality, irrelevant, or blocked |
| `watch` | `signal` | Save for later | Interesting but not urgent |
| `save` | `signal` | Save for later | Evidence building |
| `news` + high article potential | `article` | `_blog/` | Long-form analysis with personal take |
| `news` + knowledge potential | `knowledge_byte` | `_notes/` | Evergreen explanation |
| `news` + page update potential | `page_update` | Direct edit | Update existing page |
| `news` (default) | `signal` | `_news/` | Dated external event |

## Classification Rules

### Article (`article`)
**Trigger:**
- `site_article_potential >= 5`
- `personal_take_opportunity >= 4`
- Decision is `news`

**Requirements:**
- Minimum 300 words in `my_take`
- Must include `evidence_basis`
- Must have `confidence_level`
- Requires explicit approval before publishing

**Target:** `_blog/` collection

### Knowledge Byte (`knowledge_byte`)
**Trigger:**
- `knowledge_byte_potential >= 4`
- No `published_at` date (evergreen)
- Decision is `news`

**Requirements:**
- Must have `canonical_topic`
- No date in filename
- Must be reviewable and updatable

**Target:** `_notes/` collection or Atlas pages

### Signal (`signal`)
**Trigger:**
- Decision is `news`
- Does not meet article or knowledge byte criteria

**Requirements:**
- Must have `source_url`
- Must have `date` / `checked_at`
- Maximum 3 per day, 5 per week

**Target:** `_news/` collection (future: `_radar/`)

### Page Update (`page_update`)
**Trigger:**
- `page_update_potential >= 4`
- Decision is `news`

**Requirements:**
- Must specify `target_page`
- Must preserve existing URL
- Homepage updates require explicit approval

**Target:** Direct file edit

## Examples

### SAP Cloud ALM Clean Core Dashboard
- **Decision:** `news`
- **Classification:** `signal` (dated release announcement)
- **Alternative:** `knowledge_byte` if explaining Clean Core concept

### SAP Compatibility Packs Final Transition
- **Decision:** `news`
- **Classification:** `signal` (dated policy change)
- **Alternative:** `knowledge_byte` if explaining transition timeline

### Joule OTC Automation Overview
- **Decision:** `news`
- **Classification:** `knowledge_byte` (evergreen capability explanation)
- **Exception:** `signal` if tied to specific release date

## Validation

The validator checks:
1. `content_type` is present when `decision == "news"`
2. `content_type` is one of: `signal`, `knowledge_byte`, `article`, `page_update`, `reject`, `save`, `watch`
3. Content-type-specific rules (see above)

## Related

- `docs/content-taxonomy.md` — Content type definitions
- `docs/routing-contract.md` — Decision vocabulary
