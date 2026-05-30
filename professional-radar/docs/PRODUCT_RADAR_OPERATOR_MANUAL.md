# Product Radar Operator Manual

**Version:** 2026-05-30
**Purpose:** End-to-end guide for understanding, operating, and maintaining the Product Radar system.
**Audience:** Operators (D.K.), new agents, reviewers.
**Status:** Required for Definition of Done. Every PR that changes Product Radar behavior must update this manual.

---

## 1. What Product Radar Is

### 1.1 Problem It Solves
Product Radar is a disciplined, semi-automated content curation pipeline for professional signals in the SAP/AMS/enterprise AI space. It replaces ad-hoc content scanning with:
- Systematic source discovery and monitoring
- Quality filtering before any human review
- Structured draft generation with a consistent author voice
- Safe, gated publishing to site and LinkedIn
- Full audit trail of every decision

### 1.2 What It Does NOT Do
- **NOT** an autoposting system. LinkedIn requires manual approval.
- **NOT** a content farm. Weak signals are rejected, not spammed.
- **NOT** a secret manager. No credentials, tokens, or private data are stored in the repo.
- **NOT** a replacement for professional judgment. The pipeline filters and structures; humans approve.
- **NOT** a generic AI summarizer. Output is written in a specific, skeptical, consultant voice.
- **NOT** a Telegram/automation tool. No outbound notifications, no engagement automation.

### 1.3 What Counts as a Signal
A signal is any external, source-backed event that could be relevant to SAP professionals:
- SAP product announcements or documentation updates
- Architecture guidance or tooling changes
- Support notes with operational implications
- Integration or API updates
- TCO/pricing changes
- AI/ML capability releases affecting SAP workflows
- Business process or master data governance updates

A signal is NOT:
- Generic industry news without SAP relevance
- Marketing material without practical implications
- Rumors or unverified claims
- Internal/client-specific data

### 1.4 What Counts as a Source
A source is a publicly accessible URL that provides the signal. Allowed domains:
- `sap.com`, `help.sap.com`, `support.sap.com`, `news.sap.com`, `blogs.sap.com`, `community.sap.com`
- `s4hana.cloud.sap`, `btp.cloud.sap`
- `saparchitecture.center`

Sources must be reachable (HTTP 200 or acceptable redirect). 404 sources are rejected. Server-protected pages (403) are treated as "exists but inaccessible" — they may still be considered if the domain is trusted and the URL structure is canonical.

### 1.5 What Counts as a Draft
A draft is a LinkedIn-ready or site-ready content artifact generated from an approved signal. Drafts exist in these states:
- `candidate`: identified from signal, not yet drafted
- `drafted`: draft created, pending review
- `needs_review`: flagged for quality concerns
- `approved_manually`: approved by human review
- `rejected`: rejected by quality gate or human review
- `published_manually`: published by manual action (not autoposted)

### 1.6 What Counts as Published
- **Site published**: A `_radar/` or `_notes/` file exists on GitHub Pages, built by Jekyll, and is live.
- **LinkedIn published**: A LinkedIn post was manually copied and published by D.K. (never autoposted).

### 1.7 What Is Manual-Only
These actions require explicit D.K. approval:
- Live LinkedIn posting
- Site apply (converting `--dry-run` to actual file creation)
- Jekyll build verification in production
- Any command with `--apply` or `--post` flag
- Publishing more than one LinkedIn post per day
- Publishing more than three LinkedIn posts per rolling 7 days

---

## 2. Full Pipeline

### Step 1: Source Planning
- Maintain `source_plan.json` or equivalent registry
- Define source tiers, check cadence, and topic scope
- Sources are SAP-focused: architecture, support, integration, TCO, business process, AI, master data

### Step 2: Source Fetching
- Fetch source content via HTTP (HEAD then GET fallback)
- Strip noise, preserve structure
- Store raw content for downstream processing

### Step 3: Newness Detection
- Compare content hash against `seen-items.json`
- If hash exists and is unchanged → skip
- If new or changed → proceed to scoring

