# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .notification_get_content import NotificationGetContent

__all__ = ["NotificationRetrieveContentResponse"]

NotificationRetrieveContentResponse: TypeAlias = Union["NotificationContentGetResponse", NotificationGetContent]

from .notification_content_get_response import NotificationContentGetResponse
