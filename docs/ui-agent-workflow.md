# UI Agent Workflow

This is the operational loop for ChatGPT, Codex, Claude Code, and other coding agents
editing the site's visual layer. It exists to prevent one-off fixes from creating
another local design language.

## Required reading

Before a UI change, read:

1. DESIGN.md
2. docs/editorial-design-system.md
3. docs/ui-component-catalog.md
4. config/ui-components.json
5. the route markup
6. the CSS files that actually load after the component owner layer

For Labs work, also read labs/AGENTS.md.

## The loop

### 1. Frame the reader task

State what the reader is trying to do: read, compare, navigate, verify, answer, trace,
or remember. Do not start from "make this prettier."

### 2. Find the existing component

Use the registry content_signals, use_when, and avoid_when fields. Inspect the
reference route and the component source CSS or HTML.

If a stable component fits, reuse it. If a domain component fits inside the same
domain, reuse it there. A candidate is not a default.

### 3. Diagnose the actual failure

Classify the problem before editing:

- typography — text too small, line length wrong, weak hierarchy;
- density — padding or gaps too tight or too loose;
- layout — too many columns, poor wrapping, empty space;
- affordance — unclear link, action, or control;
- boundary — borders, grouping, or ownership unclear;
- cascade — later CSS silently overrides the intended component;
- content shape — the wrong component is being used for the information.

Fix the highest-level cause. Do not compensate for a wrong layout by shrinking type.

### 4. Choose change scope

Use the smallest correct owner:

- one content instance is wrong -> change markup or content;
- every usage of a component is wrong -> change the component owner;
- one domain needs a deliberate variant -> change the domain layer;
- only one route has genuinely unique semantics -> route-specific CSS.

Repeated route-specific overrides are evidence that a shared component is missing or
its contract is wrong.

### 5. Implement without visual drift

Use tokens before literal values. Preserve semantic HTML. Keep meaningful body copy
at the readability floor. Preserve 44px interaction targets where practical. Avoid
new cards, pills, shadows, colors, and type scales unless the component contract
requires them.

Do not let two layers own the same visual property accidentally. If
assets/enterprise-context-polish.css intentionally overrides
assets/css/components.css, document the domain behavior rather than adding more
specificity.

### 6. Verify the rendered behavior

At minimum check:

- desktop and mobile layout;
- 320, 375, 430, 768, 1024, and 1280 widths when the change is responsive;
- 100% and 200% zoom for reading components;
- keyboard focus for interactive elements;
- no horizontal overflow except explicit table or code scrolling;
- no text below the registry readability floor without a documented reason;
- print behavior for learning material where relevant.

CI runs Jekyll, accessibility checks, and a browser visual smoke test. A green build
does not replace visual reasoning; it only proves that known gates passed.

### 7. Systemize the result

If the change alters a reusable component contract, update in the same commit:

- config/ui-components.json;
- docs/ui-component-catalog.md;
- docs/editorial-design-system.md when the system rule changed;
- the component CSS or include;
- validation and tests if the contract gained a new invariant.

A one-page exception does not belong in the registry unless it is intended for reuse.

## New component gate

Create a new component only when all are true:

1. no stable or domain component represents the same reader task;
2. changing the information structure does not solve the problem;
3. the pattern has a clear semantic name;
4. the owner layer is clear;
5. responsive and accessibility behavior can be stated before styling;
6. at least one real route will use it.

New components start as candidate. Do not label them stable merely because they look
good in one screenshot.

## Agent handoff format

After a UI change, report:

- component IDs reused or changed;
- whether the change is global, domain, or route-local;
- files changed;
- reference routes;
- validation and CI status;
- any remaining candidate component or visual debt.

This makes the next agent's first step inspection rather than rediscovery.
