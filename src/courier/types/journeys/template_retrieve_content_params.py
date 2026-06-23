# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TemplateRetrieveContentParams"]


class TemplateRetrieveContentParams(TypedDict, total=False):
    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]

    version: str
    """Accepts `draft`, `published`, or a version string (e.g., `v001`).

    Defaults to `published`.
    """
