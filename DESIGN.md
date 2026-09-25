# Design direction

Technical SEO, structured data, indexing, and discovery rules live in [`docs/SEO_TECHNICAL_CONTRACT.md`](docs/SEO_TECHNICAL_CONTRACT.md). The operative visual contract — tokens, typography, spacing, components, templates — lives in [`docs/editorial-design-system.md`](docs/editorial-design-system.md). This file holds the product-level direction that sits above both.

## Purpose

The site is the public professional space of Dzmitryi Kharlanau: a Senior SAP Consultant at EPAM Systems. It should make complex SAP operating situations easier to understand, discuss, and act on.

The site is not a generic knowledge directory and not a lead-generation landing page. It combines three roles in a clear order:

1. Explain the kind of SAP operational problem that can be worked through.
2. Show a small amount of public, reviewed evidence and methods.
3. Give the visitor a calm next step: services, profile, knowledge, or LinkedIn.

## Positioning and voice

- Use: `Senior SAP Consultant at EPAM Systems` where current professional context matters.
- Use: `SAP operations · transformation · practical AI` as the compact descriptor.
- Do not position the site as `independent consulting`.
- Do not imply EPAM endorsement of the personal site or its materials.
- Write in direct, practical language: symptom, evidence, process, decision, operating outcome.
- Avoid generic claims such as “unlock potential”, “future-ready”, “world-class”, or “transform at scale”.

## Visual language

The active system is **editorial**: white background, dark text, one cobalt accent (`#1254f5`), Inter for text with Source Serif 4 for leads and display headings, hairline rules instead of boxes, and restrained 4/8/12px radii. Oversized display type, glossy 3D diagrams, large rounded panels, decorative gradients, tinted paper backgrounds, uppercase micro-labels, and dashboard metrics are retired patterns.

Read [`docs/editorial-design-system.md`](docs/editorial-design-system.md) before changing any visual code. It defines the tokens, page templates, component rules, and the rejected-patterns list.

Non-negotiables:

- Body text 17px mobile / 19px desktop, line-height 1.7, reading measure about 68ch.
- No fake metrics, score rings, readiness percentages, or gamified progress. Browser-local learning state must be explicitly user-chosen and labeled as browser-local.
- Cards only for genuine collections. Ordinary content uses headings, paragraphs, lists, tables, and hairlines.
- One accent color. Semantic green/amber/red only for callouts and real status.
- Every remaining image must explain something: architecture, process, model, or a real screenshot. No decorative hero illustrations.

## Navigation and homepage

- Primary navigation stays product-level and short (EN: Learn, Library, About, Search; locale variants keep their labels). Labs, frameworks, career material, and machine-readable work are reached from hubs, not from every screen.
- Page-to-page HTTP(S) links open in a new browser tab by default. Same-page anchors, downloads, and non-navigation protocols keep native behavior; use `data-open-same-tab="true"` only for a deliberate component exception.
- The homepage answers within seconds: what this is, who it is for, what to do next. Two entry routes (learn / AMS improvement), search, and a start-from-a-topic list. No competing cards, no metric strips.

## Content states and trust

- A reviewed-content badge has one consistent meaning across Atlas, scenarios, and research (see `docs/ai/CONTENT_VERIFICATION_POLICY.md`).
- Draft and noindex status stays explicit; do not let unverified material present as reviewed.
- Search is a utility route with a persistent label, 16px input text, and clear empty-state guidance.
- No client names, ticket numbers, or proprietary details anywhere.

## Accessibility and responsive

- One H1 per page, semantic heading order, landmarks (`header`/`main`/`footer`), visible `:focus-visible` outlines, 44px touch targets where practical.
- Contrast: 4.5:1 for normal text, 3:1 for large text. Never put body copy on a saturated background.
- Test at 320/375/430/768/1024/1280/1440 and at 73%/100%/200% zoom. No horizontal overflow except intentional table/code scroll.
- Honour `prefers-reduced-motion`. No meaning may depend on animation.
- Print matters: learning content is printed and exported to PDF. The print stylesheet in `assets/css/base.css` hides chrome and expands external reference URLs.

## Performance and operations

- GitHub Pages native build: no unsupported plugins, no SPA frameworks, minimal vanilla JS.
- Load only the weights and icons needed; explicit image dimensions to prevent layout shift.
- The homepage and articles must remain readable if JavaScript or external fonts fail.
- Run the full validation sequence in `AGENTS.md` before publishing; a green Jekyll build is necessary but not sufficient for visual changes — check the rendered page at desktop and mobile widths.
- Keep generated `_site/` out of version control.

## Rejected patterns

Pale low-contrast footer text; saturated panels behind body copy; mega-footers; search-as-hero; uncontrolled card grids; uppercase mono eyebrows; tinted paper canvases; lime or multicolor accents; decorative generated illustrations on ordinary articles; metric tiles and progress dashboards without persistent user identity; viewport-height heroes that push content below the fold.
