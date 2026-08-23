# Design direction

Technical SEO, structured data, indexing, and discovery rules live in [`docs/SEO_TECHNICAL_CONTRACT.md`](docs/SEO_TECHNICAL_CONTRACT.md).

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

### Core idea

The visual metaphor is a diagnostic signal: a diffuse operating situation becomes a focused line of evidence and a visible decision point.

- Light blue dispersion is the atmospheric background, never the primary source of text contrast.
- The signal beam, concentric rings, and crosshair represent focus and decision making.
- Animation is functional and quiet: one moving/pulsing signal point is enough. Respect `prefers-reduced-motion`.

### Palette

| Token | Value | Use |
| --- | --- | --- |
| Portal blue | `#1019c8` | Headings, primary navigation, links, signal paths |
| Deep ink | `#101756` | High-contrast text |
| Paper | `#f8fbff` | Reading surfaces and cards |
| Canvas | `#eef4ff` | Page background |
| Border | `#c7d7fb` | Rules and dividers |
| Lime | `#c6ff00` | One primary action per view |
| Muted text | `#59648b` | Supporting text only |

### Readability rules

- Never put muted blue-grey body copy on a saturated blue panel.
- Body text must remain readable at browser zoom 73% and 100%.
- Footer text uses deep ink or a deliberate darker muted tone; no low-opacity legal text.
- Do not use large empty panels simply to create visual drama.
- Every full-width coloured panel needs a clear purpose and a contrast check.

### Type and rhythm

- Large display headings are for a single clear claim, not for every section.
- Use a readable 16–18px body size with generous line-height.
- A section needs one message, one hierarchy, and one primary action at most.
- Use rules, numbering, and measured whitespace before adding card shadows or decorative UI.

### Spacing and corner system

Spacing follows an 8px base and scales by component role. The goal is not to put every line in a card; it is to give every meaningful surface enough room to read and to make related elements feel intentionally grouped.

| Token / role | Value | Use |
| --- | --- | --- |
| `--portal-space-1` | `8px` | Icon-to-label gap and compact metadata rhythm |
| `--portal-space-2` | `12px` | Compact control groups |
| `--portal-space-3` | `16px` | Mobile card inset and related text spacing |
| `--portal-space-4` | `24px` | Standard mobile surface padding and card gaps |
| `--portal-space-5` | `32px` | Compact desktop section spacing |
| `--portal-space-6` | `48px` | Large section separation |
| `--portal-page-gutter` | `clamp(16px, 3vw, 40px)` | Safe distance from the viewport edge |
| `--portal-page-gutters` | `clamp(32px, 6vw, 80px)` | Combined left and right gutter for bounded surfaces |
| `--portal-section-gap` | `clamp(24px, 3.5vw, 48px)` | Vertical distance between distinct surfaces |
| `--portal-surface-padding` | `clamp(24px, 4vw, 56px)` | Hero and large section inset |
| `--portal-surface-padding-compact` | `clamp(18px, 2.4vw, 32px)` | FAQ, share, footer, and utility surfaces |

Corner radius communicates hierarchy:

| Token / role | Value | Use |
| --- | --- | --- |
| `--portal-radius-control` | `14px` | Buttons, inputs, selects, language and share controls |
| `--portal-radius-card` | `20px` | Route lists, figures, search form, and compact panels |
| `--portal-radius-surface` | `28px` | Sections, FAQ, share and footer containers |
| `--portal-radius-hero` | `34px` | Primary route hero only |

- Content never starts flush against a coloured or bordered surface; large surfaces use `--portal-surface-padding`.
- Adjacent surfaces use `--portal-section-gap`; do not create spacing with empty min-height panels.
- Mobile surfaces keep at least 16px viewport gutter and 24px internal padding.
- A grouped route list has one rounded outer boundary. Its internal rows stay linear and use dividers; do not round every row.
- Tables, code blocks, timelines, and relationship lines may stay rectilinear inside a rounded containing surface.
- Shadows are optional and quiet. Spacing, border contrast, and radius must carry the hierarchy first.

