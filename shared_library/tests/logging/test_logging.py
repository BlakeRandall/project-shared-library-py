"""Docstring for shared_library."""

import logging
from shared_library.logging import setup_logging
from shared_library.logging.handlers import StdOutHandler, StdErrHandler


def test_basic_logging():
    """Basic Logging Configuration Test."""
    root_logger = logging.getLogger()
    assert not any(
        isinstance(handler, (StdOutHandler, StdErrHandler))
        for handler in root_logger.handlers
    )
    setup_logging()
    assert any(
        isinstance(handler, (StdOutHandler, StdErrHandler))
        for handler in root_logger.handlers
    )
