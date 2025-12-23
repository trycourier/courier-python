# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsChannelName"]


class SendToMsTeamsChannelName(TypedDict, total=False):
    channel_name: Required[str]

    service_url: Required[str]

    team_id: Required[str]

    tenant_id: Required[str]
