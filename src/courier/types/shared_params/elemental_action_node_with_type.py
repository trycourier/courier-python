# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

from .elemental_action_node import ElementalActionNode

__all__ = ["ElementalActionNodeWithType"]


class ElementalActionNodeWithType(ElementalActionNode, total=False):
    """Allows the user to execute an action. Can be a button or a link."""

    type: Literal["action"]
