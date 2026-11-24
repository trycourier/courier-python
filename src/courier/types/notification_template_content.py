# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel
from .shared.elemental_node import ElementalNode

__all__ = ["NotificationTemplateContent"]


class NotificationTemplateContent(BaseModel):
    """Elemental content of a notification template.

    Template variables read the data sent with the message through the `data.` prefix, as in `{{data.name}}`, and the recipient's profile through `profile.`.
    """

    elements: List[ElementalNode]

    version: str
    """For example, "2022-01-01" """
