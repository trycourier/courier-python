# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.tenants import template_list_params, template_publish_params, template_replace_params
from ....types.tenant_template_input_param import TenantTemplateInputParam
from ....types.put_tenant_template_response import PutTenantTemplateResponse
from ....types.tenants.template_list_response import TemplateListResponse
from ....types.base_template_tenant_association import BaseTemplateTenantAssociation
from ....types.post_tenant_template_publish_response import PostTenantTemplatePublishResponse

__all__ = ["TemplatesResource", "AsyncTemplatesResource"]


class TemplatesResource(SyncAPIResource):
    """
    Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
    """

    @cached_property
    def versions(self) -> VersionsResource:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return VersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return TemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return TemplatesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        template_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseTemplateTenantAssociation:
        """
        Returns a tenant's notification template with its content, version, and created,
        updated, and published timestamps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._get(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseTemplateTenantAssociation,
        )

    def list(
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
    ) -> TemplateListResponse:
        """
        Lists a tenant's notification templates, each carrying its version and published
        timestamp. Paged.

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of templates to return (defaults to 20, maximum value of 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return self._get(
            path_template("/tenants/{tenant_id}/templates", tenant_id=tenant_id),
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
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    def delete(
        self,
        template_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a tenant's notification template by id.

        Sends for that tenant then use
        the workspace template registered under the same id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def publish(
        self,
        template_id: str,
        *,
        tenant_id: str,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTenantTemplatePublishResponse:
        """
        Publishes a version of a tenant's notification template, making it the content
        that tenant's sends render from until you publish another.

        Args:
          version: The version of the template to publish (e.g., "v1", "v2", "latest"). If not
              provided, defaults to "latest".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._post(
            path_template(
                "/tenants/{tenant_id}/templates/{template_id}/publish", tenant_id=tenant_id, template_id=template_id
            ),
            body=maybe_transform({"version": version}, template_publish_params.TemplatePublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTenantTemplatePublishResponse,
        )

    def replace(
        self,
        template_id: str,
        *,
        tenant_id: str,
        template: TenantTemplateInputParam,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PutTenantTemplateResponse:
        """
        Creates or updates a notification template scoped to one tenant, letting a
        tenant override the content the workspace template would send.

        Args:
          template: Template configuration for creating or updating a tenant notification template

          published: Whether to publish the template immediately after saving. When true, the
              template becomes the active/published version. When false (default), the
              template is saved as a draft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return self._put(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            body=maybe_transform(
                {
                    "template": template,
                    "published": published,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PutTenantTemplateResponse,
        )


class AsyncTemplatesResource(AsyncAPIResource):
    """
    Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
    """

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return AsyncVersionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTemplatesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/trycourier/courier-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTemplatesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTemplatesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/trycourier/courier-python#with_streaming_response
        """
        return AsyncTemplatesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        template_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BaseTemplateTenantAssociation:
        """
        Returns a tenant's notification template with its content, version, and created,
        updated, and published timestamps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._get(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BaseTemplateTenantAssociation,
        )

    async def list(
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
    ) -> TemplateListResponse:
        """
        Lists a tenant's notification templates, each carrying its version and published
        timestamp. Paged.

        Args:
          cursor: Continue the pagination with the next cursor

          limit: The number of templates to return (defaults to 20, maximum value of 100)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        return await self._get(
            path_template("/tenants/{tenant_id}/templates", tenant_id=tenant_id),
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
                    template_list_params.TemplateListParams,
                ),
            ),
            cast_to=TemplateListResponse,
        )

    async def delete(
        self,
        template_id: str,
        *,
        tenant_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Deletes a tenant's notification template by id.

        Sends for that tenant then use
        the workspace template registered under the same id.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def publish(
        self,
        template_id: str,
        *,
        tenant_id: str,
        version: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PostTenantTemplatePublishResponse:
        """
        Publishes a version of a tenant's notification template, making it the content
        that tenant's sends render from until you publish another.

        Args:
          version: The version of the template to publish (e.g., "v1", "v2", "latest"). If not
              provided, defaults to "latest".

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._post(
            path_template(
                "/tenants/{tenant_id}/templates/{template_id}/publish", tenant_id=tenant_id, template_id=template_id
            ),
            body=await async_maybe_transform({"version": version}, template_publish_params.TemplatePublishParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PostTenantTemplatePublishResponse,
        )

    async def replace(
        self,
        template_id: str,
        *,
        tenant_id: str,
        template: TenantTemplateInputParam,
        published: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PutTenantTemplateResponse:
        """
        Creates or updates a notification template scoped to one tenant, letting a
        tenant override the content the workspace template would send.

        Args:
          template: Template configuration for creating or updating a tenant notification template

          published: Whether to publish the template immediately after saving. When true, the
              template becomes the active/published version. When false (default), the
              template is saved as a draft.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not tenant_id:
            raise ValueError(f"Expected a non-empty value for `tenant_id` but received {tenant_id!r}")
        if not template_id:
            raise ValueError(f"Expected a non-empty value for `template_id` but received {template_id!r}")
        return await self._put(
            path_template("/tenants/{tenant_id}/templates/{template_id}", tenant_id=tenant_id, template_id=template_id),
            body=await async_maybe_transform(
                {
                    "template": template,
                    "published": published,
                },
                template_replace_params.TemplateReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PutTenantTemplateResponse,
        )


class TemplatesResourceWithRawResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.retrieve = to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = to_raw_response_wrapper(
            templates.list,
        )
        self.delete = to_raw_response_wrapper(
            templates.delete,
        )
        self.publish = to_raw_response_wrapper(
            templates.publish,
        )
        self.replace = to_raw_response_wrapper(
            templates.replace,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return VersionsResourceWithRawResponse(self._templates.versions)


class AsyncTemplatesResourceWithRawResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.retrieve = async_to_raw_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            templates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            templates.delete,
        )
        self.publish = async_to_raw_response_wrapper(
            templates.publish,
        )
        self.replace = async_to_raw_response_wrapper(
            templates.replace,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return AsyncVersionsResourceWithRawResponse(self._templates.versions)


class TemplatesResourceWithStreamingResponse:
    def __init__(self, templates: TemplatesResource) -> None:
        self._templates = templates

        self.retrieve = to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = to_streamed_response_wrapper(
            templates.delete,
        )
        self.publish = to_streamed_response_wrapper(
            templates.publish,
        )
        self.replace = to_streamed_response_wrapper(
            templates.replace,
        )

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return VersionsResourceWithStreamingResponse(self._templates.versions)


class AsyncTemplatesResourceWithStreamingResponse:
    def __init__(self, templates: AsyncTemplatesResource) -> None:
        self._templates = templates

        self.retrieve = async_to_streamed_response_wrapper(
            templates.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            templates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            templates.delete,
        )
        self.publish = async_to_streamed_response_wrapper(
            templates.publish,
        )
        self.replace = async_to_streamed_response_wrapper(
            templates.replace,
        )

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        Manage the templates and template versions scoped to a single tenant, including the ones authored in the embedded designer.
        """
        return AsyncVersionsResourceWithStreamingResponse(self._templates.versions)
