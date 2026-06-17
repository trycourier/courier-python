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

__all__ = [
    "JourneyNodeParam",
    "JourneyBatchNode",
    "JourneyBatchNodeRetain",
    "JourneyAddToDigestNode",
    "JourneyBranchNode",
    "JourneyBranchNodeDefault",
    "JourneyBranchNodePath",
]


class JourneyBatchNodeRetain(TypedDict, total=False):
    """
    How to select which collected events to retain in the aggregated payload when the batch releases.
    """

    count: Required[int]

    type: Required[Literal["first", "last", "highest", "lowest"]]

    sort_key: str
    """Dot-path into the event payload (e.g.

    `data.priority`). Required when `type` is `highest` or `lowest`.
    """


class JourneyBatchNode(TypedDict, total=False):
    """
    Collect events arriving at the node into a single batch and fire one downstream step with the aggregated payload. The first event into a batch owns the run; later contributing events terminate at the batch step. The batch releases when any of `max_items` is reached, a quiet window of `wait_period` elapses, or the `max_wait_period` ceiling hits.
    """

    max_wait_period: Required[str]
    """ISO 8601 duration.

    Hard ceiling from the first event into the batch; releases the batch
    unconditionally when it elapses.
    """

    retain: Required[JourneyBatchNodeRetain]
    """
    How to select which collected events to retain in the aggregated payload when
    the batch releases.
    """

    scope: Required[Literal["user"]]

    type: Required[Literal["batch"]]

    wait_period: Required[str]
    """ISO 8601 duration.

    Quiet window that releases the batch when it elapses with no new contributing
    events. Must be less than `max_wait_period`.
    """

    id: str

    category_key: str
    """Optional partition key.

    Events with the same `category_key` are batched together; events with different
    values are batched separately.
    """

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    max_items: int
    """Releases the batch once this many events have been collected."""


class JourneyAddToDigestNode(TypedDict, total=False):
    """Add the current event to a digest keyed by the given subscription topic.

    The digest accumulates events and releases them on the schedule configured for the topic.
    """

    subscription_topic_id: Required[str]
    """The subscription topic that owns the digest the event is added to."""

    type: Required[Literal["add-to-digest"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """


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

    Routes to the first entry in `paths[]` whose `conditions` match, else falls through to `default.nodes`.
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
    JourneyBatchNode,
    JourneyAddToDigestNode,
    JourneyExitNodeParam,
    JourneyBranchNode,
]
