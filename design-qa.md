---
published: false
---

# Services Constraint Canvas — design QA

**Comparison target**

- Source visual truth: `/Users/dzmitryikharlanau/.codex/generated_images/019f9adb-f327-7253-ab65-18c43c691142/exec-50fed1bc-8dd8-4c80-8c7a-0b167315127a.png`
- Rendered implementation: `http://127.0.0.1:4010/services/`
- Implementation capture: `/tmp/services-constraint-canvas-desktop.png`
- Combined full-view comparison: `/tmp/services-constraint-canvas-comparison.png`
- Viewport and state: desktop `1440 × 1024` CSS px, initial AMS service path, light theme.
- Density normalization: source `1536 × 1024` px was resized to `1425 × 950` px; implementation capture is `1425 × 1013` px at device scale factor 1 (scrollbar excluded). The combined comparison preserves the two visible regions at the same rendered width.

**Full-view comparison evidence**

The reference and rendered top-of-page are combined in the comparison image above. Both use the same constraint-first hierarchy: an assertive left-hand proposition, a five-path operational signal map, restrained warm-neutral field, dark ink, one orange operational accent, and a bounded calculator beginning immediately after the hero. The production page intentionally retains the site’s existing global navigation and its actual service URLs, while bringing the selected direction’s hierarchy, scale, and interaction model into the Jekyll design system.

**Focused region comparison**

Focused review covered the hero type and action block, service signal map and selected state, calculator controls and recommendation, and generated operations photographs. A separate mobile capture at `390 × 844` CSS px is available at `/tmp/services-constraint-canvas-mobile.png`; it shows the headline, action hierarchy, and mobile navigation without clipping or horizontal overflow.

**Required fidelity surfaces**

- Fonts and typography: the existing site’s display/sans families are used consistently. The production headline is deliberately larger and heavier than the source mock to fit the site’s brand system, with no clipping or unintended wrapping at desktop, tablet, or mobile sizes.
- Spacing and layout rhythm: the inherited top padding that created an excessive blank band was removed. The hero now begins directly below the fixed header and preserves a generous but purposeful reading rhythm.
- Colors and visual tokens: warm paper, deep ink, muted rule lines, and orange-red operational accents map to the selected visual direction without gradients or glass effects.
- Image quality and asset fidelity: three purpose-generated, logo-free WebP photographs are correctly cropped, accessible, and served by the static preview (HTTP 200). They support real operations, data, and workshop content rather than acting as generic decoration.
- Copy and content: every published service URL, front matter field, JSON-LD block, and existing service route remains intact. The new service index copy is constraint-led and covers AMS, data, logistics, integration/automation, and practical AI.

**Findings**

- [Resolved P1] Interactive map visual selection did not update the detail panel.
  Location: `services/index.md`, service map panel.
  Evidence: the initial interaction pass selected “Master data” but kept the AMS heading; browser error showed the service panel binding was null.
  Fix: added the missing `data-service-detail` binding, rebuilt the site, and retested calculator and tab selection. The post-fix state updates the selected tab, `aria-labelledby`, detail panel content, recommended path, and canonical service URL together.

- [Resolved P2] Hero began after an unnecessary inherited content offset.
  Location: `assets/services-canvas.css`.
  Evidence: the first desktop capture placed the hero at 144 px rather than immediately below the 72 px header.
  Fix: reset the services page content padding only. The revised capture places the hero at 72 px with no horizontal overflow.

**Open questions**

None for this service-index implementation. Individual canonical service pages retain their existing content and URLs, as required; they can receive the same visual treatment in a separate, route-by-route pass.

**Implementation checklist**

- [x] Preserve service front matter, JSON-LD, public service URLs, and outbound contact behavior.
- [x] Implement interactive service map and constraint calculator with keyboard-aware tabs and live recommendation updates.
- [x] Add responsive layouts for desktop, tablet, and mobile; confirm no horizontal overflow at 1440, 768, and 390 px.
- [x] Verify generated operational imagery resolves in the local build.
- [x] Capture and compare selected visual target and revised desktop implementation.

**Follow-up polish**

- [P3] If the individual service detail pages are later redesigned, reuse the service-path markers and practical AI boundary treatment while retaining each page’s established article content.

final result: passed
