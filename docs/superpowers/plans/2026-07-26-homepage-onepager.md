# Homepage One-Pager Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the EN homepage (`index.md`) with a minimalistic one-pager (hero + journey map, constraint canvas, photo strip, tri-column row, CTA bar) per `docs/superpowers/specs/2026-07-26-homepage-onepager-design.md`.

**Architecture:** Five new page-builder section partials (one includes a sixth, the journey map) registered in `_includes/page-builder.html`, English-only data keys appended to `_data/home.yml`, one scoped stylesheet `assets/home-canvas.css` consuming `--ea-*` tokens from `assets/evidence-atlas.css`, and one dependency-free script `assets/home-canvas.js`. The 9 localized homepages keep the old sections and partials, which remain untouched.

**Tech Stack:** Jekyll 3.10 / Liquid, vanilla CSS, vanilla JS, Python pytest (source-file assertions, repo convention).

## Global Constraints

- Do NOT modify old section partials, old `home.yml` keys, or any locale homepage (`de/`, `ar/`, etc.) — they still serve 9 locales.
- Do NOT modify `_includes/header.html`, `_layouts/default.html`, `assets/evidence-atlas.css`, or the services-canvas files (uncommitted work by another stream).
- No new dependencies, no build step, no frameworks.
- New CSS classes use the `hc-` prefix and consume `var(--ea-*, <fallback>)` tokens with explicit fallbacks.
- Homepage protection (`docs/site-content-design-contract.md` §3) is explicitly waived by the user for this task; no other protected files may change.
- No invented email addresses or external links; primary CTA is `https://www.linkedin.com/in/dkharlanau` (already public in the repo).
- Commit after every task. Do not commit `_site/`.

---

### Task 1: Failing test + homepage data keys

**Files:**
- Create: `tests/test_home_onepager.py`
- Modify: `_data/home.yml` (append at end of file)

**Interfaces:**
- Produces: `site.data.home.home_hero`, `.home_journey` (5 nodes × `id, number, title, statement, bullets[], url`), `.home_canvas` (`selects[]`, `rules[]`, `default_result`, `result_label`), `.home_steps` (4 steps), `.home_ai_principles` (3 items), `.home_cta` — consumed by partials in Tasks 3–4.

- [ ] **Step 1: Write the failing test**

```python
import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

EXPECTED_SECTIONS = [
    "hero-canvas",
    "constraint-canvas-home",
    "photo-strip",
    "tri-columns",
    "cta-bar",
]

EXPECTED_PARTIALS = [
    "_includes/sections/hero-canvas.html",
    "_includes/sections/journey-map.html",
    "_includes/sections/constraint-canvas-home.html",
    "_includes/sections/photo-strip.html",
    "_includes/sections/tri-columns.html",
    "_includes/sections/cta-bar.html",
]


def parse_frontmatter(path: Path) -> dict:
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def home_data() -> dict:
    return yaml.safe_load((REPO_ROOT / "_data/home.yml").read_text(encoding="utf-8"))


def test_index_sections_are_onepager():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert fm.get("sections") == EXPECTED_SECTIONS


def test_partials_exist():
    for partial in EXPECTED_PARTIALS:
        assert (REPO_ROOT / partial).is_file(), partial


def test_page_builder_registers_new_sections():
    text = (REPO_ROOT / "_includes/page-builder.html").read_text(encoding="utf-8")
    for key in EXPECTED_SECTIONS:
        assert f"when '{key}'" in text, key


def test_head_loads_home_canvas_en_only():
    text = (REPO_ROOT / "_includes/head.html").read_text(encoding="utf-8")
    assert "/assets/home-canvas.css" in text
    assert "/assets/home-canvas.js" in text
    block = re.search(
        r"\{% if page\.home_locale and page\.locale == 'en' %\}.*?home-canvas",
        text,
        re.DOTALL,
    )
    assert block, "home-canvas assets must be scoped to the EN homepage"


def test_home_hero_data():
    hero = home_data()["home_hero"]
    for key in ("eyebrow", "title", "lead", "microcopy"):
        assert hero[key], key
    assert hero["primary_action"]["url"].startswith("/")


def test_home_journey_data():
    nodes = home_data()["home_journey"]["nodes"]
    assert len(nodes) == 5
    for node in nodes:
        for key in ("id", "number", "title", "statement", "url"):
            assert node[key], (node.get("id"), key)
        assert len(node["bullets"]) >= 3
        assert node["url"].startswith("/services/")


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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: FAIL — all 8 tests fail (missing keys, missing partials, old sections list).

- [ ] **Step 3: Append the data keys to `_data/home.yml`**

Append exactly this block at the end of `_data/home.yml`:

```yaml
home_hero:
  eyebrow: "Independent senior SAP consulting"
  title: "SAP operations that are easier to run — and easier to improve."
  lead: "Independent SAP perspective that turns operational friction into a clear, executable next step."
  primary_action:
    label: "Start SAP analysis"
    url: "/services/ams-cost-center-catalyst/"
  microcopy: "No pitch. Just clarity."

