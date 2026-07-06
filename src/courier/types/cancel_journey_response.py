# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .._models import BaseModel

__all__ = ["CancelJourneyResponse", "TokenBranch", "RunIDBranch"]


class TokenBranch(BaseModel):
    cancelation_token: str


class RunIDBranch(BaseModel):
    run_id: str

    status: str
    """The run's resulting status.

    `CANCELED` when the run was active and has been canceled; `PROCESSED` or `ERROR`
    when the run had already finished and was left unchanged; `CANCELED` for an
    already-canceled run.
    """


CancelJourneyResponse: TypeAlias = Union[TokenBranch, RunIDBranch]
