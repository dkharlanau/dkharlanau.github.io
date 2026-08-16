#!/usr/bin/env python3
"""Normalize the shared JSON-LD publication templates.

The primary dispatcher owns page identity and core Article/WebPage properties.
The sitewide graph only augments that canonical @id with knowledge relations.
Editorial review timestamps are never used as modification timestamps.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STRUCTURED = ROOT / "_includes" / "seo" / "structured-data.html"
HEAD = ROOT / "_includes" / "head.html"
AUGMENTATION = ROOT / "_includes" / "seo" / "structured-data-sitewide-graph.html"

CANONICAL_MODIFIED = (
    "page.significant_lastmod | default: page.content_updated_at | default: "
    "page.schema_updated_at | default: page.last_modified_at | default: page.updated"
)

AUGMENTATION_TEMPLATE = r'''{% comment %}
Knowledge relationship augmentation for the canonical page node.
The primary structured-data dispatcher owns @type, title, author, dates and WebSite/Person nodes.
This include only adds entity, provenance, machine-representation and semantic-link properties
to the same canonical #article / #webpage identity. No second page identity is created.
{% endcomment %}

{% assign graph_url = page.url | absolute_url %}
{% assign graph_entities = site.data.knowledge_entities.entities | default: empty %}
{% assign graph_primary_key = page.primary_topic | default: page.primary_entity %}
{% assign graph_primary = graph_entities[graph_primary_key] %}
{% assign graph_robots = page.robots | default: '' %}
{% assign graph_indexable = true %}
{% if graph_robots contains 'noindex' %}{% assign graph_indexable = false %}{% endif %}
{% assign graph_reviewed = false %}
{% if page.status == 'reviewed' and page.verified == true %}{% assign graph_reviewed = true %}{% endif %}
{% assign graph_node_suffix = 'webpage' %}
{% assign graph_declared_type = page.structured_data.type | default: '' | downcase %}
{% if graph_declared_type == 'article' or graph_declared_type == 'techarticle' %}{% assign graph_node_suffix = 'article' %}{% endif %}
{% if page.url contains '/labs/' and graph_reviewed and graph_indexable %}{% assign graph_node_suffix = 'article' %}{% endif %}
{% assign graph_emit = false %}
{% if graph_indexable and page.url != '/' %}
  {% if graph_primary or page.entity_mentions or page.ai_sidecar or page.source_links or page.semantic_links %}{% assign graph_emit = true %}{% endif %}
{% endif %}

{% if graph_emit %}
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@id": "{{ graph_url }}#{{ graph_node_suffix }}"{% if graph_primary %},
  "about": {"@id": "{{ graph_primary.id | absolute_url }}"}{% endif %}{% if page.entity_mentions and page.entity_mentions.size > 0 %},
  "mentions": [
    {% for entity_key in page.entity_mentions %}
    {% assign entity = graph_entities[entity_key] %}
    {% if entity %}{"@id": "{{ entity.id | absolute_url }}"}{% else %}{"@type":"Thing","name":{{ entity_key | replace: '-', ' ' | jsonify }}}{% endif %}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]{% endif %}{% if page.ai_sidecar %},
  "subjectOf": {"@type":"DataDownload","contentUrl":"{{ page.ai_sidecar | absolute_url }}","encodingFormat":"application/json"}{% endif %}{% if page.source_links and page.source_links.size > 0 %},
  "citation": [
    {% for source in page.source_links %}{"@type":"WebPage","name":{{ source.title | default: source.url | jsonify }},"url":{{ source.url | jsonify }}}{% unless forloop.last %},{% endunless %}{% endfor %}
  ]{% endif %}{% if page.semantic_links and page.semantic_links.size > 0 %},
  "relatedLink": [{% for relation in page.semantic_links %}{{ relation.url | absolute_url | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %}]{% endif %}
}
</script>
{% endif %}
'''


def patch_once(text: str, old: str, new: str, label: str) -> str:
    if new in text:
        return text
    if old not in text:
        raise RuntimeError(f"Cannot normalize {label}: expected anchor not found")
    return text.replace(old, new, 1)


def normalize_structured(text: str) -> str:
    # A review is an evidence event, not a content modification event.
    text = text.replace(
        "page.last_modified_at | default: page.updated | default: page.last_reviewed",
        CANONICAL_MODIFIED,
    )

    knowledge_assign = (
        "{% assign url_parts = page.url | split: '/' %}\n"
        "{% assign knowledge_entities = site.data.knowledge_entities.entities | default: empty %}\n"
    )
    text = patch_once(
        text,
        "{% assign url_parts = page.url | split: '/' %}\n",
        knowledge_assign,
        "knowledge entity registry assignment",
    )

    lab_types = (
        "{% elsif page.url == '/labs/' or page.url == '/labs/enterprise-context/' %}\n"
        "  {% assign page_type = 'CollectionPage' %}\n"
        "{% elsif page.url contains '/labs/' and page.verified == true and page.status == 'reviewed' %}\n"
        "  {% assign page_type = 'TechArticle' %}\n"
        "{% elsif page.url contains '/datasets/' %}"
    )
    text = patch_once(
        text,
        "{% elsif page.url contains '/datasets/' %}",
        lab_types,
        "Lab page type dispatch",
    )

    lab_section = (
        "{% if page.url contains '/labs/enterprise-context/' and page.url != '/labs/enterprise-context/' %}\n"
        "  {% assign article_section_url = '/labs/enterprise-context/' | absolute_url %}\n"
        "  {% assign article_section_name = 'Enterprise Context Lab' %}\n"
        "{% elsif page.url contains '/labs/' and page.url != '/labs/' %}\n"
        "  {% assign article_section_url = '/labs/' | absolute_url %}\n"
        "  {% assign article_section_name = 'Labs' %}\n"
        "{% endif %}\n\n"
        "{% comment %} DefinedTerm / DefinedTermSet"
    )
    text = patch_once(
        text,
        "{% comment %} DefinedTerm / DefinedTermSet",
        lab_section,
        "Lab collection ownership",
    )

    old_author = '''  "author": {
    "@type": "Person",
    "@id": "{{ author_id }}",
    "name": {{ resume.name | jsonify }},
    "url": "{{ author_profile_url }}",
    "sameAs": ["{{ author_website_url }}", "{{ author_linkedin_url }}", "{{ author_github_url }}"]
  },
  "publisher": {
    "@type": "Person",
    "@id": "{{ author_id }}",
    "name": {{ resume.name | jsonify }},
    "url": "{{ author_profile_url }}",
    "sameAs": ["{{ author_website_url }}", "{{ author_linkedin_url }}", "{{ author_github_url }}"]
  },'''
    new_author = '''  "author": {"@id": "{{ author_id }}"},
  "publisher": {"@id": "{{ author_id }}"},'''
    text = patch_once(text, old_author, new_author, "canonical Article author reference")

    old_about = '''  "url": "{{ canonical_url }}"
  {% if page.domain or page.sap_area or page.business_process %},
  "about": {
    "@type": "Thing",
    "name": {{ page.domain | default: page.sap_area | default: page.business_process | jsonify }}
  }{% endif %}
  {% if page.tags %},
  "mentions": {{ page.tags | jsonify }}{% endif %}'''
    new_about = '''  "url": "{{ canonical_url }}"
  {% if page.ai_sidecar %},
  "subjectOf": {"@type":"DataDownload","contentUrl":"{{ page.ai_sidecar | absolute_url }}","encodingFormat":"application/json"}{% endif %}
  {% assign primary_entity_key = page.primary_topic | default: page.primary_entity %}
  {% assign primary_entity = knowledge_entities[primary_entity_key] %}
  {% if primary_entity %},
  "about": {"@id": "{{ primary_entity.id | absolute_url }}"}{% elsif page.domain or page.sap_area or page.business_process %},
  "about": {"@type":"Thing","name":{{ page.domain | default: page.sap_area | default: page.business_process | jsonify }}}{% endif %}
  {% if page.entity_mentions and page.entity_mentions.size > 0 %},
  "mentions": [
    {% for entity_key in page.entity_mentions %}
    {% assign entity = knowledge_entities[entity_key] %}
    {% if entity %}{"@id":"{{ entity.id | absolute_url }}"}{% else %}{"@type":"Thing","name":{{ entity_key | replace: '-', ' ' | jsonify }}}{% endif %}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]{% elsif page.tags %},
  "mentions": {{ page.tags | jsonify }}{% endif %}'''
    text = patch_once(text, old_about, new_about, "Article entity ownership")

    old_related = '''  {% if page.related %},
  "relatedLink": ['''
    new_related = '''  {% if page.semantic_links and page.semantic_links.size > 0 %},
  "relatedLink": [{% for relation in page.semantic_links %}{{ relation.url | absolute_url | jsonify }}{% unless forloop.last %},{% endunless %}{% endfor %}]
  {% elsif page.related %},
  "relatedLink": ['''
    text = patch_once(text, old_related, new_related, "semantic related links")

    old_citation = '''  {% if page.sources %},
  "citation": ['''
    new_citation = '''  {% if page.source_links and page.source_links.size > 0 %},
  "citation": [
    {% for source in page.source_links %}
    {"@type":"WebPage","name":{{ source.title | default: source.url | jsonify }},"url":{{ source.url | jsonify }}}{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
  {% elsif page.sources %},
  "citation": ['''
    text = patch_once(text, old_citation, new_citation, "registry-backed Article citations")
    return text


def normalize_head(text: str) -> str:
    return text.replace(
        "{% assign modified_raw = page.last_modified_at | default: page.updated %}",
        "{% assign modified_raw = " + CANONICAL_MODIFIED + " %}",
    )


def desired_files() -> dict[Path, str]:
    return {
        STRUCTURED: normalize_structured(STRUCTURED.read_text(encoding="utf-8")),
        HEAD: normalize_head(HEAD.read_text(encoding="utf-8")),
        AUGMENTATION: AUGMENTATION_TEMPLATE,
    }


def validate_invariants(contents: dict[Path, str]) -> list[str]:
    errors: list[str] = []
    structured = contents[STRUCTURED]
    head = contents[HEAD]
    augmentation = contents[AUGMENTATION]
    if "page.updated | default: page.last_reviewed" in structured:
        errors.append("structured-data.html still uses review date as modification fallback")
    if "'/labs/enterprise-context/'" not in structured or "page_type = 'TechArticle'" not in structured:
        errors.append("structured-data.html does not own Lab TechArticle/CollectionPage typing")
    if "page.source_links" not in structured or "page.semantic_links" not in structured or "primary_topic" not in structured:
        errors.append("structured-data.html is missing knowledge provenance/entity relations")
    if CANONICAL_MODIFIED not in head:
        errors.append("head.html article:modified_time does not use canonical modification precedence")
    for forbidden in ('"@type": "Person"', '"@type": "WebSite"', '"dateModified"', '"headline"'):
        if forbidden in augmentation:
            errors.append(f"sitewide graph must not redefine core node property {forbidden}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    try:
        desired = desired_files()
    except RuntimeError as exc:
        print(f"Publication schema normalization failed: {exc}")
        return 2

    errors = validate_invariants(desired)
    if errors:
        for error in errors:
            print(f"- {error}")
        return 2

    stale = []
    for path, content in desired.items():
        current = path.read_text(encoding="utf-8") if path.exists() else ""
        if current != content:
            stale.append(path.relative_to(ROOT).as_posix())
            if not args.check:
                path.write_text(content, encoding="utf-8")

    if args.check and stale:
        print("Publication schema templates are stale:")
        for path in stale:
            print(f" - {path}")
        return 1

    print(f"Publication schema normalization OK: changed={len(stale) if not args.check else 0}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
