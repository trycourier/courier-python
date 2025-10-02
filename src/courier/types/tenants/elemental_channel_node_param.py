# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Required, TypedDict

from ..._types import SequenceNotStr

__all__ = ["ElementalChannelNodeParam"]

_ElementalChannelNodeParamReservedKeywords = TypedDict(
    "_ElementalChannelNodeParamReservedKeywords",
    {
        "if": Optional[str],
    },
    total=False,
)


class ElementalChannelNodeParam(_ElementalChannelNodeParamReservedKeywords, total=False):
    channel: Required[str]
    """The channel the contents of this element should be applied to.

    Can be `email`, `push`, `direct_message`, `sms` or a provider such as slack
    """

    channels: Optional[SequenceNotStr[str]]

    elements: Optional[Iterable["ElementalNodeParam"]]
    """An array of elements to apply to the channel.

    If `raw` has not been specified, `elements` is `required`.
    """

    loop: Optional[str]

    raw: Optional[Dict[str, object]]
    """Raw data to apply to the channel.

    If `elements` has not been specified, `raw` is `required`.
    """

    ref: Optional[str]


from .elemental_node_param import ElementalNodeParam
