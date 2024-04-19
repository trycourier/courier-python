# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

from ...core.pydantic_utilities import pydantic_v1
from .i_action_button_style import IActionButtonStyle
from .i_alignment import IAlignment
from .locales import Locales
from .text_align import TextAlign
from .text_style import TextStyle


class ElementalNode_Text(pydantic_v1.BaseModel):
    type: typing.Literal["text"] = "text"
    content: str = pydantic_v1.Field()
    """
    The text content displayed in the notification. Either this
    field must be specified, or the elements field
    """

    align: TextAlign = pydantic_v1.Field()
    """
    Text alignment.
    """

    text_style: typing.Optional[TextStyle] = pydantic_v1.Field()
    """
    Allows the text to be rendered as a heading level.
    """

    color: typing.Optional[str] = pydantic_v1.Field()
    """
    Specifies the color of text. Can be any valid css color value
    """

    bold: typing.Optional[str] = pydantic_v1.Field()
    """
    Apply bold to the text
    """

    italic: typing.Optional[str] = pydantic_v1.Field()
    """
    Apply italics to the text
    """

    strikethrough: typing.Optional[str] = pydantic_v1.Field()
    """
    Apply a strike through the text
    """

    underline: typing.Optional[str] = pydantic_v1.Field()
    """
    Apply an underline to the text
    """

    locales: typing.Optional[Locales] = pydantic_v1.Field()
    """
    Region specific content. See [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/) for more details.
    """

    format: typing.Optional[typing.Literal["markdown"]]
    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Meta(pydantic_v1.BaseModel):
    type: typing.Literal["meta"] = "meta"
    title: typing.Optional[str] = pydantic_v1.Field()
    """
    The title to be displayed by supported channels. For example, the email subject.
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Channel(pydantic_v1.BaseModel):
    type: typing.Literal["channel"] = "channel"
    channel: str = pydantic_v1.Field()
    """
    The channel the contents of this element should be applied to. Can be `email`,
    `push`, `direct_message`, `sms` or a provider such as slack
    """

    elements: typing.Optional[typing.List[ElementalNode]] = pydantic_v1.Field()
    """
    An array of elements to apply to the channel. If `raw` has not been
    specified, `elements` is `required`.
    """

    raw: typing.Optional[typing.Dict[str, typing.Any]] = pydantic_v1.Field()
    """
    Raw data to apply to the channel. If `elements` has not been
    specified, `raw` is `required`.
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Image(pydantic_v1.BaseModel):
    type: typing.Literal["image"] = "image"
    src: str = pydantic_v1.Field()
    """
    The source of the image.
    """

    href: typing.Optional[str] = pydantic_v1.Field()
    """
    A URL to link to when the image is clicked.
    """

    align: typing.Optional[IAlignment] = pydantic_v1.Field()
    """
    The alignment of the image.
    """

    alt_text: typing.Optional[str] = pydantic_v1.Field(alias="altText")
    """
    Alternate text for the image.
    """

    width: typing.Optional[str] = pydantic_v1.Field()
    """
    CSS width properties to apply to the image. For example, 50px
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Action(pydantic_v1.BaseModel):
    type: typing.Literal["action"] = "action"
    content: str = pydantic_v1.Field()
    """
    The text content of the action shown to the user.
    """

    href: str = pydantic_v1.Field()
    """
    The target URL of the action.
    """

    action_id: typing.Optional[str] = pydantic_v1.Field()
    """
    A unique id used to identify the action when it is executed.
    """

    align: typing.Optional[IAlignment] = pydantic_v1.Field()
    """
    The alignment of the action button. Defaults to "center".
    """

    background_color: typing.Optional[str] = pydantic_v1.Field()
    """
    The background color of the action button.
    """

    style: typing.Optional[IActionButtonStyle] = pydantic_v1.Field()
    """
    Defaults to `button`.
    """

    locales: Locales = pydantic_v1.Field()
    """
    Region specific content. See [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/) for more details.
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Divider(pydantic_v1.BaseModel):
    type: typing.Literal["divider"] = "divider"
    color: typing.Optional[str] = pydantic_v1.Field()
    """
    The CSS color to render the line with. For example, `#fff`
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Group(pydantic_v1.BaseModel):
    type: typing.Literal["group"] = "group"
    elements: typing.List[ElementalNode] = pydantic_v1.Field()
    """
    Sub elements to render.
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


class ElementalNode_Quote(pydantic_v1.BaseModel):
    type: typing.Literal["quote"] = "quote"
    content: str = pydantic_v1.Field()
    """
    The text value of the quote.
    """

    align: typing.Optional[IAlignment] = pydantic_v1.Field()
    """
    Alignment of the quote.
    """

    border_color: typing.Optional[str] = pydantic_v1.Field(alias="borderColor")
    """
    CSS border color property. For example, `#fff`
    """

    text_style: TextStyle
    locales: Locales = pydantic_v1.Field()
    """
    Region specific content. See [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/) for more details.
    """

    channels: typing.Optional[typing.List[str]]
    ref: typing.Optional[str]
    if_: typing.Optional[str] = pydantic_v1.Field(alias="if")
    loop: typing.Optional[str]

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        populate_by_name = True


ElementalNode = typing.Union[
    ElementalNode_Text,
    ElementalNode_Meta,
    ElementalNode_Channel,
    ElementalNode_Image,
    ElementalNode_Action,
    ElementalNode_Divider,
    ElementalNode_Group,
    ElementalNode_Quote,
]
