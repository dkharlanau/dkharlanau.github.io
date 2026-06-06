# Atlas Backlog Pipeline

**Version:** 1.1.0  
**Schema:** `dkharlanau.atlas.backlog_decision_ledger`  
**Last updated:** 2026-06-06

---

## What the ledger is

The Atlas Backlog Decision Ledger is a public-safe, immutable record of every candidate that has been evaluated for inclusion in the Atlas knowledge base. It prevents reprocessing, duplication, and accidental publication of raw or private material.

Each candidate receives:

- A stable `candidate_id`
- A `content_fingerprint` for deduplication
- A `final_state` explaining what happened
- A `cluster_id` grouping related candidates
- A `reason` for the decision

The full ledger lives in `docs/atlas/atlas_backlog_decision_ledger.json`. A human-readable summary lives in `docs/atlas/ATLAS_BACKLOG_DECISION_LEDGER.md`.

---

## When to use this pipeline

Use the pipeline when:

- A new batch of backlog candidates needs evaluation
- You need to check whether a candidate was already processed
- You need to audit why a candidate was rejected or promoted
- You need to regenerate artifacts after ledger changes

Do **not** use the pipeline to:

- Reprocess already-decided candidates without `--force-reclassify`
- Commit raw CSV exports or private draft files
- Create one page per candidate
- Publish unverified content

---

## Candidate states

| State | Meaning | Target page required |
|---|---|---|
| `promoted_page` | Created a new Atlas page | Yes |
| `merged_existing` | Added content to an existing page | Yes |
| `clustered_future` | Strong cluster, deferred for future delivery | Optional |
| `glossary_only` | Too weak for a page; glossary entry only | No |
| `ignored_low_value` | Generic, duplicate, or lacking diagnostic value | No |
| `duplicate_existing` | Overlaps with an existing Atlas page | Yes |
| `deferred_needs_research` | Needs more research before decision | No |
| `blocked_private_risk` | Contains private or sensitive material | No |

---

## Cluster states

Clusters are derived from domain + category. A cluster's dominant state is the majority state of its members. Clusters themselves do not have separate states; they summarize candidate states.

---

## How to check if a candidate was already processed

```bash
# Lookup by candidate ID
python3 scripts/atlas_backlog_status.py lookup --candidate-id CONCEPT-0001

# Lookup by topic text
python3 scripts/atlas_backlog_status.py lookup --topic "Sales Document Type Selection"

# Check fingerprint stability
python3 scripts/atlas_backlog_status.py fingerprint \
  --topic "Sales Document Type Selection" \
  --domain "sales" \
  --category "Business Process"
```

---

## How future agents must process new candidates

1. **Load the existing ledger** first. Never start from an empty state.
2. **Fingerprint every new candidate** and check against existing fingerprints.
3. **Skip already-processed IDs** unless `--force-reclassify` is used with a reason.
4. **Assign a final state** using the decision rules below.
5. **Sanitize all output**: no private paths, no raw corpus, no `source_files`.
6. **Run validation** before committing.
7. **Commit only** the ledger, report, scripts, and any genuinely new pages.

---

## Decision rules

### Create a page (`promoted_page`)

Only when **all** of the following are true:

- The candidate describes a specific SAP diagnostic failure pattern
- There is no existing Atlas page covering the same pattern
- The page would include: symptoms, likely causes, where to check in SAP, key tables/transactions, diagnostic workflow, next actions
- The page is practical, not a glossary entry or textbook summary

### Merge into existing (`merged_existing`)

When:

- The candidate adds a compact, specific diagnostic section to an existing page
- A standalone page would be too thin
- The existing page's scope naturally includes this pattern

### Ignore (`ignored_low_value`)

When:

- Generic concept without SAP operational diagnostic value
- Generic AI/ML theory without SAP context
- Generic KPI formula without AMS diagnostic value
- Glossary-only definition
- Duplicate of existing coverage
- Vague filler

### Defer (`deferred_needs_research`)

When:

- The topic is promising but needs more evidence or SAP-specific detail
- The cluster is strong but the author cannot verify the diagnostic path today

### Block (`blocked_private_risk`)

When:

- The candidate contains private paths, customer data, or internal system references
- The candidate references `kb-drafts`, `source_files`, or other private material

---

## What must stay outside the repo

- Raw CSV exports from backlog triage tools
- `RECOVERY_*` files
- Private draft files with `kb-drafts` or `source_files` references
- Any file containing `/Users/` paths, `.env` files, or secrets
- Scratch analysis files
- Nested repo folders

