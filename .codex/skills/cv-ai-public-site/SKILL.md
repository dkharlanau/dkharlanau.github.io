---
name: cv-ai-public-site
description: Use when working in this cv-ai Jekyll public GitHub Pages repo on content, datasets, SEO metadata, resume exports, public hygiene, or Codex readiness. Follow the repo's canonical dataset paths, generator flow, public-safety checks, and validation commands.
---

# CV AI Public Site

## Workflow

- Start with `AGENTS.md` for repo rules and current validation commands.
- Treat the repository as public by default. Do not add raw LinkedIn exports, local configs, secrets, bytecode, `_site/`, caches, or temporary transfer folders.
- Edit canonical content in `_data/`, `_notes/`, `_blog/`, `services/`, `legal/`, `index.md`, and `assets/main.css`.
- Keep canonical dataset JSON under `datasets/`; do not reintroduce root duplicate dataset folders or dated transfer folders.
- If generated dataset pages change, update the generator too.

## Generators

- Dataset metadata: `python3 bin/enrich_datasets.py`
- Dataset pages: `python3 bin/generate_dataset_pages.py`
- DAMA pages: `node scripts/generate_dama_pages.js`
- Static sitemap helper if needed: `python3 bin/build_static_sitemap.py`

## Public Hygiene

- Run `python3 scripts/check_public_repo.py` before publishing changes that touch repo structure, datasets, resume data, scripts, or config.
- Keep fixture data sanitized and fake. Real LinkedIn archives belong in ignored local folders only.
- Public social links are intentional; secrets, private keys, bearer tokens, and local `.env*` files are not.

## Validation

Use the smallest relevant command set, then this full sequence before a public-ready change:

```sh
./bin/setup
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```
