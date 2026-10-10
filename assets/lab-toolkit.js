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
      const statusId = button.getAttribute("data-copy-status");
      const status = statusId ? document.getElementById(statusId) : null;

      try {
        await navigator.clipboard.writeText(value.trim());
        button.textContent = "Copied";
        if (status) status.textContent = "Prompt copied. Paste it into your agent, then ask your question.";
      } catch (error) {
        const disclosure = target.closest("details");
        if (disclosure) disclosure.open = true;
        const range = document.createRange();
        range.selectNodeContents(target);
        const selection = window.getSelection();
        selection.removeAllRanges();
        selection.addRange(range);
        button.textContent = "Text selected";
        if (status) status.textContent = "Clipboard access is unavailable. The prompt is selected below; copy it manually.";
      }

      window.setTimeout(() => {
        button.textContent = original;
      }, 1600);
    });
  });
})();
