# Site Structure Inventory

Status: created for issue #6
Purpose: guide future agent-assisted updates to `dkharlanau.github.io` so new content fits the site visually, structurally, and strategically.
Last updated: 2026-05-26

---

## 1. Purpose

This file is the canonical map for autonomous and agent-assisted site updates. It exists so future Kimi/Codex agents know:

- where the site lives and what framework it uses;
- what pages and sections already exist;
- what layout and card patterns are available;
- where to place new content without breaking design consistency;
- what validation commands exist and how to run them.

Read `docs/site-content-design-contract.md` alongside this file before any update.

---

## 2. Site map

| Route | File | Purpose |
|---|---|---|
| `/` | `index.md` | Home — positioning, trust signals, CTAs, strategic frame. |
| `/about/` | `about.md` | Canonical profile — verified work history, credentials, machine-readable sources. |
| `/services/` | `services/index.md` | Service overview — four service cards, fit section, next-step CTA. |
| `/services/sap-ams-consulting/` | `services/sap-ams-consulting.md` | Service detail — problem, deliverables, related links. |
| `/services/sap-ai-ml-enablement/` | `services/sap-ai-ml-enablement.md` | Service detail. |
| `/services/sap-integration-architecture/` | `services/sap-integration-architecture.md` | Service detail. |
| `/services/sap-mini-apps/` | `services/sap-mini-apps.md` | Service detail. |
| `/services/sap-o2c-process-audit/` | `services/sap-o2c-process-audit.md` | Service detail. |
| `/services/ams-cost-center-catalyst/` | `services/ams-cost-center-catalyst.md` | Service detail. |
| `/atlas/` | `atlas/index.md` | Knowledge Atlas landing — nine section cards, pilot pages, context CTA. |
| `/atlas/concepts/` | `atlas/concepts/index.md` | Durable concept explanations (order-to-cash, ATP vs inventory, etc.). |
| `/atlas/maps/` | `atlas/maps/index.md` | Process and dependency maps. |
| `/atlas/sap/` | `atlas/sap/index.md` | SAP configuration/support notes. |
| `/atlas/diagnostics/` | `atlas/diagnostics/index.md` | Diagnostic patterns for repeat incidents. |
| `/atlas/ai-operations/` | `atlas/ai-operations/index.md` | AI-assisted support, operational memory, governance. |
| `/atlas/data-quality/` | `atlas/data-quality/index.md` | Master data, quality signals, failure modes. |
| `/atlas/automation/` | `atlas/automation/index.md` | Support automation, agentic workflows. |
| `/atlas/research-notes/` | `atlas/research-notes/index.md` | Noindex working area — useful but not polished. |
| `/atlas/links/` | `atlas/links/index.md` | Reference routes to profile, services, datasets. |
| `/blog/` | `blog/index.md` | Long-form essay listing — uses `site.blog` collection. |
| `/datasets/` | `datasets/index.md` | Dataset landing — six collections, KPIs, license block. |
| `/datasets/search/` | `datasets/search.md` | Search interface for datasets. |
| `/datasets/types/` | `datasets/types/index.md` | Browse datasets by type. |
| `/datasets/<collection>/` | `datasets/<collection>/index.md` | Collection index pages (AMS, TRIZ, agentic-bytes, etc.). |
| `/ai/` | `ai/index.md` | AI sources landing — routing page for AI-readable content. |
| `/ai/*.json` / `/ai/*.yml` | `ai/*` | Machine-readable exports (resume, profile audit, catalog, etc.). |
| `/notes/` | `notes/index.md` | Notes collection listing — uses `site.notes` collection. |
| `/notes/<slug>/` | `_notes/*.md` | Individual note pages (layout: `note`). |
| `/cv/` | `cv/index.html` | Interactive CV page. |
| `/faq/` | `faq/index.html` | FAQ page. |
| `/search/` | `search/index.md` | Site search. |
| `/legal/*` | `legal/*.md` | Policies: privacy, terms, disclosure, responsible AI, accessibility, datasets citation. |
| `/changelog/` | `changelog.md` | Release snapshot view driven by `_data/changelog.yml`. |
| `/404.html` | `404.md` | Error page. |

**Notable absence:** There is no `/news/` route or news section yet. This is expected — issue #3 will add it.

---

