# Homepage One-Pager V2 (Atlas Language) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Restyle the EN homepage one-pager into the `/atlas/` design language (Evidence Atlas layer), with a minimal landing fold, no menu header on the homepage, and a redesigned global footer.

**Architecture:** Reuse the existing atlas CSS classes (`atlas-hero`, `section-heading`, `eyebrow`, `lead`, `atlas-card-grid`, `section-shell--flat`, `button`) instead of bespoke `hc-` layout CSS. `assets/home-canvas.css` shrinks to homepage-only extras (identity line, canvas controls, ruled lists); `assets/home-canvas.js` shrinks to the constraint-canvas widget. Header suppression via `hide_global_header` frontmatter; footer via rewritten `_includes/footer.html` + new global `assets/site-footer.css`.

**Tech Stack:** Jekyll 3.10 / Liquid, vanilla CSS/JS, pytest.

**Context:** V1 (Tasks 1–6, commits up to `82e0e4b` on `feat/home-onepager`) built the one-pager with bespoke `hc-` styling. This plan replaces v1's visual layer per the spec addendum in `docs/superpowers/specs/2026-07-26-homepage-onepager-design.md` ("V2 Revision").

## Global Constraints

- Do NOT modify locale homepages, old section partials (hero.html, analysis-problem.html, etc.), `_includes/header.html`, or `assets/evidence-atlas.css` (another work stream's file).
- `_layouts/default.html` and `_includes/head.html` carry unrelated uncommitted changes from the design stream — preserve them exactly; additive edits only. They will be staged along with your hunks; that is accepted (note it in reports).
- Atlas-card indices ("ROUTE / 01") come from CSS counters in `evidence-atlas.css:594-610` — do not add index markup to cards.
- No new dependencies; no invented links or emails.
- Commit after every task; never commit `_site/` or `.superpowers/`.

---

### Task 8: V2 markup, data, CSS, JS

**Files:**
- Modify: `tests/test_home_onepager.py` (full rewrite)
- Modify: `_data/home.yml` (add 2 keys under `home_hero`)
- Create: `_includes/sections/hero-atlas.html`, `priorities-grid.html`, `steps-ruled.html`, `ai-principles.html`, `ideas-list.html`
- Modify: `_includes/sections/constraint-canvas-home.html`, `_includes/sections/cta-bar.html` (full rewrites)
- Delete: `_includes/sections/hero-canvas.html`, `journey-map.html`, `photo-strip.html`, `tri-columns.html`
- Modify: `_includes/page-builder.html` (replace v1 whens)
- Modify: `index.md` (sections list)
- Modify: `assets/home-canvas.css`, `assets/home-canvas.js` (full rewrites)

**Interfaces:**
- Consumes: `home_hero` (+ new `kicker`, `secondary_actions`), `home_journey`, `home_canvas`, `home_steps`, `home_ai_principles`, `home_cta` from `_data/home.yml`; `site.data.home_languages` (entries: `code`, `short`, `path`); `site.blog`.
- Produces: unchanged DOM-hook contract for the canvas widget (`data-hc-canvas`, `data-hc-canvas-form`, `data-hc-canvas-rules`, `data-hc-canvas-link`, `data-hc-canvas-text`).

- [ ] **Step 1: Rewrite `tests/test_home_onepager.py` completely**

```python
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

EXPECTED_SECTIONS = [
    "hero-atlas",
    "priorities-grid",
    "constraint-canvas-home",
    "steps-ruled",
    "ai-principles",
    "ideas-list",
    "cta-bar",
]

EXPECTED_PARTIALS = [
    "_includes/sections/hero-atlas.html",
    "_includes/sections/priorities-grid.html",
    "_includes/sections/constraint-canvas-home.html",
    "_includes/sections/steps-ruled.html",
    "_includes/sections/ai-principles.html",
    "_includes/sections/ideas-list.html",
    "_includes/sections/cta-bar.html",
]

REMOVED_PARTIALS = [
    "_includes/sections/hero-canvas.html",
    "_includes/sections/journey-map.html",
    "_includes/sections/photo-strip.html",
    "_includes/sections/tri-columns.html",
]


def parse_frontmatter(path: Path) -> dict:
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def home_data() -> dict:
    return yaml.safe_load((REPO_ROOT / "_data/home.yml").read_text(encoding="utf-8"))


def test_index_sections_are_onepager_v2():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert fm.get("sections") == EXPECTED_SECTIONS


def test_index_hides_global_header():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert fm.get("hide_global_header") is True


def test_partials_exist():
    for partial in EXPECTED_PARTIALS:
        assert (REPO_ROOT / partial).is_file(), partial


def test_v1_partials_removed():
    for partial in REMOVED_PARTIALS:
        assert not (REPO_ROOT / partial).exists(), partial


def test_page_builder_registers_v2_sections():
    text = (REPO_ROOT / "_includes/page-builder.html").read_text(encoding="utf-8")
    for key in EXPECTED_SECTIONS:
        assert f"when '{key}'" in text, key
    for key in ("hero-canvas", "photo-strip", "tri-columns"):
        assert f"when '{key}'" not in text, key


def test_head_scopes_home_canvas_to_en():
    text = (REPO_ROOT / "_includes/head.html").read_text(encoding="utf-8")
    block = re.search(
        r"\{% if page\.home_locale and page\.locale == 'en' %\}.*?home-canvas",
        text,
        re.DOTALL,
    )
    assert block, "home-canvas assets must be scoped to the EN homepage"


def test_home_hero_v2_data():
    hero = home_data()["home_hero"]
    for key in ("eyebrow", "kicker", "title", "lead"):
        assert hero[key], key
    assert hero["primary_action"]["url"].startswith("/")
    labels = [a["label"] for a in hero["secondary_actions"]]
    assert len(hero["secondary_actions"]) == 2
    for action in hero["secondary_actions"]:
        assert action["url"].startswith("/"), action


def test_home_journey_data():
    nodes = home_data()["home_journey"]["nodes"]
    assert len(nodes) == 5
    for node in nodes:
        assert node["url"].startswith("/services/")
        assert node["title"] and node["statement"]


def test_home_canvas_data():
    canvas = home_data()["home_canvas"]
    assert len(canvas["selects"]) == 4
    for select in canvas["selects"]:
        assert select["default"] in select["options"]
    for rule in canvas["rules"]:
        assert rule["when"] and rule["text"] and rule["url"].startswith("/services/")
    assert canvas["default_result"]["url"].startswith("/services/")


def test_home_steps_and_principles_data():
    data = home_data()
    assert len(data["home_steps"]["steps"]) == 4
    assert len(data["home_ai_principles"]["items"]) == 3
    assert data["home_cta"]["primary_action"]["url"] == "https://www.linkedin.com/in/dkharlanau"


def test_home_canvas_js_is_canvas_only():
    js = (REPO_ROOT / "assets/home-canvas.js").read_text(encoding="utf-8")
    assert "data-hc-canvas" in js
    assert "data-hc-journey" not in js


def test_home_canvas_css_has_no_journey_styles():
    css = (REPO_ROOT / "assets/home-canvas.css").read_text(encoding="utf-8")
    assert ".hc-identity" in css
    assert ".hc-canvas__controls" in css
    assert ".hc-journey__rail" not in css
    assert ".hc-photos" not in css
```

- [ ] **Step 2: Run tests to verify failures**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: most tests FAIL (new partials missing, old ones present, `kicker` missing). Data tests for journey/canvas/steps PASS.

- [ ] **Step 3: Add the two keys under `home_hero` in `_data/home.yml`**

Inside the existing `home_hero:` mapping, directly after the `eyebrow:` line, insert:

```yaml
  kicker: "SAP operations · transformation · AI readiness"
  secondary_actions:
    - label: "Explore services"
      url: "/services/"
    - label: "Knowledge Atlas"
      url: "/atlas/"
```

- [ ] **Step 4: Create `_includes/sections/hero-atlas.html`**

```liquid
{% assign hero = site.data.home.home_hero %}
<section class="section atlas-hero">
  <div class="hc-identity">
    <p class="hc-identity__name">Dzmitryi Kharlanau <span>· {{ hero.eyebrow }}</span></p>
    <nav class="hc-identity__langs" aria-label="Language">
      {% for language in site.data.home_languages %}
      <a href="{{ language.path }}"{% if page.locale == language.code %} aria-current="page"{% endif %}>{{ language.short }}</a>
      {% endfor %}
    </nav>
  </div>
  <p class="eyebrow">{{ hero.kicker }}</p>
  <h1>{{ hero.title }}</h1>
  <p class="lead">{{ hero.lead }}</p>
  <div class="atlas-hero__actions">
    <a class="button button--primary" href="{{ hero.primary_action.url }}">{{ hero.primary_action.label }}</a>
    {% for action in hero.secondary_actions %}
    <a class="button" href="{{ action.url }}">{{ action.label }}</a>
    {% endfor %}
  </div>
</section>
```

- [ ] **Step 5: Create `_includes/sections/priorities-grid.html`**

```liquid
{% assign journey = site.data.home.home_journey %}
<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Where I help</p>
    <h2>Five operating priorities</h2>
    <p class="lead">Each engagement starts from one of these constraints — stabilize what runs, fix what repeats, prepare what comes next.</p>
  </header>
  <div class="atlas-card-grid">
    {% for node in journey.nodes %}
    <a class="atlas-card" href="{{ node.url }}">
      <h3>{{ node.title }}</h3>
      <p>{{ node.statement }}</p>
      <span class="link-arrow">Open {{ node.title | downcase }}</span>
    </a>
    {% endfor %}
  </div>
</section>
```

- [ ] **Step 6: Rewrite `_includes/sections/constraint-canvas-home.html` completely**

```liquid
{% assign canvas = site.data.home.home_canvas %}
<section class="section" data-hc-canvas>
  <div class="section-shell section-shell--flat">
    <header class="section-heading">
      <p class="eyebrow">{{ canvas.eyebrow }}</p>
      <h2>{{ canvas.title }}</h2>
      <p class="lead">{{ canvas.intro }}</p>
    </header>
    <form class="hc-canvas__controls" data-hc-canvas-form>
      {% for select in canvas.selects %}
      <div class="hc-canvas__field">
        <label for="hc-canvas-{{ select.id }}">{{ select.label }}</label>
        <select id="hc-canvas-{{ select.id }}" name="{{ select.id }}">
          {% for option in select.options %}
          <option value="{{ option }}"{% if option == select.default %} selected{% endif %}>{{ option }}</option>
          {% endfor %}
        </select>
      </div>
      {% endfor %}
    </form>
    <div class="hc-canvas__result">
      <p class="eyebrow">{{ canvas.result_label }}</p>
      <a class="hc-canvas__action" href="{{ canvas.default_result.url }}" data-hc-canvas-link aria-live="polite">
        <span data-hc-canvas-text>{{ canvas.default_result.text }}</span>
        <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
      </a>
    </div>
    <script type="application/json" data-hc-canvas-rules>{{ canvas.rules | jsonify }}</script>
  </div>
</section>
```

- [ ] **Step 7: Create `_includes/sections/steps-ruled.html`**

```liquid
{% assign steps = site.data.home.home_steps %}
<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Engagement rhythm</p>
    <h2>{{ steps.title }} {{ steps.subtitle }}</h2>
  </header>
  <ol class="hc-steps">
    {% for step in steps.steps %}
    <li class="hc-steps__item">
      <span class="hc-steps__number">{{ step.number }}</span>
      <div>
        <h3>{{ step.title }}</h3>
        <p>{{ step.detail }}</p>
      </div>
    </li>
    {% endfor %}
  </ol>
</section>
```

- [ ] **Step 8: Create `_includes/sections/ai-principles.html`**

```liquid
{% assign principles = site.data.home.home_ai_principles %}
<section class="section">
  <div class="section-shell section-shell--flat">
    <header class="section-heading">
      <p class="eyebrow">{{ principles.eyebrow }}</p>
      <h2>{{ principles.title }}</h2>
      <p class="lead">{{ principles.lead }}</p>
    </header>
    <ul class="hc-principles">
      {% for item in principles.items %}
      <li>
        <div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.detail }}</p>
        </div>
      </li>
      {% endfor %}
    </ul>
    <p class="hc-note">{{ principles.footnote }}</p>
  </div>
</section>
```

- [ ] **Step 9: Create `_includes/sections/ideas-list.html`**

```liquid
{% assign posts = site.blog | sort: 'date' | reverse %}
<section class="section">
  <header class="section-heading">
    <p class="eyebrow">Field notes</p>
    <h2>Ideas from practice. Not theory.</h2>
  </header>
  <ul class="hc-ideas">
    {% for post in posts limit: 3 %}
    <li>
      <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
      <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %d, %Y' }}</time>
    </li>
    {% endfor %}
  </ul>
  <div class="section-actions">
    <a class="button" href="{{ '/blog/' | relative_url }}">View all writing</a>
  </div>
</section>
```

- [ ] **Step 10: Rewrite `_includes/sections/cta-bar.html` completely**

```liquid
{% assign cta = site.data.home.home_cta %}
<section class="section">
  <div class="section-shell section-shell--flat">
    <header class="section-heading">
      <p class="eyebrow">Next step</p>
      <h2>{{ cta.title }}</h2>
      <p class="lead">{{ cta.note }}</p>
    </header>
    <div class="section-actions">
      <a class="button button--primary" href="{{ cta.primary_action.url }}" target="_blank" rel="noopener noreferrer">{{ cta.primary_action.label }}</a>
      <a class="button" href="{{ cta.secondary.url }}">{{ cta.secondary.label }}</a>
    </div>
  </div>
</section>
```

- [ ] **Step 11: Delete the four v1 partials**

```bash
git rm _includes/sections/hero-canvas.html _includes/sections/journey-map.html _includes/sections/photo-strip.html _includes/sections/tri-columns.html
```

- [ ] **Step 12: Update `_includes/page-builder.html`**

Remove the three v1-only branches (`{% when 'hero-canvas' %}`, `{% when 'photo-strip' %}`, `{% when 'tri-columns' %}` and their include lines) and make the remaining new-section branches read exactly:

```liquid
      {% when 'hero-atlas' %}
        {% include sections/hero-atlas.html %}
      {% when 'priorities-grid' %}
        {% include sections/priorities-grid.html %}
      {% when 'constraint-canvas-home' %}
        {% include sections/constraint-canvas-home.html %}
      {% when 'steps-ruled' %}
        {% include sections/steps-ruled.html %}
      {% when 'ai-principles' %}
        {% include sections/ai-principles.html %}
      {% when 'ideas-list' %}
        {% include sections/ideas-list.html %}
      {% when 'cta-bar' %}
        {% include sections/cta-bar.html %}
```

(The `cta-bar` branch already exists; keep it. All branches stay immediately before `{% endcase %}`.)

- [ ] **Step 13: Update the sections list in `index.md` frontmatter**

```yaml
sections:
  - hero-atlas
  - priorities-grid
  - constraint-canvas-home
  - steps-ruled
  - ai-principles
  - ideas-list
  - cta-bar
```

Also add a new frontmatter key (anywhere among the other keys):

```yaml
hide_global_header: true
```

- [ ] **Step 14: Rewrite `assets/home-canvas.css` completely**

```css
/* Homepage (EN) — supplements the Evidence Atlas layer with the few
   homepage-specific patterns: identity line, constraint canvas controls,
   ruled lists. Everything else uses atlas classes directly. */

/* --- Identity line (replaces the global header on the homepage) --- */

.hc-identity {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1.5rem;
  flex-wrap: wrap;
  padding-bottom: 1.25rem;
  margin-bottom: 2.5rem;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-identity__name {
  font-weight: 700;
  font-size: 0.9375rem;
  letter-spacing: -0.01em;
  color: var(--ea-navy, #152033);
  margin: 0;
}

.hc-identity__name span {
  font-weight: 400;
  color: var(--ea-ink-muted, #5a6472);
}

.hc-identity__langs { display: flex; gap: 0.75rem; flex-wrap: wrap; }

.hc-identity__langs a {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-decoration: none;
  color: var(--ea-ink-muted, #5a6472);
}

.hc-identity__langs a:hover { color: var(--ea-signal, #a85d09); }

.hc-identity__langs a[aria-current="page"] {
  color: var(--ea-navy, #152033);
  font-weight: 700;
}

/* --- Constraint canvas --- */

.hc-canvas__controls {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1.25rem;
  margin: 0 0 2rem;
  padding: 0;
  border: 0;
}

.hc-canvas__field label {
  display: block;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ea-navy, #152033);
  margin-bottom: 0.375rem;
}

.hc-canvas__field select {
  width: 100%;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ea-navy, #152033);
  background: var(--ea-paper, #fff);
  border: 1px solid var(--ea-line, #d8dce3);
  border-radius: 3px;
  padding: 0.625rem 0.75rem;
}

.hc-canvas__result {
  border-top: 1px solid var(--ea-line, #d8dce3);
  padding-top: 1.25rem;
}

.hc-canvas__action {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.125rem;
  font-weight: 600;
  line-height: 1.4;
  color: var(--ea-navy, #152033);
  text-decoration: none;
}

.hc-canvas__action:hover { color: var(--ea-signal, #a85d09); }

/* --- Ruled lists (steps, principles, ideas) --- */

.hc-steps,
.hc-principles,
.hc-ideas {
  list-style: none;
  margin: 0;
  padding: 0;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-steps__item,
.hc-principles li,
.hc-ideas li {
  display: flex;
  gap: 1.25rem;
  align-items: baseline;
  padding: 1rem 0;
  border-top: 1px solid var(--ea-line, #d8dce3);
}

.hc-steps__number {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  color: var(--ea-signal, #a85d09);
  min-width: 2rem;
}

.hc-steps__item h3,
.hc-principles h3 {
  font-size: 1rem;
  margin: 0 0 0.25rem;
  color: var(--ea-navy, #152033);
}

.hc-steps__item p,
.hc-principles p {
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--ea-ink-muted, #5a6472);
  margin: 0;
}

.hc-ideas li { justify-content: space-between; }

.hc-ideas a {
  font-size: 0.9375rem;
  font-weight: 500;
  color: var(--ea-navy, #152033);
  text-decoration: none;
}

.hc-ideas a:hover { color: var(--ea-signal, #a85d09); }

.hc-ideas time {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  color: var(--ea-ink-muted, #5a6472);
  white-space: nowrap;
}

.hc-note {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ea-ink-muted, #5a6472);
  margin: 1.25rem 0 0;
}

@media (max-width: 960px) {
  .hc-canvas__controls { grid-template-columns: repeat(2, minmax(0, 1fr)); }
}

@media (max-width: 640px) {
  .hc-canvas__controls { grid-template-columns: 1fr; }
  .hc-ideas li { flex-direction: column; gap: 0.25rem; }
}
```

- [ ] **Step 15: Rewrite `assets/home-canvas.js` completely (canvas only)**

```js
/* Homepage constraint canvas. The section renders a complete default
   state server-side; this script only enhances. */
(function () {
  'use strict';

  var canvas = document.querySelector('[data-hc-canvas]');
  if (!canvas) { return; }

  var form = canvas.querySelector('[data-hc-canvas-form]');
  var rulesEl = canvas.querySelector('[data-hc-canvas-rules]');
  var link = canvas.querySelector('[data-hc-canvas-link]');
  var text = canvas.querySelector('[data-hc-canvas-text]');
  var fallback = { text: text.textContent, url: link.getAttribute('href') };
  var rules = [];
  try {
    rules = JSON.parse(rulesEl.textContent) || [];
  } catch (e) {
    rules = [];
  }

  function matches(when, values) {
    return Object.keys(when).every(function (key) {
      var expected = Array.isArray(when[key]) ? when[key] : [when[key]];
      return expected.indexOf(values[key]) !== -1;
    });
  }

  function update() {
    var values = {};
    Array.prototype.forEach.call(form.elements, function (field) {
      if (field.name) { values[field.name] = field.value; }
    });
    var rule = null;
    for (var i = 0; i < rules.length; i += 1) {
      if (matches(rules[i].when, values)) { rule = rules[i]; break; }
    }
    var result = rule || fallback;
    text.textContent = result.text;
    link.setAttribute('href', result.url);
  }

  form.addEventListener('change', update);
})();
```

- [ ] **Step 16: Run tests — all pass**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: 12/12 PASS (the two chrome tests — `test_index_hides_global_header` passes from Step 13; there is no layout test here, that's Task 9).

- [ ] **Step 17: Build and verify markers**

Run (timeout ≥ 180s):

```bash
bundle exec jekyll build 2>&1 | tail -2
grep -c "atlas-hero\|atlas-card-grid\|hc-canvas__controls\|hc-identity" _site/index.html
grep -c "hc-journey\|hc-photos" _site/index.html
node --check assets/home-canvas.js && echo "syntax OK"
```

Expected: build succeeds; first grep > 0; second grep = 0 (exit 1 is fine); `syntax OK`.

- [ ] **Step 18: Commit**

```bash
git add tests/test_home_onepager.py _data/home.yml index.md _includes/page-builder.html _includes/sections/ assets/home-canvas.css assets/home-canvas.js
git commit -m "Restyle homepage one-pager into atlas design language"
```

---

### Task 9: Chrome — hide homepage header, redesign footer

**Files:**
- Modify: `_layouts/default.html` (one conditional around the header include)
- Modify: `_includes/footer.html` (full rewrite)
- Create: `assets/site-footer.css`
- Modify: `_includes/head.html` (one global stylesheet link)
- Modify: `tests/test_home_onepager.py` (append 3 tests)

**Interfaces:**
- Consumes: `page.hide_global_header` (set in Task 8 Step 13); `locale_data.ui.footer` strings with English defaults.

- [ ] **Step 1: Append the chrome tests to `tests/test_home_onepager.py`**

```python
def test_default_layout_honors_hide_global_header():
    text = (REPO_ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    assert re.search(r"unless page\.hide_global_header.*?header\.html", text, re.DOTALL)


def test_footer_is_editorial_grid():
    text = (REPO_ROOT / "_includes/footer.html").read_text(encoding="utf-8")
    assert "footer-grid" in text
    assert "footer-brand" in text
    assert 'href="/atlas/"' in text


def test_head_loads_site_footer_globally():
    text = (REPO_ROOT / "_includes/head.html").read_text(encoding="utf-8")
    assert "/assets/site-footer.css" in text
```

Run the file — expected: the 3 new tests FAIL, the 12 existing PASS.

- [ ] **Step 2: Wrap the header include in `_layouts/default.html`**

Replace the line `  {% include header.html %}` with:

```liquid
  {% unless page.hide_global_header %}
  {% include header.html %}
  {% endunless %}
```

- [ ] **Step 3: Rewrite `_includes/footer.html` completely**

```liquid
{% assign footer_ui = locale_data.ui.footer %}
<div class="wrapper">
  <div class="footer-grid">
    <div class="footer-brand">
      <p class="footer-brand__name">Dzmitryi Kharlanau</p>
      <p class="footer-brand__note">SAP consulting — AMS, operations, integration, and practical AI readiness.</p>
      <p class="footer-note">&copy; {{ "now" | date: "%Y" }} Dzmitryi Kharlanau</p>
    </div>
    <nav class="footer-col" aria-label="{{ footer_ui.label | default: 'Footer' }}">
      <p class="footer-col__heading">{{ footer_ui.explore | default: 'Explore' }}</p>
      <a href="/about/">{{ footer_ui.about | default: 'About' }}</a>
      <a href="/services/">{{ footer_ui.services | default: 'Services' }}</a>
      <a href="/atlas/">{{ footer_ui.atlas | default: 'Atlas' }}</a>
      <a href="/news/">{{ footer_ui.signals | default: 'Signals' }}</a>
      <a href="/datasets/">{{ footer_ui.datasets | default: 'Datasets' }}</a>
      <a href="/ai/">{{ footer_ui.ai_sources | default: 'AI sources' }}</a>
    </nav>
    <nav class="footer-col" aria-label="Legal">
      <p class="footer-col__heading">{{ footer_ui.legal | default: 'Legal' }}</p>
      <a href="/legal/datasets/">{{ footer_ui.cite | default: 'Cite' }}</a>
      <a href="/legal/professional-disclosure/">{{ footer_ui.disclosure | default: 'Disclosure' }}</a>
      <a href="/legal/responsible-ai/">{{ footer_ui.ai_policy | default: 'AI policy' }}</a>
      <a href="/legal/privacy/">{{ footer_ui.privacy | default: 'Privacy' }}</a>
    </nav>
  </div>
</div>
```

- [ ] **Step 4: Create `assets/site-footer.css`**

```css
/* Global editorial footer. Loaded after evidence-atlas.css. */

.site-footer {
  border-top: 1px solid var(--ea-line, #d8dce3);
  margin-top: 4rem;
  padding: 3rem 0 2.5rem;
  background: var(--ea-paper, #fff);
}

.footer-grid {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) minmax(0, 1fr);
  gap: 2.5rem;
}

.footer-brand__name {
  font-weight: 700;
  font-size: 1rem;
  letter-spacing: -0.01em;
  color: var(--ea-navy, #152033);
  margin: 0 0 0.375rem;
}

.footer-brand__note {
  font-size: 0.875rem;
  line-height: 1.55;
  color: var(--ea-ink-muted, #5a6472);
  max-width: 26rem;
  margin: 0 0 1rem;
}

.footer-note {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ea-ink-muted, #5a6472);
  margin: 0;
}

.footer-col {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.footer-col__heading {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ea-signal, #a85d09);
  margin: 0 0 0.5rem;
}

.footer-col a {
  font-size: 0.875rem;
  color: var(--ea-navy, #152033);
  text-decoration: none;
  width: fit-content;
}

.footer-col a:hover { color: var(--ea-signal, #a85d09); }

@media (max-width: 720px) {
  .footer-grid { grid-template-columns: 1fr; gap: 2rem; }
}
```

- [ ] **Step 5: Add the global stylesheet link in `_includes/head.html`**

Insert immediately after the line `<link rel="stylesheet" href="{{ '/assets/evidence-atlas.css' | relative_url }}?v={{ asset_version }}" />`:

```liquid
<link rel="stylesheet" href="{{ '/assets/site-footer.css' | relative_url }}?v={{ asset_version }}" />
```

(No conditional — the footer is global.)

- [ ] **Step 6: Run tests — all pass**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: 15/15 PASS.

- [ ] **Step 7: Build and verify**

Run (timeout ≥ 180s):

```bash
bundle exec jekyll build 2>&1 | tail -2
grep -c "footer-grid" _site/index.html _site/de/index.html _site/atlas/index.html
grep -c "site-footer.css" _site/index.html
grep -c "site-header\|class=\"header" _site/index.html
```

Expected: build succeeds; `footer-grid` present on all three pages; `site-footer.css` linked; last grep = 0 on the EN homepage (header suppressed). Note: also `grep -c "site-header\|class=\"header" _site/de/index.html` must be > 0 (locales keep the header).

- [ ] **Step 8: Commit**

```bash
git add _layouts/default.html _includes/footer.html _includes/head.html assets/site-footer.css tests/test_home_onepager.py
git commit -m "Hide header on EN homepage and redesign global footer"
```

---

### Task 10: Full validation + visual QA

**Files:**
- Modify (only if a test legitimately encodes the old homepage/footer): `tests/*.py`

- [ ] **Step 1: Full validation sequence**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
```

Expected: all pass. Update assertions that legitimately encode the old EN homepage or old footer; never weaken policy assertions (verification levels, noindex). Report pre-existing failures on unrelated pages as pre-existing (verify against base commit `4ff28ca` where feasible) rather than fixing them.

- [ ] **Step 2: Visual QA (Playwright MCP)**

- Restart the local server (`lsof -nP -iTCP:4000 -sTCP:LISTEN` for the PID, kill it, `bundle exec jekyll serve` in background; first build ~70s). Leave it RUNNING at the end.
- Screenshot `/` at 1280px and 390px; compare against `/` 's target language by screenshotting `/atlas/` at 1280px too. Judge: same typography/kickers/cards/ruled aesthetics; minimal fold (identity line, no nav menu); footer shows the new 3-column editorial grid. Save screenshots to `.superpowers/sdd/qa/`.
- Canvas interaction: set impact=High + recurrence=Daily → recommendation "Stabilize incidents and reduce repeat work." linking to `/services/sap-ams-consulting/`. Check console for JS errors.
- Verify `/de/` keeps the old homepage WITH the menu header, and shows the new footer.
- Document all discrepancies in the report; do not fix them in this task.

- [ ] **Step 3: Commit any test updates**

```bash
git add tests/
git commit -m "Update assertions for atlas-style homepage and footer"
```

---

## Self-Review Notes

- Spec-v2 coverage: hero fold (Task 8 Step 4), priorities grid (Step 5), canvas restyle (Step 6), steps/AI/ideas/CTA (Steps 7–10), partial deletion (Step 11), CSS/JS slimming (Steps 14–15), header suppression (Task 8 Step 13 + Task 9 Step 2), footer (Task 9 Steps 3–5), verification (Task 10).
- No placeholders; all code complete.
- Name consistency: DOM hooks unchanged from v1 (`data-hc-canvas*`); new classes `hc-identity`, `hc-steps`, `hc-principles`, `hc-ideas`, `hc-note`, `footer-grid`, `footer-brand`, `footer-col` match across tests, markup, and CSS.
