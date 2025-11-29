"""Docstring for shared_library."""

import pytest
from shared_library.config import AppConfig


@pytest.fixture
def config() -> AppConfig:
    """Config Fixture."""
    return AppConfig()


def test_config(config):
    """Test Config."""
    assert config
    assert config.log_level == "INFO"
