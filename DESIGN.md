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

`Operating symptom → evidence → decision → reusable outcome`

### Recommended sections

1. **Hero** — a concise SAP operations claim, current EPAM role, one primary services CTA, one secondary knowledge CTA, and the diagnostic signal trace.
2. **Where I help** — three problem areas: recurring operational friction; integration and data boundaries; change that has to hold.
3. **How the work moves** — Frame the situation; Trace the evidence; Make the next move.
4. **Public working evidence** — three reviewed diagnostics. This supports trust; it must not become a catalogue.
5. **Close** — a clear invitation to view services or discuss on LinkedIn.

### Do not put on the homepage

- A raw search textarea as the principal conversion mechanism.
- Large lists of Atlas, Labs, datasets, machine tools, or every site area.
- An interview-preparation promo strip.
- Repeated profile cards or a large “about me” block.
- A mega-footer with product navigation columns.

## Navigation

Primary navigation is product-level and short:

- Work
- Knowledge
- About
- Search
- Language

Labs, frameworks, career material, and machine-readable work remain reachable from the relevant hubs, not from every screen.

## Cluster and hub design

### Work / Services

Purpose: explain engagements and the next discussion. Lead with operating situations and outcomes, not a generic service card grid.

### Knowledge

Purpose: curated, human-readable material. Give visitors a small number of routes and make review status visible.

### Atlas and scenarios

Purpose: diagnostic depth. Prioritise symptom, business context, SAP touchpoints, evidence, and the next diagnostic step.

### Labs and frameworks

Purpose: active methods and practical tools. They are secondary to the consulting narrative and must not compete with the homepage CTA.

### Machine layer

Purpose: structured exports and agent tools. Keep it a clear specialist route, not a prominent footer category.

## Footer

The footer is a compact trust and exit point, not a sitemap.

- Identity: `Dzmitryi Kharlanau` + `SAP operations · transformation · practical AI`.
- Links: Services, Profile, Knowledge, LinkedIn.
- Legal: Privacy and Accessibility.
- Keep all text high contrast and readable.
- Avoid the words “independent consulting”.

## Component inventory and acceptance criteria

| Element | Job | Content rule | Interaction / responsive rule | Acceptance check |
| --- | --- | --- | --- | --- |
| Brand mark | Identify the site without a wordmark in the header. | Signal beam, rings, and crosshair; no letter monogram. | Crisp at 30px; has a text alternative through the parent home link. | Mark is recognisable on light canvas and has no blurred edges. |
| Header | Give quick access to the site’s three main areas. | Work, Knowledge, About, Search, Language. | Sticky at desktop; collapses into an explicit menu on mobile. | All controls are visible, keyboard reachable, and do not overlap at 320px. |
| Hero | Explain the value of the site in one glance. | One claim, one EPAM role line, a short supporting sentence. | Two columns on desktop; single column on mobile. | No line exceeds the intended reading width; heading does not clip or become larger than the viewport. |
| Signal trace | Make the diagnostic method tangible. | Symptom, Evidence, Decision, each with one short question. | One quiet animated point only; no motion with reduced-motion preference. | It remains secondary to the claim and readable without the animation. |
| Primary CTA | Move visitors to the services context. | `Start with a diagnostic` or `View consulting services`. | Large hit target; lime is reserved for this action. | Links to `/services/`, has visible focus, and is readable without hover. |
| Secondary CTA | Let research-oriented visitors enter knowledge without competing with the main action. | `See the public knowledge base`. | Text link, not a second filled button. | Links to `/knowledge/` and does not visually outweigh the primary CTA. |
| Focus cards | Explain the three kinds of work. | One problem area, one explanatory sentence, one destination. | Three columns desktop, a vertical list mobile. | Whole card is clickable; card text is not smaller than 13px. |
| Method panel | Explain how the work is done. | Frame, Trace, Make the next move. | White surface with blue text; three columns desktop, one column mobile. | No dark-on-blue body copy; each step works as a standalone paragraph. |
| Evidence list | Prove the approach through selected reviewed material. | Maximum three reviewed resources on home. | Row links become stacked on mobile. | Status is visible, titles do not wrap into unreadable fragments, and all routes resolve. |
| Close / CTA | Give a calm end to the page. | One invitation and two paths: Services and LinkedIn. | Centered on desktop; stacked on mobile. | Does not repeat the hero claim verbatim. |
| Footer | Provide compact identity, exit routes, and legal links. | Name, descriptor, Services, Profile, Knowledge, LinkedIn, Privacy, Accessibility. | One compact column/row system; no sitemap grid. | Descriptor and legal line meet readable contrast; no pale text on pale canvas. |

## Component quality review

The following review is based on the current source and local browser captures at 390×844 and 1440×900 on 22 August 2026. It is not a claim of full accessibility compliance; assistive-technology testing remains a separate release activity.

| Element | Current state | Quality verdict | Required follow-up |
| --- | --- | --- | --- |
| Header | Compact navigation and standalone mark are implemented. | **Pass in browser** | At 390px the menu locks page scroll, moves focus to the first item, exposes a visible focus ring, and returns focus to the toggle on Escape. |
| Brand mark | Signal SVG replaced the D monogram; SVG favicon uses the same language. | **Pass in browser** | The 37px header mark remains crisp on desktop and mobile. |
| Hero | Consultation claim, EPAM context, two actions, and signal trace are implemented. | **Pass in browser** | Text, actions, and the decorative texture remain in the intended grid at 390px and 1440px. |
| Signal trace | Semantic ordered list and reduced-motion rule are present. | **Pass in browser** | The trace remains secondary to the claim and readable without relying on motion. |
| Focus cards | Three clear work areas and responsive grid rules are present. | **Pass in browser** | Cards form a vertical, non-overflowing reading sequence at 390px. |
| Method panel | The previous unreadable saturated-blue body copy was replaced by a white reading surface. | **Pass in browser** | The three steps remain readable and visually separate at mobile and desktop widths. |
| Evidence list | Only three reviewed diagnostics are surfaced. | **Pass in browser** | The routes resolve, status text stays visible, and titles wrap without fragments. |
| Footer | Footer structure is compact; descriptor, copyright, legal links, and exit routes use explicit readable colours. | **Pass in browser** | Legal links retain 44px tap targets on mobile. |
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

- The brand mark is a vector signal mark derived from the blue-dispersion visual: field, beam, circles, and crosshair.
- Use the same mark in the header and SVG favicon.
- Home is rendered through `_includes/sections/home-product.html`.
- The footer is `_includes/footer.html`.
- Sitewide visual tokens and responsive rules are in `assets/diagnostic-portal.css`.

## Quality gate before showing a change

1. Build Jekyll successfully.
2. Open the exact route in a browser at desktop and mobile widths.
3. Check text contrast, overflow, hierarchy, navigation, and CTA destinations.
4. Confirm the generated HTML contains no literal source markup.
5. Keep generated `_site/` out of version control.

## Open decisions

- Decide whether the hero should name EPAM in the eyebrow only or also add a discreet EPAM context line below the CTA.
- Decide whether LinkedIn is sufficient as the contact path or whether the services page should have a scoped contact form.