home_journey:
  label: "Five operating priorities"
  nodes:
    - id: "ams"
      number: "01"
      title: "AMS reliability"
      statement: "Stabilize what runs your business. Reduce incidents, repeat work, and restore confidence in support."
      bullets:
        - "Incident reduction and trend control"
        - "Runbook and knowledge health"
        - "Service governance and ownership"
      url: "/services/sap-ams-consulting/"
    - id: "data"
      number: "02"
      title: "Master data"
      statement: "Make master data dependable enough that processes and AI can trust it."
      bullets:
        - "BP / customer / vendor replication"
        - "MDG governance and quality signals"
        - "Exception handling without noise"
      url: "/services/sap-master-data-stability-assessment/"
    - id: "logistics"
      number: "03"
      title: "Logistics & planning"
      statement: "Trace where O2C, delivery, and planning flows break — and why they keep breaking."
      bullets:
        - "O2C and delivery diagnostics"
        - "ATP and availability issues"
        - "Planning exception patterns"
      url: "/services/sap-o2c-process-audit/"
    - id: "integration"
      number: "04"
      title: "Integration & automation"
      statement: "Make interface-heavy landscapes easier to monitor, recover, and govern."
      bullets:
        - "Interface monitoring and recovery"
        - "Retry and idempotency patterns"
        - "Targeted automation, not big-bang programs"
      url: "/services/sap-integration-architecture/"
    - id: "ai"
      number: "05"
      title: "Practical AI"
      statement: "Use AI where it reduces real operational friction — with controls that hold in production."
      bullets:
        - "Triage and knowledge surfacing"
        - "Assisted diagnostics"
        - "Small tools with human review"
      url: "/services/sap-ai-ml-enablement/"

home_canvas:
  eyebrow: "Constraint canvas"
  title: "What needs attention first?"
  intro: "A quick read. Not a report."
  selects:
    - id: "impact"
      label: "Business impact"
      options: ["Low", "Medium", "High"]
      default: "Medium"
    - id: "recurrence"
      label: "Recurrence"
      options: ["Rare", "Monthly", "Weekly", "Daily"]
      default: "Weekly"
    - id: "manual"
      label: "Manual work"
      options: ["Low", "Medium", "High"]
      default: "High"
    - id: "horizon"
      label: "Change horizon"
      options: ["0–3 months", "3–6 months", "6–12 months"]
      default: "0–3 months"
  result_label: "Recommended next action"
  default_result:
    text: "Stabilize incidents and reduce repeat work."
    url: "/services/sap-ams-consulting/"
  rules:
    - when:
        impact: "High"
        recurrence: ["Weekly", "Daily"]
      text: "Stabilize incidents and reduce repeat work."
      url: "/services/sap-ams-consulting/"
    - when:
        manual: "High"
        recurrence: ["Weekly", "Daily"]
      text: "Automate the repeat analysis and exception handling."
      url: "/services/sap-ai-ml-enablement/"
    - when:
        manual: "High"
      text: "Remove manual effort from exception-heavy processes."
      url: "/services/sap-master-data-stability-assessment/"
    - when:
        impact: "High"
        horizon: ["3–6 months", "6–12 months"]
      text: "Map the transformation sequence before committing budget."
      url: "/services/ams-cost-center-catalyst/"
    - when:
        recurrence: ["Weekly", "Daily"]
      text: "Trace the process breakpoints behind the repetition."
      url: "/services/sap-o2c-process-audit/"
    - when:
        impact: "Medium"
        horizon: ["3–6 months", "6–12 months"]
      text: "Strengthen integration monitoring and recovery paths."
      url: "/services/sap-integration-architecture/"

home_steps:
  title: "Clarity in 4 steps."
  subtitle: "Momentum from day one."
  steps:
    - number: "01"
      title: "Align"
      detail: "Understand the situation and define what success looks like."
    - number: "02"
      title: "Focus"
      detail: "Pick the constraint and target the first move."
    - number: "03"
      title: "Act"
      detail: "Execute together: diagnostics, quick wins, decisions documented."
    - number: "04"
      title: "Sustain"
      detail: "Runbooks, metrics, reviews — and keep it working."