## Text, contrast, and interactive sizing

### Text roles

| Role | Desktop size | Mobile size | Colour | Rule |
| --- | --- | --- | --- | --- |
| Display heading | 52–104px | 43–62px | Portal blue | One message per view; use `clamp()`, never a fixed oversized value. |
| Section heading | 42–76px | 38–52px | Portal blue | Keep to two or three lines at the intended viewport. |
| Card / step title | 20–32px | 19–26px | Portal blue | Never rely on colour alone to show hierarchy. |
| Lead paragraph | 17–21px | 16–18px | Deep ink | Maximum comfortable measure: about 60–70 characters. |
| Body text | 16–18px | 16px minimum | Deep ink or dark muted | Minimum line-height 1.5. |
| Supporting text | 13–14px | 13px minimum | `#44537d` or darker on pale backgrounds | Do not reduce contrast to make it feel secondary. |
| Metadata / eyebrow | 11–12px | 11px minimum | Portal blue or dark muted | Use uppercase only for short labels. |
| Legal footer text | 12px minimum | 12px minimum | `#44537d` or darker | Never use opacity below 1 on a pale footer surface. |

### Contrast rules

- Normal text must target at least **4.5:1** contrast against its immediate background.
- Large text (24px regular or 18.66px bold and above) must target at least **3:1**.
- Text below 16px is never used in a low-contrast colour for visual decoration.
- Muted text is for supporting copy only and must remain dark enough to read at 73% browser zoom.
- Do not apply `opacity` to text containers: it reduces link, label, and legal-text contrast together.
- Do not put dark blue body copy on saturated blue. Use a white/paper surface or white text with a verified contrast ratio.
- Footer rule: brand descriptor, copyright, and legal links must use `#44537d` or a darker colour on the pale blue canvas; the old pale-grey footer text is a rejected pattern.

### Buttons and controls

| Control | Minimum dimensions | Padding | Type | Rule |
| --- | --- | --- | --- | --- |
| Primary CTA | 56px high; 44×44px hit area minimum | 0 24–28px | 14–16px, semibold | Lime fill, portal-blue text, one per visual group. |
| Secondary text CTA | 44px hit area minimum | 8px vertical | 13–15px, semibold | No filled background; underline or clear hover/focus state. |
| Icon-only control | 44×44px | centred | 20–24px icon | Required accessible name and visible focus ring. |
| Header navigation item | 44px high | 10–14px horizontal | 13–15px, semibold | Never rely on a tiny text link as the only hit target. |
| Search / text input | 56px high | 14–18px horizontal | 16px minimum | A visible label is required; placeholder is not the label. |
| Language control | 44px high | 10–14px horizontal | 13–15px | Maintain border contrast in default and hover states. |

### Interaction states

- **Default:** clear label, normal contrast, no hidden affordance.
- **Hover:** small surface or underline change; avoid movement greater than 3px.
- **Focus-visible:** a clearly visible 2px outline with enough contrast against the page and the component.
- **Active:** preserve label contrast and avoid a colour shift that looks disabled.
- **Disabled:** only for controls that genuinely cannot be used; explain why when a form is involved.
- **External link:** use `↗` or an accessible text label, consistently.

### Text quality checklist

Before accepting a screen, check:

1. Could a visitor understand the purpose without reading every word?
2. Is every grey or muted line readable at 100% and 73% zoom?
3. Is any instruction duplicated by placeholder text, helper text, or a second CTA?
4. Does every button begin with a clear action verb?
5. Is the smallest text at least 11px for metadata and 12px for legal/footer text?
6. Can every interactive target be tapped reliably on mobile without zooming?
7. Are hover and focus states visible without relying only on colour?

## Homepage

### Primary narrative

`Visible TCO → reusable workflow → controlled AI → prevention-led AMS`

The homepage positions the site around a next-generation SAP AMS operating model. The first screen names the model; the second explains its three structural changes; bounded pilot paths appear before the broader evidence, research, and machine system.

### Recommended sections

