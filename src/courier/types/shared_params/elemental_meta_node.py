# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalMetaNode"]


class ElementalMetaNode(ElementalBaseNode, total=False):
    """
    The meta element contains information describing the notification that may  be used by a particular channel or provider. One important field is the title  field which will be used as the title for channels that support it.
    """

    title: Optional[str]
    """The title to be displayed by supported channels.

    For example, the email subject.
    """
