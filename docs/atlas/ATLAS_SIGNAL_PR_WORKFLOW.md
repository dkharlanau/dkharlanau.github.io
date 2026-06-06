---
layout: default
title: "Atlas Signal PR Workflow"
description: "Human-review and PR workflow for approved signal-driven Atlas updates."
permalink: /docs/atlas/atlas-signal-pr-workflow/
robots: noindex,follow
sitemap: false
---

# Atlas Signal PR Workflow

Signal-driven Atlas updates are review-first. A proposal can recommend content;
it cannot publish content by itself.

## Review-Ready Proposal Location

Generated examples live in:

```text
ai/atlas-proposals/examples/
```

Review-ready proposals for real updates may be committed in a PR under:

```text
ai/atlas-proposals/review/
```

Scratch proposals, local experiments, failed matcher outputs, and raw signal
logs must not be committed.

## Approval Boundary

A proposal is approved only when a human reviewer accepts it in PR review or an
equivalent explicit review note. Tool output alone is not approval.

Required before applying a proposal:

1. Matcher result exists.
2. Proposal JSON exists.
3. `scripts/validate_atlas_proposal.py` passes.
4. Target page or new-page candidate path is reviewed.
5. Human reviewer approves the proposal or the PR.

## Applying Approved Proposals

Existing page update:

1. Start from synced `main`.
2. Create a focused branch.
3. Re-run proposal quality gates.
4. Edit only the target Atlas page and directly related navigation/data files if
   needed.
5. Preserve source attribution in the page content.
6. Keep the update compact; do not rewrite the whole page.
7. Run validation commands.
8. Open a PR with the Atlas signal update template.

New page candidate:

1. Start from synced `main`.
2. Create a focused branch.
3. Re-run proposal quality gates.
4. Confirm existing pages are insufficient.
5. Create the new page with `robots: noindex,follow` and `sitemap: false`
   unless a human reviewer explicitly approves indexing.
6. Add related links back to existing Atlas pages.
7. Run validation commands.
8. Open a PR with the Atlas signal update template.

## PR Body Requirements

Use `.github/PULL_REQUEST_TEMPLATE/atlas-signal-update.md`.

Every PR must include:

- source signal(s)
- target Atlas page(s)
- files changed
- evidence summary
- why the update belongs there
- quality gates passed
- validation commands run
- safety note: no private drafts, no direct main push, no automatic publishing

## Required Validation

For proposal-only PRs:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_atlas_update_proposals.py tests/test_atlas_proposal_quality.py
python3 scripts/check_public_repo.py
```

For PRs that apply page changes:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/generate_atlas_artifacts.py --check
python3 scripts/check_public_repo.py
PATH="/opt/homebrew/opt/ruby/bin:/opt/homebrew/bin:/opt/homebrew/sbin:$PATH" bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

## Hard Stops

Stop and leave the proposal in review if:

- source-body evidence is missing
- the proposal fails quality gates
- a new page duplicates an existing page
- the update requires private notes or local paths
- the branch is not based on current `main`
- reviewer approval is missing

No direct pushes to `main`. No unreviewed page creation. No automatic GitHub
Pages publishing beyond the normal reviewed merge flow.