## 3. Page type classification

| Page | Type | Notes |
|---|---|---|
| `index.md` | home | Section-driven via `page.sections` array + `_data/home.yml`. |
| `about.md` | about/profile | Resume data-driven (`_data/resume.yml`), machine-readable links. |
| `services/index.md` | services | Overview with four service cards + fit/FAQ + CTA. |
| `services/*.md` | services | Individual service detail pages — `note-detail` layout inside `default`. |
| `atlas/index.md` | Atlas / knowledge | Landing with `atlas-card-grid`. |
| `atlas/**/*.md` | Atlas / knowledge | Topic pages, maps, diagnostics. Some are index pages, some are articles. |
| `blog/index.md` | blog / long-form | Listing page for `site.blog` collection. |
| `_blog/*.md` | blog / long-form | Individual blog posts (collection: `blog`, layout: `blog`). |
| `datasets/index.md` | datasets | Landing with `dataset-collection-grid`. |
| `datasets/<collection>/index.md` | datasets | Collection landing pages with JSON file listings. |
| `ai/index.md` | AI-readable/index | Routing page for AI-friendly content. |
| `ai/*.json`, `ai/*.yml` | AI-readable/index | Machine-readable data exports. |
| `notes/index.md` | other | Notes collection listing (similar to blog but shorter). |
| `_notes/*.md` | other | Individual notes (collection: `notes`, layout: `note`). |
| `legal/*.md` | legal/source/reference | Static policy pages. |
| `changelog.md` | other | Data-driven changelog (`_data/changelog.yml`). |
| `cv/index.html` | about/profile | Interactive CV. |

---

## 4. Existing layout patterns

### 4.1 Page layouts (`_layouts/`)

- **`default.html`** — master layout. Includes `head.html`, conditionally includes `header.html` (hidden on home), renders `{{ content }}`, includes `cta-global.html` (unless `hide_global_cta`), includes `footer.html`, includes structured data.
- **`note.html`** — article layout for notes. Backlink to `/notes/`, eyebrow, title, subtitle, metadata (published/updated/tags), body, optional `further_reading`.
- **`blog.html`** — article layout for blog posts. Same as `note.html` but backlink goes to `/blog/`.

### 4.2 Section builder (`_includes/page-builder.html`)

Homepage and some other pages declare sections in front matter:

```yaml
sections:
  - hero
  - analysis-problem
  - ai-costs-outcomes
  - strategic-context
  - credibility
  - faq
  - contact
```

`page-builder.html` routes each key to `_includes/sections/<key>.html`. This is the primary pattern for composing long pages from reusable blocks.

### 4.3 Hero sections

- **Home hero** (`_includes/sections/hero.html`): large centered composition, badge, title, subtitle, lead, profile image, contact actions, and a visual sidebar (the "operating value loop").
- **Atlas hero** (`atlas/index.md`): eyebrow, h1, lead paragraph, action buttons.
- **Dataset hero** (`datasets/index.md`): eyebrow, h1, lead, action buttons.

Rule: hero = one primary claim + one primary action + limited secondary actions.

### 4.4 Card grids

| Grid class | Used for | Location |
|---|---|---|
| `services-grid` | Service cards | `services/index.md`, `_includes/sections/services.html` |
| `atlas-card-grid` | Atlas section cards | `atlas/index.md` |
| `dataset-collection-grid` | Dataset collection cards | `datasets/index.md` |
| `notes-grid` | Blog/note cards | `blog/index.md`, `notes/index.md` |
| `signals-grid` / `signals-callouts` | Social/callout cards | `_includes/sections/signals.html` |

### 4.5 Section blocks

Standard section structure (seen across multiple pages):

```html
<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Category label</p>
    <h2>Section title</h2>
    <p class="lead">Optional framing paragraph.</p>
  </header>
  <!-- body: cards, prose, lists, etc. -->
</section>
```

Variant: `section-shell section-shell--flat` or `section-shell section-shell--premium` wraps content inside a tinted surface with internal heading block.

### 4.6 CTA areas

- **`section-actions`** — horizontal button row. Uses `.button` and `.button--primary`.
- **`cta-global.html`** — currently blank (intentionally). Home page uses inline CTAs.
- Service pages end with a `section-shell--premium` containing a next-step heading, lead, and `section-actions`.

