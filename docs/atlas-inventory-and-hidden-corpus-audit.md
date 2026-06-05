# Atlas Inventory and Hidden Corpus Audit

**Repository:** `dkharlanau.github.io`  
**Audit date:** 2026-06-09  
**Scope:** Read-only inventory and diagnosis. No files modified.  
**Auditor:** Kimi Agent Swarm

---

## 1. Executive Summary

The public Atlas discovery layer reports **22 pages** (`manifest.json`), split into **14 verified** and **8 unverified**. This count is accurate and internally consistent: the hardcoded `ATLAS_FILES` list, the filesystem under `atlas/`, and `manifest.json` are all in sync.

However, the repository contains **substantially more knowledge material** that is not counted by the Atlas discovery layer. The hidden corpus falls into three broad categories:

1. **Public Jekyll collections** (`_notes/`, `_radar/`, `_news/`, `_blog/`) — 16 markdown files, public-facing, but living outside the `atlas/` tree and lacking `atlas_section` frontmatter.
2. **Public non-Atlas pages** (`services/`, `ai/`, `datasets/`) — 184 markdown files, public-facing, but serving different purposes (service offerings, AI routing, generated dataset views).
3. **Private/excluded material** (`Kimi_Agent_SAP Atlas Expansion/`, `docs/templates/`, `professional-radar/`) — 776 files, excluded from the Jekyll build or marked noindex.

**No public Atlas article is missing from `ATLAS_FILES`.** The 22-page count is not a bug — it is a deliberate curation boundary. The main risk is that the hardcoded list makes it easy to forget new `atlas/` articles during future publishing workflows.

---

## 2. Current Public Atlas Count

| Source | Count | Verified | Unverified |
|--------|-------|----------|------------|
| `atlas/manifest.json` | 22 | 14 | 8 |
| `ATLAS_FILES` (hardcoded) | 22 | 14 | 8 |
| Actual article pages under `atlas/` | 22 | 14 | 8 |
| Section / index / support pages under `atlas/` | 10 | — | — |
| **Total files under `atlas/`** | **33** | — | — |

### 2.1 Manifest sections

| Section | Articles | Verified | Unverified |
|---------|----------|----------|------------|
| `ai-operations` | 3 | 3 | 0 |
| `automation` | 3 | 3 | 0 |
| `concepts` | 4 | 4 | 0 |
| `data-quality` | 2 | 2 | 0 |
| `diagnostics` | 4 | 0 | 4 |
| `maps` | 2 | 2 | 0 |
| `sap` | 4 | 0 | 4 |

---

## 3. Full `atlas/` File Inventory

### 3.1 Article pages (22) — all in `ATLAS_FILES`