## What may be committed

- Sanitized decision ledger (`json` + `md`)
- Sanitized promotion report
- Pipeline scripts
- Validation scripts
- Tests
- Genuinely new Atlas pages (if they pass quality gates)
- Updated generated artifacts (manifest, related, compact-index, llms-full)

---

## How to run validation

```bash
# Validate the ledger
python3 scripts/check_atlas_backlog_ledger.py

# Show summary
python3 scripts/atlas_backlog_status.py summary

# Check a new CSV against the ledger
python3 scripts/atlas_backlog_status.py check-new --csv new_candidates.csv

# Regenerate artifacts
python3 scripts/generate_atlas_artifacts.py

# Full artifact check
python3 scripts/generate_atlas_artifacts.py --check

# Public repo hygiene
python3 scripts/check_public_repo.py

# Link check
python3 scripts/check_links.py

# SEO check
python3 scripts/check_seo.py

# Run all tests
python3 -m pytest tests/test_atlas_artifacts.py tests/test_atlas_backlog_pipeline.py -v
```

---

## Examples

### Example: create

A candidate describes "SAP SD pricing condition override causing invoice block with specific tolerance check and VK11 condition record validation steps." No existing page covers this exact pattern. Decision: `promoted_page` with a new `sap-pricing-override-diagnostics.md`.

### Example: merge

A candidate describes "GR/IR clearing for consignment procurement with specific movement type 101 K and 107 K differences." The existing `sap-consignment-procurement-diagnostics.md` already covers consignment but not GR/IR clearing specifics. Decision: `merged_existing` into that page.

### Example: defer

A candidate describes "SAP EWM wave management failure patterns" but the author has no hands-on EWM diagnostic experience to verify the workflow. Decision: `deferred_needs_research`.

### Example: ignore

A candidate is "What is a purchase order?" with no diagnostic angle. Decision: `ignored_low_value`.

---

## Anti-patterns

| Anti-pattern | Why it is wrong | How to prevent |
|---|---|---|
| Raw dump committed | Leaks private paths and bloats repo | Add raw files to `.gitignore`; run `check_public_repo.py` |
| Private path committed | Exposes internal file structure | Sanitize all output; grep for `/Users/` and `.env` |
| Duplicate candidate reprocessed | Wastes time; corrupts ledger | Load existing ledger first; skip known IDs and fingerprints |
| Generic SAP term turned into weak page | Dilutes Atlas quality | Require diagnostic symptoms + SAP checks + next actions |
| Unverified page indexed | Publishes unreviewed content | All new pages: `status: needs_verification`, `verified: false`, `robots: noindex,follow`, `sitemap: false` |
| `source_files` added for private material | Links private drafts in public repo | Never include `source_files` in public output |

---

## Command reference

| Command | Purpose |
|---|---|
| `python3 scripts/check_atlas_backlog_ledger.py` | Validate ledger schema, counts, safety |
| `python3 scripts/atlas_backlog_status.py summary` | Show ledger summary |
| `python3 scripts/atlas_backlog_status.py lookup --candidate-id <ID>` | Lookup one candidate |
| `python3 scripts/atlas_backlog_status.py lookup --topic "<text>"` | Lookup by topic |
| `python3 scripts/atlas_backlog_status.py fingerprint --topic "<t>" --domain "<d>" --category "<c>"` | Compute stable fingerprint |
| `python3 scripts/atlas_backlog_status.py check-new --csv <path>` | Check new CSV against ledger |
| `python3 scripts/atlas_backlog_status.py export-summary --output <path>` | Export summary to file |
| `python3 scripts/run_atlas_backlog_cluster_pipeline.py` | Run full pipeline (idempotent) |
| `python3 scripts/run_atlas_backlog_cluster_pipeline.py --force-reclassify "reason"` | Force reclassify with reason |
| `python3 scripts/generate_atlas_artifacts.py` | Regenerate all artifacts |
| `python3 scripts/generate_atlas_artifacts.py --check` | Check artifacts are up to date |
| `python3 scripts/check_public_repo.py` | Public repo hygiene |
| `python3 scripts/check_links.py` | Broken link check |
| `python3 scripts/check_seo.py` | SEO validation |
| `python3 -m pytest tests/test_atlas_artifacts.py tests/test_atlas_backlog_pipeline.py -v` | Run all tests |

---

*This document is part of the Atlas public knowledge base. It contains no private paths, no raw corpus, and no `source_files` references.*
