# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ...commons.types.user_tenant_association import UserTenantAssociation
from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...core.request_options import RequestOptions
from ...core.unchecked_base_model import construct_type
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

        Parameters
        ----------
        user_id : str
            The user's ID. This can be any uniquely identifiable string.

        tenants : typing.Sequence[UserTenantAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from courier import UserTenantAssociation
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.add_multple(
            user_id="user_id",
            tenants=[
                UserTenantAssociation(
                    tenant_id="tenant_id",
                ),
                UserTenantAssociation(
                    tenant_id="tenant_id",
                ),
            ],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants",
            method="PUT",
            json={"tenants": tenants},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def add(
        self,
        user_id: str,
        tenant_id: str,
        *,
        profile: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters
        ----------
        user_id : str
            Id of the user to be added to the supplied tenant.

        tenant_id : str
            Id of the tenant the user should be added to.

        profile : typing.Optional[typing.Dict[str, typing.Any]]

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
        client.users.tenants.add(
            user_id="user_id",
            tenant_id="tenant_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            method="PUT",
            json={"profile": profile},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove_all(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from any tenants they may have been associated with.

        Parameters
        ----------
        user_id : str
            Id of the user to be removed from the supplied tenant.

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
        client.users.tenants.remove_all(
            user_id="user_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def remove(self, user_id: str, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters
        ----------
        user_id : str
            Id of the user to be removed from the supplied tenant.

        tenant_id : str
            Id of the tenant the user should be removed from.

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
        client.users.tenants.remove(
            user_id="user_id",
            tenant_id="tenant_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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

        Parameters
        ----------
        user_id : str
            Id of the user to retrieve all associated tenants for.

        limit : typing.Optional[int]
            The number of accounts to return
            (defaults to 20, maximum value of 100)

        cursor : typing.Optional[str]
            Continue the pagination with the next cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTenantsForUserResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.users.tenants.list(
            user_id="user_id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants",
            method="GET",
            params={"limit": limit, "cursor": cursor},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ListTenantsForUserResponse, construct_type(type_=ListTenantsForUserResponse, object_=_response.json()))  # type: ignore
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

        Parameters
        ----------
        user_id : str
            The user's ID. This can be any uniquely identifiable string.

        tenants : typing.Sequence[UserTenantAssociation]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from courier import UserTenantAssociation
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.users.tenants.add_multple(
                user_id="user_id",
                tenants=[
                    UserTenantAssociation(
                        tenant_id="tenant_id",
                    ),
                    UserTenantAssociation(
                        tenant_id="tenant_id",
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants",
            method="PUT",
            json={"tenants": tenants},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def add(
        self,
        user_id: str,
        tenant_id: str,
        *,
        profile: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        This endpoint is used to add a single tenant.

        A custom profile can also be supplied with the tenant.
        This profile will be merged with the user's main profile
        when sending to the user with that tenant.

        Parameters
        ----------
        user_id : str
            Id of the user to be added to the supplied tenant.

        tenant_id : str
            Id of the tenant the user should be added to.

        profile : typing.Optional[typing.Dict[str, typing.Any]]

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
            await client.users.tenants.add(
                user_id="user_id",
                tenant_id="tenant_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            method="PUT",
            json={"profile": profile},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove_all(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Removes a user from any tenants they may have been associated with.

        Parameters
        ----------
        user_id : str
            Id of the user to be removed from the supplied tenant.

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
            await client.users.tenants.remove_all(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def remove(
        self, user_id: str, tenant_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Removes a user from the supplied tenant.

        Parameters
        ----------
        user_id : str
            Id of the user to be removed from the supplied tenant.

        tenant_id : str
            Id of the tenant the user should be removed from.

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
            await client.users.tenants.remove(
                user_id="user_id",
                tenant_id="tenant_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants/{jsonable_encoder(tenant_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return
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

        Parameters
        ----------
        user_id : str
            Id of the user to retrieve all associated tenants for.

        limit : typing.Optional[int]
            The number of accounts to return
            (defaults to 20, maximum value of 100)

        cursor : typing.Optional[str]
            Continue the pagination with the next cursor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListTenantsForUserResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.users.tenants.list(
                user_id="user_id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"users/{jsonable_encoder(user_id)}/tenants",
            method="GET",
            params={"limit": limit, "cursor": cursor},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ListTenantsForUserResponse, construct_type(type_=ListTenantsForUserResponse, object_=_response.json()))  # type: ignore
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
