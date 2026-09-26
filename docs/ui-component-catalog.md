# UI Component Catalog

This catalog is the human-readable companion to config/ui-components.json.
The JSON registry is the machine contract. This document explains the design intent,
selection rules, markup expectations, examples, and limits that an AI coding agent
must understand before editing the visual layer.

## How to choose a component

Choose from the reader task, not from visual similarity.

| Reader task | Default component |
|---|---|
| Compare structured facts, fields, rules, or objects | study-table |
| Read common questions independently | page-faq |
| Enter a substantial Labs/research section | research-section-intro |
| State a scope or ownership distinction | boundary-note |
| Choose among peer destinations | route-list |
| Choose among three to six peer destinations with similar weight | faceted-route-grid (candidate) |
| Inspect provenance and evidence | source-register |
| Compare two or three concepts | comparison-group |
| Trace one SAP determination in depth | determination-detail |
| Offer secondary deep-dive links | context-links |
| Show a short ordered recall sequence | compact-sequence (candidate) |
| Remember one central rule or distinction inside prose | key-idea-highlight (candidate) |
| Share or cite the current page | site-share |
| Scan the shape of a detailed Skill Hub page | skill-overview |
| Copy a ready-to-reuse Skill Hub template | copyable-template |

If the content does not fit, first change the information structure. Do not create
a new component merely because a page-specific selector is easier.

## Status model

- stable — approved default inside its declared scope.
- domain — approved inside one product/domain family.
- candidate — useful pattern still being evaluated.
- legacy — existing compatibility pattern; no new usages.
- deprecated — do not use; migrate when touched.

A candidate becomes stable or domain only after it has a real route, responsive
behavior, accessibility behavior, documentation, and registry validation.

## Shared readability floor

Meaningful body copy should normally be at least 17px. Metadata and compact labels
should normally be at least 14px. Interactive targets should be at least 44px where
practical. On mobile, preserve type size and change layout instead of shrinking text.

## study-table

Purpose: educational comparisons, field matrices, reference tables, and assessment
material.

Markup contract:

    <div class="table-scroll study-table" tabindex="0" role="region"
         aria-label="Meaningful table description">
      <table class="study-table__table">
        ...
      </table>
    </div>

Use semantic th elements. Wide tables scroll horizontally. Do not add a second
route-local table skin on top of this component.

Reference implementation:
/labs/enterprise-context/master-data/#high-leverage-fields

## page-faq

Purpose: independent questions with concise answers.

Use the shared include and data model:
_includes/page-faq.html + _data/page_faqs.yml.

Native details/summary is part of the contract. Do not replace it with custom
JavaScript disclosure behavior. The eyebrow is a compact editorial plaque, not an
uppercase micro-label. Question and answer text stay at reading size.

Reference implementation:
/services/sap-o2c-process-audit/

## research-section-intro

Purpose: keep eyebrow, section heading, and supporting paragraph together as one
reading unit on Labs and research pages.

The heading is the primary signal. The eyebrow is secondary. Do not split the heading
and explanation into narrow columns simply to fill horizontal space.

Reference implementation:
/labs/enterprise-context/master-data/#sales-master-data-catalog

## boundary-note

Purpose: a short scope, ownership, or interpretation boundary.

Use it when one distinction prevents a likely conceptual mistake. It is not a warning
component and should remain visually quiet. If the content is a true warning or
status, use the semantic callout system instead.

Reference implementation:
/labs/enterprise-context/master-data/

## route-list

Purpose: navigation among peer destinations.

One row equals one destination. The row should contain enough information to choose
the route without adding a duplicate button. Do not use route lists for facts that
are not links.

Reference implementation:
/labs/enterprise-context/pricing/

## faceted-route-grid

Status: candidate.

Purpose: present a small set of peer destinations as compact, clearly clickable
cards when a plain vertical route list feels too sparse. The silhouette is
hex-inspired, but the content remains ordinary readable text.

Use it for roughly three to six destinations with comparable importance and short
descriptions. The whole card is one link. Keep the title and description inside the
same anchor; do not add duplicate Read more buttons.

Do not use it for long paragraphs, dense comparison data, non-navigation facts, or
large inventories. For seven or more routes, prefer route-list or another denser
navigation pattern.

On wide screens the component uses two columns; an odd final card is centered. On
mobile it becomes one column without reducing text size. The faceted background is
decorative only, and hover or focus must not be the only signal that an item is a
link.

Reference implementation:
/skill-hub/architecture/

## source-register

Purpose: compact source provenance for Enterprise Context pages.

Provider, source title, metadata, and action remain readable. The component may use
three columns on wide screens, two on medium screens, and one on mobile. Never
preserve the grid by shrinking meaningful text.

Reference implementation:
/labs/enterprise-context/shipping/

## comparison-group

Purpose: compare two or three conceptual alternatives.

Use only while every block remains comfortably readable. Paragraph-heavy concepts
wrap into fewer columns. If the content becomes a dense matrix, use a study table.
If it becomes a sequence, use a process or sequence component.

Reference implementation:
/labs/enterprise-context/pricing/

## determination-detail

Purpose: explain one SAP determination as a technical record.

Use for inputs, rule logic, output, evidence, failure modes, or diagnostic detail
that belong to one determination. It is not a generic card.

Reference implementation:
/labs/enterprise-context/credit/

## context-links

Purpose: secondary internal deep dives.

Use for a small set of related links after the explanation. If route choice is the
primary task, use route-list instead.

Reference implementation:
/labs/enterprise-context/master-data/#master-data-deep-dives

## compact-sequence

Status: candidate.

This Master Data pattern is useful for short ordered recall sequences because the
number rail stays narrow while the explanation keeps a normal reading measure.
Do not copy it outside its current scope yet. Prefer the semantic process-map system
for reusable cross-domain process visuals.

Reference implementation:
/labs/enterprise-context/master-data/#master-data-o2c

## key-idea-highlight

Status: candidate.

Purpose: give one central rule, distinction, or decision a quiet inline emphasis
inside normal prose. It is for memory and scanning, not for status.

Markup contract:

    <mark class="key-idea">The distinction the reader should retain.</mark>

Use only short phrases or sentences. Keep the surrounding paragraph as ordinary prose.
Do not highlight most of a paragraph, repeat the pattern on every list item, or use it
for warnings, compliance states, or verification. Multi-line highlights wrap naturally
and keep the same soft cobalt selection treatment on each line.

Reference implementation:
/skill-hub/architecture/capability-mapping-working-skill/

## skill-overview

Status: candidate.

Purpose: give a detailed Skill Hub page a small factual scan layer before the long
article begins. The component is generated from real page structures: Deliverables,
Templates, Working method, and Quality checklist. It is an editorial ledger, not a
scorecard.

The ledger appears only when at least two facts are present. Counts are derived from
the current DOM, so authors do not maintain duplicate numbers in frontmatter or prose.

Use icons only as scan aids. The definition-list labels and counts must carry the
meaning on their own. Do not add readiness percentages, difficulty scores, progress,
or decorative KPI tiles.

Reference implementation:
/skill-hub/architecture/non-functional-requirements-working-skill/

## copyable-template

Status: candidate.

Purpose: make a ready-to-reuse block in a Skill Hub `Templates` section directly
copyable without hiding or replacing the source content.

`reader-tools.js` enhances `pre` blocks inside the Templates section with a quiet
toolbar, the local template heading, and a visible `Copy template` button. The raw
preformatted block remains the no-JavaScript baseline. Copy feedback is announced to
assistive technology, and the existing manual-copy fallback is used when clipboard
access is unavailable.

Do not apply this treatment to every code sample. It is for reusable templates, not
for explanatory examples or generated output.

Reference implementation:
/skill-hub/architecture/non-functional-requirements-working-skill/#reader-section-9

## site-share

Purpose: provide standard share, copy-link, citation, email, and lightweight
feedback actions without depending on the width of the current route canvas.

Use the shared include _includes/site-share-widget.html. The component owns its own
centered width, yellow utility surface, action sizing, and mobile collapse. Route CSS
must not stretch it to the viewport edge or create a second share treatment.

Reference implementation:
/about/

## Component ownership

- Global editorial components: assets/css/components.css.
- Site share utility: assets/css/layout.css and _includes/site-share-widget.html.
- FAQ: assets/page-faq.css and _includes/page-faq.html.
- Research/Labs composition: assets/research-canvas.css.
- Enterprise Context domain components: assets/enterprise-context-polish.css.
- Route-specific CSS may own genuinely unique subject visuals, not a second version
  of a table, FAQ, source list, heading block, or comparison component.

Because Enterprise Context polish loads after the global component layer, a domain
selector can override a global component. When one component should own the final
visual behavior, remove the competing rule or explicitly carve out the shared
component. Do not solve cascade conflicts by continuously increasing selector
specificity.

## New component lifecycle

1. Write the reader task in one sentence.
2. Confirm that no stable or domain component fits after content restructuring.
3. Add the new pattern as candidate.
4. Put reusable CSS in the correct shared or domain owner layer.
5. Use semantic HTML and define keyboard/focus behavior.
6. Define mobile behavior without reducing the readability floor.
7. Add a real source route.
8. Add the component to config/ui-components.json.
9. Document it here.
10. Run python3 scripts/validate_ui_components.py and the normal site build.
11. Promote only after the rendered component has been reviewed.

## Anti-patterns

Do not add route-local table skins, decorative cards around normal prose, uppercase
decorative micro-labels, tiny source metadata, dense three-column paragraph layouts,
duplicate Open or Read more actions, or repeated rules that fragment one explanation.
These are information-design problems, not styling opportunities.
