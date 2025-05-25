from __future__ import annotations
from typing import Self

from configuration.env_file import load_env_file
from configuration.env_vars import load_env_vars


class ConfigurationBuilder:
    def __init__(self: Self) -> None:
        self._config = {}

    def add_env_vars(self: Self) -> Self:
        config = load_env_vars()
        self._config.update(config)
        return self

    def add_env_file(self: Self, file_path: str) -> Self:
        config = load_env_file(file_path)
        self._config.update(config)
        return self

    def get_config(self: Self) -> dict:
        """
        Get the current configuration as a dictionary.
        """
        return self._config
