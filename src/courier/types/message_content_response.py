# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["MessageContentResponse", "Result", "ResultContent", "ResultContentBlock"]


class ResultContentBlock(BaseModel):
    text: str
    """The block text of the rendered message block."""

    type: str
    """The block type of the rendered message block."""


class ResultContent(BaseModel):
    blocks: List[ResultContentBlock]
    """The blocks of the rendered message."""

    body: str
    """The body of the rendered message."""

    html: str
    """The html content of the rendered message."""

    subject: str
    """The subject of the rendered message."""

    text: str
    """The text of the rendered message."""

    title: str
    """The title of the rendered message."""


class Result(BaseModel):
    channel: str
    """The channel used for rendering the message."""

    channel_id: str
    """The ID of channel used for rendering the message."""

    content: ResultContent
    """Content details of the rendered message."""


class MessageContentResponse(BaseModel):
    results: List[Result]
    """An array of render output of a previously sent message."""
