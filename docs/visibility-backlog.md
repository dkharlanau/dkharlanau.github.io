# Visibility & Citations Backlog

Goal: maximize discovery, reuse, and **proper attribution** for dataset bytes, while keeping **non-commercial** terms.

## What is “done” (already implemented in repo)

- Data license split: datasets are **CC BY-NC 4.0**, site materials remain **All Rights Reserved**.
- Suggested citation surfaced:
  - in each dataset JSON (`meta.attribution.preferred_citation`)
  - in dataset entry pages (`/datasets/view/...`)
  - in dataset landing/list pages (`/datasets/...`)
- Machine-readable metadata improved:
  - JSON-LD `Dataset` on entry pages now includes `license` and `citation`
  - `datasets/manifest.json` includes top-level `license` + `attribution`
- Indexing hygiene:
  - `robots.txt` disallows legacy duplicate JSON roots (`/DAMA/`, `/agentic-bytes/`, etc.)
  - dataset pages add `rel="license"` in HTML head

## P0 — Canonical DOI (highest ROI)

- [ ] Connect GitHub repo to Zenodo and enable DOI minting (via Zenodo UI).
- [ ] Decide DOI strategy:
  - [ ] One “concept DOI” for the whole collection (`/datasets/`)
  - [ ] OR separate DOIs per collection (agentic-bytes, TRIZ-bytes, DAMA, ams, LLM-prompts)
- [ ] Create a first tagged release (`v1.0.0`) and verify Zenodo minted a DOI.
- [ ] Add DOI back into:
  - [ ] `/legal/datasets/` (recommended citation)
  - [ ] `CITATION.cff` (preferred citation)
  - [ ] dataset entry pages (show DOI + link)
  - [ ] `meta.attribution.preferred_citation` format (include DOI when present)

## P1 — Mirrors for community discovery

- [ ] Publish mirrors (keep Zenodo DOI as canonical):
  - [ ] Hugging Face `datasets` repo (dataset card + usage examples + DOI link)
  - [ ] Kaggle Dataset (description + DOI link + 1–2 demo notebooks)
- [ ] Cross-link everywhere:
  - [ ] site → DOI → GitHub → HF/Kaggle
  - [ ] HF/Kaggle → DOI + canonical site pages

## P1 — Catalogs / directories

- [ ] Add entries to relevant directories (where applicable):
  - [ ] Papers with Code (if there is a benchmark/task match)
  - [ ] OpenML (if any tabular datasets fit)

## P2 — Dataset paper (trust + citations)

- [ ] Write a short dataset paper / tech report (arXiv or similar):
  - motivation + dataset description
  - schema + examples
  - licensing + attribution
  - limitations / intended use
  - DOI + canonical URLs

## Operational checklist

- Regenerate metadata after dataset edits:
  - `./bin/enrich_datasets.py`
  - `./bin/generate_dataset_pages.py`
- SEO sanity check:
  - `python3 scripts/check_seo.py`

