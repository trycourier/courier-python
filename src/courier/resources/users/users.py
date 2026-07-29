# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tokens import (
    TokensResource,
    AsyncTokensResource,
    TokensResourceWithRawResponse,
    AsyncTokensResourceWithRawResponse,
    TokensResourceWithStreamingResponse,
    AsyncTokensResourceWithStreamingResponse,
)
from .tenants import (
    TenantsResource,
    AsyncTenantsResource,
    TenantsResourceWithRawResponse,
    AsyncTenantsResourceWithRawResponse,
    TenantsResourceWithStreamingResponse,
    AsyncTenantsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def preferences(self) -> PreferencesResource:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return PreferencesResource(self._client)

    @cached_property
    def tenants(self) -> TenantsResource:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return TenantsResource(self._client)

    @cached_property
    def tokens(self) -> TokensResource:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return TokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return AsyncPreferencesResource(self._client)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return AsyncTenantsResource(self._client)

    @cached_property
    def tokens(self) -> AsyncTokensResource:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return AsyncTokensResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return PreferencesResourceWithRawResponse(self._users.preferences)

    @cached_property
    def tenants(self) -> TenantsResourceWithRawResponse:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return TenantsResourceWithRawResponse(self._users.tenants)

    @cached_property
    def tokens(self) -> TokensResourceWithRawResponse:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return TokensResourceWithRawResponse(self._users.tokens)


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return AsyncPreferencesResourceWithRawResponse(self._users.preferences)

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithRawResponse:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return AsyncTenantsResourceWithRawResponse(self._users.tenants)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithRawResponse:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return AsyncTokensResourceWithRawResponse(self._users.tokens)


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return PreferencesResourceWithStreamingResponse(self._users.preferences)

    @cached_property
    def tenants(self) -> TenantsResourceWithStreamingResponse:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return TenantsResourceWithStreamingResponse(self._users.tenants)

    @cached_property
    def tokens(self) -> TokensResourceWithStreamingResponse:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return TokensResourceWithStreamingResponse(self._users.tokens)


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        Read and write a single user's notification preferences, per topic and per channel.
        """
        return AsyncPreferencesResourceWithStreamingResponse(self._users.preferences)

    @cached_property
    def tenants(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        Associate a user with one or more tenants, and read or remove those associations.
        """
        return AsyncTenantsResourceWithStreamingResponse(self._users.tenants)

    @cached_property
    def tokens(self) -> AsyncTokensResourceWithStreamingResponse:
        """
        Register and manage the APNS and FCM device tokens Courier delivers push notifications to.
        """
        return AsyncTokensResourceWithStreamingResponse(self._users.tokens)
