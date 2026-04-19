# AGENTS.md

Project-specific guidance for coding agents working in this public GitHub Pages repository.
Use this file as the short operational source of truth. Open deeper docs only when the task needs them.

## Project Snapshot

- Stack: Jekyll/GitHub Pages, Ruby `3.2.3`, Python generator/check scripts, and one Node generator for DAMA pages.
- Main site content: `_data/`, `_notes/`, `_blog/`, `services/`, `legal/`, `index.md`, and `assets/main.css`.
- Layout and rendering: `_layouts/`, `_includes/`, `_includes/sections/`, and `_includes/seo/structured-data.html`.
- Canonical datasets: `datasets/` plus machine-readable mirrors in `ai/`.
- Generated public dataset pages live under `datasets/view/` and `docs/dama/`; update the generator when changing their structure.

## Public Repo Safety

- Treat every committed file as public. Do not commit LinkedIn exports, raw dumps, local configs, secrets, private notes, bytecode, caches, `_site/`, or temporary transfer folders.
- Do not add personal email or phone data unless the task explicitly says it should be public.
- Before adding or reusing any third-party logo, icon, trademark, or brand asset, verify the license, applicable brand-guidelines, or obtain written permission from the rights holder. If permission is unclear, do not commit the asset.
- Keep canonical dataset content under `datasets/`; do not reintroduce root duplicate folders such as `TRIZ-bytes/`, `DAMA/`, `LLM-prompts/`, `agentic-bytes/`, or dated transfer folders.
- Use `scripts/check_public_repo.py` before publishing changes that touch repo structure, datasets, resume data, or config.

## Working Rules

- Prefer data edits in `_data/*.yml` for repeatable content and page edits in the existing Markdown files for standalone pages.
- Prefer reusing existing section partials and CSS tokens over adding one-off layouts.
- For dataset metadata, use `bin/enrich_datasets.py`; for dataset pages, use `bin/generate_dataset_pages.py`; for DAMA standalone pages, use `scripts/generate_dama_pages.js`.
- Keep generated files and generators in sync. If generated output changes, record which generator command produced it.
- Avoid broad cleanup outside the requested area unless it is public-safety related and covered by this guide.

## Validation

Run the smallest relevant set first, then the full sequence before publishing:

```sh
./bin/setup
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

Local hooks are opt-in:

```sh
git config core.hooksPath .githooks
```
