# Content Maintenance Contract

Status: living contract  
Owner: Dzmitryi Kharlanau  
Last updated: 2026-06-08  
Purpose: define how the content maintenance metadata layer operates, what it tracks, and how future agents should use it to safely maintain Atlas and Research pages.

## 1. Purpose

The content maintenance layer is a lightweight, repo-friendly metadata and version-log system for Atlas and Research pages. It exists so future agents can:

- Discover stale pages without loading the whole site
- Find pages affected by new signals
- Know what changed and why
- Avoid updating verified / draft / indexing status accidentally
- Keep a version / update log per page or per content area
- Distinguish factual updates from weak signals and speculative notes

## 2. Files

| File | Purpose |
|------|---------|
| `data/content-maintenance/page-registry.json` | Compact metadata for every Atlas and Research page |
| `data/content-maintenance/change-log.jsonl` | Append-only event log of maintenance actions |
| `scripts/content_maintenance_scan.py` | Scanner that regenerates registry and appends changelog events |
| `tests/test_content_maintenance.py` | Tests for schema, safety rules, and scanner behavior |
| `docs/maintenance/CONTENT_MAINTENANCE_CONTRACT.md` | This document |

## 3. Page Registry Schema

For each relevant Atlas and Research page, the registry stores:

| Field | Type | Description |
|-------|------|-------------|
| `path` | string | Repository-relative path to the Markdown file |
| `url` | string | Canonical public URL |
| `title` | string | Page title from frontmatter |
| `section` | string | `atlas/{sub}` or `research/{sub}` |
| `status` | string | Frontmatter `status` value |
| `verified` | boolean | Frontmatter `verified` value |
| `robots` | string | Frontmatter `robots` value |
| `sitemap` | boolean | Frontmatter `sitemap` value |
| `last_reviewed` | string \| null | ISO date from `last_reviewed` |
| `last_meaningful_update` | string \| null | ISO date from `updated`, `last_modified_at`, or `date` |
| `source_confidence` | string | `high` / `medium` / `low` / `mixed` / `unknown` |
| `update_priority` | string | `high` / `medium` / `low` / `none` |
| `staleness_status` | string | `fresh` / `watch` / `stale` / `unknown` |
| `staleness_reason` | string \| null | Human-readable reason for staleness |
| `maintenance_notes` | string | Manual notes preserved across scans |
| `known_weak_sources` | list | Detected or manually flagged weak-source markers |
| `watch_terms` | list | Manual terms to watch for this page |
| `related_pages` | list | Manual related page URLs |
| `safe_to_auto_update` | boolean | Default `false`; must be manually enabled |
| `requires_human_review` | boolean | Default `true` for research and unverified pages |
| `safety_violations` | list | Auto-detected safety issues |

### 3.1 How future agents should use the registry

1. **Read the registry first** before deciding which pages to touch.
2. **Filter by `update_priority`** to find pages that need attention.
3. **Filter by `staleness_status`** to find pages that may be outdated.
4. **Check `safety_violations`** before any edit; fix violations before content updates.
5. **Respect `safe_to_auto_update`** — if `false`, do not auto-update content.
6. **Respect `requires_human_review`** — if `true`, flag changes for human approval.
7. **Never change `verified`, `robots`, or `sitemap` automatically** (see Safety Rules).

### 3.2 When to update a page

A page should be updated when:

- A new primary source contradicts or extends existing claims
- A broken link is found and a replacement source exists
- The `staleness_status` is `stale` and new evidence is available
- A safety violation is detected and can be resolved

A page should **not** be updated when:

- The only trigger is a timestamp rollover (no new signal)
- The source is a weak signal, aggregator, or newsletter alone
- The page is `verified: true` and the new signal is speculative
- The change would relax `noindex` or add a draft page to the sitemap

### 3.3 What counts as a meaningful update

Meaningful updates change claims, sources, or structure. These count:

- Adding or removing a factual claim with source citation
- Replacing a weak source with a primary source
- Fixing a broken link with a verified replacement
- Adding a new section based on new evidence
- Correcting an error found during review

These do **not** count as meaningful updates:

- Changing `last_reviewed` without content changes
- Reformatting Markdown or fixing typos
- Adding tags or metadata without claim changes
- Timestamp-only diffs

## 4. Change Log

The change log is append-only JSONL. Each line is one event.

### 4.1 Event schema

| Field | Type | Description |
|-------|------|-------------|
| `event_id` | string | Unique event identifier |
| `timestamp` | string | ISO 8601 UTC timestamp |
| `actor` | string | `human` / `agent` / `script` |
| `page_path` | string | Repository-relative page path |
| `event_type` | string | See Event Types below |
| `summary` | string | Human-readable summary |
| `reason` | string | Why this event happened |
| `source_signal` | string | What triggered the event |
| `confidence` | string | `high` / `medium` / `low` |
| `files_changed` | list | Files affected by this event |
| `validation` | string | How the change was validated |
| `human_review_required` | boolean | Whether a human must review |

### 4.2 Event types

| Type | Use when |
|------|----------|
| `created` | A new page is added to the registry |
| `reviewed` | A human reviews a page without content changes |
| `updated` | Content is updated with new claims or sources |
| `source_downgraded` | A source is found to be weaker than previously rated |
| `source_replaced` | A source is swapped for a better one |
| `claim_removed` | A claim is removed due to lack of evidence |
| `link_fixed` | A broken link is repaired |
| `metadata_changed` | Registry metadata is updated (e.g., manual notes) |
| `deferred` | An update is intentionally postponed |

