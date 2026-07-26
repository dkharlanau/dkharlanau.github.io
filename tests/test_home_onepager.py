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
