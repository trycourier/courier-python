# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

from .._models import BaseModel

__all__ = ["NotificationContentGetResponse"]


class NotificationContentGetResponse(BaseModel):
    """Elemental content response for V2 templates.

    Contains versioned elements with content checksums.
    """

    elements: List["ElementWithChecksums"]

    version: str
    """Content version identifier."""


from .element_with_checksums import ElementWithChecksums
