# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .notification_template_state import NotificationTemplateState
from .shared_params.elemental_node import ElementalNode

__all__ = ["NotificationPutContentParams", "Content"]


class NotificationPutContentParams(TypedDict, total=False):
    content: Required[Content]
    """Elemental content payload. The server defaults `version` when omitted."""

    state: NotificationTemplateState
    """Template state. Defaults to `DRAFT`."""


class Content(TypedDict, total=False):
    """Elemental content payload. The server defaults `version` when omitted."""

    elements: Required[Iterable[ElementalNode]]

    version: str
    """Content version identifier (e.g., `2022-01-01`).

    Optional; server defaults when omitted.
    """
