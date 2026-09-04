(() => {
  const normalise = (value) => value.replace(/\s+/g, " ").trim().toLowerCase();
  const sectionForPath = (path) => {
    if (path.startsWith("/labs/interview-readiness/")) return { label: "Career", href: "/labs/interview-readiness/" };
    if (path.startsWith("/labs/assessment/")) return { label: "Career", href: "/labs/interview-readiness/" };
    if (path.startsWith("/labs/")) return { label: "Labs", href: "/labs/" };
    if (path.startsWith("/frameworks/")) return { label: "Frameworks", href: "/frameworks/" };
    if (path.startsWith("/triz/") || path.startsWith("/ddd/") || path.startsWith("/reusable-data-procedures/")) return { label: "Frameworks", href: "/frameworks/" };
    if (path.startsWith("/machine/") || path.startsWith("/ai/") || path.startsWith("/agent-tools/") || path.startsWith("/agent-skills/") || path.startsWith("/mcp/")) return { label: "Machine", href: "/machine/" };
    if (path.startsWith("/services/")) return { label: "Services", href: "/services/" };
    if (path.startsWith("/scenarios/")) return { label: "Scenarios", href: "/scenarios/" };
    if (path.startsWith("/atlas/")) return { label: "Knowledge Atlas", href: "/atlas/" };
    if (path.startsWith("/blog/")) return { label: "Journal", href: "/blog/" };
    if (path.startsWith("/notes/")) return { label: "Notes", href: "/notes/" };
    if (path.startsWith("/research/")) return { label: "Research", href: "/research/" };
    if (path.startsWith("/datasets/")) return { label: "Datasets", href: "/datasets/" };
    if (path.startsWith("/skill-hub/")) return { label: "Machine", href: "/machine/" };
    if (path.startsWith("/news/")) return { label: "Signals", href: "/news/" };
    if (path.startsWith("/radar/")) return { label: "Radar", href: "/radar/" };
    if (path === "/about/" || path.startsWith("/cv/") || path === "/certifications/" || path === "/education/" || path === "/publications/") return { label: "Profile", href: "/about/" };
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

  const normaliseFlatSkillArticle = (article) => {
    if (!window.location.pathname.startsWith("/skill-hub/") || !article.matches(".atlas-page")) return;
    if (article.querySelector(":scope > .note-header, :scope > .note-body")) return;

    const eyebrow = article.querySelector(":scope > .eyebrow");
    const heading = article.querySelector(":scope > h1");
    const lead = article.querySelector(":scope > .lead");
    if (!heading) return;

    const header = document.createElement("header");
    header.className = "note-header skill-reader__header";
    article.insertBefore(header, article.firstChild);
    [eyebrow, heading, lead].filter(Boolean).forEach((node) => header.append(node));

    const body = document.createElement("div");
    body.className = "note-body skill-reader__body";
    [...article.children].filter((node) => node !== header).forEach((node) => body.append(node));
    article.append(body);
    article.classList.add("reader-structure--normalised");
  };

  const addToc = (article) => {
    const body = article.querySelector(":scope > .note-body");
    if (!body || article.querySelector(":scope > .reader-toc")) return;

    const allHeadings = [...body.querySelectorAll("h2")];
    const sourceHeading = allHeadings[0];
    const sourceList = sourceHeading?.nextElementSibling;
    const hasSourceToc = normalise(sourceHeading?.textContent || "") === "on this page" && sourceList?.tagName === "UL";
    const eligibleHeadings = allHeadings.filter((heading) => heading !== sourceHeading || !hasSourceToc);
    const tocLimit = 12;
    const headings = eligibleHeadings.slice(0, tocLimit);
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
    summary.textContent = eligibleHeadings.length > tocLimit
      ? `On this page (${headings.length} key sections)`
      : `On this page (${headings.length})`;

    if (hasSourceToc) {
      sourceHeading.classList.add("reader-toc__visually-hidden");
      [...sourceList.children].slice(tocLimit).forEach((item) => item.remove());
      if (eligibleHeadings.length > tocLimit) {
        const remainder = document.createElement("li");
        remainder.className = "reader-toc__remainder";
        remainder.textContent = `${eligibleHeadings.length - tocLimit} additional sections continue in the article.`;
        sourceList.append(remainder);
      }
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

  const readerVisualForPath = (path) => {
    const visual = (src, alt, caption) => ({ src, alt, caption });

    if (path.startsWith("/scenarios/") && path !== "/scenarios/") {
      if (/ai-|ai-ready|pilot/.test(path)) return visual(
        "/assets/img/systems/ai-evidence-boundary-field.webp",
        "Operational evidence entering a bounded AI synthesis layer, then separating into approved action and human-review routes with an audit trail.",
        "Evidence → AI boundary → human review → controlled action."
      );
      if (/master-data|bp-|vendor|supplier|mdg|duplicate/.test(path)) return visual(
        "/assets/img/systems/master-data-lineage-field.webp",
        "Several master-data sources passing through identity and quality gates into one governed record and trusted downstream routes.",
        "Source records → quality and ownership gates → governed reuse."
      );
      if (/delivery|billing|invoice|planning|replenishment|fulfilment/.test(path)) return visual(
        "/assets/img/systems/logistics-fulfilment-field.webp",
        "An order moving through availability, warehouse execution, transport, delivery confirmation, and an operational feedback loop.",
        "Order → availability → warehouse → transport → proof of delivery."
      );
      if (/ams|incident|support-cost|knowledge-loss/.test(path)) return visual(
        "/assets/img/systems/workflow-exception-field.webp",
        "A workflow exception leaving the main operating route for evidence review before returning through a controlled decision gate.",
        "Recurring work → exception evidence → decision → controlled re-entry."
      );
      return visual(
        "/assets/img/systems/erp-document-flow-field.webp",
        "A business signal moving through ERP documents, data checks, warehouse execution, integration, and delivery confirmation.",
        "Business symptom → ERP context → evidence → defensible decision."
      );
    }

    if (path.startsWith("/atlas/")) {
      if (/data-quality|master-data|data-governance/.test(path)) return visual(
        "/assets/img/systems/master-data-lineage-field.webp",
        "Source records passing through identity, validation, and ownership checks into a governed data core with visible downstream lineage.",
        "Source → lineage and quality → governed operational use."
      );
      if (/ai-operations|automation|agent|retrieval/.test(path)) return visual(
        "/assets/img/systems/ai-evidence-boundary-field.webp",
        "Documents, events, and structured records entering a bounded AI synthesis layer with review and audit routes.",
        "Evidence → synthesis boundary → review → controlled use."
      );
      if (/logistics|warehouse|delivery|inventory|procurement/.test(path)) return visual(
        "/assets/img/systems/logistics-fulfilment-field.webp",
        "An order passing through availability, warehouse execution, transport, delivery confirmation, and a feedback route.",
        "Demand → fulfilment → proof of completion."
      );
      return visual(
        "/assets/img/systems/erp-document-flow-field.webp",
        "An ERP operating signal branching through document, data, warehouse, and integration evidence before reaching a business outcome.",
        "Use the page as an operating route: signal, evidence, decision, outcome."
      );
    }

    if (!path.startsWith("/services/") || path === "/services/") return null;
    if (/ams|incident|reliability/.test(path)) return {
      src: "/assets/img/systems/workflow-exception-field.webp",
      alt: "A repeated workflow exception routed into an evidence-and-review loop before it returns through a controlled decision gate.",
      caption: "Recurring work → exception evidence → ownership → prevention."
    };
    if (/master-data|data/.test(path)) return {
      src: "/assets/img/systems/master-data-lineage-field.webp",
      alt: "Several source records passing through identity, quality, and ownership gates into one governed record with visible downstream lineage.",
      caption: "Trace the decision through source, lineage, quality, ownership and reuse."
    };
    if (/ai-|enterprise-ai|pilot/.test(path)) return {
      src: "/assets/img/systems/ai-evidence-boundary-field.webp",
      alt: "Operational evidence entering a bounded AI synthesis layer, then separating into approved action and human-review routes with an audit trail.",
      caption: "Keep evidence, review authority and the action boundary visible."
    };
    if (/o2c|planning|replenishment|logistics|fulfilment/.test(path)) return {
      src: "/assets/img/systems/logistics-fulfilment-field.webp",
      alt: "An order passing through availability, warehouse execution, transport, delivery confirmation, and a feedback route.",
      caption: "Keep the fulfilment flow visible from demand to proof of completion."
    };
    if (/integration/.test(path)) return {
      src: "/assets/img/systems/erp-document-flow-field.webp",
      alt: "A business signal moving through ERP documents, data checks, warehouse execution, integration, and delivery confirmation.",
      caption: "Keep the business flow visible across document and system boundaries."
    };
    return {
      src: "/assets/img/systems/workflow-exception-field.webp",
      alt: "An operating workflow with one exception routed through evidence review before returning to a controlled outcome.",
      caption: "Start from the work, exception and evidence before selecting the intervention."
    };
  };

  const addReaderVisual = (article) => {
    const header = article.querySelector(":scope > .note-header");
    if (!header || header.querySelector(":scope > .reader-visual")) return;
    const visual = readerVisualForPath(window.location.pathname);
    if (!visual) return;

    const figure = document.createElement("figure");
    figure.className = "reader-visual";
    const image = document.createElement("img");
    image.src = visual.src;
    image.alt = visual.alt;
    image.width = 1728;
    image.height = /ai-evidence-boundary|workflow-exception/.test(visual.src) ? 1081 : 1106;
    image.decoding = "async";
    image.fetchPriority = "high";
    const caption = document.createElement("figcaption");
    caption.textContent = visual.caption;
    figure.append(image, caption);
    header.append(figure);
    header.classList.add("note-header--visual");
  };

  const consolidateAtlasSourceBrief = (article) => {
    if (!article.matches(".atlas-page")) return;
    const rail = article.querySelector(":scope > .atlas-meta-panel");
    if (!rail || rail.querySelector(":scope > .atlas-source-brief")) return;

    let cursor = article.previousElementSibling;
    if (cursor?.matches(".breadcrumbs, .reader-breadcrumbs, .ps-breadcrumbs")) cursor = cursor.previousElementSibling;
    const sourceParagraphs = [];
    while (cursor?.tagName === "P" && /(?:^|\s)(?:Sources|Date checked|Confidence|Practical implication):/i.test(cursor.textContent)) {
      sourceParagraphs.unshift(cursor);
      cursor = cursor.previousElementSibling;
    }
    if (!sourceParagraphs.length) return;

    const disclosure = document.createElement("details");
    disclosure.className = "atlas-source-brief";
    const summary = document.createElement("summary");
    summary.textContent = "Evidence and source note";
    const body = document.createElement("div");
    body.className = "atlas-source-brief__body";
    sourceParagraphs.forEach((paragraph) => body.append(paragraph));
    disclosure.append(summary, body);
    rail.append(disclosure);
  };

  const pageReference = () => {
    const widget = document.querySelector("[data-site-share]");
    // The build supplies the production origin, including during a local preview.
    // Never promote a location query or an external canonical into a shared URL.
    let origin;
    try {
      origin = new URL(widget?.dataset.siteShareOrigin);
      if (origin.protocol !== "https:" || origin.username || origin.password) return null;
    } catch (_) { return null; }
    const validUrl = (value) => {
      if (!value?.trim()) return null;
      try {
        const url = new URL(value, origin);
        if (url.origin !== origin.origin || url.protocol !== "https:" || url.username || url.password) return null;
        url.search = "";
        url.hash = "";
        return url;
      } catch (_) { return null; }
    };
    const canonical = validUrl(document.querySelector('link[rel="canonical"]')?.getAttribute("href"))
      || validUrl(widget.dataset.siteShareUrl);
    if (!canonical) return null;
    const url = new URL(canonical);
    // A heading on this route is safe to reference. Alias pages can have different
    // anchors, so citations and links to their canonical target remain page-level.
    if (window.location.pathname === canonical.pathname && window.location.hash) {
      try {
        const heading = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
        if (heading?.matches("h1, h2, h3, h4, h5, h6") && document.querySelector("#content")?.contains(heading)) {
          url.hash = window.location.hash;
        }
      } catch (_) { /* malformed or unknown fragments are not shared */ }
    }
    const title = widget.dataset.siteShareTitle || document.title;
    const author = widget.dataset.siteShareAuthor || document.querySelector('meta[name="author"]')?.content;
    const modified = document.querySelector('meta[property="article:modified_time"]')?.content || "";
    const date = modified.match(/^\d{4}-\d{2}-\d{2}(?=T|$)/)?.[0];
    const validDate = date && !Number.isNaN(Date.parse(modified)) && new Date(date).toISOString().slice(0, 10) === date;
    const citation = [author, `“${title}”`, validDate ? `Updated ${date}` : null, canonical.href].filter(Boolean).join(". ");
    return { title, url: url.href, canonical: canonical.href, citation };
  };

  const copyText = async (text) => {
    try {
      if (navigator.clipboard?.writeText) {
        await navigator.clipboard.writeText(text);
        return true;
      }
    } catch (_) { /* try the browser's legacy copy command */ }
    const active = document.activeElement;
    const field = document.createElement("textarea");
    field.value = text;
    field.readOnly = true;
    field.tabIndex = -1;
    field.className = "reader-copy-buffer";
    document.body.append(field);
    try {
      field.select();
      return document.execCommand?.("copy") === true;
    } catch (_) { return false; }
    finally {
      field.remove();
      // A copy trigger can be disabled while this command runs. Its caller
      // restores focus after re-enabling it; another focused control stays put.
      if (!active?.disabled) active?.focus({ preventScroll: true });
    }
  };

  const offerManualCopy = (container, text, trigger, focus = true) => {
    let panel = container.querySelector(".reader-copy-fallback");
    if (!panel) {
      panel = document.createElement("div");
      panel.className = "reader-copy-fallback";
      const label = document.createElement("label");
      label.textContent = "Select and copy manually";
      const field = document.createElement("textarea");
      field.readOnly = true;
      field.rows = 3;
      label.append(field);
      const note = document.createElement("p");
      note.textContent = "Copy the selected text using your browser or keyboard.";
      const close = document.createElement("button");
      close.type = "button";
      close.className = "site-share__action";
      close.textContent = "Close";
      close.addEventListener("click", () => {
        panel.hidden = true;
        panel.copyTrigger?.focus();
      });
      panel.append(label, note, close);
      container.append(panel);
    }
    panel.copyTrigger = trigger;
    panel.hidden = false;
    const field = panel.querySelector("textarea");
    field.value = text;
    if (focus) {
      field.focus();
      field.select();
    }
  };

  const bindCopy = (button, container, status, referenceText, kind) => {
    if (!button) return;
    button.hidden = false;
    button.addEventListener("click", async () => {
      const text = referenceText();
      if (!text) {
        if (status) status.textContent = "A permanent link is unavailable for this page.";
        return;
      }
      const activeBeforeCopy = document.activeElement;
      let focusMoved = false;
      const trackFocus = (event) => {
        if (event.target !== activeBeforeCopy && event.target !== document.body && !event.target.matches?.(".reader-copy-buffer")) {
          focusMoved = true;
        }
      };
      document.addEventListener("focusin", trackFocus);
      button.disabled = true;
      if (status) status.textContent = "Copying…";
      try {
        const copied = await copyText(text);
        button.disabled = false;
        document.removeEventListener("focusin", trackFocus);
        if (copied) {
          const panel = container.querySelector(".reader-copy-fallback");
          if (panel) panel.hidden = true;
          if (status) status.textContent = `${kind} copied to the clipboard.`;
          if (!focusMoved) activeBeforeCopy?.focus({ preventScroll: true });
        } else {
          if (status) status.textContent = "Automatic copy is unavailable. Copy the selected text below.";
          offerManualCopy(container, text, button, !focusMoved);
        }
      } finally {
        button.disabled = false;
        document.removeEventListener("focusin", trackFocus);
      }
    });
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

    const status = document.createElement("p");
    status.className = "reader-reaction-note";
    status.setAttribute("aria-live", "polite");
    status.setAttribute("aria-atomic", "true");

    const makeButton = (icon, text) => {
      const button = document.createElement("button");
      button.className = "reader-action";
      button.type = "button";
      button.innerHTML = `<span class="material-symbols-outlined" aria-hidden="true">${icon}</span><span>${text}</span>`;
      return button;
    };

    const copy = makeButton("link", "Copy link");
    bindCopy(copy, actions, status, () => pageReference()?.url, "Link");
    actions.append(copy);
    const citation = makeButton("format_quote", "Copy citation");
    bindCopy(citation, actions, status, () => pageReference()?.citation, "Citation");
    actions.append(citation);

    if (navigator.share) {
      const share = makeButton("ios_share", "Share");
      share.addEventListener("click", async () => {
        const reference = pageReference();
        if (!reference) return;
        try { await navigator.share({ title: reference.title, url: reference.url }); }
        catch (error) {
          if (error?.name !== "AbortError") status.textContent = "Sharing is unavailable. Use Copy link instead.";
        }
      });
      actions.append(share);
    }

    const linkedIn = document.createElement("a");
    linkedIn.className = "reader-action";
    linkedIn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(pageReference()?.url || "")}`;
    linkedIn.addEventListener("click", (event) => {
      const reference = pageReference();
      if (reference) linkedIn.href = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(reference.url)}`;
      else event.preventDefault();
    });
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
    actions.append(note, status);

    const header = article.querySelector(":scope > .note-header");
    if (header) header.append(actions);
    else heading.insertAdjacentElement("afterend", actions);
  };

  const addSiteShare = () => {
    const widget = document.querySelector("[data-site-share]");
    if (!widget) return;
    const copy = widget.querySelector("[data-site-share-copy]");
    const citation = widget.querySelector("[data-site-share-citation]");
    const share = widget.querySelector("[data-site-share-native]");
    const email = widget.querySelector("[data-site-share-email]");
    const like = widget.querySelector("[data-site-share-like]");
    const status = widget.querySelector("[data-site-share-status]");
    const refreshEmail = () => {
      const reference = pageReference();
      if (email && reference) email.href = `mailto:?subject=${encodeURIComponent(reference.title)}&body=${encodeURIComponent(reference.url)}`;
    };
    refreshEmail();
    window.addEventListener("hashchange", refreshEmail);
    // TOC enhancement may create the target heading after widget setup. Refresh
    // on activation as well, including keyboard activation of the mailto link.
    email?.addEventListener("click", refreshEmail);
    if (share) share.hidden = typeof navigator.share !== "function";
    share?.addEventListener("click", async () => {
      const reference = pageReference();
      if (!reference) return;
      try { await navigator.share({ title: reference.title, url: reference.url }); }
      catch (error) {
        if (error?.name !== "AbortError" && status) status.textContent = "Sharing is unavailable. Use Copy link or Send by email.";
      }
    });
    bindCopy(copy, widget, status, () => pageReference()?.url, "Link");
    bindCopy(citation, widget, status, () => pageReference()?.citation, "Citation");
    const storageKey = `dkh-page-helpful:${window.location.pathname}`;
    let helpful = false;
    let storageAvailable = true;
    try { helpful = window.localStorage.getItem(storageKey) === "true"; } catch (_) { storageAvailable = false; }
    const setHelpful = (value) => {
      helpful = value;
      like?.setAttribute("aria-pressed", String(helpful));
      if (like) like.querySelector("span:last-child").textContent = helpful ? "Marked helpful" : "Helpful";
      if (status) status.textContent = storageAvailable
        ? (helpful ? "Marked helpful on this device." : "Helpful marks are stored only on this device.")
        : (helpful ? "Marked helpful for this visit. Device storage is unavailable." : "Helpful marks last for this visit because device storage is unavailable.");
    };
    setHelpful(helpful);
    if (like) like.hidden = false;
    like?.addEventListener("click", () => {
      const next = !helpful;
      try { if (next) window.localStorage.setItem(storageKey, "true"); else window.localStorage.removeItem(storageKey); }
      catch (_) { storageAvailable = false; }
      setHelpful(next);
    });
  };

  const enhanceReader = () => {
    addPageBreadcrumbs();
    addSiteShare();
    if (document.querySelector(".article-disclosure")) {
      document.querySelectorAll("p.disclaimer").forEach((paragraph) => {
        if (!paragraph.closest(".article-disclosure")) paragraph.remove();
      });
    }
    document.querySelectorAll(".note-article, .atlas-page, article.note-detail").forEach((article) => {
      normaliseFlatSkillArticle(article);
      addBreadcrumbs(article);
      addReaderVisual(article);
      consolidateAtlasSourceBrief(article);
      addToc(article);
    });
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", enhanceReader, { once: true });
  else enhanceReader();
})();
