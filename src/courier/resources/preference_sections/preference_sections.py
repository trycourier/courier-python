# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

import httpx

from .topics import (
    TopicsResource,
    AsyncTopicsResource,
    TopicsResourceWithRawResponse,
    AsyncTopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
    AsyncTopicsResourceWithStreamingResponse,
)
from ...types import preference_section_create_params, preference_section_replace_params
from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.publish_preferences_response import PublishPreferencesResponse
from ...types.shared.channel_classification import ChannelClassification
from ...types.preference_section_get_response import PreferenceSectionGetResponse
from ...types.preference_section_list_response import PreferenceSectionListResponse

__all__ = ["PreferenceSectionsResource", "AsyncPreferenceSectionsResource"]


class PreferenceSectionsResource(SyncAPIResource):
    @cached_property
    def topics(self) -> TopicsResource:
        return TopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PreferenceSectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return PreferenceSectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferenceSectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return PreferenceSectionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        has_custom_routing: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """Create a preference section in your workspace.

        The section id is generated and
        returned. Topics are created inside a section via POST
        /preferences/sections/{section_id}/topics.

        Args:
          name: Human-readable name for the section.

          has_custom_routing: Whether the section defines custom routing for its topics.

          routing_options: Default channels for the section. Defaults to empty if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/preferences/sections",
            body=maybe_transform(
                {
                    "name": name,
                    "has_custom_routing": has_custom_routing,
                    "routing_options": routing_options,
                },
                preference_section_create_params.PreferenceSectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )

    def retrieve(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """
        Retrieve a preference section by id, including its topics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return self._get(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionListResponse:
        """List the workspace's preference sections.

        Each section embeds its topics. Scoped
        to the workspace of the API key.
        """
        return self._get(
            "/preferences/sections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionListResponse,
        )

    def archive(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a preference section.

        The section must be empty: delete its topics
        first, otherwise the request fails with 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def publish(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublishPreferencesResponse:
        """Publish the workspace's preferences page.

        Takes a snapshot of every section with
        its topics under a new published version, making the current state visible on
        the hosted preferences page (non-draft).
        """
        return self._post(
            "/preferences/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublishPreferencesResponse,
        )

    def replace(
        self,
        section_id: str,
        *,
        name: str,
        has_custom_routing: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """Replace a preference section.

        Full document replacement; missing optional fields
        are cleared. Topics attached to the section are unaffected.

        Args:
          name: Human-readable name for the section.

          has_custom_routing: Whether the section defines custom routing for its topics.

          routing_options: Default channels for the section. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return self._put(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            body=maybe_transform(
                {
                    "name": name,
                    "has_custom_routing": has_custom_routing,
                    "routing_options": routing_options,
                },
                preference_section_replace_params.PreferenceSectionReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )


class AsyncPreferenceSectionsResource(AsyncAPIResource):
    @cached_property
    def topics(self) -> AsyncTopicsResource:
        return AsyncTopicsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPreferenceSectionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferenceSectionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferenceSectionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncPreferenceSectionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        has_custom_routing: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """Create a preference section in your workspace.

        The section id is generated and
        returned. Topics are created inside a section via POST
        /preferences/sections/{section_id}/topics.

        Args:
          name: Human-readable name for the section.

          has_custom_routing: Whether the section defines custom routing for its topics.

          routing_options: Default channels for the section. Defaults to empty if omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/preferences/sections",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "has_custom_routing": has_custom_routing,
                    "routing_options": routing_options,
                },
                preference_section_create_params.PreferenceSectionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )

    async def retrieve(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """
        Retrieve a preference section by id, including its topics.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return await self._get(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionListResponse:
        """List the workspace's preference sections.

        Each section embeds its topics. Scoped
        to the workspace of the API key.
        """
        return await self._get(
            "/preferences/sections",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionListResponse,
        )

    async def archive(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a preference section.

        The section must be empty: delete its topics
        first, otherwise the request fails with 409.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def publish(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PublishPreferencesResponse:
        """Publish the workspace's preferences page.

        Takes a snapshot of every section with
        its topics under a new published version, making the current state visible on
        the hosted preferences page (non-draft).
        """
        return await self._post(
            "/preferences/publish",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PublishPreferencesResponse,
        )

    async def replace(
        self,
        section_id: str,
        *,
        name: str,
        has_custom_routing: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PreferenceSectionGetResponse:
        """Replace a preference section.

        Full document replacement; missing optional fields
        are cleared. Topics attached to the section are unaffected.

        Args:
          name: Human-readable name for the section.

          has_custom_routing: Whether the section defines custom routing for its topics.

          routing_options: Default channels for the section. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return await self._put(
            path_template("/preferences/sections/{section_id}", section_id=section_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "has_custom_routing": has_custom_routing,
                    "routing_options": routing_options,
                },
                preference_section_replace_params.PreferenceSectionReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PreferenceSectionGetResponse,
        )


class PreferenceSectionsResourceWithRawResponse:
    def __init__(self, preference_sections: PreferenceSectionsResource) -> None:
        self._preference_sections = preference_sections

        self.create = to_raw_response_wrapper(
            preference_sections.create,
        )
        self.retrieve = to_raw_response_wrapper(
            preference_sections.retrieve,
        )
        self.list = to_raw_response_wrapper(
            preference_sections.list,
        )
        self.archive = to_raw_response_wrapper(
            preference_sections.archive,
        )
        self.publish = to_raw_response_wrapper(
            preference_sections.publish,
        )
        self.replace = to_raw_response_wrapper(
            preference_sections.replace,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        return TopicsResourceWithRawResponse(self._preference_sections.topics)


class AsyncPreferenceSectionsResourceWithRawResponse:
    def __init__(self, preference_sections: AsyncPreferenceSectionsResource) -> None:
        self._preference_sections = preference_sections

        self.create = async_to_raw_response_wrapper(
            preference_sections.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            preference_sections.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            preference_sections.list,
        )
        self.archive = async_to_raw_response_wrapper(
            preference_sections.archive,
        )
        self.publish = async_to_raw_response_wrapper(
            preference_sections.publish,
        )
        self.replace = async_to_raw_response_wrapper(
            preference_sections.replace,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        return AsyncTopicsResourceWithRawResponse(self._preference_sections.topics)


class PreferenceSectionsResourceWithStreamingResponse:
    def __init__(self, preference_sections: PreferenceSectionsResource) -> None:
        self._preference_sections = preference_sections

        self.create = to_streamed_response_wrapper(
            preference_sections.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            preference_sections.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            preference_sections.list,
        )
        self.archive = to_streamed_response_wrapper(
            preference_sections.archive,
        )
        self.publish = to_streamed_response_wrapper(
            preference_sections.publish,
        )
        self.replace = to_streamed_response_wrapper(
            preference_sections.replace,
        )

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        return TopicsResourceWithStreamingResponse(self._preference_sections.topics)


class AsyncPreferenceSectionsResourceWithStreamingResponse:
    def __init__(self, preference_sections: AsyncPreferenceSectionsResource) -> None:
        self._preference_sections = preference_sections

        self.create = async_to_streamed_response_wrapper(
            preference_sections.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            preference_sections.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            preference_sections.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            preference_sections.archive,
        )
        self.publish = async_to_streamed_response_wrapper(
            preference_sections.publish,
        )
        self.replace = async_to_streamed_response_wrapper(
            preference_sections.replace,
        )

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        return AsyncTopicsResourceWithStreamingResponse(self._preference_sections.topics)
