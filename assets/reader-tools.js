(() => {
  const normalise = (value) => value.replace(/\s+/g, " ").trim().toLowerCase();
  const sectionForPath = (path) => {
    if (path.startsWith("/services/")) return { label: "Services", href: "/services/" };
    if (path.startsWith("/atlas/")) return { label: "Knowledge Atlas", href: "/atlas/" };
    if (path.startsWith("/blog/")) return { label: "Journal", href: "/blog/" };
    if (path.startsWith("/notes/")) return { label: "Notes", href: "/notes/" };
    return null;
  };

  const addBreadcrumbs = (article) => {
    const heading = article.querySelector("h1");
    if (!heading || article.previousElementSibling?.matches(".breadcrumbs, .note-backlink")) return;

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

    body.before(toc);
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

  const enhanceReader = () => {
    document.querySelectorAll(".note-article, .atlas-page").forEach((article) => {
      addBreadcrumbs(article);
      addToc(article);
    });
  };

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", enhanceReader, { once: true });
  else enhanceReader();
})();
