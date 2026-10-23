# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import (
    is_given,
    is_mapping_t,
    get_async_library,
)
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import CourierError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        auth,
        bulk,
        send,
        lists,
        users,
        brands,
        digests,
        inbound,
        tenants,
        journeys,
        messages,
        previews,
        profiles,
        requests,
        audiences,
        providers,
        broadcasts,
        automations,
        audit_events,
        translations,
        notifications,
        routing_strategies,
        workspace_preferences,
    )
    from .resources.auth import AuthResource, AsyncAuthResource
    from .resources.bulk import BulkResource, AsyncBulkResource
    from .resources.send import SendResource, AsyncSendResource
    from .resources.brands import BrandsResource, AsyncBrandsResource
    from .resources.inbound import InboundResource, AsyncInboundResource
    from .resources.messages import MessagesResource, AsyncMessagesResource
    from .resources.previews import PreviewsResource, AsyncPreviewsResource
    from .resources.requests import RequestsResource, AsyncRequestsResource
    from .resources.audiences import AudiencesResource, AsyncAudiencesResource
    from .resources.broadcasts import BroadcastsResource, AsyncBroadcastsResource
    from .resources.lists.lists import ListsResource, AsyncListsResource
    from .resources.users.users import UsersResource, AsyncUsersResource
    from .resources.audit_events import AuditEventsResource, AsyncAuditEventsResource
    from .resources.translations import TranslationsResource, AsyncTranslationsResource
    from .resources.digests.digests import DigestsResource, AsyncDigestsResource
    from .resources.tenants.tenants import TenantsResource, AsyncTenantsResource
    from .resources.journeys.journeys import JourneysResource, AsyncJourneysResource
    from .resources.profiles.profiles import ProfilesResource, AsyncProfilesResource
    from .resources.routing_strategies import RoutingStrategiesResource, AsyncRoutingStrategiesResource
    from .resources.providers.providers import ProvidersResource, AsyncProvidersResource
    from .resources.automations.automations import AutomationsResource, AsyncAutomationsResource
    from .resources.notifications.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.workspace_preferences.workspace_preferences import (
        WorkspacePreferencesResource,
        AsyncWorkspacePreferencesResource,
    )

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Courier", "AsyncCourier", "Client", "AsyncClient"]


