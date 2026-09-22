# Editorial image strategy

Images on dkharlanau.github.io are explanatory assets, not page decoration.

## Visual language

Use a restrained red/blue conceptual system:

- blue = route, evidence, confirmed path, action or controlled state;
- red = tension, risk, mismatch, failure boundary or trade-off;
- neutral paper/ink = context.

Use red/blue only when the contrast improves comprehension or recall. A page with no useful visual comparison should have no image.

## Page-type strategy

| Page type | Default image treatment |
| --- | --- |
| Homepage | At most one identity/overview visual when it explains the two main paths; no decorative hero required |
| Atlas diagnostic | One evidence map, comparison or process diagram when it shortens diagnosis |
| Long-form article | One conceptual cover/support image plus occasional diagrams only at real conceptual transitions |
| Learning / assessment | Diagrams, memory anchors and comparison visuals; avoid decorative covers |
| Services | Workflow/problem visual only when it clarifies the operating model |
| Category / archive | Usually no image; prioritise scanning and route labels |
| Search | No decorative image |
| Data / integration topics | Prefer process, boundary and correlation diagrams |
| Before/after or trade-off topics | Prefer controlled red/blue comparison treatment |

## Current representative image set

### Incident triage evidence matrix
- desktop: `assets/img/articles/incident-triage-evidence-matrix.webp`
- mobile: `assets/img/articles/incident-triage-evidence-matrix-mobile.webp`
- target page: `/atlas/diagnostics/sap-incident-triage-diagnostics/`
- purpose: turn vague incident intake into a memorable evidence sequence
- desktop ratio: 3:2
- mobile ratio: 2:3
- placement: inside the reading flow before the detailed diagnostic matrix
- attribution: `Author: Dzmitryi Kharlanau`

### Master-data diagnostic layers matrix
- desktop: `assets/img/articles/master-data-diagnostic-layers-matrix.webp`
- mobile: `assets/img/articles/master-data-diagnostic-layers-matrix-mobile.webp`
- target page: `/atlas/diagnostics/sap-master-data-diagnostics-hub/`
- purpose: separate governance, identity/validation and operational-use evidence before changing data or replication
- desktop ratio: 3:2
- mobile ratio: 2:3
- placement: after the core idea and before the symptom matrix
- attribution: `Author: Dzmitryi Kharlanau`

The existing registry in `_data/article_visuals.yml` is the canonical place for filenames, dimensions, alt text, caption, author credit and generation provenance.

## Art direction template

For a new visual, define these fields before generating or drawing it:

- target page and exact concept that needs reinforcement;
- reader question the visual should answer;
- visual type: evidence map, process flow, comparison, boundary map or technical composition;
- red/blue semantic role;
- desktop and, when needed, mobile composition;
- target aspect ratio and dimensions;
- meaningful filename;
- concise alt text that states the information, not the style;
- caption explaining how to read the figure;
- attribution `Author: Dzmitryi Kharlanau`.

Do not generate an image until the visual has a concrete information job.

## Delivery rules

- Prefer WebP and/or AVIF; WebP is the current baseline.
- Store article visuals under `assets/img/articles/`.
- Use responsive `picture` sources where a vertical crop materially improves mobile comprehension.
- Declare width and height.
- Lazy-load article-body visuals; only true above-the-fold hero media should be eager.
- Keep filenames semantic and stable.
- Do not place essential text only inside an image.
- Do not use generic stock photography, office-people imagery, glossy AI motifs, decorative blobs or heavy 3D.
- Do not add an image merely to fill whitespace.

## Attribution

The registry uses the exact credit string:

`Author: Dzmitryi Kharlanau`

The shared article figure exposes that credit as machine-readable ImageObject metadata. The visible caption stays focused on comprehension; attribution is not repeated visually on every page. Generation provenance is stored separately in the registry.
