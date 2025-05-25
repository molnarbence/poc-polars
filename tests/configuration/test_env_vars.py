from collections.abc import Generator
import pytest
from unittest.mock import Mock, patch

from configuration.env_vars import load_env_vars


@pytest.fixture(autouse=True)
def mock_env_vars() -> Generator[Mock, None, None]:
    env = {
        "NOT_AN_OBJECT": "abc123",
        "SECTION_1__KEY_1": "value_1",
        "SECTION_1__KEY_2": "value_2",
        "SECTION_2__KEY_1": "value_3",
        "SECTION_3__SUB_SECTION__KEY_1": "value_4",
    }
    with patch.dict("os.environ", env, clear=True) as mock:
        yield mock


def test_load_env_vars() -> None:
    # arrange

    # act
    config = load_env_vars()

    # assert
    assert config["NOT_AN_OBJECT"] == "abc123"
    assert config["section_1"] == {"key_1": "value_1", "key_2": "value_2"}
    assert config["section_2"] == {"key_1": "value_3"}
    assert config["section_3"] == {"sub_section": {"key_1": "value_4"}}

    assert config.get("not_an_object") is None
    assert config.get("section_1__key_1") is None
    assert config.get("section_3__sub_section__key_1") is None