1. **Hero** — `Building the next generation of SAP AMS`, visible TCO, reusable workflows, controlled AI, and direct routes to the AMS model and pilot paths. Employment context stays in the lower profile close, not in the product claim.
2. **AMS operating model** — three structural changes: TCO before ticket volume; workflow before handover; AI with an authority boundary.
3. **Pilot paths** — three bounded starts: repeat-incident prevention, AI-assisted support workflow, and governed data recovery. The supporting Atlas, research, and machine layers follow them.
4. **From pilot to operating model** — Baseline the TCO; Prove one workflow; Scale what holds, supported by a real process visual.
5. **Public working evidence** — three reviewed diagnostics. This supports trust; it must not become an unbounded catalogue.
6. **Profile close** — portrait, current EPAM context, and a clear invitation to view services or discuss on LinkedIn.

### Do not put on the homepage

- A raw search textarea as the principal conversion mechanism.
- Unbounded lists of every Atlas page, Lab, dataset, or tool. Three pilots plus three supporting layers are the maximum top-level depth shown directly on home.
- An interview-preparation promo strip.
- Repeated profile cards or a large “about me” block.
- A mega-footer with product navigation columns.

## Navigation

Primary navigation is product-level and short. It is rendered as a solid floating capsule so text and controls never lose contrast over page imagery:

- Work
- Knowledge
- About
- Search
- Language

The language control is visible on every route. On mobile it remains outside the collapsed navigation so the locale can be changed without opening the menu.

Labs, frameworks, career material, and machine-readable work remain reachable from the relevant hubs, not from every screen.

## Cluster and hub design

### Work / Services

Purpose: explain engagements and the next discussion. Lead with operating situations and outcomes, not a generic service card grid.

### Knowledge

Purpose: curated, human-readable material. Give visitors a small number of routes and make review status visible. The hero visual shows one question branching into knowledge routes with different maturity.

### Atlas and scenarios

Purpose: diagnostic depth. Prioritise symptom, business context, SAP touchpoints, evidence, and the next diagnostic step.

### Labs and frameworks

Purpose: active methods and practical tools. They are secondary to the consulting narrative and must not compete with the homepage CTA. Labs use a converging process/architecture/judgment field; Frameworks use distinct reusable instruments on one evidence spine.

### Machine layer

Purpose: structured exports and agent tools. Keep it a clear specialist route, not a prominent footer category. Its visual must show the transformation from public human knowledge into controlled machine-facing layers, not a generic server or circuit-board metaphor.

### Research

Purpose: working, source-backed evidence for changing claims. The visual model is many weak signals entering comparison and only a few stronger decision lines leaving it. Draft and noindex status stays explicit.

### Product-hub composition

- Every major hub has one relevant raster system visual with meaningful alternative text and a short explanatory caption.
- The image is a semantic model of the section, not decoration behind body text.
- The first screen pairs one claim with one model; inventory and status follow in the same reading sequence.
- Hub routes use a two-column editorial map on desktop and one continuous list on mobile.
- Status/boundary information uses a solid high-contrast band; it never relies on low-opacity text.
- Generated visuals share pale-blue dispersion, cobalt linework, white spectral light, and restrained lime checkpoints, but their underlying geometry must differ by product meaning.

### System illustration semantics

Every system illustration must answer four questions without relying on baked-in labels: where the operating signal starts, what changes or branches, where control or ownership is applied, and what outcome leaves the system. A pale-blue field alone is not a meaningful asset.

| Domain | Required operating story | Canonical asset |
| --- | --- | --- |
| ERP | Demand or business signal → document and availability checks → cross-module/warehouse execution → delivery outcome. | `assets/img/systems/erp-document-flow-field.webp` |
| Data | Imperfect source records → identity, validation, lineage and ownership gates → governed record → trusted reuse. | `assets/img/systems/master-data-lineage-field.webp` |
| Workflow | Main operating route → visible exception → evidence and review loop → decision gate → controlled re-entry. | `assets/img/systems/workflow-exception-field.webp` |
| AI | Heterogeneous evidence → bounded retrieval/synthesis → uncertainty separation and review → approved action + audit trail. | `assets/img/systems/ai-evidence-boundary-field.webp` |
| Logistics | Demand and allocation → warehouse pick/pack/stage → transport handoff → delivery confirmation + feedback. | `assets/img/systems/logistics-fulfilment-field.webp` |

