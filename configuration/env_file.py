from __future__ import annotations
from pathlib import Path


def load_env_file(file_path: str) -> dict:
    """
    Loads environment variables from a file and transforms them into a nested dictionary.
    Double underscores '__' indicate nesting. All nested keys are lowercased.
    Non-nested keys keep their original casing.

    Example:
        NOT_AN_OBJECT=abc123 -> {"NOT_AN_OBJECT": "abc123"}
        SECTION_1__KEY_1=value1  -> {"section_1": {"key_1": "value1"}}
        SECTION_1__SUB__KEY=value -> {"section_1": {"sub": {"key": "value"}}}
    """
    result = {}

    with Path(file_path).open("r") as file:
        for line in file:
            if line.strip() and not line.startswith("#"):
                key, value = line.strip().split("=", 1)
                parts = key.lower().split("__")
                if len(parts) == 1:
                    # Keep original casing for non-nested keys
                    result[key] = value
                else:
                    # Lowercase all parts for nested keys
                    d = result
                    for part in parts[:-1]:
                        if part not in d or not isinstance(d[part], dict):
                            d[part] = {}
                        d = d[part]
                    d[parts[-1]] = value
    return result