home_ai_principles:
  eyebrow: "AI only with operating context"
  title: "Practical AI. Safe by design."
  lead: "AI can amplify outcomes — when it respects your systems, data, and people."
  items:
    - icon: "lock"
      title: "Operate in your environment"
      detail: "No data leaves your control."
    - icon: "shield"
      title: "Human in the loop"
      detail: "Decisions stay with your team."
    - icon: "format_list_bulleted"
      title: "Purpose-built use cases"
      detail: "Solves real work, not experiments."
  footnote: "Guardrails: security · privacy · compliance · explainability"

home_cta:
  title: "Ready to map your constraint?"
  note: "A focused session. Leave with a clear next step."
  primary_action:
    label: "Book strategy session"
    url: "https://www.linkedin.com/in/dkharlanau"
  secondary:
    label: "Explore services"
    url: "/services/"
```

- [ ] **Step 4: Run tests — data tests pass, structure tests still fail**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: `test_home_hero_data`, `test_home_journey_data`, `test_home_canvas_data`, `test_home_steps_and_principles_data` PASS; the other 4 FAIL.

- [ ] **Step 5: Commit**

```bash
git add tests/test_home_onepager.py _data/home.yml
git commit -m "Add one-pager homepage data keys and structural tests"
```

---

### Task 2: Wire sections into index.md, page-builder, and head.html

**Files:**
- Modify: `index.md` (frontmatter `sections:` list only)
- Modify: `_includes/page-builder.html` (add 5 `when` branches before `{% endcase %}`)
- Modify: `_includes/head.html` (add scoped asset block after line 125, the `evidence-atlas.css` link)

**Interfaces:**
- Consumes: section keys from Task 1's `EXPECTED_SECTIONS`.
- Produces: dispatcher branches rendering `sections/hero-canvas.html` etc. (created in Tasks 3–4).

- [ ] **Step 1: Replace the sections list in `index.md`**

In `index.md` frontmatter, replace the entire `sections:` list with:

```yaml
sections:
  - hero-canvas
  - constraint-canvas-home
  - photo-strip
  - tri-columns
  - cta-bar
```

Do not touch any other frontmatter key or the body (`{% include page-builder.html %}`).

- [ ] **Step 2: Register the sections in `_includes/page-builder.html`**

Insert immediately before `{% endcase %}`:

```liquid
      {% when 'hero-canvas' %}
        {% include sections/hero-canvas.html %}
      {% when 'constraint-canvas-home' %}
        {% include sections/constraint-canvas-home.html %}
      {% when 'photo-strip' %}
        {% include sections/photo-strip.html %}
      {% when 'tri-columns' %}
        {% include sections/tri-columns.html %}
      {% when 'cta-bar' %}
        {% include sections/cta-bar.html %}
```

- [ ] **Step 3: Add the scoped asset block in `_includes/head.html`**

Insert immediately after the line `<link rel="stylesheet" href="{{ '/assets/evidence-atlas.css' | relative_url }}?v={{ asset_version }}" />`:

```liquid
{% if page.home_locale and page.locale == 'en' %}
<link rel="stylesheet" href="{{ '/assets/home-canvas.css' | relative_url }}?v={{ asset_version }}" />
<script src="{{ '/assets/home-canvas.js' | relative_url }}?v={{ asset_version }}" defer></script>
{% endif %}
```

- [ ] **Step 4: Run tests — wiring tests pass**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: `test_index_sections_are_onepager`, `test_page_builder_registers_new_sections`, `test_head_loads_home_canvas_en_only` now PASS; `test_partials_exist` still FAILS.

- [ ] **Step 5: Commit**

```bash
git add index.md _includes/page-builder.html _includes/head.html
git commit -m "Wire one-pager sections into EN homepage"
```

---

### Task 3: Hero + journey map partials

**Files:**
- Create: `_includes/sections/hero-canvas.html`
- Create: `_includes/sections/journey-map.html`

**Interfaces:**
- Consumes: `site.data.home.home_hero`, `site.data.home.home_journey` from Task 1.
- Produces: DOM hooks `[data-hc-journey]`, `[data-node]`, `[data-card]` consumed by `home-canvas.js` (Task 5); classes `hc-hero`, `hc-journey` styled in Task 6.

- [ ] **Step 1: Create `_includes/sections/hero-canvas.html`**

```liquid
{% assign hero = site.data.home.home_hero %}
<section class="hc-hero" aria-labelledby="hc-hero-title">
  <div class="hc-hero__copy">
    <p class="hc-eyebrow">{{ hero.eyebrow }}</p>
    <h1 id="hc-hero-title" class="hc-hero__title">{{ hero.title }}</h1>
    <p class="hc-hero__lead">{{ hero.lead }}</p>
    <div class="hc-hero__actions">
      <a class="hc-button" href="{{ hero.primary_action.url }}">
        {{ hero.primary_action.label }}
        <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
      </a>
      <p class="hc-microcopy">{{ hero.microcopy }}</p>
    </div>
  </div>
  {% include sections/journey-map.html %}
