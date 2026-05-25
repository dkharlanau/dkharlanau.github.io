# Site Content Validation

Status: operational
Purpose: lightweight pre-build content validation for `dkharlanau.github.io`
Created for: issue #5
Last updated: 2026-05-26

---

## What this validator checks

`scripts/validate_site_content.py` is a local Python script that validates site content structure **without requiring Ruby or Jekyll**. It checks:

### 1. `_data/atlas_index.yml`

- **Valid YAML** — parses without errors.
- **Required sections** — `meta`, `fallback`, and `topic_clusters` must exist.
- **Cluster completeness** — every cluster must have:
  - `id`, `title`, `path`, `topic_cluster`
  - `keywords`, `allowed_update_types`, `source_policy`
  - `last_reviewed`, `related_pages`, `agent_notes`
- **Path resolution** — existing paths must resolve to files on disk or valid Jekyll collection paths (`_notes/`, `_blog/`).
- **Future placeholders** — clusters with `path: null` are reported as pending, not errors.

### 2. `docs/templates/*.md`

- **Required body metadata** — every template must contain the required metadata block:
  - `Source:`, `Date checked:`, `Confidence:`
  - `Related page/topic:`, `Practical implication:`
- **Front matter safety** — draft/news templates must keep `robots: noindex` and `sitemap: false` defaults. Atlas templates (e.g., `atlas-fact-update.md`, `practical-process-note.md`) may use `index` because they target public Atlas pages.
- **Excluded path** — templates live under `docs/templates/`, which `_config.yml` excludes from the build.

### 3. Future news / datelined updates

- If `/news/` does **not exist**, the validator reports it as **pending** (issue #3) and does not fail.
- If `/news/` exists and contains `.md` files, it validates required front matter (`title`, `date`, `permalink`).

### 4. Homepage protection

- The validator checks **staged changes** via `git diff --cached --name-only`.
- If protected files (`index.md`, `_data/home.yml`) are staged, it warns or fails depending on flags.
- Use `--allow-homepage` to bypass this check when a homepage change is explicitly authorized.

---

## How to run it

### Default run

```bash
python3 scripts/validate_site_content.py
```

Exit codes:
- `0` — passed (no errors; warnings may be present)
- `1` — failed (errors detected)

### Strict mode

Treats all warnings as errors:

```bash
python3 scripts/validate_site_content.py --strict
```

### Allow homepage changes

Bypasses the staged-homepage-protection check:

```bash
python3 scripts/validate_site_content.py --allow-homepage
```

### Syntax check (CI-friendly)

```bash
python3 -m py_compile scripts/validate_site_content.py
```

---

## What warnings mean

| Warning | Meaning | Action |
|---|---|---|
| `path is null (future placeholder)` | A topic cluster has no page yet. | None — expected for planned content. |
| `/news/ does not exist yet` | News section not created. | Wait for issue #3 or create it. |
| `missing 'noindex' in robots` | A draft template lacks the noindex directive. | Add `robots: noindex,follow` to keep it out of search indexes until reviewed. |
| `missing 'sitemap:' front matter` | A draft template lacks an explicit sitemap declaration. | Add `sitemap: false` for drafts, `sitemap: true` for public pages. |
| `Staged changes touch protected homepage files` | A commit would modify `index.md` or `_data/home.yml`. | Use `--allow-homepage` only if a homepage issue explicitly authorizes the change. |

---

## Relationship to issue #7 (Ruby / Jekyll build validation)

This validator is **not** a replacement for `bundle exec jekyll build`. It does not:

- Render Liquid templates
- Resolve Jekyll collections or plugins
- Validate CSS, HTML, or JSON-LD output
- Check internal links in built HTML

What it does:
- Catches structural YAML errors before build
- Validates metadata completeness
- Checks file existence for paths declared in `atlas_index.yml`
- Protects homepage files from accidental commits

**Recommended pipeline:**

1. Run `python3 scripts/validate_site_content.py` (this script — issue #5).
2. Run `bundle exec jekyll build` (requires Ruby — issue #7).
3. Run `scripts/check_links.py _site/` and `scripts/check_seo.py _site/` (requires built site — issue #7).

If Ruby is unavailable, step 2–3 remain pending. This script provides a lightweight pre-check that can run in any Python environment.

---

## Files

- `scripts/validate_site_content.py` — validator script
- `docs/site-content-validation.md` — this documentation

---

## Dependencies

- Python 3.8+
- PyYAML (`pip install pyyaml`)
- Git (for homepage-protection staged-change detection)

No Ruby, Bundler, or Jekyll required.
