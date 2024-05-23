# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.query_encoder import encode_query
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from .types.audit_event import AuditEvent
from .types.list_audit_events_response import ListAuditEventsResponse


class AuditEventsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAuditEventsResponse:
        """
        Fetch the list of audit events

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of audit events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAuditEventsResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audit_events.list_(
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "audit-events"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "cursor": cursor,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(ListAuditEventsResponse, construct_type(type_=ListAuditEventsResponse, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, audit_event_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AuditEvent:
        """
        Fetch a specific audit event by ID.

        Parameters
        ----------
        audit_event_id : str
            A unique identifier associated with the audit event you wish to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuditEvent

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audit_events.get(
            audit_event_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audit-events/{jsonable_encoder(audit_event_id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(AuditEvent, construct_type(type_=AuditEvent, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAuditEventsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> ListAuditEventsResponse:
        """
        Fetch the list of audit events

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of audit events.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListAuditEventsResponse

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audit_events.list_(
            cursor="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "audit-events"),
            params=encode_query(
                jsonable_encoder(
                    remove_none_from_dict(
                        {
                            "cursor": cursor,
                            **(
                                request_options.get("additional_query_parameters", {})
                                if request_options is not None
                                else {}
                            ),
                        }
                    )
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(ListAuditEventsResponse, construct_type(type_=ListAuditEventsResponse, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, audit_event_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> AuditEvent:
        """
        Fetch a specific audit event by ID.

        Parameters
        ----------
        audit_event_id : str
            A unique identifier associated with the audit event you wish to retrieve

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AuditEvent

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audit_events.get(
            audit_event_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audit-events/{jsonable_encoder(audit_event_id)}"
            ),
            params=encode_query(
                jsonable_encoder(
                    request_options.get("additional_query_parameters") if request_options is not None else None
                )
            ),
            headers=jsonable_encoder(
                remove_none_from_dict(
                    {
                        **self._client_wrapper.get_headers(),
                        **(request_options.get("additional_headers", {}) if request_options is not None else {}),
                    }
                )
            ),
            timeout=request_options.get("timeout_in_seconds")
            if request_options is not None and request_options.get("timeout_in_seconds") is not None
            else self._client_wrapper.get_timeout(),
            retries=0,
            max_retries=request_options.get("max_retries") if request_options is not None else 0,  # type: ignore
        )
        if 200 <= _response.status_code < 300:
            return typing.cast(AuditEvent, construct_type(type_=AuditEvent, object_=_response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
