# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .elemental_action_node import ElementalActionNode

__all__ = ["ElementalActionNodeWithType"]


class ElementalActionNodeWithType(ElementalActionNode):
    """Allows the user to execute an action. Can be a button or a link."""

    type: Optional[Literal["action"]] = None
