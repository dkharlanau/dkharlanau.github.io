# Repository social-preview contract

The flagship repositories use a shared 1280×640 visual family so a link identifies both the individual product and the wider open-source system. The preview is a navigation aid, not adoption evidence.

## Source and output

Each participating repository owns two files:

- `assets/social-preview.json` — exact copy, palette, motif, dimensions, and claim boundary;
- `assets/social-preview.png` — deterministic raster export uploaded through the repository's GitHub settings.

The renderer lives in this repository at `scripts/render_repository_social_preview.py`. It rejects unknown motifs, malformed colors, incorrect dimensions, and copy that exceeds the bounded layout. The output must remain under 1 MB.

```bash
python3 scripts/render_repository_social_preview.py \
  ../dkharlanau-public/enterprise-architecture-composer/assets/social-preview.json \
  --output ../dkharlanau-public/enterprise-architecture-composer/assets/social-preview.png
```

Use `--check` in a portfolio review to confirm that a committed PNG still matches its source configuration.

## Visual and claim rules

- Keep the product title and repository path exact.
- State one implemented product purpose, not a future claim.
- Do not show stars, users, adoption, certifications, SAP endorsement, or compatibility beyond what the repository proves.
- Keep diagrams schematic and synthetic. Do not reuse client screenshots, vendor logos, or third-party assets.
- Preserve the product-specific accent while retaining the shared typography, margins, author line, and diagram frame.
- Review the rendered PNG at full size before upload; a successful render does not prove that the composition is readable.

## Current flagship surfaces

- Enterprise design: Enterprise Architecture Composer and Visual Workbench.
- Transformation assurance: Project Evidence Graph.
- SAP and practical AI: SAP Agentic Operations and Signal to Insight.

The supporting repositories remain visible in the portfolio map, but a separate preview is not required merely to make every repository look equal.

## Publication check

After uploading an image in GitHub repository settings:

1. reopen the repository settings and confirm that the preview is present;
2. verify the committed source and PNG match the repository's current `main` branch;
3. keep the image solid-background and 1280×640 for predictable rendering on light and dark platforms;
4. record no adoption claim from the presence of a preview alone.
