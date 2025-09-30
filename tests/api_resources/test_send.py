# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from courier_docs import CourierDocs, AsyncCourierDocs
from courier_docs.types import SendSendMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_send_message(self, client: CourierDocs) -> None:
        send = client.send.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )
        assert_matches_type(SendSendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_send_message(self, client: CourierDocs) -> None:
        response = client.send.with_raw_response.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(SendSendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_send_message(self, client: CourierDocs) -> None:
        with client.send.with_streaming_response.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(SendSendMessageResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_send_message(self, async_client: AsyncCourierDocs) -> None:
        send = await async_client.send.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )
        assert_matches_type(SendSendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_send_message(self, async_client: AsyncCourierDocs) -> None:
        response = await async_client.send.with_raw_response.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(SendSendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_send_message(self, async_client: AsyncCourierDocs) -> None:
        async with async_client.send.with_streaming_response.send_message(
            message={
                "content": {
                    "elements": [{}],
                    "version": "version",
                }
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(SendSendMessageResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True
