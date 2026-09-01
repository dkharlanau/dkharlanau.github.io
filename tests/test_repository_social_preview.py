import json
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from scripts.render_repository_social_preview import HEIGHT, WIDTH, PreviewError, load_config, render


class RepositorySocialPreviewTest(unittest.TestCase):
    def fixture(self) -> dict:
        return {
            "schema_version": "1.0",
            "dimensions": {"width": 1280, "height": 640},
            "track": "Enterprise design",
            "title": "Enterprise Architecture Composer",
            "subtitle": "Compose explainable architecture from explicit context and constraints.",
            "repository": "enterprise-architecture-composer",
            "author": "Dzmitryi Kharlanau",
            "motif": "composition",
            "background": "#eef3f5",
            "ink": "#171c24",
            "muted": "#596272",
            "accent": "#d35435",
            "panel": "#ffffff",
        }

    def test_renders_exact_github_dimensions(self):
        image = render(self.fixture())
        self.assertEqual(image.size, (WIDTH, HEIGHT))
        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "preview.png"
            image.save(output, format="PNG", optimize=True)
            self.assertLess(output.stat().st_size, 1_000_000)
            with Image.open(output) as rendered:
                self.assertEqual(rendered.size, (1280, 640))

    def test_rejects_unknown_motif_and_oversized_copy(self):
        fixture = self.fixture()
        fixture["motif"] = "decorative"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "preview.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            with self.assertRaises(PreviewError):
                load_config(path)

        fixture = self.fixture()
        fixture["title"] = "x" * 57
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "preview.json"
            path.write_text(json.dumps(fixture), encoding="utf-8")
            with self.assertRaises(PreviewError):
                load_config(path)


if __name__ == "__main__":
    unittest.main()
