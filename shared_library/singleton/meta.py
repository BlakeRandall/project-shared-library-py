"""Docstring for shared_library."""

from typing import Any, ClassVar
from threading import Lock


class SingletonMeta(type):
    """Metaclass for a Singleton."""

    __instances: ClassVar[dict[type, object]] = {}
    __lock: ClassVar[Lock] = Lock()

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Logic to ensure only one instance of class."""
        with cls.__lock:
            if cls not in cls.__instances:
                cls.__instances[cls] = super().__call__(*args, **kwargs)
            return cls.__instances[cls]


__all__ = ["SingletonMeta"]
