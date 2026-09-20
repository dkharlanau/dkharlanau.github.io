# Editorial design system

This document is the implementation contract for the public reading and product surfaces of dkharlanau.github.io.

## Audit summary

The site grew through several specialised surfaces: Atlas, Labs, services, research, learning, datasets and product experiments. The content is useful, but the accumulated route-specific CSS created four recurring problems:

1. reading scale and headline size varied too much between page types;
2. card, border, radius and spacing decisions were repeated with different values;
3. specialist routes could visually override the shared reading experience;
4. diagrams and decorative visuals did not always have a consistent editorial role.

The redesign keeps the existing content architecture and publication controls. It adds a final shared editorial layer instead of replacing every mature route implementation.

## Core principles

- Reading first. A long article should remain comfortable for 10–20 minutes.
- Quiet hierarchy. Headings identify structure; they do not behave like campaign billboards.
- One visual grammar. Blue marks routes, actions and evidence. Red marks tension, risk, contrast or a diagnostic boundary.
- Progressive disclosure. Index pages show paths first and detail second.
- Fewer wrappers. Prefer typography, spacing and hairline rules over more cards and badges.
- Existing URLs, Atlas verification state, robots rules, sitemap rules and machine-readable publication contracts remain authoritative.

## Tokens

The final shared layer lives in `assets/editorial-system.css`.

| Role | Token | Current value |
| --- | --- | --- |
| page | `--ed-paper` | `#fbfaf7` |
| surface | `--ed-surface` | `#ffffff` |
| primary ink | `--ed-ink` | `#18212d` |
| reading copy | `--ed-copy` | `#3c4754` |
| muted metadata | `--ed-muted` | `#66717d` |
| hairline | `--ed-line` | `#d9dee3` |
| action/evidence | `--ed-blue` | `#1858b8` |
| tension/risk | `--ed-red` | `#c63540` |
| reading measure | `--ed-measure` | `44rem` |
| wide layout | `--ed-wide` | `76rem` |

Typography uses Inter/system sans for navigation and structure and Source Serif 4/serif fallbacks for long-form reading. Body copy targets roughly 18–20px on desktop with a line-height around 1.7. Article measure remains roughly 680–760px.

## Page-type contract

### Homepage
Two primary jobs are visible early: Learn / prepare and Improve SAP / AMS. Keep selected evidence and expert context below those paths. Do not add a large catalogue above the fold.

### Atlas and diagnostic pages
Keep status and verification semantics explicit. Use one narrow reading column, compact metadata, useful tables, evidence-first diagrams and related diagnostics. Never promote verification or indexing through design changes.

### Long-form guides
Use serif reading text, restrained sans headings, a 44rem measure, strong paragraph rhythm, horizontally scrollable tables, quiet code blocks, useful captions and no decorative sticky furniture.

### Learning / interview / assessment
Use reading content first, then recall/practice blocks. Practice controls must remain native semantic `details` elements and work without JavaScript.

### Services
Lead with the operating problem, then show a small number of evidence-led service routes. Red/blue accents clarify problem vs route; they are not decorative branding stripes.

### Category / collection / archive
Prefer simple route lists or editorial grids. Avoid turning every item into a heavy card.

### Search / discovery
Search is an action surface. Keep form, result title, short explanation and route context visually clear. Avoid competing side panels.

## Components

Prefer a small reusable set:

- ArticleHeader / metadata
- ReadingContent
- Figure + caption
- Breadcrumbs
- DiagnosticSummary / decision table
- Callout
- ComparisonBlock
- RelatedContent
- CollectionList
- ExpertContext

Do not create a component solely to add a border, badge or wrapper.

## Responsive and accessibility rules

- Reflow multi-column canvases before the reading column becomes cramped.
- Keep interactive controls at practical touch sizes.
- Tables scroll within their own container; the document must not overflow horizontally.
- Preserve semantic headings, native disclosure controls and keyboard focus.
- Respect `prefers-reduced-motion`.
- Visual smoke tests must only treat painted/reachable controls as visible; descendants of a closed `details` element are not interactive until opened.

## Performance and publication safety

- The editorial layer is plain CSS; no styling framework is introduced.
- Images declare dimensions to avoid layout shift.
- Non-critical article visuals use lazy loading and async decoding.
- Existing canonical, robots, sitemap, structured-data and Atlas artifact generators remain unchanged unless a specific publication task requires it.
- Unverified/noindex material must stay unverified/noindex after visual work.
