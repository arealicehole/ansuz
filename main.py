"""Entry point for the Ansuz application."""

from __future__ import annotations

import argparse
from pathlib import Path

from src.config_loader import load_config
from src.input_handler import InputHandler
from src.llm_processor import LLMProcessor
from src.content_structurer import ContentStructurer
from src.html_generator import HTMLGenerator
from src.youtube_fetcher import YouTubeFetcher


def main() -> None:
    """Run the application."""
    parser = argparse.ArgumentParser(description="Generate structured HTML from transcripts")
    parser.add_argument("--text", help="Transcript text")
    parser.add_argument("--file", help="Path to transcript file")
    parser.add_argument("--youtube", help="YouTube video URL")
    parser.add_argument("--output", help="File to save generated HTML")

    args = parser.parse_args()

    # Load configuration though not used directly for now
    load_config()

    input_handler = InputHandler()
    llm_processor = LLMProcessor()
    content_structurer = ContentStructurer()
    html_generator = HTMLGenerator()

    transcript: str | None = None

    if args.text:
        try:
            transcript = input_handler.process_text(args.text)
        except NotImplementedError:
            transcript = args.text
    elif args.file:
        try:
            raw = input_handler.read_file(args.file)
        except NotImplementedError:
            try:
                raw = Path(args.file).read_text(encoding="utf-8")
            except Exception as exc:  # pragma: no cover - basic error handling
                parser.error(f"Failed to read file: {exc}")
        try:
            transcript = input_handler.process_text(raw)
        except NotImplementedError:
            transcript = raw
    elif args.youtube:
        fetcher = YouTubeFetcher()
        try:
            raw = fetcher.fetch_transcript(args.youtube)
        except NotImplementedError:
            parser.error("YouTube transcript fetching not implemented")
        try:
            transcript = input_handler.process_text(raw)
        except NotImplementedError:
            transcript = raw
    else:
        parser.error("Provide --text, --file or --youtube")

    # Process transcript through remaining components
    try:
        analysis = llm_processor.call_api(transcript)
    except NotImplementedError:
        analysis = {}

    try:
        structured = content_structurer.organize_segments(transcript, analysis)
    except NotImplementedError:
        structured = transcript

    try:
        html = html_generator.generate_html(structured)
    except NotImplementedError:
        html = str(structured)

    if args.output:
        try:
            Path(args.output).write_text(html, encoding="utf-8")
        except Exception as exc:  # pragma: no cover - basic error handling
            parser.error(f"Failed to write output: {exc}")
    else:
        print(html)


if __name__ == "__main__":
    main()
