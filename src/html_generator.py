"""HTML generation utilities using Jinja2 templates.

`HTMLGenerator` will transform structured content into styled HTML
output. Future implementations will load templates and render them with
data provided by the content structurer."""

from __future__ import annotations
from jinja2 import Template


class HTMLGenerator:
    """Generate HTML from structured content."""

    def generate_html(self, structured_content) -> str:
        """Return HTML representing ``structured_content``."""
        template_str = """
        <html>
        <head>
            <meta charset='utf-8'>
            <title>Ansuz Output</title>
            <style>
                body {font-family: Arial, sans-serif; margin: 2em;}
                h2 {margin-top: 1.5em;}
            </style>
        </head>
        <body>
        {% for section in content %}
            {% if section.heading %}<h2>{{ section.heading }}</h2>{% endif %}
            {% for paragraph in section.content %}
                <p>{{ paragraph }}</p>
            {% endfor %}
        {% endfor %}
        </body>
        </html>
        """

        template = Template(template_str)
        return template.render(content=structured_content)
