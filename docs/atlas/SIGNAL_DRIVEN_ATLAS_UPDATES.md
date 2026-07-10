---
layout: default
title: "Signal-Driven Atlas Update Workflow"
description: "Safe v1 workflow for matching professional signals to Atlas page updates."
permalink: /docs/atlas/signal-driven-atlas-updates/
robots: noindex,follow
sitemap: false
---

# Signal-Driven Atlas Update Workflow

This workflow lets Product Radar signals propose safe, source-backed updates to
Atlas pages without directly publishing content.

Core flow:

```text
signal -> classify -> match Atlas page -> propose update -> quality gates -> PR review
```

## Current Atlas Source Of Truth

Public Atlas pages live under `atlas/`. Article pages are discovered from
frontmatter by `scripts/generate_atlas_artifacts.py`.

The current public discovery artifacts are:

- `atlas/manifest.json` - full machine-readable Atlas page manifest.
- `ai/atlas-compact-index.json` - compact signal-matching index for agents.
- `ai/rag/related.json` - related-page graph from public frontmatter.
- `llms-full.txt` - full text for reviewed and verified Atlas pages only.

Agents must not scan generated site output, local reports, private notes, raw
backlogs, export archives, runtime logs, or scratch files for signal matching.

## Atlas Page Metadata

Atlas article pages intended for matching should expose these frontmatter
fields when available:

- `title`
- `description`
- `permalink`
- `atlas_section`
- `domain`
- `subdomain`
- `concept_type`
- `sap_area`
- `business_process`
- `status`
- `verified`
- `last_reviewed`
- `tags`
- `related`

The compact index adds extracted headings and matching terms, but it does not
store full page bodies.

## Compact Index

Stable path: `ai/atlas-compact-index.json`

This public index contains only reviewed, verified, indexable Atlas pages. It
does not expose review candidates or noindex page metadata. Before proposing a
new draft, also search the repository source to avoid duplicating an existing
review candidate.

The compact index includes:

- public source path
- canonical production URL
- title and description
- Atlas section
- domain, subdomain, concept type
- SAP area and business process
- reviewed status, verification flag, last reviewed date
- tags
- headings
- SAP domain/process keywords
- compact matching terms

Regenerate all Atlas discovery artifacts, including the compact index:

```sh
python3 scripts/generate_atlas_artifacts.py
```

Validate that committed artifacts are fresh:

```sh
python3 scripts/generate_atlas_artifacts.py --check
```

## Signal Classification

Structured signal decision records use `ai/signal-to-atlas.schema.json`.
The state and field policy is documented in
`docs/atlas/SIGNAL_TO_ATLAS_SCHEMA.md`.

For v1, classify each enriched signal with simple public metadata:

- source name, URL, publication date, author or organization when available
- source type: official vendor, documentation, customer story, analyst/news, community, internal proposal
- SAP domain: S/4HANA, BTP, MM, SD, EWM, TM, Ariba, MDG, AMS, integration, data quality, AI operations
- business process: procure to pay, order to cash, support operations, master data, logistics, finance, security
- technology area: integration, workflow automation, AI agents, release management, security notes, developer tooling
- operational implication: support cost, downtime risk, traceability, handover, testing, ownership, integration risk

Title-only and snippet-only signals cannot produce Atlas updates.

## Matching Policy

Use simple index matching for v1:

1. Match signal terms against page title, tags, domain fields, SAP area,
   business process, headings, and compact matching terms.
2. Prefer existing-page updates when a relevant page exists.
3. Create a new-page candidate only when no existing page covers the topic and
   source evidence is strong enough.
4. Reject or mark `needs_research` when source evidence is weak, the match is
   ambiguous, or the proposed update would duplicate existing content.

RAG/vector search is not part of v1. It should be reconsidered only after
matcher failures show that better frontmatter/tags are insufficient.
The v1/v2 decision is documented in
`docs/atlas/ATLAS_SIGNAL_RAG_EVALUATION.md`.

