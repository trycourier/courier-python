# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .journey_state import JourneyState

__all__ = ["JourneyReplaceParams"]


class JourneyReplaceParams(TypedDict, total=False):
    name: Required[str]

    nodes: Required[Iterable["JourneyNodeParam"]]

    enabled: bool

    state: JourneyState
    """Lifecycle state of a journey."""


from .journey_node_param import JourneyNodeParam