</section>
```

- [ ] **Step 2: Create `_includes/sections/journey-map.html`**

```liquid
{% assign journey = site.data.home.home_journey %}
<div class="hc-journey" aria-label="{{ journey.label }}" data-hc-journey>
  <div class="hc-journey__rail">
    {% for node in journey.nodes %}
    <button
      class="hc-journey__node{% if forloop.first %} is-active{% endif %}"
      type="button"
      aria-pressed="{% if forloop.first %}true{% else %}false{% endif %}"
      data-node="{{ node.id }}"
    >
      <span class="hc-journey__number">{{ node.number }}</span>
      <span class="hc-journey__marker hc-journey__marker--{{ node.id }}" aria-hidden="true"></span>
      <span class="hc-journey__name">{{ node.title }}</span>
    </button>
    {% endfor %}
  </div>
  <div class="hc-journey__cards" aria-live="polite">
    {% for node in journey.nodes %}
    <article
      class="hc-journey__card{% if forloop.first %} is-visible{% endif %}"
      data-card="{{ node.id }}"
      {% unless forloop.first %}hidden{% endunless %}
    >
      <h2 class="hc-journey__card-title">{{ node.title }}</h2>
      <p class="hc-journey__card-statement">{{ node.statement }}</p>
      <p class="hc-journey__card-label">Typical work</p>
      <ul class="hc-journey__card-list">
        {% for bullet in node.bullets %}
        <li>{{ bullet }}</li>
        {% endfor %}
      </ul>
      <a class="hc-journey__card-link" href="{{ node.url }}">
        Explore {{ node.title | downcase }}
        <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
      </a>
    </article>
    {% endfor %}
  </div>
</div>
```

- [ ] **Step 3: Run tests**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: `test_partials_exist` still FAILS (4 partials missing); everything else PASS.

- [ ] **Step 4: Commit**

```bash
git add _includes/sections/hero-canvas.html _includes/sections/journey-map.html
git commit -m "Add one-pager hero and journey map partials"
```

---

### Task 4: Remaining four partials

**Files:**
- Create: `_includes/sections/constraint-canvas-home.html`
- Create: `_includes/sections/photo-strip.html`
- Create: `_includes/sections/tri-columns.html`
- Create: `_includes/sections/cta-bar.html`

**Interfaces:**
- Consumes: `home_canvas`, `home_steps`, `home_ai_principles`, `home_cta` from Task 1; `site.blog` collection.
- Produces: DOM hooks `[data-hc-canvas]`, `[data-hc-canvas-form]`, `[data-hc-canvas-rules]`, `[data-hc-canvas-link]`, `[data-hc-canvas-text]` consumed by `home-canvas.js` (Task 5).

- [ ] **Step 1: Create `_includes/sections/constraint-canvas-home.html`**

```liquid
{% assign canvas = site.data.home.home_canvas %}
<section class="hc-canvas" aria-labelledby="hc-canvas-title" data-hc-canvas>
  <div class="hc-canvas__intro">
    <p class="hc-eyebrow">{{ canvas.eyebrow }}</p>
    <h2 id="hc-canvas-title" class="hc-section-title">{{ canvas.title }}</h2>
    <p class="hc-canvas__note">{{ canvas.intro }}</p>
  </div>
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
    <p class="hc-eyebrow">{{ canvas.result_label }}</p>
    <a class="hc-canvas__action" href="{{ canvas.default_result.url }}" data-hc-canvas-link aria-live="polite">
      <span data-hc-canvas-text>{{ canvas.default_result.text }}</span>
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    </a>
  </div>
  <script type="application/json" data-hc-canvas-rules>{{ canvas.rules | jsonify }}</script>
