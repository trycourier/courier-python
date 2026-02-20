<!-- AUTO-GENERATED-OVERVIEW:START — Do not edit this section. It is synced from mintlify-docs. -->
# Courier Python SDK

The Courier Python SDK provides typed access to the Courier REST API from any Python 3.9+ application. It includes synchronous and asynchronous clients, Pydantic response models, TypedDict request params, and automatic retries.

## Installation

```bash
pip install trycourier
```

Also available via `poetry add trycourier` and `pipenv install trycourier`.

## Quick Start

```python
from courier import Courier

client = Courier()

response = client.send.message(
    message={
        "to": {"email": "you@example.com"},
        "content": {
            "title": "Hello from Courier!",
            "body": "Your first notification, sent with the Python SDK.",
        },
    },
)

print(response.request_id)
```

The client reads `COURIER_API_KEY` from your environment automatically. You can also pass it explicitly: `Courier(api_key='your-key')`.

### Async usage

Import `AsyncCourier` instead of `Courier` and use `await`:

```python
import asyncio
from courier import AsyncCourier

client = AsyncCourier()

async def main():
    response = await client.send.message(
        message={
            "to": {"email": "you@example.com"},
            "content": {
                "title": "Hello from Courier!",
                "body": "Sent from the async Python client.",
            },
        },
    )
    print(response.request_id)

asyncio.run(main())
```

## Common Operations

```python
# Check message delivery status
message = client.messages.retrieve("message-id")
print(message.status)

# Create or update a user profile
client.profiles.create("user_123", profile={
    "email": "jane@example.com",
    "name": "Jane Doe",
})

# Issue a JWT for client-side SDK auth
result = client.auth.issue_token(
    scope="user_id:user_123 inbox:read:messages inbox:write:events",
    expires_in="2 days",
)
```

## Documentation

Full documentation: **[courier.com/docs/sdk-libraries/python](https://www.courier.com/docs/sdk-libraries/python/)**

- [Quickstart](https://www.courier.com/docs/getting-started/quickstart/)
- [Send API](https://www.courier.com/docs/platform/sending/send-message/)
- [API Reference](https://www.courier.com/docs/reference/get-started/)
<!-- AUTO-GENERATED-OVERVIEW:END -->
