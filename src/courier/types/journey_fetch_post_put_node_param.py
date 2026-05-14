# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .journey_merge_strategy import JourneyMergeStrategy
from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyFetchPostPutNodeParam"]


class JourneyFetchPostPutNodeParam(TypedDict, total=False):
    merge_strategy: Required[JourneyMergeStrategy]

    method: Required[Literal["post", "put"]]

    type: Required[Literal["fetch"]]

    url: Required[str]

    id: str

    body: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    headers: Dict[str, str]

    query_params: Dict[str, str]

    response_schema: Dict[str, object]
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""
