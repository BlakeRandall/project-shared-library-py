"""Docstring for shared_library."""

import logging


class ErrorFilter(logging.Filter):
    """ErrorFilter Logging Filter.

    Filter for Logging Class to only show Errors.
    """

    def __init__(self) -> None:
        """Initalization of ErrorFilter."""
        super().__init__(__name__)

    def filter(self, record):
        """Filter logic."""
        return record.levelno >= logging.ERROR


__all__ = ["ErrorFilter"]
