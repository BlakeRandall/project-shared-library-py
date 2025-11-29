"""Docstring for shared_library."""

import logging


class NonErrorFilter(logging.Filter):
    """NonErrorFilter Logging Filter.

    Filter for Logging Class to only show Non Errors.
    """

    def __init__(self) -> None:
        """Initalization of NonErrorFilter."""
        super().__init__(__name__)

    def filter(self, record):
        """Filter logic."""
        return record.levelno <= logging.WARN


__all__ = ["NonErrorFilter"]
