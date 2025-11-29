"""Docstring for shared_library."""

import sys
import logging
from shared_library.logging.filters import NonErrorFilter


class StdOutHandler(logging.StreamHandler):
    """StdOutHandler."""

    def __init__(self):
        """Initalization of StdOutHandler."""
        super().__init__(stream=sys.stdout)
        self.addFilter(NonErrorFilter())


__all__ = ["StdOutHandler"]
