from __future__ import annotations

from configuration.config_builder import ConfigurationBuilder

config_builder = ConfigurationBuilder()


def load_config() -> dict:
    config_builder.add_env_file(".env")
    return config_builder.get_config()


def get_config() -> dict:
    return config_builder.get_config()
