# CV AI Design System

Compact design guidance for extending this site without drifting away from the current homepage style.

This is the canonical visual reference for new pages, sections, and components. If a new page looks noticeably more playful, more product-like, or more generic than the homepage, it is off-system.

## Design Intent

The site uses a restrained editorial B2B style:

- calm, premium, and analytical rather than flashy;
- strong hierarchy with large headlines and generous whitespace;
- light surfaces, dark ink, and very limited accent usage;
- structured storytelling instead of dashboard UI clutter;
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

`assets/site.css` is loaded last and currently establishes most of the homepage look. Reuse existing tokens and patterns before creating new ones.

## Foundations

### Typography

- Primary sans: `Inter`
- Editorial serif: `Source Serif 4`
- Default body and headings are sans-based.
- Serif is reserved for selective editorial emphasis, not full-page switching.

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

- page background: light grey-white, not pure white;
- primary ink: near-black blue-grey;
- soft ink: restrained slate for body text;
- muted ink: quieter metadata tone;
- accent: deep navy-charcoal;
- accent-soft: pale grey-blue tint;
- borders: low-contrast cool greys.

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

- Rounded corners are soft, not playful.
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

### Hero Pattern

Homepage hero sets the tone:

- centered composition;
- large title;
- concise subtitle and lead;
- compact personal/context cue;
- limited action set.

Use this pattern when the page represents a point of view, offer, capability, or summary page.

Rules:

- One primary message.
- One primary action, optionally one secondary.
- Do not overload the hero with badges, metrics, and three paragraphs at once.
- Keep imagery secondary to the statement.

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

## Implementation Notes

- Prefer editing data-driven content where possible.
- Reuse existing section partials and structural classes before adding new ones.
- If new CSS is required, add it in the existing stylesheet layer that matches the page, and avoid token duplication.
- If a new component becomes reusable, add it to this document after implementation.

## Short System Summary

If you need one sentence to guide future work, use this:

Build pages as calm editorial narratives with strong typography, light structured surfaces, disciplined dark accents, and enough whitespace to make expertise feel obvious.
