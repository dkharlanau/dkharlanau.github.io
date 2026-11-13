"""Canonical HTML fingerprints for the IndexNow production release workflow."""

from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.error import HTTPError
from urllib.parse import unquote, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener
import xml.etree.ElementTree as ET

SCHEMA = "atlas.indexnow-release.v1"
GENERATOR = "atlas.rendered-html.v1"
SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"
NOINDEX = re.compile(r"\b(noindex|none)\b", re.I)
DIGEST = re.compile(r"[a-f0-9]{64}")
STRUCTURE = frozenset("h1 h2 h3 h4 h5 h6 table thead tbody tfoot tr th td caption ol ul li".split())
NON_HTML = frozenset(".json .jsonld .yml .yaml .xml .txt .md .csv .pdf .xlsx .epub .zip .svg .png .webp .jpg .jpeg .js .css".split())


def digest(value):
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def canonical_path(url, origin):
    parsed = urlsplit(url)
    path = unquote(parsed.path)
    if (not url.startswith(origin + "/") or parsed.query or parsed.fragment
            or parsed.netloc != urlsplit(origin).netloc or path.startswith("//")
            or any(part in (".", "..") for part in path.split("/"))
            or "\\" in path or any(ord(ch) < 32 for ch in path)):
        raise ValueError(f"Invalid canonical URL: {url}")
    return path


class SearchDocument(HTMLParser):
    """Keep search-facing metadata and main content independent of site chrome."""

    def __init__(self, html):
        super().__init__()
        self.canonicals, self.robots, self.parts = [], [], []
        self.in_head = self.in_main = self.has_main = self.in_title = self.ignored = False
        self.jsonld = None
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "head":
            self.in_head = True
        elif tag == "main":
            self.in_main = self.has_main = True
        elif tag == "title":
            self.in_title = self.in_head
        elif tag == "link" and "canonical" in (attrs.get("rel") or "").lower().split():
            self.canonicals.append(attrs.get("href"))
        elif tag == "meta":
            name = (attrs.get("name") or attrs.get("property") or "").lower()
            content = attrs.get("content") or ""
            if name in {"robots", "googlebot", "bingbot"}:
                self.robots.append(content)
            if name in {"description", "robots", "googlebot", "bingbot"} or name.startswith(("og:", "twitter:")):
                self.parts.append(("meta", name, content))
        elif tag in {"script", "style", "template"}:
            self.ignored = True
            if tag == "script" and (attrs.get("type") or "").lower() == "application/ld+json":
                self.jsonld = []
        elif self.in_main and not self.ignored:
            if tag == "a":
                self.parts.append((tag, attrs.get("href"), attrs.get("rel")))
            elif tag == "img":
                self.parts.append((tag, attrs.get("src"), attrs.get("srcset"), attrs.get("alt")))
            elif tag in STRUCTURE:
                self.parts.append((tag, attrs.get("id"), attrs.get("scope"), attrs.get("colspan"), attrs.get("rowspan")))

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False
        elif tag == "main":
            self.in_main = False
        elif tag == "title":
            self.in_title = False
        elif tag in {"script", "style", "template"}:
            self.ignored = False
            if tag == "script" and self.jsonld is not None:
                self.parts.append(("jsonld", json.loads("".join(self.jsonld))))
                self.jsonld = None
        elif self.in_main and not self.ignored and tag in STRUCTURE:
            self.parts.append(("/" + tag,))

    def handle_data(self, data):
        if self.jsonld is not None:
            self.jsonld.append(data)
        if not self.ignored and (self.in_main or self.in_title):
            text = " ".join(data.split())
            if text:
                self.parts.append(text)

    def indexable(self, url, response_robots=""):
        return self.has_main and self.canonicals == [url] and not self.noindex(response_robots)

    def noindex(self, response_robots=""):
        return any(NOINDEX.search(value) for value in [response_robots, *self.robots])