### 4.3 How to add a change-log event

1. Generate a unique `event_id` (e.g., `uuid4` or prefixed slug).
2. Set `timestamp` to current UTC time.
3. Set `actor` to `agent` if an agent performed the action, `human` if a person did, or `script` for automated scans.
4. Set `event_type` from the table above.
5. Write a clear `summary` and `reason`.
6. Set `human_review_required` to `true` for claim changes, source upgrades, and indexing changes.
7. Append the JSON object as a single line to `change-log.jsonl`.

Do not edit or delete existing lines.

## 5. Safety Rules

These rules are enforced by the scanner and must be respected by all agents.

### 5.1 Research pages

- Research pages must remain `noindex` unless explicitly reviewed by a human.
- Research pages must have `sitemap: false`.
- Research pages must have `status: draft`.

### 5.2 Unverified pages

- Unverified pages (`verified: false` or missing) must not be added to the sitemap.
- Unverified pages must not be marked `verified: true` automatically.

### 5.3 Verified pages

- `verified: true` must never be set by the scanner or any automated script.
- A page with `verified: true` must not have weak-source markers in its content.

### 5.4 Auto-update safety

- `safe_to_auto_update` defaults to `false`.
- An agent may only auto-update a page if `safe_to_auto_update` is `true` and `requires_human_review` is `false`.
- Human review is required for:
  - Claim changes
  - Source upgrades
  - Indexing changes (`robots`, `sitemap`)
  - Promotion from research to atlas

### 5.5 Privacy and security

- Do not include private paths or private notes in the registry.
- Do not store raw source dumps in the registry or change log.
- Do not create agent-generated claims without source references.
- Do not expose credentials, secrets, or internal system details.

## 6. Weak Sources

Weak sources are signals that should not be treated as proof. The scanner detects these markers in page content:

- `weak_signal`
- `low confidence`
- `aggregator`
- `market report`
- `newsletter`
- `future-dated`
- `verify against official docs`
- `unverified`
- `speculation`
- `rumor`

### 6.1 How to handle weak sources

- Flag them in `known_weak_sources`.
- Set `source_confidence` to `low` or `mixed`.
- Do not upgrade `verified` based on weak sources alone.
- If a weak source is replaced by a primary source, log `source_replaced`.

### 6.2 How to handle research signals

Research pages are intentionally lower-confidence. When a research signal graduates:

1. Verify the claim against at least one primary source.
2. Update the source list with confidence ratings.
3. Log a `source_replaced` or `updated` event.
4. Promote the page to Atlas only after human review.
5. Update `robots` and `sitemap` only after promotion is approved.

## 7. Scanner Behavior

### 7.1 Running the scanner

```sh
python3 scripts/content_maintenance_scan.py
```

This regenerates `page-registry.json` and appends new events to `change-log.jsonl`.

Check mode (no writes):

```sh
python3 scripts/content_maintenance_scan.py --check
```

### 7.2 What the scanner does

1. Discovers all Atlas and Research Markdown files.
2. Parses frontmatter using PyYAML.
3. Builds or updates registry entries.
4. Preserves manual fields (`safe_to_auto_update`, `maintenance_notes`, `watch_terms`, `related_pages`).
5. Detects weak-source markers in page bodies.
6. Computes staleness from `last_reviewed` or `last_meaningful_update`.
7. Checks safety violations.
8. Generates initial `metadata_changed` events for new pages.
9. Prints a concise report.
10. Exits non-zero only for safety violations.

### 7.3 Staleness thresholds

| Status | Days since last review |
|--------|------------------------|
| `fresh` | ≤ 30 |
| `watch` | 31–90 |
| `stale` | > 90 |
| `unknown` | No date found |

### 7.4 How to avoid timestamp-only diffs

The scanner preserves manual fields and only updates auto-computed fields. If you run the scanner twice with no repository changes, the registry should be identical (except for `generated_at`).

To verify:

```sh
python3 scripts/content_maintenance_scan.py
git diff data/content-maintenance/page-registry.json
```

Only `generated_at` should change. If other fields shift, the scanner is not idempotent.

## 8. Validation

Run these checks before committing maintenance changes:

```sh
python3 scripts/content_maintenance_scan.py
python3 scripts/check_public_repo.py
python3 scripts/generate_atlas_artifacts.py --check
pytest tests/
```

Link and SEO checks require a built Jekyll site:

```sh
bundle exec jekyll build
python3 scripts/check_links.py
python3 scripts/check_seo.py
```

## 9. Committing Maintenance Changes

Only commit:

- `docs/maintenance/CONTENT_MAINTENANCE_CONTRACT.md`
- `scripts/content_maintenance_scan.py`
- `tests/test_content_maintenance.py`
- `data/content-maintenance/page-registry.json`
- `data/content-maintenance/change-log.jsonl`

Do not commit:

- Private notes or source dumps
- Changes to `verified`, `robots`, or `sitemap` made automatically
- New public pages created by an agent

## 10. Glossary

| Term | Meaning |
|------|---------|
| **Atlas** | The curated, reviewed knowledge surface (`/atlas/`) |
| **Research** | The draft, noindex signal-tracking layer (`/research/`) |
| **Primary source** | Official vendor docs, release notes, or GitHub repos |
| **Weak source** | Aggregators, newsletters, speculation, unverified claims |
| **Safety violation** | A rule breach that could expose drafts or false claims |
| **Meaningful update** | A content change that affects claims, sources, or structure |
