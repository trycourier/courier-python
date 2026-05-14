# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_merge_strategy import JourneyMergeStrategy
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyFetchPostPutNode"]


class JourneyFetchPostPutNode(BaseModel):
    merge_strategy: JourneyMergeStrategy

    method: Literal["post", "put"]

    type: Literal["fetch"]

    url: str

    id: Optional[str] = None

    body: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    headers: Optional[Dict[str, str]] = None

    query_params: Optional[Dict[str, str]] = None

    response_schema: Optional[Dict[str, object]] = None
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""
