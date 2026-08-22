# CV AI Design System — legacy reference

> Historical reference only. The current blue diagnostic-signal system, navigation, accessibility, typography, and acceptance criteria are defined in [`DESIGN.md`](DESIGN.md) and implemented last in `assets/diagnostic-portal.css`. Do not use the coral/Inter tokens below for new work.

Compact design guidance for extending this site without drifting away from the current homepage style.

Use this document only to understand older route-canvas patterns that have not yet been migrated. New work must follow `DESIGN.md`.

## Design Intent

The site uses a restrained technical-editorial system:

- calm, premium, and analytical rather than flashy;
- strong hierarchy with large headlines, deliberate empty space, and direct manager-facing language;
- light surfaces, ink-blue type, hairline rules, and a single coral signal accent;
- system maps, diagnostic routes, and impact models instead of dashboard UI clutter;
- credibility first, decoration second.

The homepage is the benchmark. New work should feel like the same publication, not a separate template pack.

## Core Principles

- Narrative before interface. Each page should read like a guided argument, not a widget gallery.
- Typography carries hierarchy. Use type scale, spacing, and contrast before adding decoration.
- One strong idea per section. Avoid sections that try to explain everything at once.
- Calm surfaces. Prefer light backgrounds, soft borders, and minimal shadow.
- Accent with discipline. Dark accent is for emphasis and action, not for filling large areas.
- Breathing room matters. Dense layouts break the tone faster than color mistakes.
- Components may vary, but the mood must stay consistent.

## Source Of Truth

Current visual behavior is defined by these files, in this order:

1. `assets/material3.css`
2. `assets/main.css`
3. `assets/site.css`
4. `assets/evidence-atlas.css`
5. `assets/product-system.css`

`assets/product-system.css` is the shared token and reader layer. It follows the legacy stylesheets deliberately, normalising typography, spacing, focus states, navigation, long-form reading, and responsive behavior. `assets/site-chrome.css` and `assets/site-footer.css` provide the editorial chrome. Page-specific canvas files may compose these shared tokens but must not introduce a second visual language.

## Foundations

### Typography

- Primary sans: `Inter`
- Editorial serif: `Source Serif 4` (optional, only for long-form editorial emphasis)
- Technical labels: platform monospace stack.
- Default body and headings are sans-based.

Preferred hierarchy:

- `h1`: very large, compact, assertive, tight tracking.
- `h2`: prominent section headline, still editorial rather than product-marketing.
- `h3`: short subheads inside cards, comparisons, and lists.
- Body: readable, slightly enlarged, comfortable line-height.
- Eyebrow/kicker: uppercase, small, high letter-spacing, muted ink.

Rules:

- Keep headlines short enough to balance naturally on desktop.
- Use 1 to 2 short paragraphs before moving into structure.
- Avoid long centered text blocks except in the hero.
- Do not mix too many font voices on one page.

### Color

The live system is a cool light-neutral palette with dark ink:

- page background: mineral white `#fafaf8`, not pure white;
- primary ink: `#132238`;
- soft ink: restrained slate for body text;
- muted ink: quieter metadata tone;
- signal accent: coral `#ef5637`; it indicates an active path, a change, or an important action;
- muted system accent: blue-grey `#759bb7`;
- borders: hairline cool grey `#d8dde1`.

Practical rules:

- Use dark accent for buttons, emphasis, and selected visual anchors.
- Use tinted surfaces to separate content blocks.
- Avoid saturated colors unless the content truly requires semantic meaning.
- Avoid gradients unless they are extremely subtle and already aligned with existing section art direction.

### Space And Rhythm

- Pages should feel spacious, not stretched.
- Default content width is intentionally narrow for editorial reading.
- Sections need visible separation; the homepage uses large vertical gaps.
- Internal spacing should create rhythm in descending order:
  headline block -> section body -> card internals -> metadata.

Rules:

- Prefer fewer, larger sections over many shallow sections.
- Do not stack multiple dense grids without a quieter block between them.
- Keep mobile spacing generous; do not compress to “fit more”.

