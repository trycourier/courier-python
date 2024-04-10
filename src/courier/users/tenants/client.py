# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...commons.types.user_tenant_association import UserTenantAssociation
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.pydantic_utilities import pydantic_v1
from ...core.remove_none_from_dict import remove_none_from_dict
from ...core.request_options import RequestOptions
from .types.add_user_to_single_tenants_params_profile import AddUserToSingleTenantsParamsProfile
from .types.list_tenants_for_user_response import ListTenantsForUserResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class TenantsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def add_multple(
        self,
        user_id: str,
        *,
        tenants: typing.Sequence[UserTenantAssociation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a user to
        multiple tenants in one call.
        A custom profile can also be supplied for each tenant.
        This profile will be merged with the user's main
        profile when sending to the user with that tenant.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - tenants: typing.Sequence[UserTenantAssociation].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier import UserTenantAssociation
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.add_multple(
            user_id="string",
            tenants=[
                UserTenantAssociation(
                    user_id="string",
                    type="user",
                    tenant_id="string",
                    profile={"string": {"key": "value"}},
                )
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"tenants": tenants})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"tenants": tenants}),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add(
        self,
        user_id: str,
        tenant_id: str,
        *,
        profile: AddUserToSingleTenantsParamsProfile,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters:
            - user_id: str. Id of the user to be added to the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be added to.

            - profile: AddUserToSingleTenantsParamsProfile.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier
        from courier.users import AddUserToSingleTenantsParamsProfile

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.add(
            user_id="string",
            tenant_id="string",
            profile=AddUserToSingleTenantsParamsProfile(
                title="string",
                email="string",
                phone_number="string",
                locale="string",
                additional_fields={"string": {"key": "value"}},
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"profile": profile})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"profile": profile}),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove_all(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from any tenants they may have been associated with.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.remove_all(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
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

    def remove(self, user_id: str, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be removed from.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.remove(
            user_id="string",
            tenant_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
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

    def list(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTenantsForUserResponse:
        """
        Returns a paginated list of user tenant associations.

        Parameters:
            - user_id: str. Id of the user to retrieve all associated tenants for.

            - limit: typing.Optional[int]. The number of accounts to return
                                           (defaults to 20, maximum value of 100)
            - cursor: typing.Optional[str]. Continue the pagination with the next cursor

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.list(
            user_id="string",
            limit=1,
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "limit": limit,
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
            return pydantic_v1.parse_obj_as(ListTenantsForUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncTenantsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def add_multple(
        self,
        user_id: str,
        *,
        tenants: typing.Sequence[UserTenantAssociation],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a user to
        multiple tenants in one call.
        A custom profile can also be supplied for each tenant.
        This profile will be merged with the user's main
        profile when sending to the user with that tenant.

        Parameters:
            - user_id: str. The user's ID. This can be any uniquely identifiable string.

            - tenants: typing.Sequence[UserTenantAssociation].

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier import UserTenantAssociation
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tenants.add_multple(
            user_id="string",
            tenants=[
                UserTenantAssociation(
                    user_id="string",
                    type="user",
                    tenant_id="string",
                    profile={"string": {"key": "value"}},
                )
            ],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"tenants": tenants})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"tenants": tenants}),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add(
        self,
        user_id: str,
        tenant_id: str,
        *,
        profile: AddUserToSingleTenantsParamsProfile,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters:
            - user_id: str. Id of the user to be added to the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be added to.

            - profile: AddUserToSingleTenantsParamsProfile.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier
        from courier.users import AddUserToSingleTenantsParamsProfile

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tenants.add(
            user_id="string",
            tenant_id="string",
            profile=AddUserToSingleTenantsParamsProfile(
                title="string",
                email="string",
                phone_number="string",
                locale="string",
                additional_fields={"string": {"key": "value"}},
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PUT",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            ),
            params=jsonable_encoder(
                request_options.get("additional_query_parameters") if request_options is not None else None
            ),
            json=jsonable_encoder({"profile": profile})
            if request_options is None or request_options.get("additional_body_parameters") is None
            else {
                **jsonable_encoder({"profile": profile}),
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
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove_all(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from any tenants they may have been associated with.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tenants.remove_all(
            user_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
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

    async def remove(
        self, user_id: str, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters:
            - user_id: str. Id of the user to be removed from the supplied tenant.

            - tenant_id: str. Id of the tenant the user should be removed from.

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tenants.remove(
            user_id="string",
            tenant_id="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/",
                f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
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

    async def list(
        self,
        user_id: str,
        *,
        limit: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ListTenantsForUserResponse:
        """
        Returns a paginated list of user tenant associations.

        Parameters:
            - user_id: str. Id of the user to retrieve all associated tenants for.

            - limit: typing.Optional[int]. The number of accounts to return
                                           (defaults to 20, maximum value of 100)
            - cursor: typing.Optional[str]. Continue the pagination with the next cursor

            - request_options: typing.Optional[RequestOptions]. Request-specific configuration.
        ---
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        await client.users.tenants.list(
            user_id="string",
            limit=1,
            cursor="string",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"users/{jsonable_encoder(user_id)}/tenants"
            ),
            params=jsonable_encoder(
                remove_none_from_dict(
                    {
                        "limit": limit,
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
            return pydantic_v1.parse_obj_as(ListTenantsForUserResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
