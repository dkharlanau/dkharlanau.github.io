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
