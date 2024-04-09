# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import pydantic_v1
from .automation_fetch_data_webhook import AutomationFetchDataWebhook
from .automation_step import AutomationStep
from .merge_algorithm import MergeAlgorithm


class AutomationFetchDataStep(AutomationStep):
    """
    from courier import AutomationFetchDataStep, AutomationFetchDataWebhook

    AutomationFetchDataStep(
        action="fetch-data",
        merge_strategy="none",
        webhook=AutomationFetchDataWebhook(
            body={"foo": "bar"},
            params={"hello": "world"},
            headers={"content-type": "application/json"},
            method="POST",
            url="https://bryan-at-courier.free.beeceptor.com",
        ),
    )
    """

    action: typing.Literal["fetch-data"]
    webhook: AutomationFetchDataWebhook
    merge_strategy: MergeAlgorithm
    idempotency_expiry: typing.Optional[str] = None
    idempotency_key: typing.Optional[str] = None

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
