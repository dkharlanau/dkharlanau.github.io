# Runway Design System

A lightweight design language for Dzmitryi Kharlanau's GitHub Pages site. Runway focuses on clarity, professional credibility, and calm confidence--reducing visual noise while keeping key calls-to-action obvious.

## Principles
- **Clarity over ornamentation:** Use contrast, spacing, and hierarchy instead of heavy decoration.
- **Guided momentum:** Lead visitors through the narrative with consistent grids and meaningful accent color usage.
- **Calm confidence:** Favor soft surfaces, measured elevation, and balanced typography to convey expertise without hype.
- **Accessible by default:** Maintain AA contrast, large tap targets, and keyboard-friendly focus states.

## Foundations
### Color Palette
| Token | Hex | Primary Use |
| --- | --- | --- |
| `--color-page` | `#f4f6f9` | Site background, crisp light canvas. |
| `--color-card` | `#ffffff` | Core surfaces such as hero, cards, and footer content blocks. |
| `--color-card-alt` | `#eef2ff` | Secondary surfaces (stat tiles, supporting cards). |
| `--color-border` | `rgba(15, 23, 42, 0.08)` | Subtle dividers and container outlines. |
| `--color-border-soft` | `rgba(15, 23, 42, 0.06)` | Quiet separators and list dividers. |
| `--color-ink` | `#0f172a` | Primary copy and heading color. |
| `--color-ink-soft` | `#334155` | Long-form body copy, supportive text. |
| `--color-ink-muted` | `#64748b` | Captions, metadata, helper text. |
| `--color-accent` | `#2563eb` | Primary accent for CTAs and interactive states. |
| `--color-accent-strong` | `#1d4ed8` | Hover/active accent and strong highlights. |
| `--color-accent-soft` | `#e6efff` | Accent tint backgrounds, tags, subtle highlights. |

### Typography
- **Typeface:** Manrope for display and body.
- **Scale:**
  - `h1`: clamp(2.65rem, 4vw, 3.35rem), semi-bold, -0.01em letter spacing.
  - `h2`: clamp(2rem, 3.2vw, 2.55rem), semi-bold.
  - `h3`: clamp(1.35rem, 2.4vw, 1.65rem), semi-bold.
  - **Body:** clamp(1rem, 0.9vw + 0.9rem, 1.08rem) with 1.7+ line height.
  - **Kicker/eyebrow:** 0.9rem, uppercase, 0.14em letter spacing, muted color.
- **Usage notes:** Keep body copy to max ~65 characters per line, rely on typography + spacing for flow.

### Spacing & Layout
- **Scale:** `--space-3xs` 0.3rem, `--space-2xs` 0.45rem, `--space-xs` 0.65rem, `--space-sm` 0.9rem, `--space-md` 1.25rem, `--space-lg` 2rem, `--space-xl` 3rem, `--space-2xl` 4.5rem.
- **Container:** `.wrapper` and `.page-content` use a `1120px` max width with fluid horizontal padding.
- **Vertical rhythm:** `.page-content` spaces sections with generous top/bottom padding, scaled per breakpoint.
- **Grids:** Cards default to responsive `repeat(auto-fit, minmax(220px, 1fr))`, adapting down to single column below 600px.

### Shape & Elevation
- **Radii:** 12px to 20px, with larger sections using 20px for a calm, modern profile.
- **Elevation:** Soft, directional shadows only (no hard borders). Default `--shadow-card` and `--shadow-card-soft` provide a subtle lift without heavy outlines.
- **Philosophy:** Prefer light shadows and tinted surfaces over strong borders; keep elevation consistent across sections.
- **Material-inspired elevation:** Use `--shadow-elev-1`, `--shadow-elev-2`, and `--shadow-elev-3` for small, medium, and pronounced emphasis while staying understated.

## Components & Patterns
### Content Containers
- `.content-box`: Primary section wrapper; uses `--color-surface`, border, `--radius-lg`, and `--shadow-subtle`.
- Sub-cards (`.value-card`, `.program-card`, `.approach-card`, `.presence-card`) balance tints and borders to differentiate hierarchy without stacking shadows.
- `.section-shell`: Material-inspired surface for blocks inside a page section. Use `.section-shell--tint` for a quiet alternate surface and `.section-shell--flat` when you need a section without elevation.

### Hero & Stats
- `.hero`: Two-column grid with responsive collapse at 900px.
- `.avatar`: Padded frame with border; no drop shadow to keep portrait crisp.
- `.hero-stats`: Auto-fit grid; each `.stat-card` uses the muted surface tint and uppercase label treatment.

### Buttons & Links
- `.cta`: Primary pill using `--color-accent` with hover to `--color-accent-strong`.
- `.cta.secondary`: Transparent fill, accent border, soft-hover tint.
- Focus states rely on `:focus-visible` outline for both keyboard and mouse accessibility.
- `.link`: Emphasized inline link with animated underline; use `.link--muted` for low-emphasis text links.
- `.link--pill`: Chip-like link for compact navigation and tag-style actions.
- `.link-group`: Wrap multiple links consistently; pairs well with `.section-actions`.

### Tags & Metadata
- `.tag`: Accent-soft chip, medium weight text, rounded to 999px.
- `.section-kicker`: Re-usable eyebrow style to introduce sections.
- `.breadcrumbs`: Navigation trail for hierarchical pages. Use an ordered list and `aria-current="page"` for the current location.

### Dividers
- `.divider`: Default 1px divider with spacing baked in.
- `.divider--strong`: Higher-contrast separator for key breaks.
- `.divider--accent`: Accent-tinted divider for emphasis.
- `.divider--vertical`: Vertical divider for horizontal stacks.

### Cards & Grids
- `.impact-card`: Solid surface with accent border; no gradients.
- `.program-card` lists use disc bullets with comfortable line-height.
- `.presence-card`: Largest radius to establish final call-to-action area.

### Social Actions & Footer
- `.social-icon`: Circular outline buttons with soft elevation on hover.
- `.site-footer`: Light surface with subtle divider to keep the page calm and professional.

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

## Usage Snippets
### Section Shell + Actions
```html
<section class="section">
  <header class="section-header">
    <div class="section-header__meta">
      <span class="eyebrow">Overview</span>
      <h2 class="section-header__title">System Health</h2>
      <p class="section-header__subtitle">Last updated 2 minutes ago</p>
    </div>
    <div class="section-actions">
      <a class="link link--pill" href="#">Export</a>
      <a class="button button--primary" href="#">Create report</a>
    </div>
  </header>
  <div class="section-shell">
    <p class="lead">Material-inspired surface for grouped content.</p>
  </div>
</section>
```

### Breadcrumbs
```html
<nav class="breadcrumbs" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/notes">Notes</a></li>
    <li><span aria-current="page">Design System</span></li>
  </ol>
</nav>
```

### Dividers
```html
<hr class="divider" />
<hr class="divider divider--strong" />
<div class="divider divider--vertical"></div>
```
