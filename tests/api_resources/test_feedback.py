# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import FeedbackCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        feedback = client.feedback.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        feedback = client.feedback.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
            expected_behavior="Every page before the last one contains at least one item.",
            harness="Claude Code",
            location="GET /lists/{list_id}/subscriptions",
            model="claude-opus-5-5",
            request_id="1-67f340b1-58b7b231d9485ef0cda0a38b",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.feedback.with_raw_response.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.feedback.with_streaming_response.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        feedback = await async_client.feedback.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        feedback = await async_client.feedback.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
            expected_behavior="Every page before the last one contains at least one item.",
            harness="Claude Code",
            location="GET /lists/{list_id}/subscriptions",
            model="claude-opus-5-5",
            request_id="1-67f340b1-58b7b231d9485ef0cda0a38b",
        )
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.feedback.with_raw_response.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.feedback.with_streaming_response.create(
            category="possible_bug",
            description="GET /lists/{list_id}/subscriptions returned items: [] with paging.more set to true, and following the cursor returned the remaining subscribers.",
            surface="api",
            title="List subscriptions returns an empty page with a next cursor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackCreateResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
