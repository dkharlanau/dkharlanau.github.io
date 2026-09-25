# Site Content and Design Contract

This file is the mandatory bridge between editorial content and the visual system.
AGENTS.md requires article-like work to read it, so this path must remain valid.

## Core rule

Content structure comes before decoration. A page should expose the reader task, the
information hierarchy, and the evidence boundary first. UI components then make that
structure easier to read, compare, navigate, verify, answer, trace, or remember.

## Sources of truth

- Product-level direction: DESIGN.md
- Visual tokens and system rules: docs/editorial-design-system.md
- Reusable component catalog: docs/ui-component-catalog.md
- Machine-readable component registry: config/ui-components.json
- UI editing loop for agents: docs/ui-agent-workflow.md
- Repository and publication rules: AGENTS.md
- Labs-specific rules: labs/AGENTS.md

Do not create a competing design specification in a route README or page-local
stylesheet.

## Content shape to UI shape

Use prose for explanation, lists for grouped facts, tables for real two-dimensional
comparison, FAQ for independent questions, route lists for navigation, source
registers for provenance, comparison groups for a few conceptual alternatives, and
semantic diagrams for relationships or process structure.

The component exists to reveal the information model. If the model is unclear, fix
the content before adding visual treatment.

## Writing contract

Public site copy is English. Keep technical explanations clear enough for a B2 reader
without flattening SAP meaning. Prefer direct terms, short paragraphs, specific
objects, process ownership, and observable effects. Avoid generic AI phrasing,
marketing filler, and decorative labels.

## Readability contract

- Body copy uses the site normal reading scale and line height.
- Metadata is compact but still readable.
- Long explanations keep a useful reading measure instead of filling the viewport.
- Mobile layouts reflow; they do not solve density by shrinking text.
- Wide tables and code may scroll horizontally.
- Paragraph-heavy content does not stay in narrow three-column layouts.

## Reuse contract

Before adding CSS, identify the component in config/ui-components.json. Reuse stable
or domain components before inventing route-local variants. If the same fix is needed
on more than one route, treat that as a component-system signal.

When a reusable component changes, update its CSS or include, registry entry, and
catalog documentation in the same commit.

## Evidence and status

Visual prominence must not imply a stronger verification state than the content owns.
Draft and noindex material remains structurally distinct from reviewed content.
Source blocks show provenance without turning sources into decorative cards.

## Accessibility and responsive behavior

Semantic HTML, heading order, keyboard access, visible focus, sufficient contrast,
and meaningful link text are part of the component contract. They are not optional
QA work after styling.

## Completion condition

A content or UI edit is complete only when:

1. the right information structure is used;
2. the correct existing component is reused or a justified candidate is added;
3. mobile and desktop behavior are defined;
4. accessibility behavior is preserved;
5. registry and documentation remain synchronized;
6. repository validation and rendered checks pass.
