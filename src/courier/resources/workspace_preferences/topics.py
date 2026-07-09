# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional
from typing_extensions import Literal

import httpx

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
from ...types.workspace_preferences import topic_create_params, topic_replace_params
from ...types.shared.channel_classification import ChannelClassification
from ...types.workspace_preference_topic_get_response import WorkspacePreferenceTopicGetResponse
from ...types.workspace_preference_topic_list_response import WorkspacePreferenceTopicListResponse

__all__ = ["TopicsResource", "AsyncTopicsResource"]


class TopicsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TopicsResourceWithStreamingResponse(self)

    def create(
        self,
        section_id: str,
        *,
        default_status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        name: str,
        allowed_preferences: Optional[List[Literal["snooze", "channel_preferences"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        include_unsubscribe_header: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        topic_data: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Create a subscription preference topic inside a workspace preference.

        Fails with
        404 if the workspace preference does not exist. The topic id is generated and
        returned.

        Args:
          default_status: The default subscription status applied when a recipient has not set their own.

          name: Human-readable name for the preference topic.

          allowed_preferences: Preference controls a recipient may customize for this topic. Defaults to empty
              if omitted.

          description: Optional description shown under the topic on the hosted preferences page.

          include_unsubscribe_header: Whether to include a list-unsubscribe header on emails for this topic.

          routing_options: Default channels delivered for this topic. Defaults to empty if omitted.

          topic_data: Arbitrary metadata associated with the topic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return self._post(
            path_template("/preferences/sections/{section_id}/topics", section_id=section_id),
            body=maybe_transform(
                {
                    "default_status": default_status,
                    "name": name,
                    "allowed_preferences": allowed_preferences,
                    "description": description,
                    "include_unsubscribe_header": include_unsubscribe_header,
                    "routing_options": routing_options,
                    "topic_data": topic_data,
                },
                topic_create_params.TopicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )

    def retrieve(
        self,
        topic_id: str,
        *,
        section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Retrieve a topic within a workspace preference.

        Returns 404 if the workspace
        preference does not exist, the topic does not exist, or the topic belongs to a
        different workspace preference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._get(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )

    def list(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicListResponse:
        """
        List the topics in a workspace preference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return self._get(
            path_template("/preferences/sections/{section_id}/topics", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicListResponse,
        )

    def archive(
        self,
        topic_id: str,
        *,
        section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a topic and remove it from its workspace preference.

        Same 404 rules as
        GET.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def replace(
        self,
        topic_id: str,
        *,
        section_id: str,
        default_status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        name: str,
        allowed_preferences: Optional[List[Literal["snooze", "channel_preferences"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        include_unsubscribe_header: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        topic_data: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Replace a topic within a workspace preference.

        Full document replacement;
        missing optional fields are cleared. Same 404 rules as GET.

        Args:
          default_status: The default subscription status applied when a recipient has not set their own.

          name: Human-readable name for the preference topic.

          allowed_preferences: Preference controls a recipient may customize. Omit to clear.

          description: Optional description shown under the topic on the hosted preferences page. Omit
              to clear.

          include_unsubscribe_header: Whether to include a list-unsubscribe header on emails for this topic.

          routing_options: Default channels delivered for this topic. Omit to clear.

          topic_data: Arbitrary metadata associated with the topic. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return self._put(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            body=maybe_transform(
                {
                    "default_status": default_status,
                    "name": name,
                    "allowed_preferences": allowed_preferences,
                    "description": description,
                    "include_unsubscribe_header": include_unsubscribe_header,
                    "routing_options": routing_options,
                    "topic_data": topic_data,
                },
                topic_replace_params.TopicReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )


class AsyncTopicsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTopicsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTopicsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopicsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTopicsResourceWithStreamingResponse(self)

    async def create(
        self,
        section_id: str,
        *,
        default_status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        name: str,
        allowed_preferences: Optional[List[Literal["snooze", "channel_preferences"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        include_unsubscribe_header: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        topic_data: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Create a subscription preference topic inside a workspace preference.

        Fails with
        404 if the workspace preference does not exist. The topic id is generated and
        returned.

        Args:
          default_status: The default subscription status applied when a recipient has not set their own.

          name: Human-readable name for the preference topic.

          allowed_preferences: Preference controls a recipient may customize for this topic. Defaults to empty
              if omitted.

          description: Optional description shown under the topic on the hosted preferences page.

          include_unsubscribe_header: Whether to include a list-unsubscribe header on emails for this topic.

          routing_options: Default channels delivered for this topic. Defaults to empty if omitted.

          topic_data: Arbitrary metadata associated with the topic.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return await self._post(
            path_template("/preferences/sections/{section_id}/topics", section_id=section_id),
            body=await async_maybe_transform(
                {
                    "default_status": default_status,
                    "name": name,
                    "allowed_preferences": allowed_preferences,
                    "description": description,
                    "include_unsubscribe_header": include_unsubscribe_header,
                    "routing_options": routing_options,
                    "topic_data": topic_data,
                },
                topic_create_params.TopicCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )

    async def retrieve(
        self,
        topic_id: str,
        *,
        section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Retrieve a topic within a workspace preference.

        Returns 404 if the workspace
        preference does not exist, the topic does not exist, or the topic belongs to a
        different workspace preference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._get(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )

    async def list(
        self,
        section_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicListResponse:
        """
        List the topics in a workspace preference.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        return await self._get(
            path_template("/preferences/sections/{section_id}/topics", section_id=section_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicListResponse,
        )

    async def archive(
        self,
        topic_id: str,
        *,
        section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Archive a topic and remove it from its workspace preference.

        Same 404 rules as
        GET.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def replace(
        self,
        topic_id: str,
        *,
        section_id: str,
        default_status: Literal["OPTED_OUT", "OPTED_IN", "REQUIRED"],
        name: str,
        allowed_preferences: Optional[List[Literal["snooze", "channel_preferences"]]] | Omit = omit,
        description: Optional[str] | Omit = omit,
        include_unsubscribe_header: Optional[bool] | Omit = omit,
        routing_options: Optional[List[ChannelClassification]] | Omit = omit,
        topic_data: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WorkspacePreferenceTopicGetResponse:
        """Replace a topic within a workspace preference.

        Full document replacement;
        missing optional fields are cleared. Same 404 rules as GET.

        Args:
          default_status: The default subscription status applied when a recipient has not set their own.

          name: Human-readable name for the preference topic.

          allowed_preferences: Preference controls a recipient may customize. Omit to clear.

          description: Optional description shown under the topic on the hosted preferences page. Omit
              to clear.

          include_unsubscribe_header: Whether to include a list-unsubscribe header on emails for this topic.

          routing_options: Default channels delivered for this topic. Omit to clear.

          topic_data: Arbitrary metadata associated with the topic. Omit to clear.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not section_id:
            raise ValueError(f"Expected a non-empty value for `section_id` but received {section_id!r}")
        if not topic_id:
            raise ValueError(f"Expected a non-empty value for `topic_id` but received {topic_id!r}")
        return await self._put(
            path_template(
                "/preferences/sections/{section_id}/topics/{topic_id}", section_id=section_id, topic_id=topic_id
            ),
            body=await async_maybe_transform(
                {
                    "default_status": default_status,
                    "name": name,
                    "allowed_preferences": allowed_preferences,
                    "description": description,
                    "include_unsubscribe_header": include_unsubscribe_header,
                    "routing_options": routing_options,
                    "topic_data": topic_data,
                },
                topic_replace_params.TopicReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WorkspacePreferenceTopicGetResponse,
        )


class TopicsResourceWithRawResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.create = to_raw_response_wrapper(
            topics.create,
        )
        self.retrieve = to_raw_response_wrapper(
            topics.retrieve,
        )
        self.list = to_raw_response_wrapper(
            topics.list,
        )
        self.archive = to_raw_response_wrapper(
            topics.archive,
        )
        self.replace = to_raw_response_wrapper(
            topics.replace,
        )


class AsyncTopicsResourceWithRawResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.create = async_to_raw_response_wrapper(
            topics.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            topics.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            topics.list,
        )
        self.archive = async_to_raw_response_wrapper(
            topics.archive,
        )
        self.replace = async_to_raw_response_wrapper(
            topics.replace,
        )


class TopicsResourceWithStreamingResponse:
    def __init__(self, topics: TopicsResource) -> None:
        self._topics = topics

        self.create = to_streamed_response_wrapper(
            topics.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            topics.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            topics.list,
        )
        self.archive = to_streamed_response_wrapper(
            topics.archive,
        )
        self.replace = to_streamed_response_wrapper(
            topics.replace,
        )


class AsyncTopicsResourceWithStreamingResponse:
    def __init__(self, topics: AsyncTopicsResource) -> None:
        self._topics = topics

        self.create = async_to_streamed_response_wrapper(
            topics.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            topics.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            topics.list,
        )
        self.archive = async_to_streamed_response_wrapper(
            topics.archive,
        )
        self.replace = async_to_streamed_response_wrapper(
            topics.replace,
        )