| # | Path | Title | Section | Status | Verified |
|---|------|-------|---------|--------|----------|
| 1 | `atlas/ai-operations/ai-agent-for-sap-support.md` | AI Agent for SAP Support | ai-operations | reviewed | true |
| 2 | `atlas/ai-operations/ai-ready-process-documentation.md` | AI-Ready Process Documentation | ai-operations | reviewed | true |
| 3 | `atlas/ai-operations/authorization-aware-ai-for-sap.md` | Authorization-Aware AI for SAP | ai-operations | reviewed | true |
| 4 | `atlas/automation/agent-assisted-development-workflows.md` | Agent-Assisted Development Workflows | automation | reviewed | true |
| 5 | `atlas/automation/operational-memory-for-sap-ams.md` | Operational Memory for SAP AMS | automation | reviewed | true |
| 6 | `atlas/automation/rule-based-automation-vs-ai.md` | Rule-Based Automation vs AI | automation | reviewed | true |
| 7 | `atlas/concepts/order-to-cash.md` | Order to Cash | concepts | reviewed | true |
| 8 | `atlas/concepts/sap-atp-is-not-inventory.md` | SAP ATP Is Not Inventory | concepts | reviewed | true |
| 9 | `atlas/concepts/sap-stock-exists-not-promisable.md` | SAP Stock Exists but Is Not Promisable | concepts | reviewed | true |
| 10 | `atlas/concepts/store-receiving-sap-retail.md` | Store Receiving in SAP Retail | concepts | reviewed | true |
| 11 | `atlas/data-quality/master-data-governance-failure-modes.md` | Master Data Governance Failure Modes | data-quality | reviewed | true |
| 12 | `atlas/data-quality/sap-master-data-quality.md` | SAP Master Data Quality | data-quality | reviewed | true |
| 13 | `atlas/diagnostics/pos-sales-not-reflected-in-sap.md` | POS Sales Not Reflected in SAP | diagnostics | needs_verification | false |
| 14 | `atlas/diagnostics/sap-goods-receipt-diagnostics.md` | SAP Goods Receipt Diagnostics | diagnostics | needs_verification | false |
| 15 | `atlas/diagnostics/sap-invoice-split-analysis.md` | SAP Invoice Split Analysis | diagnostics | needs_verification | false |
| 16 | `atlas/diagnostics/sap-sales-order-block-diagnosis.md` | SAP Sales Order Block Diagnosis | diagnostics | needs_verification | false |
| 17 | `atlas/maps/order-to-cash-map.md` | Order to Cash Map | maps | reviewed | true |
| 18 | `atlas/maps/procure-to-pay-map.md` | Procure to Pay Map | maps | reviewed | true |
| 19 | `atlas/sap/gr-ir-clearing-explained.md` | SAP GR/IR Clearing Explained | sap | needs_verification | false |
| 20 | `atlas/sap/sap-item-category-determination.md` | SAP Item Category Determination | sap | needs_verification | false |
| 21 | `atlas/sap/sap-partner-determination-failures.md` | SAP Partner Determination Failures | sap | needs_verification | false |
| 22 | `atlas/sap/sap-pricing-procedure-debugging.md` | SAP Pricing Procedure Debugging | sap | needs_verification | false |

### 3.2 Section / index / support pages (10) — NOT in `ATLAS_FILES`

| Path | Title | Purpose |
|------|-------|---------|
| `atlas/index.md` | Knowledge Atlas — SAP, Operations, Data, Automation, and AI Support Concepts | Root index |
| `atlas/ai-operations/index.md` | Atlas AI Operations — AI-Assisted Support and Operational Memory | Section index |
| `atlas/automation/index.md` | Atlas Automation — SAP Support Automation and Agentic Workflows | Section index |
| `atlas/concepts/index.md` | Atlas Concepts — Business and SAP Concepts | Section index |
| `atlas/data-quality/index.md` | Atlas Data Quality — SAP Master Data and Operational Data Quality | Section index |
| `atlas/diagnostics/index.md` | Atlas Diagnostics — SAP Support and AMS Diagnostics | Section index |
| `atlas/links/index.md` | Atlas Links — Reference Routes | Reference index |
| `atlas/maps/index.md` | Atlas Maps — Process and Dependency Maps | Section index |
| `atlas/research-notes/index.md` | Atlas Research Notes — Noindex Working Notes | Noindex working notes |
| `atlas/sap/index.md` | Atlas SAP Section — Configuration and Support Concepts | Section index |

### 3.3 Non-markdown files (1)

| Path | Purpose |
|------|---------|
| `atlas/manifest.json` | Discovery layer artifact |

---

## 4. ATLAS_FILES Coverage Check

| Check | Result |
|-------|--------|
| Manifest count matches `ATLAS_FILES` length | ✅ 22 == 22 |
| Manifest verified/unverified matches frontmatter | ✅ 14 verified, 8 unverified |
| All article pages present in `ATLAS_FILES` | ✅ 22/22 |
| All `ATLAS_FILES` exist on disk | ✅ 22/22 |
| No extra article pages outside `ATLAS_FILES` | ✅ |
| Section/index pages excluded from `ATLAS_FILES` (by design) | ✅ 10 excluded |
| **No discrepancies found** | ✅ |

---

## 5. Hidden / Excluded Corpus Inventory

### 5.1 Public Jekyll collections (outside `atlas/`)

