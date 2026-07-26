import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

EXPECTED_SECTIONS = [
    "hero-atlas",
    "priorities-grid",
    "value-loop",
    "ai-principles",
    "ideas-list",
    "cta-bar",
]

EXPECTED_PARTIALS = [
    "_includes/sections/hero-atlas.html",
    "_includes/sections/priorities-grid.html",
    "_includes/sections/value-loop.html",
    "_includes/sections/ai-principles.html",
    "_includes/sections/ideas-list.html",
    "_includes/sections/cta-bar.html",
]

REMOVED_PARTIALS = [
    "_includes/sections/hero-canvas.html",
    "_includes/sections/journey-map.html",
    "_includes/sections/photo-strip.html",
    "_includes/sections/tri-columns.html",
    "_includes/sections/constraint-canvas-home.html",
    "_includes/sections/steps-ruled.html",
]


def parse_frontmatter(path: Path) -> dict:
    match = FRONT_MATTER_RE.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(match.group(1)) if match else {}


def home_data() -> dict:
    return yaml.safe_load((REPO_ROOT / "_data/home.yml").read_text(encoding="utf-8"))


def test_index_sections_are_onepager():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert fm.get("sections") == EXPECTED_SECTIONS


def test_index_hides_global_header():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert fm.get("hide_global_header") is True


def test_partials_exist():
    for partial in EXPECTED_PARTIALS:
        assert (REPO_ROOT / partial).is_file(), partial


def test_old_partials_removed():
    for partial in REMOVED_PARTIALS:
        assert not (REPO_ROOT / partial).exists(), partial


def test_page_builder_registers_sections():
    text = (REPO_ROOT / "_includes/page-builder.html").read_text(encoding="utf-8")
    for key in EXPECTED_SECTIONS:
        assert f"when '{key}'" in text, key
    for key in ("hero-canvas", "photo-strip", "tri-columns", "constraint-canvas-home", "steps-ruled"):
        assert f"when '{key}'" not in text, key


def test_head_scopes_home_canvas_to_en():
    text = (REPO_ROOT / "_includes/head.html").read_text(encoding="utf-8")
    block = re.search(
        r"\{% if page\.home_locale and page\.locale == 'en' %\}.*?home-canvas",
        text,
        re.DOTALL,
    )
    assert block, "home-canvas assets must be scoped to the EN homepage"


def test_hero_has_language_dropdown():
    text = (REPO_ROOT / "_includes/sections/hero-atlas.html").read_text(encoding="utf-8")
    assert 'class="hc-langs"' in text
    assert "native_name" in text
    assert "hc-identity__langs" not in text


def test_home_hero_data():
    hero = home_data()["home_hero"]
    for key in ("eyebrow", "kicker", "title", "lead"):
        assert hero[key], key
    assert hero["primary_action"]["url"].startswith("/")
    assert len(hero["secondary_actions"]) == 2
    for action in hero["secondary_actions"]:
        assert action["url"].startswith("/"), action


def test_home_journey_data():
    nodes = home_data()["home_journey"]["nodes"]
    assert len(nodes) == 5
    for node in nodes:
        assert node["url"].startswith("/services/")
        assert node["title"] and node["statement"]


def test_home_value_data():
    items = home_data()["home_value"]["items"]
    assert len(items) == 3
    for item in items:
        for key in ("number", "title", "detail", "metric", "metric_label", "tag"):
            assert item[key], (item.get("title"), key)


def test_home_principles_and_cta_data():
    data = home_data()
    assert len(data["home_ai_principles"]["items"]) == 3
    assert data["home_cta"]["primary_action"]["url"] == "https://www.linkedin.com/in/dkharlanau"


def test_home_js_is_value_loop_only():
    js = (REPO_ROOT / "assets/home-canvas.js").read_text(encoding="utf-8")
    assert "data-hc-value" in js
    assert "data-hc-canvas" not in js
    assert "data-hc-journey" not in js
    assert "prefers-reduced-motion" in js


def test_home_css_covers_value_and_langs():
    css = (REPO_ROOT / "assets/home-canvas.css").read_text(encoding="utf-8")
    assert ".hc-identity" in css
    assert ".hc-langs" in css
    assert ".hc-value__card" in css
    assert ".hc-canvas__controls" not in css
    assert ".hc-journey__rail" not in css


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


def test_blog_index_uses_ruled_list():
    text = (REPO_ROOT / "blog/index.md").read_text(encoding="utf-8")
    assert "blog-list" in text
    assert "blog-featured" in text
    head = (REPO_ROOT / "_includes/head.html").read_text(encoding="utf-8")
    block = re.search(r"\{% if page\.url == '/blog/' %\}.*?blog-list\.css", head, re.DOTALL)
    assert block, "blog-list.css must be scoped to /blog/"
