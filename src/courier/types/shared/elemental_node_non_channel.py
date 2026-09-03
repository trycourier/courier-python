# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .elemental_html_node import ElementalHTMLNode
from .elemental_meta_node import ElementalMetaNode
from .elemental_text_node import ElementalTextNode
from .elemental_image_node import ElementalImageNode
from .elemental_quote_node import ElementalQuoteNode
from .elemental_action_node import ElementalActionNode
from .elemental_divider_node import ElementalDividerNode

__all__ = [
    "ElementalNodeNonChannel",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
    "UnionMember5",
    "UnionMember6",
]


class UnionMember0(ElementalTextNode):
    """Represents a body of text to be rendered inside of the notification."""

    type: Optional[Literal["text"]] = None


class UnionMember1(ElementalMetaNode):
    """
    The meta element contains information describing the notification that may  be used by a particular channel or provider. One important field is the title  field which will be used as the title for channels that support it.
    """

    type: Optional[Literal["meta"]] = None


class UnionMember2(ElementalImageNode):
    """Used to embed an image into the notification."""

    type: Optional[Literal["image"]] = None


class UnionMember3(ElementalActionNode):
    """Allows the user to execute an action. Can be a button or a link."""

    type: Optional[Literal["action"]] = None


class UnionMember4(ElementalDividerNode):
    """Renders a dividing line between elements."""

    type: Optional[Literal["divider"]] = None


class UnionMember5(ElementalQuoteNode):
    """Renders a quote block."""

    type: Optional[Literal["quote"]] = None


class UnionMember6(ElementalHTMLNode):
    """Raw HTML string inside an Elemental document.

    When rendering a message, this node is turned into output only for the email channel; for other channels it produces no blocks.
    """

    type: Optional[Literal["html"]] = None


ElementalNodeNonChannel: TypeAlias = Union[
    UnionMember0, UnionMember1, UnionMember2, UnionMember3, UnionMember4, UnionMember5, UnionMember6
]
