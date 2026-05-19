# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyAPIInvokeTriggerNodeParam"]


class JourneyAPIInvokeTriggerNodeParam(TypedDict, total=False):
    """Trigger fired when the journey is invoked via the API.

    The optional `schema` field is a JSON Schema that validates the invocation payload.
    """

    trigger_type: Required[Literal["api-invoke"]]

    type: Required[Literal["trigger"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    schema: Dict[str, object]
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""
