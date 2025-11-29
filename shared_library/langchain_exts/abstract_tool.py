"""Docstring for shared_library."""

from typing import Any
from abc import abstractmethod
from pydantic import BaseModel
from langchain.tools import tool, BaseTool, ToolRuntime


class AsyncAbstractTool(BaseModel, arbitrary_types_allowed=True):
    """Abstract Tool for LangChain/LangGraph Tools."""

    @abstractmethod
    async def __call__(self, runtime: ToolRuntime[Any, Any], *args, **kwargs) -> Any:
        """Tool Logic."""
        return

    @property
    def as_tool(self) -> BaseTool:
        """Return Current Class as a Tool."""
        return tool(self.__class__.__name__, description=self.__class__.__doc__)(
            self.__call__
        )


class SyncAbstractTool(BaseModel, arbitrary_types_allowed=True):
    """Abstract Tool for LangChain/LangGraph Tools."""

    @abstractmethod
    def __call__(self, runtime: ToolRuntime[Any, Any], *args, **kwargs) -> Any:
        """Tool Logic."""
        return

    @property
    def as_tool(self) -> BaseTool:
        """Return Current Class as a Tool."""
        return tool(self.__class__.__name__, description=self.__class__.__doc__)(
            self.__call__
        )


__all__ = ["AsyncAbstractTool", "SyncAbstractTool"]
