# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict

from .shared_params.elemental_content import ElementalContent
from .shared_params.elemental_content_sugar import ElementalContentSugar

__all__ = ["InboundBulkMessageParam", "Content"]

Content: TypeAlias = Union[ElementalContentSugar, ElementalContent]


class InboundBulkMessageParam(TypedDict, total=False):
    """Bulk message definition.

    Supports two formats:
    - V1 format: Requires `event` field (event ID or notification ID)
    - V2 format: Optionally use `template` (notification ID) or `content` (Elemental content) in addition to `event`
    """

    event: Required[str]
    """Event ID or Notification ID (required).

    Can be either a Notification ID (e.g., "FRH3QXM9E34W4RKP7MRC8NZ1T8V8") or a
    custom Event ID (e.g., "welcome-email") mapped to a notification.
    """

    brand: Optional[str]

    content: Optional[Content]
    """Elemental content (optional, for V2 format).

    When provided, this will be used instead of the notification associated with the
    `event` field.
    """

    data: Optional[Dict[str, object]]

    locale: Optional[Dict[str, Dict[str, object]]]

    override: Optional[Dict[str, object]]

    template: Optional[str]
    """Notification ID or template ID (optional, for V2 format).

    When provided, this will be used instead of the notification associated with the
    `event` field.
    """
