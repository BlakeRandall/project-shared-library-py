"""Docstring for shared_library."""

import pytest
from shared_library.config import ChatModelConfig


@pytest.fixture
def config() -> ChatModelConfig:
    """Config Fixture."""
    return ChatModelConfig()


def test_config(config):
    """Test Config."""
    assert config
