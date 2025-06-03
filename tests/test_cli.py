import os
from pathlib import Path
import subprocess
import sys

from src.input_handler import InputHandler

CLI_PYTHON = sys.executable


def test_cli_creates_output(tmp_path):
    output = tmp_path / "out.txt"
    result = subprocess.run([
        CLI_PYTHON,
        "-m",
        "main",
        "--text",
        "sample",
        "--output",
        str(output),
    ], capture_output=True, text=True)
    assert result.returncode == 0
    assert output.read_text() == "sample"
