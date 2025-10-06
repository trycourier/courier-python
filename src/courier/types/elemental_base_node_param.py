# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from .._types import SequenceNotStr

__all__ = ["ElementalBaseNodeParam"]

_ElementalBaseNodeParamReservedKeywords = TypedDict(
    "_ElementalBaseNodeParamReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalBaseNodeParam(_ElementalBaseNodeParamReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]
