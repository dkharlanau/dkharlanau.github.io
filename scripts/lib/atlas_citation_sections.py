"""Project explicit, visible Atlas sections into the existing retrieval exports."""

from hashlib import sha256
from html.parser import HTMLParser
import json
import re
from urllib.parse import urlsplit


class CitationSections(HTMLParser):
    def __init__(self, anchors):
        super().__init__(convert_charrefs=True)
        self.anchors = set(anchors)
        self.sections = {}
        self.active = None
        self.element = None
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        hidden = "hidden" in attrs or attrs.get("aria-hidden") == "true"
        if self.active is None:
            anchor = attrs.get("id")
            if anchor not in self.anchors:
                return
            if tag != "section" or hidden or anchor in self.sections:
                raise ValueError(f"Expected one visible section with ID {anchor}")
            self.active = {"anchor": anchor, "heading": "", "paragraphs": [], "sources": []}
            self.sections[anchor] = self.active
            return
        if tag in {"section", "script", "style", "template", "details"} or hidden:
            raise ValueError(f"Unsupported or hidden content in #{self.active['anchor']}")
        if tag in {"h2", "p", "li"}:
            if self.element is not None:
                raise ValueError(f"Nested citation text in #{self.active['anchor']}")
            self.element = tag
            self.chunks = []
        if tag == "a" and self.element and attrs.get("href"):
            href = attrs["href"]
            parts = urlsplit(href)
            if parts.scheme == "https" and parts.hostname and not (parts.username or parts.password):
                if href not in self.active["sources"]:
                    self.active["sources"].append(href)

    def handle_data(self, data):
        if self.active is not None and self.element is not None:
            if "{%" in data or "{{" in data:
                raise ValueError(f"Template expressions are unsupported in #{self.active['anchor']}")
            self.chunks.append(data)

    def handle_endtag(self, tag):
        if self.active is None:
            return
        if tag == self.element:
            text = " ".join("".join(self.chunks).split())
            if tag == "h2":
                if self.active["heading"]:
                    raise ValueError(f"Multiple headings in #{self.active['anchor']}")
                self.active["heading"] = text
            elif text:
                self.active["paragraphs"].append(text)
            self.element = None
        if tag == "section":
            if self.element is not None:
                raise ValueError(f"Unclosed citation text in #{self.active['anchor']}")
            self.active = None


def read_atlas_citation_sections(body, anchors, canonical):
    if anchors is None:
        return []
    if not isinstance(anchors, list) or any(
        not isinstance(anchor, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", anchor)
        for anchor in anchors
    ) or len(set(anchors)) != len(anchors):
        raise ValueError(f"{canonical}: invalid or duplicate citation section IDs")
    parser = CitationSections(anchors)
    parser.feed(body)
    parser.close()
    if parser.active is not None:
        raise ValueError(f"{canonical}: unclosed citation section")
    sections = []
    for anchor in anchors:
        match = parser.sections.get(anchor)
        if not match or not all(match[key] for key in ("heading", "paragraphs", "sources")):
            raise ValueError(f"{canonical}#{anchor}: heading, visible text and an HTTPS source are required")
        record = {"section_url": f"{canonical}#{anchor}", **{k: match[k] for k in ("heading", "paragraphs", "sources")}}
        record["sha256"] = sha256(json.dumps(record, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
        sections.append(record)
    return sections
