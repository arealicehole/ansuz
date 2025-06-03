"""HTML generation utilities using Jinja2 templates.

`HTMLGenerator` will transform structured content into styled HTML
output. Future implementations will load templates and render them with
data provided by the content structurer."""

from __future__ import annotations


class HTMLGenerator:
    """Generate HTML from structured content."""

    def generate_html(self, structured_content) -> str:
        """Return HTML representing ``structured_content``."""
        raise NotImplementedError
