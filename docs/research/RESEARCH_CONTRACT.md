# Research Contract

Status: living contract
Owner: Dzmitryi Kharlanau
Last updated: 2026-06-07
Purpose: define how the `/research/` section operates, what it produces, and how research material graduates into Atlas, articles, or LinkedIn posts.

## 1. Purpose

The `/research/` section is a source-backed signal-tracking layer for enterprise technology topics that matter to SAP operations, AI-assisted support, data architecture, and integration strategy. It is not a news dump. Every page must support future Atlas updates, articles, LinkedIn posts, or operational decision-making.

## 2. Content types

| Type | Purpose | Location |
|------|---------|----------|
| `research_brief` | Deep dive on a single signal, technology, or pattern. | `/research/briefs/` |
| `comparison` | Side-by-side evaluation of two or more approaches, products, or architectures. | `/research/comparisons/` |
| `watchlist` | Tracking sheet for a domain: what changed, what to monitor, open questions. | `/research/watchlists/` |
| `source_map` | Curated list of primary sources for a domain, with quality ratings. | `/research/sources/` |

## 3. Citation rules

- Every factual claim must have an inline Markdown citation.
- Every external source must be linked.
- Prefer official / primary sources.
- Do not invent product claims, dates, benchmarks, pricing, roadmaps, or comparisons.
- Do not copy private notes or expose private paths.
- Citation format: `[claim text](URL)` or footnote-style `[^1]` with linked source list.

## 4. Source quality rules

Use sources in this order:

1. **Official vendor docs / news / release notes** — highest confidence
2. **Official GitHub repos / standards / papers** — high confidence
3. **Reputable technical sources** — medium confidence (analyst reports, established blogs, vendor-neutral publications)
4. **Weak sources** — low confidence; use only as signals, not proof

Each source entry in the Sources section must include:
- link
- type: `official` | `documentation` | `release_notes` | `paper` | `repository` | `article` | `weak_signal`
- accessed date
- confidence: `high` | `medium` | `low`
- used for: brief description of what the source supports

## 5. Evidence levels

| Level | Definition |
|-------|------------|
| `high` | Multiple independent primary sources confirm the claim; official documentation exists. |
| `medium` | One primary source or several reputable secondary sources support the claim; some uncertainty remains. |
| `low` | Weak signals, analyst speculation, or single unverified source; treat as orientation only. |

## 6. Noindex rule

All research pages are draft material. Every page must include:
- `status: draft`
- `robots: noindex,follow`
- `sitemap: false`

Research pages must not appear in search indexes or sitemaps until they are promoted to Atlas or another reviewed surface.

## 7. Internal linking rule

- Link to Atlas pages only when a valid, published page exists.
- No fake links. No broken links.
- No links to private paths or unpublished drafts.
- Research pages may link to other research pages within the same section.

## 8. Public safety rule

- No private content exposed.
- No private paths exposed.
- No credentials, secrets, or internal system details.
- All content must be safe to publish on a public GitHub repository.

## 9. Promotion path

Research material graduates through this pipeline:

```
research draft
    ↓ (verified, reviewed, expanded)
Atlas update → new or updated Atlas page
    ↓ (polished, narrative-ready)
article → blog post or LinkedIn long-form
    ↓ (distilled, hook-driven)
LinkedIn post → short-form signal
```

### Automated proposal generation

A script scans all research pages and generates structured Atlas update candidates:

```sh
python3 scripts/generate_research_atlas_proposals.py
```

This produces `ai/research-atlas-proposals.json`, which contains:
- source research page metadata
- proposed action: `create`, `extend`, `ignore`, or `needs_review`
- candidate Atlas target page (if known)
- rationale and confidence
- source confidence warnings
- safety flags

Safety rules:
- Proposals never edit Atlas pages directly.
- Proposals never mark content as verified.
- Proposals never create public pages automatically.
- Research pages remain `noindex` and `sitemap: false`.

Validate existing proposals:

```sh
python3 scripts/generate_research_atlas_proposals.py --check
```

Promotion criteria:
- Evidence level upgraded from `low` to `medium` or `high`
- Sources verified and updated
- Claims tested against at least one additional primary source
- Page reviewed for public safety
- Author approves promotion

## 10. Page quality checklist

Every research page must answer:
- What changed?
- Why does it matter?
- What evidence supports it?
- What is uncertain?
- What should I do next?

Required sections:
1. Research question
2. Short answer
3. What changed
4. Evidence
5. Why it matters
6. Practical implications
7. Risks and unknowns
8. Related Atlas links
9. Next actions
10. Sources

## 11. Maintenance

- Review watchlists quarterly.
- Update briefs when new primary sources emerge.
- Archive outdated comparisons with a clear deprecation note.
- Keep source maps current; remove dead links.

## 12. Default front matter

```yaml
---
title: ""
type: research_brief | comparison | watchlist | source_map
status: draft
date: 2026-06-07
updated: 2026-06-07
robots: noindex,follow
sitemap: false
evidence_level: low | medium | high
topics: []
source_count: 0
related_atlas: []
related_research: []
next_actions: []
---
```
