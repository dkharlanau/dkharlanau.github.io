# Professional Radar — Site Content Routing Contract

## Overview

This document defines the explicit contract between Professional Radar scoring output and site content generation.

## Decision Vocabulary

| Decision | Meaning | Target Collection |
|---|---|---|
| `ignore` | Signal is irrelevant or low quality | No action |
| `watch` | Signal is interesting but not actionable | Save for future reference |
| `news` | Signal is suitable for site publication | `_news/` Jekyll collection |
| `atlas_update` | Signal updates existing Atlas knowledge | Atlas pages |
| `social_candidate` | Signal is suitable for LinkedIn | LinkedIn drafts |

## Routing Rules

1. Scoring script emits decisions from the vocabulary above
2. Governor validates decisions against `VALID_DECISIONS` set
3. Unsupported decisions fail validation with clear error
4. Site generation maps `news` → `_news/` collection, `atlas_update` → Atlas pages
5. No manual mapping required at runtime

## Date Validation

All dates must be:
- ISO 8601 format (`YYYY-MM-DDTHH:MM:SS+00:00` or `YYYY-MM-DDTHH:MM:SSZ`)
- Not in the future relative to UTC time at validation
- Checked at item validation time

Fields validated:
- `checked_at` — when signal was processed
- `published_at` — when source content was published

## Example

```json
{
  "signal_id": "sap-clean-core-2026-05-15",
  "decision": "news",
  "decision_reason": "high_channel_potential",
  "checked_at": "2026-05-26T19:00:00Z",
  "published_at": "2026-05-15T00:00:00Z"
}
```

## Constraints

- No LinkedIn draft generation from site routing
- No autoposting
- No homepage modifications
- No service page creation
- No weakening of governor validation
