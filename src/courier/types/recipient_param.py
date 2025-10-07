# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypeAlias

from .shared_params.list_recipient import ListRecipient
from .shared_params.user_recipient import UserRecipient

__all__ = ["RecipientParam"]

RecipientParam: TypeAlias = Union[UserRecipient, ListRecipient]
