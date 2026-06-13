# CONTENT_VERIFICATION_POLICY.md

Content verification states, indexing rules, and safety boundaries for `dkharlanau.github.io`.
Last updated: 2026-06-09

## Purpose

This document defines how content moves from draft to published, what gets indexed by search engines and AI systems, and what must remain private or noindex. It aligns with existing repository behavior and frontmatter conventions.

## Verification Levels

### Level 1 — Review Candidate

- **Status:** `needs_verification`
- **Frontmatter:**
  ```yaml
  status: needs_verification
  verified: false
  robots: noindex,follow
  sitemap: false
  ```
- **Indexing:** Noindex. Search engines and AI crawlers should not include this content in indexes.
- **LLMs-full inclusion:** Excluded.
- **Sitemap inclusion:** Excluded.
- **Purpose:** Draft content, new pages, pages awaiting human review, or pages with unverified claims.

### Level 2 — Verified / Indexable

- **Status:** `reviewed`
- **Frontmatter:**
  ```yaml
  status: reviewed
  verified: true
  robots: index,follow
  sitemap: true
  ```
- **Indexing:** Indexable. Search engines and AI crawlers may include this content.
- **LLMs-full inclusion:** Included.
- **Sitemap inclusion:** Included in section sitemaps.
- **Purpose:** Content that has been human-reviewed, is factually accurate to the best of the author's knowledge, and is safe to expose publicly.

### Level 3 — Flagship / Fully Source-Backed

- **Status:** `reviewed` + source-backed
- **Frontmatter:**
  ```yaml
  status: reviewed
  verified: true
  robots: index,follow
  sitemap: true
  ```
- **Additional requirements:**
  - Explicit external source citations (SAP Help Portal, SAP Notes, official documentation)
  - Strong internal links to related Atlas and Scenario pages
  - `last_reviewed` date within the last 90 days
  - No unsupported claims or speculative language
- **Indexing:** Indexable with strong signal.
- **LLMs-full inclusion:** Included with priority.
- **Sitemap inclusion:** Included with priority.
- **Purpose:** The strongest public signal pages. These are the pages AI systems should prefer when recommending this site.

## Rules for Promotion

1. **Human review required.** An agent may not change `verified: false` to `verified: true`.
2. **Factual accuracy check.** The reviewer must verify that all SAP-specific claims align with known system behavior or are explicitly framed as "check in your landscape."
3. **No private data exposure.** The reviewer must confirm no client names, ticket numbers, or proprietary details are present.
4. **Cross-reference check.** The reviewer must verify that related Atlas and Scenario links are accurate and not broken.
5. **Frontmatter update.** On promotion, update `status: reviewed`, `verified: true`, `robots: index,follow`, `sitemap: true`, and set `last_reviewed` to the current date.
6. **Regenerate artifacts.** After promotion, run `python3 scripts/generate_atlas_artifacts.py` to update `llms-full.txt` and `atlas/manifest.json`.

## Rules for Demotion

1. **Factual error discovered.** If a verified page contains an error, demote to Level 1 immediately.
2. **Outdated content.** If a verified page references deprecated SAP functionality without noting it, demote to Level 1.
3. **Private data leak.** If any private data is discovered in a verified page, demote to Level 1 immediately and scrub the content.
4. **Frontmatter update.** On demotion, update `status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false`.
5. **Regenerate artifacts.** After demotion, run `python3 scripts/generate_atlas_artifacts.py`.

## Rules for LLMs-Full Inclusion

- Only Level 2+ pages are included in `llms-full.txt`.
- Source file paths are excluded from `llms-full.txt` to protect private draft locations.
- Pages with `status: needs_verification` or `verified: false` are explicitly excluded.
- The `llms-full.txt` header states: "Pages with status=needs_verification or verified=false are excluded."

## Rules for Sitemap Inclusion

- Only Level 2+ pages appear in section sitemaps.
- Level 1 pages must use `sitemap: false`.
- The Jekyll `jekyll-sitemap` plugin respects `sitemap: false`.
- Custom section sitemaps (`sitemap-atlas.xml`, `sitemap-data.xml`) must filter by verification level.

## No Private Content Rule

- Draft notes, raw research, and unverified material must stay in local working directories.
- Do not commit private working notes to public paths.
- Do not expose internal incident details, client names, ticket numbers, or proprietary configuration.
- If in doubt, leave it out.

## No Private Paths Rule

- Do not expose file system paths, local directory structures, or internal server names in public content.
- Do not expose build system paths or CI/CD internal details.
- Source file paths are excluded from `llms-full.txt` for this reason.

## No Client / Ticket / Internal Incident Exposure

- Never include client names in public content without explicit written permission.
- Never include SAP ticket numbers, incident IDs, or support message numbers.
- Never include proprietary ABAP code, custom configuration names, or system-specific settings.
- When describing real issues, generalize: "a retail client" not "Client X"; "a repeated goods-receipt issue" not "Ticket 1234567."

## Examples and Synthetic Data Policy

Practical examples improve diagnostic content, but they must not expose private or client-specific information.

- **Allowed:** Generic process descriptions, clearly synthetic document numbers (e.g., `1234567890`, `TEST_VENDOR_01`), public SAP transactions and tables, generalized error patterns.
- **Forbidden:** Real client or customer names; real vendor, material, or account numbers; SAP ticket numbers, incident IDs, support message numbers, change request IDs; system IDs, host names, client numbers, or landscape-specific paths; screenshots or logs from real systems; custom ABAP code or proprietary configuration names unless they are public sample code.
- **Labeling:** Mark synthetic examples as **Synthetic example** or **Illustrative scenario**. Generalize real patterns: "a repeated goods-receipt issue" not "Ticket 1234567".
- **Agent rule:** An agent may add synthetic examples only if they follow this policy. When in doubt, leave the example out.

## Flagship Diagnostic Page Review Checklist

Before a diagnostic page can move from Level 1 to Level 2 or Level 3, the human reviewer must confirm:

1. **Public safety** — no client names, ticket numbers, incident IDs, system IDs, or proprietary details.
2. **SAP source validation** — SAP-specific claims align with public documentation or are explicitly framed as "check in your landscape."
3. **Transaction / table / object accuracy** — referenced SAP objects exist and are used correctly for the described symptom.
4. **Evidence checklist** — the page lists concrete data to collect before escalation.
5. **Related links** — internal links point to existing Atlas pages, maps, or scenarios; no broken links.
6. **No private examples** — all examples are synthetic or generalized and labeled if needed.
7. **Last reviewed date** — `last_reviewed` is set to the review date and is within 90 days for flagship pages.
8. **Frontmatter correctness** — `status`, `verified`, `robots`, and `sitemap` match the intended verification level.

Only humans may complete this checklist and promote a page.

## Current Repository State

As of 2026-06-09:
- Most Atlas diagnostic pages are Level 1 (`needs_verification`, `noindex`).
- The Atlas index page (`atlas/index.md`) is Level 2 (`reviewed`, `verified: true`).
- All Scenario pages are Level 1 (`needs_verification`, `noindex`).
- The Scenarios index page (`scenarios/index.md`) is Level 1 (`needs_verification`, `noindex`).
- `llms-full.txt` includes only verified Atlas pages.