### Step 4: Duplicate Detection
- Check `items.jsonl` for existing `source_url` or `canonical_url`
- Check `seen-items.json` for content hash
- If duplicate → mark as `digest_only` or `rejected`

### Step 5: Signal Normalization
- Map source fields to canonical signal schema:
  - `source_name` → `source`
  - `item_url` → `source_url`
  - `short_summary` → `summary`
- Ensure all required fields present: `source_url`, `topic`, `summary`, `date`

### Step 6: Scoring / Governor
- Score signal on: relevance, confidence, practical impact, source quality
- Apply decision: `publishable`, `needs_edit`, `digest_only`, `reject`
- Low-confidence or low-impact signals → `reject` or `digest_only`

### Step 7: Source Validation
- Check URL reachability (HTTP HEAD + GET fallback)
- Check domain whitelist
- Canonicalize URL (strip query params, fragments, normalize)
- 404 or unreachable → reject
- 403 on trusted domain → warn but may proceed

### Step 8: Atlas / Content Lookup
- Check `_radar/` and `_news/` directories for existing content
- Matching rules: exact source URL, canonical URL, slug, title similarity (>0.7), topic match
- If exact match → `update_existing`
- If similar title/topic → `digest_only`
- If no match → `create`
- Missing directories are reported, not silently passed

### Step 9: Author Voice Contract
- Load `author-voice.yaml` as mandatory input
- Enforce: English by default, B2 professional English, consultant voice
- Apply hard blockers:
  - No source URL in LinkedIn main post
  - No invented metrics
  - No generic AI tone
  - Must have "My take" / professional interpretation
  - No Atlas check bypass
  - No duplicate `_radar` + `_news` without justification
  - No READY without Jekyll build test

### Step 10: Lens Selection
- Select 1 primary lens + up to 2 secondary lenses from 8 options:
  - transformation, integration, tco, architecture, business_process, ams_support, data_master_data, ai_operating_model
- Based on keyword scoring from signal content + YAML config
- Primary lens must not be forced to `ams_support` if signal is broader

### Step 11: Site Draft Generation
- Generate `_radar/` markdown with YAML frontmatter
- Sections: Signal, Selected lens, Why it matters, Practical check, My take, Related Atlas topics
- Frontmatter includes: `primary_lens`, `secondary_lenses`, `source_url`, `source_name`, `checked_at`, `topic`
- Title must be unique and search-oriented (no generic source title, no date-led title)
- Filename: `YYYY-MM-DD-slug.md`

### Step 12: LinkedIn Draft Generation
- Main post: opens with lens question, then signal, then practical impact, then My take
- No source URL in main post
- No hashtags by default
- No invented metrics
- First comment: `Source: <source_name> — <url>`
- Character count tracked (limit 3000)
- My take must be distinct from lens interpretation (no repetition)

### Step 13: Preview Generation
- Runs all validation gates in sequence
- Produces `PRODUCT RADAR PREVIEW REPORT` with:
  - Voice contract status
  - Source validation status
  - Lens selection
  - Full contract enforcement table (all 10 checks)
  - LinkedIn output (main post + first comment)
  - Site output (frontmatter + body preview)
  - Atlas check results
  - Hard blocker summary
  - Final readiness: `READY` / `NOT READY` / `PARTIAL PREVIEW ONLY`

### Step 14: Validation
- `py_compile` for all Python scripts
- `--test-lenses` for 5 signal types (architecture, support, integration, TCO, business process)
- `--jekyll-tested` for READY path verification
- `professional_radar_validate.py` for schema/content checks
- `pytest` for regression tests

### Step 15: Manual Approval
- D.K. reviews preview report
- If all gates pass and Jekyll tested → may approve
- If any blocker → fix and re-run preview
- Approval is implicit: D.K. says "publish" or "post"

### Step 16: Publishing / Handoff
- Site: apply `--dry-run` output to actual files, commit, push, Jekyll build
- LinkedIn: copy draft to clipboard, paste manually, never autopost
- Record event to lifecycle log
- Generate closeout report

---

## 3. What Is Considered in Decisions

