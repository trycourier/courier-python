# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BrandTemplateParam"]


class BrandTemplateParam(TypedDict, total=False):
    enabled: Required[bool]

    background_color: Annotated[Optional[str], PropertyInfo(alias="backgroundColor")]

    blocks_background_color: Annotated[Optional[str], PropertyInfo(alias="blocksBackgroundColor")]

    footer: Optional[str]

    head: Optional[str]

    header: Optional[str]

    width: Optional[str]
