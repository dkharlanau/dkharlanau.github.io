"""Read-only review signals over ContentPage and emitted HTML; no eligibility policy.

These signals select material for reading. They do not grade truth, originality,
expertise, ranking potential, or inclusion in a recommendation system.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from urllib.robotparser import RobotFileParser
import xml.etree.ElementTree as ET


def prose_lines(body):
    """Exclude fenced code, preserving source line numbers and fence state."""
    body = re.sub(r"(?is)<(pre|code)\b[^>]*>.*?</\1\s*>", lambda match: "\n" * match.group().count("\n"), body)
    lines, fence = [], None
    for number, line in enumerate(body.splitlines(), 1):
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})(.*)$", line)
        if marker:
            run, suffix = marker.groups()
            if fence is None:
                fence = (run[0], len(run), number)
                continue
            if run[0] == fence[0] and len(run) >= fence[1] and not suffix.strip():
                fence = None
                continue
        if fence is None:
            lines.append((number, line))
    return lines, fence


def source_review_signals(pages):
    findings, records, paragraph_owners, body_owners = [], {}, defaultdict(set), defaultdict(list)
    article_models = {"diagnostic", "technical_guide", "architecture", "research", "reference", "opinion", "scenario", "service", "learning_pack"}

    def issue(page, rule, message, remediation, line=""):
        findings.append(dict(path=page.relative_path, rule_id=rule, severity="warning", message=message, remediation=remediation, location=str(line)))

    for page in pages:
        lines, fence = prose_lines(page.body)
        text = "\n".join(line for _, line in lines)
        nonempty = [(n, line) for n, line in lines if line.strip()]
        if fence:
            issue(page, "INTEGRITY001_OPEN_FENCE", "Code fence has no matching closing delimiter; inspect the rendered ending.", "Complete the example after reading its context; do not discard the article.", fence[2])
        if nonempty and re.match(r"^\s{0,3}#{1,6}\s+", nonempty[-1][1]):
            issue(page, "INTEGRITY002_EMPTY_END_SECTION", "The source ends with a heading and no following content.", "Check whether the final section is unfinished or supplied by a template.", nonempty[-1][0])
        for n, line in lines:
            if re.match(r"^\s*(?:TODO|TBD|FIXME|lorem ipsum|\[insert .+\])(?:\s|:|$)", line, re.I):
                issue(page, "INTEGRITY003_DRAFT_MARKER", "A standalone draft marker occurs outside a code fence.", "Read the section and remove only confirmed drafting residue.", n)
                break
        if re.search(r"(?im)^\s*(?:as an ai (?:language )?model|here is (?:the|your) (?:requested|rewritten) article|вот (?:готовая|переписанная) статья|как языковая модель)\b", text):
            issue(page, "INTEGRITY004_GENERATION_RESIDUE", "Possible generation preamble in the article body.", "Check quoted educational examples before editing; remove confirmed authoring residue.")
        # A table separator with a different number of columns is reviewable,
        # but legal Markdown, inline pipes, and one-cell tables need care.
        for i in range(1, len(lines)):
            previous, current = lines[i - 1][1].strip(), lines[i][1].strip()
            if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+\|?", current):
                cells = lambda value: len(re.split(r"(?<!\\)\|", value.strip("|")))
                if cells(previous) != cells(current):
                    issue(page, "INTEGRITY005_TABLE_COLUMNS", "Table header and separator have different column counts.", "Inspect the rendered table; escaped or code-span pipes may explain the signal.", lines[i][0])
        if page.content_model not in article_models:
            continue
        readable = re.sub(r"(?is)<(nav|aside|footer)\b[^>]*>.*?</\1\s*>", "", text)
        readable = re.sub(r"(?is)<h[1-6]\b[^>]*>(.*?)</h[1-6]>", r"\n\n# \1\n\n", readable)
        readable = re.sub(r"(?i)</?(?:p|section|article|ul|ol|li|div)\b[^>]*>", "\n\n", readable)
        readable = html.unescape(re.sub(r"<[^>]+>", "", readable))
        paragraphs = [re.sub(r"\s+", " ", p).strip() for p in re.split(r"\n\s*\n", readable)]
        content_paragraphs = [p for p in paragraphs if not p.startswith(("#", "|", "{%", "<!--")) and len(p.split()) >= 18]
        first_paragraph = next((p for p in paragraphs if p and not p.startswith(("#", "|", "{%", "<!--")) and len(p.split()) >= 18), None)
        evidence = {
            "source_sha256": hashlib.sha256(page.body.encode()).hexdigest(),
            "model": page.content_model,
            "intro_paragraph_present": bool(first_paragraph and re.sub(r"\s+", " ", readable).find(first_paragraph) in range(1400)),
            "example_signal": bool(re.search(r"\b(?:example|for instance|suppose|sample|например|пример)\b", text, re.I)),
            "decision_signal": bool(re.search(r"\b(?:if|when|unless|choose|compare|если|когда|выберите)\b", text, re.I)),
            "boundary_signal": bool(re.search(r"\b(?:limitation|boundary|caveat|risk|depends|does not|cannot|ограничен\w*|риск\w*)\b", text, re.I)),
            "external_reference_count": len(set(re.findall(r"https?://[^\s)<>\"']+", text))),
            "substantive_paragraphs": len(content_paragraphs),
            "review_required": True,
        }
        records[page.relative_path] = evidence
        if page.is_indexable and not evidence["intro_paragraph_present"]:
            issue(page, "SEMANTIC001_INTRO_REVIEW", "No substantial opening paragraph was detected before the first 1,400 source characters.", "Check whether the opening answers the title's question; concise references and include-based pages may be complete.")
        if page.is_indexable and not evidence["example_signal"] and page.content_model in {"diagnostic", "technical_guide", "learning_pack"}:
            issue(page, "SEMANTIC002_EXAMPLE_REVIEW", "No explicit example cue was detected in this practical content model.", "Check for a concrete decision, input/output example, or reproducible check; a keyword alone is not evidence.")
        if page.is_indexable and not evidence["external_reference_count"] and not page.evidence_urls:
            issue(page, "SEMANTIC003_EVIDENCE_REVIEW", "No external reference or evidence URL was detected in the source body.", "Assess whether the page's factual claims need attributable sources or clearly identified first-hand evidence.")
        normalized = re.sub(r"\s+", " ", readable).strip().lower()
        if page.is_indexable and len(normalized.split()) >= 80:
            body_owners[hashlib.sha256(normalized.encode()).hexdigest()].append(page.relative_path)
            for paragraph in content_paragraphs:
                if len(paragraph.split()) >= 40:
                    paragraph_owners[hashlib.sha256(paragraph.lower().encode()).hexdigest()].add(page.relative_path)
    duplicate_bodies = [dict(sha256=key, paths=values) for key, values in body_owners.items() if len(values) > 1]
    repeated_paragraphs = [dict(sha256=key, paths=sorted(values)) for key, values in paragraph_owners.items() if len(values) >= 3]
    return {"findings": findings, "pages": records, "exact_body_candidates": duplicate_bodies, "repeated_paragraph_candidates": repeated_paragraphs, "limits": "No semantic truth/originality score. Shared warnings, legitimate references and template includes require reading. Fuzzy plagiarism is not assessed."}


class RenderedPage(HTMLParser):
    """Inspect real HTML links and metadata, excluding navigation from body graph."""
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.stack, self.meta, self.links, self.text, self.jsonld = [], {}, [], [], []
        self.canonical, self.script, self.main_seen = "", None, False
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            key = (attrs.get("name") or attrs.get("property") or "").lower()
            if key:
                self.meta[key] = attrs.get("content", "")
        if tag == "link" and "canonical" in attrs.get("rel", "").split():
            self.canonical = attrs.get("href", "")
        if tag == "main":
            self.main_seen = True
        context = self.stack + [tag]
        in_main = "main" in context and not any(item in context for item in ("nav", "footer", "aside", "script", "style", "template"))
        if tag == "a" and attrs.get("href"):
            self.links.append((attrs["href"], in_main))
        if tag == "script" and attrs.get("type", "").lower() == "application/ld+json":
            self.script = []
        if tag not in self.VOID:
            self.stack.append(tag)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in self.VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "script" and self.script is not None:
            self.jsonld.append("".join(self.script))
            self.script = None
        if tag in self.stack:
            self.stack = self.stack[:len(self.stack) - 1 - self.stack[::-1].index(tag)]

    def handle_data(self, text):
        if self.script is not None:
            self.script.append(text)
        if "main" in self.stack and not any(tag in self.stack for tag in ("nav", "footer", "aside", "script", "style", "template")):
            self.text.append(text)


def local_path(url, base):
    parsed = urlsplit(urljoin(base, url))
    if parsed.scheme not in {"http", "https"} or parsed.netloc != urlsplit(base).netloc:
        return None
    return unquote(parsed.path).rstrip("/") or "/"


def rendered_review(site_dir, pages, base):
    """Observe emitted policy; source eligibility still comes from ContentPage."""
    site_dir = site_dir.resolve()
    files, parsed, inbound, issues = {}, {}, Counter(), []
    manifest = hashlib.sha256()
    for path in sorted(site_dir.rglob("*.html")):
        rel = path.relative_to(site_dir).as_posix()
        data = path.read_bytes()
        manifest.update(rel.encode() + b"\0" + hashlib.sha256(data).digest())
        route = "/" + rel.removesuffix("index.html") if rel.endswith("index.html") else "/" + rel.removesuffix(".html")
        route = route.rstrip("/") or "/"
        files[route] = rel
        parsed[route] = RenderedPage(data.decode("utf-8", errors="replace"))
    edges = set()
    for route, doc in parsed.items():
        for target, main in doc.links:
            destination = local_path(target, base + route + "/")
            if main and destination in parsed and destination != route:
                edges.add((route, destination))
    for _, destination in edges:
        inbound[destination] += 1

    sitemap_urls, sitemap_files, seen = [], [], set()

    def read_sitemap(path):
        if path in seen:
            return
        seen.add(path)
        sitemap_files.append(path.relative_to(site_dir).as_posix())
        try:
            root = ET.fromstring(path.read_bytes())
        except (OSError, ET.ParseError):
            issues.append({"rule_id": "DISCOVERY001_SITEMAP_UNREADABLE", "severity": "error", "path": path.relative_to(site_dir).as_posix()})
            return
        if root.tag.split("}")[-1] == "sitemapindex":
            for loc in root.findall("{*}sitemap/{*}loc"):
                route = local_path(loc.text or "", base)
                child = (site_dir / (route or "").lstrip("/")).resolve()
                if route is not None and child.is_relative_to(site_dir.resolve()):
                    read_sitemap(child)
                else:
                    issues.append({"rule_id": "DISCOVERY002_EXTERNAL_SITEMAP", "severity": "warning", "path": sitemap_files[-1]})
        else:
            sitemap_urls.extend(loc.text.strip() for loc in root.findall("{*}url/{*}loc") if loc.text)
    read_sitemap(site_dir / "sitemap.xml")
    noindex_listed, noncanonical_listed, unresolved = [], [], []
    for url in sitemap_urls:
        route = local_path(url, base)
        doc = parsed.get(route)
        if doc is None:
            # Non-HTML sitemap entries can be legitimate resources.
            if route is None or not (site_dir / route.lstrip("/")).is_file():
                unresolved.append(url)
            continue
        if "noindex" in doc.meta.get("robots", "").lower():
            noindex_listed.append(url)
        if doc.canonical and doc.canonical.rstrip("/") != url.rstrip("/"):
            noncanonical_listed.append(url)
    for rule, values in [("DISCOVERY003_NOINDEX_SITEMAP", noindex_listed), ("DISCOVERY004_CANONICAL_SITEMAP", noncanonical_listed), ("DISCOVERY005_MISSING_SITEMAP_TARGET", unresolved)]:
        for url in values:
            issues.append({"rule_id": rule, "severity": "error", "path": urlsplit(url).path})
    robots = RobotFileParser()
    robot_path = site_dir / "robots.txt"
    robot_exists = robot_path.is_file()
    if robot_exists:
        robots.parse(robot_path.read_text().splitlines())
    article_records = []
    for page in pages:
        if not page.is_indexable or not page.permalink:
            continue
        route = local_path(page.canonical_url, base)
        doc = parsed.get(route)
        if doc is None:
            continue
        article_records.append({"source_path": page.relative_path, "url": page.canonical_url, "model": page.content_model, "main_present": doc.main_seen, "main_text_characters": len(" ".join(doc.text).strip()), "contextual_inbound_pages": inbound[route], "main_outbound_pages": sum(src == route for src, _ in edges), "snippet_limited": bool(re.search(r"nosnippet|max-snippet\s*:\s*0\b", doc.meta.get("robots", ""), re.I)), "large_image_preview": "max-image-preview:large" in doc.meta.get("robots", "").replace(" ", "").lower(), "og_image": doc.meta.get("og:image", ""), "crawl_policy": {bot: robots.can_fetch(bot, page.canonical_url) if robot_exists else None for bot in ("Googlebot", "OAI-SearchBot", "Bingbot")}, "jsonld_blocks": len(doc.jsonld)})
    return {"html_files": len(parsed), "html_manifest_sha256": manifest.hexdigest(), "sitemap": {"files": sitemap_files, "urls": len(sitemap_urls), "duplicates": len(sitemap_urls) - len(set(sitemap_urls)), "noindex": noindex_listed, "noncanonical": noncanonical_listed, "unresolved": unresolved}, "robots_file_present": robot_exists, "contextual_edges": len(edges), "source_indexable_pages_observed": len(article_records), "pages": article_records, "issues": issues, "limits": "Local artifacts only: no HTTP/WAF or actual indexing check. HTML graph excludes nav/footer/aside but a main-body related block is still contextual. Image dimensions and relevance require visual review. No AI/Discover inclusion guarantee."}
