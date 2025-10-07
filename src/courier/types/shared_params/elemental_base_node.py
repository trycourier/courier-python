# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["ElementalBaseNode"]

_ElementalBaseNodeReservedKeywords = TypedDict(
    "_ElementalBaseNodeReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalBaseNode(_ElementalBaseNodeReservedKeywords, total=False):
    channels: Optional[SequenceNotStr[str]]

    loop: Optional[str]

    ref: Optional[str]
