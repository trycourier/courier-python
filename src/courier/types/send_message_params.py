# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .message_param import MessageParam

__all__ = ["SendMessageParams"]


class SendMessageParams(TypedDict, total=False):
    message: Required[MessageParam]
    """Defines the message to be delivered"""
