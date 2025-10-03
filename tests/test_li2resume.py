import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "li2resume.py"
FIXTURE_DIR = Path(__file__).resolve().parent / "fixtures" / "sample_linkedin"


class Li2ResumeTest(unittest.TestCase):
    def setUp(self) -> None:
        self.workspace = Path(tempfile.mkdtemp())

    def tearDown(self) -> None:
        shutil.rmtree(self.workspace, ignore_errors=True)

    def run_script(
        self,
        extra_args=None,
        provide_cli=True,
        include_email=False,
        email_value="case@example.com",
        include_location=False,
        location_value="Remote",
    ):
        input_dir = self.workspace / "LinkedinComplete"
        shutil.copytree(FIXTURE_DIR, input_dir)
        args = [sys.executable, str(SCRIPT)]
        if provide_cli:
            args.extend(
                [
                    "--input",
                    str(input_dir),
                    "--name",
                    "Case Tester",
                    "--site",
                    "https://example.com",
                    "--headline",
                    "SAP Program Lead",
                ]
            )
            if include_email:
                args.extend(["--email", email_value])
            if include_location:
                args.extend(["--location", location_value])
        if extra_args:
            args.extend(extra_args)
        subprocess.check_call(args, cwd=self.workspace)
        yaml_path = self.workspace / "_data" / "resume.yml"
        json_path = self.workspace / "ai" / "resume.json"
        self.assertTrue(yaml_path.exists(), "resume.yml should be created")
        self.assertTrue(json_path.exists(), "resume.json should be created")
        return json.loads(json_path.read_text(encoding="utf-8"))

    def test_basic_export(self):
        resume = self.run_script()
        self.assertEqual(resume["name"], "Case Tester")
        self.assertEqual(resume["headline"], "SAP Program Lead")
        self.assertGreaterEqual(len(resume["experience"]), 1)
        self.assertIn("skills", resume)
        urls = [link["url"] for link in resume["links"]]
        self.assertEqual(len(urls), len(set(urls)))
        self.assertTrue(
            any(link for link in resume["links"] if "linkedin" not in link["url"]),
            "Should include custom links",
        )
        self.assertNotIn("email", resume["contact"])
        self.assertNotIn("location", resume)

    def test_cli_email_included(self):
        resume = self.run_script(include_email=True)
        self.assertEqual(resume["contact"].get("email"), "case@example.com")

    def test_cli_location_included(self):
        resume = self.run_script(include_location=True, location_value="Remote-Only")
        self.assertEqual(resume.get("location"), "Remote-Only")

    def test_config_driven_run(self):
        config_path = self.workspace / "li2resume.local.json"
        cfg = {
            "input": "./LinkedinComplete",
            "name": "Config Tester",
            "email": "config@example.com",
            "site": "https://config.example.com",
            "headline": "Config Headline",
            "links": [{"label": "Portfolio", "url": "https://config.example.com/portfolio"}],
        }
        config_path.write_text(json.dumps(cfg), encoding="utf-8")
        resume = self.run_script(extra_args=["--config", str(config_path)], provide_cli=False)
        self.assertEqual(resume["name"], "Config Tester")
        self.assertEqual(resume["headline"], "Config Headline")
        self.assertEqual(resume["contact"]["email"], "config@example.com")


if __name__ == "__main__":
    unittest.main()