Dry-run matcher command:

```sh
python3 scripts/match_atlas_signal.py \
  --signal path/to/enriched-signal.json \
  --index ai/atlas-compact-index.json \
  --output path/to/matcher-result.json
```

The matcher returns ranked candidates with confidence scores and reasons. It
does not load full page bodies and does not edit public pages.

## Proposal Types

Proposal output is documented in
`docs/atlas/ATLAS_SIGNAL_PROPOSAL_FORMAT.md`.

Dry-run proposal command:

```sh
python3 scripts/propose_atlas_update.py \
  --signal path/to/enriched-signal.json \
  --match path/to/matcher-result.json \
  --output path/to/atlas-proposal.json
```

### Existing Page Update

Use when a signal adds a source-backed fact, example, risk, checklist item, or
clarification to an existing Atlas page.

Required evidence:

- source URL
- source name
- source date or date checked
- extracted facts
- relevance note explaining why the signal belongs on the target page
- proposed compact content block
- validation checklist

### New Page Candidate

Use only when the signal exposes a distinct topic not covered by existing Atlas
pages.

Required evidence:

- all existing-page evidence fields
- proposed slug/path
- why related pages are insufficient
- expected Atlas section
- noindex/review status until verified
- related page candidates
- reason this should not be a short addition to an existing page

### Reject Or Needs Research

Use when:

- source body was not opened
- source URL/date attribution is missing
- extracted facts are missing
- topic is already covered
- signal is generic AI/SAP commentary
- proposal depends on private notes or local draft paths
- source evidence is too weak for a public page

## Quality Gates

Quality gates are documented in
`docs/atlas/ATLAS_SIGNAL_QUALITY_GATES.md`.

Dry-run quality command:

```sh
python3 scripts/validate_atlas_proposal.py --proposal path/to/atlas-proposal.json
```

Before a PR, a proposal must pass these gates:

- source URL and date are present
- source-body evidence exists
- at least two concrete extracted facts are present
- target page exists, or new-page rationale explains why no existing page fits
- proposed content is compact and specific
- update explains operational relevance to the Atlas page
- no private paths, local files, secrets, raw dumps, or runtime logs
- no duplicate page creation
- no generic AI/SAP commentary
- site artifacts validate

## Review And PR Boundary

PR review workflow is documented in
`docs/atlas/ATLAS_SIGNAL_PR_WORKFLOW.md`.

Signal-driven updates are proposal-first. An agent may open a PR, but must not
push directly to `main` and must not rely on GitHub Pages publishing until a
human review/merge happens.

PRs should include:

- source signal(s)
- target Atlas page(s)
- files changed
- evidence summary
- why the update belongs there
- quality gates passed
- validation commands run
- safety note: no private drafts, no direct main push, no automatic publishing

## Validation Commands

Minimum for index/workflow changes:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_atlas_artifacts.py
python3 scripts/generate_atlas_artifacts.py --check
python3 scripts/check_public_repo.py
```

Research-to-Atlas proposal validation:

```sh
python3 scripts/generate_research_atlas_proposals.py --check
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_research_atlas_proposals.py
```

Before PRs that change public pages:

```sh
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

## Architecture Answers

1. Current Atlas structure: public content lives under `atlas/`; generated
   discovery artifacts live under `atlas/`, `ai/`, and `llms-full.txt`.
2. Metadata: frontmatter carries title, description, permalink, Atlas section,
   domain/process fields, status, verification, tags, and related links.
3. Classification: use SAP domain, business process, technology area, source
   type, and operational implication.
4. Search: use `ai/atlas-compact-index.json`, not full site scans.
5. RAG: not needed for v1; evaluate later from matcher failures.
6. Evidence: URL, source, date, facts, attribution, target-page rationale.
7. Gates: block title-only, duplicate, generic, weakly sourced, or private-path
   proposals.
8. Validation: artifact check, tests, public-repo hygiene, and Jekyll/link/SEO
   checks for page changes.
