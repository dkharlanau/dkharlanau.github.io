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

### Atlas task packs

Reviewed, verified and indexable Atlas pages can select a visible citation section with
`task_pack_sections` in front matter. Each selected anchor must also appear in
`citation_sections`. Mark the relevant paragraphs or list items with
`data-atlas-task-part` using `task`, `conditions`, `method`, `example`, `check` or
`limits`. Use one task statement, at least one entry for each other part and at least
one visible HTTPS source link. Use a documented case and explain the limits of its application.

The existing `/ai/verified-pages.json` inventory attaches an `atlas.read_only_task.v1`
pack to that citation section. The pack version is a SHA-256 of its canonical URL,
schema, visible text and source URLs. A consumer can use those fields directly for
diagnostic context. `scripts/generate_atlas_artifacts.py --check` verifies the generated
inventory against the eligible source pages.

## Bulk integrity, meaning and discovery review

The same `audit --site-dir _site` command also produces
`reports/content-semantic-review.json` and `reports/content-rendered-discovery.json`.
It reuses `ContentPage`; it does not create a second definition of indexability or
human verification. Each run records source/config hashes and a hash of the
complete HTML inventory. Run it against the final production build.

Source review flags unmatched fenced examples, empty final sections, standalone
draft markers, generation preambles, and table-header mismatches. Fenced examples
are excluded from residue detection. It also inventories opening paragraphs,
examples, decision cues, boundaries, evidence URLs, exact body duplicates and
substantial paragraphs shared by at least three indexable articles. Duplicate
receipts contain hashes and paths, not copied text. These are review candidates,
including for intentionally short reference pages, not claims of plagiarism or
low quality. Every configured semantic signal has an implementation; unknown
signals cause a configuration failure instead of silently skipping a check.

The rendered pass follows the sitemap index recursively, checks emitted targets
and noindex/canonical consistency, and builds a graph from actual main-content
links. Global navigation, footer, sidebar, scripts and styles do not create
contextual inbound credit. Relative, query and fragment links resolve to the
same destination. Source-only orphan candidates and rendered orphan candidates
remain separate, because includes can emit useful links absent from Markdown.

For source-indexable pages it reports visible main-text coverage, snippet controls,
JSON-LD block counts, crawler policy from the built robots.txt, Open Graph image
URLs and large-image-preview permission. These are observable prerequisites,
not an AI or recommendation score. Remote image dimensions/relevance, CDN access,
actual indexing, source accuracy and search intent still require separate review.
The existing rendered SEO/schema tests remain the release checks for those contracts.

Read a stratified sample of flagged and unflagged pages in full before editing.
Check whether the page answers its title, explains an actual decision, provides
usable examples, states limits, and supports factual claims. Do not add headings,
word count, schema types or keywords solely to clear a heuristic. No articles,
review dates or publication states are rewritten by this audit.

## Adding rules

Keep policy in `config/content-quality.yml` where possible. Add a stable rule identifier, a concise explanation, a remediation, and a test fixture in `tests/test_content_quality.py`. Hard safety rules must not have suppression comments or baseline exceptions. Prefer warnings for heuristics that cannot establish a fact, and redact sensitive values from messages.

## CI behavior

Pull requests build the Jekyll site, run `content_quality.py check --changed-from origin/main`, verify generated Atlas artifacts, run the test suite, and preserve the existing link, SEO, indexing, sitemap, accessibility, and AI endpoint checks. The default branch runs the same deterministic checks and can publish the generated reports as workflow artifacts. External URL verification remains separate because remote sites change independently of the repository.

### Review the Atlas ATP case against its source

The Atlas generator checks the published ATP case against three claim bindings.
The bindings record the visible case paragraph, the supporting SAP passage,
its fingerprint and the SAP revision last reviewed. Regeneration checks the
local paragraph. Supply a fresh capture of the public KBA for a source check.

```sh
python3 scripts/generate_atlas_artifacts.py --claims-only --claim-source-html /path/to/sap-kba-3701626.html
```

The command reports each claim and its dependent outputs. An edited Atlas
paragraph or an unavailable or changed passage in a supplied capture requires
review before regeneration. When the command receives no capture, source status
is unknown. A new SAP page revision with the same scoped passages is reported
alongside the reviewed revision. The check reads the article text and metadata
without updating editorial review dates. The ATP case applies to the Create
and Change Sales Order comparison in SAP S/4HANA Cloud Public Edition.

The ATP section also exposes stable links to its case, verification step and
limits. Put `data-atlas-cite` and a unique `id` on an existing visible paragraph
or list item inside a declared citation section. The generator adds its exact
text, URL, fingerprint and any links found in that passage to the existing
`ai/verified-pages.json` entry. The text manifest lists the same links.
For method, example and verification passages in a task pack, the JSON includes
the visible conditions and limits under `context`, with their section URL.
The passage fingerprint covers that context. Inline sources still identify
links in the cited passage. A passage with no inline source cites Atlas for its
wording. Section-level sources describe the section as a whole.
