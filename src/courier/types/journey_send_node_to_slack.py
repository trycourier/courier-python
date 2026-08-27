# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .journey_send_node_to_slack_email import JourneySendNodeToSlackEmail
from .journey_send_node_to_slack_channel import JourneySendNodeToSlackChannel
from .journey_send_node_to_slack_user_id import JourneySendNodeToSlackUserID

__all__ = ["JourneySendNodeToSlack"]

JourneySendNodeToSlack: TypeAlias = Union[
    JourneySendNodeToSlackChannel, JourneySendNodeToSlackUserID, JourneySendNodeToSlackEmail
]
