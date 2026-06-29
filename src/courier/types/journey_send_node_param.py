# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .journey_experiment_param import JourneyExperimentParam
from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneySendNodeParam", "Message", "MessageDelay", "MessageTo"]


class MessageDelay(TypedDict, total=False):
    until: Required[str]

    timezone: str


class MessageTo(TypedDict, total=False):
    email_override: str

    phone_number_override: str

    user_id_override: str


class Message(TypedDict, total=False):
    data: Dict[str, object]

    delay: MessageDelay

    template: str

    to: MessageTo


class JourneySendNodeParam(TypedDict, total=False):
    """Send to the recipient.

    A send node sources its content from EXACTLY ONE of `message.template` (a single notification template) or `experiment` (an A/B split across weighted template variants) — supplying both, or neither, is rejected. Optionally override the recipient address, delay the send, or attach `data`.
    """

    message: Required[Message]

    type: Required[Literal["send"]]

    id: str

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
