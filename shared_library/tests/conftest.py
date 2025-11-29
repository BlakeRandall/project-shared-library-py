"""Docstring for shared_library."""

import logging
import pytest
from dotenv import dotenv_values

logger = logging.getLogger(__name__)


@pytest.fixture(
    autouse=True,
)
def env(monkeypatch):
    """Monkeypatch Environment Variables for Tests."""
    data = {**dotenv_values(".env.example")}
    for k, v in data.items():
        logger.debug(f"patching env var {k}")
        monkeypatch.setenv(k, v)