### 4.7 Dataset/list patterns

- Dataset index: `dataset-hero` + `dataset-grid` (license block) + `dataset-kpis` (three KPI pills) + `dataset-collection-grid` (collection cards with `pill` + `link-arrow`).
- Dataset collection pages: simple listing of JSON entries with `neub-card` + `link-arrow`.

### 4.8 Footer / navigation

- **Header** (`_includes/header.html`): minimal. Branding link + "Back to main" on non-home pages. No top nav menu.
- **Footer** (`_includes/footer.html`): rich. Links to About, Services, AI sources, Datasets, Cite, Disclosure, AI policy, Privacy.

Navigation policy: new major sections should be added to the footer. The header stays minimal.

---

## 5. Component and card patterns

Future agents should reuse these exact patterns before inventing new ones.

### 5.1 Core CSS classes

| Class | Purpose | When to use |
|---|---|---|
| `section` | Content block wrapper | Every major page block. |
| `section-heading` | Standard heading block | Eyebrow + h2 + lead. |
| `eyebrow` | Small uppercase kicker | Before every h2 in sections. |
| `lead` | Framing paragraph | After heading, before body. |
| `neub-card` | Generic card shell | Any content container needing the site card style. |
| `service-card` | Service offer card | Services grid only. |
| `atlas-card` | Atlas section card | Atlas grid only. |
| `dataset-card` | Dataset collection card | Dataset grid only. |
| `note-card` | Blog/note listing card | Notes/blog grids only. |
| `button` | Action button | CTAs, hero actions. |
| `button--primary` | Primary action | One per section maximum. |
| `button--secondary` / `button--ghost` | Secondary action | Multiple allowed. |
| `link-arrow` | Text link with arrow | "Learn more", "Read page", "Open". |
| `pill` | Small tag/label | Dataset entry counts, tags. |
| `section-shell` | Tinted content wrapper | Flat or premium surface. |
| `section-actions` | Button row wrapper | End-of-section CTAs. |
| `faq-item` | FAQ block | Services fit section, FAQ page. |
| `breadcrumbs` | Breadcrumb nav | Atlas, service detail pages. |

### 5.2 Card anatomy

**Service card** (from `services/index.md`):
- eyebrow label (e.g., "1. Diagnose")
- h3 title
- subtitle (pain)
- summary (deliverable)
- `link-arrow` footer

**Atlas card** (from `atlas/index.md`):
- h2/h3 title
- paragraph description
- `link-arrow`

**Dataset card** (from `datasets/index.md`):
- h2 title
- paragraph description
- footer with `pill` (count) + `link-arrow`

**Note/blog card** (from `blog/index.md`):
- h2 title linked
- optional subtitle
- meta (date + tags)
- excerpt/summary paragraph
- `link-arrow`

### 5.3 Data-driven sections

Many homepage sections read from `_data/home.yml`. If adding a new homepage section, prefer adding data there and wiring it through `page-builder.html` rather than hardcoding in `index.md`.

---

## 6. Navigation and CTA map

### Footer links (canonical navigation)

```
About → /about/
Services → /services/
AI sources → /ai/
Datasets → /datasets/
Cite → /legal/datasets/
Disclosure → /legal/professional-disclosure/
AI policy → /legal/responsible-ai/
Privacy → /legal/privacy/
```

### When to add a new footer link