### Shape And Surface

- Corners are square-to-subtle (3–8px), never pill-first or app-like.
- Borders are light and structural.
- Shadows are subtle or removed entirely.
- Large surfaces should feel like paper panels, not floating app windows.

Rules:

- If a card needs attention, use stronger type or contrast before increasing shadow.
- Avoid glossy, glassmorphism, neon, or overly elevated UI.
- Prefer one surface treatment per section.

## Page Composition

New pages should generally follow this order:

1. Strong hero with one core claim.
2. Supporting narrative or problem framing.
3. Structured proof, comparison, framework, or evidence.
4. Trust or credibility block.
5. FAQ, next step, or contact CTA.

This does not mean every page must copy the homepage sections. It means each page should move from claim -> context -> proof -> action.

### Knowledge Product Canvas

For high-level knowledge products—Diagnostics, Scenarios, Research, Agent Tools, Datasets, and Profile—use a narrow family of canvas patterns rather than generic card grids:

- a short, direct hero that identifies the problem or access route;
- a ruled inventory, route list, or operating map that makes the choice visible;
- one clearly labelled system boundary (verification, noindex status, citation, or AI control);
- a concrete next route into a diagnostic, dataset, scenario, or service;
- source, citation, and related-content blocks kept quiet at the end.

The visual device must communicate structure. For example, a Research inventory separates monitoring, comparison, and investigation; a Dataset library separates human browsing from machine endpoints; an Atlas reader separates content from navigation. Do not add diagrams simply to decorate whitespace.

### Intent Brief

Use an **intent brief** for an AI-routing page. It is a public routing record, not a product landing page:

- state the route title, a short summary, review date, and public scope at the top;
- show the practical starting condition, covered problems, and search signals before related links;
- group next checks, datasets, notes, and services into a ruled route map; links must point to a useful record rather than repeat a generic CTA;
- show fit, non-fit, citation, and evidence boundaries as a compact comparison near the end;
- use only a short entrance reveal for section hierarchy and remove it completely when reduced motion is requested.

The underlying content remains ordinary HTML so the page works for a person, a crawler, or an AI client without the enhancement.

### Work-Library Map

Use the **work-library map** for Skill Hub index and group pages. It makes a large knowledge library navigable without reducing it to a badge or card catalogue:

- make the hero a concise statement of the work the library supports, with a narrow route list beside it;
- use a ruled topic map for skill groups; each entry needs a direct work label and one factual description;
- use an offset heading column for explanatory sections, comparison tables, and long learning paths;
- render recommended paths as ordered, two-column lists on larger screens and one source-order list on smaller screens;
- reserve hover movement for linked routes and honour reduced-motion preferences.

Do not remove detailed paths, limitations, or agent instructions merely to make the library shorter. Reduce interface noise, not useful content.

### Policy Record

Use the **policy record** treatment for legal, privacy, disclosure, accessibility, and responsible-AI pages:

- lead with the policy title and one short scope statement, without a sales CTA or decorative diagram;
- use ruled section headings and a small policy label to help a reader locate obligations quickly;
- retain clear lists and tables in ordinary document order;
- use the same reading width, focus states, mobile hierarchy, and ink/coral token system as the rest of the site.

Policy content should feel calm and direct. The visual treatment must clarify the record, not turn it into a branded campaign page.

### Dataset Source Record

Use the **dataset source record** for collection pages, search results, and generated item views:

- state the collection or item clearly, then place human routes and machine endpoints in one narrow action list;
- render filters as ordinary input controls with visible focus, never as a decorative control panel;
- render collection entries as ruled records with title, concise description, type, identifier, and raw-data route;
- use a square, low-contrast metadata treatment and reserve coral for the active type or link state;
- render generated structures, option sets, and raw JSON as inspectable documents with no elevation or rounded card mosaic.

The data structure, JSON routes, client-side filtering, and no-JavaScript fallback must remain unchanged.

### Hero Pattern

Homepage hero sets the tone:

- asymmetric composition with a live dependency trace: several inputs converge on one diagnostic decision;
- large, concrete title and one concise supporting line;
- one primary action and one quiet secondary path;
- only relevant proof cues; avoid dense self-description.

### Global Navigation

Navigation is a compact route selector, not a secondary homepage:

- keep the persistent routes limited to services, scenarios, Atlas, journal, profile, and search; the contact action is the single contrasting action;
- expose the current route with both a visible state and `aria-current="page"`;
- on smaller screens, open one full-width ruled list from a labelled menu control rather than shrinking desktop links until they wrap;
- move keyboard focus into the open list, support Escape, keep Tab travel within the toggle and its list, and close the list when the viewport returns to desktop width;
- language selection remains a native disclosure and must retain its current-language state and keyboard baseline.

The menu animation is limited to the menu mark and a short layout reveal. Route finding must remain immediate with reduced motion and without JavaScript.

Use this pattern when the page represents a point of view, offer, capability, or summary page.

Rules:

- One primary message.
- One primary action, optionally one secondary.
- Do not overload the hero with badges, metrics, and three paragraphs at once.
- Keep imagery secondary to the statement.
- When motion is used, animate a meaningful state change such as a signal moving along the trace. Keep the static diagram legible and disable the animation for reduced-motion preferences.

### Section Pattern

Most sections on the homepage share the same logic:

- short eyebrow or badge;
- strong title;
- one statement or framing paragraph;
- a structured body: cards, comparison, list, proof points, quote, or CTA.

Rules:

- Every section should answer one question.
- If a section contains cards, make their differences meaningful.
- Use quotes and highlighted notes sparingly; they work because they are not everywhere.

### Grid Pattern

The system uses grids, but not as generic SaaS cards.

Allowed grid uses:

- comparison blocks;
- evidence/stat cards;
- capability lists;
- editorial summaries with a clear hierarchy.

Rules:

- Mix card sizes only when there is a clear content hierarchy.
- Avoid identical cards repeated without narrative progression.
- On mobile, stacked cards must still read in a deliberate order.

## Component Guidance

### Buttons And Links

- Primary actions are dark, compact, and confident.
- Secondary actions are quieter and often outlined or lightly tinted.
- Inline links should feel editorial, not like app navigation chrome.

Rules:

- Keep action labels short and specific.
- Do not place more than two prominent actions in the same local cluster.
- External-link indicators are acceptable when already used in that pattern.

### Cards

Cards are content containers, not decoration.

Use cards for:

- proof points;
- comparisons;
- stat summaries;
- capability capsules;
- structured excerpts.

Avoid:

- decorative empty cards;
- nested cards inside cards unless the pattern already exists;
- rainbow card sets or arbitrary per-card colors.

### Route Lists And Inventories

Use a ruled route list when the reader is choosing among entries that have equal informational weight:

- number, title, a concise decision-oriented description, count or state, and directional affordance;
- one link per row, with the entire row as the target;
- a low-contrast hover state that confirms the row is interactive;
- no duplicate “open” buttons or icon-only actions;
- stack fields in source order on small screens.

Use a tab selector only when it changes a genuinely different view of the same inventory. It must use semantic tabs, arrow-key navigation, `aria-selected`, and a readable no-JavaScript default.

### Public Evidence Registers

For publications, certifications, education records, and other proof surfaces, use the **public evidence register** pattern rather than a CV grid:

- a short claim about what can be verified;
- a compact numerical ledger, not badge tiles;
- three restrained scope rows that explain what the record covers;
- a ruled source register with date, authority or publisher, record, category, and one verification action;
- category filters that only improve browsing: all records remain in the static HTML and usable without JavaScript.

The relevant visual signals are provenance and scope. Do not use provider logos, completion-badge mosaics, motivational learning copy, or unsupported progression claims. Filters must use buttons with `aria-pressed`, announce the visible record count, preserve keyboard use, and respect reduced-motion preferences.

### Professional Record

