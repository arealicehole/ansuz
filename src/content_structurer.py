"""Utilities for organizing processed transcript content.

The `ContentStructurer` class will take a raw transcript and the output
from the LLM to group segments under relevant topics while preserving
original order. The resulting structure can then be rendered into HTML."""

from __future__ import annotations


class ContentStructurer:
    """Organize transcript segments into a structured form."""

    def organize_segments(self, transcript: str, analysis: dict) -> list:
        """Return a structured representation of ``transcript``."""
        headings = analysis.get("topics", []) if analysis else []

        paragraphs = [p.strip() for p in transcript.split("\n\n") if p.strip()]

        if not headings:
            return [{"heading": None, "content": paragraphs}]

        structure = []
        num_headings = len(headings)
        for i, heading in enumerate(headings):
            start = i * len(paragraphs) // num_headings
            end = (i + 1) * len(paragraphs) // num_headings
            structure.append({
                "heading": heading,
                "content": paragraphs[start:end],
            })

        return structure
