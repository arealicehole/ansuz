from typing import Dict, List


class HTMLGenerator:
    """Generate HTML from structured content."""

    def generate(self, sections: List[Dict[str, str]]) -> str:
        html_parts = ["<html>", "<body>"]
        for section in sections:
            heading = section.get("heading", "")
            content = section.get("content", "")
            html_parts.append(f"<h2>{heading}</h2>")
            html_parts.append(f"<p>{content}</p>")
        html_parts.append("</body>")
        html_parts.append("</html>")
        return "\n".join(html_parts)