| Directory | Exists | Files | Markdown | Jekyll output | Public? | Atlas? | Classification |
|-----------|--------|-------|----------|---------------|---------|--------|----------------|
| `_notes/` | Yes | 7 | 7 | `true` | Public | Partial | `ready_for_review_candidate` (6/7) |
| `_radar/` | Yes | 5 | 5 | `true` | Public | Partial | `should_not_publish` (dated signals) |
| `_news/` | Yes | 3 | 3 | `true` | Public | Partial | `should_not_publish` (dated news) |
| `_blog/` | Yes | 1 | 1 | `true` | Public | No | `should_not_publish` (editorial) |

**`_notes/` detail:**

| Path | Title | Atlas candidate? | Classification |
|------|-------|------------------|----------------|
| `_notes/ai_ml.md` | AI & ML Around SAP | Yes — deep SAP AI concept | `ready_for_review_candidate` |
| `_notes/ams.md` | SAP AMS Playbook | Yes — AMS operations knowledge | `ready_for_review_candidate` |
| `_notes/composable_erp.md` | Composable ERP Strategy for SAP Finance & Logistics | Yes — ERP architecture concept | `ready_for_review_candidate` |
| `_notes/consulting_principles.md` | Consulting Principles | Partial — delivery principles, not SAP procedure | `should_not_publish` |
| `_notes/process_audit.md` | Process Audit & Diagnostics | Yes — O2C/P2P diagnostics | `ready_for_review_candidate` |
| `_notes/system-architecture.md` | Operating a Neubrutalist design system | No — site design system note | `should_not_publish` |
| `_notes/tools_mini_apps.md` | Mini Apps & Prototypes | Yes — SAP mini-app patterns | `ready_for_review_candidate` |

**`_radar/` detail:**

| Path | Title | Classification |
|------|-------|----------------|
| `_radar/2026-04-14-sap-business-ai-q1-2026.md` | SAP Business AI Q1 2026 | `should_not_publish` (dated signal) |
| `_radar/2026-05-15-sap-clean-core-dashboard-cloud-alm.md` | SAP Clean Core Dashboard in Cloud ALM | `should_not_publish` (dated signal) |
| `_radar/2026-05-26-sap-s4hana-compatibility-packs-final-transition.md` | S/4HANA Compatibility Packs — Final Transition | `should_not_publish` (dated signal) |
| `_radar/2026-05-30-finding-the-needle-ai-assisted-debugging.md` | Finding the Needle — AI-Assisted Debugging | `should_not_publish` (dated signal) |
| `_radar/2026-05-31-mulesoft-developer-hub-serves-humans-and-ai-agents.md` | How MuleSoft Developer Hub Serves Humans and AI Agents | `should_not_publish` (dated signal) |

**`_news/` detail:**

| Path | Title | Classification |
|------|-------|----------------|
| `_news/2026-04-14-sap-business-ai-q1-2026.md` | SAP Business AI Q1 2026 | `should_not_publish` (dated news) |
| `_news/2026-05-15-sap-clean-core-dashboard-cloud-alm.md` | SAP Clean Core Dashboard and Cloud ALM Integration | `should_not_publish` (dated news) |
| `_news/2026-05-26-sap-s4hana-compatibility-packs-final-transition.md` | SAP S/4HANA Compatibility Packs Final Transition | `should_not_publish` (dated news) |

### 5.2 Public non-Atlas pages

| Directory | Exists | Files | Markdown | Jekyll excluded? | Public? | Atlas? | Classification |
|-----------|--------|-------|----------|------------------|---------|--------|----------------|
| `services/` | Yes | 7 | 7 | No | Public | Partial | `should_not_publish` (service pages) |
| `ai/` | Yes | 9 | 9 | No | Public | Partial | `should_not_publish` (routing pages) |
| `datasets/` | Yes | 320 | 168 | No | Public | Yes | `dataset_not_article` |

**`services/` detail:**

| Path | Title | Classification |
|------|-------|----------------|
| `services/index.md` | Services overview | `should_not_publish` (index) |
| `services/ams-cost-center-catalyst.md` | AMS Cost Center or Catalyst | `should_not_publish` (service page) |
| `services/sap-ai-ml-enablement.md` | SAP AI and ML Enablement | `should_not_publish` (service page) |
| `services/sap-ams-consulting.md` | SAP AMS Consulting | `should_not_publish` (service page) |
| `services/sap-integration-architecture.md` | SAP Integration Architecture Consulting | `should_not_publish` (service page) |
| `services/sap-mini-apps.md` | SAP Mini Apps and Automation Tools | `should_not_publish` (service page) |
| `services/sap-o2c-process-audit.md` | SAP O2C Process Audit | `should_not_publish` (service page) |

