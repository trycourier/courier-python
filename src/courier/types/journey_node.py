# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel
from .journey_ai_node import JourneyAINode
from .journey_exit_node import JourneyExitNode
from .journey_send_node import JourneySendNode
from .journey_conditions_field import JourneyConditionsField
from .journey_delay_until_node import JourneyDelayUntilNode
from .journey_delay_duration_node import JourneyDelayDurationNode
from .journey_fetch_post_put_node import JourneyFetchPostPutNode
from .journey_segment_trigger_node import JourneySegmentTriggerNode
from .journey_throttle_static_node import JourneyThrottleStaticNode
from .journey_fetch_get_delete_node import JourneyFetchGetDeleteNode
from .journey_throttle_dynamic_node import JourneyThrottleDynamicNode
from .journey_api_invoke_trigger_node import JourneyAPIInvokeTriggerNode

__all__ = ["JourneyNode", "JourneyBranchNode", "JourneyBranchNodeDefault", "JourneyBranchNodePath"]


class JourneyBranchNodeDefault(BaseModel):
    nodes: List["JourneyNode"]

    label: Optional[str] = None


class JourneyBranchNodePath(BaseModel):
    conditions: JourneyConditionsField
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    nodes: List["JourneyNode"]

    label: Optional[str] = None


class JourneyBranchNode(BaseModel):
    """Branch node.

    Routes to one of `paths[]` whose `conditions` match, else falls through to `default.nodes`. Inlined rather than referenced so the recursive `nodes: JourneyNode[]` cycle stays within a single generated module (Stainless Python forward-ref resolution does not span modules well for this recursion shape).
    """

    default: JourneyBranchNodeDefault

    paths: List[JourneyBranchNodePath]

    type: Literal["branch"]

    id: Optional[str] = None


JourneyNode: TypeAlias = Union[
    JourneyAPIInvokeTriggerNode,
    JourneySegmentTriggerNode,
    JourneySendNode,
    JourneyDelayDurationNode,
    JourneyDelayUntilNode,
    JourneyFetchGetDeleteNode,
    JourneyFetchPostPutNode,
    JourneyAINode,
    JourneyThrottleStaticNode,
    JourneyThrottleDynamicNode,
    JourneyExitNode,
    JourneyBranchNode,
]
