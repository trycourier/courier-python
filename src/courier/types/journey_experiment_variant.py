# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["JourneyExperimentVariant"]


class JourneyExperimentVariant(BaseModel):
    """A single weighted variant of an experiment.

    Variant ids must be unique within the experiment and the sum of all variant weights must be greater than 0. Weights are relative (no sum-to-100 requirement) — routing normalizes them proportionally.
    """

    id: str

    template_id: str = FieldInfo(alias="templateId")
    """The notification template sent for this variant."""

    weight: float
    """Relative routing weight. Must be non-negative."""

    name: Optional[str] = None
    """Optional display name for the variant."""
