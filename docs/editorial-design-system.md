# Editorial Design System

The site's visual language: a calm editorial reading experience for long
technical material. White background, dark text, one blue accent, generous
whitespace, and typography that carries hierarchy instead of boxes.

This document is the contract for future site work. If you change the system,
change this document in the same commit.

## Principles

1. **Content first.** Every component must help the reader understand,
   navigate, compare, decide, or remember. If it does not, remove it.
2. **Typography is the hierarchy.** Headings, spacing, and rules structure the
   page. Borders and backgrounds are the exception, not the tool.
3. **Fewer boxes.** Do not put ordinary content in cards, panels, or bordered
   sections. Collections of comparable items may use a card; linear content
   uses hairlines and whitespace.
4. **One accent.** Cobalt blue marks links, active navigation, primary
   actions, and the category label. Semantic colors (green, amber, red) appear
   only in callouts and genuine status. Never as decoration.
5. **Honest UI.** No fake metrics, no gamification, no dashboard theater.
   Browser-local state is labeled as such.

## Files

| Layer | File | Owns |
|---|---|---|
| Tokens | `assets/css/tokens.css` | All custom properties |
| Base | `assets/css/base.css` | Reset, typography, links, focus, quotes, media, print, reduced motion |
| Layout | `assets/css/layout.css` | Containers, header, nav, footer, breadcrumbs, article shell, TOC, page furniture |
| Components | `assets/css/components.css` | Buttons, tables, code, callouts, cards, disclosures, forms, utilities, atlas process maps |
| Focus pages | `assets/site-focus.css` | Homepage, `/learn/`, service landing pattern (`focus-page`) |
| Hubs / labs | `assets/research-canvas.css` | Research-canvas pattern: hubs, labs, enterprise-context, interview-readiness |
| Services | `assets/services-canvas.css` | Services index and service-canvas pages |

Legacy files (`main.css`, `site.css`, `product-system.css`,
`diagnostic-portal.css`, `internal-page-polish.css`, and route canvases) are
compatibility layers kept small deliberately. They load **before** the
editorial system and must not re-introduce overrides for domains the editorial
system owns (header, article chrome, typography, buttons, tables).

## Tokens

### Color

| Token | Value | Use |
|---|---|---|
| `--color-bg` | `#ffffff` | Page background |
| `--color-text` | `#1f242c` | Primary text, headings |
| `--color-text-muted` | `#57606e` | Secondary text |
| `--color-text-faint` | `#868e9a` | Metadata, placeholders |
| `--color-border` | `#e3e6ea` | Hairlines, table rules, input borders |
| `--color-surface` | `#f7f8fa` | Code blocks, quiet fills |
| `--color-accent` | `#1254f5` | Links, active nav, primary actions, category label |
| `--color-accent-hover` | `#0d3fd0` | Hover/focus accent |
| `--color-accent-soft` | `#eef3fe` | Selected/hover fills |
| `--color-success` / `--color-warning` / `--color-danger` | `#1d7a4c` / `#8f6106` / `#b3261e` | Callouts only |

No gradients. No tinted page sections. No large colored panels.

### Type

| Token | Size | Use |
|---|---|---|
| `--text-xs` | 13px | Legal, fine print |
| `--text-sm` | 14px | Metadata, breadcrumbs, captions, TOC |
| `--text-md` | 16px | Supporting UI text |
| `--text-base` | 17px | Body, mobile |
| `--text-lg` | 19px | Body, desktop (≥768px) |
| `--text-xl` | 22px | H4 |
| `--text-2xl` | 26px | H3 |
| `--text-3xl` | 34px | H2 |
| `--text-4xl` | 44px | H1 |

Body line-height 1.7. Sans: Inter with system fallbacks. Serif (Source Serif
4) is reserved for article leads (`.note-subtitle`, `.lead`), blockquotes,
and canvas H1s. Mono for code.

Article reading measure: `max-width: 68ch` inside `--container-content`
(720px). Deep technical heroes may use `--container-wide` for the headline while
keeping explanatory copy and the article body on the narrower reading measure.

### Spacing

`--space-1` … `--space-10` = 4, 8, 12, 16, 24, 32, 48, 64, 96, 128px.
Section separation is `--space-7`/`--space-8`; page top/bottom
`--space-7`/`--space-9`.

### Radius

`--radius-sm` 4px, `--radius-md` 8px, `--radius-lg` 12px. Pills (999px) only
for real tags and status. Compact section labels use `--radius-md` rather than pill geometry.

### Containers

`--container-content` 720px (articles), `--container-medium` 920px (hubs,
landing pages), `--container-wide` 1200px (wide technical pages, tables,
diagrams).

## Components

