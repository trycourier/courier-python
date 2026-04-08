# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    RoutingStrategyGetResponse,
    RoutingStrategyListResponse,
    RoutingStrategyMutationResponse,
    AssociatedNotificationListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutingStrategies:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
            channels={
                "email": {
                    "brand_id": "brand_id",
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {"foo": "bar"},
                    "providers": ["sendgrid", "ses"],
                    "routing_method": "all",
                    "timeouts": {
                        "channel": 0,
                        "provider": 0,
                    },
                }
            },
            description="Routes email through sendgrid with SES failover",
            providers={
                "sendgrid": {
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {},
                    "timeouts": 0,
                }
            },
            tags=["production", "email"],
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.retrieve(
            "id",
        )
        assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_strategies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.list()
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_archive(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.archive(
            "id",
        )
        assert routing_strategy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_archive(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert routing_strategy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_archive(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert routing_strategy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_archive(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_strategies.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_notifications(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.list_notifications(
            id="id",
        )
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_notifications_with_all_params(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.list_notifications(
            id="id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_notifications(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.list_notifications(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_notifications(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.list_notifications(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_notifications(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_strategies.with_raw_response.list_notifications(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_replace_with_all_params(self, client: Courier) -> None:
        routing_strategy = client.routing_strategies.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
            channels={
                "email": {
                    "brand_id": "brand_id",
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {"foo": "bar"},
                    "providers": ["ses", "sendgrid"],
                    "routing_method": "all",
                    "timeouts": {
                        "channel": 0,
                        "provider": 0,
                    },
                }
            },
            description="Updated routing with SES primary",
            providers={
                "ses": {
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {},
                    "timeouts": 0,
                }
            },
            tags=["production", "email", "v2"],
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_replace(self, client: Courier) -> None:
        response = client.routing_strategies.with_raw_response.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = response.parse()
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_replace(self, client: Courier) -> None:
        with client.routing_strategies.with_streaming_response.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = response.parse()
            assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_replace(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.routing_strategies.with_raw_response.replace(
                id="",
                name="Email via SendGrid v2",
                routing={
                    "channels": ["email"],
                    "method": "single",
                },
            )


class TestAsyncRoutingStrategies:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
            channels={
                "email": {
                    "brand_id": "brand_id",
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {"foo": "bar"},
                    "providers": ["sendgrid", "ses"],
                    "routing_method": "all",
                    "timeouts": {
                        "channel": 0,
                        "provider": 0,
                    },
                }
            },
            description="Routes email through sendgrid with SES failover",
            providers={
                "sendgrid": {
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {},
                    "timeouts": 0,
                }
            },
            tags=["production", "email"],
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.create(
            name="Email via SendGrid",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.retrieve(
            "id",
        )
        assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert_matches_type(RoutingStrategyGetResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_strategies.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.list()
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.list(
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert_matches_type(RoutingStrategyListResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_archive(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.archive(
            "id",
        )
        assert routing_strategy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_archive(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.archive(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert routing_strategy is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_archive(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.archive(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert routing_strategy is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_archive(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_strategies.with_raw_response.archive(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_notifications(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.list_notifications(
            id="id",
        )
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_notifications_with_all_params(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.list_notifications(
            id="id",
            cursor="cursor",
            limit=1,
        )
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_notifications(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.list_notifications(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_notifications(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.list_notifications(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert_matches_type(AssociatedNotificationListResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_notifications(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_strategies.with_raw_response.list_notifications(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_replace_with_all_params(self, async_client: AsyncCourier) -> None:
        routing_strategy = await async_client.routing_strategies.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
            channels={
                "email": {
                    "brand_id": "brand_id",
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {"foo": "bar"},
                    "providers": ["ses", "sendgrid"],
                    "routing_method": "all",
                    "timeouts": {
                        "channel": 0,
                        "provider": 0,
                    },
                }
            },
            description="Updated routing with SES primary",
            providers={
                "ses": {
                    "if": "if",
                    "metadata": {
                        "utm": {
                            "campaign": "campaign",
                            "content": "content",
                            "medium": "medium",
                            "source": "source",
                            "term": "term",
                        }
                    },
                    "override": {},
                    "timeouts": 0,
                }
            },
            tags=["production", "email", "v2"],
        )
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_replace(self, async_client: AsyncCourier) -> None:
        response = await async_client.routing_strategies.with_raw_response.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routing_strategy = await response.parse()
        assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_replace(self, async_client: AsyncCourier) -> None:
        async with async_client.routing_strategies.with_streaming_response.replace(
            id="id",
            name="Email via SendGrid v2",
            routing={
                "channels": ["email"],
                "method": "single",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routing_strategy = await response.parse()
            assert_matches_type(RoutingStrategyMutationResponse, routing_strategy, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_replace(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.routing_strategies.with_raw_response.replace(
                id="",
                name="Email via SendGrid v2",
                routing={
                    "channels": ["email"],
                    "method": "single",
                },
            )
