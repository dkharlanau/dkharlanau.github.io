# Design Principles

<cite>
**Referenced Files in This Document**   
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md)
- [main.css](file://assets/main.css)
- [hero.html](file://_includes/sections/hero.html)
- [social-line.html](file://_includes/components/social-line.html)
- [default.html](file://_layouts/default.html)
- [index.html](file://cv/index.html)
</cite>

## Table of Contents
1. [Neubrutalist Design Philosophy](#neubrutalist-design-philosophy)
2. [Core Tenets of the Design System](#core-tenets-of-the-design-system)
3. [Typography and Visual Hierarchy](#typography-and-visual-hierarchy)
4. [Color and Contrast Strategy](#color-and-contrast-strategy)
5. [Layout and Structural Decisions](#layout-and-structural-decisions)
6. [Accessibility Considerations](#accessibility-considerations)

## Neubrutalist Design Philosophy

The cv-ai project implements a neubrutalist design philosophy that emphasizes raw functionality, minimal abstraction, and typographic clarity. This approach prioritizes content and machine readability over decorative aesthetics, aligning with the project's dual purpose as both a human-readable portfolio and a machine-consumable knowledge base. The design deliberately embraces visual austerity, eliminating graphical embellishments in favor of structural honesty and functional transparency.

This philosophy manifests through the consistent use of monospaced fonts, high-contrast color schemes, deliberate whitespace, and the absence of decorative elements. The implementation focuses on content-first presentation, where information architecture takes precedence over visual flair. This creates a direct, unmediated experience between the user and the content, reducing cognitive load and enhancing information retrieval efficiency.

**Section sources**
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md#L1-L90)
- [main.css](file://assets/main.css#L0-L799)

## Core Tenets of the Design System

The design system adheres to four foundational principles that guide all visual and structural decisions. First, **clarity over ornamentation** ensures that contrast, spacing, and hierarchy serve as the primary tools for visual organization, replacing decorative elements. Second, **guided momentum** leads visitors through the narrative using consistent grids and meaningful accent color usage to create a predictable user journey.

Third, **calm confidence** is achieved through soft surfaces, measured elevation, and balanced typography that convey expertise without hype. This principle rejects aggressive marketing aesthetics in favor of professional credibility. Fourth, **accessible by default** maintains WCAG AA contrast standards, provides large tap targets, and ensures keyboard-friendly focus states, making the interface usable for diverse audiences.

These tenets collectively support the neubrutalist approach by eliminating unnecessary visual noise while keeping key calls-to-action obvious and information hierarchies clear. The design system documentation explicitly prioritizes reusability of design tokens and existing grid utilities, reinforcing the minimalist philosophy.

**Section sources**
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md#L6-L17)
- [main.css](file://assets/main.css#L0-L799)

## Typography and Visual Hierarchy

Typography serves as the primary vehicle for establishing visual hierarchy and ensuring readability. The system employs a deliberate typographic scale using CSS clamp() functions to ensure responsive legibility across devices. Headings use the Manrope typeface with carefully calibrated sizes: h1 at clamp(2.65rem, 4vw, 3.35rem), h2 at clamp(2rem, 3.2vw, 2.55rem), and h3 at clamp(1.35rem, 2.4vw, 1.65rem), creating a clear information hierarchy.

Body text uses DM Sans at 1.08rem with a 1.72 line-height, optimized for extended reading. The design enforces a maximum of approximately 65 characters per line to enhance readability. Kicker/eyebrow text appears in uppercase with 0.14em letter spacing, creating distinctive section introductions without relying on graphical elements.

Monospaced presentation is implied through the consistent use of fixed-width spacing and the absence of decorative typography. The system avoids italics, text shadows, and other typographic flourishes, maintaining a clean, functional aesthetic that prioritizes content over form.

**Section sources**
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md#L29-L40)
- [main.css](file://assets/main.css#L45-L85)

## Color and Contrast Strategy

The color system implements a high-contrast palette that enhances readability while maintaining visual interest through strategic accent usage. The primary color variables establish a warm, parchment-like background (`--color-page: #f9f5d6`) paired with dark ink text (`--color-ink: #161616`), creating optimal contrast for reading. Secondary text appears in softer ink tones (`--color-ink-soft: #383838`), establishing clear visual hierarchy.

Accent colors serve functional purposes rather than decorative ones. The primary accent (`--color-accent: #ffcc00`) highlights interactive elements, while border colors (`--color-border: #101010`) define component boundaries. The system uses yellow highlights (`--color-highlight: #ffe032`) for text selection, maintaining visibility without overwhelming the content.

This limited palette eliminates gradients, patterns, and decorative color usage, adhering to the neubrutalist principle of visual austerity. The intentional color choices support both human readability and machine parsing, as the consistent use of semantic color variables makes the design system predictable and analyzable.

**Section sources**
- [main.css](file://assets/main.css#L1-L44)
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md#L19-L28)

## Layout and Structural Decisions

Layout decisions reflect the neubrutalist emphasis on functional structure over decorative arrangement. The page container uses a max-width of min(1120px, 92vw), creating a focused reading experience that prevents text lines from becoming too long. Section spacing employs a comprehensive scale from `--space-3xs` (0.3rem) to `--space-2xl` (4.5rem), establishing consistent vertical rhythm.

Cards and content containers use the `.neub-card` class with 3px solid borders, generous padding, and subtle box shadows that create a "stamped" effect rather than attempting realistic elevation. The hover interaction translates the card slightly upward with an intensified shadow, providing feedback without animation extravagance.

Grid systems employ auto-fit with minmax() functions to create responsive layouts that adapt gracefully across viewports. The hero section uses a two-column grid that collapses to single-column on smaller screens, ensuring content remains accessible. Social links and statistics use auto-fit grids with minimum column widths, maintaining usability while maximizing space efficiency.

**Section sources**
- [main.css](file://assets/main.css#L87-L150)
- [hero.html](file://_includes/sections/hero.html#L1-L55)
- [social-line.html](file://_includes/components/social-line.html#L1-L41)

## Accessibility Considerations

The design system incorporates accessibility as a fundamental requirement rather than an afterthought. The color palette maintains WCAG AA contrast standards, with primary text on background achieving sufficient contrast ratios. Focus states use `:focus-visible` to provide a 3px accent outline with offset, ensuring keyboard navigation is clearly visible without affecting mouse users.

Interactive elements have minimum touch targets of 44px, meeting mobile accessibility requirements. The system respects `prefers-reduced-motion` by disabling animations and transitions when users have indicated sensitivity to motion. Semantic HTML is reinforced through the use of proper heading hierarchy and ARIA labels for interactive elements.

While the minimalist approach enhances screen reader compatibility by reducing non-essential content, the heavy reliance on visual contrast could present challenges for users with certain visual impairments. The absence of decorative cues means all information must be conveyed through text and structure, which benefits machine readability but requires careful consideration of alternative presentation methods.

**Section sources**
- [DESIGN-SYSTEM.md](file://DESIGN-SYSTEM.md#L80-L88)
- [main.css](file://assets/main.css#L15-L25)
- [default.html](file://_layouts/default.html#L1-L47)