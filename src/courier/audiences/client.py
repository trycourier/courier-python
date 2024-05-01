# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ..commons.errors.bad_request_error import BadRequestError
from ..commons.types.bad_request import BadRequest
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.pydantic_utilities import pydantic_v1
from ..core.remove_none_from_dict import remove_none_from_dict
from ..core.request_options import RequestOptions
from .types.audience import Audience
from .types.audience_list_response import AudienceListResponse
from .types.audience_member_list_response import AudienceMemberListResponse
from .types.audience_update_response import AudienceUpdateResponse
from .types.filter import Filter

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class AudiencesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, audience_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Audience:
        """
        Returns the specified audience by id.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Audience

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audiences.get(
            audience_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic_v1.parse_obj_as(Audience, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        audience_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudienceUpdateResponse:
        """
        Creates or updates audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

        name : typing.Optional[str]
            The name of the audience

        description : typing.Optional[str]
            A description of the audience

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceUpdateResponse

        Examples
        --------
        from courier import SingleFilterConfig
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audiences.update(
            audience_id="string",
            name="string",
            description="string",
            filter=SingleFilterConfig(
                value="string",
                path="string",
                operator="ENDS_WITH",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if name is not OMIT:
            _request["name"] = name
        if description is not OMIT:
            _request["description"] = description
        if filter is not OMIT:
            _request["filter"] = filter
        _response = self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(AudienceUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, audience_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the specified audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

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
        client.audiences.delete(
            audience_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_members(
        self,
        audience_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudienceMemberListResponse:
        """
        Get list of members of an audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of members

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceMemberListResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audiences.list_members(
            audience_id="string",
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}/members"
            ),
            params=jsonable_encoder(
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
            return pydantic_v1.parse_obj_as(AudienceMemberListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list_audiences(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AudienceListResponse:
        """
        Get the audiences associated with the authorization token.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of audiences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceListResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.audiences.list_audiences(
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "audiences"),
            params=jsonable_encoder(
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
            return pydantic_v1.parse_obj_as(AudienceListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncAudiencesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, audience_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Audience:
        """
        Returns the specified audience by id.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience_id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Audience

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audiences.get(
            audience_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return pydantic_v1.parse_obj_as(Audience, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        audience_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        description: typing.Optional[str] = OMIT,
        filter: typing.Optional[Filter] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudienceUpdateResponse:
        """
        Creates or updates audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

        name : typing.Optional[str]
            The name of the audience

        description : typing.Optional[str]
            A description of the audience

        filter : typing.Optional[Filter]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceUpdateResponse

        Examples
        --------
        from courier import SingleFilterConfig
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audiences.update(
            audience_id="string",
            name="string",
            description="string",
            filter=SingleFilterConfig(
                value="string",
                path="string",
                operator="ENDS_WITH",
            ),
        )
        """
        _request: typing.Dict[str, typing.Any] = {}
        if name is not OMIT:
            _request["name"] = name
        if description is not OMIT:
            _request["description"] = description
        if filter is not OMIT:
            _request["filter"] = filter
        _response = await self._client_wrapper.httpx_client.request(
            method="PUT",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(_request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(_request),
                **(jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))),
            },
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
            return pydantic_v1.parse_obj_as(AudienceUpdateResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, audience_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the specified audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audiences.delete(
            audience_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="DELETE",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
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
            return
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_members(
        self,
        audience_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AudienceMemberListResponse:
        """
        Get list of members of an audience.

        Parameters
        ----------
        audience_id : str
            A unique identifier representing the audience id

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of members

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceMemberListResponse

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audiences.list_members(
            audience_id="string",
            cursor="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"audiences/{jsonable_encoder(audience_id)}/members"
            ),
            params=jsonable_encoder(
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
            return pydantic_v1.parse_obj_as(AudienceMemberListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list_audiences(
        self, *, cursor: typing.Optional[str] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> AudienceListResponse:
        """
        Get the audiences associated with the authorization token.

        Parameters
        ----------
        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of audiences

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AudienceListResponse

        Examples
        --------
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.audiences.list_audiences(
            cursor="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            method="GET",
            url=urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "audiences"),
            params=jsonable_encoder(
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
            return pydantic_v1.parse_obj_as(AudienceListResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