The `/cv/` route is a complete professional record, not the site’s primary brand page. Its entry view should therefore answer four practical questions before chronology begins: what work is covered, whose public record this is, what company/profile context is available, and where the machine-readable source can be checked. Keep full role history, credentials, and education intact below the fold, but present them as ruled records with dates and evidence links—not as résumé tiles or capability claims.

### Manager FAQ

Use a manager FAQ as a decision guide, not an accordion full of sales copy:

- begin with the decision that has to be made, in plain operational language;
- make each question the summary line so it is useful before it is opened;
- use native `details` / `summary` controls for keyboard access and a no-JavaScript baseline;
- number questions only to make scanning and discussion easier; do not add badges, icons, or decorative illustrations;
- retain a compact route table beneath the guide when the reader needs to turn a visible constraint into a sensible first route.

### Service Brief

Use the **service brief** pattern for a consulting detail page. It lets a manager establish scope before reading the implementation detail:

- use a large, direct service title with one short statement of the operational condition it addresses;
- put the subtitle beside the title on larger screens so the page starts with both the offer and its practical boundary;
- provide a generated in-page outline when there are three or more sections; it is a native disclosure on small screens and highlights the current section during reading;
- number primary sections and delivery steps only to support discussion and handover, not to imply a rigid method;
- render delivery stages and decision tables as ruled documents, with no floating cards or decorative illustration;
- retain all detailed diagnostic questions, boundaries, outputs, and related links below the scan layer.

This pattern is intentionally content-led. Its only interactive details are the readable outline, copy/share tools, and current-section state; all content remains usable without JavaScript.

### Diagnostic Record

Use a **diagnostic record** for Atlas and Scenario detail pages. The page should make it easy to establish scope, then follow a structured investigation without reducing technical depth:

- use a large title and one short statement of the condition under investigation;
- place review state, process, SAP area, and indexing boundary in a narrow record rail rather than a colored badge stack;
- number primary sections as a reading and handover aid; the numbers do not imply a fixed solution sequence;
- keep the body as the dominant reading column, with a sticky in-page outline only on larger screens;
- show copy, share, and useful actions as light text controls; retain their visible keyboard focus and no-JavaScript reading baseline;
- leave original evidence, verification status, public sources, and related diagnostics untouched.

This is intentionally a technical record, not a product page. Avoid capability cards, achievement claims, generic summaries, or decorative diagrams that do not help a reader diagnose an issue.

### Signal Register

Use a **signal register** for dated News and Radar collections. It makes the status of provisional material explicit without making it look like a content-marketing feed:

- use a large, concise distinction in the hero: changes to track versus signals under review;
- give the collection a compact ledger for item count, purpose, and indexing status;
- render each item as a ruled chronological row with its date, source, confidence, scope labels, and one “Open” link;
- keep News and Radar visually identical while their headers make the different evidence boundary clear;
- do not use coloured cards, category chips, source logos, or a featured-item carousel for these collections.

### Quotes, Notes, And Callouts

These appear on the homepage as editorial punctuation.

Rules:

- Use them to create pause or emphasis, not as filler.
- Keep them short.
- Surround them with enough whitespace.
- If everything is highlighted, nothing is highlighted.

### Icons

- Icons support scanning, not branding.
- Material Symbols are already in use.
- Icons should be simple, outline-friendly, and semantically clear.

Rules:

- One icon per card/header is enough.
- Do not build icon-heavy feature grids that feel like SaaS marketing.

## Content Style

The visual system depends on the writing style.

Preferred tone:

- analytical;
- concise;
- credible;
- operational;
- buyer-aware;
- calm under pressure.

Writing rules:

- Lead with the business or operational implication.
- Prefer precise language over hype.
- Avoid generic AI slogans.
- Keep paragraphs short.
- Use lists when structure improves scanning.
- Use evidence, ratios, consequences, and tradeoffs where possible.

Avoid copy that sounds:

- overly inspirational;
- startup-pitch heavy;
- vague or trend-chasing;
- stuffed with buzzwords.

## Rules For New Pages

When creating a new page:

