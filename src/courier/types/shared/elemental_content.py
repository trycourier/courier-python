# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel
from .elemental_node import ElementalNode

__all__ = ["ElementalContent"]


class ElementalContent(BaseModel):
    elements: List[ElementalNode]

    version: str
    """For example, "2022-01-01" """

    scope: Optional[Literal["default", "strict"]] = None
    """How template variables read the data sent with the message.

    Under `strict`, data fields are read only through the `data.` prefix, as in
    `{{data.name}}`. Under `default`, `data` is spread onto the root, so `{{name}}`
    resolves and `{{data.name}}` renders as an empty string. Templates saved in
    Design Studio are `strict`. When omitted, the content is `default`. A write that
    replaces a template's content resets it to `default` unless the request sends
    `scope` again.
    """
