"""Command-line interface for the Ansuz application."""

from argparse import ArgumentParser
from pathlib import Path

from src.config_loader import load_config
from src.input_handler import InputHandler
from src.llm_processor import LLMProcessor
from src.content_structurer import ContentStructurer
from src.html_generator import HTMLGenerator


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(description="Process transcripts into structured HTML")
    parser.add_argument(
        "--text",
        help="Raw text input provided directly on the command line",
    )
    parser.add_argument(
        "--file",
        help="Path to a text file containing the transcript",
    )
    parser.add_argument(
        "--youtube",
        help="URL of a YouTube video to fetch the transcript from",
    )
    parser.add_argument(
        "--output",
        default="output.html",
        help="Path to save the generated HTML (default: output.html)",
    )
    return parser


def main() -> None:
    parser = parse_args()
    args = parser.parse_args()

    if not any([args.text, args.file, args.youtube]):
        parser.print_help()
        raise SystemExit("Please provide --text, --file, or --youtube")

    config = load_config()

    input_handler = InputHandler()
    transcript = input_handler.get_input(
        text=args.text, file_path=args.file, youtube_url=args.youtube
    )

    llm = LLMProcessor(config)
    analysis = llm.analyze(transcript)

    structurer = ContentStructurer()
    structured = structurer.structure(transcript, analysis)

    generator = HTMLGenerator()
    html = generator.generate(structured)

    output_path = Path(args.output)
    output_path.write_text(html, encoding="utf-8")
    print(f"HTML saved to {output_path}")


if __name__ == "__main__":
    main()
