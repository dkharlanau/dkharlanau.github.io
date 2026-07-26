/* Homepage widgets: value loop auto-advance + language dropdown close-on-outside-click.
   Both sections render a complete default state server-side; this script only enhances. */
(function () {
  'use strict';

  // --- Value loop: auto-advance cards with progress bar ---
  var root = document.querySelector('[data-hc-value]');
  if (root) {
    var tabs = root.querySelectorAll('[data-value-tab]');
    var panels = root.querySelectorAll('[data-value-panel]');
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    var DURATION = 5000;
    var current = 0;
    var timer = null;

    function activate(index) {
      current = index;
      Array.prototype.forEach.call(tabs, function (tab, i) {
        var active = i === index;
        tab.classList.toggle('is-active', active);
        tab.setAttribute('aria-selected', active ? 'true' : 'false');
      });
      Array.prototype.forEach.call(panels, function (panel, i) {
        var visible = i === index;
        panel.classList.toggle('is-visible', visible);
        panel.hidden = !visible;
      });
    }

    function restartBar() {
      Array.prototype.forEach.call(tabs, function (tab) {
        var fill = tab.querySelector('.hc-value__bar-fill');
        if (fill) {
          fill.style.animation = 'none';
          void fill.offsetWidth;
          fill.style.animation = '';
        }
      });
    }

    function next() {
      activate((current + 1) % tabs.length);
      restartBar();
    }

    function start() {
      if (!reduceMotion && !timer) { timer = window.setInterval(next, DURATION); }
    }

    function stop() {
      if (timer) { window.clearInterval(timer); timer = null; }
    }

    Array.prototype.forEach.call(tabs, function (tab, i) {
      tab.addEventListener('click', function () {
        activate(i);
        restartBar();
        stop();
        start();
      });
    });
    root.addEventListener('mouseenter', stop);
    root.addEventListener('mouseleave', start);
    root.addEventListener('focusin', stop);
    root.addEventListener('focusout', start);
    start();
  }

  // --- Language dropdown: close when clicking outside ---
  var langs = document.querySelector('.hc-langs');
  if (langs) {
    document.addEventListener('click', function (event) {
      if (langs.open && !langs.contains(event.target)) { langs.open = false; }
    });
  }
})();
