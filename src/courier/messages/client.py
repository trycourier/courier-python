# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.message_not_found_error import MessageNotFoundError
from ..commons.types.bad_request import BadRequest
from ..commons.types.message_not_found import MessageNotFound
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from .types.list_messages_response import ListMessagesResponse
from .types.message_details import MessageDetails
from .types.message_history_response import MessageHistoryResponse
from .types.render_output_response import RenderOutputResponse


class MessagesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        archived: typing.Optional[bool] = None,
        cursor: typing.Optional[str] = None,
        event: typing.Optional[str] = None,
        list_: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        provider: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        recipient: typing.Optional[str] = None,
        status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tags: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        enqueued_after: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMessagesResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Parameters
        ----------
        archived : typing.Optional[bool]
            A boolean value that indicates whether archived messages should be included in the response.

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of messages.

        event : typing.Optional[str]
            A unique identifier representing the event that was used to send the event.

        list_ : typing.Optional[str]
            A unique identifier representing the list the message was sent to.

        message_id : typing.Optional[str]
            A unique identifier representing the message_id returned from either /send or /send/list.

        notification : typing.Optional[str]
            A unique identifier representing the notification that was used to send the event.

        provider : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The key assocated to the provider you want to filter on. E.g., sendgrid, inbox, twilio, slack, msteams, etc. Allows multiple values to be set in query parameters.

        recipient : typing.Optional[str]
            A unique identifier representing the recipient associated with the requested profile.

        status : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            An indicator of the current status of the message. Allows multiple values to be set in query parameters.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A tag placed in the metadata.tags during a notification send. Allows multiple values to be set in query parameters.

        tags : typing.Optional[str]
            A comma delimited list of 'tags'. Messages will be returned if they match any of the tags passed in.

        tenant_id : typing.Optional[str]
            Messages sent with the context of a Tenant

        enqueued_after : typing.Optional[str]
            The enqueued datetime of a message to filter out messages received before.

        trace_id : typing.Optional[str]
            The unique identifier used to trace the requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMessagesResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.list(
            archived=True,
            cursor="string",
            event="string",
            list_="string",
            message_id="string",
            notification="string",
            provider="string",
            recipient="string",
            status="string",
            tag="string",
            tags="string",
            tenant_id="string",
            enqueued_after="string",
            trace_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "messages",
            method="GET",
            params={
                "archived": archived,
                "cursor": cursor,
                "event": event,
                "list": list_,
                "messageId": message_id,
                "notification": notification,
                "provider": provider,
                "recipient": recipient,
                "status": status,
                "tag": tag,
                "tags": tags,
                "tenant_id": tenant_id,
                "enqueued_after": enqueued_after,
                "traceId": trace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ListMessagesResponse, construct_type(type_=ListMessagesResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> MessageDetails:
        """
        Fetch the status of a message you've previously sent.

        Parameters
        ----------
        message_id : str
            A unique identifier associated with the message you wish to retrieve (results from a send).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageDetails

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.get(
            message_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageDetails, construct_type(type_=MessageDetails, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def cancel(
        self,
        message_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageDetails:
        """
        Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).

        Parameters
        ----------
        message_id : str
            A unique identifier representing the message ID

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageDetails

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.cancel(
            message_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/cancel",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageDetails, construct_type(type_=MessageDetails, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_history(
        self,
        message_id: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Parameters
        ----------
        message_id : str
            A unique identifier representing the message ID

        type : typing.Optional[str]
            A supported Message History type that will filter the events returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageHistoryResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.get_history(
            message_id="string",
            type="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/history",
            method="GET",
            params={"type": type},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageHistoryResponse, construct_type(type_=MessageHistoryResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_content(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RenderOutputResponse:
        """
        Parameters
        ----------
        message_id : str
            A unique identifier associated with the message you wish to retrieve (results from a send).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RenderOutputResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.get_content(
            message_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/output", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RenderOutputResponse, construct_type(type_=RenderOutputResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def archive(self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_id : str
            A unique identifier representing the request ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.messages.archive(
            request_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"requests/{jsonable_encoder(request_id)}/archive", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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
        list_: typing.Optional[str] = None,
        message_id: typing.Optional[str] = None,
        notification: typing.Optional[str] = None,
        provider: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        recipient: typing.Optional[str] = None,
        status: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tag: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        tags: typing.Optional[str] = None,
        tenant_id: typing.Optional[str] = None,
        enqueued_after: typing.Optional[str] = None,
        trace_id: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListMessagesResponse:
        """
        Fetch the statuses of messages you've previously sent.

        Parameters
        ----------
        archived : typing.Optional[bool]
            A boolean value that indicates whether archived messages should be included in the response.

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of messages.

        event : typing.Optional[str]
            A unique identifier representing the event that was used to send the event.

        list_ : typing.Optional[str]
            A unique identifier representing the list the message was sent to.

        message_id : typing.Optional[str]
            A unique identifier representing the message_id returned from either /send or /send/list.

        notification : typing.Optional[str]
            A unique identifier representing the notification that was used to send the event.

        provider : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            The key assocated to the provider you want to filter on. E.g., sendgrid, inbox, twilio, slack, msteams, etc. Allows multiple values to be set in query parameters.

        recipient : typing.Optional[str]
            A unique identifier representing the recipient associated with the requested profile.

        status : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            An indicator of the current status of the message. Allows multiple values to be set in query parameters.

        tag : typing.Optional[typing.Union[str, typing.Sequence[str]]]
            A tag placed in the metadata.tags during a notification send. Allows multiple values to be set in query parameters.

        tags : typing.Optional[str]
            A comma delimited list of 'tags'. Messages will be returned if they match any of the tags passed in.

        tenant_id : typing.Optional[str]
            Messages sent with the context of a Tenant

        enqueued_after : typing.Optional[str]
            The enqueued datetime of a message to filter out messages received before.

        trace_id : typing.Optional[str]
            The unique identifier used to trace the requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListMessagesResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.list(
                archived=True,
                cursor="string",
                event="string",
                list_="string",
                message_id="string",
                notification="string",
                provider="string",
                recipient="string",
                status="string",
                tag="string",
                tags="string",
                tenant_id="string",
                enqueued_after="string",
                trace_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "messages",
            method="GET",
            params={
                "archived": archived,
                "cursor": cursor,
                "event": event,
                "list": list_,
                "messageId": message_id,
                "notification": notification,
                "provider": provider,
                "recipient": recipient,
                "status": status,
                "tag": tag,
                "tags": tags,
                "tenant_id": tenant_id,
                "enqueued_after": enqueued_after,
                "traceId": trace_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ListMessagesResponse, construct_type(type_=ListMessagesResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> MessageDetails:
        """
        Fetch the status of a message you've previously sent.

        Parameters
        ----------
        message_id : str
            A unique identifier associated with the message you wish to retrieve (results from a send).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageDetails

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.get(
                message_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageDetails, construct_type(type_=MessageDetails, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def cancel(
        self,
        message_id: str,
        *,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageDetails:
        """
        Cancel a message that is currently in the process of being delivered. A well-formatted API call to the cancel message API will return either `200` status code for a successful cancellation or `409` status code for an unsuccessful cancellation. Both cases will include the actual message record in the response body (see details below).

        Parameters
        ----------
        message_id : str
            A unique identifier representing the message ID

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageDetails

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.cancel(
                message_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/cancel",
            method="POST",
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageDetails, construct_type(type_=MessageDetails, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_history(
        self,
        message_id: str,
        *,
        type: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MessageHistoryResponse:
        """
        Fetch the array of events of a message you've previously sent.

        Parameters
        ----------
        message_id : str
            A unique identifier representing the message ID

        type : typing.Optional[str]
            A supported Message History type that will filter the events returned.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MessageHistoryResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.get_history(
                message_id="string",
                type="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/history",
            method="GET",
            params={"type": type},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MessageHistoryResponse, construct_type(type_=MessageHistoryResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_content(
        self, message_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> RenderOutputResponse:
        """
        Parameters
        ----------
        message_id : str
            A unique identifier associated with the message you wish to retrieve (results from a send).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RenderOutputResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.get_content(
                message_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"messages/{jsonable_encoder(message_id)}/output", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(RenderOutputResponse, construct_type(type_=RenderOutputResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 404:
                raise MessageNotFoundError(
                    typing.cast(MessageNotFound, construct_type(type_=MessageNotFound, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def archive(self, request_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Parameters
        ----------
        request_id : str
            A unique identifier representing the request ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.messages.archive(
                request_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"requests/{jsonable_encoder(request_id)}/archive", method="PUT", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
