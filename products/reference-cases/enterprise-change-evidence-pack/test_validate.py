from __future__ import annotations

import copy
import tempfile
import unittest
from pathlib import Path

from validate import (
    ROOT,
    load_json,
    validate_case,
    validate_eac_reference,
    validate_expected_file,
    validate_research_packet,
)
from normalize_render import normalize


class ReferenceCaseValidationTest(unittest.TestCase):
    def test_committed_case_is_valid(self) -> None:
        self.assertEqual(validate_case(), [])

    def test_eac_identity_is_case_owned_and_version_bounded(self) -> None:
        valid = (
            "eac://dkharlanau/dkharlanau.github.io/reference-case/"
            "enterprise-change-evidence-pack/research-context?version=1.0.0"
        )
        self.assertEqual(validate_eac_reference(valid), [])
        self.assertTrue(validate_eac_reference(valid.replace("dkharlanau.github.io", "visual-workbench")))
        self.assertTrue(validate_eac_reference(valid.replace("version=1.0.0", "version=latest")))
        self.assertTrue(validate_eac_reference(valid + "&trusted=true"))

    def test_tampered_research_payload_breaks_canonical_digest(self) -> None:
        packet = load_json(ROOT / "fixtures" / "research-context.json")
        expected = load_json(ROOT / "expected-artifacts.json")["assertions"]["research_context"]
        tampered = copy.deepcopy(packet)
        tampered["claims"][0]["text"] = "Changed without regenerating integrity metadata."

        errors = validate_research_packet(tampered, expected)

        self.assertIn("research context canonical payload digest is invalid", errors)

    def test_expected_artifact_hash_detects_tampering(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path = root / "artifact.txt"
            path.write_text("original\n", encoding="utf-8")
            record = {
                "path": "artifact.txt",
                "sha256": "f00d",
                "bytes": len("original\n".encode("utf-8")),
                "source_contract_url": "https://example.com/contract",
            }

            errors = validate_expected_file(root, record)

            self.assertIn("artifact.txt: SHA-256 mismatch", errors)

    def test_svg_normalization_is_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "render.svg"
            path.write_text("<svg>  \n  <g/>\t\n</svg>\n", encoding="utf-8")

            normalize(path)
            first = path.read_text(encoding="utf-8")
            normalize(path)

            self.assertEqual(first, "<svg>\n  <g/>\n</svg>\n")
            self.assertEqual(path.read_text(encoding="utf-8"), first)


if __name__ == "__main__":
    unittest.main()
