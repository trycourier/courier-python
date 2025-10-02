# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .merge_algorithm import MergeAlgorithm
from .automation_step_param import AutomationStepParam

__all__ = [
    "InvokeInvokeAdHocParams",
    "Automation",
    "AutomationStep",
    "AutomationStepAutomationAddToDigestStep",
    "AutomationStepAutomationAddToBatchStep",
    "AutomationStepAutomationAddToBatchStepRetain",
    "AutomationStepAutomationThrottleStep",
    "AutomationStepAutomationThrottleStepOnThrottle",
    "AutomationStepAutomationCancelStep",
    "AutomationStepAutomationDelayStep",
    "AutomationStepAutomationFetchDataStep",
    "AutomationStepAutomationFetchDataStepWebhook",
    "AutomationStepAutomationInvokeStep",
    "AutomationStepAutomationSendStep",
    "AutomationStepAutomationV2SendStep",
    "AutomationStepAutomationSendListStep",
    "AutomationStepAutomationUpdateProfileStep",
]


class InvokeInvokeAdHocParams(TypedDict, total=False):
    automation: Required[Automation]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    profile: object

    recipient: Optional[str]

    template: Optional[str]


class AutomationStepAutomationAddToDigestStep(AutomationStepParam, total=False):
    action: Required[Literal["add-to-digest"]]

    subscription_topic_id: Required[str]
    """The subscription topic that has digests enabled"""


class AutomationStepAutomationAddToBatchStepRetain(TypedDict, total=False):
    count: Required[int]
    """The number of records to keep in batch.

    Default is 10 and only configurable by requesting from support. When
    configurable minimum is 2 and maximum is 100.
    """

    type: Required[Literal["first", "last", "highest", "lowest"]]
    """Keep N number of notifications based on the type.

    First/Last N based on notification received. highest/lowest based on a scoring
    key providing in the data accessed by sort_key
    """

    sort_key: Optional[str]
    """Defines the data value data[sort_key] that is used to sort the stored items.

    Required when type is set to highest or lowest.
    """


class AutomationStepAutomationAddToBatchStep(AutomationStepParam, total=False):
    action: Required[Literal["add-to-batch"]]

    max_wait_period: Required[str]
    """Defines the maximum wait time before the batch should be released.

    Must be less than wait period. Maximum of 60 days. Specified as an
    [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    """

    retain: Required[AutomationStepAutomationAddToBatchStepRetain]
    """
    Defines what items should be retained and passed along to the next steps when
    the batch is released
    """

    wait_period: Required[str]
    """Defines the period of inactivity before the batch is released.

    Specified as an
    [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    """

    batch_id: Optional[str]

    batch_key: Optional[str]
    """
    If using scope=dynamic, provide the key or a reference (e.g.,
    refs.data.batch_key)
    """

    category_key: Optional[str]
    """Defines the field of the data object the batch is set to when complete.

    Defaults to `batch`
    """

    max_items: Union[str, int, None]
    """If specified, the batch will release as soon as this number is reached"""

    scope: Optional[Literal["user", "global", "dynamic"]]
    """Determine the scope of the batching.

    If user, chosen in this order: recipient, profile.user_id, data.user_id,
    data.userId. If dynamic, then specify where the batch_key or a reference to the
    batch_key
    """


class AutomationStepAutomationThrottleStepOnThrottle(TypedDict, total=False):
    node_id: Required[Annotated[str, PropertyInfo(alias="$node_id")]]
    """The node to go to if the request is throttled"""


class AutomationStepAutomationThrottleStep(AutomationStepParam, total=False):
    action: Required[Literal["throttle"]]

    max_allowed: Required[int]
    """Maximum number of allowed notifications in that timeframe"""

    on_throttle: Required[AutomationStepAutomationThrottleStepOnThrottle]

    period: Required[str]
    """Defines the throttle period which corresponds to the max_allowed.

    Specified as an ISO 8601 duration,
    https://en.wikipedia.org/wiki/ISO_8601#Durations
    """

    scope: Required[Literal["user", "global", "dynamic"]]

    should_alert: Required[bool]
    """Value must be true"""

    throttle_key: Optional[str]
    """
    If using scope=dynamic, provide the reference (e.g., refs.data.throttle_key) to
    the how the throttle should be identified
    """


class AutomationStepAutomationCancelStep(AutomationStepParam, total=False):
    action: Required[Literal["cancel"]]

    cancelation_token: Optional[str]


class AutomationStepAutomationDelayStep(AutomationStepParam, total=False):
    action: Required[Literal["delay"]]

    duration: Optional[str]
    """
    The [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) string
    for how long to delay for
    """

    until: Optional[str]
    """The ISO 8601 timestamp for when the delay should end"""


class AutomationStepAutomationFetchDataStepWebhook(TypedDict, total=False):
    method: Required[Literal["GET", "POST"]]

    url: Required[str]

    body: Optional[Dict[str, object]]

    headers: Optional[Dict[str, object]]

    params: Optional[Dict[str, object]]


class AutomationStepAutomationFetchDataStep(AutomationStepParam, total=False):
    action: Required[Literal["fetch-data"]]

    merge_strategy: Required[MergeAlgorithm]

    webhook: Required[AutomationStepAutomationFetchDataStepWebhook]

    idempotency_expiry: Optional[str]

    idempotency_key: Optional[str]


class AutomationStepAutomationInvokeStep(AutomationStepParam, total=False):
    action: Required[Literal["invoke"]]

    template: Required[str]


class AutomationStepAutomationSendStep(AutomationStepParam, total=False):
    action: Required[Literal["send"]]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    override: Optional[Dict[str, object]]

    profile: object

    recipient: Optional[str]

    template: Optional[str]


class AutomationStepAutomationV2SendStep(AutomationStepParam, total=False):
    action: Required[Literal["send"]]

    message: Required["MessageParam"]
    """
    Describes the content of the message in a way that will work for email, push,
    chat, or any channel.
    """


class AutomationStepAutomationSendListStep(AutomationStepParam, total=False):
    action: Required[Literal["send-list"]]

    list: Required[str]

    brand: Optional[str]

    data: Optional[Dict[str, object]]

    override: Optional[Dict[str, object]]

    template: Optional[str]


class AutomationStepAutomationUpdateProfileStep(TypedDict, total=False):
    action: Required[Literal["update-profile"]]

    merge: Required[MergeAlgorithm]

    profile: Required[object]

    recipient_id: Required[str]


AutomationStep: TypeAlias = Union[
    AutomationStepAutomationAddToDigestStep,
    AutomationStepAutomationAddToBatchStep,
    AutomationStepAutomationThrottleStep,
    AutomationStepAutomationCancelStep,
    AutomationStepAutomationDelayStep,
    AutomationStepAutomationFetchDataStep,
    AutomationStepAutomationInvokeStep,
    AutomationStepAutomationSendStep,
    AutomationStepAutomationV2SendStep,
    AutomationStepAutomationSendListStep,
    AutomationStepAutomationUpdateProfileStep,
]


class Automation(TypedDict, total=False):
    steps: Required[Iterable[AutomationStep]]

    cancelation_token: Optional[str]


from ..message_param import MessageParam
