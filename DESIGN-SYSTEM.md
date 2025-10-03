# Runway Design System

A light-weight design language for Dzmitryi Kharlanau's GitHub Pages site. Runway focuses on clarity, professional credibility, and calm confidence--reducing visual noise while keeping key calls-to-action obvious.

## Principles
- **Clarity over ornamentation:** Use contrast, spacing, and hierarchy instead of heavy decoration.
- **Guided momentum:** Lead visitors through the narrative with consistent grids and meaningful accent color usage.
- **Calm confidence:** Favor soft surfaces, measured elevation, and balanced typography to convey expertise without hype.
- **Accessible by default:** Maintain AA contrast, large tap targets, and keyboard-friendly focus states.

## Foundations
### Color Palette
| Token | Hex | Primary Use |
| --- | --- | --- |
| `--color-page` | `#f3f6fb` | Application background, keeps content floating on a light mist. |
| `--color-surface` | `#ffffff` | Core surfaces such as hero, cards, footer content blocks. |
| `--color-surface-muted` | `#eef2ff` | Secondary surfaces (stat tiles, supporting cards). |
| `--color-border` | `#d6deeb` | Base borders, dividers, card outlines. |
| `--color-border-strong` | `#b8c5d9` | Focused dividers or hover states that need a touch more contrast. |
| `--color-text` | `#0f172a` | Primary copy and heading color. |
| `--color-text-secondary` | `#475569` | Long-form body copy, supportive text. |
| `--color-text-soft` | `#64748b` | Captions, meta data, helper text. |
| `--color-accent` | `#2563eb` | Primary accent for CTAs and interactive states. |
| `--color-accent-strong` | `#1e4fd6` | Hover/active accent and strong highlights. |
| `--color-accent-soft` | `#e3edff` | Accent tint backgrounds, tags, subtle highlights. |
| `--color-accent-on` | `#f8fafc` | Text/icon color when placed on accent backgrounds. |

### Typography
- **Typeface:** `--font-sans` ? "Manrope" fallback stack.
- **Scale:**
  - `h1`: clamp(2.4rem, 5vw, 3rem), bold, -0.01em letter spacing.
  - `h2`: clamp(1.9rem, 4vw, 2.4rem), bold.
  - `h3`: clamp(1.3rem, 2.5vw, 1.55rem), semi-bold.
  - **Body large:** 18px base with 1.65 line-height.
  - **Kicker/eyebrow:** 0.75rem, uppercase, 0.08em letter spacing, accent color.
- **Usage notes:** Keep body copy to max ~65 characters per line, rely on typography + spacing for flow.

### Spacing & Layout
- **Scale:** `--space-2xs` 0.25rem, `--space-xs` 0.5rem, `--space-sm` 0.75rem, `--space-md` 1rem, `--space-lg` 1.5rem, `--space-xl` 2rem, `--space-2xl` 3rem, `--space-3xl` 4.5rem.
- **Container:** `.wrapper` locks content to `min(1080px, 92vw)`.
- **Vertical rhythm:** `.page-content` spaces sections with `clamp(2.5rem, 6vw, 4rem)` and generous padding top/bottom.
- **Grids:** Cards default to responsive `repeat(auto-fit, minmax(220px, 1fr))`, adapting down to single column below 600px.

### Shape & Elevation
- **Radii:** `--radius-sm` 12px, `--radius-md` 16px, `--radius-lg` 22px.
- **Elevation:**
  - `--shadow-subtle`: 0 6px 18px rgba(15, 23, 42, 0.05) for section containers.
  - `--shadow-soft`: 0 10px 30px rgba(15, 23, 42, 0.08) reserved for hover states or key emphasis.
- **Philosophy:** One layer of elevation at a time. Use border + tint before introducing shadows.

## Components & Patterns
### Content Containers
- `.content-box`: Primary section wrapper; uses `--color-surface`, border, `--radius-lg`, and `--shadow-subtle`.
- Sub-cards (`.value-card`, `.program-card`, `.approach-card`, `.presence-card`) balance tints and borders to differentiate hierarchy without stacking shadows.

### Hero & Stats
- `.hero`: Two-column grid with responsive collapse at 900px.
- `.avatar`: Padded frame with border; no drop shadow to keep portrait crisp.
- `.hero-stats`: Auto-fit grid; each `.stat-card` uses the muted surface tint and uppercase label treatment.

### Buttons & Links
- `.cta`: Primary pill using `--color-accent` with hover to `--color-accent-strong`.
- `.cta.secondary`: Transparent fill, accent border, soft-hover tint.
- Focus states rely on `:focus-visible` outline for both keyboard and mouse accessibility.

### Tags & Metadata
- `.tag`: Accent-soft chip, medium weight text, rounded to 999px.
- `.section-kicker`: Re-usable eyebrow style to introduce sections.

### Cards & Grids
- `.impact-card`: Solid surface with accent border; no gradients.
- `.program-card` lists use disc bullets with comfortable line-height.
- `.presence-card`: Largest radius to establish final call-to-action area.

### Social Actions & Footer
- `.social-button`: Circular outline buttons that lift slightly on hover.
- `.site-footer`: Deep navy (`#0f172a`) background, light text, and accent links for clear contrast.

## Accessibility & Motion
- `:focus-visible` provides a 3px accent outline with offset.
- All accent-on-white combinations meet WCAG AA (contrast ~ 5.6:1).
- Hover transitions use `--transition-all` (0.2s ease) and avoid large transforms; vertical shifts capped at 2px.
- Minimum touch target: 44px for social buttons, >44px width for CTAs on mobile.

## Extending the System
1. Re-use design tokens (`:root` custom properties) when adding new patterns.
2. Prefer existing grid utilities before crafting new layouts.
3. Keep shadows optional--introduce additional elevation only when a surface needs clear priority.
4. Document any new component variants in this file to maintain a living system.