- A new top-level page type is introduced (e.g., `/news/` when issue #3 closes).
- A page moves from draft to primary surface.
- Do not add every new subpage to the footer.

### Header behavior

- Home page: no header visible.
- All other pages: branding + "Back to main" only.
- Do not add a traditional top nav menu without an explicit design issue.

### Internal CTAs

Common cross-links used across pages:
- `/about/` — profile
- `/services/` — services overview
- `/services/sap-ams-consulting/` — specific service
- `/services/sap-ai-ml-enablement/` — specific service
- `/ai/` — AI sources
- `/datasets/` — evidence
- `/faq/` — FAQ
- `/cv/` — CV
- `/legal/datasets/` — citation policy

---

## 7. Content placement guide

| Content type | Target location | Avoid |
|---|---|---|
| Durable knowledge (concepts, frameworks, diagnostics) | Atlas page under relevant section (`atlas/<section>/<slug>/`) | News feed, blog post, dataset JSON |
| Dated professional signal (announcement, release, research) | News section (`/news/` when created, or `blog/` for long-form analysis) | Homepage hero, service copy |
| Service offer (consulting, audit, enablement) | Services page or new service detail | Dataset page, Atlas concept page |
| Reusable structured byte (checklist, pattern, metric) | Dataset JSON + collection index | Random markdown page without schema |
| Profile / positioning | `about.md`, `cv/`, `ai/resume.*` | Service copy, news items |
| Social draft source | Materialist OS social drafts (other repo) | Public page unless approved |
| Source / citation policy | `legal/datasets.md`, dataset `meta.attribution` | Main sales copy |

Placement decision tree:

1. Is it evergreen operational knowledge? → Atlas
2. Is it time-sensitive industry signal? → News (when available)
3. Is it a concrete offer with problem/solution/CTA? → Services
4. Is it a structured, citable, reusable byte? → Dataset JSON
5. Is it personal positioning or credentials? → About / CV / AI sources
6. Is it a social media draft? → Materialist OS (do not publish directly)

---

## 8. Agent update rules

For any site addition, follow this exact sequence:

1. **Inspect** the existing site structure and nearest similar page.
2. **Identify** content type: home / service / Atlas / news / dataset / legal / source.
3. **Select** target path and layout pattern from this inventory.
4. **Generate** a small draft or patch. Reuse existing classes and components.
5. **Check** internal links and metadata (title, description, permalink, `last_modified_at`).
6. **Validate** using available commands (see §11). If no command runs, document what was checked manually.
7. **Report** changed files, design pattern used, validation result, and remaining risk.

### Hard rules

- Inspect the nearest similar page first. Copy its front matter and section structure.
- Preserve existing layout style. Do not introduce new colors, typography, or card shapes.
- Avoid random new components. If a new component is needed, create an issue instead of adding it inline.
- Keep additions compact. Short paragraphs, scannable lists, one claim per section.
- Validate links/build if possible. See §11.
- If placement is unclear, create an issue. Do not guess.
- Do not change homepage positioning without reviewing the full site.
- Do not add temporary news to the homepage hero.
- Do not duplicate copy across pages. Link instead.
- Every new page must have: `title`, `description`, `permalink`, `layout: default` (or appropriate layout), and `last_modified_at`.
- Atlas pages should include: source, date checked, confidence, related topic, practical implication.
- News items (when added) must include: title, date, source URL, summary, why it matters, related page/topic, confidence, tags.
- Service pages must include: problem, who it helps, what is delivered, boundaries/non-goals, next step.

---

## 9. Known design risks

| Risk | Manifestation | Prevention |
|---|---|---|
| Homepage overload | Adding every new signal, metric, or paragraph to `/` | Home updates limited to small copy refinement and navigation links for major sections only. |
| Atlas becomes news dump | Dated announcements mixed with evergreen concepts | Strict content placement (§7). Dated items go to news; Atlas gets evergreen updates only. |
| Visual inconsistency | New page looks like a different template | Reuse nearest existing page pattern. Check `DESIGN-SYSTEM.md` and `site-content-design-contract.md`. |
| Copy duplication | Same paragraph on services + Atlas + about | Link across pages. Maintain one canonical location per claim. |
| Service pages without CTA | Service detail ends without next step | Every service page must end with `section-actions` or `section-shell--premium` with contact/profile links. |
| Weak source metadata | Claims without source, date, or confidence | Atlas pages require source metadata. Dataset JSON requires `meta.attribution`. |
| New color/type tokens | Agent invents new visual language | Reuse existing CSS tokens. New tokens require design review. |
| Missing `last_modified_at` | Pages have stale freshness signals | Every new page must include `last_modified_at`. Update it when content changes. |
| Broken internal links | Added pages not linked from anywhere | Check links with `scripts/check_links.py` after build. |
| News section missing | Professional Radar has nowhere to put signals | Issue #3 covers this. Until then, park dated signals in drafts or blog collection. |

---

## 10. Examples

### Example A: Add a new SAP AI news item

**Scenario:** SAP releases a new Joule capability. Professional Radar classifies it as a dated signal.

**Before issue #3 is closed:**
- Create a draft in Materialist OS (other repo) under social drafts.
- If long-form analysis is warranted, add a blog post: `_blog/sap-joule-update-2026.md` with layout `blog`, date, tags, summary.
- Do not add to homepage.

**After issue #3 is closed (news section exists):**
- Add a news entry to the news collection or data file at `/news/`.
- Required: title, date, source URL, summary, why it matters, related Atlas page, confidence, tags.
- Cross-link to relevant Atlas page (e.g., `/atlas/ai-operations/ai-agent-for-sap-support/`).

### Example B: Add an Atlas update about integration reliability

**Scenario:** A new practical pattern for diagnosing IDoc failures is ready.

**Placement:** `atlas/diagnostics/sap-idoc-reliability-patterns.md` (new file) or update existing `atlas/diagnostics/index.md` to link it.

**Structure:**
```yaml
---
layout: default
title: "SAP IDoc Reliability Patterns"
description: "..."
permalink: /atlas/diagnostics/sap-idoc-reliability-patterns/
last_modified_at: 2026-05-26
---

<section class="section note-detail">
  <article class="note-article neub-card">
    <header class="note-header">
      <p class="eyebrow">Diagnostics</p>
      <h1>SAP IDoc Reliability Patterns</h1>
    </header>
    <div class="note-body">
      <!-- content -->
    </div>
  </article>
</section>
```

**Cross-links:** Link from `atlas/diagnostics/index.md` and `atlas/automation/index.md` if relevant.

### Example C: Add a new service page

**Scenario:** A new service offering for SAP MDG governance is ready.

**Placement:** `services/sap-mdg-governance.md`

**Structure:** Reuse `services/sap-ams-consulting.md` pattern:
- `note-detail` wrapper + `neub-card`
- eyebrow "Service"
- h1 title, subtitle
- problem section (h2 + ul)
- deliverables section (h2 + ul)
- related pages paragraph with inline links
- JSON-LD Service structured data
- BreadcrumbList structured data

**Cross-links:** Add link from `services/index.md` grid. Update footer if it becomes a primary service.

### Example D: Add a dataset entry

**Scenario:** A new AMS byte about chat-first triage is ready.

**Placement:** `datasets/ams/ams-052.json` (or next available ID)

**Structure:** Follow `datasets/ams/ams-001.json` schema:
- `id`, `title`, `hook`, `idea`, structured sections
- `meta` block with schema version, source, attribution, license, DOI, canonical URL

**Steps:**
1. Write JSON file.
2. Update `datasets/ams/index.md` to list the new entry (if index is manually maintained).
3. Update `datasets/manifest.json` if required by the dataset build pipeline.
4. Run `scripts/check_links.py` after site build.

---

## 11. Validation

### Available commands

| Command | Purpose | Status |
|---|---|---|
| `scripts/preview_site.sh` | Local Jekyll dev server with LiveReload | Requires Ruby >= 3.0 and Bundler |
| `scripts/preview_site_docker.sh` | Docker-based Jekyll preview | Requires Docker |
| `bin/setup` | Installs Ruby gems via Bundler | Requires Ruby >= 3.0 |
| `scripts/check_links.py <_site>` | Validates local links in built HTML | Requires built `_site` directory |
| `scripts/check_seo.py <_site>` | Checks title, description, canonical, og:url | Requires built `_site` directory |
| `scripts/check_public_repo.py` | Public repo health check | Python script |
| `bundle exec jekyll build` | Build static site to `_site/` | Requires Ruby + gems |
| `bundle exec jekyll serve` | Build + serve | Requires Ruby + gems |

### Commands found and inspected

- `scripts/preview_site.sh` — found, well-documented, handles port conflicts, rbenv support.
- `scripts/check_links.py` — found, validates `href`/`src`/`srcset` against local filesystem.
- `scripts/check_seo.py` — found, checks title, meta description, canonical, og:url for absolute HTTPS and localhost leaks.
- `bin/setup` — found, installs bundler and gems.

### Commands actually run in this session

- **Ruby availability:** `ruby -v` → not available in this environment.
- **Jekyll build:** not run — Ruby missing.
- **Link check:** not run — `_site` not built.
- **SEO check:** not run — `_site` not built.

### Validation gap

This environment lacks Ruby, so Jekyll build and the dependent validation scripts could not be executed. The inventory was constructed via direct file inspection. Recommended: run `bin/setup` and `bundle exec jekyll build` in a Ruby-equipped environment, then run `scripts/check_links.py _site` and `scripts/check_seo.py _site` before merging any site changes.

---

## 12. Framework and tooling summary

- **Generator:** Jekyll 4 (GitHub Pages compatible via `github-pages` gem).
- **Theme:** `minima` (heavily overridden by custom CSS).
- **CSS layers:** `assets/material3.css` → `assets/main.css` → `assets/site.css` (last wins).
- **Plugins:** `jekyll-seo-tag`, `jekyll-sitemap`, `jekyll-feed`.
- **Collections:** `notes`, `blog`.
- **Data:** `_data/home.yml`, `_data/resume.yml`, `_data/social.yml`, `_data/datasets.yml`, etc.
- **Design system reference:** `DESIGN-SYSTEM.md` (tokens, typography, color, spacing, composition rules).
- **Content contract:** `docs/site-content-design-contract.md` (placement, visual, agent workflow rules).
- **Design system source of truth:** `assets/site.css` establishes the live homepage look.

---

## 13. File inventory for agent reference

### Layouts
- `_layouts/default.html` — master layout
- `_layouts/note.html` — article/note layout
- `_layouts/blog.html` — blog post layout

### Includes (sections)
- `_includes/page-builder.html` — section router
- `_includes/sections/hero.html` — home hero
- `_includes/sections/services.html` — services grid (data-driven)
- `_includes/sections/signals.html` — social/callout grid (data-driven)
- `_includes/sections/topics.html` — topic cloud (data-driven)
- `_includes/sections/datasets.html` — editorial dataset block (data-driven; note: `datasets` key missing from `_data/home.yml`)
- `_includes/sections/credibility.html` — trust block
- `_includes/sections/faq.html` — FAQ block
- `_includes/sections/contact.html` — contact block
- `_includes/cta-global.html` — global CTA (currently blank)
- `_includes/header.html` — site header
- `_includes/footer.html` — site footer
- `_includes/head.html` — HTML head
- `_includes/seo/structured-data.html` — JSON-LD structured data
- `_includes/atlas/author-block.html` — Atlas author attribution
- `_includes/atlas/disclaimer.html` — Atlas disclaimer
- `_includes/atlas/status-badge.html` — Atlas status badge
- `_includes/components/social-line.html` — social link line

### Data files
- `_data/home.yml` — homepage copy and structure
- `_data/resume.yml` — canonical resume
- `_data/social.yml` — social profile links
- `_data/datasets.yml` — dataset metadata
- `_data/certifications.yml` — credentials
- `_data/changelog.yml` — changelog entries
- `_data/principles.yml` — principles
- `_data/publications.yml` — publications
- `_data/recommendations.yml` — recommendations
- `_data/profile_audit.yml` — profile audit
- `_data/knowledge_surfaces.yml` — knowledge surfaces
- `_data/discovery_map.yml` — discovery map
- `_data/ams_bytes.yml` — AMS bytes
- `_data/brands.yml` — brand references
- `_data/connect.yml` — connect page data
- `_data/edu.yml` — education data

### Stylesheets
- `assets/site.css` — primary live styles (homepage look)
- `assets/main.css` — base/component styles
- `assets/material3.css` — Material 3 token layer
- `assets/dataset-render.js` — dataset rendering script

### Scripts
- `bin/setup` — dependency installation
- `scripts/preview_site.sh` — local preview
- `scripts/check_links.py` — link validation
- `scripts/check_seo.py` — SEO metadata validation
- `scripts/check_public_repo.py` — repo health
- `scripts/generate_dama_pages.js` — DAMA page generation
- `scripts/generate_entity_blog.py` — blog generation
- `scripts/build_static_sitemap.py` — sitemap generation
- `scripts/enrich_datasets.py` — dataset enrichment
- `scripts/generate_dataset_pages.py` — dataset page generation

---

## 14. Closeout cross-reference

This inventory was created for:
- **Repository:** `dkharlanau/dkharlanau.github.io`
- **Issue:** #6 — Create site structure and component inventory for agent updates
- **Next recommended issue:** #2 — Add structured topic index for public knowledge pages
- **Blocking dependency:** Ruby environment required for full build validation.