class Courier(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Courier client instance.

        This automatically infers the `api_key` argument from the `COURIER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COURIER_API_KEY")
        if api_key is None:
            raise CourierError(
                "The api_key client option must be set either by passing api_key to the client or by setting the COURIER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("COURIER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.courier.com"

        custom_headers_env = os.environ.get("COURIER_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def send(self) -> SendResource:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.SendResource(self)

    @cached_property
    def audiences(self) -> AudiencesResource:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AudiencesResource(self)

    @cached_property
    def providers(self) -> ProvidersResource:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.ProvidersResource(self)

    @cached_property
    def audit_events(self) -> AuditEventsResource:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AuditEventsResource(self)

    @cached_property
    def auth(self) -> AuthResource:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AuthResource(self)

    @cached_property
    def automations(self) -> AutomationsResource:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AutomationsResource(self)

    @cached_property
    def journeys(self) -> JourneysResource:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.JourneysResource(self)

    @cached_property
    def broadcasts(self) -> BroadcastsResource:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.BroadcastsResource(self)

    @cached_property
    def previews(self) -> PreviewsResource:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.PreviewsResource(self)

    @cached_property
    def bulk(self) -> BulkResource:
        from .resources import bulk

        return bulk.BulkResource(self)

    @cached_property
    def brands(self) -> BrandsResource:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.BrandsResource(self)

    @cached_property
    def digests(self) -> DigestsResource:
        from .resources import digests

        return digests.DigestsResource(self)

    @cached_property
    def inbound(self) -> InboundResource:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.InboundResource(self)

    @cached_property
    def lists(self) -> ListsResource:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.ListsResource(self)

    @cached_property
    def messages(self) -> MessagesResource:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.MessagesResource(self)

    @cached_property
    def requests(self) -> RequestsResource:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.RequestsResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.NotificationsResource(self)

    @cached_property
    def routing_strategies(self) -> RoutingStrategiesResource:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.RoutingStrategiesResource(self)

    @cached_property
    def workspace_preferences(self) -> WorkspacePreferencesResource:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.WorkspacePreferencesResource(self)

    @cached_property
    def profiles(self) -> ProfilesResource:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.ProfilesResource(self)

    @cached_property
    def tenants(self) -> TenantsResource:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.TenantsResource(self)

    @cached_property
    def translations(self) -> TranslationsResource:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.TranslationsResource(self)

    @cached_property
    def users(self) -> UsersResource:
        from .resources import users

        return users.UsersResource(self)

    @cached_property
    def with_raw_response(self) -> CourierWithRawResponse:
        return CourierWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CourierWithStreamedResponse:
        return CourierWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncCourier(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncCourier client instance.

        This automatically infers the `api_key` argument from the `COURIER_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("COURIER_API_KEY")
        if api_key is None:
            raise CourierError(
                "The api_key client option must be set either by passing api_key to the client or by setting the COURIER_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("COURIER_BASE_URL")
        if base_url is None:
            base_url = f"https://api.courier.com"

        custom_headers_env = os.environ.get("COURIER_CUSTOM_HEADERS")
        if custom_headers_env is not None:
            parsed: dict[str, str] = {}
            for line in custom_headers_env.split("\n"):
                colon = line.find(":")
                if colon >= 0:
                    parsed[line[:colon].strip()] = line[colon + 1 :].strip()
            default_headers = {**parsed, **(default_headers if is_mapping_t(default_headers) else {})}

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def send(self) -> AsyncSendResource:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.AsyncSendResource(self)

    @cached_property
    def audiences(self) -> AsyncAudiencesResource:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AsyncAudiencesResource(self)

    @cached_property
    def providers(self) -> AsyncProvidersResource:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.AsyncProvidersResource(self)

    @cached_property
    def audit_events(self) -> AsyncAuditEventsResource:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AsyncAuditEventsResource(self)

    @cached_property
    def auth(self) -> AsyncAuthResource:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AsyncAuthResource(self)

    @cached_property
    def automations(self) -> AsyncAutomationsResource:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AsyncAutomationsResource(self)

    @cached_property
    def journeys(self) -> AsyncJourneysResource:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.AsyncJourneysResource(self)

    @cached_property
    def broadcasts(self) -> AsyncBroadcastsResource:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.AsyncBroadcastsResource(self)

    @cached_property
    def previews(self) -> AsyncPreviewsResource:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.AsyncPreviewsResource(self)

    @cached_property
    def bulk(self) -> AsyncBulkResource:
        from .resources import bulk

        return bulk.AsyncBulkResource(self)

    @cached_property
    def brands(self) -> AsyncBrandsResource:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.AsyncBrandsResource(self)

    @cached_property
    def digests(self) -> AsyncDigestsResource:
        from .resources import digests

        return digests.AsyncDigestsResource(self)

    @cached_property
    def inbound(self) -> AsyncInboundResource:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.AsyncInboundResource(self)

    @cached_property
    def lists(self) -> AsyncListsResource:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.AsyncListsResource(self)

    @cached_property
    def messages(self) -> AsyncMessagesResource:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.AsyncMessagesResource(self)

    @cached_property
    def requests(self) -> AsyncRequestsResource:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.AsyncRequestsResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.AsyncNotificationsResource(self)

    @cached_property
    def routing_strategies(self) -> AsyncRoutingStrategiesResource:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.AsyncRoutingStrategiesResource(self)

    @cached_property
    def workspace_preferences(self) -> AsyncWorkspacePreferencesResource:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.AsyncWorkspacePreferencesResource(self)

    @cached_property
    def profiles(self) -> AsyncProfilesResource:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.AsyncProfilesResource(self)

    @cached_property
    def tenants(self) -> AsyncTenantsResource:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.AsyncTenantsResource(self)

    @cached_property
    def translations(self) -> AsyncTranslationsResource:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.AsyncTranslationsResource(self)

    @cached_property
    def users(self) -> AsyncUsersResource:
        from .resources import users

        return users.AsyncUsersResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncCourierWithRawResponse:
        return AsyncCourierWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCourierWithStreamedResponse:
        return AsyncCourierWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class CourierWithRawResponse:
    _client: Courier

    def __init__(self, client: Courier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.SendResourceWithRawResponse:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.SendResourceWithRawResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithRawResponse:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithRawResponse:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.ProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithRawResponse:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AuthResourceWithRawResponse:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AutomationsResourceWithRawResponse:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AutomationsResourceWithRawResponse(self._client.automations)

    @cached_property
    def journeys(self) -> journeys.JourneysResourceWithRawResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.JourneysResourceWithRawResponse(self._client.journeys)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithRawResponse:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.BroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def previews(self) -> previews.PreviewsResourceWithRawResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.PreviewsResourceWithRawResponse(self._client.previews)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithRawResponse:
        from .resources import bulk

        return bulk.BulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithRawResponse:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.BrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def digests(self) -> digests.DigestsResourceWithRawResponse:
        from .resources import digests

        return digests.DigestsResourceWithRawResponse(self._client.digests)

    @cached_property
    def inbound(self) -> inbound.InboundResourceWithRawResponse:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.InboundResourceWithRawResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.ListsResourceWithRawResponse:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.ListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithRawResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.MessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithRawResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.RequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def routing_strategies(self) -> routing_strategies.RoutingStrategiesResourceWithRawResponse:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.RoutingStrategiesResourceWithRawResponse(self._client.routing_strategies)

    @cached_property
    def workspace_preferences(self) -> workspace_preferences.WorkspacePreferencesResourceWithRawResponse:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.WorkspacePreferencesResourceWithRawResponse(self._client.workspace_preferences)

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithRawResponse:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.ProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithRawResponse:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.TenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithRawResponse:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.TranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def users(self) -> users.UsersResourceWithRawResponse:
        from .resources import users

        return users.UsersResourceWithRawResponse(self._client.users)


class AsyncCourierWithRawResponse:
    _client: AsyncCourier

    def __init__(self, client: AsyncCourier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.AsyncSendResourceWithRawResponse:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.AsyncSendResourceWithRawResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithRawResponse:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AsyncAudiencesResourceWithRawResponse(self._client.audiences)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithRawResponse:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.AsyncProvidersResourceWithRawResponse(self._client.providers)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithRawResponse:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AsyncAuditEventsResourceWithRawResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithRawResponse:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AsyncAuthResourceWithRawResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AsyncAutomationsResourceWithRawResponse:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AsyncAutomationsResourceWithRawResponse(self._client.automations)

    @cached_property
    def journeys(self) -> journeys.AsyncJourneysResourceWithRawResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.AsyncJourneysResourceWithRawResponse(self._client.journeys)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithRawResponse:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.AsyncBroadcastsResourceWithRawResponse(self._client.broadcasts)

    @cached_property
    def previews(self) -> previews.AsyncPreviewsResourceWithRawResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.AsyncPreviewsResourceWithRawResponse(self._client.previews)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithRawResponse:
        from .resources import bulk

        return bulk.AsyncBulkResourceWithRawResponse(self._client.bulk)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithRawResponse:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.AsyncBrandsResourceWithRawResponse(self._client.brands)

    @cached_property
    def digests(self) -> digests.AsyncDigestsResourceWithRawResponse:
        from .resources import digests

        return digests.AsyncDigestsResourceWithRawResponse(self._client.digests)

    @cached_property
    def inbound(self) -> inbound.AsyncInboundResourceWithRawResponse:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.AsyncInboundResourceWithRawResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithRawResponse:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.AsyncListsResourceWithRawResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithRawResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.AsyncMessagesResourceWithRawResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithRawResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.AsyncRequestsResourceWithRawResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def routing_strategies(self) -> routing_strategies.AsyncRoutingStrategiesResourceWithRawResponse:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.AsyncRoutingStrategiesResourceWithRawResponse(self._client.routing_strategies)

    @cached_property
    def workspace_preferences(self) -> workspace_preferences.AsyncWorkspacePreferencesResourceWithRawResponse:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.AsyncWorkspacePreferencesResourceWithRawResponse(
            self._client.workspace_preferences
        )

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithRawResponse:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.AsyncProfilesResourceWithRawResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithRawResponse:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.AsyncTenantsResourceWithRawResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithRawResponse:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.AsyncTranslationsResourceWithRawResponse(self._client.translations)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithRawResponse:
        from .resources import users

        return users.AsyncUsersResourceWithRawResponse(self._client.users)


class CourierWithStreamedResponse:
    _client: Courier

    def __init__(self, client: Courier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.SendResourceWithStreamingResponse:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.SendResourceWithStreamingResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AudiencesResourceWithStreamingResponse:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def providers(self) -> providers.ProvidersResourceWithStreamingResponse:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.ProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def audit_events(self) -> audit_events.AuditEventsResourceWithStreamingResponse:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AuthResourceWithStreamingResponse:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AutomationsResourceWithStreamingResponse:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AutomationsResourceWithStreamingResponse(self._client.automations)

    @cached_property
    def journeys(self) -> journeys.JourneysResourceWithStreamingResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.JourneysResourceWithStreamingResponse(self._client.journeys)

    @cached_property
    def broadcasts(self) -> broadcasts.BroadcastsResourceWithStreamingResponse:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.BroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def previews(self) -> previews.PreviewsResourceWithStreamingResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.PreviewsResourceWithStreamingResponse(self._client.previews)

    @cached_property
    def bulk(self) -> bulk.BulkResourceWithStreamingResponse:
        from .resources import bulk

        return bulk.BulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def brands(self) -> brands.BrandsResourceWithStreamingResponse:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.BrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def digests(self) -> digests.DigestsResourceWithStreamingResponse:
        from .resources import digests

        return digests.DigestsResourceWithStreamingResponse(self._client.digests)

    @cached_property
    def inbound(self) -> inbound.InboundResourceWithStreamingResponse:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.InboundResourceWithStreamingResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.ListsResourceWithStreamingResponse:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.ListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.MessagesResourceWithStreamingResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.MessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.RequestsResourceWithStreamingResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.RequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def routing_strategies(self) -> routing_strategies.RoutingStrategiesResourceWithStreamingResponse:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.RoutingStrategiesResourceWithStreamingResponse(self._client.routing_strategies)

    @cached_property
    def workspace_preferences(self) -> workspace_preferences.WorkspacePreferencesResourceWithStreamingResponse:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.WorkspacePreferencesResourceWithStreamingResponse(
            self._client.workspace_preferences
        )

    @cached_property
    def profiles(self) -> profiles.ProfilesResourceWithStreamingResponse:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.ProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.TenantsResourceWithStreamingResponse:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.TenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.TranslationsResourceWithStreamingResponse:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.TranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def users(self) -> users.UsersResourceWithStreamingResponse:
        from .resources import users

        return users.UsersResourceWithStreamingResponse(self._client.users)


class AsyncCourierWithStreamedResponse:
    _client: AsyncCourier

    def __init__(self, client: AsyncCourier) -> None:
        self._client = client

    @cached_property
    def send(self) -> send.AsyncSendResourceWithStreamingResponse:
        """
        Send a message to one or more recipients — users, lists, audiences, or tenants — across every channel you have configured.
        """
        from .resources import send

        return send.AsyncSendResourceWithStreamingResponse(self._client.send)

    @cached_property
    def audiences(self) -> audiences.AsyncAudiencesResourceWithStreamingResponse:
        """
        Define filter-based groups whose membership Courier recalculates as user profiles change.
        """
        from .resources import audiences

        return audiences.AsyncAudiencesResourceWithStreamingResponse(self._client.audiences)

    @cached_property
    def providers(self) -> providers.AsyncProvidersResourceWithStreamingResponse:
        """
        Configure the channel providers Courier delivers through, and browse the provider types it supports.
        """
        from .resources import providers

        return providers.AsyncProvidersResourceWithStreamingResponse(self._client.providers)

    @cached_property
    def audit_events(self) -> audit_events.AsyncAuditEventsResourceWithStreamingResponse:
        """Read the audit trail of configuration and access changes in your workspace."""
        from .resources import audit_events

        return audit_events.AsyncAuditEventsResourceWithStreamingResponse(self._client.audit_events)

    @cached_property
    def auth(self) -> auth.AsyncAuthResourceWithStreamingResponse:
        """
        Issue scoped, short-lived JWTs so client-side SDKs — Inbox, Preferences, and the embedded designer — can call Courier as a single user. Server-side requests authenticate with your workspace API key instead.
        """
        from .resources import auth

        return auth.AsyncAuthResourceWithStreamingResponse(self._client.auth)

    @cached_property
    def automations(self) -> automations.AsyncAutomationsResourceWithStreamingResponse:
        """
        Invoke a stored automation template or an ad hoc automation defined in the request.
        """
        from .resources import automations

        return automations.AsyncAutomationsResourceWithStreamingResponse(self._client.automations)

    @cached_property
    def journeys(self) -> journeys.AsyncJourneysResourceWithStreamingResponse:
        """
        Build, version, publish, invoke, and cancel multi-step notification workflows, along with the templates scoped to them.
        """
        from .resources import journeys

        return journeys.AsyncJourneysResourceWithStreamingResponse(self._client.journeys)

    @cached_property
    def broadcasts(self) -> broadcasts.AsyncBroadcastsResourceWithStreamingResponse:
        """
        Create a one-off send to a list or audience, author its content, then send it immediately or schedule it for later.
        """
        from .resources import broadcasts

        return broadcasts.AsyncBroadcastsResourceWithStreamingResponse(self._client.broadcasts)

    @cached_property
    def previews(self) -> previews.AsyncPreviewsResourceWithStreamingResponse:
        """
        Render a template's email content on real email clients and read back the screenshots, so you can check how it looks before you send it.
        """
        from .resources import previews

        return previews.AsyncPreviewsResourceWithStreamingResponse(self._client.previews)

    @cached_property
    def bulk(self) -> bulk.AsyncBulkResourceWithStreamingResponse:
        from .resources import bulk

        return bulk.AsyncBulkResourceWithStreamingResponse(self._client.bulk)

    @cached_property
    def brands(self) -> brands.AsyncBrandsResourceWithStreamingResponse:
        """
        Manage the logos, colors, and layout that give the templates you send a consistent look.
        """
        from .resources import brands

        return brands.AsyncBrandsResourceWithStreamingResponse(self._client.brands)

    @cached_property
    def digests(self) -> digests.AsyncDigestsResourceWithStreamingResponse:
        from .resources import digests

        return digests.AsyncDigestsResourceWithStreamingResponse(self._client.digests)

    @cached_property
    def inbound(self) -> inbound.AsyncInboundResourceWithStreamingResponse:
        """
        Record an inbound event that triggers the journeys and automations mapped to it.
        """
        from .resources import inbound

        return inbound.AsyncInboundResourceWithStreamingResponse(self._client.inbound)

    @cached_property
    def lists(self) -> lists.AsyncListsResourceWithStreamingResponse:
        """
        Manage static groups of users that you subscribe explicitly, and send to them by list id or list pattern.
        """
        from .resources import lists

        return lists.AsyncListsResourceWithStreamingResponse(self._client.lists)

    @cached_property
    def messages(self) -> messages.AsyncMessagesResourceWithStreamingResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import messages

        return messages.AsyncMessagesResourceWithStreamingResponse(self._client.messages)

    @cached_property
    def requests(self) -> requests.AsyncRequestsResourceWithStreamingResponse:
        """
        Look up the messages Courier has accepted, inspect their delivery history and rendered output, and cancel, resend, or archive them.
        """
        from .resources import requests

        return requests.AsyncRequestsResourceWithStreamingResponse(self._client.requests)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        """
        Create, update, version, publish, and localize notification templates and their content.
        """
        from .resources import notifications

        return notifications.AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def routing_strategies(self) -> routing_strategies.AsyncRoutingStrategiesResourceWithStreamingResponse:
        """
        Define reusable channel routing and failover strategies, and see which templates use them.
        """
        from .resources import routing_strategies

        return routing_strategies.AsyncRoutingStrategiesResourceWithStreamingResponse(self._client.routing_strategies)

    @cached_property
    def workspace_preferences(self) -> workspace_preferences.AsyncWorkspacePreferencesResourceWithStreamingResponse:
        """
        Manage the workspace catalog of subscription topics, the sections that group them, and publishing the preference page.
        """
        from .resources import workspace_preferences

        return workspace_preferences.AsyncWorkspacePreferencesResourceWithStreamingResponse(
            self._client.workspace_preferences
        )

    @cached_property
    def profiles(self) -> profiles.AsyncProfilesResourceWithStreamingResponse:
        """
        Store the contact information Courier delivers to for each user — email, phone number, push tokens, and any custom data you send to.
        """
        from .resources import profiles

        return profiles.AsyncProfilesResourceWithStreamingResponse(self._client.profiles)

    @cached_property
    def tenants(self) -> tenants.AsyncTenantsResourceWithStreamingResponse:
        """
        Manage tenants — the organizations, teams, or accounts your users belong to — along with their users and default preferences.
        """
        from .resources import tenants

        return tenants.AsyncTenantsResourceWithStreamingResponse(self._client.tenants)

    @cached_property
    def translations(self) -> translations.AsyncTranslationsResourceWithStreamingResponse:
        """
        Store and retrieve the translation strings Courier uses to render localized template content.
        """
        from .resources import translations

        return translations.AsyncTranslationsResourceWithStreamingResponse(self._client.translations)

    @cached_property
    def users(self) -> users.AsyncUsersResourceWithStreamingResponse:
        from .resources import users

        return users.AsyncUsersResourceWithStreamingResponse(self._client.users)


Client = Courier

AsyncClient = AsyncCourier
