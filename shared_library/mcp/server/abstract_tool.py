"""Docstring for shared_library."""

import logging
import inspect
import re
from abc import abstractmethod
from pydantic import BaseModel, Field, PrivateAttr
from typing import Callable, Any, ClassVar
from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)


class AbstractTool(BaseModel, arbitrary_types_allowed=True):
    """Abstract Tool for MCP Tools."""

    mcp: FastMCP = Field(frozen=True)

    __tools: list[str] = PrivateAttr(default_factory=list, init=False)

    __tool_identifier_pattern__: ClassVar[re.Pattern] = re.compile(
        r"^tool_(?P<tool_name>.*)$", re.IGNORECASE
    )
    __tool_identifier_predicate__: ClassVar[Callable[[Any], bool]] = (
        lambda member: inspect.isroutine(member) and not inspect.isbuiltin(member)
    )

    @property
    def tools(self) -> list[str]:
        """Registered Tools."""
        return self.__tools

    def model_post_init(self, context: Any) -> None:
        """Post Initalization."""
        for name, member in {
            name: member
            for name, member in inspect.getmembers(
                self, self.__class__.__tool_identifier_predicate__
            )
            if self.__class__.__tool_identifier_pattern__.match(name) is not None
        }.items():
            name_match = self.__class__.__tool_identifier_pattern__.match(name)
            if name_match:
                name = name_match.group("tool_name")
            logger.info(f"Registering tool: {name}")
            self.__tools.append(name)
            self.mcp.tool(name=name)(member)
        super().model_post_init(context)


class AsyncAbstractTool(BaseModel, arbitrary_types_allowed=True):
    """Abstract Tool for MCP Tools."""

    mcp: FastMCP = Field(frozen=True)

    @abstractmethod
    async def __call__(self, *args, **kwargs) -> Any:
        """Tool Logic."""
        return  # pragma: no cover

    def model_post_init(self, context: Any) -> None:
        """Post Initalization."""
        self.mcp.tool(
            name=self.__class__.__name__, description=self.__class__.__name__
        )(self.__call__)
        super().model_post_init(context)


class SyncAbstractTool(BaseModel, arbitrary_types_allowed=True):
    """Abstract Tool for MCP Tools."""

    mcp: FastMCP = Field(frozen=True)

    @abstractmethod
    def __call__(self, *args, **kwargs) -> Any:
        """Tool Logic."""
        return  # pragma: no cover

    def model_post_init(self, context: Any) -> None:
        """Post Initalization."""
        self.mcp.tool(
            name=self.__class__.__name__, description=self.__class__.__name__
        )(self.__call__)
        super().model_post_init(context)


__all__ = ["AbstractTool", "AsyncAbstractTool", "SyncAbstractTool"]
