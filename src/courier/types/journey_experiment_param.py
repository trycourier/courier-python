# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .journey_experiment_variant_param import JourneyExperimentVariantParam

__all__ = ["JourneyExperimentParam"]


class JourneyExperimentParam(TypedDict, total=False):
    """A/B experiment config for a send node.

    The recipient is deterministically bucketed by `bucketingKey` and routed to one of the `variants` in proportion to its `weight`. Present on a send node INSTEAD OF `message.template`.
    """

    bucketing_key: Required[Annotated[str, PropertyInfo(alias="bucketingKey")]]
    """The value used to deterministically assign a recipient to a variant.

    Must be non-empty with no leading or trailing whitespace.
    """

    variants: Required[Iterable[JourneyExperimentVariantParam]]
    """Between 2 and 10 weighted template variants."""

    id: str
    """Unique experiment id (prefixed `exp_`).

    Omit to have one generated automatically; when supplied it must be a valid
    `exp_` id.
    """

    name: str
    """Optional display name for the experiment."""
