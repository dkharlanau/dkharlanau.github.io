"""Catch missing topic identities before publication rewrites generated metadata."""

from scripts import ai_search_trust_loop as publication


def test_source_topics_resolve_to_canonical_entities():
    entities = publication.load_entities()
    unresolved = []
    for path, _text, metadata, _raw, _body in publication.iter_sources():
        topic = metadata.get("primary_topic")
        if not topic:
            continue
        entity = entities.get(topic)
        if not entity or entity.get("id") != f"/entities/#{topic}":
            unresolved.append(f"{path.relative_to(publication.ROOT)}: {topic}")
    assert not unresolved, "Unresolved primary_topic references:\n" + "\n".join(sorted(unresolved))
