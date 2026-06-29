# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    JourneyResponse,
    JourneysListResponse,
    CancelJourneyResponse,
    JourneysInvokeResponse,
    JourneyVersionsListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJourneys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        journey = client.journeys.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "trigger-1",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "send-1",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                },
            ],
            enabled=True,
            state="DRAFT",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        journey = client.journeys.retrieve(
            template_id="x",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.retrieve(
            template_id="x",
            version="published",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.retrieve(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.retrieve(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.retrieve(
                template_id="",
            )

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
    def test_method_archive(self, client: Courier) -> None:
        journey = client.journeys.archive(
            "x",
        )
        assert journey is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert journey is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert journey is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_overload_1(self, client: Courier) -> None:
        journey = client.journeys.cancel(
            cancelation_token="x",
        )
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_overload_1(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.cancel(
            cancelation_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_overload_1(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.cancel(
            cancelation_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(CancelJourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_overload_2(self, client: Courier) -> None:
        journey = client.journeys.cancel(
            run_id="x",
        )
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel_overload_2(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.cancel(
            run_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel_overload_2(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.cancel(
            run_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(CancelJourneyResponse, journey, path=["response"])

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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_versions(self, client: Courier) -> None:
        journey = client.journeys.list_versions(
            "x",
        )
        assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_versions(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.list_versions(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_versions(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.list_versions(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_versions(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.list_versions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish(self, client: Courier) -> None:
        journey = client.journeys.publish(
            template_id="x",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_publish_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.publish(
            template_id="x",
            version="v321669910225",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_publish(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.publish(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_publish(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.publish(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_publish(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.publish(
                template_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        journey = client.journeys.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        journey = client.journeys.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "x",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                }
            ],
            enabled=True,
            state="DRAFT",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.journeys.with_raw_response.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.journeys.with_streaming_response.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            client.journeys.with_raw_response.replace(
                template_id="",
                name="Welcome Journey v2",
                nodes=[
                    {
                        "trigger_type": "api-invoke",
                        "type": "trigger",
                    }
                ],
            )


class TestAsyncJourneys:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "trigger-1",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "send-1",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                },
            ],
            enabled=True,
            state="DRAFT",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.create(
            name="Welcome Journey",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                },
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.retrieve(
            template_id="x",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.retrieve(
            template_id="x",
            version="published",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.retrieve(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.retrieve(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.retrieve(
                template_id="",
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
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.archive(
            "x",
        )
        assert journey is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.archive(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert journey is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.archive(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert journey is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_overload_1(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.cancel(
            cancelation_token="x",
        )
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_overload_1(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.cancel(
            cancelation_token="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_overload_1(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.cancel(
            cancelation_token="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(CancelJourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_overload_2(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.cancel(
            run_id="x",
        )
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel_overload_2(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.cancel(
            run_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(CancelJourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel_overload_2(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.cancel(
            run_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(CancelJourneyResponse, journey, path=["response"])

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

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_versions(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.list_versions(
            "x",
        )
        assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_versions(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.list_versions(
            "x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_versions(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.list_versions(
            "x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneyVersionsListResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_versions(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.list_versions(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.publish(
            template_id="x",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_publish_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.publish(
            template_id="x",
            version="v321669910225",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_publish(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.publish(
            template_id="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_publish(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.publish(
            template_id="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_publish(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.publish(
                template_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        journey = await async_client.journeys.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                    "id": "x",
                    "conditions": ["string", "string"],
                    "schema": {"foo": "bar"},
                }
            ],
            enabled=True,
            state="DRAFT",
        )
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.journeys.with_raw_response.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        journey = await response.parse()
        assert_matches_type(JourneyResponse, journey, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.journeys.with_streaming_response.replace(
            template_id="x",
            name="Welcome Journey v2",
            nodes=[
                {
                    "trigger_type": "api-invoke",
                    "type": "trigger",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            journey = await response.parse()
            assert_matches_type(JourneyResponse, journey, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `template_id` but received ''"):
            await async_client.journeys.with_raw_response.replace(
                template_id="",
                name="Welcome Journey v2",
                nodes=[
                    {
                        "trigger_type": "api-invoke",
                        "type": "trigger",
                    }
                ],
            )
