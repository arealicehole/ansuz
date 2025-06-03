"""Utilities for organizing processed transcript content.

The `ContentStructurer` class will take a raw transcript and the output
from the LLM to group segments under relevant topics while preserving
original order. The resulting structure can then be rendered into HTML."""

from __future__ import annotations


class ContentStructurer:
    """Organize transcript segments into a structured form."""

    def organize_segments(self, transcript: str, analysis: dict) -> list:
        """Return a structured representation of ``transcript``."""
        raise NotImplementedError