- Map the asset to the page's actual operating model; do not use one generic “technology” scene across unrelated routes.
- Preserve source, control point, and outcome inside the central crop on desktop and mobile.
- Captions name the operational chain; alternative text describes the same visible model in plain language.
- Do not use generic neural-network constellations, random orbs, decorative circuit boards, dashboards, or unlicensed brand marks.
- One small lime checkpoint may signal approval or completion. The rest of the scene stays within the powder-blue, white, cobalt, ultramarine, and cool neutral palette.

### Long-form reading composition

- Service and Atlas detail pages use a split opening: editorial title and explanation on one side, a real captioned system visual on the other. Text never sits over the image.
- The visual must explain the page's operating model. AMS uses the workflow exception-and-review loop; data uses source-to-governed-record lineage; integration uses the ERP document flow; AI uses the evidence, review, action, and audit boundary; logistics uses the order-to-delivery route.
- The opening becomes one continuous column below 760px. The image follows the title and explanation, keeps its caption, and must not create horizontal page overflow.
- Long-form body copy remains on a solid reading surface with a 68ch maximum measure, 17.5–19px body type, generous line-height, numbered H2 sections, and a sticky desktop table of contents.
- Atlas source, date, confidence, and practical-implication notes belong in a collapsed `Evidence and source note` inside the evidence rail. They must not appear as a loose paragraph above breadcrumbs.
- Research and Lab boundary components must support any number of paragraphs. Use a stable `icon + sequential content` grid; never rely on auto-placement into a fixed three-column pattern.

## Footer

The footer is a compact trust and exit point, not a sitemap.

- Identity: a real circular portrait + `Dzmitryi Kharlanau` + `SAP operations · transformation · practical AI`.
- Site links: Services, Profile, Knowledge.
- Social profiles: LinkedIn and GitHub use a separate, visibly interactive group sourced from `_data/identity.yml`.
- Legal: Privacy and Accessibility.
- Keep all text high contrast and readable.
- Avoid the words “independent consulting”.
- The portrait is 56×56px on desktop and remains at least 48×48px on mobile; it uses a stable crop and explicit dimensions.
- Social links have visible labels, an external-link indicator, keyboard focus, and a minimum 44px hit height.

## Component inventory and acceptance criteria

