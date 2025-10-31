# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalChannelNode"]


class ElementalChannelNode(ElementalBaseNode):
    channel: str
    """The channel the contents of this element should be applied to.

    Can be `email`, `push`, `direct_message`, `sms` or a provider such as slack
    """

    raw: Optional[Dict[str, object]] = None
    """Raw data to apply to the channel.

    If `elements` has not been specified, `raw` is required.
    """
