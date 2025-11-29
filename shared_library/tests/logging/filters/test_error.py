"""Docstring for shared_library."""

import logging
from shared_library.logging.filters import ErrorFilter


def test_filter(caplog):
    """ErrorFilter test."""
    logger = logging.getLogger(f"{__name__}.error_filter")
    logger.addFilter(ErrorFilter())
    with caplog.at_level(logging.DEBUG):
        logger.log(logging.CRITICAL, "CRITICAL")
        logger.log(logging.ERROR, "CRITICAL")
        assert len(caplog.records) == 2
