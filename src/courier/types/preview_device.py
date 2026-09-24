# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["PreviewDevice"]


class PreviewDevice(BaseModel):
    """
    One mail app on one platform, operating system and theme that a preview can be rendered on. Reference data, identical for every workspace. Every field is always present; `platform` and `platform_version` are null where they do not apply.
    """

    id: str
    """
    The device's identifier, used in `device_ids` when creating a device set or a
    run.
    """

    app: str
    """The mail app.

    For webmail it is the service (`outlook_com`, `gmail_com`); for mobile the app
    (`apple_mail`, `gmail`); for desktop the app together with the version it is
    sold under (`outlook_2019`, `outlook_microsoft_365`, `apple_mail_16`), because
    that version is what separates one desktop Outlook from another.
    """

    category: Literal["webmail", "mobile", "desktop"]
    """Where the app runs."""

    name: str
    """Display name.

    Render it as-is rather than parsing it. It is also what separates the two
    120-dpi Outlook renders from their 100% siblings, which are otherwise identical
    field for field.
    """

    os: str
    """The operating system."""

    os_version: str
    """The operating system's version. Always set."""

    platform: Optional[str] = None
    """
    What the app runs on — the browser for webmail (`chrome`, `edge`, `firefox`),
    the phone for mobile (`iphone`, `pixel`). Null for desktop, where the app runs
    on nothing but the OS.
    """

    platform_version: Optional[str] = None
    """Which one of the platform — the phone model for mobile (`15_pro_max`, `10`).

    Null for webmail, which always renders in the current browser, and for desktop.
    """

    theme: Literal["light", "dark"]
    """Whether the email is rendered in light or dark mode."""
