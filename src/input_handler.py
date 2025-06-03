from pathlib import Path
from typing import Optional


class InputHandler:
    """Handle user-provided input for transcript processing."""

    def get_input(
        self,
        *,
        text: Optional[str] = None,
        file_path: Optional[str] = None,
        youtube_url: Optional[str] = None,
    ) -> str:
        """Return transcript text from one of the supported sources."""
        if text:
            return text

        if file_path:
            path = Path(file_path)
            if not path.is_file():
                raise FileNotFoundError(f"File not found: {file_path}")
            return path.read_text(encoding="utf-8")

        if youtube_url:
            # Placeholder for YouTube transcript fetching logic.
            # Future implementations will fetch the transcript from the URL.
            raise NotImplementedError("YouTube URL handling not implemented yet")

        raise ValueError("No valid input source provided")