**`ai/` detail:**

| Path | Title | Classification |
|------|-------|----------------|
| `ai/index.md` | AI Routing Hub | `should_not_publish` (index) |
| `ai/certifications.md` | Certifications — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/incident-prevention-rca.md` | Incident Prevention and RCA — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/integration-reliability.md` | Integration Reliability — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/mdg-bp-governance.md` | MDG and BP Governance — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/operational-continuity.md` | Operational Continuity — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/practical-ai-for-sap-support.md` | Practical AI for SAP Support — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/publications.md` | Publications — AI Intent Entity | `should_not_publish` (routing page) |
| `ai/sap-ams-improvement.md` | SAP AMS Improvement — AI Intent Entity | `should_not_publish` (routing page) |

**`datasets/` detail:**

| Subdirectory | Files | Markdown | JSON/YAML | Classification |
|--------------|-------|----------|-----------|----------------|
| `datasets/` (root indexes) | 9 | 9 | 0 | `dataset_not_article` (catalog pages) |
| `datasets/DAMA/` | 11 | 1 | 10 | `dataset_not_article` |
| `datasets/TRIZ-bytes/` | 46 | 1 | 45 | `dataset_not_article` |
| `datasets/agentic-bytes/` | 24 | 1 | 23 | `dataset_not_article` |
| `datasets/LLM-prompts/` | 5 | 1 | 4 | `dataset_not_article` |
| `datasets/ai-business-signals/` | 18 | 1 | 17 | `dataset_not_article` |
| `datasets/ams/` | 52 | 1 | 51 | `dataset_not_article` |
| `datasets/view/` | 150 | 150 | 0 | `dataset_not_article` (generated view pages) |
| `datasets/types/` | 9 | 9 | 0 | `dataset_not_article` (type index pages) |

### 5.3 Private / excluded material

| Directory | Exists | Files | Markdown | Jekyll excluded? | Public? | Atlas? | Classification |
|-----------|--------|-------|----------|------------------|---------|--------|----------------|
| `Kimi_Agent_SAP Atlas Expansion/` | Yes | 753 | 753 | **Yes** | Private | Yes | `draft_needs_cleanup` / `internal_only` |
| `docs/templates/` | Yes | 12 | 12 | **Yes** | Private | No | `internal_only` |
| `professional-radar/` | Yes | 11 | 2 | **Yes** | Private | No | `internal_only` |
| `docs/` (non-templates) | Yes | 37 | 23 | Partial | Mixed | Partial | `internal_only` |

**`docs/` (non-templates) detail:**

| Path | Classification |
|------|----------------|
| `docs/atlas/ATLAS_EDITORIAL_REGISTER.md` | `internal_only` (noindex editorial control) |
| `docs/atlas/ATLAS_PUBLISHING_ROADMAP.md` | `internal_only` (noindex publishing roadmap) |
| `docs/classification-rules.md` | `internal_only` (radar classification rules) |
| `docs/content-taxonomy.md` | `internal_only` (content taxonomy) |
| `docs/homepage-datasets-review.md` | `internal_only` (internal design decision) |
| `docs/linkedin-editorial-policy.md` | `internal_only` (editorial policy) |
| `docs/local-site-validation.md` | `internal_only` (validation guide) |
| `docs/routing-contract.md` | `internal_only` (routing contract) |
| `docs/site-content-design-contract.md` | `internal_only` (design contract) |
| `docs/site-content-validation.md` | `internal_only` (validation rules) |
| `docs/site-structure-inventory.md` | `internal_only` (site structure map) |

### 5.4 Other root-level knowledge-related files

