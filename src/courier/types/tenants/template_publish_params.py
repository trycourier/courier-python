# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TemplatePublishParams"]


class TemplatePublishParams(TypedDict, total=False):
    tenant_id: Required[str]

    version: str
    """The version of the template to publish (e.g., "v1", "v2", "latest").

    If not provided, defaults to "latest".
    """
