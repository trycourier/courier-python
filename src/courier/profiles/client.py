# This file was auto-generated by Fern from our API Definition.

import typing
from json.decoder import JSONDecodeError

from ..commons.errors.bad_request_error import BadRequestError
from ..commons.types.bad_request import BadRequest
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.jsonable_encoder import jsonable_encoder
from ..core.request_options import RequestOptions
from ..core.unchecked_base_model import construct_type
from .types.delete_list_subscription_response import DeleteListSubscriptionResponse
from .types.get_list_subscriptions_response import GetListSubscriptionsResponse
from .types.merge_profile_response import MergeProfileResponse
from .types.profile_get_response import ProfileGetResponse
from .types.replace_profile_response import ReplaceProfileResponse
from .types.subscribe_to_lists_request import SubscribeToListsRequest
from .types.subscribe_to_lists_response import SubscribeToListsResponse

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ProfileGetResponse:
        """
        Returns the specified user profile.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileGetResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.get(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ProfileGetResponse, construct_type(type_=ProfileGetResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        user_id: str,
        *,
        profile: typing.Dict[str, typing.Any],
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MergeProfileResponse:
        """
        Merge the supplied values with an existing profile or create a new profile if one doesn't already exist.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        profile : typing.Dict[str, typing.Any]

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergeProfileResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.create(
            user_id="string",
            profile={"string": {"key": "value"}},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}",
            method="POST",
            json={"profile": profile},
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MergeProfileResponse, construct_type(type_=MergeProfileResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def replace(
        self,
        user_id: str,
        *,
        profile: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceProfileResponse:
        """
        When using `PUT`, be sure to include all the key-value pairs required by the recipient's profile.
        Any key-value pairs that exist in the profile but fail to be included in the `PUT` request will be
        removed from the profile. Remember, a `PUT` update is a full replacement of the data. For partial updates,
        use the [Patch](https://www.courier.com/docs/reference/profiles/patch/) request.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        profile : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceProfileResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.replace(
            user_id="string",
            profile={"string": {"key": "value"}},
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}",
            method="PUT",
            json={"profile": profile},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ReplaceProfileResponse, construct_type(type_=ReplaceProfileResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the specified user profile.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

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
        client.profiles.delete(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_list_subscriptions(
        self,
        user_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListSubscriptionsResponse:
        """
        Returns the subscribed lists for a specified user.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of message statuses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListSubscriptionsResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.get_list_subscriptions(
            user_id="string",
            cursor="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists",
            method="GET",
            params={"cursor": cursor},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(GetListSubscriptionsResponse, construct_type(type_=GetListSubscriptionsResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def subscribe_to_lists(
        self,
        user_id: str,
        *,
        request: SubscribeToListsRequest,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeToListsResponse:
        """
        Subscribes the given user to one or more lists. If the list does not exist, it will be created.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request : SubscribeToListsRequest

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeToListsResponse

        Examples
        --------
        from courier import (
            RecipientPreferences,
            SubscribeToListsRequest,
            SubscribeToListsRequestListObject,
        )
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.subscribe_to_lists(
            user_id="string",
            request=SubscribeToListsRequest(
                lists=[
                    SubscribeToListsRequestListObject(
                        list_id="string",
                        preferences=RecipientPreferences(
                            categories={"string": {"key": "value"}},
                            notifications={"string": {"key": "value"}},
                        ),
                    )
                ],
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists",
            method="POST",
            json=request,
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(SubscribeToListsResponse, construct_type(type_=SubscribeToListsResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_list_subscription(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteListSubscriptionResponse:
        """
        Removes all list subscriptions for given user.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteListSubscriptionResponse

        Examples
        --------
        from courier.client import Courier

        client = Courier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )
        client.profiles.delete_list_subscription(
            user_id="string",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DeleteListSubscriptionResponse, construct_type(type_=DeleteListSubscriptionResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> ProfileGetResponse:
        """
        Returns the specified user profile.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ProfileGetResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.get(
                user_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}", method="GET", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ProfileGetResponse, construct_type(type_=ProfileGetResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        user_id: str,
        *,
        profile: typing.Dict[str, typing.Any],
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> MergeProfileResponse:
        """
        Merge the supplied values with an existing profile or create a new profile if one doesn't already exist.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        profile : typing.Dict[str, typing.Any]

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        MergeProfileResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.create(
                user_id="string",
                profile={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}",
            method="POST",
            json={"profile": profile},
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(MergeProfileResponse, construct_type(type_=MergeProfileResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def replace(
        self,
        user_id: str,
        *,
        profile: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> ReplaceProfileResponse:
        """
        When using `PUT`, be sure to include all the key-value pairs required by the recipient's profile.
        Any key-value pairs that exist in the profile but fail to be included in the `PUT` request will be
        removed from the profile. Remember, a `PUT` update is a full replacement of the data. For partial updates,
        use the [Patch](https://www.courier.com/docs/reference/profiles/patch/) request.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        profile : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ReplaceProfileResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.replace(
                user_id="string",
                profile={"string": {"key": "value"}},
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}",
            method="PUT",
            json={"profile": profile},
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(ReplaceProfileResponse, construct_type(type_=ReplaceProfileResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> None:
        """
        Deletes the specified user profile.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

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
            await client.profiles.delete(
                user_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_list_subscriptions(
        self,
        user_id: str,
        *,
        cursor: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetListSubscriptionsResponse:
        """
        Returns the subscribed lists for a specified user.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        cursor : typing.Optional[str]
            A unique identifier that allows for fetching the next set of message statuses.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetListSubscriptionsResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.get_list_subscriptions(
                user_id="string",
                cursor="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists",
            method="GET",
            params={"cursor": cursor},
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(GetListSubscriptionsResponse, construct_type(type_=GetListSubscriptionsResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def subscribe_to_lists(
        self,
        user_id: str,
        *,
        request: SubscribeToListsRequest,
        idempotency_key: typing.Optional[str] = None,
        idempotency_expiry: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> SubscribeToListsResponse:
        """
        Subscribes the given user to one or more lists. If the list does not exist, it will be created.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request : SubscribeToListsRequest

        idempotency_key : typing.Optional[str]

        idempotency_expiry : typing.Optional[str]
            The expiry can either be an ISO8601 datetime or a duration like "1 Day".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        SubscribeToListsResponse

        Examples
        --------
        import asyncio

        from courier import (
            RecipientPreferences,
            SubscribeToListsRequest,
            SubscribeToListsRequestListObject,
        )
        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.subscribe_to_lists(
                user_id="string",
                request=SubscribeToListsRequest(
                    lists=[
                        SubscribeToListsRequestListObject(
                            list_id="string",
                            preferences=RecipientPreferences(
                                categories={"string": {"key": "value"}},
                                notifications={"string": {"key": "value"}},
                            ),
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists",
            method="POST",
            json=request,
            headers={
                "Idempotency-Key": str(idempotency_key) if idempotency_key is not None else None,
                "X-Idempotency-Expiration": str(idempotency_expiry) if idempotency_expiry is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(SubscribeToListsResponse, construct_type(type_=SubscribeToListsResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_list_subscription(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteListSubscriptionResponse:
        """
        Removes all list subscriptions for given user.

        Parameters
        ----------
        user_id : str
            A unique identifier representing the user associated with the requested profile.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteListSubscriptionResponse

        Examples
        --------
        import asyncio

        from courier.client import AsyncCourier

        client = AsyncCourier(
            authorization_token="YOUR_AUTHORIZATION_TOKEN",
        )


        async def main() -> None:
            await client.profiles.delete_list_subscription(
                user_id="string",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profiles/{jsonable_encoder(user_id)}/lists", method="DELETE", request_options=request_options
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(DeleteListSubscriptionResponse, construct_type(type_=DeleteListSubscriptionResponse, object_=_response.json()))  # type: ignore
            if _response.status_code == 400:
                raise BadRequestError(
                    typing.cast(BadRequest, construct_type(type_=BadRequest, object_=_response.json()))  # type: ignore
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