| File | Public? | Atlas? | Classification |
|------|---------|--------|----------------|
| `about.md` | Public | No | `should_not_publish` (bio page) |
| `certifications.md` | Public | Partial | `should_not_publish` (credentials page) |
| `publications.md` | Public | Partial | `should_not_publish` (publications list) |
| `education.md` | Public | No | `should_not_publish` (education page) |
| `ARCHITECTURE.md` | Public | Yes | `internal_only` (site architecture doc) |
| `DESIGN-SYSTEM.md` | Public | Yes | `internal_only` (design system doc) |
| `AGENTS.md` | Public | Yes | `internal_only` (agent operational guidance) |
| `index.md` | Public | No | `should_not_publish` (homepage — untouched) |
| `changelog.md` | Public | No | `should_not_publish` (changelog) |
| `404.md` | Public | No | `should_not_publish` (error page) |
| `closeout-*.md` (6 files) | Excluded | No | `internal_only` (project closeouts) |
| `implementation-*.md` (4 files) | Excluded | No | `internal_only` (implementation plans) |
| `site-audit-report.md` | Excluded | No | `internal_only` (audit report) |
| `README.md` | Excluded | No | `internal_only` (repo README) |
| `LLM.txt`, `llms.txt`, `llms-full.txt` | Public | Yes | `should_not_publish` (AI-readable manifests) |

---

## 6. Top Hidden Candidate Clusters

### 6.1 Best promotion candidates (`ready_for_review_candidate`)

These files are public, evergreen, SAP-topical, and structurally similar to Atlas articles. They lack only `atlas_section` / `status` / `verified` frontmatter and a move into `atlas/`.

| # | Path | Title | Suggested Atlas section |
|---|------|-------|------------------------|
| 1 | `_notes/ai_ml.md` | AI & ML Around SAP | `ai-operations` |
| 2 | `_notes/ams.md` | SAP AMS Playbook | `automation` or new `ams` |
| 3 | `_notes/composable_erp.md` | Composable ERP Strategy for SAP Finance & Logistics | `concepts` |
| 4 | `_notes/process_audit.md` | Process Audit & Diagnostics | `diagnostics` |
| 5 | `_notes/tools_mini_apps.md` | Mini Apps & Prototypes | `automation` or `ai-operations` |

**Total ready-for-review candidates: 5**

### 6.2 Draft workspace (`draft_needs_cleanup`)

| Directory | Files | Notes |
|-----------|-------|-------|
| `Kimi_Agent_SAP Atlas Expansion/` | 753 | Excluded from Jekyll. Contains raw source material, SEO topic maps, agentic workflows, verification logs. Per `ATLAS_EDITORIAL_REGISTER`: 18 reviewed, 15 needs verification, 0 research notes, 672 merge/consolidation candidates, 35 private, 13 archive/delete. |

### 6.3 Dataset corpus (`dataset_not_article`)

| Directory | Files | Notes |
|-----------|-------|-------|
| `datasets/view/` | 150 | Generated human-readable views of JSON dataset entries. Not authored articles. |
| `datasets/` (root + sub-indexes) | 18 | Catalog and type index pages. |

### 6.4 Dated signals (`should_not_publish`)

| Directory | Files | Notes |
|-----------|-------|-------|
| `_radar/` | 5 | Time-bounded industry signals. Not evergreen Atlas knowledge. |
| `_news/` | 3 | Dated news briefs. Not evergreen Atlas knowledge. |

---

## 7. Public Atlas vs Hidden Material — Comparison Table

| Public Atlas section | Current public page count | Hidden/draft candidate count | Main topic gaps | Best promotion candidates |
|----------------------|--------------------------|------------------------------|-----------------|---------------------------|
| `ai-operations` | 3 | 1 (`_notes/ai_ml.md`) | AI/ML sidecars, forecasting, risk scoring | `_notes/ai_ml.md` |
| `automation` | 3 | 2 (`_notes/ams.md`, `_notes/tools_mini_apps.md`) | AMS operating model, mini-app patterns | `_notes/ams.md`, `_notes/tools_mini_apps.md` |
| `concepts` | 4 | 1 (`_notes/composable_erp.md`) | Composable ERP, clean core strategy | `_notes/composable_erp.md` |
| `data-quality` | 2 | 0 | Master data governance depth | — |
| `diagnostics` | 4 | 1 (`_notes/process_audit.md`) | Process audit methodology, O2C/P2P diagnostics | `_notes/process_audit.md` |
| `maps` | 2 | 0 | Additional process maps (P2P depth, integration maps) | — |
| `sap` | 4 | 0 | SD pricing, partner determination, item category | — |
| **Total Atlas** | **22** | **5 ready-for-review** + **753 draft workspace** + **168 dataset views** | AMS playbook, composable ERP, AI/ML sidecars, process audit, mini apps | See section 6.1 |