- **Buttons**: `.btn--primary` (accent fill, white text), `.btn--secondary`
  (neutral border), text links otherwise. 44px minimum hit target.
- **Tables**: full width, 2px top/bottom rules, hairline row separators,
  strong header. Give cells real breathing room: use about 16px vertical and
  20–24px horizontal padding for normal tables. On mobile the table box scrolls
  horizontally; text never shrinks below readable size.
- **Study table**: use the named `.table-scroll.study-table` wrapper with a
  `.study-table__table` table for educational comparisons, reference matrices,
  assessment material, and compact object/field catalogues. It is the default
  reusable table pattern for new study content: 17px body text, 14px headers,
  relaxed cell padding, a quiet accent header, light row separation, and
  horizontal scrolling on small screens. Reuse this component before adding
  route-local table CSS.
- **Code**: `pre` on `--color-surface`, 1px border, 8px radius, horizontal
  scroll. Inline code with a subtle border.
- **Callouts**: `.callout--note` (accent), `.callout--important` (amber),
  `.callout--warning` (red). Left rule + quiet fill; nothing brighter.
- **Cards**: `.card` only for genuine collections (pathways, offers, related
  topics). Most pages should show almost no card chrome.
- **Structured technical rows**: `.ecg-determination-detail` uses one divider per
  record, a narrow number/meta rail, and a compact title/context stack. Detail
  groups align under the title and use vertical separators rather than repeated
  horizontal rules. Do not repeat the same question in the header and body.
  Keep body text in normal sentence case and at a readable size.
- **Enterprise Context diagrams**: dependency rails and similar inline schemes need a small separation from the prose that follows. Keep about 16px of bottom space so the diagram reads as one visual unit instead of running directly into the next paragraph.
- **Enterprise Context comparison groups**: paragraph-heavy concepts must not be
  compressed into three or more narrow reading columns. `.ecg-decision-columns`
  wraps responsively, keeps body text at normal reading size, and removes legacy
  left indentation when there is no real number rail. Three columns are only
  acceptable when each block is short; long explanations should resolve to two
  or one column. The sentence after a comparison group may be shown as a quiet
  memory rule when it summarizes the distinction.
- **Atlas process maps**: `.atlas-process-map` renders a semantic ordered
  list of process steps as a five-tile grid (one column on mobile) with
  numbered step tiles, arrow connectors, and a caption. Used on Atlas
  process/evidence maps.
- **Breadcrumbs**: 14px, normal casing, `/` separators, muted with a darker
  current page. Never uppercase micro-labels.
- **TOC**: `reader-tools.js` injects `.reader-toc` from H2s (min 3, max 12).
  Desktop ≥1400px: sticky rail in the page margin. Mobile: disclosure.
- **Eyebrows**: 14px, semibold, accent color, normal casing. Hero and page-category
  eyebrows stay as plain accent text. In research-canvas section headers, an eyebrow may use
  a compact `--color-accent-soft` plaque with `--radius-md`; keep it small and let the heading
  remain the primary signal. Keep the section heading and its supporting paragraph together
  as one readable block rather than splitting them into narrow columns.

## Page templates

- **Article** (`blog`/`note` layouts, atlas pages): breadcrumb → category →
  H1 → serif lead → quiet meta (date, reading time, verification status) →
  body at reading measure → TOC → related/further reading → prev/next.
- **Hub / landing** (`research-canvas`, `focus-page`): H1 → lead → primary
  action → numbered route lists with hairlines → method sequence → boundary
  note. No KPI tiles, no card grids of ordinary text.
- **Wide technical** (enterprise-context graphs): `--container-wide` is allowed
  for diagrams, wide tables, and the hero headline. The headline should use the
  available width instead of being constrained to a narrow text column; the
  supporting lead and evidence rail can share the row below. Do not hard-code
  line breaks in technical hero titles: a title that fits should stay on one
  line, while longer titles wrap naturally. Body sections keep the normal
  editorial measure.
- **Home**: headline, short explanation, two entry routes, search,
  start-from-a-topic list. Nothing else competes for the first viewport.

## Responsive and accessibility rules

- Mobile first; test at 320, 375, 430, 768, 1024, 1280, 1440.
- No horizontal overflow except intentional table/code scroll.
- Visible `:focus-visible` outline (2px accent) on all interactive elements.
- Touch targets ≥44px where practical.
- `prefers-reduced-motion` disables smooth scroll and transitions.
- Print: chrome hidden, black text, external link URLs shown, code/quotes/
  tables avoid page breaks.

## What is deliberately gone

Score rings, readiness percentages, metric cards, calibration gaps, tile
strips with arrows, lime/cyan accents, uppercase mono eyebrows, tinted paper
backgrounds, decorative hero illustrations, route-list card borders, and
viewport-height heroes. Do not reintroduce them.