| Factor | How Used | Where Stored |
|--------|----------|--------------|
| Source tier | Trusted domains get lenient 403 handling | `source_validation.allowed_domains` in author-voice.yaml |
| Source quality | Reachability, domain reputation | `source-checks.jsonl` (runtime, reverted to main) |
| Source URL validity | HTTP check (HEAD + GET fallback) | `source_validation` field in preview report |
| Canonical URL | Normalized, deduped URL | `canonical_url` in source validation result |
| Content hash | Detects identical content | `seen-items.json` |
| Topic | Determines lens selection, Atlas matching | Signal field `topic` |
| Stream | Content type (signal, knowledge_byte, article) | `content_type` in classification |
| Confidence | high/medium/low → publish/digest/reject | Signal field `confidence` |
| Signal status | candidate, drafted, approved, rejected, published | `items.jsonl` (runtime, reverted) |
| Duplicate risk | Exact/similar URL, title, topic | `atlas_check` result |
| Atlas match | `_radar/` and `_news/` directory scan | `atlas_check` function |
| Previous drafts | Prevents re-drafting | `items.jsonl` (if status tracked) |
| Previous published content | Prevents duplicate publication | `events.jsonl` (if implemented) |
| Author voice rules | Hard blockers enforced on every draft | `author-voice.yaml` |
| LinkedIn safety rules | Rate limits, source URL, confidence | `linkedin_output` rules in author-voice.yaml |
| Site readiness rules | Jekyll build required for READY | `jekyll_tested` flag in preview report |
| Jekyll/build status | Must pass before READY | `bundle exec jekyll build` |
| Manual approval state | Only human can approve live actions | Chat / D.K. instruction |

---

## 4. State Files

### 4.1 `professional-radar/data/professional-radar/items.jsonl`
- **Path:** `professional-radar/data/professional-radar/items.jsonl`
- **Purpose:** Stores fetched and scored signals
- **Schema:** JSONL, one JSON object per line
  - `source_id`, `item_url`, `content_type`, `tags`, `summary`, `practical_impact`, `topic`, `confidence`, `status`, `date`
- **Committed or runtime:** Runtime (should be reverted to main before PR)
- **Append-only or mutable:** Append-only
- **Safe to reset:** Yes (will re-fetch signals)
- **Affects future runs:** Yes — status field prevents re-processing

### 4.2 `professional-radar/data/professional-radar/seen-items.json`
- **Path:** `professional-radar/data/professional-radar/seen-items.json`
- **Purpose:** Tracks content hashes for deduplication
- **Schema:** JSON, key-value map of `hash` → `last_seen_date`
- **Committed or runtime:** Runtime (should be reverted to main)
- **Append-only or mutable:** Mutable (updates on each run)
- **Safe to reset:** Yes (will cause re-processing of all signals)
- **Affects future runs:** Yes — prevents duplicate content from being re-scored

### 4.3 `professional-radar/data/professional-radar/source-checks.jsonl`
- **Path:** `professional-radar/data/professional-radar/source-checks.jsonl`
- **Purpose:** Records source URL reachability checks
- **Schema:** JSONL with `url`, `checked_at`, `status_code`, `domain_allowed`, `valid`
- **Committed or runtime:** Runtime (should be reverted to main)
- **Append-only or mutable:** Append-only
- **Safe to reset:** Yes (will re-validate sources)
- **Affects future runs:** Yes — cached validation results can skip re-checking

### 4.4 `professional-radar/data/professional-radar/events.jsonl` (PLANNED)
- **Path:** `professional-radar/data/professional-radar/events.jsonl`
- **Purpose:** Append-only lifecycle event log for signals
- **Schema:** JSONL with `event_id`, `signal_id`, `event_type`, `timestamp`, `actor`, `details`
- **Event types:** `seen`, `scored`, `rejected`, `routed_to_digest`, `site_draft_created`, `linkedin_draft_created`, `site_published`, `linkedin_published`, `duplicate_detected`
- **Committed or runtime:** Runtime (not committed to repo)
- **Append-only or mutable:** Append-only (never delete or edit)
- **Safe to reset:** No (loses audit trail)
- **Affects future runs:** Yes — provides ground truth for processed-state rules
- **Status:** NOT YET IMPLEMENTED (see gap note below)

