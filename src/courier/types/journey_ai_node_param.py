# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, TypedDict

from .journey_conditions_field_param import JourneyConditionsFieldParam

__all__ = ["JourneyAINodeParam"]


class JourneyAINodeParam(TypedDict, total=False):
    """Invoke an AI step with `user_prompt` and optional `web_search`.

    Returns a structured response conforming to `output_schema`.
    """

    output_schema: Required[Dict[str, object]]
    """A JSONSchema object (Draft-07-compatible). Validated at runtime by Ajv."""

    type: Required[Literal["ai"]]

    id: str

    conditions: JourneyConditionsFieldParam
    """Condition spec for a journey node.

    Accepts a single condition atom, an AND/OR group, or an AND/OR nested group.
    Omit the `conditions` property entirely to express "no conditions".
    """

    model: str
    """A supported AI model id.

    Requests with an unknown id may be rejected with a 400 that lists the supported
    ids. Supported ids: `claude-fable-5-1`, `claude-opus-5-5`, `claude-sonnet-5-5`,
    `claude-haiku-5-5`, `gpt-6-astra`, `gpt-5.5`, `gpt-5.4`, `gpt-6.1-sol`,
    `gpt-6.1-terra`, `gpt-5.4-mini`, `gpt-5.4-nano`, `gpt-6-luna`.
    """

    user_prompt: str

    web_search: bool
