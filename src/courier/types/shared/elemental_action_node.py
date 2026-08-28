# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .locales import Locales
from .alignment import Alignment
from .elemental_base_node import ElementalBaseNode

__all__ = ["ElementalActionNode"]


class ElementalActionNode(ElementalBaseNode):
    """Allows the user to execute an action. Can be a button or a link."""

    content: str
    """The text content of the action shown to the user."""

    href: str
    """The target URL of the action."""

    action_id: Optional[str] = None
    """A unique id used to identify the action when it is executed."""

    align: Optional[Alignment] = None
    """The alignment of the action button. Defaults to "center"."""

    background_color: Optional[str] = None
    """The background color of the action button."""

    border_radius: Optional[str] = None
    """CSS border-radius applied to the action button. For example, `4px`"""

    border_size: Optional[str] = None
    """CSS border width applied to the action button. For example, `1px`"""

    disable_tracking: Optional[bool] = None
    """
    When true, the action's href is not rewritten for click-through tracking, even
    when click-through tracking is enabled for the workspace.
    """

    font_size: Optional[str] = None
    """CSS font-size applied to the action button label. For example, `14px`"""

    locales: Optional[Locales] = None
    """Region specific content.

    See
    [locales docs](https://www.courier.com/docs/platform/content/elemental/locales/)
    for more details.
    """

    padding: Optional[str] = None
    """CSS padding applied to the action button. For example, `8px 16px`"""

    style: Optional[Literal["button", "link"]] = None
    """Defaults to `button`."""
