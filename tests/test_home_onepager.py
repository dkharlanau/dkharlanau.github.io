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
