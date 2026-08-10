# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .notification_template_write_payload_param import NotificationTemplateWritePayloadParam

__all__ = ["NotificationCreateParams"]


class NotificationCreateParams(TypedDict, total=False):
    notification: Required[NotificationTemplateWritePayloadParam]
    """
    Template fields accepted in POST and PUT request bodies, nested under a
    `notification` key.
    """

    state: Literal["DRAFT", "PUBLISHED"]
    """Template state after creation.

    Case-insensitive input, normalized to uppercase in the response. Defaults to
    "DRAFT".
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
