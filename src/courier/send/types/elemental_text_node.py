# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ...core.datetime_utils import serialize_datetime
from ...core.pydantic_utilities import deep_union_pydantic_dicts, pydantic_v1
from .elemental_base_node import ElementalBaseNode
from .locales import Locales
from .text_align import TextAlign
from .text_style import TextStyle


class ElementalTextNode(ElementalBaseNode):
    """
    Represents a body of text to be rendered inside of the notification.
    """

    content: str = pydantic_v1.Field()
    """
    The text content displayed in the notification. Either this
    field must be specified, or the elements field
    """

    align: TextAlign = pydantic_v1.Field()
    """
    Text alignment.
    """

    text_style: typing.Optional[TextStyle] = pydantic_v1.Field(default=None)
    """
    Allows the text to be rendered as a heading level.
    """

    color: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Specifies the color of text. Can be any valid css color value
    """

    bold: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Apply bold to the text
    """

    italic: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Apply italics to the text
    """

    strikethrough: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Apply a strike through the text
    """

    underline: typing.Optional[str] = pydantic_v1.Field(default=None)
    """
    Apply an underline to the text
    """

    locales: typing.Optional[Locales] = pydantic_v1.Field(default=None)
    """
    Region specific content. See [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/) for more details.
    """

    format: typing.Optional[typing.Literal["markdown"]] = None

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
