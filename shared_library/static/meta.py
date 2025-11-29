"""Docstring for shared_library."""

from typing import Any


class StaticMeta(type):
    """Metaclass for a Static Object which cannot be created."""

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        """Logic to restrict object to be created."""
        raise NotImplementedError(
            f"class, {cls.__name__},(metaclass={cls.__class__.__class__}) should not be instantiated"  # noqa: E501
        )


__all__ = ["StaticMeta"]