---

## 8. Generator Design Recommendation

### 8.1 Current design

`scripts/generate_atlas_artifacts.py` uses a **hardcoded `ATLAS_FILES` list** (22 entries). It iterates this list to generate `manifest.json`, `llms-full.txt`, and `ai/rag/related.json`. Section/index pages are explicitly excluded. `llms-full.txt` further filters to `status == "reviewed"` and `verified == true`.

### 8.2 Options assessed

| Option | Approach | Pros | Cons |
|--------|----------|------|------|
| **A — Keep hardcoded list** | Maintain `ATLAS_FILES` manually | Safer; curated; manual control; no accidental inclusion of drafts or section pages | Risk: pages can be forgotten when new articles are added to `atlas/` |
| **B — Dynamic scan of `atlas/**/*.md`** | Discover all markdown files under `atlas/` automatically | Easier to scale; less drift | Risk: section pages, drafts, research notes, and noindex pages could be accidentally included unless filtered |
| **C — Dynamic scan with frontmatter filters** | Scan `atlas/**/*.md` but only include files where frontmatter has: `atlas_section` present, `status` defined, `permalink` under `/atlas/`, and not `layout: default` section index, and not `sitemap: false` unless intentionally included | Easier to scale; less drift; automatic exclusion of section pages and noindex content; curation moves from path list to content signals | Slightly more complex frontmatter parsing; requires consistent frontmatter hygiene |

### 8.3 Recommendation: Option C

**Recommended: Option C — dynamic scan with frontmatter filters.**

Rationale:
- The `atlas/` tree already uses consistent frontmatter signals (`atlas_section`, `status`, `verified`, `permalink`).
- Option C preserves curation but shifts it from a **path list** (easy to forget) to **content signals** (self-documenting).
- Section pages can be excluded by checking for the absence of `atlas_section` (all 10 section/index pages lack it; all 22 article pages have it).
- The `atlas/research-notes/index.md` page already has `sitemap: false` and no `atlas_section`, so it would be naturally excluded.
- This eliminates the risk of publishing a new `atlas/` article and forgetting to add it to `ATLAS_FILES`.
- The existing tests (`test_atlas_artifacts.py`) already validate manifest structure; they would catch any unexpected inclusions.

**Implementation note:** The generator should still validate counts (e.g., expect ≥ 22 articles) and fail loudly if the dynamic scan produces an unexpected number, preventing mass accidental inclusion.

---

## 9. Recommended Next PR Slices

### Slice 1 — Generator modernization (low risk, high value)
- Refactor `scripts/generate_atlas_artifacts.py` from hardcoded `ATLAS_FILES` to dynamic scan with frontmatter filters (Option C).
- Add a count-sanity check (e.g., expect 22–30 articles; fail if > 35 or < 20).
- Update tests if needed.
- **Do not change `scripts/generate_atlas_artifacts.py` yet** per audit constraints; this is a recommended future PR.

### Slice 2 — Promote `_notes` to Atlas (medium risk, editorial work)
- Select 1–2 best candidates from `_notes/` (e.g., `process_audit.md` and `ai_ml.md`).
- Add `atlas_section`, `status`, `verified` frontmatter.
- Move to `atlas/<section>/` with permalink under `/atlas/`.
- Run generator and tests.
- Update `_notes/` index or add redirects if needed.

