# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .message_details import MessageDetails

__all__ = ["MessageRetrieveResponse"]


class MessageRetrieveResponse(MessageDetails):
    providers: Optional[List[Dict[str, object]]] = None
