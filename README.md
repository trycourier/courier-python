[![Courier: Your Complete Communication Stack](https://marketing-assets-public.s3.us-west-1.amazonaws.com/github_nodejs.png)](https://courier.com)

[![pypi](https://img.shields.io/pypi/v/trycourier.svg)](https://pypi.python.org/pypi/trycourier)
[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-SDK%20generated%20by%20Fern-brightgreen)](https://buildwithfern.com/?utm_source=trycourier/courier-node/readme)

This is the official Python package for sending notifications with the [Courier](https://courier.com) REST API.

## Installation

Install from PyPI

```shell
pip install trycourier
# or 
poetry add trycourier
```

Python 3.7 or later is required.

## Usage
Use the `Courier` class to access all of our endpoints.

```python
import os
import courier

from courier.client import Courier

client = Courier(
  authorization_token="YOUR_TOKENY" # Defaults to COURIER_AUTH_TOKEN
)

response = client.send(
  message=courier.ContentMessage(
    to=courier.UserRecipient(
      email="marty_mcfly@email.com",
      data={
        name: "Marty",
      }
    ),
    content=courier.ElementalContentSugar(
      title="Back to the Future",
      body="Oh my {{name}}, we need 1.21 Gigawatts!",
    ),
    routing=courier.Routing(
      method=courier.RoutingMethod.ALL,
      channels=["email"]
    )
  )
)

print(response)
```

## Async Client
The SDK also exports an asynchronous client, `AsyncCourier`. 

```python
import os
import courier
import asyncio

from courier.client import AsyncCourier

client = AsyncCourier(
  authorization_token="YOUR_TOKEN" # Defaults to COURIER_AUTH_TOKEN
)

async def main() -> None: 
  response = await client.send(
    message=courier.ContentMessage(
      to=courier.UserRecipient(
        email="marty_mcfly@email.com",
        data={
          name: "Marty",
        }
      ),
      content=courier.ElementalContentSugar(
        title="Back to the Future",
        body="Oh my {{name}}, we need 1.21 Gigawatts!",
      ),
      routing=courier.Routing(
        method=courier.RoutingMethod.ALL,
        channels=["email"]
      )
    )
  )

asyncio.run(main())
```

## Timeouts
By default, the client is configured to have a timeout of 60 seconds. 
You can customize this value at client instantiation. 

```python
from courier.client import Courier

client = Courier(
  authorization_token="YOUR_TOKEN",
  timeout=30
)
```

## Handling Exceptions
All exceptions thrown by the SDK will sublcass [courier.ApiError](./src/courier/core/api_error.py). 

```python
import courier

from courier.core import ApiError

try:
  courier.send(...)
except APIError as e:  
  # handle any api related error
```

## Idempotency Keys

For `POST` methods, you can supply an `idempotencyKey` in the config parameter to 
ensure the idempotency of the API Call. We recommend that you use a `V4 UUID` for the key. 
Keys are eligible to be removed from the system after they're at least 24 hours old, 
and a new request is generated if a key is reused after the original has been removed. 
For more info, see [Idempotent Requests](https://docs.courier.com/reference/idempotent-requests) 
in the Courier documentation.

```python
import courier

courier.send(
  message={...}, 
  idempotency_key"YOUR_KEY", 
  idempotency_expiration="YOUR_EXPIRATION")
```

## Additional Usage Examples

### Send Template Message

```python
import courier

from courier import Courier

client = Courier(
  authorization_token="YOUR_TOKEN")

response = client.send(
    message=courier.TemplateMessage(
      template="my-template",
      to=courier.UserRecipient(email="foo@bar.com")
    )
)
print(response.message_id)
```

### UTM Metadata with Message

```python
import courier

from courier import Courier

client = Courier(
  authorization_token="YOUR_TOKEN")

response = client.send(
    message=courier.ContentMessage(
      content=courier.ElementalContent(
        version='2020-01-01',
        elements=[
          courier.ElementalNode_Action(
            content="ELEMENTAL",
            href="courier.com",
            style="button",
            align="center"
          )
        ]
      ),
      to=courier.UserRecipient(email="foo@bar.com"),
      routing=courier.Routing(
        method=courier.RoutingMethod.SINGLE,
        channels=["email"]
      ),
      metadata=courier.MessageMetadata(
        utm=courier.Utm(source="python")
      )
    )
)
print(response.request_id)
```

## Advanced

### Overriding HTTP Client
You can override the httpx client to customize it for your use case. Some common usecases 
include support for proxies and transports.

```python 
import httpx
from courier.client import Courier

client = Courier(
    http_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically. Additions made directly to this library would have to be moved over to our generation code, otherwise they would be overwritten upon the next generated release. Feel free to open a PR as a proof of concept, but know that we will not be able to merge it as-is. We suggest opening an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!

## License

[MIT License](http://www.opensource.org/licenses/mit-license.php)

## Author

[Courier](https://github.com/trycourier) ([support@courier.com](mailto:support@courier.com))
