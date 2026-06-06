---
layout: default
title: "Signal-to-Atlas Schema"
description: "Structured data contract and states for signal-driven Atlas update decisions."
permalink: /docs/atlas/signal-to-atlas-schema/
robots: noindex,follow
sitemap: false
---

# Signal-to-Atlas Schema

Machine-readable schema:

```text
ai/signal-to-atlas.schema.json
```

This contract defines how an enriched professional signal becomes an Atlas page
decision. It is intentionally compact and review-first: schema compliance does
not publish a page.

## State Model

```text
RAW_SIGNAL -> ENRICHED_SIGNAL -> MATCHED_TO_ATLAS -> UPDATE_PROPOSED -> REVIEW_READY -> APPROVED
```

Terminal or holding states:

- `REJECTED` - the signal should not update Atlas.
- `NEEDS_RESEARCH` - source evidence, classification, or matching is not strong
  enough for an update.

State meanings:

| State | Meaning | Required next action |
|---|---|---|
| `RAW_SIGNAL` | Signal metadata exists but source-body evidence is not attached. | Enrich source evidence. |
| `ENRICHED_SIGNAL` | Source body was opened and concrete facts were extracted. | Classify and match against the compact index. |
| `MATCHED_TO_ATLAS` | Candidate Atlas pages were ranked. | Decide update, new page candidate, reject, or needs research. |
| `UPDATE_PROPOSED` | A structured proposal exists. | Run quality gates. |
| `REVIEW_READY` | Proposal passed gates and is ready for human PR review. | Open/review PR. |
| `APPROVED` | Human approval exists. | Apply in a scoped PR branch only. |
| `REJECTED` | Signal is not useful/safe for Atlas. | Record reason; do not draft page content. |
| `NEEDS_RESEARCH` | More source or matching work is needed. | Recheck source or improve metadata; do not draft page content. |

## Required Blocks

Every record has these blocks:

- `signal` - title, source name, source URL, source date, date checked, source type.
- `evidence` - source-body flag, facts, product names, named components, numbers, examples.
- `classification` - SAP domain, business process, technology area, operational implication, tags.
- `decision` - target decision, decision reason, review status, optional rejection reason.

## Target Decisions

### `update_existing_page`

Use when an existing Atlas page clearly fits the signal.

Required:

- at least one `atlas_candidates` entry
- `proposed_update`
- `evidence.source_body_opened: true`
- at least two `evidence.concrete_facts`

The proposal must include target path, section heading, compact content block,
source attribution block, risks, and validation checklist.

### `create_new_page_candidate`

Use only when a signal is strong and no existing page covers the topic.

Required:

- `atlas_candidates` with nearest related pages, even if scores are low
- `proposed_new_page`
- `proposed_update`
- `evidence.source_body_opened: true`
- at least two `evidence.concrete_facts`

New page candidates must set `noindex_until_reviewed: true` and explain why
existing pages are insufficient.

### `reject`

Use when the signal is not useful, duplicates existing content, has weak
evidence, or would create generic public content.

Required:

- `decision.rejection_reason`

Do not include public page content.

### `needs_research`

Use when the signal may be useful but the source body, facts, or page match are
not strong enough yet.

Required:

- `decision.rejection_reason`

Do not include public page content until evidence is stronger.

## Title-Only Prevention

A title-only or snippet-only signal cannot reach `update_existing_page` or
`create_new_page_candidate`.

The schema enforces this by requiring, for both proposal decisions:

- `evidence.source_body_opened: true`
- at least two concrete facts
- source URL and source date
- source attribution block

## Review Safety

Schema-valid records are still proposals. Agents must:

- avoid direct pushes to `main`
- avoid automatic publishing
- keep weak signals in `needs_research` or `reject`
- avoid creating new pages when an existing Atlas page can absorb the update
- keep proposed content source-backed and compact
- avoid private draft paths, raw dumps, local config, secrets, and runtime logs

## Validation

Schema contract tests:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_signal_to_atlas_schema.py
```

Public repo hygiene:

```sh
python3 scripts/check_public_repo.py
```
