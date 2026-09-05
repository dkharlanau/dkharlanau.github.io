from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def test_internal_polish_is_loaded_outside_the_homepage_only():
    layout = read("_layouts/default.html")

    assert "{% unless page.home_locale %}" in layout
    assert "{% unless page.url == '/' %}" in layout
    assert "/assets/internal-page-polish.css" in layout
    assert "Generated expert context remains available to the machine layer" in layout
    assert "expert-promotion-generated" not in layout


def test_enterprise_context_styles_are_detected_from_component_markup():
    layout = read("_layouts/default.html")

    assert "page.enterprise_context_graph or page.content contains 'ecg-'" in layout
    assert "/assets/enterprise-context-graph.css" in layout


def test_author_and_expert_components_use_distinct_roles():
    author = read("_includes/atlas/author-block.html")
    context = read("_includes/expert/context.html")
    cta = read("_includes/expert/cta.html")

    assert "article-author" in author
    assert "DzmitryiKharlanau.avif" in author
    assert "editorial-aside" in context
    assert "atlas-author atlas-expert-context" not in context
    assert "article-service-cta" in cta
    assert "atlas-author atlas-expert-cta" not in cta


def test_flat_skill_pages_get_reader_structure_and_bounded_toc():
    reader = read("assets/reader-tools.js")

    assert "normaliseFlatSkillArticle" in reader
    assert "reader-structure--normalised" in reader
    assert "const tocLimit = 12" in reader
    assert "additional sections continue in the article" in reader


def test_ai_business_signals_render_source_relevance_and_commentary():
    renderer = read("assets/dataset-render.js")

    assert "renderAiBusinessSignal" in renderer
    assert "data.business_relevance" in renderer
    assert "data.dzmitryi_commentary" in renderer
    assert "Open the original source" in renderer


def test_business_ai_case_facts_are_not_self_links():
    cases = read("labs/business-ai/cases.md")

    assert '<a href="#{{ item.id }}"><span>SYS</span>' not in cases
    assert '<a href="#{{ item.id }}"><span>KPI</span>' not in cases
    assert "case-evidence-row--commentary" in cases
    assert "case-evidence-list--grades" in cases


def test_visual_smoke_covers_representative_reader_failures():
    smoke = read("scripts/visual_smoke_test.mjs")

    assert "/labs/enterprise-assurance/" in smoke
    assert "/labs/business-ai/cases/" in smoke
    assert "/atlas/diagnostics/sap-idoc-diagnostics/" in smoke
    assert "/skill-hub/ai-assisted-analysis/ai-agent-authority-design-working-skill/" in smoke
    assert "/datasets/view/ai-business-signals/aibs-004/" in smoke
