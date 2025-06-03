"""Interface with the chosen Large Language Model API.

The `LLMProcessor` class will be responsible for sending prompts to the
underlying LLM service and returning the generated responses.
Actual API integration will be added in later development stages."""

from __future__ import annotations


class LLMProcessor:
    """Wrapper for LLM API calls."""

    def call_api(self, prompt: str) -> str:
        """Send ``prompt`` to the LLM and return its response."""
        # This is a lightweight stub used for development and testing
        # without making actual API requests.
        _ = prompt  # acknowledge the prompt without using it
        return {
            "topics": [
                "Introduction",
                "Main Discussion",
                "Conclusion",
            ]
        }
