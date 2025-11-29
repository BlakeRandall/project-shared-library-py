"""Docstring for shared_library."""

import pytest
from typing import Any
from langchain.tools import ToolRuntime
from shared_library.langchain_exts.abstract_tool import (
    SyncAbstractTool,
    AsyncAbstractTool,
)


@pytest.mark.asyncio
async def test_abstract_tool():
    """Test Abstract Tool for LangChain."""

    class HelloWorldTools(SyncAbstractTool):
        def __call__(self, query: str, runtime: ToolRuntime[Any, Any]) -> str:
            return f"Hello World, {query}!"

    class HelloWorldToolsAsync(AsyncAbstractTool):
        async def __call__(self, query: str, runtime: ToolRuntime[Any, Any]) -> str:
            return f"Hello World, {query}!"

    assert "Hello World, Name!" == await HelloWorldTools().as_tool.ainvoke(
        {
            "query": "Name",
            "runtime": ToolRuntime(None, None, {}, (lambda _: None), None, None),
        }
    )

    assert "Hello World, Name!" == await HelloWorldToolsAsync().as_tool.ainvoke(
        {
            "query": "Name",
            "runtime": ToolRuntime(None, None, {}, (lambda _: None), None, None),
        }
    )
