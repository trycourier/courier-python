# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .elemental_base_node import ElementalBaseNode
from .elemental_meta_node_with_type import ElementalMetaNodeWithType
from .elemental_text_node_with_type import ElementalTextNodeWithType
from .elemental_image_node_with_type import ElementalImageNodeWithType
from .elemental_quote_node_with_type import ElementalQuoteNodeWithType
from .elemental_action_node_with_type import ElementalActionNodeWithType
from .elemental_channel_node_with_type import ElementalChannelNodeWithType
from .elemental_divider_node_with_type import ElementalDividerNodeWithType

__all__ = ["ElementalNode", "UnionMember7"]


class UnionMember7(ElementalBaseNode):
    type: Optional[Literal["html"]] = None


ElementalNode: TypeAlias = Union[
    ElementalTextNodeWithType,
    ElementalMetaNodeWithType,
    ElementalChannelNodeWithType,
    ElementalImageNodeWithType,
    ElementalActionNodeWithType,
    ElementalDividerNodeWithType,
    ElementalQuoteNodeWithType,
    UnionMember7,
]
