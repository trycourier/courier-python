# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SendToMsTeamsChannelName"]


class SendToMsTeamsChannelName(TypedDict, total=False):
    """`team_id` is required alongside `channel_name`.

    Also provide at least one of `tenant_id` or `service_url`; if you provide both, they must agree.
    """

    channel_name: Required[str]

    team_id: Required[str]

    service_url: str

    tenant_id: str
