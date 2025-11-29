"""Docstring for shared_library."""

import logging
from shared_library.logging.handlers import StdOutHandler


def test_handler(caplog):
    """StdOutHandler test."""
    logger = logging.getLogger(f"{__name__}.non_error_filter")
    logger.addHandler(StdOutHandler())
    with caplog.at_level(logging.DEBUG):
        logger.log(logging.WARNING, "WARNING")
        logger.log(logging.INFO, "INFO")
        logger.log(logging.DEBUG, "DEBUG")
        assert len(caplog.records) == 3
