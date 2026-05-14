# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["JourneyExitNodeParam"]


class JourneyExitNodeParam(TypedDict, total=False):
    type: Required[Literal["exit"]]

    id: str