| Element | Job | Content rule | Interaction / responsive rule | Acceptance check |
| --- | --- | --- | --- | --- |
| Surface container | Group one coherent message or task without turning every row into a card. | One hero, section, utility group, or route list per surface. | 34px hero radius, 28px section radius, 20px card radius; padding drops from 24–56px to 24px on mobile. | Content never touches the edge, adjacent surfaces keep a visible gap, internal dividers align, and no horizontal overflow appears at 390px. |
| Brand mark | Identify the site without a wordmark in the header. | Signal beam, rings, and crosshair; no letter monogram. | Crisp at 30px; has a text alternative through the parent home link. | Mark is recognisable on light canvas and has no blurred edges. |
| Header | Give quick access to the site’s three main areas. | Work, Knowledge, About, Search, Language. | Sticky at desktop; collapses into an explicit menu on mobile. | All controls are visible, keyboard reachable, and do not overlap at 320px. |
| Hero | Position the next-generation SAP AMS model in one glance. | One AMS claim and visible TCO/workflow/AI language; no employment or disclaimer line. | Two columns on desktop; single column on mobile. | No line exceeds the intended reading width; heading does not clip or become larger than the viewport. |
| Signal trace | Make the AMS operating model tangible. | TCO, Workflow, AI control, each with one short operational statement. | One quiet animated point only; no motion with reduced-motion preference. | It remains secondary to the claim and readable without the animation. |
| Primary CTA | Move visitors to the concrete AMS offer. | `Explore the AMS model`. | Large hit target; lime is reserved for this action. | Links to `/services/sap-ams-consulting/`, has visible focus, and is readable without hover. |
| Secondary CTA | Let visitors jump directly to bounded starting points. | `See the pilot paths`. | Text link with a 44px hit height, not a second filled button. | Links to `#pilots`, moves to the pilot heading, and does not visually outweigh the primary CTA. |
| Focus cards | Explain the three structural changes in the AMS model. | TCO before ticket volume; workflow before handover; AI with an authority boundary. | One vertical operating sequence beside the semantic workflow visual. | Each full card links to a relevant existing service route; card text is not smaller than 13px. |
| Cluster map | Put bounded pilots before the supporting system without creating a mega-menu. | Exactly three pilot paths followed by Atlas evidence, research, and machine layers. | Asymmetric editorial grid on desktop; one image-led card per row on mobile. | Every card uses a relevant system asset, keeps text contrast over the image, and links to a stable route. |
| Product-hub visual | Explain the section model before the route inventory. | One distinct model for Knowledge, Labs, Frameworks, Research, or Machine. | Half-width desktop figure; full-width mobile figure before the status summary. | Real raster asset, useful alt text, stable crop, no text baked into the image, and no generic UI/dashboard imagery. |
| Reader opening | Give a long technical page a visual orientation point without turning it into a landing-page poster. | One title, one explanatory sentence, one semantic visual and caption. | Split desktop; continuous title → explanation → visual sequence on mobile. | No text over images, no broken crop, no horizontal overflow, and title/visual heights remain visually balanced. |
| Atlas evidence rail | Keep status, scope, source note and TOC available without interrupting the article. | Process, SAP area, indexing state, collapsed evidence note, then page sections. | Sticky on wide screens; moves before the body on mobile. | No source metadata above breadcrumbs; disclosure remains keyboard accessible; body text never collapses below a readable width. |
| Lab visual hero | Show the model and current inventory as separate evidence layers. | Claim and CTA, semantic figure, then catalogue/readiness strip. | Two-column first row and full-width status row; single-column mobile. | Image has explicit dimensions and alt text; status cells have 44px+ actions where interactive; variable catalogue counts do not break the grid. |
| Hub route map | Turn a long catalogue into a scannable path. | Stable route label, practical description, and one consistent icon. | Two columns desktop; one column below 800px. | Titles and descriptions remain readable, every card is a full link, and no horizontal overflow appears at 390px. |
| Method panel | Explain how the work is done. | Frame, Trace, Make the next move. | White surface with blue text; three columns desktop, one column mobile. | No dark-on-blue body copy; each step works as a standalone paragraph. |
| Evidence list | Prove the approach through selected reviewed material. | Maximum three reviewed resources on home. | Row links become stacked on mobile. | Status is visible, titles do not wrap into unreadable fragments, and all routes resolve. |
| Close / CTA | Give a calm end to the page. | One invitation and two paths: Services and LinkedIn. | Centered on desktop; stacked on mobile. | Does not repeat the hero claim verbatim. |
| Footer | Provide compact identity, trusted public profiles, exit routes, and legal links. | Portrait, name, descriptor, Services, Profile, Knowledge, LinkedIn, GitHub, Privacy, Accessibility. | Identity and social profiles share the first row on desktop and stack on mobile; social actions stay at least 44px high; no sitemap grid. | Portrait crop is clear, profile URLs come from `_data/identity.yml`, controls wrap without overflow, and descriptor/legal text meet readable contrast. |

## Component quality review

The following review is based on the current source and local browser captures at 390×844 and desktop widths on 22–23 August 2026. It is not a claim of full accessibility compliance; assistive-technology testing remains a separate release activity.

