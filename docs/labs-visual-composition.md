# Labs visual composition

Use the shared Labs patterns before adding page-specific CSS.

- Put the page opening in `.research-canvas__hero` and major groups in `.research-canvas__inventory`.
- Give each inventory section one eyebrow, one `h2`, and an optional short introduction.
- Use `.research-canvas__boundary` for constraints, warnings, and architecture boundaries.
- Use the existing ECG grids for comparable entities and decision groups; do not add fixed card heights.
- Wrap wide tables in `.research-canvas__table-wrap` and add a useful accessible label when the wrapper is focusable.
- Keep flows in `.ecg-rail__branch` or `.ecg-trace__path`; both retain readable node widths and scroll locally on narrow screens.
- Keep code in semantic `pre > code`. Inline identifiers belong in `code` outside `pre`.
- Do not add route-specific width, heading-size, table-overflow, or mobile-grid fixes unless the shared system cannot express the layout.

Check at 1280px, 1024px, 768px, and 390px. The page itself must not scroll horizontally; wide tables, code, and technical flows may scroll inside their own region.
