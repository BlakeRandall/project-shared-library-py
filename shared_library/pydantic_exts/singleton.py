"""Docstring for shared_library."""

from typing import Any, ClassVar, Self
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class BaseModelSingleton(BaseModel):
    """BaseModelSingleton."""

    __instance: ClassVar[Self | None] = None
    __initalized: ClassVar[bool] = False
    __post_initalized: ClassVar[bool] = False

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """New."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, **data: Any) -> None:
        """Initalization."""
        if not self.__class__.__initalized:
            super().__init__(**data)
            self.__class__.__initalized = True

    def model_post_init(self, context: Any) -> None:
        """Post Initalization."""
        if not self.__class__.__post_initalized:
            super().model_post_init(context)
            self.__class__.__post_initalized = True


class BaseSettingsSingleton(BaseSettings):
    """BaseSettingsSingleton."""

    __instance: ClassVar[Self | None] = None
    __initalized: ClassVar[bool] = False
    __post_initalized: ClassVar[bool] = False

    def __new__(cls, *args: Any, **kwargs: Any) -> Self:
        """New."""
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, **data: Any) -> None:
        """Initalization."""
        if not self.__class__.__initalized:
            super().__init__(**data)
            self.__class__.__initalized = True

    def model_post_init(self, context: Any) -> None:
        """Post Initalization."""
        if not self.__class__.__post_initalized:
            super().model_post_init(context)
            self.__class__.__post_initalized = True


__all__ = ["BaseModelSingleton", "BaseSettingsSingleton"]