| Element | Current state | Quality verdict | Required follow-up |
| --- | --- | --- | --- |
| Spacing and corners | Route heroes, service sections, route-list groups, FAQ, share and footer now use the shared spacing and radius tokens. | **Pass in browser** | Services was checked at 1407×844 and 390×844: 34/24px hero radius, 20/17px route-list radius, 28/22px section radius, 56/24px section padding, and no horizontal overflow. |
| Header | Compact navigation and standalone mark are implemented. | **Pass in browser** | At 390px the menu locks page scroll, moves focus to the first item, exposes a visible focus ring, and returns focus to the toggle on Escape. |
| Brand mark | Signal SVG replaced the D monogram; SVG favicon uses the same language. | **Pass in browser** | The 37px header mark remains crisp on desktop and mobile. |
| Hero | Next-generation SAP AMS positioning, visible TCO/workflow/AI language, and two distinct actions are implemented; employment context is reserved for the lower profile close. | **Pass in browser** | Checked at 1407×844 and 390×844: 68px primary action, 44px secondary action, no clipping, and zero horizontal overflow. |
| Signal trace | TCO, Workflow, and AI control are rendered as a semantic ordered list with a reduced-motion rule. | **Pass in browser** | The trace remains secondary to the claim and readable without relying on motion. |
| Focus cards | TCO, workflow, and controlled-AI changes link to three real service routes beside the AMS exception visual. | **Pass in browser** | Cards form a vertical, non-overflowing reading sequence at 390px. |
| Method panel | The previous unreadable saturated-blue body copy was replaced by a white reading surface. | **Pass in browser** | The three steps remain readable and visually separate at mobile and desktop widths. |
| Evidence list | Only three reviewed diagnostics are surfaced. | **Pass in browser** | The routes resolve, status text stays visible, and titles wrap without fragments. |
| Footer | A 56px circular portrait identifies the personal trust block; LinkedIn and GitHub are separated from site navigation as labelled external actions. Descriptor, copyright, and legal links use explicit readable colours. | **Pass in browser** | Checked at 1407×844 and 390×844: portrait radius 50%, social-control radius 14px, social and legal targets 44px high, canonical profile URLs, and zero horizontal overflow. |
| Jekyll preview | Full production builds complete successfully; generated output is served locally for visual QA. | **Pass** | Do not accept later design changes without rebuilding before capture. |

## Missing layers to design deliberately

### 1. Professional context and trust

- Mention EPAM only as current employment context: `Senior SAP Consultant at EPAM Systems`.
- Do not use EPAM’s logo or imply company sponsorship without permission and a clear reason.
- Keep the personal-site disclaimer concise and readable in the footer or legal page.
- Separate public evidence from personal claims: reviewed diagnostics and profile facts carry trust; decorative “metrics” do not.
- Every external profile or service link must be intentional, current, and open safely in a new tab where appropriate.

### 2. Accessibility beyond colour

- Use semantic heading order: one H1, then H2s for major sections, H3s for internal groups.
- Every image needs meaningful alt text or an empty alt when it is decorative.
- Decorative signal texture and animation must be hidden from assistive technology.
- Keyboard focus order must follow the visual reading order.
- The mobile menu must trap neither focus nor page scroll and must close with Escape.
- Honour `prefers-reduced-motion`; no important meaning may depend on animation.
- Test at 200% zoom and at a 320px viewport; no horizontal scrolling except intentional data tables.

### 3. Responsive behaviour

- Define breakpoints by layout failure, not device names.
- Hero changes from two columns to one before the signal trace becomes cramped.
- Cards stack before their readable width falls below roughly 260px.
- Footer links wrap with real gaps; legal links remain separate, tappable targets.
- Keep the primary CTA visible without requiring precision tapping or horizontal scrolling.
- Check browser zoom at 73%, 100%, and 200%; screenshots at one zoom level are not sufficient.

### 4. Content states

- Design empty search, no-result, loading, error, and success states — not only the ideal content-rich page.
- Long titles, translated strings, missing images, and noindex/review status must not break cards or headings.
- A reviewed-content badge needs one consistent meaning and visual treatment across Atlas, scenarios, and research.
- Avoid turning status labels into decoration; explain their practical implication where it affects trust.

### 5. Search and knowledge discovery

- Search is a utility route, not the homepage’s primary conversion action.
- The search field has a persistent label, 16px input text, clear empty-state guidance, and obvious result grouping.
- Search results should show title, short useful excerpt, section/type, and review status where relevant.
- Do not make visitors infer whether a page is a public working note or reviewed reference.

