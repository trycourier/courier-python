# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .journey_ai_node_param import JourneyAINodeParam
from .journey_exit_node_param import JourneyExitNodeParam
from .journey_send_node_param import JourneySendNodeParam
from .journey_conditions_field_param import JourneyConditionsFieldParam
from .journey_delay_until_node_param import JourneyDelayUntilNodeParam
from .journey_delay_duration_node_param import JourneyDelayDurationNodeParam
from .journey_fetch_post_put_node_param import JourneyFetchPostPutNodeParam
from .journey_segment_trigger_node_param import JourneySegmentTriggerNodeParam
from .journey_throttle_static_node_param import JourneyThrottleStaticNodeParam
from .journey_fetch_get_delete_node_param import JourneyFetchGetDeleteNodeParam
from .journey_throttle_dynamic_node_param import JourneyThrottleDynamicNodeParam
from .journey_api_invoke_trigger_node_param import JourneyAPIInvokeTriggerNodeParam

__all__ = ["JourneyNodeParam", "JourneyBranchNode", "JourneyBranchNodeDefault", "JourneyBranchNodePath"]


class JourneyBranchNodeDefault(TypedDict, total=False):
    nodes: Required[Iterable["JourneyNodeParam"]]

    label: str


class JourneyBranchNodePath(TypedDict, total=False):
    conditions: Required[JourneyConditionsFieldParam]
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    nodes: Required[Iterable["JourneyNodeParam"]]

    label: str


class JourneyBranchNode(TypedDict, total=False):
    """Branch node.

    Routes to one of `paths[]` whose `conditions` match, else falls through to `default.nodes`. Inlined rather than referenced so the recursive `nodes: JourneyNode[]` cycle stays within a single generated module (Stainless Python forward-ref resolution does not span modules well for this recursion shape).
    """

    default: Required[JourneyBranchNodeDefault]

    paths: Required[Iterable[JourneyBranchNodePath]]

    type: Required[Literal["branch"]]

    id: str


JourneyNodeParam: TypeAlias = Union[
    JourneyAPIInvokeTriggerNodeParam,
    JourneySegmentTriggerNodeParam,
    JourneySendNodeParam,
    JourneyDelayDurationNodeParam,
    JourneyDelayUntilNodeParam,
    JourneyFetchGetDeleteNodeParam,
    JourneyFetchPostPutNodeParam,
    JourneyAINodeParam,
    JourneyThrottleStaticNodeParam,
    JourneyThrottleDynamicNodeParam,
    JourneyExitNodeParam,
    JourneyBranchNode,
]