### 4.5 LinkedIn Draft Files
- **Path:** `professional-radar/output/linkedin_*.md` or `output/linkedin_drafts/`
- **Purpose:** Generated copy-ready LinkedIn drafts
- **Schema:** Markdown with YAML frontmatter
  - `draft_id`, `source_signal_id`, `source_urls`, `topic`, `angle`, `status`, `style_pattern`, `human_voice_score`, `template_risk`
- **Committed or runtime:** Runtime (not committed)
- **Safe to reset:** Yes (regenerable from signals)
- **Affects future runs:** Yes — prevents re-drafting same signal

### 4.6 Site Draft Files
- **Path:** `_radar/YYYY-MM-DD-slug.md`
- **Purpose:** Jekyll-compatible site content
- **Schema:** Markdown with YAML frontmatter
  - `layout`, `title`, `date`, `source_url`, `source_name`, `checked_at`, `tags`, `confidence`, `topic`, `primary_lens`, `secondary_lenses`
- **Committed or runtime:** Committed (via PR)
- **Safe to reset:** No (published content)
- **Affects future runs:** Yes — Atlas check uses these files for deduplication

### 4.7 Run Reports / Closeout Reports
- **Path:** `closeout-*.md` or `output/run_report_*.md`
- **Purpose:** Post-run summary of what was processed, accepted, rejected, published
- **Schema:** Markdown with sections for sources, signals, accepted, rejected, site files, validation, next actions
- **Committed or runtime:** Committed (via PR)
- **Safe to reset:** N/A

### 4.8 Author Voice Config
- **Path:** `professional-radar/config/author-voice.yaml`
- **Purpose:** Source of truth for voice, tone, structure, hard blockers, lenses
- **Schema:** YAML with `voice`, `banned_patterns`, `default_post_structure`, `radar_lenses`, `hard_blockers`, `quality_gate`
- **Committed or runtime:** Committed
- **Safe to reset:** No (part of repo)
- **Affects future runs:** Yes — all generators read this file

### 4.9 Sources Config
- **Path:** `professional-radar/config/source_plan.json` or `sources.json`
- **Purpose:** Defines sources to monitor, check cadence, topics
- **Committed or runtime:** Committed
- **Safe to reset:** No (part of repo)

### 4.10 Topics Config
- **Path:** `docs/content-taxonomy.md` or `professional-radar/config/topics.yaml`
- **Purpose:** Defines content types, collections, and routing rules
- **Committed or runtime:** Committed
- **Safe to reset:** No (part of repo)

### 4.11 Validation Config
- **Path:** `professional-radar/config/validation.yaml` or `professional_radar_validate.py`
- **Purpose:** Schema checks, content quality rules, safety gates
- **Committed or runtime:** Committed
- **Safe to reset:** No (part of repo)

---

## 5. Keys, Credentials, and Environment

### 5.1 LinkedIn
- **Variable:** `LINKEDIN_ACCESS_TOKEN`
- **Stored in:** `/root/.openclaw/secrets/linkedin.env`
- **Used by:** `scripts/linkedin_publish.py`
- **Required for:** live LinkedIn publish only
- **Not required for:** draft generation, preview, dry-run, validation
- **Safety rule:** Never print value. Never commit file. Never include in logs.

- **Variable:** `LINKEDIN_PERSON_URN`
- **Stored in:** `/root/.openclaw/secrets/linkedin.env`
- **Used by:** `scripts/linkedin_publish.py`
- **Required for:** live LinkedIn publish only
- **Safety rule:** Never print value.

- **Variable:** `LINKEDIN_CLIENT_ID`, `LINKEDIN_CLIENT_SECRET`
- **Stored in:** `/root/.openclaw/secrets/linkedin.env`
- **Used by:** OAuth flow (if needed for token refresh)
- **Required for:** token refresh only
- **Safety rule:** Never print value.

