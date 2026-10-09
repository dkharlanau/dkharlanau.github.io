from __future__ import annotations

import json
from pathlib import Path
import tempfile
import subprocess
import unittest
from unittest.mock import patch

import reproduce


class ReproductionTest(unittest.TestCase):
    def test_clean_exact_revision_passes(self):
        with patch.object(reproduce, "git", side_effect=["a" * 40, ""]):
            reproduce.verify_checkout(Path("tool"), "tool", "a" * 40)

    def test_newer_revision_fails_before_dirty_check(self):
        with patch.object(reproduce, "git", return_value="b" * 40) as git:
            with self.assertRaisesRegex(reproduce.ReproductionError, "expected .*found"):
                reproduce.verify_checkout(Path("tool"), "tool", "a" * 40)
            self.assertEqual(git.call_count, 1)

    def test_dirty_revision_fails(self):
        for status in [" M source.py", "?? shadow.py"]:
            with self.subTest(status=status), patch.object(reproduce, "git", side_effect=["a" * 40, status]):
                with self.assertRaisesRegex(reproduce.ReproductionError, "dirty"):
                    reproduce.verify_checkout(Path("tool"), "tool", "a" * 40)

    def test_unbounded_pin_fails_before_git(self):
        with patch.object(reproduce, "git") as git:
            with self.assertRaisesRegex(reproduce.ReproductionError, "invalid commit pin"):
                reproduce.verify_checkout(Path("tool"), "tool", "main")
            git.assert_not_called()

    def test_existing_output_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            sentinel = output / "receipt.json"
            sentinel.write_text("previous evidence")
            with self.assertRaisesRegex(reproduce.ReproductionError, "already exists"):
                reproduce.reproduce(output, {})
            self.assertEqual(sentinel.read_text(), "previous evidence")

    def test_output_cannot_be_inside_any_source(self):
        for source in [reproduce.ROOT, reproduce.ROOT.parents[2]]:
            with self.subTest(source=source):
                with self.assertRaisesRegex(reproduce.ReproductionError, "outside"):
                    reproduce.check_output_path(source / "new-output", {})

    def test_output_cannot_be_inside_sibling_source(self):
        source = Path("/synthetic-checkout")
        with self.assertRaisesRegex(reproduce.ReproductionError, "outside"):
            reproduce.check_output_path(source / "new-output", {"tool": source})

    def test_exact_copy_matches_and_tampered_or_missing_output_fails(self):
        relative = "artifacts/architecture.blueprint.json"
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "output.json"
            output.write_bytes((reproduce.ROOT / relative).read_bytes())
            self.assertEqual(reproduce.compare_output(output, relative)["retained_path"], relative)
            output.write_bytes(output.read_bytes() + b" ")
            with self.assertRaisesRegex(reproduce.ReproductionError, "byte mismatch"):
                reproduce.compare_output(output, relative)
            output.unlink()
            with self.assertRaisesRegex(reproduce.ReproductionError, "byte mismatch"):
                reproduce.compare_output(output, relative)

    def test_bad_pack_records_failure_and_never_runs_products(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(reproduce, "validate_case", return_value=["tampered fixture"]), patch.object(reproduce.subprocess, "run") as run:
            output = Path(temp) / "failed"
            with self.assertRaisesRegex(reproduce.ReproductionError, "tampered fixture"):
                reproduce.reproduce(output, {})
            run.assert_not_called()
            receipt = json.loads((output / "receipt.json").read_text())
            self.assertEqual(receipt["status"], "failed")
            self.assertEqual(receipt["outputs"], {})

    def test_unsupported_lock_records_failure_without_running_products(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(reproduce, "load_json", return_value={"schema_version": "2.0.0"}), patch.object(reproduce.subprocess, "run") as run:
            output = Path(temp) / "failed"
            with self.assertRaisesRegex(reproduce.ReproductionError, "unsupported runtime lock"):
                reproduce.reproduce(output, {})
            run.assert_not_called()
            self.assertEqual(json.loads((output / "receipt.json").read_text())["status"], "failed")

    def test_failed_command_keeps_logs_and_failed_receipt(self):
        result = subprocess.CompletedProcess(["node", "--version"], 73, b"partial output", b"runtime failed")
        with tempfile.TemporaryDirectory() as temp, patch.object(reproduce, "validate_case", return_value=[]), patch.object(reproduce, "verify_checkout"), patch.object(reproduce.subprocess, "run", return_value=result):
            root = Path(temp)
            output = root / "failed"
            repositories = {name: root / name for name in reproduce.REPOSITORIES}
            with self.assertRaisesRegex(reproduce.ReproductionError, "exit 73"):
                reproduce.reproduce(output, repositories)
            receipt = json.loads((output / "receipt.json").read_text())
            self.assertEqual(receipt["status"], "failed")
            self.assertEqual(receipt["steps"], [{"id": "node-version", "exit_code": 73}])
            self.assertEqual(receipt["outputs"], {})
            self.assertEqual((output / "node-version.stdout.log").read_bytes(), b"partial output")
            self.assertEqual((output / "node-version.stderr.log").read_bytes(), b"runtime failed")

    def test_missing_runtime_keeps_failed_receipt(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(reproduce, "validate_case", return_value=[]), patch.object(reproduce, "verify_checkout"), patch.object(reproduce.subprocess, "run", side_effect=FileNotFoundError("node unavailable")):
            root = Path(temp)
            output = root / "failed"
            repositories = {name: root / name for name in reproduce.REPOSITORIES}
            with self.assertRaisesRegex(reproduce.ReproductionError, "node unavailable"):
                reproduce.reproduce(output, repositories)
            receipt = json.loads((output / "receipt.json").read_text())
            self.assertEqual(receipt["status"], "failed")
            self.assertEqual(receipt["steps"], [])


if __name__ == "__main__":
    unittest.main()