### 6. Performance and resilience

- The background texture must be optimised and never block the first readable paint.
- Load only the type weights, icons, and imagery needed for the first screen.
- Use explicit image dimensions to prevent layout shift.
- The homepage must remain understandable if the texture, animation, JavaScript, or external fonts fail.
- Treat a stable local Jekyll build as a design-quality prerequisite: an unrenderable change cannot pass visual QA.

### 7. Internationalisation

- English is the reference layout; every translation must be checked for expansion before release.
- Do not embed layout-critical text inside images.
- Language selector labels must be readable and unambiguous.
- Date, number, currency, and directionality conventions need a shared implementation rule.

### 8. SEO and sharing surfaces

- Each hub and flagship page needs a concise human title, meta description, canonical URL, and share image strategy.
- Social cards should use the signal language but remain legible without tiny text.
- Do not repeat the entire navigation or generic keywords in descriptions.
- Structured data and visible page content must make the same claims.

### 9. Measurement and privacy

- Define what a successful page action is before adding analytics: services click, profile click, knowledge route, LinkedIn discussion.
- Avoid collecting unnecessary personal data; any form needs a clear purpose and privacy notice.
- Do not use pop-ups, forced newsletter gates, or artificial urgency on a professional consulting site.

### 10. Design operations

- Keep component names and tokens stable; do not create one-off colours or spacing values per page.
- Record every accepted visual change with route, viewport, browser zoom, and screenshot.
- Review the homepage, services, knowledge, a long Atlas page, search, and mobile menu together before a release.
- Maintain a short “rejected patterns” list: pale footer text, saturated-blue body-copy panels, mega-footers, search-as-hero, and uncontrolled card grids.

## Current implementation notes

- The brand mark is clipped to a circular signal surface and separated from the navigation capsule, so it no longer reads as a square header block.
- Use the same mark in the header and SVG favicon.
- Home is rendered through `_includes/sections/home-product.html`.
- The footer is `_includes/footer.html`.
- Sitewide visual tokens and responsive rules are in `assets/diagnostic-portal.css`.
- Long-form routes never place the dispersion texture behind body copy. Atmospheric imagery is reserved for deliberate hero or visual slots; reading surfaces use solid paper and high-contrast text.
- `assets/reader-tools.js` adds the long-form visual opening and consolidates Atlas source notes without changing publication metadata.
- `assets/reader-tools.js` selects the ERP, data, workflow, AI, or logistics model from the actual route rather than reusing one generic hub image.
- The canonical operational illustration set lives under `assets/img/systems/`; generated originals remain outside the repository in the Codex generated-images folder.
- `assets/img/labs/interview-readiness-field.webp` is the dedicated Career Lab system visual; it follows the same blue-dispersion family and contains no baked-in text.
- `.system-opening-visual` is the shared first-screen figure for pages that need to explain an operating model. It uses a real raster asset, `object-fit: contain`, a visible caption, exact intrinsic dimensions, and route-specific alternative text.
- Enterprise Context, Sales Process Atlas, AI Ready, Career Roadmap, Reusable Data Procedures, Datasets, Agent Skills, and SAP Diagnostics MCP use the shared system-opening contract. Their visuals are selected by subject rather than rotated decoratively.
- A page-level grid must always use `minmax(0, 1fr)` for content tracks. Long tables and code blocks may scroll inside their own container; they must never increase the document width.

## Quality gate before showing a change

1. Build Jekyll successfully.
2. Open the exact route in a browser at desktop and mobile widths.
3. Check text contrast, overflow, hierarchy, navigation, and CTA destinations.
4. Confirm the generated HTML contains no literal source markup.
5. Keep generated `_site/` out of version control.

## Open decisions

- Decide whether the hero should name EPAM in the eyebrow only or also add a discreet EPAM context line below the CTA.
- Decide whether LinkedIn is sufficient as the contact path or whether the services page should have a scoped contact form.
