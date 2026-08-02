(() => {
  const normalise = (value) => value.replace(/\s+/g, " ").trim().toLowerCase();
  const sectionForPath = (path) => {
    if (path.startsWith("/services/")) return { label: "Services", href: "/services/" };
    if (path.startsWith("/scenarios/")) return { label: "Scenarios", href: "/scenarios/" };
    if (path.startsWith("/atlas/")) return { label: "Knowledge Atlas", href: "/atlas/" };
    if (path.startsWith("/blog/")) return { label: "Journal", href: "/blog/" };
    if (path.startsWith("/notes/")) return { label: "Notes", href: "/notes/" };
    if (path.startsWith("/research/")) return { label: "Research", href: "/research/" };
    if (path.startsWith("/datasets/")) return { label: "Datasets", href: "/datasets/" };
    if (path.startsWith("/skill-hub/")) return { label: "Skill Hub", href: "/skill-hub/" };
    if (path.startsWith("/news/")) return { label: "Signals", href: "/news/" };
    if (path.startsWith("/radar/")) return { label: "Radar", href: "/radar/" };
    if (path === "/about/") return { label: "Profile", href: "/about/" };
    return null;
  };

  const addPageBreadcrumbs = () => {
    const main = document.querySelector("#content");
    const path = window.location.pathname;
    if (!main || path === "/" || /^\/(?:ar|de|es|fr|it|nl|pl|pt-br|zh-cn)\/$/.test(path)) return;
    if (main.querySelector(".breadcrumbs, .note-backlink, .reader-breadcrumbs, .ps-breadcrumbs")) return;

    const section = sectionForPath(path);
    const heading = main.querySelector("h1");
    if (!section || !heading) return;

    const nav = document.createElement("nav");
    nav.className = "ps-breadcrumbs";
    nav.setAttribute("aria-label", "Breadcrumb");
    const list = document.createElement("ol");
    [["Home", "/"], [section.label, section.href]].forEach(([label, href]) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      item.append(link);
      list.append(item);
    });
    if (path !== section.href) {
      const current = document.createElement("li");
      current.setAttribute("aria-current", "page");
      current.textContent = heading.textContent.trim();
      list.append(current);
    }
    nav.append(list);
    main.prepend(nav);
  };

  const addBreadcrumbs = (article) => {
    const heading = article.querySelector("h1");
    const pageBreadcrumb = document.querySelector("#content > .ps-breadcrumbs");
    if (!heading || pageBreadcrumb || article.previousElementSibling?.matches(".breadcrumbs, .note-backlink")) return;

    const section = sectionForPath(window.location.pathname);
    if (!section) return;

    const nav = document.createElement("nav");
    nav.className = "breadcrumbs reader-breadcrumbs";
    nav.setAttribute("aria-label", "Breadcrumb");
    const list = document.createElement("ol");
    [["Home", "/"], [section.label, section.href]].forEach(([label, href]) => {
      const item = document.createElement("li");
      const link = document.createElement("a");
      link.href = href;
      link.textContent = label;
      item.append(link);
      list.append(item);
    });
    const current = document.createElement("li");
    current.setAttribute("aria-current", "page");
    current.textContent = heading.textContent.trim();
    list.append(current);
    nav.append(list);
    article.before(nav);
  };

  const makeLink = (heading) => {
    const item = document.createElement("li");
    const link = document.createElement("a");
    link.href = `#${heading.id}`;
    link.textContent = heading.textContent.trim();
    item.append(link);
    return item;
  };

  const addToc = (article) => {
    const body = article.querySelector(":scope > .note-body");
    if (!body || article.querySelector(":scope > .reader-toc")) return;

    const allHeadings = [...body.querySelectorAll("h2")];
    const sourceHeading = allHeadings[0];
    const sourceList = sourceHeading?.nextElementSibling;
    const hasSourceToc = normalise(sourceHeading?.textContent || "") === "on this page" && sourceList?.tagName === "UL";
    const headings = allHeadings.filter((heading) => heading !== sourceHeading || !hasSourceToc);
    if (headings.length < 3 && !hasSourceToc) return;

    headings.forEach((heading, index) => {
      if (!heading.id) heading.id = `reader-section-${index + 1}`;
    });

    const toc = document.createElement("nav");
    toc.className = `reader-toc${hasSourceToc ? " reader-toc--source" : ""}`;
    toc.setAttribute("aria-label", "On this page");
    const disclosure = document.createElement("details");
    disclosure.className = "reader-toc__disclosure";
    disclosure.open = !window.matchMedia("(max-width: 760px)").matches;
    const summary = document.createElement("summary");
    summary.className = "reader-toc__summary";
    summary.textContent = `On this page (${headings.length})`;

    if (hasSourceToc) {
      sourceHeading.classList.add("reader-toc__visually-hidden");
      disclosure.append(summary, sourceList);
      toc.append(sourceHeading, disclosure);
      const sourceLinks = [...toc.querySelectorAll("a[href^='#']")];
      sourceLinks.forEach((link) => {
        const target = document.getElementById(link.getAttribute("href").slice(1));
        if (target && !target.id) target.id = link.getAttribute("href").slice(1);
      });
    } else {
      const list = document.createElement("ol");
      headings.forEach((heading) => list.append(makeLink(heading)));
      disclosure.append(summary, list);
      toc.append(disclosure);
    }

    const diagnosticRail = article.matches(".atlas-page")
      ? article.querySelector(":scope > .atlas-meta-panel")
      : null;
    if (diagnosticRail) diagnosticRail.append(toc);
    else body.before(toc);
    article.classList.add("reader-ready");

    const links = [...toc.querySelectorAll("a[href^='#']")];
    const linkById = new Map(links.map((link) => [link.getAttribute("href").slice(1), link]));
    if (!("IntersectionObserver" in window) || !linkById.size) return;

    const observer = new IntersectionObserver((entries) => {
      const current = entries.filter((entry) => entry.isIntersecting).sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
      if (!current) return;
      links.forEach((link) => link.removeAttribute("aria-current"));
      linkById.get(current.target.id)?.setAttribute("aria-current", "location");
    }, { rootMargin: "-18% 0px -68%", threshold: [0, .2, .6] });
    headings.forEach((heading) => observer.observe(heading));
  };

  const addArticleTools = (article) => {
    if (article.querySelector(":scope .reader-actions")) return;
    const heading = article.querySelector("h1");
    if (!heading) return;

    const actions = document.createElement("div");
    actions.className = "reader-actions";
    actions.setAttribute("aria-label", "Article actions");

    const label = document.createElement("span");
    label.className = "reader-actions__label";
    label.textContent = "Article tools";
    actions.append(label);

    const makeButton = (icon, text) => {
      const button = document.createElement("button");
      button.className = "reader-action";
      button.type = "button";
      button.innerHTML = `<span class="material-symbols-outlined" aria-hidden="true">${icon}</span><span>${text}</span>`;
      return button;
    };

    const copy = makeButton("link", "Copy link");
    copy.addEventListener("click", async () => {
      try {
        await navigator.clipboard.writeText(window.location.href);
      } catch (_) {
        const field = document.createElement("textarea");
        field.value = window.location.href;
        field.setAttribute("readonly", "");
        field.style.position = "fixed";
        field.style.opacity = "0";
        document.body.append(field);
        field.select();
        document.execCommand("copy");
        field.remove();
      }
      copy.querySelector("span:last-child").textContent = "Copied";
      window.setTimeout(() => { copy.querySelector("span:last-child").textContent = "Copy link"; }, 1800);
    });
    actions.append(copy);

    if (navigator.share) {
      const share = makeButton("ios_share", "Share");
      share.addEventListener("click", async () => {
        try { await navigator.share({ title: document.title, url: window.location.href }); } catch (_) { /* user cancelled */ }
      });
      actions.append(share);
    }

    const linkedIn = document.createElement("a");
    linkedIn.className = "reader-action";
    linkedIn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(window.location.href)}`;
    linkedIn.target = "_blank";
    linkedIn.rel = "noopener noreferrer";
    linkedIn.innerHTML = '<span class="material-symbols-outlined" aria-hidden="true">badge</span><span>LinkedIn</span>';
    actions.append(linkedIn);

    const reactionKey = `dkh-reader-useful:${window.location.pathname}`;
    const reaction = makeButton("recommend", "Useful to me");
    let reacted = false;
    try { reacted = window.localStorage.getItem(reactionKey) === "true"; } catch (_) { /* storage unavailable */ }
    reaction.setAttribute("aria-pressed", String(reacted));
    if (reacted) reaction.querySelector("span:last-child").textContent = "Marked useful";
    reaction.addEventListener("click", () => {
      reacted = !reacted;
      reaction.setAttribute("aria-pressed", String(reacted));
      reaction.querySelector("span:last-child").textContent = reacted ? "Marked useful" : "Useful to me";
      try {
        if (reacted) window.localStorage.setItem(reactionKey, "true");
        else window.localStorage.removeItem(reactionKey);
      } catch (_) { /* personal reaction remains active for this page view */ }
    });
    actions.append(reaction);

    const note = document.createElement("p");
    note.className = "reader-reaction-note";
    note.textContent = "Your reaction is stored only on this device. No public count is shown.";
    actions.append(note);

    const header = article.querySelector(":scope > .note-header");
    if (header) header.append(actions);
    else heading.insertAdjacentElement("afterend", actions);
  };

  const addSiteShare = () => {
    const widget = document.querySelector("[data-site-share]");
    if (!widget) return;
    const copy = widget.querySelector("[data-site-share-copy]");
    const share = widget.querySelector("[data-site-share-native]");
    const email = widget.querySelector("[data-site-share-email]");
    const like = widget.querySelector("[data-site-share-like]");
    const status = widget.querySelector("[data-site-share-status]");
    const title = document.title;
    const url = window.location.href;

    if (email) email.href = `mailto:?subject=${encodeURIComponent(title)}&body=${encodeURIComponent(url)}`;
    if (share && !navigator.share) share.hidden = true;
    share?.addEventListener("click", async () => {
      try { await navigator.share({ title, url }); } catch (_) { /* user cancelled */ }
    });
    copy?.addEventListener("click", async () => {
      try { await navigator.clipboard.writeText(url); }
      catch (_) {
        const field = document.createElement("textarea");
        field.value = url;
        field.setAttribute("readonly", "");
        field.style.position = "fixed";
        field.style.opacity = "0";
        document.body.append(field);
        field.select();
        document.execCommand("copy");
        field.remove();
      }
      copy.querySelector("span:last-child").textContent = "Copied";
      if (status) status.textContent = "Link copied to the clipboard.";
      window.setTimeout(() => { copy.querySelector("span:last-child").textContent = "Copy link"; }, 1800);
    });
    const storageKey = `dkh-page-helpful:${window.location.pathname}`;
    let helpful = false;
    try { helpful = window.localStorage.getItem(storageKey) === "true"; } catch (_) { /* storage unavailable */ }
    const setHelpful = (value) => {
      helpful = value;
      like?.setAttribute("aria-pressed", String(helpful));
      if (like) like.querySelector("span:last-child").textContent = helpful ? "Marked helpful" : "Helpful";
      if (status) status.textContent = helpful ? "Marked helpful on this device." : "Helpful marks are stored only on this device.";
    };
    setHelpful(helpful);
    like?.addEventListener("click", () => {
      setHelpful(!helpful);
      try { if (helpful) window.localStorage.setItem(storageKey, "true"); else window.localStorage.removeItem(storageKey); } catch (_) { /* keep page state */ }
    });
  };

  const enhanceReader = () => {
    addPageBreadcrumbs();
    addSiteShare();
    document.querySelectorAll(".note-article, .atlas-page, article.note-detail").forEach((article) => {
      addBreadcrumbs(article);
      addToc(article);
    });
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", enhanceReader, { once: true });
  else enhanceReader();
})();
