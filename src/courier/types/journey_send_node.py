# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneySendNode", "Message", "MessageDelay", "MessageTo"]


class MessageDelay(BaseModel):
    until: str

    timezone: Optional[str] = None


class MessageTo(BaseModel):
    email_override: Optional[str] = None

    phone_number_override: Optional[str] = None

    user_id_override: Optional[str] = None


class Message(BaseModel):
    template: str

    data: Optional[Dict[str, object]] = None

    delay: Optional[MessageDelay] = None

    to: Optional[MessageTo] = None


class JourneySendNode(BaseModel):
    """Send a notification template to the recipient.

    Optionally override the recipient address, delay the send, or attach `data`.
    """

    message: Message

    type: Literal["send"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """
