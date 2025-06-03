try:
    from dotenv import load_dotenv  # type: ignore
except Exception:  # pragma: no cover - fallback when package missing
    def load_dotenv(path: str = ".env") -> None:
        """Simple dotenv loader used when python-dotenv is unavailable."""
        if not os.path.exists(path):
            return
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line:
                    key, value = line.strip().split("=", 1)
                    os.environ.setdefault(key, value)

import os


def load_config(env_file: str = ".env") -> dict:
    """Load configuration from a .env file.

    Parameters
    ----------
    env_file : str, optional
        Path to the environment file. Defaults to ".env".

    Returns
    -------
    dict
        Dictionary containing configuration values with fallbacks when
        environment variables are missing.
    """
    load_dotenv(env_file)

    def _bool(val: str, default: bool = False) -> bool:
        if val is None:
            return default
        return val.lower() in {"1", "true", "yes", "on"}

    config = {
        "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
        "PERPLEXITY_API_KEY": os.getenv("PERPLEXITY_API_KEY"),
        "MODEL": os.getenv("MODEL", "claude-3-7-sonnet-20250219"),
        "PERPLEXITY_MODEL": os.getenv("PERPLEXITY_MODEL", "sonar-pro"),
        "MAX_TOKENS": int(os.getenv("MAX_TOKENS", "64000")),
        "TEMPERATURE": float(os.getenv("TEMPERATURE", "0.2")),
        "DEBUG": _bool(os.getenv("DEBUG"), default=False),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "info"),
        "DEFAULT_SUBTASKS": int(os.getenv("DEFAULT_SUBTASKS", "5")),
        "DEFAULT_PRIORITY": os.getenv("DEFAULT_PRIORITY", "medium"),
        "PROJECT_NAME": os.getenv("PROJECT_NAME"),
    }

    return config
