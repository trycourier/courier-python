# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ElementalChannelNode"]


class ElementalChannelNode(BaseModel):
    channel: str
    """The channel the contents of this element should be applied to.

    Can be `email`, `push`, `direct_message`, `sms` or a provider such as slack
    """

    channels: Optional[List[str]] = None

    elements: Optional[List["ElementalNode"]] = None
    """An array of elements to apply to the channel.

    If `raw` has not been specified, `elements` is `required`.
    """

    if_: Optional[str] = FieldInfo(alias="if", default=None)

    loop: Optional[str] = None

    raw: Optional[Dict[str, object]] = None
    """Raw data to apply to the channel.

    If `elements` has not been specified, `raw` is `required`.
    """

    ref: Optional[str] = None


from .elemental_node import ElementalNode
