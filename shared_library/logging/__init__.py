"""Docstring for shared_library."""

import logging
from shared_library.logging.handlers import StdOutHandler, StdErrHandler
from shared_library.config import AppConfig

app_config = AppConfig()


def setup_logging():
    """BasicLogging Initalize basic logging configurations."""
    logging.basicConfig(
        level=app_config.log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[StdOutHandler(), StdErrHandler()],
        force=True,
    )


__all__ = ["setup_logging"]
