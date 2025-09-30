# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import InboundTrackEventResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInbound:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_track_event(self, client: Courier) -> None:
        inbound = client.inbound.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        )
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_track_event_with_all_params(self, client: Courier) -> None:
        inbound = client.inbound.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
            user_id="1234",
        )
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_track_event(self, client: Courier) -> None:
        response = client.inbound.with_raw_response.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound = response.parse()
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_track_event(self, client: Courier) -> None:
        with client.inbound.with_streaming_response.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound = response.parse()
            assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInbound:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_track_event(self, async_client: AsyncCourier) -> None:
        inbound = await async_client.inbound.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        )
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_track_event_with_all_params(self, async_client: AsyncCourier) -> None:
        inbound = await async_client.inbound.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
            user_id="1234",
        )
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_track_event(self, async_client: AsyncCourier) -> None:
        response = await async_client.inbound.with_raw_response.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        inbound = await response.parse()
        assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_track_event(self, async_client: AsyncCourier) -> None:
        async with async_client.inbound.with_streaming_response.track_event(
            event="New Order Placed",
            message_id="4c62c457-b329-4bea-9bfc-17bba86c393f",
            properties={
                "order_id": "bar",
                "total_orders": "bar",
                "last_order_id": "bar",
            },
            type="track",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            inbound = await response.parse()
            assert_matches_type(InboundTrackEventResponse, inbound, path=["response"])

        assert cast(Any, response.is_closed) is True
