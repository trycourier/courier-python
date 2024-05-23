# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .automation_add_to_batch_max_items_type import AutomationAddToBatchMaxItemsType
from .automation_add_to_batch_retain import AutomationAddToBatchRetain
from .automation_add_to_batch_scope import AutomationAddToBatchScope
from .automation_step import AutomationStep


class AutomationAddToBatchStep(AutomationStep):
    """
    Examples
    --------
    from courier import AutomationAddToBatchRetain, AutomationAddToBatchStep

    AutomationAddToBatchStep(
        action="add-to-batch",
        wait_period="PT5M",
        max_wait_period="PT1H",
        retain=AutomationAddToBatchRetain(
            type="highest",
            count=10,
            sort_key="refs.data.my_custom_scoring",
        ),
        scope="user",
        category_key="refs.data.status",
    )
    """

    action: typing.Literal["add-to-batch"]
    wait_period: str = pydantic_v1.Field()
    """
    Defines the period of inactivity before the batch is released. Specified as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    """

    max_wait_period: str = pydantic_v1.Field()
    """
    Defines the maximum wait time before the batch should be released. Must be less than wait period. Maximum of 60 days. Specified as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations)
    """

    max_items: typing.Optional[AutomationAddToBatchMaxItemsType] = pydantic_v1.Field(default=None)
    """
    If specified, the batch will release as soon as this number is reached
    """

    retain: AutomationAddToBatchRetain
    scope: typing.Optional[AutomationAddToBatchScope] = pydantic_v1.Field(default=None)
    """
    Determine the scope of the batching. If user, chosen in this order: recipient, profile.user_id, data.user_id, data.userId.
    If dynamic, then specify where the batch_key or a reference to the batch_key
    """

    batch_key: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    If using scope=dynamic, provide the key or a reference (e.g., refs.data.batch_key)
    """

    batch_id: typing.Optional[str] = None
    category_key: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Defines the field of the data object the batch is set to when complete. Defaults to `batch`
    """

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults_exclude_unset: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        kwargs_with_defaults_exclude_none: typing.Any = {"by_alias": True, "exclude_none": True, **kwargs}

        return deep_union_pydantic_dicts(
            super().dict(**kwargs_with_defaults_exclude_unset), super().dict(**kwargs_with_defaults_exclude_none)
        )

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True
        extra = pydantic_v1.Extra.allow
        json_encoders = {dt.datetime: serialize_datetime}
