# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...commons.errors.bad_request_error import BadRequestError
from ...commons.types.bad_request import BadRequest
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from .types.get_all_tokens_response import GetAllTokensResponse
from .types.get_user_token_response import GetUserTokenResponse
from .types.patch_user_token_opts import PatchUserTokenOpts
from .types.user_token import UserToken

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TokensClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_multiple(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Adds multiple tokens to a user and overwrites matching existing tokens.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tokens.add_multiple(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tokens"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
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
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add(
        self, user_id: str, token: str, *, request: UserToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a single token to a user and overwrites a matching existing token.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request: UserToken.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier
        from courier.users import Device, Tracking, UserToken

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tokens.add(
            user_id="string",
            token="string",
            request=UserToken(
                token="string",
                provider_key="firebase-fcm",
                expiry_date="string",
                properties={"key": "value"},
                device=Device(
                    app_id="string",
                    ad_id="string",
                    device_id="string",
                    platform="string",
                    manufacturer="string",
                    model="string",
                ),
                tracking=Tracking(
                    os_version="string",
                    ip="string",
                    lat="string",
                    long_="string",
                ),
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        user_id: str,
        token: str,
        *,
        request: PatchUserTokenOpts,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Apply a JSON Patch (RFC 6902) to the specified token.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request: PatchUserTokenOpts.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier
        from courier.users import PatchOperation, PatchUserTokenOpts

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tokens.update(
            user_id="string",
            token="string",
            request=PatchUserTokenOpts(
                patch=[PatchOperation()],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(
        self, user_id: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserTokenResponse:
        """
        Get single token available for a `:token`

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tokens.get(
            user_id="string",
            token="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
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
            return pydantic_v1.parse_obj_as(GetUserTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def list(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> GetAllTokensResponse:
        """
        Gets all tokens available for a :user_id

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tokens.list(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tokens"
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
            return pydantic_v1.parse_obj_as(GetAllTokensResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTokensClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_multiple(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Adds multiple tokens to a user and overwrites matching existing tokens.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tokens.add_multiple(
            user_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tokens"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(remove_none_from_dict(request_options.get("additional_body_parameters", {})))
            if request_options is not None
            else None,
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
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add(
        self, user_id: str, token: str, *, request: UserToken, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Adds a single token to a user and overwrites a matching existing token.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request: UserToken.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier
        from courier.users import Device, Tracking, UserToken

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tokens.add(
            user_id="string",
            token="string",
            request=UserToken(
                token="string",
                provider_key="firebase-fcm",
                expiry_date="string",
                properties={"key": "value"},
                device=Device(
                    app_id="string",
                    ad_id="string",
                    device_id="string",
                    platform="string",
                    manufacturer="string",
                    model="string",
                ),
                tracking=Tracking(
                    os_version="string",
                    ip="string",
                    lat="string",
                    long_="string",
                ),
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        user_id: str,
        token: str,
        *,
        request: PatchUserTokenOpts,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Apply a JSON Patch (RFC 6902) to the specified token.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request: PatchUserTokenOpts.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier
        from courier.users import PatchOperation, PatchUserTokenOpts

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tokens.update(
            user_id="string",
            token="string",
            request=PatchUserTokenOpts(
                patch=[PatchOperation()],
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder(request)
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder(request),
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
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(
        self, user_id: str, token: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetUserTokenResponse:
        """
        Get single token available for a `:token`

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - token: str. The full token string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tokens.get(
            user_id="string",
            token="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tokens/{jsonable_encoder(token)}",
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
            return pydantic_v1.parse_obj_as(GetUserTokenResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def list(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetAllTokensResponse:
        """
        Gets all tokens available for a :user_id

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tokens.list(
            user_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tokens"
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
            return pydantic_v1.parse_obj_as(GetAllTokensResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic_v1.parse_obj_as(BadRequest, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
