# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..types import audience_list_params, audience_update_params, audience_list_members_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.audience import Audience
from ..types.filter_param import FilterParam
from ..types.audience_list_response import AudienceListResponse
from ..types.audience_update_response import AudienceUpdateResponse
from ..types.audience_list_members_response import AudienceListMembersResponse

__all__ = ["AudiencesResource", "AsyncAudiencesResource"]


class AudiencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AudiencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """
        Returns the specified audience by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._get(
            f"/audiences/{audience_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
        )

    def update(
        self,
        audience_id: str,
        *,
        description: Optional[str] | Omit = omit,
        filter: Optional[FilterParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceUpdateResponse:
        """
        Creates or updates audience.

        Args:
          description: A description of the audience

          filter: A single filter to use for filtering

          name: The name of the audience

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._put(
            f"/audiences/{audience_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "filter": filter,
                    "name": name,
                },
                audience_update_params.AudienceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceUpdateResponse,
        )

    def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceListResponse:
        """
        Get the audiences associated with the authorization token.

        Args:
          cursor: A unique identifier that allows for fetching the next set of audiences

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/audiences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, audience_list_params.AudienceListParams),
            ),
            cast_to=AudienceListResponse,
        )

    def delete(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the specified audience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/audiences/{audience_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list_members(
        self,
        audience_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceListMembersResponse:
        """
        Get list of members of an audience.

        Args:
          cursor: A unique identifier that allows for fetching the next set of members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return self._get(
            f"/audiences/{audience_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"cursor": cursor}, audience_list_members_params.AudienceListMembersParams),
            ),
            cast_to=AudienceListMembersResponse,
        )


class AsyncAudiencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAudiencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAudiencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAudiencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncAudiencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Audience:
        """
        Returns the specified audience by id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._get(
            f"/audiences/{audience_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Audience,
        )

    async def update(
        self,
        audience_id: str,
        *,
        description: Optional[str] | Omit = omit,
        filter: Optional[FilterParam] | Omit = omit,
        name: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceUpdateResponse:
        """
        Creates or updates audience.

        Args:
          description: A description of the audience

          filter: A single filter to use for filtering

          name: The name of the audience

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._put(
            f"/audiences/{audience_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "filter": filter,
                    "name": name,
                },
                audience_update_params.AudienceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AudienceUpdateResponse,
        )

    async def list(
        self,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceListResponse:
        """
        Get the audiences associated with the authorization token.

        Args:
          cursor: A unique identifier that allows for fetching the next set of audiences

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/audiences",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"cursor": cursor}, audience_list_params.AudienceListParams),
            ),
            cast_to=AudienceListResponse,
        )

    async def delete(
        self,
        audience_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes the specified audience.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/audiences/{audience_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list_members(
        self,
        audience_id: str,
        *,
        cursor: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AudienceListMembersResponse:
        """
        Get list of members of an audience.

        Args:
          cursor: A unique identifier that allows for fetching the next set of members

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audience_id:
            raise ValueError(f"Expected a non-empty value for `audience_id` but received {audience_id!r}")
        return await self._get(
            f"/audiences/{audience_id}/members",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"cursor": cursor}, audience_list_members_params.AudienceListMembersParams
                ),
            ),
            cast_to=AudienceListMembersResponse,
        )


class AudiencesResourceWithRawResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = to_raw_response_wrapper(
            audiences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            audiences.update,
        )
        self.list = to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = to_raw_response_wrapper(
            audiences.delete,
        )
        self.list_members = to_raw_response_wrapper(
            audiences.list_members,
        )


class AsyncAudiencesResourceWithRawResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = async_to_raw_response_wrapper(
            audiences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            audiences.update,
        )
        self.list = async_to_raw_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_raw_response_wrapper(
            audiences.delete,
        )
        self.list_members = async_to_raw_response_wrapper(
            audiences.list_members,
        )


class AudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = to_streamed_response_wrapper(
            audiences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            audiences.update,
        )
        self.list = to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = to_streamed_response_wrapper(
            audiences.delete,
        )
        self.list_members = to_streamed_response_wrapper(
            audiences.list_members,
        )


class AsyncAudiencesResourceWithStreamingResponse:
    def __init__(self, audiences: AsyncAudiencesResource) -> None:
        self._audiences = audiences

        self.retrieve = async_to_streamed_response_wrapper(
            audiences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            audiences.update,
        )
        self.list = async_to_streamed_response_wrapper(
            audiences.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            audiences.delete,
        )
        self.list_members = async_to_streamed_response_wrapper(
            audiences.list_members,
        )
