# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .notification_template_state import NotificationTemplateState

__all__ = ["NotificationPutElementParams"]


class NotificationPutElementParams(TypedDict, total=False):
    id: Required[str]

    type: Required[str]
    """Element type (text, meta, action, image, etc.)."""

    channels: SequenceNotStr[str]

    data: Dict[str, object]

    if_: Annotated[str, PropertyInfo(alias="if")]

    loop: str

    ref: str

    state: NotificationTemplateState
    """Template state. Defaults to `DRAFT`."""
