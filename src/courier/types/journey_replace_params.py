# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .journey_state import JourneyState

__all__ = ["JourneyReplaceParams"]


class JourneyReplaceParams(TypedDict, total=False):
    name: Required[str]

    nodes: Required[Iterable["JourneyNodeParam"]]

    cancelation_token: str
    """Cancelation token stored on the journey definition.

    It tags every run the journey creates so that `POST /journeys/cancel` can later
    cancel those runs by token. Accepts a templated string such as
    `order-{{data.order_id}}`, which is resolved per run when the journey is
    invoked. On a replace, omitting this field preserves any existing token and
    sending a value replaces it.
    """

    enabled: bool

    state: JourneyState
    """Lifecycle state of a journey."""


from .journey_node_param import JourneyNodeParam
