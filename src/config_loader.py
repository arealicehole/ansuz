import os
from typing import Dict


def load_config() -> Dict[str, str]:
    """Load configuration settings from environment variables.

    This simple loader checks common environment variables that might be
    required by other modules. It can be expanded later to read from files
    or other sources.
    """
    return {
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY", ""),
    }
