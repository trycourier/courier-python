# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ElementalGroupNodeParam"]

_ElementalGroupNodeParamReservedKeywords = TypedDict(
    "_ElementalGroupNodeParamReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalGroupNodeParam(_ElementalGroupNodeParamReservedKeywords, total=False):
    elements: Required[Iterable["ElementalNodeParam"]]
    """Sub elements to render."""

    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]


from .elemental_node_param import ElementalNodeParam
