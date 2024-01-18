# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.remove_none_from_dict import remove_none_from_dict
from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.message_not_found_error import MessageNotFoundError
from ..commons.types.bad_request import BadRequest
from ..commons.types.message_not_found import MessageNotFound
from .types.list_messages_response import ListMessagesResponse
from .types.message_details import MessageDetails
from .types.message_history_response import MessageHistoryResponse
from .types.render_output_response import RenderOutputResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        archived: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        list: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        enqueued_after: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
    ) -> ListMessagesResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Parameters:
            - archived: typing.Optional[bool]. A boolean value that indicates whether archived messages should be included in the response.

            - cursor: typing.Optional[str]. A unique identifier that allows for fetching the next set of message statuses.

            - event: typing.Optional[str]. A unique identifier representing the event that was used to send the event.

            - list: typing.Optional[str]. A unique identifier representing the list the message was sent to.

            - message_id: typing.Optional[str]. A unique identifier representing the message_id returned from either /send or /send/list.

            - notification: typing.Optional[str]. A unique identifier representing the notification that was used to send the event.

            - recipient: typing.Optional[str]. A unique identifier representing the recipient associated with the requested profile.

            - status: typing.Optional[str]. An indicator of the current status of the message. Multiple status values can be passed in.

            - tags: typing.Optional[str]. A comma delimited list of 'tags'. Messages will be returned if they match any of the tags passed in.

            - enqueued_after: typing.Optional[str]. The enqueued datetime of a message to filter out messages received before.

            - trace_id: typing.Optional[str]. The unique identifier used to trace the requests
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "messages"),
            params=remove_none_from_dict(
                {
                    "archived": archived,
                    "cursor": cursor,
                    "event": event,
                    "list": list,
                    "messageId": message_id,
                    "notification": notification,
                    "recipient": recipient,
                    "status": status,
                    "tags": tags,
                    "enqueued_after": enqueued_after,
                    "traceId": trace_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListMessagesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, message_id: str) -> MessageDetails:
        """
        Fetch the status of a message you've previously sent.

        Parameters:
            - message_id: str. A unique identifier associated with the message you wish to retrieve (results from a send).
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageDetails, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def cancel(self, message_id: str) -> MessageDetails:
        """
        Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).

        Parameters:
            - message_id: str. A unique identifier representing the message ID
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/cancel"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageDetails, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_history(self, message_id: str, *, type: typing.Optional[str] = None) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Parameters:
            - message_id: str. A unique identifier representing the message ID

            - type: typing.Optional[str]. A supported Message History type that will filter the events returned.
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/history"),
            params=remove_none_from_dict({"type": type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageHistoryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_content(self, message_id: str) -> RenderOutputResponse:
        """
        Parameters:
            - message_id: str. A unique identifier associated with the message you wish to retrieve (results from a send).
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/output"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RenderOutputResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def archive(self, request_id: str) -> None:
        """
        Parameters:
            - request_id: str. A unique identifier representing the request ID
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"requests/{request_id}/archive"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncMessagesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        archived: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        list: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        recipient: typing.Optional[str] = None,
        status: typing.Optional[str] = None,
        tags: typing.Optional[str] = None,
        enqueued_after: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
    ) -> ListMessagesResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Parameters:
            - archived: typing.Optional[bool]. A boolean value that indicates whether archived messages should be included in the response.

            - cursor: typing.Optional[str]. A unique identifier that allows for fetching the next set of message statuses.

            - event: typing.Optional[str]. A unique identifier representing the event that was used to send the event.

            - list: typing.Optional[str]. A unique identifier representing the list the message was sent to.

            - message_id: typing.Optional[str]. A unique identifier representing the message_id returned from either /send or /send/list.

            - notification: typing.Optional[str]. A unique identifier representing the notification that was used to send the event.

            - recipient: typing.Optional[str]. A unique identifier representing the recipient associated with the requested profile.

            - status: typing.Optional[str]. An indicator of the current status of the message. Multiple status values can be passed in.

            - tags: typing.Optional[str]. A comma delimited list of 'tags'. Messages will be returned if they match any of the tags passed in.

            - enqueued_after: typing.Optional[str]. The enqueued datetime of a message to filter out messages received before.

            - trace_id: typing.Optional[str]. The unique identifier used to trace the requests
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "messages"),
            params=remove_none_from_dict(
                {
                    "archived": archived,
                    "cursor": cursor,
                    "event": event,
                    "list": list,
                    "messageId": message_id,
                    "notification": notification,
                    "recipient": recipient,
                    "status": status,
                    "tags": tags,
                    "enqueued_after": enqueued_after,
                    "traceId": trace_id,
                }
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ListMessagesResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, message_id: str) -> MessageDetails:
        """
        Fetch the status of a message you've previously sent.

        Parameters:
            - message_id: str. A unique identifier associated with the message you wish to retrieve (results from a send).
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageDetails, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def cancel(self, message_id: str) -> MessageDetails:
        """
        Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).

        Parameters:
            - message_id: str. A unique identifier representing the message ID
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/cancel"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageDetails, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_history(self, message_id: str, *, type: typing.Optional[str] = None) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Parameters:
            - message_id: str. A unique identifier representing the message ID

            - type: typing.Optional[str]. A supported Message History type that will filter the events returned.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/history"),
            params=remove_none_from_dict({"type": type}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(MessageHistoryResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_content(self, message_id: str) -> RenderOutputResponse:
        """
        Parameters:
            - message_id: str. A unique identifier associated with the message you wish to retrieve (results from a send).
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"messages/{message_id}/output"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(RenderOutputResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise MessageNotFoundError(pydantic.parse_obj_as(MessageNotFound, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def archive(self, request_id: str) -> None:
        """
        Parameters:
            - request_id: str. A unique identifier representing the request ID
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"requests/{request_id}/archive"),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
