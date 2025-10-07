# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from courier import Courier, AsyncCourier
from tests.utils import assert_matches_type
from courier.types import (
    Brand,
    BrandListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrands:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Courier) -> None:
        brand = client.brands.create(
            name="name",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Courier) -> None:
        brand = client.brands.create(
            name="name",
            id="id",
            settings={
                "colors": {
                    "primary": "primary",
                    "secondary": "secondary",
                },
                "email": {
                    "footer": {
                        "content": "content",
                        "inherit_default": True,
                    },
                    "head": {
                        "inherit_default": True,
                        "content": "content",
                    },
                    "header": {
                        "logo": {
                            "href": "href",
                            "image": "image",
                        },
                        "bar_color": "barColor",
                        "inherit_default": True,
                    },
                    "template_override": {
                        "enabled": True,
                        "background_color": "backgroundColor",
                        "blocks_background_color": "blocksBackgroundColor",
                        "footer": "footer",
                        "head": "head",
                        "header": "header",
                        "width": "width",
                        "mjml": {
                            "enabled": True,
                            "background_color": "backgroundColor",
                            "blocks_background_color": "blocksBackgroundColor",
                            "footer": "footer",
                            "head": "head",
                            "header": "header",
                            "width": "width",
                        },
                        "footer_background_color": "footerBackgroundColor",
                        "footer_full_width": True,
                    },
                },
                "inapp": {
                    "colors": {
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "icons": {
                        "bell": "bell",
                        "message": "message",
                    },
                    "widget_background": {
                        "bottom_color": "bottomColor",
                        "top_color": "topColor",
                    },
                    "border_radius": "borderRadius",
                    "disable_message_icon": True,
                    "font_family": "fontFamily",
                    "placement": "top",
                },
            },
            snippets={
                "items": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ]
            },
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Courier) -> None:
        response = client.brands.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Courier) -> None:
        with client.brands.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Courier) -> None:
        brand = client.brands.retrieve(
            "brand_id",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Courier) -> None:
        response = client.brands.with_raw_response.retrieve(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Courier) -> None:
        with client.brands.with_streaming_response.retrieve(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: Courier) -> None:
        brand = client.brands.update(
            brand_id="brand_id",
            name="name",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Courier) -> None:
        brand = client.brands.update(
            brand_id="brand_id",
            name="name",
            settings={
                "colors": {
                    "primary": "primary",
                    "secondary": "secondary",
                },
                "email": {
                    "footer": {
                        "content": "content",
                        "inherit_default": True,
                    },
                    "head": {
                        "inherit_default": True,
                        "content": "content",
                    },
                    "header": {
                        "logo": {
                            "href": "href",
                            "image": "image",
                        },
                        "bar_color": "barColor",
                        "inherit_default": True,
                    },
                    "template_override": {
                        "enabled": True,
                        "background_color": "backgroundColor",
                        "blocks_background_color": "blocksBackgroundColor",
                        "footer": "footer",
                        "head": "head",
                        "header": "header",
                        "width": "width",
                        "mjml": {
                            "enabled": True,
                            "background_color": "backgroundColor",
                            "blocks_background_color": "blocksBackgroundColor",
                            "footer": "footer",
                            "head": "head",
                            "header": "header",
                            "width": "width",
                        },
                        "footer_background_color": "footerBackgroundColor",
                        "footer_full_width": True,
                    },
                },
                "inapp": {
                    "colors": {
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "icons": {
                        "bell": "bell",
                        "message": "message",
                    },
                    "widget_background": {
                        "bottom_color": "bottomColor",
                        "top_color": "topColor",
                    },
                    "border_radius": "borderRadius",
                    "disable_message_icon": True,
                    "font_family": "fontFamily",
                    "placement": "top",
                },
            },
            snippets={
                "items": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ]
            },
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Courier) -> None:
        response = client.brands.with_raw_response.update(
            brand_id="brand_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Courier) -> None:
        with client.brands.with_streaming_response.update(
            brand_id="brand_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.update(
                brand_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Courier) -> None:
        brand = client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Courier) -> None:
        brand = client.brands.list(
            cursor="cursor",
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Courier) -> None:
        response = client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Courier) -> None:
        with client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: Courier) -> None:
        brand = client.brands.delete(
            "brand_id",
        )
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Courier) -> None:
        response = client.brands.with_raw_response.delete(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Courier) -> None:
        with client.brands.with_streaming_response.delete(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Courier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            client.brands.with_raw_response.delete(
                "",
            )


class TestAsyncBrands:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.create(
            name="name",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.create(
            name="name",
            id="id",
            settings={
                "colors": {
                    "primary": "primary",
                    "secondary": "secondary",
                },
                "email": {
                    "footer": {
                        "content": "content",
                        "inherit_default": True,
                    },
                    "head": {
                        "inherit_default": True,
                        "content": "content",
                    },
                    "header": {
                        "logo": {
                            "href": "href",
                            "image": "image",
                        },
                        "bar_color": "barColor",
                        "inherit_default": True,
                    },
                    "template_override": {
                        "enabled": True,
                        "background_color": "backgroundColor",
                        "blocks_background_color": "blocksBackgroundColor",
                        "footer": "footer",
                        "head": "head",
                        "header": "header",
                        "width": "width",
                        "mjml": {
                            "enabled": True,
                            "background_color": "backgroundColor",
                            "blocks_background_color": "blocksBackgroundColor",
                            "footer": "footer",
                            "head": "head",
                            "header": "header",
                            "width": "width",
                        },
                        "footer_background_color": "footerBackgroundColor",
                        "footer_full_width": True,
                    },
                },
                "inapp": {
                    "colors": {
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "icons": {
                        "bell": "bell",
                        "message": "message",
                    },
                    "widget_background": {
                        "bottom_color": "bottomColor",
                        "top_color": "topColor",
                    },
                    "border_radius": "borderRadius",
                    "disable_message_icon": True,
                    "font_family": "fontFamily",
                    "placement": "top",
                },
            },
            snippets={
                "items": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ]
            },
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCourier) -> None:
        response = await async_client.brands.with_raw_response.create(
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCourier) -> None:
        async with async_client.brands.with_streaming_response.create(
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.retrieve(
            "brand_id",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCourier) -> None:
        response = await async_client.brands.with_raw_response.retrieve(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCourier) -> None:
        async with async_client.brands.with_streaming_response.retrieve(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.update(
            brand_id="brand_id",
            name="name",
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.update(
            brand_id="brand_id",
            name="name",
            settings={
                "colors": {
                    "primary": "primary",
                    "secondary": "secondary",
                },
                "email": {
                    "footer": {
                        "content": "content",
                        "inherit_default": True,
                    },
                    "head": {
                        "inherit_default": True,
                        "content": "content",
                    },
                    "header": {
                        "logo": {
                            "href": "href",
                            "image": "image",
                        },
                        "bar_color": "barColor",
                        "inherit_default": True,
                    },
                    "template_override": {
                        "enabled": True,
                        "background_color": "backgroundColor",
                        "blocks_background_color": "blocksBackgroundColor",
                        "footer": "footer",
                        "head": "head",
                        "header": "header",
                        "width": "width",
                        "mjml": {
                            "enabled": True,
                            "background_color": "backgroundColor",
                            "blocks_background_color": "blocksBackgroundColor",
                            "footer": "footer",
                            "head": "head",
                            "header": "header",
                            "width": "width",
                        },
                        "footer_background_color": "footerBackgroundColor",
                        "footer_full_width": True,
                    },
                },
                "inapp": {
                    "colors": {
                        "primary": "primary",
                        "secondary": "secondary",
                    },
                    "icons": {
                        "bell": "bell",
                        "message": "message",
                    },
                    "widget_background": {
                        "bottom_color": "bottomColor",
                        "top_color": "topColor",
                    },
                    "border_radius": "borderRadius",
                    "disable_message_icon": True,
                    "font_family": "fontFamily",
                    "placement": "top",
                },
            },
            snippets={
                "items": [
                    {
                        "name": "name",
                        "value": "value",
                    }
                ]
            },
        )
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCourier) -> None:
        response = await async_client.brands.with_raw_response.update(
            brand_id="brand_id",
            name="name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(Brand, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCourier) -> None:
        async with async_client.brands.with_streaming_response.update(
            brand_id="brand_id",
            name="name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(Brand, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.update(
                brand_id="",
                name="name",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.list()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.list(
            cursor="cursor",
        )
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCourier) -> None:
        response = await async_client.brands.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandListResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCourier) -> None:
        async with async_client.brands.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandListResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCourier) -> None:
        brand = await async_client.brands.delete(
            "brand_id",
        )
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCourier) -> None:
        response = await async_client.brands.with_raw_response.delete(
            "brand_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert brand is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCourier) -> None:
        async with async_client.brands.with_streaming_response.delete(
            "brand_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert brand is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCourier) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `brand_id` but received ''"):
            await async_client.brands.with_raw_response.delete(
                "",
            )
