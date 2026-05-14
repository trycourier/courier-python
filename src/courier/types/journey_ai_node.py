# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyAINode"]


class JourneyAINode(BaseModel):
    output_schema: Dict[str, object]
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""

    type: Literal["ai"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    model: Optional[str] = None

    user_prompt: Optional[str] = None

    web_search: Optional[bool] = None
