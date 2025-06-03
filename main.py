"""Entry point for the Ansuz application."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.config_loader import load_config
from src.input_handler import InputHandler


def main(argv: list[str] | None = None) -> None:
    """Run the application."""
    parser = argparse.ArgumentParser(description="Ansuz processing pipeline")
    parser.add_argument("--input", help="Path to input text file")
    parser.add_argument("--text", help="Raw text to process")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument(
        "--env-file", default=".env", help="Environment file for configuration"
    )

    args = parser.parse_args(argv)

    load_config(args.env_file)
    handler = InputHandler()

    text = ""
    if args.input:
        text = handler.read_file(args.input)
    elif args.text:
        text = args.text

    if not handler.validate_input(text):
        parser.error("No valid input provided")

    processed = handler.process_text(text)

    out_path = Path(args.output)
    out_path.write_text(processed, encoding="utf-8")
    print(f"Output written to {out_path}")


if __name__ == "__main__":
    main()
