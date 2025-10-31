# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalChannelNode"]


class ElementalChannelNode(ElementalBaseNode, total=False):
    channel: Required[str]
    """The channel the contents of this element should be applied to.

    Can be `email`, `push`, `direct_message`, `sms` or a provider such as slack
    """

    raw: Optional[Dict[str, object]]
    """Raw data to apply to the channel.

    If `elements` has not been specified, `raw` is required.
    """
