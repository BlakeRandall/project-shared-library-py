"""Docstring for shared_library."""

import pytest
from shared_library.config import MCPClientConfig


@pytest.fixture
def config() -> MCPClientConfig:
    """Config Fixture."""
    return MCPClientConfig()


def test_config(config):
    """Test Config."""
    assert config