</section>
```

- [ ] **Step 2: Create `_includes/sections/photo-strip.html`**

```liquid
<section class="hc-photos" aria-label="Field context">
  <figure class="hc-photos__item">
    <img src="{{ '/assets/img/services/logistics-terminal.webp' | relative_url }}" alt="Container terminal with trucks — logistics operations in action" loading="lazy" />
    <figcaption>Logistics in action</figcaption>
  </figure>
  <figure class="hc-photos__item">
    <img src="{{ '/assets/img/services/data-operations.webp' | relative_url }}" alt="Warehouse worker reviewing stock data on a screen" loading="lazy" />
    <figcaption>Data operations</figcaption>
  </figure>
  <figure class="hc-photos__item">
    <img src="{{ '/assets/img/services/collaborative-workshop.webp' | relative_url }}" alt="Consultants mapping a process on a whiteboard with sticky notes" loading="lazy" />
    <figcaption>Collaborative workshop</figcaption>
  </figure>
</section>
```

- [ ] **Step 3: Create `_includes/sections/tri-columns.html`**

```liquid
{% assign steps = site.data.home.home_steps %}
{% assign principles = site.data.home.home_ai_principles %}
{% assign posts = site.blog | sort: 'date' | reverse %}
<section class="hc-tri">
  <div class="hc-tri__col">
    <h2 class="hc-section-title">{{ steps.title }}<br />{{ steps.subtitle }}</h2>
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
  </div>
  <div class="hc-tri__col">
    <p class="hc-eyebrow">{{ principles.eyebrow }}</p>
    <h2 class="hc-section-title">{{ principles.title }}</h2>
    <p class="hc-tri__lead">{{ principles.lead }}</p>
    <ul class="hc-principles">
      {% for item in principles.items %}
      <li>
        <span class="material-symbols-outlined" aria-hidden="true">{{ item.icon }}</span>
        <div>
          <h3>{{ item.title }}</h3>
          <p>{{ item.detail }}</p>
        </div>
      </li>
      {% endfor %}
    </ul>
    <p class="hc-microcopy">{{ principles.footnote }}</p>
  </div>
  <div class="hc-tri__col">
    <p class="hc-eyebrow">Field notes</p>
    <h2 class="hc-section-title">Ideas from practice.<br />Not theory.</h2>
    <ul class="hc-ideas">
      {% for post in posts limit: 3 %}
      <li>
        <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
        <time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: '%b %d, %Y' | upcase }}</time>
      </li>
      {% endfor %}
    </ul>
    <a class="hc-text-link" href="{{ '/blog/' | relative_url }}">
      View all
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    </a>
  </div>
</section>
```

- [ ] **Step 4: Create `_includes/sections/cta-bar.html`**

```liquid
{% assign cta = site.data.home.home_cta %}
<section class="hc-cta" aria-labelledby="hc-cta-title">
  <h2 id="hc-cta-title" class="hc-section-title">{{ cta.title }}</h2>
  <p class="hc-cta__note">{{ cta.note }}</p>
  <div class="hc-cta__actions">
    <a class="hc-button" href="{{ cta.primary_action.url }}" target="_blank" rel="noopener noreferrer">
      {{ cta.primary_action.label }}
      <span class="material-symbols-outlined" aria-hidden="true">arrow_forward</span>
    </a>
    <a class="hc-text-link" href="{{ cta.secondary.url }}">{{ cta.secondary.label }}</a>
  </div>
</section>
```

- [ ] **Step 5: Run tests — all pass**

Run: `PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests/test_home_onepager.py -v`
Expected: 8/8 PASS.

- [ ] **Step 6: Build to verify Liquid renders**

Run: `bundle exec jekyll build 2>&1 | tail -5`
Expected: `done in ... seconds.` with no Liquid errors. Verify markers exist:

```bash
grep -c "hc-journey\|hc-canvas\|hc-tri\|hc-cta" _site/index.html
grep -c "home-canvas" _site/index.html
grep -c "home-canvas" _site/de/index.html
```

Expected: first two greps > 0; the `de` grep = 0 (locales untouched).

- [ ] **Step 7: Commit**

```bash
git add _includes/sections/constraint-canvas-home.html _includes/sections/photo-strip.html _includes/sections/tri-columns.html _includes/sections/cta-bar.html
git commit -m "Add constraint canvas, photo strip, tri-column, and CTA bar partials"
```

---

### Task 5: Widget JavaScript

**Files:**
- Create: `assets/home-canvas.js`

**Interfaces:**
- Consumes: DOM hooks from Tasks 3–4 (`[data-hc-journey]`, `[data-node]`, `[data-card]`, `[data-hc-canvas-form]`, `[data-hc-canvas-rules]`, `[data-hc-canvas-link]`, `[data-hc-canvas-text]`).

- [ ] **Step 1: Create `assets/home-canvas.js`**

```js
/* Homepage one-pager widgets: journey map + constraint canvas.
   Both sections render a complete default state server-side;
   this script only enhances. */
