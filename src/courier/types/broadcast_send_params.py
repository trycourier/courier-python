# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["BroadcastSendParams"]


class BroadcastSendParams(TypedDict, total=False):
    recipient_id: Required[str]
    """ID of the target list or audience."""

    recipient_type: Required[Literal["list", "audience"]]
    """Whether the broadcast targets a list or an audience."""
