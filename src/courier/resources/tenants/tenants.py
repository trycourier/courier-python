# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional

import httpx

from ...types import tenant_list_params, tenant_update_params, tenant_list_users_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .templates import (
    TemplatesResource,
    AsyncTemplatesResource,
    TemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
    AsyncTemplatesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.tenant import Tenant
from .preferences.preferences import (
    PreferencesResource,
    AsyncPreferencesResource,
    PreferencesResourceWithRawResponse,
    AsyncPreferencesResourceWithRawResponse,
    PreferencesResourceWithStreamingResponse,
    AsyncPreferencesResourceWithStreamingResponse,
)
from ...types.tenant_list_response import TenantListResponse
from ...types.default_preferences_param import DefaultPreferencesParam
from ...types.tenant_list_users_response import TenantListUsersResponse

__all__ = ["TenantsResource", "AsyncTenantsResource"]


class TenantsResource(SyncAPIResource):
    @cached_property
    def preferences(self) -> PreferencesResource:
        return PreferencesResource(self._client)

    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> TenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TenantsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Get a Tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    def update(
        self,
        tenant_id: str,
        *,
        name: str,
        brand_id: Optional[str] | Omit = omit,
        default_preferences: Optional[DefaultPreferencesParam] | Omit = omit,
        parent_tenant_id: Optional[str] | Omit = omit,
        properties: Optional[Dict[str, object]] | Omit = omit,
        user_profile: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Create or Replace a Tenant

        Args:
          name: Name of the tenant.

          brand_id: Brand to be used for the account when one is not specified by the send call.

          default_preferences: Defines the preferences used for the tenant when the user hasn't specified their
              own.

          parent_tenant_id: Tenant's parent id (if any).

          properties: Arbitrary properties accessible to a template.

          user_profile: A user profile object merged with user profile on send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._put(
            f"/tenants/{tenant_id}",
            body=maybe_transform(
                {
                    "name": name,
                    "brand_id": brand_id,
                    "default_preferences": default_preferences,
                    "parent_tenant_id": parent_tenant_id,
                    "properties": properties,
                    "user_profile": user_profile,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        parent_tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListResponse:
        """
        Get a List of Tenants

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of tenants to return (defaults to 20, maximum value of 100)

          parent_tenant_id: Filter the list of tenants by parent_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/tenants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "parent_tenant_id": parent_tenant_id,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            cast_to=TenantListResponse,
        )

    def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_users(
        self,
        tenant_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListUsersResponse:
        """
        Get Users in Tenant

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of accounts to return (defaults to 20, maximum value of 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            f"/tenants/{tenant_id}/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    tenant_list_users_params.TenantListUsersParams,
                ),
            ),
            cast_to=TenantListUsersResponse,
        )


class AsyncTenantsResource(AsyncAPIResource):
    @cached_property
    def preferences(self) -> AsyncPreferencesResource:
        return AsyncPreferencesResource(self._client)

    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTenantsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTenantsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTenantsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTenantsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Get a Tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    async def update(
        self,
        tenant_id: str,
        *,
        name: str,
        brand_id: Optional[str] | Omit = omit,
        default_preferences: Optional[DefaultPreferencesParam] | Omit = omit,
        parent_tenant_id: Optional[str] | Omit = omit,
        properties: Optional[Dict[str, object]] | Omit = omit,
        user_profile: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Tenant:
        """
        Create or Replace a Tenant

        Args:
          name: Name of the tenant.

          brand_id: Brand to be used for the account when one is not specified by the send call.

          default_preferences: Defines the preferences used for the tenant when the user hasn't specified their
              own.

          parent_tenant_id: Tenant's parent id (if any).

          properties: Arbitrary properties accessible to a template.

          user_profile: A user profile object merged with user profile on send.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._put(
            f"/tenants/{tenant_id}",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "brand_id": brand_id,
                    "default_preferences": default_preferences,
                    "parent_tenant_id": parent_tenant_id,
                    "properties": properties,
                    "user_profile": user_profile,
                },
                tenant_update_params.TenantUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Tenant,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        parent_tenant_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListResponse:
        """
        Get a List of Tenants

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of tenants to return (defaults to 20, maximum value of 100)

          parent_tenant_id: Filter the list of tenants by parent_id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/tenants",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "parent_tenant_id": parent_tenant_id,
                    },
                    tenant_list_params.TenantListParams,
                ),
            ),
            cast_to=TenantListResponse,
        )

    async def delete(
        self,
        tenant_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete a Tenant

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/tenants/{tenant_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_users(
        self,
        tenant_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        limit: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TenantListUsersResponse:
        """
        Get Users in Tenant

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of accounts to return (defaults to 20, maximum value of 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            f"/tenants/{tenant_id}/users",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    tenant_list_users_params.TenantListUsersParams,
                ),
            ),
            cast_to=TenantListUsersResponse,
        )


class TenantsResourceWithRawResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_raw_response_wrapper(
            tenants.update,
        )
        self.list = to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = to_raw_response_wrapper(
            tenants.delete,
        )
        self.list_users = to_raw_response_wrapper(
            tenants.list_users,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithRawResponse:
        return PreferencesResourceWithRawResponse(self._tenants.preferences)

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._tenants.templates)


class AsyncTenantsResourceWithRawResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = async_to_raw_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            tenants.update,
        )
        self.list = async_to_raw_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_raw_response_wrapper(
            tenants.delete,
        )
        self.list_users = async_to_raw_response_wrapper(
            tenants.list_users,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithRawResponse:
        return AsyncPreferencesResourceWithRawResponse(self._tenants.preferences)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._tenants.templates)


class TenantsResourceWithStreamingResponse:
    def __init__(self, tenants: TenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = to_streamed_response_wrapper(
            tenants.delete,
        )
        self.list_users = to_streamed_response_wrapper(
            tenants.list_users,
        )

    @cached_property
    def preferences(self) -> PreferencesResourceWithStreamingResponse:
        return PreferencesResourceWithStreamingResponse(self._tenants.preferences)

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._tenants.templates)


class AsyncTenantsResourceWithStreamingResponse:
    def __init__(self, tenants: AsyncTenantsResource) -> None:
        self._tenants = tenants

        self.retrieve = async_to_streamed_response_wrapper(
            tenants.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            tenants.update,
        )
        self.list = async_to_streamed_response_wrapper(
            tenants.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            tenants.delete,
        )
        self.list_users = async_to_streamed_response_wrapper(
            tenants.list_users,
        )

    @cached_property
    def preferences(self) -> AsyncPreferencesResourceWithStreamingResponse:
        return AsyncPreferencesResourceWithStreamingResponse(self._tenants.preferences)

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._tenants.templates)
