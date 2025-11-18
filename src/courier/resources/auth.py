# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import auth_issue_token_params
from .._types import Body, Query, Headers, NotGiven, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.auth_issue_token_response import AuthIssueTokenResponse

__all__ = ["AuthResource", "AsyncAuthResource"]


class AuthResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AuthResourceWithStreamingResponse(self)

    def issue_token(
        self,
        *,
        expires_in: str,
        scope: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthIssueTokenResponse:
        """
        Returns a new access token.

        Args:
          expires_in:
              Duration for token expiration. Accepts various time formats:

              - "2 hours" - 2 hours from now
              - "1d" - 1 day
              - "3 days" - 3 days
              - "10h" - 10 hours
              - "2.5 hrs" - 2.5 hours
              - "1m" - 1 minute
              - "5s" - 5 seconds
              - "1y" - 1 year

          scope:
              Available scopes:

              - `user_id:<user-id>` - Defines which user the token will be scoped to. Multiple
                can be listed if needed. Ex `user_id:pigeon user_id:bluebird`.
              - `read:messages` - Read messages.
              - `read:user-tokens` - Read user push tokens.
              - `write:user-tokens` - Write user push tokens.
              - `read:brands[:<brand_id>]` - Read brands, optionally restricted to a specific
                brand_id. Examples `read:brands`, `read:brands:my_brand`.
              - `write:brands[:<brand_id>]` - Write brands, optionally restricted to a
                specific brand_id. Examples `write:brands`, `write:brands:my_brand`.
              - `inbox:read:messages` - Read inbox messages.
              - `inbox:write:events` - Write inbox events, such as mark message as read.
              - `read:preferences` - Read user preferences.
              - `write:preferences` - Write user preferences. Example:
                `user_id:user123 write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/auth/issue-token",
            body=maybe_transform(
                {
                    "expires_in": expires_in,
                    "scope": scope,
                },
                auth_issue_token_params.AuthIssueTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthIssueTokenResponse,
        )


class AsyncAuthResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuthResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuthResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuthResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncAuthResourceWithStreamingResponse(self)

    async def issue_token(
        self,
        *,
        expires_in: str,
        scope: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuthIssueTokenResponse:
        """
        Returns a new access token.

        Args:
          expires_in:
              Duration for token expiration. Accepts various time formats:

              - "2 hours" - 2 hours from now
              - "1d" - 1 day
              - "3 days" - 3 days
              - "10h" - 10 hours
              - "2.5 hrs" - 2.5 hours
              - "1m" - 1 minute
              - "5s" - 5 seconds
              - "1y" - 1 year

          scope:
              Available scopes:

              - `user_id:<user-id>` - Defines which user the token will be scoped to. Multiple
                can be listed if needed. Ex `user_id:pigeon user_id:bluebird`.
              - `read:messages` - Read messages.
              - `read:user-tokens` - Read user push tokens.
              - `write:user-tokens` - Write user push tokens.
              - `read:brands[:<brand_id>]` - Read brands, optionally restricted to a specific
                brand_id. Examples `read:brands`, `read:brands:my_brand`.
              - `write:brands[:<brand_id>]` - Write brands, optionally restricted to a
                specific brand_id. Examples `write:brands`, `write:brands:my_brand`.
              - `inbox:read:messages` - Read inbox messages.
              - `inbox:write:events` - Write inbox events, such as mark message as read.
              - `read:preferences` - Read user preferences.
              - `write:preferences` - Write user preferences. Example:
                `user_id:user123 write:user-tokens inbox:read:messages inbox:write:events read:preferences write:preferences read:brands`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/auth/issue-token",
            body=await async_maybe_transform(
                {
                    "expires_in": expires_in,
                    "scope": scope,
                },
                auth_issue_token_params.AuthIssueTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuthIssueTokenResponse,
        )


class AuthResourceWithRawResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.issue_token = to_raw_response_wrapper(
            auth.issue_token,
        )


class AsyncAuthResourceWithRawResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.issue_token = async_to_raw_response_wrapper(
            auth.issue_token,
        )


class AuthResourceWithStreamingResponse:
    def __init__(self, auth: AuthResource) -> None:
        self._auth = auth

        self.issue_token = to_streamed_response_wrapper(
            auth.issue_token,
        )


class AsyncAuthResourceWithStreamingResponse:
    def __init__(self, auth: AsyncAuthResource) -> None:
        self._auth = auth

        self.issue_token = async_to_streamed_response_wrapper(
            auth.issue_token,
        )
