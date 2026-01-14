# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalChannelNode"]


class ElementalChannelNode(ElementalBaseNode):
    """
    The channel element allows a notification to be customized based on which channel it is sent through.
    For example, you may want to display a detailed message when the notification is sent through email,
    and a more concise message in a push notification. Channel elements are only valid as top-level
    elements; you cannot nest channel elements. If there is a channel element specified at the top-level
    of the document, all sibling elements must be channel elements.
    Note: As an alternative, most elements support a `channel` property. Which allows you to selectively
    display an individual element on a per channel basis. See the
    [control flow docs](https://www.courier.com/docs/platform/content/elemental/control-flow/) for more details.
    """

    channel: Optional[str] = None
    """The channel the contents of this element should be applied to.

    Can be `email`, `push`, `direct_message`, `sms` or a provider such as slack
    """

    raw: Optional[Dict[str, object]] = None
    """Raw data to apply to the channel.

    If `elements` has not been specified, `raw` is required.
    """
