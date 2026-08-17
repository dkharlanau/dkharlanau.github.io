from scripts.normalize_heading_hierarchy import normalize_text


def test_promotes_peer_card_titles_under_h2_to_h3():
    source = """
<section>
  <header><h2>Lead frame</h2></header>
  <div class="ecg-decision-columns">
    <div><h4>One</h4><p>A</p></div>
    <div><h4>Two</h4><p>B</p></div>
    <div><h4>Three</h4><p>C</p></div>
  </div>
</section>
"""
    normalized, count = normalize_text(source)
    assert count == 3
    assert "<h4>" not in normalized
    assert normalized.count("<h3>") == 3

    second_pass, second_count = normalize_text(normalized)
    assert second_count == 0
    assert second_pass == normalized


def test_keeps_nested_h4_titles_after_h3():
    source = """
<section>
  <header><h2>Runtime</h2></header>
  <article>
    <h3>Stage</h3>
    <div class="ecg-decision-columns">
      <div><h4>Inputs</h4></div>
      <div><h4>Output</h4></div>
    </div>
  </article>
</section>
"""
    normalized, count = normalize_text(source)
    assert count == 0
    assert normalized == source
