# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["JourneySendNodeToMsTeams"]


class JourneySendNodeToMsTeams(BaseModel):
    """
    Send to a Microsoft Teams address directly, bypassing the recipient's stored profile. Requires exactly one target: `channel_id`, `channel_name` (with `team_id`), `user_id`, or `email`. `channel_name`, `user_id`, and `email` also need at least one of `service_url` or `tenant_id` — if you provide both, they must agree. `channel_id` doesn't require tenant context to publish, but provide `service_url` or `tenant_id` anyway: sends without either have failed at delivery in testing. `conversation_id` and `reply_to_activity_id`, available on the send API's `MsTeams` profile, aren't supported here yet.
    """

    channel_id: Optional[str] = None
    """Bot Framework channel ID to send to."""

    channel_name: Optional[str] = None
    """Teams channel name to send to. Requires `team_id`."""

    email: Optional[str] = None
    """Email address of the Teams user to send to."""

    service_url: Optional[str] = None
    """The regional Bot Framework host for this conversation, e.g.

    `https://smba.trafficmanager.net/amer`. A path segment naming the Microsoft
    tenant may follow it and is used to derive `tenant_id` when it is not supplied
    directly.
    """

    team_id: Optional[str] = None
    """Microsoft Teams team ID. Required alongside `channel_name`."""

    tenant_id: Optional[str] = None
    """The Microsoft (Azure AD) tenant this send targets or authenticates against.

    Unrelated to `message.context.tenant_id`, which is the Courier customer's own
    multi-tenant context.
    """

    user_id: Optional[str] = None
    """Microsoft Teams user ID to send to."""
