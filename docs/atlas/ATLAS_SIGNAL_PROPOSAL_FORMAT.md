---
layout: default
title: "Atlas Signal Proposal Format"
description: "Reviewable proposal format for signal-driven Atlas updates."
permalink: /docs/atlas/atlas-signal-proposal-format/
robots: noindex,follow
sitemap: false
---

# Atlas Signal Proposal Format

Atlas signal proposals are review artifacts. They do not edit public pages by
themselves.

Generator:

```sh
python3 scripts/propose_atlas_update.py \
  --signal path/to/enriched-signal.json \
  --match path/to/matcher-result.json \
  --output path/to/atlas-proposal.json
```

## Proposal Types

### `existing_page_update`

Use when the matcher identifies a target Atlas page above the update threshold.

Required fields:

- `signal.title`
- `signal.source_name`
- `signal.source_url`
- `signal.source_date`
- `evidence.concrete_facts`
- `target.path`
- `target.url`
- `why_this_update_belongs_there`
- `proposed_content_block`
- `source_attribution_block`
- `risks`
- `validation_checklist`

### `new_page_candidate`

Use when the source evidence is strong but no existing Atlas page clears the
review threshold.

Required fields:

- all existing-page evidence fields
- `proposed_new_page.proposed_path`
- `proposed_new_page.title`
- `proposed_new_page.atlas_section`
- `proposed_new_page.noindex_until_reviewed: true`
- `proposed_new_page.related_pages`
- `proposed_new_page.why_existing_pages_are_insufficient`

New page candidates must remain noindex until human review.

### `reject` / `needs_research`

Use when evidence is weak, matcher confidence is too low, or a page update would
be generic or duplicate.

Required fields:

- `matcher_decision`
- `why_this_update_belongs_there`
- `source_attribution_block`
- `risks`
- `validation_checklist`

Do not include a public page content block for rejected or research-needed
signals.

## Safety Flags

Every proposal includes:

```json
{
  "safety": {
    "direct_page_edits": false,
    "auto_publish": false,
    "requires_human_review": true
  }
}
```

## Quality Gate

Validate a proposal before PR review:

```sh
python3 scripts/validate_atlas_proposal.py --proposal path/to/atlas-proposal.json
```

Gate policy is documented in `docs/atlas/ATLAS_SIGNAL_QUALITY_GATES.md`.

## Sample Proposals

- `ai/atlas-proposals/examples/existing-page-update.json`
- `ai/atlas-proposals/examples/new-page-candidate.json`

These are examples only. They are not approval to edit the target pages.
