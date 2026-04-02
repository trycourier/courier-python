# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .notification_template_payload_param import NotificationTemplatePayloadParam

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    notification: Required[NotificationTemplatePayloadParam]
    """
    Full document shape used in POST and PUT request bodies, and returned inside the
    GET response envelope.
    """

    state: Literal["DRAFT", "PUBLISHED"]
    """Template state after creation.

    Case-insensitive input, normalized to uppercase in the response. Defaults to
    "DRAFT".
    """