(function () {
  'use strict';

  // --- Journey map: activate a node on hover / focus / click ---
  var journey = document.querySelector('[data-hc-journey]');
  if (journey) {
    var nodes = journey.querySelectorAll('[data-node]');
    var cards = journey.querySelectorAll('[data-card]');

    function activate(id) {
      Array.prototype.forEach.call(nodes, function (node) {
        var active = node.getAttribute('data-node') === id;
        node.classList.toggle('is-active', active);
        node.setAttribute('aria-pressed', active ? 'true' : 'false');
      });
      Array.prototype.forEach.call(cards, function (card) {
        var visible = card.getAttribute('data-card') === id;
        card.classList.toggle('is-visible', visible);
        card.hidden = !visible;
      });
    }

    Array.prototype.forEach.call(nodes, function (node) {
      var id = node.getAttribute('data-node');
      node.addEventListener('click', function () { activate(id); });
      node.addEventListener('mouseenter', function () { activate(id); });
      node.addEventListener('focus', function () { activate(id); });
    });
  }

  // --- Constraint canvas: first matching rule wins, else server-rendered default ---
  var canvas = document.querySelector('[data-hc-canvas]');
  if (canvas) {
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
  }
})();
```

- [ ] **Step 2: Verify the script loads in the built page**

Run:

```bash
bundle exec jekyll build 2>&1 | tail -2
grep -c "home-canvas.js" _site/index.html
node --check assets/home-canvas.js && echo "syntax OK"
```

Expected: build succeeds, grep = 1, `syntax OK`.

- [ ] **Step 3: Commit**

```bash
git add assets/home-canvas.js
git commit -m "Add journey map and constraint canvas widget script"
```

---

### Task 6: Stylesheet

**Files:**
- Create: `assets/home-canvas.css`

**Interfaces:**
- Consumes: `hc-` classes from Tasks 3–4; `--ea-page`, `--ea-navy`, `--ea-line`, `--ea-signal` tokens from `assets/evidence-atlas.css` (every `var()` gets a literal fallback).

- [ ] **Step 1: Create `assets/home-canvas.css`**

```css
/* Homepage one-pager (EN). Consumes --ea-* tokens from evidence-atlas.css. */

.hc-eyebrow {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--ea-signal, #a85d09);
  margin: 0 0 0.75rem;
}

.hc-microcopy {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--ea-navy, #152033);
  opacity: 0.55;
  margin: 0;
}

