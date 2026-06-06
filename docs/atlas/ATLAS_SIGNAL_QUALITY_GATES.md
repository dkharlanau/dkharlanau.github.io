---
layout: default
title: "Atlas Signal Quality Gates"
description: "Quality gates for signal-driven Atlas update proposals."
permalink: /docs/atlas/atlas-signal-quality-gates/
robots: noindex,follow
sitemap: false
---

# Atlas Signal Quality Gates

Quality gates prevent weak, duplicate, generic, or unsafe signal proposals from
becoming Atlas content.

Validator:

```sh
python3 scripts/validate_atlas_proposal.py --proposal path/to/atlas-proposal.json
```

## Required Gates

For `existing_page_update` and `new_page_candidate` proposals:

- source URL is present
- source date is present
- source body was opened
- at least two concrete facts are present
- proposed content block is compact and source-backed
- source attribution includes the source URL
- no private paths, local files, secrets, raw dumps, or runtime logs
- content does not use generic AI/SAP commentary

Additional gates for `existing_page_update`:

- target Atlas page exists
- proposed content is not already present in the target page

Additional gates for `new_page_candidate`:

- proposed path does not already exist
- `noindex_until_reviewed` is true
- no existing Atlas candidate clears the update threshold

Additional gates for `reject` and `needs_research`:

- no public page content block is present

## Outcomes

- `passed` - proposal can move to PR review.
- `rejected` - proposal should not become content without revision.
- `needs_research` - source/matching evidence is insufficient.

Passing gates does not publish content. It only means the proposal is safe to
review in a PR.

## Examples

Good evidence-backed update:

```sh
python3 scripts/validate_atlas_proposal.py \
  --proposal ai/atlas-proposals/examples/existing-page-update.json
```

New page candidate:

```sh
python3 scripts/validate_atlas_proposal.py \
  --proposal ai/atlas-proposals/examples/new-page-candidate.json
```

The new-page candidate example should remain a candidate until human review
confirms that no existing page should absorb the content.
