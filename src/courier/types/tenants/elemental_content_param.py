# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["ElementalContentParam"]


class ElementalContentParam(TypedDict, total=False):
    elements: Required[Iterable["ElementalNodeParam"]]

    version: Required[str]
    """For example, "2022-01-01" """

    brand: object


from .elemental_node_param import ElementalNodeParam
