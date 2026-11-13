"""Check a published Atlas section against scoped SAP evidence fingerprints."""

from hashlib import sha256
from html.parser import HTMLParser
import json
from pathlib import Path
import re

from .atlas_citation_sections import read_atlas_citation_sections


def digest(text):
    return sha256(text.encode("utf-8")).hexdigest()


class SapEvidence(HTMLParser):
    """Collect paragraphs under the named headings of a public SAP KBA."""

    def __init__(self, html):
        super().__init__(convert_charrefs=True)
        self.article_ids = []
        self.revisions = []
        self.sections = {}
        self.current_section = None
        self.paragraph = None
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        fields = dict(attrs)
        if tag == "meta" and fields.get("name") == "id":
            self.article_ids.append(fields.get("content"))
        if tag == "meta" and fields.get("name") == "updated_timestamp":
            self.revisions.append(fields.get("content"))
        if tag in ("h1", "h2", "h3"):
            self.current_section = fields.get("id") if tag == "h3" else None
            if self.current_section:
                if self.current_section in self.sections:
                    raise ValueError("Duplicate SAP section: " + self.current_section)
                self.sections[self.current_section] = []
        if tag == "p" and self.current_section:
            self.paragraph = []

    def handle_data(self, data):
        if self.paragraph is not None:
            self.paragraph.append(data)

    def handle_endtag(self, tag):
        if tag == "p" and self.paragraph is not None:
            self.sections[self.current_section].append(" ".join("".join(self.paragraph).split()))
            self.paragraph = None

    def observe(self, article_id, heading, paragraph):
        if self.article_ids != [article_id]:
            raise ValueError("Expected a capture of SAP KBA " + article_id)
        paragraphs = self.sections.get(heading, [])
        if paragraph >= len(paragraphs):
            return None
        return {
            "version": self.revisions[0] if len(self.revisions) == 1 else None,
            "sha256": digest(paragraphs[paragraph]),
        }


def review_atlas_claims(repo, parse_frontmatter, source_html=None):
    config = json.loads((repo / "scripts/atlas-claim-bindings.json").read_text(encoding="utf-8"))
    source = config["source"]
    article_id = source["articleId"]
    if (
        config["schema"] != "atlas.claim-review.v1"
        or not re.fullmatch(r"[0-9]+", article_id)
        or source["url"] != f"https://userapps.support.sap.com/sap/support/knowledge/en/{article_id}"
    ):
        raise ValueError("Unsupported Atlas claim review or SAP source")
    document = (repo / config["document"]).resolve()
    if not document.is_relative_to(repo / "atlas") or document.suffix != ".md":
        raise ValueError("The claim review requires an Atlas Markdown source")
    frontmatter, body = parse_frontmatter(document)
    canonical = "https://dkharlanau.github.io" + frontmatter["permalink"]
    section_url = canonical + "#" + config["anchor"]
    sections = read_atlas_citation_sections(body, frontmatter.get("citation_sections"), canonical,
                                           task_anchors=frontmatter.get("task_pack_sections"))
    section = next((row for row in sections if row["section_url"] == section_url), None)
    if section is None or source["url"] not in section["sources"]:
        raise ValueError("Atlas claim review section or visible SAP citation missing")
    evidence = SapEvidence(Path(source_html).read_text(encoding="utf-8")) if source_html else None

    rows = []
    ids = set()
    for claim in config["claims"]:
        claim_id = claim["id"]
        if claim_id in ids or not claim_id:
            raise ValueError("Duplicate or missing Atlas claim ID")
        ids.add(claim_id)
        section_name, paragraph = claim["sourceSection"], claim["sourceParagraph"]
        if type(paragraph) is not int or paragraph < 0:
            raise ValueError("Invalid SAP source paragraph for " + claim_id)
        observed = evidence.observe(article_id, section_name, paragraph) if evidence else None
        expected = claim["sourceSha256"]
        if not re.fullmatch(r"[a-f0-9]{64}", expected):
            raise ValueError("Invalid source fingerprint for " + claim_id)
        atlas_matches = [
            paragraph for paragraph in section["paragraphs"]
            if claim["atlasText"] in paragraph
        ]
        local_match = len(atlas_matches) == 1 and digest(atlas_matches[0]) == claim["atlasParagraphSha256"]
        source_status = "unknown"
        if observed is not None:
            if observed["sha256"] != expected:
                source_status = "changed"
            elif observed["version"]:
                source_status = "matched"
        review_required = not local_match or (evidence is not None and source_status != "matched")
        rows.append({
            "id": claim_id,
            "canonical": section_url,
            "scope": claim["scope"],
            "unknown": claim["unknown"],
            "dependentOutputs": config["dependentOutputs"],
            "localTextMatched": local_match,
            "source": {
                "url": source["url"] + "#" + section_name,
                "reviewedVersion": source["reviewedVersion"],
                "expectedSha256": expected,
                "observed": observed,
                "status": source_status,
            },
            "state": "needs_review" if review_required else "source_unknown" if evidence is None else "matched",
        })
    if not rows:
        raise ValueError("Atlas claim review requires at least one claim")
    return rows
