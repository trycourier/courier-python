# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required, TypedDict

from .elemental_node import ElementalNode

__all__ = ["ElementalContent"]


class ElementalContent(TypedDict, total=False):
    elements: Required[Iterable[ElementalNode]]

    version: Required[str]
    """For example, "2022-01-01" """

    scope: Literal["default", "strict"]
    """How template variables read the data sent with the message.

    Under `strict`, data fields are read only through the `data.` prefix, as in
    `{{data.name}}`. Under `default`, `data` is spread onto the root, so `{{name}}`
    resolves and `{{data.name}}` renders as an empty string. Templates saved in
    Design Studio are `strict`. When omitted, the content is `default`. A write that
    replaces a template's content resets it to `default` unless the request sends
    `scope` again.
    """
