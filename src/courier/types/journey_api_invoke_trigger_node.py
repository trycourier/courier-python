# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .journey_conditions_field import JourneyConditionsField

__all__ = ["JourneyAPIInvokeTriggerNode"]


class JourneyAPIInvokeTriggerNode(BaseModel):
    trigger_type: Literal["api-invoke"]

    type: Literal["trigger"]

    id: Optional[str] = None

    conditions: Optional[JourneyConditionsField] = None
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""
