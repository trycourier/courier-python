# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["FeedbackCreateParams"]


class FeedbackCreateParams(TypedDict, total=False):
    category: Required[Literal["possible_bug", "confusing_behavior", "feature_request", "other"]]
    """
    What kind of report this is: `possible_bug` for behavior that looks wrong,
    `confusing_behavior` for behavior that works but was hard to understand,
    `feature_request` for something Courier does not do yet, and `other`.
    """

    description: Required[str]
    """What happened, in enough detail for someone at Courier to follow it."""

    surface: Required[Literal["api", "sdk", "mcp", "ui", "docs", "other"]]
    """
    Where you met the problem: the REST `api`, an `sdk`, the Courier `mcp` server,
    the Courier app `ui`, the `docs`, or `other`.
    """

    title: Required[str]
    """A one-line summary of the report."""

    expected_behavior: str
    """What you expected to happen instead."""

    harness: str
    """The agent or tool that submitted the report, such as `Claude Code`."""

    location: str
    """
    Where it happened, such as an endpoint (`POST /send`), an SDK method, an MCP
    tool name or a docs URL.
    """

    model: str
    """The AI model that submitted the report, such as `claude-opus-5-5`."""

    request_id: str
    """The request ID of an API call that shows the problem, if there is one."""