def sitemap_dates(site_dir, origin):
    entries, seen, active = {}, set(), set()

    def read(name):
        if name in active:
            raise ValueError(f"Cyclic sitemap: {name}")
        if name in seen:
            return
        active.add(name)
        root = ET.parse(site_dir / name).getroot()
        if root.tag == SITEMAP_NS + "sitemapindex":
            for child in root.findall(SITEMAP_NS + "sitemap"):
                loc = child.findtext(SITEMAP_NS + "loc", default="").strip()
                path = canonical_path(loc, origin)
                if not re.fullmatch(r"/sitemap[\w.-]*\.xml", path):
                    raise ValueError(f"Unexpected sitemap path: {loc}")
                read(path[1:])
        elif root.tag == SITEMAP_NS + "urlset":
            for entry in root.findall(SITEMAP_NS + "url"):
                loc = entry.findtext(SITEMAP_NS + "loc", default="").strip()
                canonical_path(loc, origin)
                date = entry.findtext(SITEMAP_NS + "lastmod")
                if loc in entries and entries[loc] != date:
                    raise ValueError(f"Conflicting sitemap dates: {loc}")
                entries[loc] = date
        else:
            raise ValueError(f"Invalid sitemap root: {name}")
        active.remove(name)
        seen.add(name)

    read("sitemap.xml")
    if not entries:
        raise ValueError("Empty sitemap inventory")
    return entries


def build_manifest(site_dir, origin, commit, artifact=None):
    if not re.fullmatch(r"[a-f0-9]{40}", commit):
        raise ValueError("Expected a full Git commit SHA")
    pages = {}
    for url, date in sorted(sitemap_dates(site_dir, origin).items()):
        path = canonical_path(url, origin)
        suffix = Path(path).suffix.lower()
        if suffix in NON_HTML:
            continue
        file = site_dir / path.lstrip("/")
        if path.endswith("/") or file.is_dir():
            file = file / "index.html"
        elif suffix != ".html":
            file = file.with_name(file.name + ".html")
        if not file.is_file():
            raise ValueError(f"Missing sitemap HTML: {url}")
        document = SearchDocument(file.read_text(encoding="utf-8"))
        if not document.indexable(url):
            raise ValueError(f"Sitemap HTML lacks a unique self-canonical, indexable main: {url}")
        pages[url] = {"signature": digest(document.parts), "lastmod": date}
    if not pages:
        raise ValueError("No canonical HTML in sitemap")
    result = {"schema": SCHEMA, "generator": GENERATOR, "origin": origin, "commit": commit, "artifact": artifact, "pages": pages}
    return {**result, "digest": digest(result)}


def load_manifest(file, origin):
    manifest = json.loads(file.read_text(encoding="utf-8"))
    content = {key: value for key, value in manifest.items() if key != "digest"}
    if (manifest.get("schema") != SCHEMA or manifest.get("generator") != GENERATOR
            or manifest.get("origin") != origin or manifest.get("digest") != digest(content)):
        raise ValueError("Incompatible release manifest")
    if not isinstance(manifest.get("pages"), dict) or not manifest["pages"]:
        raise ValueError("Empty release manifest")
    for url, page in manifest["pages"].items():
        canonical_path(url, origin)
        if not DIGEST.fullmatch(page["signature"]):
            raise ValueError(f"Invalid page signature: {url}")
    return manifest


def compare(before, after):
    old, new = before["pages"], after["pages"]
    both = old.keys() & new.keys()
    return {
        "added": sorted(new.keys() - old.keys()),
        "changed": sorted(url for url in both if old[url]["signature"] != new[url]["signature"]),
        "deleted": sorted(old.keys() - new.keys()),
        "changed_lastmod": sorted(url for url in both if old[url]["lastmod"] != new[url]["lastmod"]),
    }


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def read_live(url):
    request = Request(url, headers={"Cache-Control": "no-cache", "User-Agent": "Atlas IndexNow release verification"})
    try:
        with build_opener(NoRedirect()).open(request, timeout=15) as response:
            return response.status, response.headers, response.read().decode("utf-8")
    except HTTPError as error:
        with error:
            return error.code, error.headers, ""


def verify_live(url, page, fetch=read_live):
    status, headers, html = fetch(url)
    if page is None and status in {301, 302, 303, 307, 308, 404, 410}:
        return True
    if status != 200 or not headers.get("Content-Type", "").lower().startswith("text/html"):
        raise ValueError(f"Unexpected live response {status}: {url}")
    document = SearchDocument(html)
    robots = ", ".join(headers.get_all("X-Robots-Tag", []))
    if page is None:
        return document.noindex(robots)
    if not document.indexable(url, robots) or digest(document.parts) != page["signature"]:
        raise ValueError(f"Live canonical HTML differs from the release: {url}")
    return True
