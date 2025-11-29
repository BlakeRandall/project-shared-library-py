"""Docstring for shared_library."""

import sys
import logging
from shared_library.logging.filters import ErrorFilter


class StdErrHandler(logging.StreamHandler):
    """StdErrHandler."""

    def __init__(self):
        """Initalization of StdErrHandler."""
        super().__init__(stream=sys.stderr)
        self.addFilter(ErrorFilter())


__all__ = ["StdErrHandler"]
