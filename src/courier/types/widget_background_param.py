# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WidgetBackgroundParam"]


class WidgetBackgroundParam(TypedDict, total=False):
    bottom_color: Annotated[Optional[str], PropertyInfo(alias="bottomColor")]

    top_color: Annotated[Optional[str], PropertyInfo(alias="topColor")]