### Slice 3 — Triage `Kimi_Agent_SAP Atlas Expansion/` (high volume, long-term)
- Use `ATLAS_EDITORIAL_REGISTER.md` and `ATLAS_PUBLISHING_ROADMAP.md` as the control surface.
- The register already classifies 753 files into buckets (A–F).
- Focus on the 18 "reviewed/index" (A) and 15 "noindex/needs verification" (B) files first.
- Merge or consolidate the 672 "merge/consolidation" (D) files into fewer, stronger articles.
- Keep 35 private (E) and delete/archive 13 (F).

### Slice 4 — Dataset-to-Atlas bridge (optional, architectural)
- Consider whether high-value dataset entries (e.g., `datasets/ams/`) deserve authored Atlas companion pages that explain the methodology behind the dataset.
- Keep dataset views as generated pages; do not conflate them with Atlas articles.

---

## 10. Validation Results

All validation commands were run. No files were modified during the audit.

| Command | Result |
|---------|--------|
| `git status --short` | 5 untracked files: `implementation-plan.md`, `implementation-report-slice-2.md`, `implementation-report-slice-3.md`, `implementation-report.md`, `site-audit-report.md` |
| `git diff --stat` | No tracked-file changes (empty output) |
| `python3 scripts/check_public_repo.py` | ✅ **Passed** — "Public repo hygiene check passed for 647 tracked files." |
| `python3 scripts/generate_atlas_artifacts.py --check` | ✅ **Passed** — "CHECK PASSED — all artifacts are up to date and valid." (5 YAML parse errors in docs/templates/ and docs/homepage-datasets-review.md are expected for template files with Jinja-like syntax; they do not affect artifact validity) |
| `python3 -m pytest tests` | ✅ **13 passed** in 0.44s |

### 10.1 Homepage untouched

Confirmed: `index.md` was not read for content modification, not edited, and not written to. The homepage remains unchanged.

---

## 11. Summary

| Metric | Value |
|--------|-------|
| Current public Atlas count (manifest) | **22** |
| Actual `atlas/**/*.md` count | **32** (22 articles + 10 section/index pages) |
| ATLAS_FILES coverage | **100%** — no missing articles, no dangling references |
| Public hidden knowledge material (outside `atlas/`) | **~200 markdown files** across `_notes/`, `_radar/`, `_news/`, `_blog/`, `services/`, `ai/`, `datasets/` |
| Ready-for-review Atlas candidates | **5** (in `_notes/`) |
| Private draft workspace | **753** markdown files (excluded from Jekyll) |
| Dataset generated views | **150** markdown files (not authored articles) |
| More Atlas-like material exists? | **Yes** — 5 public notes are strong candidates; 753 draft files are in the excluded workspace |
| Why it is not counted today? | 1) Jekyll collections live outside `atlas/` and lack `atlas_section`; 2) Service/dataset/AI pages serve different purposes; 3) Draft workspace is explicitly excluded; 4) Generator only reads hardcoded `ATLAS_FILES` |
| Recommended next action | **Slice 1:** Modernize generator to Option C (dynamic scan with frontmatter filters). **Slice 2:** Promote 1–2 `_notes/` articles to `atlas/` after editorial review. **Slice 3:** Continue triaging `Kimi_Agent_SAP Atlas Expansion/` using the existing editorial register. |

---

## 8. Post-Implementation Note (Slice 1 — Dynamic Discovery)

**Status:** Completed on branch `feature/atlas-dynamic-discovery`.

The hardcoded `ATLAS_FILES` list has been replaced with `discover_atlas_articles()`, which dynamically scans `atlas/**/*.md` and includes only curated public Atlas article pages that satisfy all of the following:

- Frontmatter `permalink` starts with `/atlas/`
- Frontmatter contains `atlas_section`, `status`, and `verified`
- Path is not a section or index page (`*/index.md` is excluded)
- Pages marked `sitemap: false` are still included if they carry full article frontmatter (this preserves the 8 unverified article pages that set `sitemap: false` while remaining part of the Atlas)

**Result:**
- Atlas article count remains **22** (14 verified, 8 unverified)
- `manifest.json`, `llms-full.txt`, and `ai/rag/related.json` are generated from the same 22 pages as before
- Draft material outside `atlas/` and the private workspace remain intentionally excluded
- New Atlas pages will be discovered automatically as long as they include the required frontmatter fields

*End of audit report.*
