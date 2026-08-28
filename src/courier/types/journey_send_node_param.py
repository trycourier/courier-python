# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .journey_experiment_param import JourneyExperimentParam
from .journey_conditions_field_param import JourneyConditionsFieldParam
from .journey_send_node_to_slack_param import JourneySendNodeToSlackParam
from .journey_send_node_to_ms_teams_param import JourneySendNodeToMsTeamsParam

__all__ = ["JourneySendNodeParam", "Message", "MessageContext", "MessageDelay", "MessageTo"]


class MessageContext(TypedDict, total=False):
    """Tenant context for this send.

    Set it to deliver on behalf of one of your customers, so the message uses that tenant's brand and settings.
    """

    tenant_id: Required[str]
    """The tenant to send as.

    Accepts either a literal tenant id (`acme-tenant`) or a whole-string mustache
    reference to a value the run already holds — `{{data.tenant_id}}` from the
    invocation payload, or `{{f1.body.tenant_id}}` from the response of an earlier
    fetch node with id `f1`. A reference is resolved separately on every run, so a
    single journey can deliver as many tenants. Two forms are rejected with `400`:
    mid-string interpolation such as `tenant-{{data.region}}`, and any value
    beginning with `refs.`, which is reserved for internal use. A reference that
    resolves to nothing at run time does not stop the run — the message is still
    sent, with no tenant context — so make sure the referenced value is always
    present. `GET` returns the value in the same form it was supplied.
    """


class MessageDelay(TypedDict, total=False):
    until: Required[str]

    timezone: str


class MessageTo(TypedDict, total=False):
    """Recipient override for this send.

    Provide exactly one of `email_override`, `phone_number_override`, `user_id_override`, `slack`, or `ms_teams` — not a combination.
    """

    email_override: str

    ms_teams: JourneySendNodeToMsTeamsParam
    """
    Send to a Microsoft Teams address directly, bypassing the recipient's stored
    profile. Requires exactly one target: `channel_id`, `channel_name` (with
    `team_id`), `user_id`, or `email`. `channel_name`, `user_id`, and `email` also
    need at least one of `service_url` or `tenant_id` — if you provide both, they
    must agree. `channel_id` doesn't require tenant context to publish, but provide
    `service_url` or `tenant_id` anyway: sends without either have failed at
    delivery in testing. `conversation_id` and `reply_to_activity_id`, available on
    the send API's `MsTeams` profile, aren't supported here yet.
    """

    phone_number_override: str

    slack: JourneySendNodeToSlackParam
    """Send to a Slack address directly, bypassing the recipient's stored profile.

    Requires exactly one of `channel`, `user_id`, or `email`.
    """

    user_id_override: str


class Message(TypedDict, total=False):
    context: MessageContext
    """Tenant context for this send.

    Set it to deliver on behalf of one of your customers, so the message uses that
    tenant's brand and settings.
    """

    data: Dict[str, object]

    delay: MessageDelay

    template: str

    to: MessageTo
    """Recipient override for this send.

    Provide exactly one of `email_override`, `phone_number_override`,
    `user_id_override`, `slack`, or `ms_teams` — not a combination.
    """


class JourneySendNodeParam(TypedDict, total=False):
    """Send to the recipient.

    A send node sources its content from EXACTLY ONE of `message.template` (a single notification template) or `experiment` (an A/B split across weighted template variants) — supplying both, or neither, is rejected. Optionally override the recipient address, send as a tenant, delay the send, or attach `data`.
    """

    message: Required[Message]

    type: Required[Literal["send"]]

    id: str

    channel: Literal["email", "sms", "push", "inbox", "slack", "msteams"]
    """The channel this node sends through.

    Optional — when omitted, the field is absent from the node, including on `GET`;
    nodes created before this field existed have it unset. Setting it makes the
    node's channel explicit to any client reading the journey.
    """

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    experiment: JourneyExperimentParam
    """A/B experiment config for a send node.

    The recipient is deterministically bucketed by `bucketingKey` and routed to one
    of the `variants` in proportion to its `weight`. Present on a send node INSTEAD
    OF `message.template`.
    """
