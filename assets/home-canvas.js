/* Homepage constraint canvas. The section renders a complete default
   state server-side; this script only enhances. */
(function () {
  'use strict';

  var canvas = document.querySelector('[data-hc-canvas]');
  if (!canvas) { return; }

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
  update();
})();
