# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .notification_template_state import NotificationTemplateState
from .shared_params.elemental_node import ElementalNode

__all__ = ["BroadcastPutContentParams", "Content"]


class BroadcastPutContentParams(TypedDict, total=False):
    content: Required[Content]
    """Elemental content payload. The server defaults `version` when omitted."""

    state: NotificationTemplateState
    """Template state. Defaults to `DRAFT`."""


class Content(TypedDict, total=False):
    """Elemental content payload. The server defaults `version` when omitted."""

    elements: Required[Iterable[ElementalNode]]

    scope: Literal["default", "strict"]
    """How template variables read the data sent with the message.

    Under `strict`, data fields are read only through the `data.` prefix, as in
    `{{data.name}}`. Under `default`, `data` is spread onto the root, so `{{name}}`
    resolves and `{{data.name}}` renders as an empty string. This request replaces
    the stored content, so omitting `scope` resets it to `default`.
    """

    version: str
    """Content version identifier (e.g., `2022-01-01`).

    Optional; server defaults when omitted.
    """
