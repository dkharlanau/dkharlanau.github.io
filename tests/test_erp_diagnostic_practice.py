"""Run the lab's pure JavaScript checks in the repository's regular pytest gate."""
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]


def test_erp_diagnostic_engine_regressions():
    node = shutil.which("node")
    if node is None:
        pytest.skip("Node.js is required to run the browser engine regression checks")
    result = subprocess.run(
        [node, "--test", "tests/erp_diagnostic_practice.test.mjs"],
        cwd=ROOT, capture_output=True, text=True, check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
