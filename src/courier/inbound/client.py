# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..commons.errors.bad_request_error import BadRequestError
from ..commons.errors.conflict_error import ConflictError
from ..commons.types.bad_request import BadRequest
from ..commons.types.conflict import Conflict
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from .types.inbound_track_event import InboundTrackEvent
from .types.track_accepted_response import TrackAcceptedResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InboundClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def track(
        self, *, request: InboundTrackEvent, request_options: typing.Optional[RequestOptions] = None
    ) -> TrackAcceptedResponse:
        """
        Parameters
        ----------
        request : InboundTrackEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackAcceptedResponse

        Examples
        --------
        from courier import InboundTrackEvent
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.inbound.track(
            request=InboundTrackEvent(
                event="New Order Placed",
                message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
                user_id="1234",
                properties={"order_id": 123, "total_orders": 5, "last_order_id": 122},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "inbound/courier", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(TrackAcceptedResponse, construct_type(type_=TrackAcceptedResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(Conflict, construct_type(type_=Conflict, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInboundClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def track(
        self, *, request: InboundTrackEvent, request_options: typing.Optional[RequestOptions] = None
    ) -> TrackAcceptedResponse:
        """
        Parameters
        ----------
        request : InboundTrackEvent

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrackAcceptedResponse

        Examples
        --------
        import asyncio

        from courier import InboundTrackEvent
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.inbound.track(
                request=InboundTrackEvent(
                    event="New Order Placed",
                    message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
                    user_id="1234",
                    properties={
                        "order_id": 123,
                        "total_orders": 5,
                        "last_order_id": 122,
                    },
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "inbound/courier", method="POST", json=request, request_options=request_options, omit=OMIT
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(TrackAcceptedResponse, construct_type(type_=TrackAcceptedResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            if _response.status_code == 409:
                raise ConflictError(
                    typing.cast(Conflict, construct_type(type_=Conflict, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)