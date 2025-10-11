# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from .elemental_node import ElementalNode

__all__ = ["ElementalContent"]


class ElementalContent(TypedDict, total=False):
    elements: Required[Iterable[ElementalNode]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: Optional[str]
