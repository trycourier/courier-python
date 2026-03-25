# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationRetrieveParams"]


class NotificationRetrieveParams(TypedDict, total=False):
    version: str
    """Version to retrieve.

    One of "draft", "published", or a version string like "v001". Defaults to
    "published".
    """
