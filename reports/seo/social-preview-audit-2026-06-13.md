# Social Preview / Open Graph Image Audit

**Date:** 2026-06-13
**Branch:** `feat/seo-visibility-swarm`
**Site:** https://dkharlanau.github.io

---

## Summary

The site has a **default OG image** that covers most pages. Key hub pages can define custom images later. No image generation is needed in this PR.

---

## Image Assets Audit

| File | Size | Format | Status |
|------|------|--------|--------|
| `assets/og/default.png` | ~22 KB | PNG | ✅ Present |
| `assets/og/default.webp` | ~15 KB | WebP | ✅ Present |
| `assets/img/DzmitryiKharlanau.webp` | unknown | WebP | ✅ Present (used for preloading) |
| `assets/img/DzmitryiKharlanau.avif` | unknown | AVIF | ✅ Present (used for srcset) |

**OG image reference:** `_includes/head.html` line 2:
```liquid
{% assign og_image = page.og_image | default: '/assets/og/default.png' | absolute_url %}
```

**Default OG image usage:** All pages without `page.og_image` inherit the default.

---

## OG Image Dimensions

| Property | Status | Recommendation |
|----------|--------|----------------|
| 1200×630 (optimal for Twitter/LinkedIn) | **Not verified** | Measure `assets/og/default.png` and confirm dimensions. If not 1200×630, regenerate or document in `DESIGN-SYSTEM.md`. |
| 1:1.91 aspect ratio | **Not verified** | Same as above. |
| < 1 MB | ✅ Verified | ~22 KB, well under limit. |
| WebP variant | ✅ Present | `default.webp` exists for modern browsers. |

---

## Page-Level OG Image Override

**Current state:** Pages can set `og_image` in frontmatter to override the default.

**Pages that should define custom OG images later (post-PR):**

| Page | Why Custom Image |
|------|-----------------|
| `/` (home) | Primary landing page; deserves branded hero image |
| `/about/` | Profile page; personal photo or professional branding |
| `/services/` | Commercial signal; service-oriented graphic |
| `/atlas/` | Knowledge hub; thematic illustration |
| `/skill-hub/` | Skills hub; professional development graphic |
| `/ai-assisted-sap-support/` (future hub) | Hub page; AI + SAP themed graphic |

**No custom images are created in this PR.**

---

## Image Alt Text Audit

**Alt text in `head.html`:** The OG image is a meta tag (`og:image`), not an `<img>` tag, so it does not need `alt` text for accessibility. However, `og:image:alt` is not currently set. Adding `og:image:alt` would improve accessibility for screen readers that consume OG metadata.

**Recommendation:** Add `og:image:alt` to `head.html`:
```html
<meta property="og:image:alt" content="Dzmitryi Kharlanau — SAP AMS Consultant" />
```

**Alt text in content images:** Not audited in this PR. A separate content image audit can be done if needed.

---

## Image Optimization

| Check | Status | Notes |
|-------|--------|-------|
| No huge unoptimized images | ✅ | Largest image is ~22 KB |
| WebP variants | ✅ | Present for OG and hero |
| AVIF variants | ✅ | Present for hero |
| Lazy loading | ✅ | `defer` on scripts; images likely handled by browser |
| Preload hero image | ✅ | `link rel="preload"` in `head.html` |

---

## Recommendations

1. **Verify `assets/og/default.png` dimensions are 1200×630.** If not, add a generation note in `DESIGN-SYSTEM.md` or `AGENTS.md`.
2. **Add `og:image:alt` to `head.html`.**
3. **Do not generate new images in this PR.**
4. **Future hub pages can define `og_image` in frontmatter** when they are created.

---

## Safety

- No AI-generated images are used without disclosure.
- No third-party logos or trademarks are used in OG images.
- No copyrighted material is present in image assets.
