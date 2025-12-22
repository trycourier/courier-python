# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsChannelID"]


class SendToMsTeamsChannelID(TypedDict, total=False):
    channel_id: Required[str]

    service_url: Required[str]

    tenant_id: Required[str]
