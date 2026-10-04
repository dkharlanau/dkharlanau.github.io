(() => {
  const buttons = document.querySelectorAll("[data-copy-target]");
  if (!buttons.length) return;

  buttons.forEach((button) => {
    button.addEventListener("click", async () => {
      const targetId = button.getAttribute("data-copy-target");
      const target = targetId ? document.getElementById(targetId) : null;
      if (!target) return;

      const value = target.textContent || "";
      const original = button.textContent;

      try {
        await navigator.clipboard.writeText(value.trim());
        button.textContent = "Copied";
      } catch (error) {
        const range = document.createRange();
        range.selectNodeContents(target);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        button.textContent = "Select";
      }

      window.setTimeout(() => {
        button.textContent = original;
      }, 1600);
    });
  });
})();
