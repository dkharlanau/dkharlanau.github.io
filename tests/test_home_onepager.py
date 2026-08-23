import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

EXPECTED_SECTIONS = ["home-product"]

EXPECTED_PARTIALS = ["_includes/sections/home-product.html"]

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


def test_all_localized_homepages_use_the_shared_product_page():
    home_paths = [
        "index.md", "ar/index.md", "de/index.md", "es/index.md", "fr/index.md",
        "it/index.md", "nl/index.md", "pl/index.md", "pt-br/index.md", "zh-cn/index.md",
    ]
    for home_path in home_paths:
        fm = parse_frontmatter(REPO_ROOT / home_path)
        assert fm.get("sections") == EXPECTED_SECTIONS, home_path
        assert fm.get("home_locale") is True, home_path


def test_index_uses_global_header():
    fm = parse_frontmatter(REPO_ROOT / "index.md")
    assert not fm.get("hide_global_header")


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


def test_home_uses_the_shared_portal_theme_and_real_portrait():
    layout = (REPO_ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    partial = (REPO_ROOT / "_includes/sections/home-product.html").read_text(encoding="utf-8")
    css = (REPO_ROOT / "assets/diagnostic-portal.css").read_text(encoding="utf-8")
    assert "diagnostic-portal.css" in layout
    assert "DzmitryiKharlanau.avif" in partial
    assert re.search(r"\.portal-text-link\s*\{[^}]*min-height:\s*44px", css)


def test_product_home_leads_with_person_learning_and_machine_access():
    text = (REPO_ROOT / "_includes/sections/home-product.html").read_text(encoding="utf-8")
    copy = yaml.safe_load((REPO_ROOT / "_data/home_portal.yml").read_text(encoding="utf-8"))["en"]
    assert "personal-hero" in text
    assert "personal-machine" in text
    assert copy["personal"]["hero"]["title"] == "Dzmitryi Kharlanau"
    assert copy["personal"]["hero"]["primary_href"] == "/about/"
    assert copy["personal"]["hero"]["secondary_href"] == "/knowledge/"
    assert [item["title"] for item in copy["personal"]["start"]["items"]] == [
        "Understand my work", "Learn and prepare", "Use the knowledge with AI"
    ]
    assert [item["label"] for item in copy["personal"]["map"]["items"]] == [
        "Knowledge", "Labs", "Frameworks", "Machine"
    ]
    assert "systems/" not in text.split("{% else %}", 1)[0]


def test_home_hero_data():
    hero = home_data()["hero"]
    for key in ("title", "lead", "person_meta", "trust_line"):
        assert hero[key], key
    assert hero["primary_action"]["url"].startswith("/")
    assert len(hero["loop_card"]["items"]) == 3
    assert len(hero["visual"]["items"]) == 4


def test_home_product_copy_covers_every_locale():
    locales = {"en", "de", "es", "fr", "it", "nl", "pl", "pt-BR", "zh-Hans", "ar"}
    data = yaml.safe_load((REPO_ROOT / "_data/home_product.yml").read_text(encoding="utf-8"))
    assert set(data) == locales
    for locale, copy in data.items():
        assert copy["calculator"]["disclaimer"], locale
        assert len(copy["profile"]["principles"]) == 3, locale
        assert copy["writing"]["all"], locale


def test_diagnostic_portal_copy_covers_every_locale():
    locales = {"en", "de", "es", "fr", "it", "nl", "pl", "pt-BR", "zh-Hans", "ar"}
    data = yaml.safe_load((REPO_ROOT / "_data/home_portal.yml").read_text(encoding="utf-8"))
    assert set(data) == locales
    for locale, copy in data.items():
        assert copy["hero"]["title"], locale
        assert len(copy["trace"]["items"]) == 3, locale
        assert len(copy["focus"]["cards"]) == 3, locale
        assert len(copy["method"]["steps"]) == 3, locale
        assert len(copy["evidence"]["items"]) == 3, locale


def test_home_js_runs_operational_visual_and_calculator():
    js = (REPO_ROOT / "assets/home-canvas.js").read_text(encoding="utf-8")
    assert "data-op-flow" in js
    assert "data-incident-calculator" in js
    assert "Intl.NumberFormat" in js
    assert "prefers-reduced-motion" in js


def test_home_css_covers_product_sections_and_responsive_states():
    css = (REPO_ROOT / "assets/home-canvas.css").read_text(encoding="utf-8")
    assert ".op-hero" in css
    assert ".op-signal-map" in css
    assert ".op-calculator" in css
    assert ".op-profile" in css
    assert "prefers-reduced-motion" in css


def test_default_layout_always_uses_shared_header():
    text = (REPO_ROOT / "_layouts/default.html").read_text(encoding="utf-8")
    assert "{% include header.html %}" in text
    assert "unless page.hide_global_header" not in text


def test_reader_tools_have_sharing_and_personal_local_reaction():
    text = (REPO_ROOT / "assets/reader-tools.js").read_text(encoding="utf-8")
    assert "navigator.share" in text
    assert "linkedin.com/sharing/share-offsite" in text
    assert "localStorage" in text
    assert "No public count is shown" in text


def test_footer_is_compact_and_trust_oriented():
    text = (REPO_ROOT / "_includes/footer.html").read_text(encoding="utf-8")
    assert "portal-footer__nav" in text
    assert "portal-footer__social" in text
    assert "footer-brand" in text
    assert "DzmitryiKharlanau.avif" in text
    assert 'href="/services/"' in text
    assert 'href="/knowledge/"' in text
    assert "site.data.identity.profiles.linkedin" in text
    assert "site.data.identity.profiles.github" in text
    assert 'href="/atlas/"' not in text


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
