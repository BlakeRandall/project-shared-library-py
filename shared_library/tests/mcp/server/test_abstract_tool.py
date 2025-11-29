"""Docstring for shared_library."""

import pytest
from mcp.server import FastMCP
from shared_library.mcp.server import AbstractTool, AsyncAbstractTool, SyncAbstractTool


@pytest.mark.asyncio
async def test_abstract_tool():
    """Test Abstract Tool for MCP."""
    mcp = FastMCP()

    class HelloWorldTools(AbstractTool):
        def tool_helloworld(self, query) -> str:
            return f"Hello World, {query}"

    helloworld_tools = HelloWorldTools(mcp=mcp)
    assert (
        len(
            [
                mcp_tool.name
                for mcp_tool in await mcp.list_tools()
                if mcp_tool.name in helloworld_tools.tools
            ]
        )
        > 0
    )


@pytest.mark.asyncio
async def test_abstract_tool_async():
    """Test Async Abstract Tool for MCP."""
    mcp = FastMCP()

    class HelloWorldTool(AsyncAbstractTool):
        async def __call__(self, query) -> str:
            return f"Hello World, {query}"

    tool = HelloWorldTool(mcp=mcp)
    assert all(
        mcp_tool.name == tool.__class__.__name__ for mcp_tool in await mcp.list_tools()
    )


@pytest.mark.asyncio
async def test_abstract_tool_sync():
    """Test Async Abstract Tool for MCP."""
    mcp = FastMCP()

    class HelloWorldTool(SyncAbstractTool):
        def __call__(self, query) -> str:
            return f"Hello World, {query}"

    tool = HelloWorldTool(mcp=mcp)
    assert all(
        mcp_tool.name == tool.__class__.__name__ for mcp_tool in await mcp.list_tools()
    )
