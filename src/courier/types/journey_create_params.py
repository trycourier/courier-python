# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .journey_state import JourneyState

__all__ = ["JourneyCreateParams"]


class JourneyCreateParams(TypedDict, total=False):
    name: Required[str]

    nodes: Required[Iterable["JourneyNodeParam"]]

    enabled: bool

    state: JourneyState
    """Lifecycle state of a journey."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]


from .journey_node_param import JourneyNodeParam
