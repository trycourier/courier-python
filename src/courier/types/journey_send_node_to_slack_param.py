# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .journey_send_node_to_slack_email_param import JourneySendNodeToSlackEmailParam
from .journey_send_node_to_slack_channel_param import JourneySendNodeToSlackChannelParam
from .journey_send_node_to_slack_user_id_param import JourneySendNodeToSlackUserIDParam

__all__ = ["JourneySendNodeToSlackParam"]

JourneySendNodeToSlackParam: TypeAlias = Union[
    JourneySendNodeToSlackChannelParam, JourneySendNodeToSlackUserIDParam, JourneySendNodeToSlackEmailParam
]