### 5.2 GitHub
- **gh CLI auth:** Managed by `gh auth` in cloud environment
- **Used by:** PR creation, branch push, merge
- **Required for:** all GitHub operations
- **Safety rule:** Never commit `.git/credentials` or `.env` files

### 5.3 OpenClaw / Kimi Environment
- **Workspace:** `/root/.openclaw/workspace` (cloud) or `~/Developments/cv-ai` (Mac Mini)
- **Secrets path:** `/root/.openclaw/secrets/`
- **Safety rule:** Never commit workspace state, memory files, or group chat logs

### 5.4 Jekyll / Ruby
- **Ruby version:** 3.2.3 (see `.ruby-version`)
- **Used by:** `bundle exec jekyll build`
- **Required for:** site build validation and READY status
- **Not required for:** draft generation, preview, LinkedIn drafts
- **Safety rule:** `Gemfile.lock` is committed. `vendor/bundle` and `_site/` are not.

### 5.5 Which Commands Require Credentials

| Command | Credentials Required | Notes |
|---------|---------------------|-------|
| `linkedin_publish.py --post` | Yes (LinkedIn token) | Never run without explicit D.K. approval |
| `linkedin_publish.py --dry-run` | No | Safe to run without credentials |
| `gh pr create` | Yes (gh auth) | Requires GitHub CLI auth |
| `git push` | Yes (SSH or HTTPS) | Requires GitHub auth |
| `professional_radar_author_voice_generator.py` | No | Purely local validation |
| `bundle exec jekyll build` | No | Requires Ruby/Bundler, not credentials |
| `python3 -m pytest` | No | Purely local |

### 5.6 How to Check Credentials Without Exposing Them
```bash
# Check LinkedIn credentials exist (not their values)
test -f /root/.openclaw/secrets/linkedin.env && echo "linkedin.env exists" || echo "missing"
# Check keys exist without showing values
grep -c "=" /root/.openclaw/secrets/linkedin.env 2>/dev/null || echo "0 keys"
# Check gh auth
gh auth status 2>/dev/null | head -3
# Check GitHub permissions
gh repo view <repo> --json viewerPermission 2>/dev/null | grep viewerPermission
```

---

## 6. Commands

### 6.1 Source Plan
```bash
# Inspect source registry
python3 professional-radar/scripts/professional_radar_source_plan.py --list
# Reads: professional-radar/config/source_plan.json
# Writes: stdout
# Mutates state: No
# External contact: No
# Safe for CI: Yes
```

### 6.2 Fetch Dry-Run
```bash
python3 professional-radar/scripts/professional_radar_fetch.py --dry-run
# Reads: source_plan.json, seen-items.json
# Writes: preview output to stdout
# Mutates state: No
# External contact: Yes (HTTP requests to sources)
# Safe for CI: Yes (no state changes)
```

### 6.3 Fetch Real
```bash
python3 professional-radar/scripts/professional_radar_fetch.py
# Reads: source_plan.json, seen-items.json
# Writes: items.jsonl, seen-items.json, source-checks.jsonl
# Mutates state: Yes
# External contact: Yes
# Safe for CI: No (mutates state files)
# Requires: git status clean, on feature branch
```

### 6.4 Score / Governor
```bash
python3 professional-radar/scripts/professional_radar_score.py --input items.jsonl
# Reads: items.jsonl, classification-rules.yaml
# Writes: stdout with decisions
# Mutates state: No (unless --output specified)
# External contact: No
# Safe for CI: Yes
```

### 6.5 Generate Author Voice Preview
```bash
python3 professional-radar/scripts/professional_radar_author_voice_generator.py   --contract professional-radar/config/author-voice.yaml   --output preview-report.md
# Reads: author-voice.yaml, candidate.json (optional)
# Writes: preview-report.md
# Mutates state: No
# External contact: Yes (source URL validation via HTTP)
# Safe for CI: Yes (use --skip-source-validation for offline)
# Expected output: PRODUCT RADAR PREVIEW REPORT with all validation gates
```

