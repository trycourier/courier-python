# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo
from ..shared_params.elemental_node import ElementalNode

__all__ = [
    "TemplateCreateParams",
    "Notification",
    "NotificationBrand",
    "NotificationContent",
    "NotificationSubscription",
]


class TemplateCreateParams(TypedDict, total=False):
    channel: Required[str]

    notification: Required[Notification]

    provider_key: Annotated[str, PropertyInfo(alias="providerKey")]

    state: str


class NotificationBrand(TypedDict, total=False):
    id: Required[str]


class NotificationContent(TypedDict, total=False):
    elements: Required[Iterable[ElementalNode]]

    version: Required[Literal["2022-01-01"]]

    scope: Literal["default", "strict"]


class NotificationSubscription(TypedDict, total=False):
    topic_id: Required[str]


class Notification(TypedDict, total=False):
    brand: Required[Optional[NotificationBrand]]

    content: Required[NotificationContent]

    name: Required[str]

    subscription: Required[Optional[NotificationSubscription]]

    tags: Required[SequenceNotStr[str]]