1. Start from an existing section or page pattern before inventing a new layout.
2. Reuse global tokens from `:root`.
3. Reuse the existing width and spacing discipline.
4. Introduce at most one new visual idea per page.
5. Keep the page visually lighter than a dashboard and more structured than a plain article.
6. Make sure the page still feels correct without animation.
7. Check mobile early; the style relies on proportion and spacing.

## What To Avoid

- generic template-card SaaS layouts;
- oversized colored gradients;
- purple-heavy palettes;
- dark mode as the default visual direction;
- excessive badges/chips;
- too many equal-weight sections;
- long walls of centered copy;
- deep component nesting;
- decorative motion without purpose;
- mixing neubrutalism, glassmorphism, and editorial minimalism on one page.

## Fast Review Checklist

Before considering a new page done, verify:

- Does it look like it belongs next to the homepage?
- Is the main claim obvious within a few seconds?
- Is there enough whitespace?
- Are accents used sparingly?
- Are cards serving content rather than filling space?
- Is there a clear reading order on mobile?
- Is the CTA count disciplined?
- Does the copy sound operational and credible?

## Page Hierarchy and Navigation

Landing, catalogue, and knowledge-product pages use the same decision order:

1. State the operating subject in a small label.
2. Give one concrete title.
3. Explain the scope in one short paragraph.
4. Offer one primary action and one secondary route.
5. Put the available routes or evidence immediately beside or below that choice.

Do not treat a catalogue page as a billboard. At desktop widths, its title should remain below `3rem`; on compact widths, it should remain below `2.85rem`. The first useful routes must be visible without a second hero-sized section.

The header is intentionally responsive: direct primary navigation is visible from `1101px`; the menu control is reserved for narrower layouts. Do not hide the desktop routes to create a stylistic effect.

## Implementation Notes

- Prefer editing data-driven content where possible.
- Reuse existing section partials and structural classes before adding new ones.
- If new CSS is required, add it in the existing stylesheet layer that matches the page, and avoid token duplication.
- If a new component becomes reusable, add it to this document after implementation.
- Page-specific canvas CSS belongs in `assets/<section>-canvas.css`; it must consume the shared `--ps-*` token values or matching local aliases, include a mobile layout, keyboard focus state, and `prefers-reduced-motion` behavior.
- Canvas JavaScript may add reveal, tab, calculator, or filtering behavior only after the static page remains fully usable. JavaScript must not contain source-of-truth content or change a page's indexing boundary.

## Evidence Atlas Production Layer

`assets/evidence-atlas.css` is the canonical styling layer for all templates and localisations. It deliberately turns the site into an evidence-led personal publication rather than a rounded-card SaaS interface:

- **Palette:** quiet grey-white page (`--ea-page`), white paper surfaces, navy ink (`--ea-navy`), cool-grey hairlines, and one restrained amber signal (`--ea-signal`) for metadata, focus, and status. Amber is never used as a large decorative fill.
- **Structure:** pages, cards, evidence grids, process rails, tables, and metadata use a shared 1px ruled system. Corners are 3px; elevation is removed except for an intentional offset-paper shadow on key dark or code surfaces.
- **Typography:** Inter carries display and body hierarchy; Source Serif 4 is reserved for quotation and editorial pause; the system mono face distinguishes labels, chronology, status, and compact metadata.
- **Actions:** rectangular, high-contrast controls with visible focus. Nav states use an underline rather than a decorative pill.
- **Responsive and locale behaviour:** the header collapses to an accessible menu, grids stack without reordering content, long translations can wrap, and RTL changes directional spacing and header alignment.
- **Motion:** short entrance and hover transitions only where they strengthen hierarchy. Every animation and smooth-scroll effect is neutralised for `prefers-reduced-motion`.

New reusable components belong in `assets/evidence-atlas.css`, should consume the `--ea-*` tokens, and must be checked in both a long-form page and a mobile/RTL page before release.

## Short System Summary

If you need one sentence to guide future work, use this:

Build pages as calm editorial narratives with strong typography, light structured surfaces, disciplined dark accents, and enough whitespace to make expertise feel obvious.
