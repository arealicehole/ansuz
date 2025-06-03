"""YouTube transcript retrieval helper.

This optional module provides a placeholder `YouTubeFetcher` class which
will interface with libraries like `youtube-transcript-api` to download
transcripts for valid YouTube videos."""

from __future__ import annotations


class YouTubeFetcher:
    """Fetch transcripts from YouTube videos."""

    def fetch_transcript(self, url: str) -> str:
        """Return the transcript text for ``url`` when implemented."""
        raise NotImplementedError
