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

__all__ = [
    "JourneyNode",
    "JourneyBatchNode",
    "JourneyBatchNodeRetain",
    "JourneyBranchNode",
    "JourneyBranchNodeDefault",
    "JourneyBranchNodePath",
]


class JourneyBatchNodeRetain(BaseModel):
    """
    How to select which collected events to retain in the aggregated payload when the batch releases.
    """

    count: int

    type: Literal["first", "last", "highest", "lowest"]

    sort_key: Optional[str] = None
    """Dot-path into the event payload (e.g.

    `data.priority`). Required when `type` is `highest` or `lowest`.
    """


class JourneyBatchNode(BaseModel):
    """
    Collect events arriving at the node into a single batch and fire one downstream step with the aggregated payload. The first event into a batch owns the run; later contributing events terminate at the batch step. The batch releases when any of `max_items` is reached, a quiet window of `wait_period` elapses, or the `max_wait_period` ceiling hits.
    """

    max_wait_period: str
    """ISO 8601 duration.

    Hard ceiling from the first event into the batch; releases the batch
    unconditionally when it elapses.
    """

    retain: JourneyBatchNodeRetain
    """
    How to select which collected events to retain in the aggregated payload when
    the batch releases.
    """

    scope: Literal["user"]

    type: Literal["batch"]

    wait_period: str
    """ISO 8601 duration.

    Quiet window that releases the batch when it elapses with no new contributing
    events. Must be less than `max_wait_period`.
    """

    id: Optional[str] = None

    category_key: Optional[str] = None
    """Optional partition key.

    Events with the same `category_key` are batched together; events with different
    values are batched separately.
    """

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    max_items: Optional[int] = None
    """Releases the batch once this many events have been collected."""


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

    Routes to the first entry in `paths[]` whose `conditions` match, else falls through to `default.nodes`.
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
    JourneyBatchNode,
    JourneyExitNode,
    JourneyBranchNode,
]
