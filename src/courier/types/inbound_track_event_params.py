# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["InboundTrackEventParams"]


class InboundTrackEventParams(TypedDict, total=False):
    event: Required[str]
    """A descriptive name of the event.

    This name will appear as a trigger in the Courier Automation Trigger node.
    """

    message_id: Required[Annotated[str, PropertyInfo(alias="messageId")]]
    """A required unique identifier that will be used to de-duplicate requests.

    If not unique, will respond with 409 Conflict status
    """

    properties: Required[Dict[str, object]]

    type: Required[Literal["track"]]

    user_id: Annotated[Optional[str], PropertyInfo(alias="userId")]
    """The user id associatiated with the track"""
