# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemplatePublishParams"]


class TemplatePublishParams(TypedDict, total=False):
    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]

    version: str

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
