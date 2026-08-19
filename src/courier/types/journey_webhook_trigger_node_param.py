# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyWebhookTriggerNodeParam"]


class JourneyWebhookTriggerNodeParam(TypedDict, total=False):
    """
    Trigger fired when an external system POSTs to the webhook URL minted for `event_source`. Narrow it to one event with `event_id`, or omit `event_id` to accept every event delivered to the URL.
    """

    event_source: Required[str]
    """The provider key the webhook URL is minted for.

    Required, and must not contain a forward slash.
    """

    trigger_type: Required[Literal["webhook"]]

    type: Required[Literal["trigger"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    event_id: str
    """An optional event filter, matched against the payload's `event` field.

    A sender that supplies no `event` matches the literal `custom`. Must not contain
    a forward slash. Omit to accept every event delivered to the URL.
    """
