# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

from .shared_params.elemental_node import ElementalNode

__all__ = ["NotificationTemplateContentParam"]


class NotificationTemplateContentParam(TypedDict, total=False):
    """Elemental content of a notification template.

    Template variables read the data sent with the message through the `data.` prefix, as in `{{data.name}}`, and the recipient's profile through `profile.`.
    """

    elements: Required[Iterable[ElementalNode]]

    version: Required[str]
    """For example, "2022-01-01" """
