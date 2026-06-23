# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..notification_template_state import NotificationTemplateState

__all__ = ["TemplatePutLocaleParams", "Element"]


class TemplatePutLocaleParams(TypedDict, total=False):
    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]

    notification_id: Required[Annotated[str, PropertyInfo(alias="notificationId")]]

    elements: Required[Iterable[Element]]
    """Elements with locale-specific content overrides."""

    state: NotificationTemplateState
    """Template state. Defaults to `DRAFT`."""


class Element(TypedDict, total=False, extra_items=object):  # type: ignore[call-arg]
    id: Required[str]
    """Target element ID."""
