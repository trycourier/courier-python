# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import JourneysListResponse, JourneysInvokeResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJourneys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        journey = client.journeys.list()
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.list(
            cursor="cursor",
            version="published",
        )
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneysListResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invoke(self, client: Courier) -> None:
        journey = client.journeys.invoke(
            template_id="templateId",
        )
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_invoke_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.invoke(
            template_id="templateId",
            data={
                "order_id": "bar",
                "amount": "bar",
            },
            profile={"foo": "bar"},
            user_id="user-123",
        )
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_invoke(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.invoke(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_invoke(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.invoke(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_invoke(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.invoke(
                template_id="",
            )


class TestAsyncJourneys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.list()
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.list(
            cursor="cursor",
            version="published",
        )
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneysListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneysListResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invoke(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.invoke(
            template_id="templateId",
        )
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_invoke_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.invoke(
            template_id="templateId",
            data={
                "order_id": "bar",
                "amount": "bar",
            },
            profile={"foo": "bar"},
            user_id="user-123",
        )
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_invoke(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.invoke(
            template_id="templateId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_invoke(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.invoke(
            template_id="templateId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneysInvokeResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_invoke(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.invoke(
                template_id="",
            )
