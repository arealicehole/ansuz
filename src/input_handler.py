"""Input handling utilities for Ansuz.

This module defines the `InputHandler` class which provides methods for
processing raw text input, reading text files and performing basic
validation. The actual implementation will handle user input from the
command line or other sources and normalize it for further processing."""

from __future__ import annotations


class InputHandler:
    """Handle user supplied text from various sources."""

    def process_text(self, text: str) -> str:
        """Return cleaned text from a pasted string.

        Parameters
        ----------
        text: str
            Raw text supplied by the user.
        """
        return text.strip()

    def read_file(self, file_path: str) -> str:
        """Read text from ``file_path`` and return its contents."""
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    def validate_input(self, text: str) -> bool:
        """Validate provided text input.

        This check will ensure the text is not empty and meets any
        additional criteria defined in future development.
        """
        return bool(text and text.strip())
