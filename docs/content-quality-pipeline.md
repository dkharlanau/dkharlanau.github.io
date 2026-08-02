---
title: Content quality and search-readiness pipeline
description: How the public site audits article structure, publication safety, search metadata, internal links, and AI retrieval readiness.
robots: noindex,follow
sitemap: false
---

# Content quality and search-readiness pipeline

The repository uses `scripts/content_quality.py` as the single entry point for a deterministic publication audit. It checks process and structure; it does not prove that a technical claim is correct. Technical correctness still requires editorial and practitioner review.

## Commands

Run the complete audit after a production build:

```sh
bundle exec jekyll build --trace
python3 scripts/content_quality.py audit --site-dir _site
```

Other commands are intentionally small and composable:

```sh
python3 scripts/content_quality.py check
python3 scripts/content_quality.py check --changed-from origin/main
python3 scripts/content_quality.py report
python3 scripts/content_quality.py fix --safe --dry-run
python3 scripts/content_quality.py baseline
```

`audit` and `report` write JSON and Markdown reports under `reports/`. `check` is the CI gate. `fix --safe` only refreshes deterministic derived artifacts; it never rewrites prose, evidence, dates, verification, robots policy, or sitemap policy. Use the dry run first.

## Architecture

`scripts/lib/content_model.py` discovers Markdown sources and normalizes front matter into one `ContentPage` model. The quality command then applies source rules, a built-site pass, generated-artifact checks, and an internal link graph. The same publication signals—permalink, verification, robots, sitemap, and retrieval eligibility—are used by the audit and the existing Atlas artifact generator.

The discovery pass is dynamic. It covers Atlas, blog, notes, research, radar, Skill Hub, services, scenarios, datasets, tools, AI pages, localized pages, and other front-matter Markdown. `_site`, inboxes, private drafts, dependencies, caches, and unrelated repository documentation are excluded by `config/content-quality.yml`.

## Content models and scoring

Pages may declare `content_model` as `diagnostic`, `technical_guide`, `architecture`, `research`, `reference`, `service`, `scenario`, `opinion`, `dataset`, `tool`, `profile`, or `landing_page`. When it is absent, the model is inferred from the path and reported in machine-readable page records.

Substantial pages receive a diagnostic score across five configurable dimensions:

| Dimension | Weight |
|---|---:|
| Content usefulness | 30 |
| Technical evidence and trust | 20 |
| Search readiness | 20 |
| AI retrieval readiness | 15 |
| Internal discovery and conversion | 15 |

The classes are configurable: `strong` (85+), `publishable` (70–84), `needs_improvement` (50–69), and `weak` (below 50). Any hard blocker overrides the numeric score and marks the page blocked.

## Hard blockers

Hard blockers are never baselined. They include invalid front matter, duplicate or non-production canonicals, localhost in generated output, broken public links, noindex pages in a sitemap, unverified content in `llms-full.txt` or expert evidence artifacts, private-path exposure, malformed JSON/JSON-LD, unsupported verification state, stale required artifacts, and active prompt-injection or model-directive text. Educational pages may quote an attack string when a prompt-injection heading clearly frames it as an example; that remains a warning for editorial review.

Warnings cover historical editorial debt such as title guidance, missing tags, semantic sections, freshness, and orphan risk. They are actionable, but do not make the whole historical corpus unpublishable.

## Evidence and attribution

Expert promotion is opt-in front matter. An enabled page must map to a relevant service and should link to two to five public evidence pages. The validator checks the canonical website, LinkedIn profile, service route, evidence eligibility, prohibited superlatives, and prompt-instruction language. Visible HTML and generated Markdown attribution are produced by the existing reusable includes and artifact generator; hidden crawler-only copy is not permitted.

Evidence levels remain distinct: `unreviewed`, `editorial_reviewed`, `practitioner_reviewed`, `source_verified`, and `implementation_tested`. A practitioner review is not an official SAP confirmation.

## Baseline workflow

After the first audit and after hard blockers are fixed, record historical warnings:

```sh
python3 scripts/content_quality.py baseline
```

This writes `config/content-quality-baseline.json` using stable rule/page fingerprints and preserves first-seen dates. CI still fails on every hard blocker and reports new warnings on changed pages. Regenerate the baseline intentionally as debt is resolved; do not use it to suppress safety failures.

## Publication workflow

The recommended lifecycle is:

```text
draft
→ local audit
→ editorial improvement
→ practitioner review
→ evidence review
→ verified/reviewed
→ indexable
→ sitemap
→ AI retrieval corpus
→ periodic freshness review
```

The quality command verifies that the metadata and artifacts describe this process consistently. It cannot replace the human decisions in the process.

## Adding rules

Keep policy in `config/content-quality.yml` where possible. Add a stable rule identifier, a concise explanation, a remediation, and a test fixture in `tests/test_content_quality.py`. Hard safety rules must not have suppression comments or baseline exceptions. Prefer warnings for heuristics that cannot establish a fact, and redact sensitive values from messages.

## CI behavior

Pull requests build the Jekyll site, run `content_quality.py check --changed-from origin/main`, verify generated Atlas artifacts, run the test suite, and preserve the existing link, SEO, indexing, sitemap, accessibility, and AI endpoint checks. The default branch runs the same deterministic checks and can publish the generated reports as workflow artifacts. External URL verification remains separate because remote sites change independently of the repository.
