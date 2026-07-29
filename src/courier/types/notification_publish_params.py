# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["NotificationPublishParams"]


class NotificationPublishParams(TypedDict, total=False):
    version: str
    """Historical version to publish (e.g. "v001"). Omit to publish the current draft."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