### 6.6 Generate LinkedIn Draft
```bash
python3 professional-radar/scripts/professional_radar_author_voice_generator.py   --contract professional-radar/config/author-voice.yaml   --candidate candidate.json
# Reads: author-voice.yaml, candidate.json
# Writes: stdout with LinkedIn main post + first comment
# Mutates state: No
# External contact: Yes (source URL validation)
# Safe for CI: Yes (use --skip-source-validation)
```

### 6.7 Generate Site Draft
```bash
python3 professional-radar/scripts/professional_radar_site_update.py --dry-run
# Reads: accepted candidates, _radar/ directory
# Writes: preview of files to create
# Mutates state: No (dry-run)
# External contact: No
# Safe for CI: Yes
```

### 6.8 Validate Product Radar
```bash
python3 professional-radar/scripts/professional_radar_validate.py --all --stage draft
# Reads: draft files, validation rules
# Writes: stdout with PASS/FAIL per file
# Mutates state: No
# External contact: No
# Safe for CI: Yes
```

### 6.9 Run E2E Tests
```bash
python3 -m pytest professional-radar/tests -q
# Reads: test files, fixtures
# Writes: stdout with test results
# Mutates state: No (unless test creates temp files)
# External contact: No
# Safe for CI: Yes
# Expected output: All pass (except known stale test_e2e.py drift)
```

### 6.10 Run Jekyll Test
```bash
bundle exec jekyll build
# Reads: _config.yml, all collections, layouts, includes
# Writes: _site/
# Mutates state: No (generates to _site/)
# External contact: No
# Safe for CI: Yes (if Ruby available)
# Expected output: Build succeeds, no errors
```

### 6.11 Produce Run Report
```bash
python3 professional-radar/scripts/professional_radar_closeout.py   --sources N --signals M --accepted A --rejected R   --site-files F --validation PASS --next-actions "..."
# Reads: CLI args
# Writes: closeout report markdown
# Mutates state: No
# External contact: No
# Safe for CI: Yes
```

### 6.12 Inspect Duplicates
```bash
python3 professional-radar/scripts/professional_radar_author_voice_generator.py   --contract professional-radar/config/author-voice.yaml   --candidate candidate.json
# (Atlas check section of preview report shows duplicate status)
```

### 6.13 Inspect Already Processed Signals
```bash
# Check items.jsonl for existing signals
cat professional-radar/data/professional-radar/items.jsonl | grep '"status"'
# Check seen-items.json for hashes
python3 -c "import json; d=json.load(open('seen-items.json')); print(len(d), 'items seen')"
```

### 6.14 Reprocess One Signal Safely
```bash
# 1. Generate preview for single signal
python3 professional-radar/scripts/professional_radar_author_voice_generator.py   --contract professional-radar/config/author-voice.yaml   --candidate single_signal.json
# 2. Review preview report
# 3. If READY and approved, apply site changes
python3 professional-radar/scripts/professional_radar_site_update.py --apply --limit 1
# 4. Generate LinkedIn draft
# 5. Manual copy-paste to LinkedIn
# 6. Record event (when events.jsonl is implemented)
```

---

## 7. Processed-State Rules

### 7.1 Signal Already Seen
- Detected by: content hash in `seen-items.json` OR exact `source_url` in `items.jsonl`
- Action: Skip (do not re-fetch or re-score)
- Override: Manual reprocessing with `--force-reprocess` (if implemented)

### 7.2 Signal Already Scored
- Detected by: `status` field in `items.jsonl` (not `candidate`)
- Action: Skip scoring, proceed to routing if status is `publishable`
- Override: Manual re-scoring with `--force-score`

### 7.3 Signal Already Rejected
- Detected by: `status` = `reject` in `items.jsonl`
- Action: Skip on future runs (unless source changed significantly)
- Override: Manual re-scoring if source updated
- NOTE: Current system uses `items.jsonl` for this, but `events.jsonl` is the intended ground truth.

### 7.4 Signal Already Drafted
- Detected by: existence of draft file in `output/linkedin_drafts/` or `output/site_drafts/`
- Action: Skip re-drafting
- NOTE: Not fully tracked. Draft file existence is the de facto check.

