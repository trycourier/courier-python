# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    Broadcast,
    BroadcastListResponse,
    NotificationContentGetResponse,
    NotificationContentMutationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBroadcasts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        broadcast = client.broadcasts.create(
            channel="email",
            name="Spring Sale Announcement",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.create(
            channel="email",
            name="Spring Sale Announcement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.create(
            channel="email",
            name="Spring Sale Announcement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        broadcast = client.broadcasts.retrieve(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.retrieve(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.retrieve(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        broadcast = client.broadcasts.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.update(
                broadcast_id="",
                name="Spring Sale Announcement (v2)",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        broadcast = client.broadcasts.list()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        broadcast = client.broadcasts.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        broadcast = client.broadcasts.archive(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.archive(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.archive(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Courier) -> None:
        broadcast = client.broadcasts.cancel(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.cancel(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.cancel(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_duplicate(self, client: Courier) -> None:
        broadcast = client.broadcasts.duplicate(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_duplicate(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.duplicate(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_duplicate(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.duplicate(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_duplicate(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.duplicate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_content(self, client: Courier) -> None:
        broadcast = client.broadcasts.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        )
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_put_content_with_all_params(self, client: Courier) -> None:
        broadcast = client.broadcasts.put_content(
            broadcast_id="broadcastId",
            content={
                "elements": [
                    {
                        "channels": ["string"],
                        "if": "if",
                        "loop": "loop",
                        "ref": "ref",
                        "type": "meta",
                    },
                    {
                        "channels": ["string"],
                        "if": "if",
                        "loop": "loop",
                        "ref": "ref",
                        "type": "text",
                    },
                ],
                "version": "2022-01-01",
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_put_content(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_put_content(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_put_content(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.put_content(
                broadcast_id="",
                content={"elements": [{}, {}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_content(self, client: Courier) -> None:
        broadcast = client.broadcasts.retrieve_content(
            broadcast_id="broadcastId",
        )
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_content_with_all_params(self, client: Courier) -> None:
        broadcast = client.broadcasts.retrieve_content(
            broadcast_id="broadcastId",
            version="version",
        )
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_content(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.retrieve_content(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_content(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.retrieve_content(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_content(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.retrieve_content(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule(self, client: Courier) -> None:
        broadcast = client.broadcasts.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_schedule_with_all_params(self, client: Courier) -> None:
        broadcast = client.broadcasts.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
            timezone="America/New_York",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_schedule(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_schedule(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_schedule(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.schedule(
                broadcast_id="",
                recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
                recipient_type="audience",
                scheduled_to="2026-08-01T15:00:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_send(self, client: Courier) -> None:
        broadcast = client.broadcasts.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_send(self, client: Courier) -> None:
        response = client.broadcasts.with_raw_response.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_send(self, client: Courier) -> None:
        with client.broadcasts.with_streaming_response.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_send(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            client.broadcasts.with_raw_response.send(
                broadcast_id="",
                recipient_id="cool-customers",
                recipient_type="list",
            )


class TestAsyncBroadcasts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.create(
            channel="email",
            name="Spring Sale Announcement",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.create(
            channel="email",
            name="Spring Sale Announcement",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.create(
            channel="email",
            name="Spring Sale Announcement",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.retrieve(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.retrieve(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.retrieve(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.update(
            broadcast_id="broadcastId",
            name="Spring Sale Announcement (v2)",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.update(
                broadcast_id="",
                name="Spring Sale Announcement (v2)",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.list()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(BroadcastListResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.archive(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.archive(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.archive(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.cancel(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.cancel(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.cancel(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.cancel(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_duplicate(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.duplicate(
            "broadcastId",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_duplicate(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.duplicate(
            "broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_duplicate(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.duplicate(
            "broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_duplicate(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.duplicate(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_content(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        )
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_put_content_with_all_params(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.put_content(
            broadcast_id="broadcastId",
            content={
                "elements": [
                    {
                        "channels": ["string"],
                        "if": "if",
                        "loop": "loop",
                        "ref": "ref",
                        "type": "meta",
                    },
                    {
                        "channels": ["string"],
                        "if": "if",
                        "loop": "loop",
                        "ref": "ref",
                        "type": "text",
                    },
                ],
                "version": "2022-01-01",
            },
            state="DRAFT",
        )
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_put_content(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_put_content(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.put_content(
            broadcast_id="broadcastId",
            content={"elements": [{}, {}]},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(NotificationContentMutationResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_put_content(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.put_content(
                broadcast_id="",
                content={"elements": [{}, {}]},
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_content(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.retrieve_content(
            broadcast_id="broadcastId",
        )
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_content_with_all_params(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.retrieve_content(
            broadcast_id="broadcastId",
            version="version",
        )
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_content(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.retrieve_content(
            broadcast_id="broadcastId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_content(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.retrieve_content(
            broadcast_id="broadcastId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(NotificationContentGetResponse, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_content(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.retrieve_content(
                broadcast_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_schedule_with_all_params(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
            timezone="America/New_York",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_schedule(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_schedule(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.schedule(
            broadcast_id="broadcastId",
            recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
            recipient_type="audience",
            scheduled_to="2026-08-01T15:00:00",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_schedule(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.schedule(
                broadcast_id="",
                recipient_id="aud_01kx4h2jdafq8bk9amzvy6hbv0",
                recipient_type="audience",
                scheduled_to="2026-08-01T15:00:00",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_send(self, async_client: AsyncCourier) -> None:
        broadcast = await async_client.broadcasts.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        )
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_send(self, async_client: AsyncCourier) -> None:
        response = await async_client.broadcasts.with_raw_response.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        broadcast = await response.parse()
        assert_matches_type(Broadcast, broadcast, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_send(self, async_client: AsyncCourier) -> None:
        async with async_client.broadcasts.with_streaming_response.send(
            broadcast_id="broadcastId",
            recipient_id="cool-customers",
            recipient_type="list",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            broadcast = await response.parse()
            assert_matches_type(Broadcast, broadcast, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_send(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `broadcast_id` but received ''"):
            await async_client.broadcasts.with_raw_response.send(
                broadcast_id="",
                recipient_id="cool-customers",
                recipient_type="list",
            )
