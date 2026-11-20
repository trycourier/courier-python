from __future__ import annotations

import httpx
import pytest

from courier import Courier, AsyncCourier


@pytest.mark.parametrize("prefix", ["/gateway", "/gateway/"])
@pytest.mark.parametrize("suffix", ["?workspace=demo", "?workspace=demo#section", "#section"])
def test_sync_base_url_components(prefix: str, suffix: str) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"id": "message-id"})

    with Courier(
        api_key="test-key",
        base_url=f"https://gateway.example{prefix}{suffix}",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        client.messages.retrieve("message-id")

    assert len(requests) == 1
    assert requests[0].url.path == "/gateway/messages/message-id"
    assert requests[0].url.params == httpx.QueryParams("workspace=demo" if "?" in suffix else "")
    assert requests[0].url.fragment == ("section" if "#" in suffix else "")


@pytest.mark.parametrize("prefix", ["/gateway", "/gateway/"])
@pytest.mark.parametrize("suffix", ["?workspace=demo", "?workspace=demo#section", "#section"])
async def test_async_base_url_components(prefix: str, suffix: str) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"id": "message-id"})

    async with AsyncCourier(
        api_key="test-key",
        base_url=f"https://gateway.example{prefix}{suffix}",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond)),
    ) as client:
        await client.messages.retrieve("message-id")

    assert len(requests) == 1
    assert requests[0].url.path == "/gateway/messages/message-id"
    assert requests[0].url.params == httpx.QueryParams("workspace=demo" if "?" in suffix else "")
    assert requests[0].url.fragment == ("section" if "#" in suffix else "")


@pytest.mark.parametrize(
    "endpoint, expected",
    [
        (
            "/messages/message-id?view=full",
            "https://gateway.example/gateway%2Ftenant/messages/message-id?workspace=demo&view=full",
        ),
        ("https://other.example/messages/message-id?view=full", "https://other.example/messages/message-id?view=full"),
    ],
)
def test_sync_request_query_and_absolute_url(endpoint: str, expected: str) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    with Courier(
        api_key="test-key",
        base_url="https://gateway.example/gateway%2Ftenant?workspace=demo",
        http_client=httpx.Client(transport=httpx.MockTransport(respond)),
    ) as client:
        client.get(endpoint, cast_to=object)

    assert requests[0].url == expected


@pytest.mark.parametrize(
    "endpoint, expected",
    [
        (
            "/messages/message-id?view=full",
            "https://gateway.example/gateway%2Ftenant/messages/message-id?workspace=demo&view=full",
        ),
        ("https://other.example/messages/message-id?view=full", "https://other.example/messages/message-id?view=full"),
    ],
)
async def test_async_request_query_and_absolute_url(endpoint: str, expected: str) -> None:
    requests: list[httpx.Request] = []

    def respond(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={})

    async with AsyncCourier(
        api_key="test-key",
        base_url="https://gateway.example/gateway%2Ftenant?workspace=demo",
        http_client=httpx.AsyncClient(transport=httpx.MockTransport(respond)),
    ) as client:
        await client.get(endpoint, cast_to=object)

    assert requests[0].url == expected
