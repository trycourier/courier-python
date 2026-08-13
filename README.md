# Courier Python SDK

The Courier Python SDK provides typed access to the Courier REST API from Python applications. Use it to send notifications, manage user profiles, check message status, issue JWT tokens for client-side SDKs, and more.

## Installation

```bash
pip install trycourier
```

Requires Python 3.8+.

## Quick Start

```python
import os
from courier import Courier

client = Courier(
    api_key=os.environ.get("COURIER_API_KEY"),  # the default, can be omitted
)

response = client.send.message(
    message={
        "to": {"user_id": "your_user_id"},
        "template": "your_template_id",
        "data": {"foo": "bar"},
    },
)
print(response.request_id)
```

The client reads `COURIER_API_KEY` from your environment automatically.

An async client is also available as `AsyncCourier`, with the same methods.

## Documentation

Full documentation: **[courier.com/docs/sdk-libraries/python](https://www.courier.com/docs/sdk-libraries/python/)**

- [Quickstart](https://www.courier.com/docs/getting-started/quickstart/)
- [Send API](https://www.courier.com/docs/platform/sending/send-message/)
- [API Reference](https://www.courier.com/docs/reference/get-started/)
