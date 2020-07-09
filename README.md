# `trycourier`

This Python Package helps you send notifications through [Courier](https://www.trycourier.com/), the smartest way to design &amp; deliver notifications. Design your notifications once using our drag &amp; drop editor, then deliver to any channel through one API. Email, mobile push, SMS, Slack &mdash; you name it!

## Installation

Install from PyPI using [pip](http://www.pip-installer.org/en/latest/):

```shell
$ pip install trycourier
```

Python 3.5 or later is required.

## Usage

### Using Token Auth

```python
from trycourier import Courier

client = Courier(auth_token="your-auth-token") #or set via COURIER_AUTH_TOKEN env var

resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={
        "email": "example@example.com",
        "phone_number": "555-867-5309"
    },
    data={
      "world": "Python!"
    }
)
print(resp['messageId'])
```

### Using Basic Auth

```python
from trycourier import Courier

client = Courier(username="your-username", password="your-password")

resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={
        "email": "example@example.com",
        "phone_number": "555-867-5309"
    },
    data={
      "world": "Python!"
    }
)
print(resp['messageId'])
```

### Timeouts

As of v1.4.0, the timeout is defaulted to 5 seconds. This is configurable using the `timeout` parameter when creating a client. You can specify the time in seconds using a `float` value for both Connect and Read or use a tuple to set them for each individual one `(Connect, Read)`.

```python
client = Courier(auth_token="your-auth-token",
                 timeout=3.5)

client = Courier(auth_token="your-auth-token",
                 timeout=(3.2, 3.3))
```

## Advanced Usage

```python
from trycourier import Courier

client = Courier(auth_token="your-auth-token")

"""
Example: send a message
"""
resp = client.send(
    event="your-event-id",
    recipient="your-recipient-id",
    profile={}, # optional
    brand="your-brand-id", # optional
    data={}, # optional
    preferences={}, # optional
    override={} # optional
)
print(resp['messageId'])

"""
Example: replace or create a recipient's profile
"""
resp = client.replace_profile(
  recipient_id,
  {
    "email": "example@example.com"
  }
)
print(resp['status'])

"""
Example: merge or create a recipient's profile
"""
resp = client.merge_profile(
  recipient_id,
  {
    "phone_number": "+15555555555"
  }
)
print(resp['status'])

"""
Example: get a recipient's profile
"""
resp = client.get_profile(recipient_id)
print(resp)

"""
Example: fetch the statuses of messages you've previously sent.
"""
resp = client.get_messages(
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
  recipient=recipient_id, # optional
)
print(resp)

"""
Example: fetch the status of a message you've previously sent
"""
resp = client.get_message(message_id)
print(resp)

"""
Example: fetch the list of events
"""
resp = client.get_events()
print(resp)

"""
Example: fetch a specific event by event ID
"""
resp = client.get_event(event_id)
print(resp)

"""
Example: create or replace an event
"""
resp = client.replace_event(
  event_id,
  notification_id="GRPVB5P0BHMEZSNY6TP2X7TQHEBF",
  type="notificaton" ## optional, defaults to notification
)
print(resp)

"""
Example: get all brands
"""
resp = client.get_brands(
  cursor="MTU4OTQ5NTI1ODY4NywxLTVlYmRjNWRhLTEwODZlYWFjMWRmMjEwMTNjM2I0ZjVhMA", # optional
)
print(resp)

"""
Example: get a specific brand
"""
resp = client.get_brand(brand_id)
print(resp)

"""
Example: create a brand
"""
resp = client.create_brand({
  name="My Brand",
  settings={
    "color": {
      "primary": "#0000FF",
      "secondary": "#FF0000",
      "tertiary": "#00FF00"
    }
  }
})
print resp

"""
Example: replace a brand
"""
resp = client.replace_brand(
  brand_id,
  name="My New Brand",
  settings={
    "color": {
      "primary": "#FF0000",
      "secondary": "#00FF00",
      "tertiary": "#0000FF"
    }
  }
)
print resp

"""
Example: delete a brand
"""
client.delete_brand(brand_id)

```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/trycourier/courier-python. See [CONTRIBUTING.md](CONTRIBUTING.md) for more info.

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
