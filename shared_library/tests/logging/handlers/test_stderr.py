"""Docstring for shared_library."""

import logging
from shared_library.logging.handlers import StdErrHandler


def test_handler(caplog):
    """StdErrHandler test."""
    logger = logging.getLogger(f"{__name__}.error_filter")
    logger.addHandler(StdErrHandler())
    with caplog.at_level(logging.DEBUG):
        logger.log(logging.CRITICAL, "CRITICAL")
        logger.log(logging.ERROR, "CRITICAL")
        assert len(caplog.records) == 2
