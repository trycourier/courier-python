# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsChannelID"]


class SendToMsTeamsChannelID(TypedDict, total=False):
    """Sends directly to a Microsoft Teams channel by its Bot Framework ID.

    Still provide at least one of `tenant_id` or `service_url` — sends without either have failed Bot Framework authentication in testing.
    """

    channel_id: Required[str]

    service_url: str

    tenant_id: str
