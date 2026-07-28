# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WorkspacePreferencePublishParams"]


class WorkspacePreferencePublishParams(TypedDict, total=False):
    brand_id: Optional[str]
    """
    Brand for the hosted page - "default" (workspace default brand), "none" (no
    brand), or a specific brand id. Defaults to "default".
    """

    description: Optional[str]
    """Description shown under the heading on the hosted preferences page."""

    heading: Optional[str]
    """Heading shown at the top of the hosted preferences page."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
