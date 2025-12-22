# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .ms_teams import MsTeams
from ..._models import BaseModel

__all__ = ["MsTeamsRecipient"]


class MsTeamsRecipient(BaseModel):
    """Send via Microsoft Teams"""

    ms_teams: MsTeams
