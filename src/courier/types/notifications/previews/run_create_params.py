# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["RunCreateParams"]


class RunCreateParams(TypedDict, total=False):
    data: Dict[str, object]
    """
    Template variables to render with, the same shape as the `data` object on a
    send.
    """

    device_ids: SequenceNotStr[str]
    """The devices to render on, by `PreviewDevice.id`, for a one-off run.

    Mutually exclusive with `device_set_id`.
    """

    device_set_id: str
    """A saved device set naming the devices to render on.

    Mutually exclusive with `device_ids`.
    """

    locale: str
    """Render the template's content for this locale, e.g. "fr-FR"."""

    template_version: str
    """Which version of the template to render.

    Omit for the latest saved draft, which always exists and is what the editor
    shows. `published` renders the live version; a zero-padded `v002` renders that
    specific publish. Versions are 1-based, so `v000` is not a version, and the
    unpadded `v2` is rejected — that spelling belongs to journeys'
    AutomationVersionId, a different scheme in which `v0` means published.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]

    x_idempotency_expiration: Annotated[str, PropertyInfo(alias="x-idempotency-expiration")]
