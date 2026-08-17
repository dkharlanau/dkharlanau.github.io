from pathlib import Path

from scripts.normalize_heading_hierarchy import normalize_path_text, normalize_text


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


def test_derivation_cards_use_h3_and_nested_detail_h4():
    source = """
<section>
  <header><h2>Find the owner</h2></header>
  <div class="sm-card-grid">
    <article class="sm-card">
      <header><h4>{{ item.field }}</h4></header>
      <details><section><h5>Manual change</h5></section></details>
    </article>
  </div>
</section>
"""
    path = Path("labs/enterprise-context/sales-processes/mechanisms/derivation/index.html")
    normalized, count = normalize_path_text(path, source)
    assert count == 2
    assert "<h3>{{ item.field }}</h3>" in normalized
    assert "<h4>Manual change</h4>" in normalized


def test_promotion_review_dynamic_rule_title_is_h3():
    source = """
<section><h2>Review rule</h2><div id="pr-rules"></div></section>
<script>const title=document.createElement('h4');</script>
"""
    path = Path("labs/assessment/promotion-review/index.html")
    normalized, count = normalize_path_text(path, source)
    assert count == 1
    assert "document.createElement('h3')" in normalized
