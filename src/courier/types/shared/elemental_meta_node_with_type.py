# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_meta_node import ElementalMetaNode

__all__ = ["ElementalMetaNodeWithType"]


class ElementalMetaNodeWithType(ElementalMetaNode):
    """
    The meta element contains information describing the notification that may  be used by a particular channel or provider. One important field is the title  field which will be used as the title for channels that support it.
    """

    type: Optional[Literal["meta"]] = None
