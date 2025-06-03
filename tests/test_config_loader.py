import os
from src.config_loader import load_config

def test_load_config_defaults_and_env(tmp_path, monkeypatch):
    env_file = tmp_path / "test.env"
    env_file.write_text("MODEL=custom\nTEMPERATURE=0.5\n")
    monkeypatch.setenv("LOG_LEVEL", "debug")
    monkeypatch.delenv("PERPLEXITY_MODEL", raising=False)
    config = load_config(str(env_file))
    assert config["MODEL"] == "custom"
    assert config["TEMPERATURE"] == 0.5
    assert config["LOG_LEVEL"] == "debug"
    assert config["PERPLEXITY_MODEL"] == "sonar-pro"

