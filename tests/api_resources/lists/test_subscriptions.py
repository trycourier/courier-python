# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types.lists import (
    SubscriptionListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubscriptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.list(
            list_id="list_id",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.list(
            list_id="list_id",
            cursor="cursor",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.lists.subscriptions.with_raw_response.list(
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.lists.subscriptions.with_streaming_response.list(
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscriptions.with_raw_response.list(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add(self, client: Courier) -> None:
        response = client.lists.subscriptions.with_raw_response.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add(self, client: Courier) -> None:
        with client.lists.subscriptions.with_streaming_response.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_add(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscriptions.with_raw_response.add(
                list_id="",
                recipients=[{"recipient_id": "recipientId"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_subscribe(self, client: Courier) -> None:
        response = client.lists.subscriptions.with_raw_response.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_subscribe(self, client: Courier) -> None:
        with client.lists.subscriptions.with_streaming_response.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_subscribe(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscriptions.with_raw_response.subscribe(
                list_id="",
                recipients=[{"recipient_id": "recipientId"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe_user(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_subscribe_user_with_all_params(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.subscribe_user(
            user_id="user_id",
            list_id="list_id",
            preferences={
                "categories": {
                    "foo": {
                        "status": "OPTED_IN",
                        "channel_preferences": [{"channel": "direct_message"}],
                        "rules": [
                            {
                                "until": "until",
                                "start": "start",
                            }
                        ],
                    }
                },
                "notifications": {
                    "foo": {
                        "status": "OPTED_IN",
                        "channel_preferences": [{"channel": "direct_message"}],
                        "rules": [
                            {
                                "until": "until",
                                "start": "start",
                            }
                        ],
                    }
                },
            },
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_subscribe_user(self, client: Courier) -> None:
        response = client.lists.subscriptions.with_raw_response.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_subscribe_user(self, client: Courier) -> None:
        with client.lists.subscriptions.with_streaming_response.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_subscribe_user(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscriptions.with_raw_response.subscribe_user(
                user_id="user_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.lists.subscriptions.with_raw_response.subscribe_user(
                user_id="",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_unsubscribe_user(self, client: Courier) -> None:
        subscription = client.lists.subscriptions.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_unsubscribe_user(self, client: Courier) -> None:
        response = client.lists.subscriptions.with_raw_response.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_unsubscribe_user(self, client: Courier) -> None:
        with client.lists.subscriptions.with_streaming_response.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_unsubscribe_user(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            client.lists.subscriptions.with_raw_response.unsubscribe_user(
                user_id="user_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            client.lists.subscriptions.with_raw_response.unsubscribe_user(
                user_id="",
                list_id="list_id",
            )


class TestAsyncSubscriptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.list(
            list_id="list_id",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.list(
            list_id="list_id",
            cursor="cursor",
        )
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.lists.subscriptions.with_raw_response.list(
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.lists.subscriptions.with_streaming_response.list(
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert_matches_type(SubscriptionListResponse, subscription, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.list(
                list_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add(self, async_client: AsyncCourier) -> None:
        response = await async_client.lists.subscriptions.with_raw_response.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add(self, async_client: AsyncCourier) -> None:
        async with async_client.lists.subscriptions.with_streaming_response.add(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_add(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.add(
                list_id="",
                recipients=[{"recipient_id": "recipientId"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_subscribe(self, async_client: AsyncCourier) -> None:
        response = await async_client.lists.subscriptions.with_raw_response.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe(self, async_client: AsyncCourier) -> None:
        async with async_client.lists.subscriptions.with_streaming_response.subscribe(
            list_id="list_id",
            recipients=[{"recipient_id": "recipientId"}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_subscribe(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.subscribe(
                list_id="",
                recipients=[{"recipient_id": "recipientId"}],
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe_user(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_subscribe_user_with_all_params(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.subscribe_user(
            user_id="user_id",
            list_id="list_id",
            preferences={
                "categories": {
                    "foo": {
                        "status": "OPTED_IN",
                        "channel_preferences": [{"channel": "direct_message"}],
                        "rules": [
                            {
                                "until": "until",
                                "start": "start",
                            }
                        ],
                    }
                },
                "notifications": {
                    "foo": {
                        "status": "OPTED_IN",
                        "channel_preferences": [{"channel": "direct_message"}],
                        "rules": [
                            {
                                "until": "until",
                                "start": "start",
                            }
                        ],
                    }
                },
            },
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_subscribe_user(self, async_client: AsyncCourier) -> None:
        response = await async_client.lists.subscriptions.with_raw_response.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_subscribe_user(self, async_client: AsyncCourier) -> None:
        async with async_client.lists.subscriptions.with_streaming_response.subscribe_user(
            user_id="user_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_subscribe_user(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.subscribe_user(
                user_id="user_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.subscribe_user(
                user_id="",
                list_id="list_id",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_unsubscribe_user(self, async_client: AsyncCourier) -> None:
        subscription = await async_client.lists.subscriptions.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        )
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_unsubscribe_user(self, async_client: AsyncCourier) -> None:
        response = await async_client.lists.subscriptions.with_raw_response.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        subscription = await response.parse()
        assert subscription is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_unsubscribe_user(self, async_client: AsyncCourier) -> None:
        async with async_client.lists.subscriptions.with_streaming_response.unsubscribe_user(
            user_id="user_id",
            list_id="list_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            subscription = await response.parse()
            assert subscription is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_unsubscribe_user(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `list_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.unsubscribe_user(
                user_id="user_id",
                list_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_id` but received ''"):
            await async_client.lists.subscriptions.with_raw_response.unsubscribe_user(
                user_id="",
                list_id="list_id",
            )