### 7.5 Signal Already Published
- Detected by: `_radar/` file with matching `source_url` OR `events.jsonl` with `site_published` or `linkedin_published` event
- Action: Skip entirely (update_existing only if new info)
- NOTE: `events.jsonl` is NOT YET IMPLEMENTED. Atlas check is the current de facto check.

### 7.6 Signal Is Duplicate
- Detected by: `atlas_check` returning `update_existing` or `digest_only`
- Action: Do not create new file
- Record: `duplicate_detected` event (when events.jsonl implemented)

### 7.7 Signal May Be Reprocessed
- Conditions: Source URL changed, content changed (new hash), or manual override flag set
- Action: Re-score and re-route
- Safety: Must not overwrite published content without approval

### 7.8 Signal Must Be Skipped
- Conditions: `reject` status, `digest_only` decision, duplicate with exact match, 404 source, banned domain
- Action: Skip all downstream processing
- Record: Skip reason in closeout report

### 7.9 GAP: Events.jsonl Not Implemented
The `events.jsonl` append-only lifecycle log is NOT YET IMPLEMENTED. Current processed-state relies on:
- `seen-items.json` (for dedupe)
- `items.jsonl` (for status, but this is runtime data, not an audit log)
- Atlas check (for published content detection)
- Draft file existence (for drafted content detection)

This is a gap. The intended system is:
- All lifecycle events go to `events.jsonl`
- `events.jsonl` is the ground truth for processed-state rules
- `items.jsonl` is a working data file, not an audit log
- `seen-items.json` is a dedupe cache, not an audit log

**Recommended:** Create issue "Add Product Radar signal lifecycle event ledger" and implement `events.jsonl`.

---

## 8. Safety and Approval Gates

### 8.1 No Live LinkedIn Posting Without D.K. Approval
- All LinkedIn drafts are `drafted` or `approved_manually` only
- No script autoposts
- The `linkedin_publish.py` script requires `--post` flag AND credentials
- `--post` is only run after explicit D.K. "post" instruction

### 8.2 No Telegram Sends
- No Telegram integration in Product Radar
- No notifications, no alerts, no group messages

### 8.3 No Secrets in Repo
- `.gitignore` excludes: `secrets/`, `.env`, `*.env`, `_site/`, `.kimi/`, `memory/`, `kimi-group-chat/`
- `AGENTS.md` defines repo safety rules
- `scripts/check_public_repo.py` validates before commit

### 8.4 No Runtime/Private Data Commits
- Runtime data files (`items.jsonl`, `seen-items.json`, `source-checks.jsonl`) are reverted to main before PR
- No drafts, no credentials, no personal data in commits

### 8.5 Dry-Run Default
- All scripts default to `--dry-run` mode
- `--apply` and `--post` require explicit flags
- No accidental mutations

### 8.6 What Manual Approval Means
- D.K. reviews the preview report
- D.K. explicitly states "publish" or "post" or "apply"
- Verbal approval is not enough — must be explicit instruction
- If D.K. says nothing, no action is taken

### 8.7 What Files Prove Approval
- No file-based approval gate exists yet
- Approval is conversational (chat-based)
- Recommended: Add a `approved.json` or D.K. signature mechanism (future enhancement)

### 8.8 What Must Happen Before Live Publish
All must be true:
- [ ] Preview report shows `READY` status
- [ ] Jekyll build passed (`bundle exec jekyll build`)
- [ ] All hard blockers pass
- [ ] Source validation passes (reachable, allowed domain)
- [ ] Atlas check shows `create` (not duplicate)
- [ ] Lens selection is not forced to `ams_support`
- [ ] My take is present and distinct from lens interpretation
- [ ] Repetition check passes (no template overlap)
- [ ] No invented metrics
- [ ] Source URL only in first comment, not main post
- [ ] D.K. explicitly approved
- [ ] LinkedIn rate limit allows (max 1/day, 3/7 days)
- [ ] No live post already made today

---

## 9. Troubleshooting

### 9.1 No New Signals Found
- Check `source_plan.json` for cadence and URLs
- Check `seen-items.json` — may have stale hashes
- Check `source-checks.jsonl` for source failures
- Try `--force-reprocess` if source changed

