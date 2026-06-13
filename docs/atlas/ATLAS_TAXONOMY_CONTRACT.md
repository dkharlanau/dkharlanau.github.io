# Atlas Taxonomy Contract

## Purpose

This contract defines the Atlas taxonomy backbone for SAP S/4HANA and the modern SAP product/technology landscape. It governs how new pages are classified, what frontmatter they must carry, and the quality bar for inclusion.

## Scope

- SAP S/4HANA functional domains and process areas
- SAP products and cloud services
- SAP technologies, platforms, and integration mechanisms
- Cross-domain maps that connect the above

## Page Types

| Type | Purpose | Example |
|------|---------|---------|
| `map` | Cross-domain navigation and landscape overview | `sap-s4hana-landscape-map` |
| `domain` | Functional area within S/4HANA or SAP ecosystem | `sales`, `sourcing-and-procurement` |
| `product` | Named SAP product or service | `sap-s4hana`, `sap-btp` |
| `technology` | Technical component, framework, or protocol | `rap`, `odata`, `cds-views` |
| `integration` | Integration mechanism or middleware pattern | `business-events`, `idoc` |
| `diagnostic` | Support-oriented troubleshooting pattern | Existing diagnostics section |

## Required Frontmatter Fields

All Atlas taxonomy pages MUST include:

```yaml
layout: default
title: "..."
description: "..."
permalink: "/atlas/.../"
atlas_section: maps | sap | diagnostics | concepts | data-quality | ai-operations | automation
domain: "..."
subdomain: "..."
concept_type: map | domain | product | technology | integration | diagnostic
sap_area: "..."
business_process: "..."
status: needs_verification | reviewed
verified: true | false
last_reviewed: YYYY-MM-DD
author: Dzmitryi Kharlanau
tags:
  - tag-one
  - tag-two
related:
  - /atlas/.../
```

## Indexing Rules

| Status | `verified` | `robots` | `sitemap` |
|--------|-----------|----------|-----------|
| reviewed | true | `index,follow,max-snippet:-1,max-image-preview:large,max-video-preview:-1` | true (default) |
| needs_verification | false | `noindex,follow` | false |

All new taxonomy skeleton pages start as `status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`.

## Quality Bar

1. **No generic article spam.** Every page must have a specific analytical purpose.
2. **No SAP Help text copying.** Descriptions must be analytical, not documentation excerpts.
3. **Compact and analytical.** Each page answers: what it is, business purpose, landscape position, main objects, integrations, extension points, monitoring/diagnostics, strong sides, weak sides/risks, AMS incident patterns, related Atlas links, source references, verification limitations.
4. **Source-backed hierarchy.** Parent/child relationships in `taxonomy.yml` must reference source documents in `sources.yml`.
5. **No private corpus exposure.** No `source_files`, `private-source`, `kb-drafts`, `/Users/`, or `.env` references.
6. **No duplicate pages.** Check existing Atlas pages before creating new ones.
7. **No homepage modification.** Taxonomy pages live under `/atlas/` only.
8. **Follow the author/editorial profile.** Before drafting or editing, read `docs/content/author-editorial-profile.md`. Use it as a decision system for voice, density, and practical framing, but do not use it to replace source-backed facts or change indexing policy.

## Machine-Readable Taxonomy

The canonical taxonomy lives in `data/atlas/taxonomy.yml`. Each entry:

```yaml
- id: unique-kebab-case-id
  type: map | domain | product | technology | integration
  parent: id-of-parent-or-null
  title: "Human-readable title"
  permalink: "/atlas/section/slug/"
  source_refs:
    - source-id-from-sources-yml
  related_products:
    - product-id
  related_technologies:
    - technology-id
  related_diagnostics:
    - diagnostic-page-permalink
  status: skeleton | draft | reviewed
```

## Source Registry

The canonical source registry lives in `data/atlas/sources.yml`. Each entry:

```yaml
- id: unique-source-id
  title: "Source title"
  url: "https://..."
  type: pdf | web | documentation
  publisher: "SAP SE"
  version: "2025"
  scope: "public-safe topic discovery and source-backed hierarchy"
  accessed_at: YYYY-MM-DD
  notes: "Used for taxonomy hierarchy only; no content copied"
```

## Agent Extension Guidelines

When extending this taxonomy:

1. Read this contract first.
2. Check `data/atlas/taxonomy.yml` for existing IDs to avoid duplicates.
3. Check `data/atlas/sources.yml` for existing sources before adding new ones.
4. Create pages with `status: needs_verification`, `verified: false`.
5. Run `scripts/generate_atlas_artifacts.py --check` after adding pages.
6. Run `scripts/check_public_repo.py` before committing.
7. Update `tests/test_atlas_artifacts.py` counts if the test has hardcoded expectations.
8. Do not commit until all validation passes.

## Verification Lifecycle

```
skeleton → needs_verification → reviewed
     ↑___________________________↓
          (periodic re-review)
```

- `skeleton`: page exists with minimal structure, no claims verified
- `needs_verification`: content drafted, claims need source verification
- `reviewed`: claims verified against public sources, safe to index

## Safety Confirmations

- All new pages in this taxonomy are unverified review candidates.
- No private paths or credentials are exposed.
- No homepage or existing reviewed pages are modified.
- Source references are public URLs only.
- The SAP S/4HANA 2025 FSD is used for topic discovery and hierarchy only; no content is copied from it.
