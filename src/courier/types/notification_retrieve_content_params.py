# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NotificationRetrieveContentParams"]


class NotificationRetrieveContentParams(TypedDict, total=False):
    version: str
    """Accepts `draft`, `published`, or a version string (e.g., `v001`).

    Defaults to `published`.
    """