### 9.2 Source Returns Landing Page Only
- Source may be generic (e.g., `sap.com` root page)
- Use specific sub-URLs: `/products/...`, `/docs/...`, `/notes/...`
- Check if source changed structure

### 9.3 Source URL 404
- URL is dead or changed
- Check `source-checks.jsonl` for exact error
- Remove from source plan or update URL
- Signal is rejected automatically

### 9.4 Duplicate Detected
- Check `atlas_check` output for which file matched
- If exact source URL match → `update_existing`
- If similar title → `digest_only`
- If you believe it's not a duplicate → check `similarity_threshold` in author-voice.yaml

### 9.5 Source-Check Stale
- `source-checks.jsonl` may have old results
- Run with `--force-source-check` or delete stale entries
- Or rely on preview generator's real-time validation

### 9.6 Jekyll Not Available
- Ruby/Jekyll not installed in environment
- Site drafts can still be generated and previewed
- Readiness will be `NOT READY` — this is correct
- Install Ruby 3.2.3, `bundle install`, then `bundle exec jekyll build`

### 9.7 LinkedIn Credentials Missing
- `linkedin_publish.py` will skip posting with reason: "credentials not configured"
- Draft is still generated and saved
- Handoff is manual copy-paste
- Check credential file: `test -f /root/.openclaw/secrets/linkedin.env`

### 9.8 Draft Generated but Not Publish-Ready
- Check preview report for which blocker failed
- Common causes: invented metrics, missing My take, source URL in main post, duplicate detected
- Fix the issue and re-run preview

### 9.9 Validation Mismatch
- `professional_radar_validate.py` may flag schema issues
- Check frontmatter fields: required vs optional
- Check content length, tags, date format
- Fix and re-validate

### 9.10 Test Drift vs Real Regression
- `test_e2e.py` may fail with stale expectations
- Check if failure is in character count rules, missing API exports, or content_type requirements
- If these are known drift → document in issue #183
- If new failure → investigate as potential regression
- Use `git bisect` to find if failure is new

---

## 10. Maintenance Rule

### 10.1 PR Checklist for Product Radar Changes
Every PR that changes Product Radar behavior must include:

- [ ] **Product Radar operator manual updated** (this file)
- [ ] **New/changed env vars documented** without secret values
- [ ] **New/changed state files documented** (path, schema, purpose, safe-to-reset)
- [ ] **New/changed commands documented** (reads, writes, mutates state, external contact, CI-safe)
- [ ] **Processed-state behavior documented** (how the system knows signal is already seen/scored/rejected/drafted/published)
- [ ] **Safety gates unchanged or updated** (no autoposting, no secrets, dry-run default)
- [ ] **Validation results included** (py_compile, test-lenses, jekyll-tested, pytest)
- [ ] **Closeout report generated** if this is a run PR

### 10.2 Versioning
- Update the version header at the top of this manual when changed
- Format: `Version: YYYY-MM-DD`
- If the change is minor, increment the date only
- If the change is structural, note it in the Purpose section

### 10.3 Review Process
- This manual is reviewed as part of every Product Radar PR
- If a PR changes behavior but does not update this manual, the PR is blocked
- The conductor (Kimi) enforces this checklist before approving merge

---

## Gaps and Known Issues

| Issue | Status | Location |
|-------|--------|----------|
| `events.jsonl` not implemented | OPEN | Signal lifecycle tracking |
| `test_e2e.py` stale failures | OPEN | Issue #183 in materialistOS |
| Jekyll build not available in cloud | KNOWN | No Ruby in coordinator environment |
| Mac Mini git push timeouts | KNOWN | Agent reliability issue |
| File attachment UI issues | KNOWN | Coordinator → user file delivery |
| `approved.json` or approval file mechanism | NOT YET | Manual approval is chat-based only |
| Repeated-structure detection (full history) | NOT YET | Currently only checks My take vs lens |
| Human voice score (1-5) | NOT YET | Currently only pass/fail |

---

*End of manual. Last updated: 2026-05-30*
