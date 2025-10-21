# CV AI Architecture

This site is a Jekyll project tuned for fast storytelling iterations, structured data reuse, and AI-friendly exports.

## System overview

- **Static site generator:** Jekyll 4 (GitHub Pages compatible).
- **Design system:** `assets/main.css` implements the light Neubrutalist theme with section primitives (`.section`, `.neub-card`, `.hero-*`, `.note-*`).
- **Content model:** Declarative data in `_data/`, component partials in `_includes/`, document types via collections.
- **AI surface:** JSON mirrors of major datasets in `/ai` for agent handoff or prompt grounding.

## Content pipeline

### Homepage
- Section order is defined in `index.md` (`sections` front matter array).
- Copy and structure data live in `_data/home.yml`.
- Rendering is handled by `_includes/page-builder.html`, which routes to `_includes/sections/*.html` partials (e.g. `signals.html` for the social/channel strip and `llm-profiles.html` for machine-readable downloads).
- Adjust styling or layout in `assets/main.css`; each partial uses consistent class hooks.
- Reusable UI components (such as the social line) sit in `_includes/components/` and are styled with `.social-*` helpers.

### Resume
- `_data/resume.yml` powers both `cv/index.html` and `ai/resume.json`.
- Modify data once to update markup, downloads, and structured exports.

### Notes collection
- `_notes/` contains individual notes (`_notes/*.md`).
- Collection defaults (`_config.yml`) apply the `_layouts/note.html` layout and ensure clean permalinks (`/notes/:slug/`).
- `notes/index.md` lists all notes using `site.notes`, styled via `.notes-landing` and `.note-card` classes.
- To add a new note, drop a Markdown file in `_notes/` with at least `title`, `date`, and optional `tags`, `summary`, `subtitle`.

### Standalone pages
- `/changelog/` reads `_data/changelog.yml` through `changelog.html` to provide a release snapshot view.
- The `/legal/` directory houses evergreen policies (code of conduct, terms of engagement, privacy notice, professional disclosure, responsible AI statement, accessibility statement) authored as standalone Markdown pages.

## AI & automation

- `ai/resume.json`, `ai/resume.yml`, and `ai/home.json` expose resume and homepage data for copilots or APIs.
- Add further exports by creating files with `layout: null` and serialising data structures using `| jsonify`.
- `LLM.txt` remains the long-form system profile surface, and the homepage `llm-profiles` section links to all machine-readable variants.

## SEO & metadata

- `_includes/seo/structured-data.html` emits Person, WebSite, Breadcrumb, and Article JSON-LD based on the current page context.
- `_config.yml` provides language, author, and Twitter metadata for `jekyll-seo-tag`.
- Social profiles are centralised in `_data/social.yml` and reused in both UI components and structured data.

## Styling guidelines

- Custom properties in `:root` control typography, spacing, and colour tokens.
- Components share the `neub-card` shell for consistent shadow and border language.
- Responsive behaviour is handled with modern CSS (grid, clamp) and media queries at 960px/720px/540px breakpoints.
- When introducing new components, prefer extending existing utility classes (e.g., `.section-heading`, `.chip-list`).

## Development workflow

1. Update or add data in `_data/` for repeatable content.
2. Compose/reuse partials in `_includes/sections` or create new ones in `_includes/components` as needed.
3. Style new primitives in `assets/main.css`, keeping tokens centralised.
4. Run `bundle exec jekyll serve` locally (after adding a Gemfile) to preview.
5. For AI surfaces, mirror any new structures in `/ai` with JSON exports.

## Future extensions

- Define additional collections (e.g., `case_studies`, `playbooks`) using the same pattern as notes.
- Introduce CMS integration by mapping `_data/home.yml` to a headless backend if needed.
- Expand structured data with more Schema.org entities (Projects, Articles) as content grows.
