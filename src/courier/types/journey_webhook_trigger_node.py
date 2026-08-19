# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyWebhookTriggerNode"]


class JourneyWebhookTriggerNode(BaseModel):
    """
    Trigger fired when an external system POSTs to the webhook URL minted for `event_source`. Narrow it to one event with `event_id`, or omit `event_id` to accept every event delivered to the URL.
    """

    event_source: str
    """The provider key the webhook URL is minted for.

    Required, and must not contain a forward slash.
    """

    trigger_type: Literal["webhook"]

    type: Literal["trigger"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    event_id: Optional[str] = None
    """An optional event filter, matched against the payload's `event` field.

    A sender that supplies no `event` matches the literal `custom`. Must not contain
    a forward slash. Omit to accept every event delivered to the URL.
    """
