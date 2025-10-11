# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .elemental_meta_node_with_type import ElementalMetaNodeWithType
from .elemental_text_node_with_type import ElementalTextNodeWithType
from .elemental_image_node_with_type import ElementalImageNodeWithType
from .elemental_quote_node_with_type import ElementalQuoteNodeWithType
from .elemental_action_node_with_type import ElementalActionNodeWithType
from .elemental_channel_node_with_type import ElementalChannelNodeWithType
from .elemental_divider_node_with_type import ElementalDividerNodeWithType

__all__ = ["ElementalNode"]

ElementalNode: TypeAlias = Union[
    ElementalTextNodeWithType,
    ElementalMetaNodeWithType,
    ElementalChannelNodeWithType,
    ElementalImageNodeWithType,
    ElementalActionNodeWithType,
    ElementalDividerNodeWithType,
    ElementalQuoteNodeWithType,
]
