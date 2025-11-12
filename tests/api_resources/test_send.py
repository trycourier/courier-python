# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import SendMessageResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSend:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_message(self, client: Courier) -> None:
        send = client.send.message(
            message={},
        )
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_message_with_all_params(self, client: Courier) -> None:
        send = client.send.message(
            message={
                "brand_id": "brand_id",
                "channels": {
                    "foo": {
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
                        "providers": ["string"],
                        "routing_method": "all",
                        "timeouts": {
                            "channel": 0,
                            "provider": 0,
                        },
                    }
                },
                "content": {
                    "body": "body",
                    "title": "title",
                },
                "context": {"tenant_id": "tenant_id"},
                "data": {"foo": "bar"},
                "delay": {
                    "duration": 0,
                    "until": "until",
                },
                "expiry": {
                    "expires_in": "string",
                    "expires_at": "expires_at",
                },
                "metadata": {
                    "event": "event",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                    "utm": {
                        "campaign": "campaign",
                        "content": "content",
                        "medium": "medium",
                        "source": "source",
                        "term": "term",
                    },
                },
                "preferences": {"subscription_topic_id": "subscription_topic_id"},
                "providers": {
                    "foo": {
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
                        "timeouts": 0,
                    }
                },
                "routing": {
                    "channels": ["string"],
                    "method": "all",
                },
                "template": "template_id",
                "timeout": {
                    "channel": {"foo": 0},
                    "criteria": "no-escalation",
                    "escalation": 0,
                    "message": 0,
                    "provider": {"foo": 0},
                },
                "to": {
                    "account_id": "account_id",
                    "context": {"tenant_id": "tenant_id"},
                    "data": {"foo": "bar"},
                    "email": "email",
                    "list_id": "list_id",
                    "locale": "locale",
                    "phone_number": "phone_number",
                    "preferences": {
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
                                "source": "subscription",
                            }
                        },
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
                                "source": "subscription",
                            }
                        },
                        "template_id": "templateId",
                    },
                    "tenant_id": "tenant_id",
                    "user_id": "example_user",
                },
            },
        )
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_message(self, client: Courier) -> None:
        response = client.send.with_raw_response.message(
            message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = response.parse()
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_message(self, client: Courier) -> None:
        with client.send.with_streaming_response.message(
            message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = response.parse()
            assert_matches_type(SendMessageResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSend:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_message(self, async_client: AsyncCourier) -> None:
        send = await async_client.send.message(
            message={},
        )
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_message_with_all_params(self, async_client: AsyncCourier) -> None:
        send = await async_client.send.message(
            message={
                "brand_id": "brand_id",
                "channels": {
                    "foo": {
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
                        "providers": ["string"],
                        "routing_method": "all",
                        "timeouts": {
                            "channel": 0,
                            "provider": 0,
                        },
                    }
                },
                "content": {
                    "body": "body",
                    "title": "title",
                },
                "context": {"tenant_id": "tenant_id"},
                "data": {"foo": "bar"},
                "delay": {
                    "duration": 0,
                    "until": "until",
                },
                "expiry": {
                    "expires_in": "string",
                    "expires_at": "expires_at",
                },
                "metadata": {
                    "event": "event",
                    "tags": ["string"],
                    "trace_id": "trace_id",
                    "utm": {
                        "campaign": "campaign",
                        "content": "content",
                        "medium": "medium",
                        "source": "source",
                        "term": "term",
                    },
                },
                "preferences": {"subscription_topic_id": "subscription_topic_id"},
                "providers": {
                    "foo": {
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
                        "timeouts": 0,
                    }
                },
                "routing": {
                    "channels": ["string"],
                    "method": "all",
                },
                "template": "template_id",
                "timeout": {
                    "channel": {"foo": 0},
                    "criteria": "no-escalation",
                    "escalation": 0,
                    "message": 0,
                    "provider": {"foo": 0},
                },
                "to": {
                    "account_id": "account_id",
                    "context": {"tenant_id": "tenant_id"},
                    "data": {"foo": "bar"},
                    "email": "email",
                    "list_id": "list_id",
                    "locale": "locale",
                    "phone_number": "phone_number",
                    "preferences": {
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
                                "source": "subscription",
                            }
                        },
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
                                "source": "subscription",
                            }
                        },
                        "template_id": "templateId",
                    },
                    "tenant_id": "tenant_id",
                    "user_id": "example_user",
                },
            },
        )
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_message(self, async_client: AsyncCourier) -> None:
        response = await async_client.send.with_raw_response.message(
            message={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        send = await response.parse()
        assert_matches_type(SendMessageResponse, send, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_message(self, async_client: AsyncCourier) -> None:
        async with async_client.send.with_streaming_response.message(
            message={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            send = await response.parse()
            assert_matches_type(SendMessageResponse, send, path=["response"])

        assert cast(Any, response.is_closed) is True
