# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

import httpx

from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .core.jsonable_encoder import jsonable_encoder
from .environment import CourierEnvironment
from .resources.audiences.client import AsyncAudiencesClient, AudiencesClient
from .resources.audit_events.client import AsyncAuditEventsClient, AuditEventsClient
from .resources.auth_tokens.client import AsyncAuthTokensClient, AuthTokensClient
from .resources.automations.client import AsyncAutomationsClient, AutomationsClient
from .resources.brands.client import AsyncBrandsClient, BrandsClient
from .resources.bulk.client import AsyncBulkClient, BulkClient
from .resources.lists.client import AsyncListsClient, ListsClient
from .resources.messages.client import AsyncMessagesClient, MessagesClient
from .resources.notifications.client import AsyncNotificationsClient, NotificationsClient
from .resources.profiles.client import AsyncProfilesClient, ProfilesClient
from .resources.send.types.message import Message
from .resources.templates.client import AsyncTemplatesClient, TemplatesClient
from .resources.tenants.client import AsyncTenantsClient, TenantsClient
from .resources.translations.client import AsyncTranslationsClient, TranslationsClient
from .resources.users.client import AsyncUsersClient, UsersClient
from .types.send_message_response import SendMessageResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class Courier:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CourierEnvironment = CourierEnvironment.PRODUCTION,
        authorization_token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.Client] = None,
    ):
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization_token=authorization_token,
            httpx_client=httpx.Client(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.audiences = AudiencesClient(client_wrapper=self._client_wrapper)
        self.audit_events = AuditEventsClient(client_wrapper=self._client_wrapper)
        self.auth_tokens = AuthTokensClient(client_wrapper=self._client_wrapper)
        self.automations = AutomationsClient(client_wrapper=self._client_wrapper)
        self.brands = BrandsClient(client_wrapper=self._client_wrapper)
        self.bulk = BulkClient(client_wrapper=self._client_wrapper)
        self.lists = ListsClient(client_wrapper=self._client_wrapper)
        self.messages = MessagesClient(client_wrapper=self._client_wrapper)
        self.notifications = NotificationsClient(client_wrapper=self._client_wrapper)
        self.profiles = ProfilesClient(client_wrapper=self._client_wrapper)
        self.templates = TemplatesClient(client_wrapper=self._client_wrapper)
        self.tenants = TenantsClient(client_wrapper=self._client_wrapper)
        self.translations = TranslationsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)

    def send(self, *, message: Message) -> SendMessageResponse:
        """
        Use the send API to send a message to one or more recipients.

        Parameters:
            - message: Message. Defines the message to be delivered
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "send"),
            json=jsonable_encoder({"message": message}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SendMessageResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCourier:
    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: CourierEnvironment = CourierEnvironment.PRODUCTION,
        authorization_token: typing.Union[str, typing.Callable[[], str]],
        timeout: typing.Optional[float] = 60,
        httpx_client: typing.Optional[httpx.AsyncClient] = None,
    ):
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            authorization_token=authorization_token,
            httpx_client=httpx.AsyncClient(timeout=timeout) if httpx_client is None else httpx_client,
        )
        self.audiences = AsyncAudiencesClient(client_wrapper=self._client_wrapper)
        self.audit_events = AsyncAuditEventsClient(client_wrapper=self._client_wrapper)
        self.auth_tokens = AsyncAuthTokensClient(client_wrapper=self._client_wrapper)
        self.automations = AsyncAutomationsClient(client_wrapper=self._client_wrapper)
        self.brands = AsyncBrandsClient(client_wrapper=self._client_wrapper)
        self.bulk = AsyncBulkClient(client_wrapper=self._client_wrapper)
        self.lists = AsyncListsClient(client_wrapper=self._client_wrapper)
        self.messages = AsyncMessagesClient(client_wrapper=self._client_wrapper)
        self.notifications = AsyncNotificationsClient(client_wrapper=self._client_wrapper)
        self.profiles = AsyncProfilesClient(client_wrapper=self._client_wrapper)
        self.templates = AsyncTemplatesClient(client_wrapper=self._client_wrapper)
        self.tenants = AsyncTenantsClient(client_wrapper=self._client_wrapper)
        self.translations = AsyncTranslationsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)

    async def send(self, *, message: Message) -> SendMessageResponse:
        """
        Use the send API to send a message to one or more recipients.

        Parameters:
            - message: Message. Defines the message to be delivered
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", "send"),
            json=jsonable_encoder({"message": message}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(SendMessageResponse, _response.json())  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: CourierEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
