---
published: false
robots: noindex,follow
sitemap: false
---

# Workflows — dkharlanau.github.io

Status: draft — internal documentation for maintainers and AI agents.  
Last updated: 2026-06-12

## Local setup workflow

1. Ensure Ruby >= 3.3.4 is available.
   - macOS (Homebrew): `brew install ruby@3.3` and `export PATH="/opt/homebrew/opt/ruby@3.3/bin:$PATH"`.
   - macOS/Linux (rbenv): `rbenv install -s 3.3.4 && rbenv local 3.3.4`.
2. Run the setup script:
   ```bash
   bin/setup
   ```
   It reads `.ruby-version`, installs the matching Bundler version, and runs `bundle install`.
3. Verify:
   ```bash
   ruby -v      # should report 3.3.4
   bundle -v    # should report 2.5.22
   ```

If Ruby is not available, you can still run the Python-only validators (`scripts/check_public_repo.py`, `scripts/validate_site_content.py`, `scripts/generate_atlas_artifacts.py --check`, pytest), but Jekyll build and post-build checks must be deferred to an environment with Ruby.

## Local validation workflow

Run the smallest relevant checks first, then the full sequence before publishing.

### Full sequence (run before any PR that touches content, structure, datasets, or config)

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
python3 scripts/generate_atlas_artifacts.py --check
python3 scripts/validate_site_content.py --strict
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/audit_discovery_outputs.py _site
```

### Smallest relevant set (for quick iteration)

```bash
python3 scripts/check_public_repo.py
python3 scripts/generate_atlas_artifacts.py --check
python3 -m pytest tests/test_atlas_artifacts.py
```

### Notes

- `pytest` covers Atlas artifacts, backlog pipeline, proposal quality, RAG evaluation, signal matching, IndexNow hardening, and more.
- `check_public_repo.py` scans tracked files for disallowed paths, secrets, and LinkedIn export references.
- `generate_atlas_artifacts.py --check` verifies that `atlas/manifest.json`, `llms-full.txt`, `ai/rag/related.json`, and `ai/atlas-compact-index.json` are up to date and consistent.
- `validate_site_content.py --strict` checks `_data/atlas_index.yml`, template fields, news section frontmatter, and homepage protection.
- `audit_discovery_outputs.py` audits built sitemaps, `robots.txt`, `llms.txt`/`llms-full.txt`, and JSON-LD blocks for leaks and unsupported fields.

## Content creation workflow

1. **Inspect** the nearest existing page of the same type.
2. **Identify** the content type and target path using `docs/site-structure-inventory.md` §7.
3. **Copy** the frontmatter pattern from the nearest page.
4. **Write** the new file. Reuse existing CSS classes and includes.
5. **Add** required frontmatter:
   - `title`, `description`, `permalink`, `layout: default`, `last_modified_at`.
6. **Cross-link** from relevant index pages.
7. **Validate**:
   ```bash
   bundle exec jekyll build
   python3 scripts/check_links.py _site
   python3 scripts/check_seo.py _site
   ```
8. **Report** changed files, verification level, validation results, and any gaps.

## Atlas page workflow

1. Inspect existing Atlas pages in the target section (`atlas/<section>/`).
2. Create `atlas/<section>/<slug>.md` with Level 1 frontmatter:
   ```yaml
   ---
   layout: default
   title: "..."
   description: "..."
   permalink: /atlas/<section>/<slug>/
   atlas_section: <section>
   domain: SAP AMS
   subdomain: ...
   concept_type: ...
   sap_area: "..."
   business_process: "..."
   status: needs_verification
   verified: false
   last_reviewed: YYYY-MM-DD
   author: Dzmitryi Kharlanau
   tags:
     - tag1
     - tag2
   related:
     - /atlas/<section>/<existing-page>/
   robots: noindex,follow
   sitemap: false
   ---
   ```
3. Add a link from `atlas/<section>/index.md` if appropriate.
4. Do **not** set `verified: true`, `robots: index,follow`, or `sitemap: true`.
5. Do **not** expose client names, ticket numbers, or proprietary details.
6. Validate with:
   ```bash
   python3 scripts/generate_atlas_artifacts.py --check
   bundle exec jekyll build
   python3 scripts/check_links.py _site
   python3 scripts/check_seo.py _site
   ```
7. If the check fails because the new page changes counts, run `python3 scripts/generate_atlas_artifacts.py` to regenerate artifacts.

## Skill Hub page workflow

1. Inspect `skill-hub/skill-page-template.md` and the nearest skill in the target group.
2. Create `skill-hub/<group>/<slug>-working-skill.md` with frontmatter and the standard skill structure:
   - When to use this skill
   - Inputs you need
   - Working method
   - Deliverables
   - Quality checklist
   - Agent instructions
   - Limitations
3. Update `skill-hub/<group>/index.md` to list the new skill.
4. If an agent skill counterpart is needed:
   - Create `agent-skills/skills/<skill-name>/SKILL.md` plus `references/method.md`, `references/templates.md`, `references/examples.md`.
   - Add the skill to `agent-skills/skill-index.yml` and relevant profiles.
   - Run `python3 agent-skills/exporters/validate_agent_skills.py`.
5. Validate with `bundle exec jekyll build` and `python3 scripts/check_links.py _site`.
6. Do not commit generated `.agents/skills/` or `.claude/skills/` exports.

## Generated artifact workflow

Regenerate after any change to Atlas content, dataset JSON files, or DAMA decision blocks.

### Atlas artifacts

```bash
python3 scripts/generate_atlas_artifacts.py
```

This updates:
- `atlas/manifest.json`
- `llms-full.txt`
- `ai/rag/related.json`
- `ai/atlas-compact-index.json`

Then verify:
```bash
python3 scripts/generate_atlas_artifacts.py --check
```

### Dataset artifacts

```bash
python3 bin/enrich_datasets.py
python3 bin/generate_dataset_pages.py
```

This updates:
- `datasets/manifest.json`
- `datasets/README.md`
- `datasets/index.md`
- `datasets/search.md`
- `datasets/types/**`
- `datasets/view/**`

### DAMA pages

```bash
node scripts/generate_dama_pages.js
```

This updates `docs/dama/*.html`, `docs/dama/tags/*.html`, and `docs/dama/assets/dama.css`.

### Commit rule

Always include the generator command in the commit message or PR description. Do not manually edit generated files.

## SEO validation workflow

1. Build the site:
   ```bash
   bundle exec jekyll build
   ```
2. Check for broken internal links:
   ```bash
   python3 scripts/check_links.py _site
   ```
3. Check SEO metadata:
   ```bash
   python3 scripts/check_seo.py _site
   ```
   This flags missing `<title>`/description, non-HTTPS canonicals, localhost URLs, and canonical/`og:url` mismatches.
4. Audit discovery outputs:
   ```bash
   python3 scripts/audit_discovery_outputs.py _site
   ```
   Use `--warn-only` to match CI behavior; use `--strict` to fail on any violation.
5. Fix issues, rebuild, and rerun until clean.

## GitHub Actions workflow

Two workflows are defined under `.github/workflows/`:

### CI — `.github/workflows/ci.yml`

Triggered on:
- Every pull request.
- Every push to `main`.

Steps:
1. Checkout.
2. Setup Ruby 3.3.4 with bundler cache.
3. Setup Python 3.12 and install `pytest pyyaml`.
4. Setup Node 22.
5. Run `python3 scripts/check_public_repo.py`.
6. Run `python3 scripts/generate_atlas_artifacts.py --check`.
7. Run `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests`.
8. Run `node scripts/generate_dama_pages.js`.
9. Run `bundle exec jekyll build`.
10. Run `python3 scripts/check_links.py _site`.
11. Run `python3 scripts/check_seo.py _site`.
12. Run `python3 scripts/validate_ai_endpoints.py _site`.

### IndexNow dry-run — `.github/workflows/indexnow-dry-run.yml`

Triggered on:
- Every push to `main`.
- Manual `workflow_dispatch` with optional `submit` and `use_all` booleans.

Steps:
1. Build the site.
2. Run `python3 scripts/audit_discovery_outputs.py _site --warn-only`.
3. Determine URL scope (changed files from `HEAD~1..HEAD`, or all if `use_all` is true).
4. Report mode.
5. Dry-run IndexNow submission by default.
6. Real submission only on manual dispatch with `submit: true` and `INDEXNOW_KEY` secret present.

## PR workflow

1. Create a branch from `main` with a descriptive name, e.g.:
   ```bash
   git checkout -b docs/current-architecture-workflows
   ```
2. Make the intended change. Do not mix unrelated changes.
3. Run the smallest relevant validation set.
4. Run the full validation sequence before publishing.
5. Stage and commit only the intended files.
6. Push the branch:
   ```bash
   git push -u origin docs/current-architecture-workflows
   ```
7. Open a pull request using the template in `.github/PULL_REQUEST_TEMPLATE/atlas-signal-update.md` when applicable.
8. PR description must include:
   - What changed and why.
   - Files changed and verification levels (for Atlas/Scenario pages).
   - Generator commands run.
   - Validation results summary.
   - Safety confirmations.
   - Known gaps or follow-up items.

## Merge workflow

1. Ensure CI is green.
2. Ensure Atlas artifact checks pass (`generate_atlas_artifacts.py --check`).
3. Squash or merge via GitHub UI. The default merge method should preserve the commit message.
4. GitHub Pages will build and deploy `main` automatically.

## Post-merge cleanup workflow

1. Delete the feature branch if it is no longer needed.
2. Verify the site is live at `https://dkharlanau.github.io`.
3. If IndexNow submission is desired, run the workflow manually from GitHub Actions with `submit: true`.
4. Regenerate any stale artifacts on `main` if the merge did not include them.

## Recovery workflow when local tree is dirty

1. Check status:
   ```bash
   git status --short
   ```
2. If the dirty files are unrelated to your task, **do not touch them**. Report them in your final output.
3. If you accidentally modified a file you should not have, restore it:
   ```bash
   git checkout -- <file>
   ```
4. If you created untracked files by mistake, remove them after confirming they are not needed:
   ```bash
   rm <file>
   ```
5. Create your branch only after the tree is in a known state, or stage only the files that belong to your task.
6. Never commit unrelated dirty files.

## Commands table

| Command | Purpose | When to run |
|---|---|---|
| `bin/setup` | Install Ruby/Bundler dependencies | Once per environment or after Gemfile changes |
| `bundle exec jekyll build` | Build site to `_site/` | After content/structure changes |
| `bundle exec jekyll serve` | Local preview server | Local development |
| `python3 scripts/check_public_repo.py` | Public-safety scan | Every validation pass |
| `python3 scripts/generate_atlas_artifacts.py --check` | Verify Atlas artifacts are up to date | After Atlas changes |
| `python3 scripts/generate_atlas_artifacts.py` | Regenerate Atlas artifacts | After promoting/demoting pages or adding Atlas pages |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests` | Run full test suite | Every validation pass |
| `python3 scripts/validate_site_content.py --strict` | Validate content structure | After data/template/homepage changes |
| `python3 scripts/check_links.py _site` | Find broken internal links | After Jekyll build |
| `python3 scripts/check_seo.py _site` | Validate title/description/canonical/og:url | After Jekyll build |
| `python3 scripts/audit_discovery_outputs.py _site` | Audit sitemap/robots/llms/JSON-LD | After Jekyll build |
| `python3 scripts/audit_discovery_outputs.py _site --warn-only` | Same, but allow baselined violations | CI and cautious local runs |
| `python3 bin/enrich_datasets.py` | Enrich dataset JSON files and regenerate manifest | After adding/editing dataset JSON |
| `python3 bin/generate_dataset_pages.py` | Generate dataset list/detail pages | After `bin/enrich_datasets.py` |
| `node scripts/generate_dama_pages.js` | Generate DAMA HTML pages | After changing `datasets/DAMA/*.json` |
| `python3 agent-skills/exporters/validate_agent_skills.py` | Validate agent skill packages | After skill changes |
| `python3 agent-skills/exporters/export_codex_skills.py --profile <profile>` | Export skills for Codex | After skill changes |
| `python3 agent-skills/exporters/export_claude_skills.py --profile <profile>` | Export skills for Claude Code | After skill changes |
| `python3 scripts/indexnow_submit.py` | Dry-run IndexNow submission | After merges that change indexable pages |
| `python3 scripts/indexnow_submit.py --submit --from-git-diff HEAD~1 HEAD` | Real IndexNow submission for changed URLs | Manual, requires `INDEXNOW_KEY` |
| `git diff --check` | Check for whitespace errors | Before commit |
