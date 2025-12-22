# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToSlackChannel"]


class SendToSlackChannel(TypedDict, total=False):
    access_token: Required[str]

    channel: Required[str]
