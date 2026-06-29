# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["JourneyExperimentVariantParam"]


class JourneyExperimentVariantParam(TypedDict, total=False):
    """A single weighted arm of an experiment.

    Variant ids must be unique within the experiment and the sum of all variant weights must be greater than 0. Weights are relative (no sum-to-100 requirement) — routing normalizes them proportionally.
    """

    id: Required[str]

    template_id: Required[Annotated[str, PropertyInfo(alias="templateId")]]
    """The notification template sent for this variant."""

    weight: Required[float]
    """Relative routing weight. Must be non-negative."""

    name: str
    """Optional, cosmetic display name for the variant."""