.hc-section-title {
  font-size: clamp(1.5rem, 3vw, 2.125rem);
  line-height: 1.1;
  letter-spacing: -0.02em;
  color: var(--ea-navy, #152033);
  margin: 0 0 1rem;
}

.hc-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  background: var(--ea-signal, #a85d09);
  color: #fff;
  font-weight: 600;
  font-size: 0.8125rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.875rem 1.5rem;
  border-radius: 3px;
}

.hc-button:hover { filter: brightness(1.08); }

.hc-text-link {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.8125rem;
  font-weight: 600;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--ea-navy, #152033);
  text-decoration: none;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
  padding-bottom: 0.125rem;
}

.hc-text-link:hover { color: var(--ea-signal, #a85d09); }

/* --- Hero --- */

.hc-hero {
  display: grid;
  grid-template-columns: minmax(0, 5fr) minmax(0, 7fr);
  gap: 3rem;
  align-items: start;
  padding: 3rem 0 4rem;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-hero__title {
  font-size: clamp(2.5rem, 5.5vw, 4.25rem);
  line-height: 1.02;
  letter-spacing: -0.03em;
  color: var(--ea-navy, #152033);
  margin: 0 0 1.5rem;
}

.hc-hero__lead {
  font-size: 1.0625rem;
  line-height: 1.6;
  max-width: 32rem;
  color: var(--ea-navy, #152033);
  opacity: 0.8;
  margin: 0 0 2rem;
}

.hc-hero__actions {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  flex-wrap: wrap;
}

/* --- Journey map --- */

.hc-journey__rail {
  display: flex;
  justify-content: space-between;
  position: relative;
  padding-top: 1rem;
  margin-bottom: 2rem;
}

.hc-journey__rail::before {
  content: "";
  position: absolute;
  top: calc(1rem + 19px);
  left: 0;
  right: 0;
  border-top: 1px solid var(--ea-line, #d8dce3);
}

.hc-journey__node {
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  background: none;
  border: 0;
  padding: 0;
  cursor: pointer;
  font: inherit;
  color: var(--ea-navy, #152033);
}

.hc-journey__number {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  color: var(--ea-signal, #a85d09);
}

.hc-journey__marker {
  width: 38px;
  height: 38px;
  background: var(--ea-page, #f6f7f9);
  border: 1px solid var(--ea-navy, #152033);
  position: relative;
  z-index: 1;
  transition: background 120ms ease;
}

.hc-journey__marker--ams { border-radius: 50%; }
.hc-journey__marker--data { border-radius: 3px; }
.hc-journey__marker--logistics { border-radius: 3px; transform: rotate(45deg) scale(0.85); }
.hc-journey__marker--integration { border-radius: 50% 50% 3px 3px; }
.hc-journey__marker--ai { border-radius: 3px; border-style: dashed; }

.hc-journey__node.is-active .hc-journey__marker {
  background: var(--ea-signal, #a85d09);
  border-color: var(--ea-signal, #a85d09);
}

.hc-journey__name {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.625rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  text-align: center;
  max-width: 7rem;
}

.hc-journey__card {
  background: #fff;
  border: 1px solid var(--ea-line, #d8dce3);
  border-radius: 3px;
  padding: 1.5rem;
  max-width: 22rem;
  box-shadow: 6px 6px 0 rgba(21, 32, 51, 0.08);
}

.hc-journey__card[hidden] { display: none; }

.hc-journey__card-title {
  font-size: 0.8125rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--ea-signal, #a85d09);
  margin: 0 0 0.5rem;
}

.hc-journey__card-statement { font-size: 0.9375rem; line-height: 1.5; margin: 0 0 1rem; }

.hc-journey__card-label {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  opacity: 0.55;
  margin: 0 0 0.375rem;
}

.hc-journey__card-list {
  margin: 0 0 1rem;
  padding-left: 1.125rem;
  font-size: 0.875rem;
  line-height: 1.7;
}

.hc-journey__card-link {
  display: inline-flex;
  align-items: center;
  gap: 0.375rem;
  font-size: 0.8125rem;
  font-weight: 600;
  color: var(--ea-signal, #a85d09);
  text-decoration: none;
}

/* --- Constraint canvas --- */

.hc-canvas {
  display: grid;
  grid-template-columns: minmax(0, 4fr) minmax(0, 6fr) minmax(0, 3fr);
  gap: 2.5rem;
  align-items: start;
  padding: 3rem 0;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-canvas__note { font-size: 0.875rem; opacity: 0.6; margin: 0; }

.hc-canvas__controls {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1.25rem;
  border: 0;
}

.hc-canvas__field label {
  display: block;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  margin-bottom: 0.375rem;
  color: var(--ea-navy, #152033);
}

.hc-canvas__field select {
  width: 100%;
  font: inherit;
  font-size: 0.9375rem;
  color: var(--ea-navy, #152033);
  background: #fff;
  border: 1px solid var(--ea-line, #d8dce3);
  border-radius: 3px;
  padding: 0.625rem 0.75rem;
}

.hc-canvas__action {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.0625rem;
  font-weight: 600;
  line-height: 1.4;
  color: var(--ea-navy, #152033);
  text-decoration: none;
}

.hc-canvas__action:hover { color: var(--ea-signal, #a85d09); }

/* --- Photo strip --- */

.hc-photos {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.25rem;
  padding: 2.5rem 0;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-photos__item { margin: 0; }

.hc-photos__item img {
  width: 100%;
  aspect-ratio: 16 / 9;
  object-fit: cover;
  border-radius: 3px;
  display: block;
}

.hc-photos__item figcaption {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  padding-top: 0.5rem;
  opacity: 0.65;
}

/* --- Tri-column row --- */

.hc-tri {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 2.5rem;
  padding: 3rem 0;
  border-bottom: 1px solid var(--ea-line, #d8dce3);
}

.hc-tri__lead { font-size: 0.9375rem; line-height: 1.6; opacity: 0.8; margin: 0 0 1.5rem; }

.hc-steps { list-style: none; margin: 0; padding: 0; }

.hc-steps__item {
  display: flex;
  gap: 1rem;
  padding: 0.875rem 0;
  border-top: 1px solid var(--ea-line, #d8dce3);
}

.hc-steps__number {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.75rem;
  color: var(--ea-signal, #a85d09);
  padding-top: 0.125rem;
}

.hc-steps__item h3,
.hc-principles h3 {
  font-size: 0.9375rem;
  margin: 0 0 0.25rem;
  color: var(--ea-navy, #152033);
}

.hc-steps__item p,
.hc-principles p { font-size: 0.875rem; line-height: 1.5; opacity: 0.75; margin: 0; }

.hc-principles { list-style: none; margin: 0 0 1.5rem; padding: 0; }

.hc-principles li {
  display: flex;
  gap: 0.875rem;
  padding: 0.75rem 0;
  border-top: 1px solid var(--ea-line, #d8dce3);
}

.hc-principles .material-symbols-outlined { color: var(--ea-signal, #a85d09); }

.hc-ideas { list-style: none; margin: 0 0 1.5rem; padding: 0; }

.hc-ideas li {
  padding: 0.75rem 0;
  border-top: 1px solid var(--ea-line, #d8dce3);
}

.hc-ideas a {
  display: block;
  font-size: 0.9375rem;
  font-weight: 500;
  line-height: 1.4;
  color: var(--ea-navy, #152033);
  text-decoration: none;
}

.hc-ideas a:hover { color: var(--ea-signal, #a85d09); }

.hc-ideas time {
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.6875rem;
  letter-spacing: 0.08em;
  opacity: 0.55;
}

/* --- CTA bar --- */

.hc-cta {
  display: flex;
  align-items: center;
  gap: 2rem;
  flex-wrap: wrap;
  padding: 2.5rem 0;
}

.hc-cta .hc-section-title { margin: 0; }

.hc-cta__note { font-size: 0.875rem; opacity: 0.65; margin: 0; flex: 1 1 auto; }

.hc-cta__actions { display: flex; align-items: center; gap: 1.5rem; flex-wrap: wrap; }

/* --- Responsive --- */

@media (max-width: 960px) {
  .hc-hero { grid-template-columns: 1fr; }
  .hc-canvas { grid-template-columns: 1fr; }
  .hc-tri { grid-template-columns: 1fr; }
}

@media (max-width: 640px) {
  .hc-journey__rail { flex-wrap: wrap; gap: 1rem; justify-content: flex-start; }
  .hc-journey__rail::before { display: none; }
  .hc-canvas__controls { grid-template-columns: 1fr; }
  .hc-photos { grid-template-columns: 1fr; }
  .hc-cta { flex-direction: column; align-items: flex-start; }
}

@media (prefers-reduced-motion: reduce) {
  .hc-journey__marker { transition: none; }
}
```

- [ ] **Step 2: Build and confirm the stylesheet is linked**

Run:

```bash
bundle exec jekyll build 2>&1 | tail -2
grep -c "home-canvas.css" _site/index.html
grep -c "home-canvas.css" _site/de/index.html
```

Expected: build succeeds; EN grep = 1; DE grep = 0.

- [ ] **Step 3: Commit**

```bash
git add assets/home-canvas.css
git commit -m "Add one-pager homepage stylesheet"
```

---

### Task 7: Full validation + visual QA

**Files:**
- Modify (only if a test legitimately encodes the old EN homepage): `tests/*.py`

**Interfaces:**
- Consumes: everything above.

- [ ] **Step 1: Run the full validation sequence**

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
python3 scripts/check_page_quality.py --site-dir _site --fail-on-critical
```

Expected: all pass. If a pytest test fails because it asserts old EN-homepage content (hero title, old section markers), update that assertion to the new one-pager reality and note it in the commit message. Do not weaken assertions that encode policy (verification levels, noindex rules).

- [ ] **Step 2: Visual QA in the browser**

Serve locally (a server is already running at `http://127.0.0.1:4000/` with auto-regeneration; otherwise `bundle exec jekyll serve`). With Playwright:
- Screenshot `/` at 1280px and 390px widths; compare against the reference screenshot.
- Click/hover journey nodes 02–05; confirm the card swaps and `aria-pressed` updates.
- Change each canvas select; confirm the recommendation and link target update (e.g. impact=High + recurrence=Daily → "Stabilize incidents and reduce repeat work." → `/services/sap-ams-consulting/`).
- Confirm `/de/` renders the old homepage unchanged.
- Check browser console for JS errors.

- [ ] **Step 3: Commit any test updates**

```bash
git add tests/
git commit -m "Update homepage assertions for one-pager structure"
```

---

## Self-Review Notes

- Spec coverage: all six spec sections map to Tasks 1–6; verification maps to Task 7. Locales, header, old partials explicitly untouched per Global Constraints.
- No placeholders: every code step contains complete code.
- Type/name consistency: DOM hooks (`data-hc-journey`, `data-node`, `data-card`, `data-hc-canvas-form`, `data-hc-canvas-rules`, `data-hc-canvas-link`, `data-hc-canvas-text`) and data keys (`home_hero`, `home_journey`, `home_canvas`, `home_steps`, `home_ai_principles`, `home_cta`) are identical across tests, data, partials, JS, and CSS.
